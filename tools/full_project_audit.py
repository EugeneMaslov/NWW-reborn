"""Audit NWW's effective HOI4 filesystem. No game files are modified.

python tools/full_project_audit.py --game "/path/to/Hearts of Iron IV"
Use --baseline docs/audit/baseline.json --verify to include regression checks.
The Markdown report is Russian; the JSON retains every individual diagnostic.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime
from functools import lru_cache
import csv
import io
import json
import os
from pathlib import Path
import re
import struct
import subprocess
import sys
import zipfile
from zoneinfo import ZoneInfo

from PIL import Image
from hoi4_script import parse as legacy_parse, engine_script_errors, scalar

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    'syntax': 'Синтаксис и разбор', 'gfx': 'Графика и ресурсы',
    'localisation': 'Локализация и кодировка', 'map': 'Карта и регионы',
    'characters': 'Персонажи и советники', 'focus': 'Национальные фокусы',
    'decisions': 'Решения, миссии и переменные', 'tooling': 'Инструменты и воспроизводимость',
}

VARIABLE_REVIEW = {
    'MKN_raids_done': (
        'Счётчик успешных рейдов',
        'Стартует с 0; растёт на 1. Перед третьим рейдом значение 2 включает постоянный MKN_ukr_angered. Верхнего предела нет; это счётчик, а не шкала или индекс.',
        'Без изменений; искусственный clamp не добавлялся.'),
    'mkn_consecutive_border_wars': (
        'Счётчик недавних пограничных боёв',
        'Инициализация и сброс в 0; флаг недавнего боя действует 180 дней. При значении >= 3 эскалация становится 5. Это порог реакции, а не жёсткий предел счётчика.',
        'Без изменений; используются порог и сброс.'),
    'mkn_ukr_attacking_state': (
        'ID штата атакующей стороны',
        'Присваивается из выбранной области штата; перед отменой боя проверяется has_variable. Числовой clamp мог бы подменить ID другим штатом.',
        'Без изменений; clamp для ID не нужен.'),
    'mkn_ukr_defending_state': (
        'ID штата обороняющейся стороны',
        'Присваивается из целевого штата; перед отменой боя проверяется has_variable. Это ссылка на штат, а не уровень механики.',
        'Без изменений; clamp для ID не нужен.'),
    'mkn_ukr_escalation_level': (
        'Уровень эскалации',
        'Начальное значение 1. Уже существующий clamp поддерживает диапазон 1–5; прямые присваивания используют значения этого диапазона.',
        'Без изменений; существующее ограничение проверено.'),
    'num_owned_states': (
        'Число принадлежащих стране штатов',
        'Вычисляемая переменная движка. Её нельзя и не требуется инициализировать или ограничивать через set_variable/clamp_variable.',
        'Без изменений; проверена штатная переменная.'),
}


@dataclass
class Node:
    key: str | None
    value: str | list[Node]
    line: int
    op: str = '='


class ScriptError(ValueError):
    def __init__(self, line, message):
        super().__init__(message)
        self.line = line


LEX = re.compile(r'\s+|#[^\n]*|"(?:\\.|[^"\\])*"|[{}]|[=<>!]=?|[^\s{}=<>!#"]+')


def parse(text):
    """Consume every character; ignore braces in comments/strings, retain lines."""
    text = text.lstrip('\ufeff')
    tokens, end, line = [], 0, 1
    for match in LEX.finditer(text):
        if match.start() != end:
            raise ScriptError(line, 'Незакрытая строка или недопустимый символ')
        token = match.group()
        if not token.isspace() and not token.startswith('#'):
            tokens.append((token, line))
        line += token.count('\n')
        end = match.end()
    if end != len(text):
        raise ScriptError(line, 'Незакрытая строка')
    pos = 0

    def block(nested=False):
        nonlocal pos
        nodes = []
        while pos < len(tokens):
            key, number = tokens[pos]
            pos += 1
            if key == '}':
                if not nested:
                    raise ScriptError(number, 'Лишняя закрывающая скобка')
                return nodes
            if key == '{':
                nodes.append(Node(None, block(True), number))
            elif key in ('=', '<', '>', '<=', '>=', '!=', '==', '!'):
                raise ScriptError(number, f'Оператор {key} без ключа')
            elif pos < len(tokens) and tokens[pos][0] in ('=', '<', '>', '<=', '>=', '!=', '=='):
                op = tokens[pos][0]
                pos += 1
                if pos == len(tokens) or tokens[pos][0] in ('}', '=', '<', '>'):
                    raise ScriptError(number, f'Нет значения после {key} {op}')
                value = tokens[pos][0]
                pos += 1
                nodes.append(Node(scalar(key), block(True) if value == '{' else scalar(value), number, op))
            else:
                if not nested:
                    raise ScriptError(number, f'Лишний токен верхнего уровня: {key}')
                nodes.append(Node(None, scalar(key), number, ''))
        if nested:
            raise ScriptError(line, 'Незакрытый блок')
        return nodes

    return block()


def children(node):
    return node if isinstance(node, list) else []


def items(node, key):
    return [n for n in children(node) if n.key == key]


def get(node, key, default=None):
    return next((n.value for n in children(node) if n.key == key), default)


def walk(node):
    for n in children(node):
        yield n
        yield from walk(n.value)


@dataclass
class Issue:
    category: str
    severity: str
    code: str
    file: str
    line: int
    message: str


class VFS:
    """Base + unpacked/ZIP DLC + mod overrides, including descriptor replace_path."""
    def __init__(self, game, root):
        self.game, self.root = game, root
        self.files, self.archives = {}, {}
        self.paths = [game, *sorted((game / 'integrated_dlc').glob('*')),
                      *sorted((game / 'dlc').glob('*'))]
        for base in self.paths:
            if not base.is_dir():
                continue
            for folder in ('common', 'events', 'history', 'interface', 'localisation', 'gfx', 'map', 'portraits'):
                for path in (base / folder).rglob('*'):
                    if path.is_file():
                        self.files[path.relative_to(base).as_posix()] = path
            for path in sorted(base.glob('*.zip')):
                archive = zipfile.ZipFile(path)
                self.archives[path] = archive
                for name in archive.namelist():
                    if not name.endswith('/'):
                        self.files[name] = (path, name)
        descriptor = next(iter(root.glob('*.mod')), None)
        if descriptor:
            for folder in re.findall(r'replace_path\s*=\s*"([^"]+)"', descriptor.read_text(encoding='utf-8-sig')):
                self.files = {k: v for k, v in self.files.items() if not k.startswith(folder.rstrip('/') + '/')}
        for folder in ('common', 'events', 'history', 'interface', 'localisation', 'gfx', 'map', 'portraits'):
            for path in (root / folder).rglob('*'):
                if path.is_file():
                    self.files[path.relative_to(root).as_posix()] = path
        self.folded = {p.casefold(): p for p in self.files}

    def read(self, name):
        source = self.files[name]
        return self.archives[source[0]].read(source[1]) if isinstance(source, tuple) else source.read_bytes()

    @lru_cache(maxsize=None)
    def doc(self, name):
        return parse(self.read(name).decode('utf-8-sig'))

    def names(self, folder, suffix='.txt'):
        return sorted(p for p in self.files if p.startswith(folder.rstrip('/') + '/') and p.endswith(suffix))

    def mod(self, name):
        return self.files.get(name) == self.root / name


class Audit:
    def __init__(self, root, game):
        self.root, self.game = root, game
        self.vfs = VFS(game, root)
        self.issues, self.stats = [], Counter()
        self.scanned = set()
        self.loc = {lang: {} for lang in ('russian', 'english')}
        self.required_loc = defaultdict(list)
        self.sprites = {}
        self.variable_inventory = {}

    def issue(self, category, code, path, line, message, severity='error'):
        self.issues.append(Issue(category, severity, code, path, line, message))

    def docs(self, folder, mod=False, suffix='.txt'):
        for name in self.vfs.names(folder, suffix):
            if mod and not self.vfs.mod(name):
                continue
            try:
                yield name, self.vfs.doc(name)
            except (UnicodeError, ScriptError) as exc:
                # Mod parse failures are reported once by syntax(); native parser
                # extensions are not silently used as a partial registry.
                if not self.vfs.mod(name):
                    # Some installed 1.19.3 DLC files have an unmatched outer
                    # wrapper. Recover only that wrapper IN MEMORY for registries.
                    text = self.vfs.read(name).decode('utf-8-sig')
                    tokens = [m.group() for m in LEX.finditer(text) if not m.group().startswith('#')]
                    balance = tokens.count('{') - tokens.count('}')
                    repaired = None
                    if isinstance(exc, ScriptError) and str(exc) == 'Незакрытый блок' and balance > 0:
                        repaired = text + '\n' + '}' * balance
                    elif isinstance(exc, ScriptError) and str(exc) == 'Лишняя закрывающая скобка' and balance == -1 and text.rstrip().endswith('}'):
                        repaired = text.rstrip()[:-1]
                    self.issue('tooling', 'native_parse', name, getattr(exc, 'line', 1),
                               f'Установленная игра: {exc}; ' + ('внешняя скобка восстановлена в памяти для чтения реестра, файл игры не изменён' if repaired else 'реестр неполон'), 'warning')
                    if repaired:
                        yield name, parse(repaired)

    def syntax(self):
        for name in sorted(self.vfs.files):
            if not self.vfs.mod(name) or not name.endswith(('.txt', '.gfx', '.gui')) or name.split('/')[0] not in ('common', 'events', 'history', 'interface', 'map'):
                continue
            # CSV-style map .txt files are checked by the map validator.
            if name.startswith('map/') and not name.startswith('map/strategicregions/'):
                continue
            self.scanned.add(name)
            self.stats['script_files'] += 1
            try:
                raw = self.vfs.read(name)
                if name.endswith(('.gfx', '.gui')) and raw.startswith(b'\xef\xbb\xbf'):
                    self.issue('syntax', 'interface_bom', name, 1, 'BOM становится частью первого токена интерфейсного скрипта; требуется UTF-8 без BOM')
                text = raw.decode('utf-8-sig')
                doc = self.vfs.doc(name)
                for n in walk(doc):
                    if isinstance(n.value, list) and any(c.key for c in n.value) and any(c.key is None and isinstance(c.value, str) for c in n.value):
                        self.issue('syntax', 'record_scalar', name, n.line, f'{n.key}: свободные токены внутри блока с именованными параметрами; проверить экранирование строк')
                    if isinstance(n.value, str) and re.fullmatch(r'-?\.\d+', n.value):
                        self.issue('syntax', 'decimal', name, n.line, f'{n.value}: требуется ведущий ноль')
                    if n.op not in ('=', '<', '>', ''):
                        self.issue('syntax', 'operator', name, n.line, f'Недопустимый оператор движка {n.op}')
                    if name.startswith('common/ai_strategy_plans/') and n.key == 'allowed':
                        for condition in walk(n.value):
                            if condition.key == 'has_focus_tree':
                                self.issue('syntax', 'ai_allowed_trigger', name, condition.line, 'has_focus_tree разрешён в enable, но отвергается статическим allowed плана ИИ')
                    if name.startswith('common/characters/') and n.key in ('on_add', 'on_remove'):
                        # Character callbacks start in character scope. Native
                        # SWE explicitly enters SWE before changing country ideas.
                        def callback(nodes):
                            for effect in children(nodes):
                                if effect.key in ('add_ideas', 'remove_ideas', 'add_timed_idea'):
                                    self.issue('characters', 'advisor_callback_scope', name, effect.line, f'{n.key}: {effect.key} требует явной области страны')
                                elif effect.key in ('if', 'else_if', 'else', 'hidden_effect'):
                                    callback(effect.value)
                        callback(n.value)
                for message in engine_script_errors(legacy_parse(text)):
                    # Operator diagnostics above already retain exact source lines.
                    if 'unsupported raw operator' not in message:
                        key = message.split(':')[0].split('/')[-1]
                        number = next((n.line for n in walk(doc) if n.key == key), 1)
                        self.issue('syntax', 'engine_syntax', name, number, message)
            except UnicodeError as exc:
                self.issue('syntax', 'encoding', name, 1, str(exc))
            except ScriptError as exc:
                self.issue('syntax', 'parse', name, exc.line, str(exc))

    def need_loc(self, key, path, line):
        if isinstance(key, str) and re.fullmatch(r'[\w.\-]+', key) and key not in ('yes', 'no'):
            self.required_loc[key].append((path, line))

    def localisation(self):
        pattern = re.compile(r'^([ \t]+)([^\s:#]+):\d*\s*"((?:\\.|[^"\\])*)"\s*(?:#.*)?$')
        native_pattern = re.compile(r'^([ \t]+)([^\s:#]+):\d*\s*"(.*)"\s*(?:#.*)?$')
        mod_seen = {lang: {} for lang in self.loc}
        names = self.vfs.names('localisation', '.yml')
        # Native first, ordinary mod second, explicit /replace/ last.
        names.sort(key=lambda p: (self.vfs.mod(p), '/replace/' in p, p))
        for path in names:
            lang = next((l for l in self.loc if path.endswith(f'_l_{l}.yml')), None)
            if lang is None:
                continue
            local = self.vfs.mod(path)
            if local:
                self.scanned.add(path)
                self.stats['localisation_files'] += 1
            raw = self.vfs.read(path)
            try:
                text = raw.decode('utf-8-sig')
            except UnicodeError as exc:
                if local:
                    self.issue('localisation', 'utf8', path, 1, str(exc))
                continue
            significant = [(i, l) for i, l in enumerate(text.splitlines(), 1) if l.strip() and not l.lstrip().startswith('#')]
            if local and (not significant or significant[0][1].strip() != f'l_{lang}:'):
                self.issue('localisation', 'header', path, significant[0][0] if significant else 1, f'Требуется l_{lang}:')
            if local and not raw.startswith(b'\xef\xbb\xbf'):
                self.issue('localisation', 'bom', path, 1, 'Отсутствует UTF-8 BOM')
            for number, line in significant:
                if line.strip() == f'l_{lang}:':
                    continue
                # Native localisation deliberately contains literal interior
                # quotes. Its loader uses the first/last quote on the line.
                match = (pattern if local else native_pattern).fullmatch(line)
                if not match:
                    if local:
                        self.issue('localisation', 'entry', path, number, 'Неверная запись: отступ, ключ, версия или кавычки')
                    continue
                indent, key, value = match.groups()
                self.loc[lang][key] = value
                if not local:
                    continue
                self.stats['localisation_entries'] += 1
                if '\t' in indent:
                    self.issue('localisation', 'indent', path, number, 'Использован табулятор в отступе')
                old = mod_seen[lang].get(key)
                if old and '/replace/' not in path:
                    self.issue('localisation', 'duplicate', path, number, f'{key}: повтор ключа из {old[0]}:{old[1]}' + (' с другим текстом' if old[2] != value else ''))
                mod_seen[lang][key] = (path, number, value)
                if key in {p + suffix for p in ('fascism', 'democratic', 'neutrality', 'communism') for suffix in ('', '_noun', '_desc')} and re.search(r'\[\w', value):
                    self.issue('localisation', 'static_ideology_callback', path, number, f'{key}: статическая подпись идеологии не вычисляет scripted localisation')
                active = False
                for token in re.findall(r'§(.)', value):
                    if token == '!':
                        active = False
                    else:
                        active = True
                if active:
                    self.issue('localisation', 'colour', path, number, f'{key}: незакрытый цветовой тег §')
                if len(re.findall(r'(?<!\\)\$', value)) % 2:
                    self.issue('localisation', 'substitution', path, number, f'{key}: непарный $')
                if value.count('[') != value.count(']'):
                    self.issue('localisation', 'brackets', path, number, f'{key}: непарные скобки форматтера')
                if re.search(r'\b(?:TODO|FIXME|PLACEHOLDER|lorem ipsum)\b|\?{3,}|�', value, re.I):
                    self.issue('localisation', 'placeholder', path, number, f'{key}: заглушка или повреждённый текст')

    def asset(self, value, path, number):
        if not isinstance(value, str) or value.startswith(('[', '$')):
            return
        value = value.replace('\\', '/')
        if value.startswith('GFX_'):
            if value not in self.sprites:
                self.issue('gfx', 'sprite_missing', path, number, value)
            else:
                self.stats['sprite_references'] += 1
                sprite_path, sprite_node = self.sprites[value]
                texture = next((n for n in children(sprite_node.value) if n.key and n.key.lower() == 'texturefile'), None)
                if texture and isinstance(texture.value, str):
                    self.asset(texture.value, sprite_path, texture.line)
            return
        if value.lower().endswith(('.dds', '.png', '.tga')):
            canonical = re.sub('/+', '/', value)
            if canonical != value:
                self.issue('gfx', 'texture_noncanonical', path, number, f'{value} → {canonical}', 'warning')
                value = canonical
            if value not in self.vfs.files:
                other = self.vfs.folded.get(value.casefold())
                self.issue('gfx', 'texture_case' if other else 'texture_missing', path, number, f'{value}' + (f' → {other}' if other else ''))
            else:
                self.stats['texture_references'] += 1

    def graphics(self):
        mod_sprites = {}
        for path, doc in self.docs('interface', suffix='.gfx'):
            for n in walk(doc):
                if n.key and n.key.lower() == 'spritetype':
                    token = get(n.value, 'name')
                    if token:
                        if self.vfs.mod(path) and token in mod_sprites:
                            self.issue('gfx', 'sprite_duplicate', path, n.line, f'{token}: повтор из {mod_sprites[token]}')
                        if self.vfs.mod(path):
                            mod_sprites[token] = path
                        # Prefer a custom sprite even if its filename sorts first.
                        if token not in self.sprites or self.vfs.mod(path):
                            self.sprites[token] = (path, n)
        self.stats['custom_sprites'] = len(mod_sprites)
        for path, doc in self.docs('interface', mod=True, suffix='.gfx'):
            for n in walk(doc):
                if n.key and n.key.lower() in ('texturefile', 'texture', 'effectfile'):
                    if n.key.lower() != 'effectfile':
                        self.asset(n.value, path, n.line)
        for path in sorted(self.vfs.files):
            if not self.vfs.mod(path) or not path.startswith('gfx/'):
                continue
            if path.lower().endswith(('.dds', '.tga', '.png')):
                self.scanned.add(path)
                self.stats['image_files'] += 1
                raw = self.vfs.read(path)
                try:
                    with Image.open(io.BytesIO(raw)) as image:
                        image.load()
                        w, h = image.size
                        if w < 1 or h < 1:
                            raise ValueError('Нулевая размерность')
                        if path.lower().endswith('.dds'):
                            self.stats['dds_files'] += 1
                            if len(raw) < 128 or raw[:4] != b'DDS ' or struct.unpack_from('<I', raw, 4)[0] != 124 or struct.unpack_from('<I', raw, 76)[0] != 32:
                                raise ValueError('Неверный DDS_HEADER или DDS_PIXELFORMAT')
                            if struct.unpack_from('<II', raw, 12) != (h, w):
                                raise ValueError('Размерность DDS не соответствует декодеру')
                            if (w & (w - 1)) or (h & (h - 1)):
                                self.stats['dds_non_pot_ui'] += 1
                                if '/models/' in path:
                                    self.issue('gfx', 'dds_non_pot_model', path, 1, f'{w}×{h}: проверить требования материала и mipmap', 'warning')
                except (OSError, ValueError, struct.error) as exc:
                    self.issue('gfx', 'image_header', path, 1, str(exc))
        # References in ALL mod script folders, including GUI and scripted effects.
        for path in sorted(self.scanned):
            if not path.endswith(('.txt', '.gfx', '.gui')):
                continue
            try:
                for n in walk(self.vfs.doc(path)):
                    if isinstance(n.value, str) and (n.value.startswith('GFX_') or n.value.lower().endswith(('.dds', '.tga', '.png'))):
                        self.asset(n.value, path, n.line)
            except (ScriptError, UnicodeError):
                pass

    def definitions(self):
        self.focuses, self.shared, self.trees = {}, {}, []
        for path, doc in self.docs('common/national_focus'):
            for tree in items(doc, 'focus_tree'):
                self.trees.append((path, tree.value))
            defs = items(doc, 'shared_focus') + [n for tree in items(doc, 'focus_tree') for n in items(tree.value, 'focus')]
            for n in defs:
                fid = get(n.value, 'id')
                if fid in self.focuses and (self.vfs.mod(path) or self.vfs.mod(self.focuses[fid][0])):
                    self.issue('focus', 'duplicate', path, n.line, f'{fid}: повтор из {self.focuses[fid][0]}')
                self.focuses[fid] = (path, n)
                if n.key == 'shared_focus':
                    self.shared[fid] = n
        self.character_ids, self.traits, self.category_ids = set(), set(), set()
        self.native_idea_ids = set()
        for base in self.vfs.paths:
            for p in (base / 'common/ideas').glob('*.txt'):
                try:
                    text = p.read_text(encoding='utf-8-sig')
                    try:
                        doc = parse(text)
                    except ScriptError as exc:
                        tokens = [m.group() for m in LEX.finditer(text) if not m.group().startswith('#')]
                        balance = tokens.count('{') - tokens.count('}')
                        if str(exc) != 'Незакрытый блок' or balance <= 0:
                            raise
                        doc = parse(text + '\n' + '}' * balance)
                        self.stats['native_reference_wrappers_restored'] += 1
                    self.native_idea_ids.update(n.key for g in children(get(doc, 'ideas', [])) for n in children(g.value) if isinstance(n.value, list))
                except (ScriptError, UnicodeError):
                    pass
        for path, doc in self.docs('common/characters'):
            self.character_ids.update(n.key for n in children(get(doc, 'characters', [])))
        for folder in ('common/country_leader', 'common/unit_leader'):
            for path, doc in self.docs(folder):
                self.traits.update(n.key for n in children(get(doc, 'leader_traits', [])))
        for path, doc in self.docs('common/scientist_traits'):
            self.traits.update(n.key for n in doc)
        for path, doc in self.docs('common/decisions/categories'):
            self.category_ids.update(n.key for n in doc)
        self.stats['effective_focuses'] = len(self.focuses)
        self.stats['effective_characters'] = len(self.character_ids)

    def focus(self):
        graph = {}
        for fid, (path, n) in self.focuses.items():
            refs = [c.value for g in items(n.value, 'prerequisite') for c in items(g.value, 'focus')]
            graph[fid] = refs
            if not self.vfs.mod(path):
                continue
            self.stats['custom_focuses'] += 1
            hidden = get(get(n.value, 'allow_branch', []), 'always') == 'no'
            if hidden:
                self.stats['hidden_compatibility_focuses'] += 1
            else:
                self.need_loc(get(n.value, 'text', fid), path, n.line)
                self.need_loc(get(n.value, 'desc', fid + '_desc'), path, n.line)
            for field in ('cost', 'x', 'y'):
                value = get(n.value, field)
                if value is None and field in ('x', 'y') and hidden:
                    self.stats['hidden_focus_default_coordinates'] += 1
                    continue
                valid = isinstance(value, str) and bool(re.fullmatch(r'-?\d+(?:\.\d+)?', value))
                if valid:
                    valid = float(value) > 0 if field == 'cost' else float(value).is_integer()
                if not valid:
                    self.issue('focus', 'grid_or_cost', path, n.line, f'{fid}: {field}={value}')
            for g in items(n.value, 'prerequisite') + items(n.value, 'mutually_exclusive'):
                for c in items(g.value, 'focus'):
                    if c.value not in self.focuses:
                        self.issue('focus', 'reference', path, c.line, f'{fid}: неизвестный {c.value}')
                    elif g.key == 'mutually_exclusive':
                        other = self.focuses[c.value][1]
                        reverse = [r.value for ex in items(other.value, 'mutually_exclusive') for r in items(ex.value, 'focus')]
                        if fid not in reverse:
                            self.issue('focus', 'exclusion', path, c.line, f'{fid} → {c.value}: отсутствует обратное исключение')
            relative = get(n.value, 'relative_position_id')
            if relative and relative not in self.focuses:
                self.issue('focus', 'position', path, n.line, f'{fid}: неизвестный relative_position_id {relative}')
        colours = {}
        def visit(fid, trail):
            if colours.get(fid) == 1:
                path, n = self.focuses[fid]
                if any(self.vfs.mod(self.focuses[f][0]) for f in trail):
                    self.issue('focus', 'cycle', path, n.line, ' → '.join(trail + [fid]))
                return
            if colours.get(fid) == 2:
                return
            colours[fid] = 1
            for ref in graph.get(fid, []):
                if ref in graph:
                    visit(ref, trail + [fid])
            colours[fid] = 2
        for fid in graph:
            visit(fid, [])
        for path, tree in self.trees:
            if not self.vfs.mod(path):
                continue
            direct = {get(n.value, 'id') for n in items(tree, 'focus')}
            imported = {n.value for n in items(tree, 'shared_focus') if isinstance(n.value, str)}
            for token in imported - self.shared.keys():
                self.issue('focus', 'shared_missing', path, 1, str(token))
            while True:
                new = {fid for fid in self.shared if set(graph.get(fid, [])) & imported} - imported
                if not new:
                    break
                imported.update(new)
            present = direct | imported
            for fid in present & self.focuses.keys():
                for parent in graph.get(fid, []):
                    if parent not in present:
                        p, n = self.focuses[fid]
                        self.issue('focus', 'tree_reference', p, n.line, f'{fid}: {parent} отсутствует в дереве {get(tree, "id")}')

    def content(self):
        slots = set()
        for path, doc in self.docs('common/characters'):
            if not self.vfs.mod(path):
                slots.update(get(n.value, 'slot') for n in walk(doc) if n.key == 'advisor')
        for path, doc in self.docs('common/characters', mod=True):
            for character in children(get(doc, 'characters', [])):
                self.stats['custom_characters'] += 1
                self.need_loc(get(character.value, 'name', character.key), path, character.line)
                for n in walk(character.value):
                    if n.key == 'advisor':
                        slot = get(n.value, 'slot')
                        if slot not in slots:
                            self.issue('characters', 'slot', path, n.line, f'{character.key}: неизвестный слот {slot}')
                        self.need_loc(get(n.value, 'idea_token'), path, n.line)
                    if n.key == 'traits':
                        for trait in children(n.value):
                            if trait.key is None and trait.value not in self.traits:
                                self.issue('characters', 'trait', path, trait.line, f'{character.key}: неизвестный трейт {trait.value}')
        for path, doc in self.docs('history/countries', mod=True):
            for n in walk(doc):
                if n.key == 'recruit_character':
                    self.stats['recruit_references'] += 1
                    if n.value not in self.character_ids:
                        self.issue('characters', 'recruit', path, n.line, f'Не определён {n.value}')
                if n.key in ('create_country_leader', 'create_field_marshal', 'create_corps_commander', 'create_navy_leader'):
                    self.need_loc(get(n.value, 'name'), path, n.line)
        for folder in ('history/units', 'common/scripted_effects'):
            for path, doc in self.docs(folder, mod=True):
                for n in walk(doc):
                    if n.key == 'division_template' and isinstance(n.value, list):
                        token = get(n.value, 'name')
                        if isinstance(token, str) and re.fullmatch(r'MKN_\w+', token):
                            self.need_loc(token, path, n.line)
        for path, doc in self.docs('common/ideas', mod=True):
            for group in children(get(doc, 'ideas', [])):
                for idea in children(group.value):
                    if not isinstance(idea.value, list):
                        continue
                    self.need_loc(get(idea.value, 'name', idea.key), path, idea.line)
                    # Native ideas often deliberately omit optional descriptions.
                    # Custom, visible spirits are expected to supply explanatory text.
                    if group.key == 'country' and idea.key not in self.native_idea_ids:
                        self.need_loc(idea.key + '_desc', path, idea.line)
                    picture = get(idea.value, 'picture')
                    if picture:
                        self.asset(picture if picture.startswith('GFX_') else 'GFX_idea_' + picture, path, idea.line)
        for folder in ('common/country_leader', 'common/unit_leader'):
            for path, doc in self.docs(folder, mod=True):
                for trait in children(get(doc, 'leader_traits', [])):
                    self.need_loc(trait.key, path, trait.line)
        for path, doc in self.docs('events', mod=True):
            for event in doc:
                for n in walk(event.value):
                    if n.key in ('title', 'desc') and isinstance(n.value, str):
                        self.need_loc(n.value, path, n.line)
                    if n.key in ('title', 'desc') and isinstance(n.value, list):
                        self.need_loc(get(n.value, 'text'), path, n.line)
                    if n.key == 'option':
                        self.need_loc(get(n.value, 'name'), path, n.line)
                    if n.key in ('create_country_leader', 'create_field_marshal', 'create_corps_commander', 'create_navy_leader'):
                        self.need_loc(get(n.value, 'name'), path, n.line)
        # Tooltip/display keys may appear inside any content/effect folder.
        keys = {'custom_effect_tooltip', 'custom_trigger_tooltip', 'tooltip', 'localization_key',
                'custom_cost_text', 'custom_cost_tooltip', 'pdx_tooltip'}
        for path in sorted(self.scanned):
            if not path.endswith(('.txt', '.gui')):
                continue
            try:
                doc = self.vfs.doc(path)
            except (ScriptError, UnicodeError):
                continue
            for n in walk(doc):
                if path.endswith('.gui') and n.key == 'text' and isinstance(n.value, str):
                    self.need_loc(n.value, path, n.line)
                if n.key in keys and isinstance(n.value, str):
                    self.need_loc(n.value, path, n.line)
                if n.key == 'custom_trigger_tooltip' and isinstance(n.value, list):
                    self.need_loc(get(n.value, 'tooltip'), path, n.line)
        for key, refs in sorted(self.required_loc.items()):
            for lang, entries in self.loc.items():
                if key not in entries:
                    path, number = refs[0]
                    self.issue('localisation', 'missing', path, number, f'{lang}: {key}')
        self.stats['required_localisation_keys'] = len(self.required_loc)

    def map(self):
        path = 'map/definition.csv'
        provinces = {r[0]: r for r in csv.reader(io.StringIO(self.vfs.read(path).decode('utf-8-sig')), delimiter=';') if len(r) >= 6 and r[0].isdigit() and r[0] != '0'}
        country_tags = {n.key for _, doc in self.docs('common/country_tags') for n in doc if n.key and re.fullmatch('[A-Z0-9]{3}', n.key)}
        state_categories = {n.key for _, doc in self.docs('common/state_category') for n in children(get(doc, 'state_categories', []))}
        buildings = {n.key: get(n.value, 'level_cap', []) for _, doc in self.docs('common/buildings') for n in children(get(doc, 'buildings', []))}
        regions, region_ids, states, membership = defaultdict(list), {}, {}, defaultdict(list)
        for path, doc in self.docs('map/strategicregions'):
            region = get(doc, 'strategic_region', [])
            rid = get(region, 'id')
            if rid in region_ids:
                self.issue('map', 'region_id', path, 1, f'{rid}: повтор из {region_ids[rid]}')
            region_ids[rid] = path
            for n in children(get(region, 'provinces', [])):
                regions[n.value].append(rid)
                if n.value not in provinces:
                    self.issue('map', 'region_province', path, n.line, str(n.value))
        for path, doc in self.docs('history/states'):
            state = get(doc, 'state', [])
            sid = get(state, 'id')
            if sid in states:
                self.issue('map', 'state_id', path, 1, f'{sid}: повтор из {states[sid][0]}')
            states[sid] = (path, state)
            if get(state, 'state_category') not in state_categories:
                self.issue('map', 'state_category', path, 1, f'{sid}: неизвестная категория {get(state, "state_category")}')
            manpower = get(state, 'manpower', '0')
            if not re.fullmatch(r'\d+(?:\.\d+)?', str(manpower)):
                self.issue('map', 'manpower', path, 1, f'{sid}: неверное население {manpower}')
            owned = {n.value for n in children(get(state, 'provinces', []))}
            for n in children(get(state, 'provinces', [])):
                membership[n.value].append(sid)
                if n.value not in provinces:
                    self.issue('map', 'province', path, n.line, f'Неизвестная провинция {n.value}')
                elif provinces[n.value][4] == 'sea':
                    self.issue('map', 'water_province', path, n.line, f'Морская провинция {n.value} включена в штат')
                elif provinces[n.value][4] == 'lake':
                    # Vanilla 1.19.3 assigns lakes to states intentionally.
                    self.stats['state_lake_provinces'] += 1
            for n in walk(get(state, 'history', [])):
                if n.key in ('owner', 'controller', 'add_core_of') and n.value not in country_tags:
                    self.issue('map', 'country_tag', path, n.line, f'{sid}: {n.key}={n.value} не определён')
                if n.key == 'victory_points':
                    vals = children(n.value)
                    if len(vals) % 2 or any(v.value not in owned for v in vals[::2]):
                        self.issue('map', 'victory_point', path, n.line, f'Очки победы вне штата {sid}')
                    if any(not isinstance(v.value, str) or not re.fullmatch(r'\d+(?:\.\d+)?', v.value) for v in vals[1::2]):
                        self.issue('map', 'victory_point_value', path, n.line, f'{sid}: неверная величина очков победы')
                    self.stats['victory_point_entries'] += len(vals) // 2
                if n.key == 'buildings':
                    for b in children(n.value):
                        if b.key and b.key.isdigit():
                            if b.key not in owned:
                                self.issue('map', 'building_province', path, b.line, f'{b.key}: здание вне штата {sid}')
                            if any(x.key in ('naval_base', 'coastal_bunker') for x in children(b.value)) and provinces.get(b.key, ['', '', '', '', '', 'false'])[5] != 'true':
                                self.issue('map', 'coastal_building', path, b.line, f'{b.key}: береговое здание во внутренней провинции')
                        for level in (children(b.value) if isinstance(b.value, list) else [b]):
                            self.stats['building_entries'] += 1
                            if level.key not in buildings:
                                self.issue('map', 'building_type', path, level.line, f'{sid}: неизвестное здание {level.key}')
                            if isinstance(level.value, str) and (not re.fullmatch(r'\d+', level.value)):
                                self.issue('map', 'building_level', path, level.line, f'{level.key}: неверный уровень {level.value}')
                            elif isinstance(level.value, str):
                                cap = get(buildings.get(level.key, []), 'province_max' if b.key and b.key.isdigit() else 'state_max')
                                if isinstance(cap, str) and cap.isdigit() and int(level.value) > int(cap):
                                    self.issue('map', 'building_cap', path, level.line, f'{sid}: {level.key}={level.value} превышает лимит {cap}')
            if sid in ('200', '1082'):
                self.stats[f'state_{sid}_provinces'] = len(owned)
                self.stats[f'state_{sid}_vp'] = sum(1 for n in walk(get(state, 'history', [])) if n.key == 'victory_points')
        for pid, row in provinces.items():
            if len(regions[pid]) != 1:
                self.issue('map', 'region_assignment', 'map/strategicregions', 1, f'{pid}: регионы {regions[pid]}')
            if len(membership[pid]) > 1 or (row[4] == 'land' and len(membership[pid]) != 1):
                self.issue('map', 'state_assignment', 'history/states', 1, f'{pid}: штаты {membership[pid]}')
        self.stats.update({'effective_states': len(states), 'effective_provinces': len(provinces), 'strategic_regions': len(region_ids)})
        from validate_map_initialization import validate_map_initialization
        validate_map_initialization(self.root, self.game, lambda ok, msg: None if ok else self.issue('map', 'initialization', 'map', 1, msg))

    @staticmethod
    def contradictions(node):
        """Only provable conjunction conflicts; OR/variable/scripted triggers opaque."""
        positive, negative = set(), set()
        simple = {'tag', 'original_tag', 'has_government', 'has_country_flag', 'has_completed_focus', 'has_idea', 'exists', 'always'}
        def add(nodes):
            for n in children(nodes):
                if n.key == 'AND':
                    add(n.value)
                elif n.key in simple and isinstance(n.value, str):
                    positive.add((n.key, n.value))
                elif n.key == 'NOT' and len(children(n.value)) == 1:
                    c = n.value[0]
                    if c.key in simple and isinstance(c.value, str):
                        negative.add((c.key, c.value))
        add(node)
        conflicts = positive & negative
        for key in ('tag', 'original_tag', 'has_government', 'exists', 'always'):
            vals = {v for k, v in positive if k == key}
            if len(vals) > 1:
                conflicts.add((key, '/'.join(sorted(vals))))
        return conflicts

    def decisions(self):
        for path, doc in self.docs('common/decisions/categories', mod=True):
            for category in doc:
                self.need_loc(category.key, path, category.line)
                icon = get(category.value, 'icon')
                if icon:
                    self.asset(icon if icon.startswith('GFX_') else 'GFX_decision_category_' + icon, path, category.line)
                else:
                    self.issue('decisions', 'category_icon', path, category.line, f'{category.key}: нет иконки')
        initialized, bounded, used = defaultdict(list), defaultdict(list), defaultdict(list)
        dynamic_doc = (self.game / 'documentation/dynamic_variables_documentation.md').read_text(encoding='utf-8-sig')
        dynamic_vars = set(re.findall(r'^### (\w+)', dynamic_doc, re.M))
        for path in sorted(self.scanned):
            if not path.endswith('.txt'):
                continue
            try:
                doc = self.vfs.doc(path)
            except (ScriptError, UnicodeError):
                continue
            for n in walk(doc):
                if n.key not in ('set_variable', 'set_temp_variable', 'clamp_variable', 'check_variable', 'add_to_variable', 'subtract_from_variable', 'multiply_variable', 'divide_variable', 'clear_variable'):
                    continue
                var = get(n.value, 'var') if isinstance(n.value, list) else n.value
                if not var and isinstance(n.value, list):
                    var = next((c.key for c in n.value if c.key not in ('value', 'tooltip', 'compare', 'min', 'max')), None)
                if not isinstance(var, str):
                    continue
                if n.key in ('set_variable', 'set_temp_variable', 'clear_variable'):
                    initialized[var].append(f'{path}:{n.line}')
                if n.key == 'clamp_variable':
                    bounded[var].append((get(n.value, 'min'), get(n.value, 'max'), f'{path}:{n.line}'))
                if path.startswith('common/decisions/'):
                    used[var].append((path, n.line))
        for var, refs in sorted(used.items()):
            self.variable_inventory[var] = {'references': refs, 'initializers': initialized[var], 'bounds': bounded[var]}
            if var in dynamic_vars:
                self.variable_inventory[var]['initializers'] = ['Динамическая переменная движка: documentation/dynamic_variables_documentation.md']
            elif not initialized[var]:
                self.issue('decisions', 'variable_init', refs[0][0], refs[0][1], f'{var}: явная инициализация в моде не найдена; проверить наследуемые/временные переменные', 'warning')
            if not bounded[var]:
                self.stats['decision_variables_without_clamp'] += 1
        self.stats['decision_variables'] = len(used)
        for path, doc in self.docs('common/decisions', mod=True):
            if '/categories/' in path:
                continue
            for category in doc:
                if category.key not in self.category_ids:
                    self.issue('decisions', 'category_missing', path, category.line, str(category.key))
                for d in children(category.value):
                    if not isinstance(d.value, list):
                        continue
                    self.stats['decisions'] += 1
                    hidden = get(get(d.value, 'allowed', []), 'always') == 'no'
                    if hidden:
                        self.stats['disabled_compatibility_decisions'] += 1
                    else:
                        self.need_loc(get(d.value, 'name', d.key), path, d.line)
                        self.need_loc(d.key + '_desc', path, d.line)
                    icon = get(d.value, 'icon')
                    if isinstance(icon, str):
                        self.asset(icon if icon.startswith('GFX_') else 'GFX_decision_' + icon, path, d.line)
                    timeout = get(d.value, 'days_mission_timeout')
                    if timeout:
                        self.stats['missions'] += 1
                        effect = get(d.value, 'timeout_effect')
                        if not isinstance(effect, list):
                            self.issue('decisions', 'timeout', path, d.line, f'{d.key}: отсутствует timeout_effect')
                        if re.fullmatch(r'-?\d+', str(timeout)) and int(timeout) <= 0:
                            self.issue('decisions', 'timeout_days', path, d.line, f'{d.key}: {timeout} дней')
                    for field in ('visible', 'available'):
                        for conflict in self.contradictions(get(d.value, field, [])):
                            self.issue('decisions', 'contradiction', path, d.line, f'{d.key}/{field}: {conflict}')
                    combined = children(get(d.value, 'visible', [])) + children(get(d.value, 'available', []))
                    for conflict in self.contradictions(combined):
                        self.issue('decisions', 'cross_contradiction', path, d.line, f'{d.key}: visible/available {conflict}')

    def tooling(self):
        import hashlib
        for manifest in (self.root / 'docs/art').glob('*.json'):
            self.scanned.add(manifest.relative_to(self.root).as_posix())
            self.stats['art_manifests'] += 1
            def visit(value):
                if isinstance(value, list):
                    for child in value:
                        visit(child)
                elif isinstance(value, dict):
                    source = value.get('source')
                    if isinstance(source, str) and source.startswith(('docs/', 'gfx/')):
                        path = self.root / source
                        if not path.is_file():
                            self.issue('tooling', 'source_missing', manifest.relative_to(self.root).as_posix(), 1, source)
                        elif 'source_sha256' in value and hashlib.sha256(path.read_bytes()).hexdigest() != value['source_sha256']:
                            self.issue('tooling', 'source_hash', manifest.relative_to(self.root).as_posix(), 1, source)
                        if path.is_file():
                            self.scanned.add(source)
                    for child in value.values():
                        if isinstance(child, (dict, list)):
                            visit(child)
            visit(json.loads(manifest.read_text(encoding='utf-8-sig')))

    def run(self):
        self.syntax()
        self.localisation()
        self.graphics()
        self.definitions()
        self.focus()
        self.map()
        self.decisions()
        self.content()
        self.tooling()
        # A reference may be reached through more than one independent registry.
        self.issues = list({(x.category, x.code, x.file, x.line, x.message): x for x in self.issues}.values())
        self.stats['total_files_scanned'] = len(self.scanned)
        excluded = {'.git', '.codex', '.agents', '.aws', '.kilo', '__pycache__', 'old-mod'}
        for directory, dirs, files in os.walk(self.root):
            dirs[:] = [d for d in dirs if d not in excluded]
            self.stats['workspace_inventory_files'] += len(files)
        version_file = self.game / 'launcher-settings.json'
        version = json.loads(version_file.read_text(encoding='utf-8-sig')).get('rawVersion') if version_file.exists() else 'не определена'
        return {'schema': 1, 'game': str(self.game), 'version': version,
                'generated_at': datetime.now(ZoneInfo('Europe/Minsk')).isoformat(timespec='seconds'), 'stats': dict(self.stats),
                'issues': [asdict(x) for x in self.issues], 'variables': self.variable_inventory}


def verification(game):
    results = []
    # Some validate_*.py are libraries without a CLI; the main validator calls
    # these explicitly. A zero-exit import alone is NOT counted as a test.
    scripts = ('validate_country_content.py',
               'validate_runtime_setup.py', 'validate_soviet_content.py',
               'validate_turkey_balkans.py', 'validate_austria_campaigns.py',
               'validate_mkn_overhaul.py', 'validate_mkn_art.py', 'validate_repository_layout.py')
    for filename in scripts:
        cmd = [sys.executable, str(ROOT / 'tools' / filename)]
        if filename != 'validate_repository_layout.py':
            cmd += ['--game', str(game)]
        result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        results.append({'name': filename, 'command': cmd, 'returncode': result.returncode, 'output': result.stdout + result.stderr})
    cmd = [sys.executable, '-m', 'unittest', 'discover', '-s', 'tools', '-p', 'test_full_project_audit.py', '-v']
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    results.append({'name': 'test_full_project_audit.py', 'command': cmd, 'returncode': result.returncode, 'output': result.stdout + result.stderr})
    result = subprocess.run(['git', 'diff', '--check'], cwd=ROOT, capture_output=True, text=True)
    results.append({'name': 'git diff --check', 'command': ['git', 'diff', '--check'], 'returncode': result.returncode, 'output': result.stdout + result.stderr})
    return results


def markdown(result, baseline, checks, notes):
    issues, stats = result['issues'], result['stats']
    before = baseline.get('issues', []) if baseline else []
    ident = lambda x: (x['category'], x['code'], x['file'], x['message'])
    remaining = {ident(x) for x in issues}
    fixed = [x for x in before if ident(x) not in remaining]
    count = lambda xs, level: sum(x['severity'] == level for x in xs)
    def remedy(issue):
        code = issue['code']
        if code == 'record_scalar':
            return 'Исправлено экранирование create_unit; устранена повторная порча в hoi4_script.py'
        if code == 'sprite_duplicate':
            return 'Удалён повтор; сохранена последняя регистрация'
        if code in ('texture_missing', 'texture_case'):
            return 'Указан существующий штатный ресурс; см. точные замены выше'
        if code == 'texture_noncanonical':
            return 'Двойные / заменены одинарными'
        if code == 'sprite_missing':
            return 'Регистрация MKN_decision_categories.gfx' if '/categories/' in issue['file'] else 'Исправлено имя на зарегистрированный спрайт'
        if code == 'duplicate':
            return 'Описание сохранено в nww_UKR_expansion_l_*, прежняя копия удалена'
        if code == 'missing':
            lang, key = issue['message'].split(': ', 1)
            owner = 'TUR_audit' if key.startswith('TUR_') else ('NWW_native_audit' if key.startswith('MTG_') else 'SOV_audit')
            return f'Добавлена строка в localisation/{lang}/{owner}_l_{lang}.yml'
        if code == 'source_missing':
            return 'PNG извлечён из DDS; обновлён манифест, прежнее происхождение сохранено'
        return 'См. описание подтверждённых исправлений выше'
    rows = ['# Полный статический аудит NWW Reborn', '',
            f'Дата и время (Europe/Minsk): {result["generated_at"]}. Установленная HOI4: {result["version"]}.', '',
            '## Краткие результаты', '',
            f'- Инвентаризация рабочего каталога: **{stats["workspace_inventory_files"]} файлов**, без Git и служебных кешей.',
            f'- Проверено содержимое **{stats["total_files_scanned"]} файлов**: игровые скрипты, локализация, изображения и арт-манифесты.',
            f'- Исходный замер: **{count(before, "error")} ошибок**, **{count(before, "warning")} предупреждений**.',
            f'- Устранено диагностик исходного замера: **{count(fixed, "error")} ошибок**, **{count(fixed, "warning")} предупреждений**.',
            f'- Финальный замер: **{count(issues, "error")} ошибок**, **{count(issues, "warning")} предупреждений**.', '',
            f'Каталог игры: `{result["game"]}`. Windows-путь из AGENTS.md заменён фактическим Linux-путём.', '',
            '## Методика и границы', '',
            '**`old-mod/` исключён из аудита по указанию пользователя. Изменений в архиве нет.**', '',
            'Аудитор читает реальные файлы игры, распакованные DLC и ZIP, затем применяет файловые переопределения мода. '
            'Реестры включают только определения соответствующего типа; вложенные event/province ID не становятся ID фокусов. '
            'Скобки и кавычки проверяются лексером с полным потреблением текста; комментарии, строки и экранирование учитываются. '
            'Локализация учитывает корневые файлы и replace, а также обе языковые папки и наследуемые строки игры. '
            'Отсутствие копии ванильного ресурса в моде не считается ошибкой.', '',
            'Статический анализ не доказывает отсутствие всех логических ошибок в произвольных скриптах. '
            'Проверка конфликтов условий ограничена доказуемыми противоречиями AND/NOT; OR и зависимые от мира условия требуют сценариев. '
            'Переменные представлены отдельным реестром и дополнительно проверены сценарными валидаторами. '
            'Некратные степени двойки размеры интерфейса допустимы: портреты 65×67, фокусы 96×96 и иллюстрации нельзя автоматически растягивать до POT. '
            'Статус запуска пользователя и исправлений по его журналу указан отдельно ниже. '
            'Успешный статический прогон не подтверждает результат повторного запуска игры после этих исправлений.', '',
            '## Подтверждённые исправления и ссылки на образцы', '', notes.strip() if notes else 'См. диагностики ниже.', '',
            '## Подробные результаты по категориям', '']
    for cat, title in CATEGORIES.items():
        rows += [f'### {title}', '']
        old = [x for x in fixed if x['category'] == cat]
        current = [x for x in issues if x['category'] == cat]
        rows += [f'Устранено: {len(old)}. Осталось: {len(current)}.', '']
        if old:
            rows += ['| Файл и строка исходного замера | Проверка | Исходная проблема | Применённое исправление |', '|---|---|---|---|']
            for x in old:
                msg = x['message'].replace('|', '\\|').replace('\n', ' ')
                rows.append(f'| `{x["file"]}:{x["line"]}` | `{x["code"]}` | {msg} | {remedy(x)} |')
            rows.append('')
        if current:
            rows += ['| Уровень | Файл и строка | Проверка | Результат |', '|---|---|---|---|']
            for x in current:
                msg = x['message'].replace('|', '\\|').replace('\n', ' ')
                rows.append(f'| {x["severity"]} | `{x["file"]}:{x["line"]}` | `{x["code"]}` | {msg} |')
            rows.append('')
    rows += ['## Объём автоматических проверок', '', '| Метрика | Значение |', '|---|---|']
    rows += [f'| `{key}` | {value} |' for key, value in sorted(stats.items())]
    rows += ['', '## Переменные решений', '',
             '`clamp_variable` принудительно удерживает число в диапазоне min…max. Его отсутствие само по себе не означает ошибку: '
             'счётчик может расти, а ID штата нельзя обрезать как шкалу. Этот раздел — реестр и разбор, а не список исправленных багов. '
             '**В первом аудите значения, пороги и ограничения перечисленных переменных не менялись.**', '',
             '| Переменная и назначение | Присваивание / очистка | Защита и диапазон | Что изменено |', '|---|---|---|---|']
    for var, info in result['variables'].items():
        init = ', '.join(f'`{v}`' for v in info['initializers']) or 'Явная не найдена; см. предупреждения'
        purpose, protection, action = VARIABLE_REVIEW.get(var, ('Назначение требует разбора', 'Явный clamp не найден' if not info['bounds'] else 'Есть явный clamp', 'Автоматически не изменялась'))
        bounds = '; '.join(f'{v[0]}…{v[1]} (`{v[2]}`)' for v in info['bounds'])
        rows.append(f'| `{var}` — {purpose} | {init} | {protection}' + (f' Места clamp: {bounds}' if bounds else '') + f' | {action} |')
    rows += ['', '## Статус верификации', '', '| Проверка | Код возврата | Статус |', '|---|---|---|']
    rows += [f'| `{v["name"]}` | {v["returncode"]} | {"PASS" if v["returncode"] == 0 else "FAIL"} |' for v in checks]
    if not checks:
        rows += ['| Дополнительные валидаторы | — | Не запущены: требуется --verify |']
    for v in checks:
        rows += ['', f'### Вывод `{v["name"]}`', '', '```text', v['output'].strip() or '(пустой вывод)', '```']
    rows += ['', '## Повторный запуск', '', '```bash',
             'python tools/full_project_audit.py --game "/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV" --baseline docs/audit/baseline.json --verify',
             '```', '', 'Полные машинные результаты: `docs/audit/latest.json`; исходный замер: `docs/audit/baseline.json`. '
             'Аудитор не исправляет контент эвристически при каждом запуске: внесённые исправления находятся в Git и перечислены выше.', '']
    return '\n'.join(rows)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--game', type=Path, required=True)
    p.add_argument('--output', type=Path, default=ROOT / 'docs/audit/latest.json')
    p.add_argument('--report', type=Path, default=ROOT / 'docs/AUDIT_REPORT.md')
    p.add_argument('--baseline', type=Path)
    p.add_argument('--verify', action='store_true')
    args = p.parse_args()
    if not (args.game / 'common').is_dir():
        p.error('Не найден установленный каталог HOI4/common')
    result = Audit(ROOT, args.game).run()
    baseline = json.loads(args.baseline.read_text(encoding='utf-8')) if args.baseline else None
    checks = verification(args.game) if args.verify else []
    result['verification'] = checks
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    notes = ROOT / 'docs/audit/change_notes.md'
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(markdown(result, baseline, checks, notes.read_text(encoding='utf-8') if notes.exists() else ''), encoding='utf-8')
    counts = Counter(x['severity'] for x in result['issues'])
    print(f'Audit: {result["stats"]["total_files_scanned"]} files; {counts["error"]} errors; {counts["warning"]} warnings')
    for cat in CATEGORIES:
        print(cat, dict(Counter(x['code'] for x in result['issues'] if x['category'] == cat)))
    print(f'Report: {args.report}')
    return int(counts['error'] > 0 or any(v['returncode'] != 0 for v in checks))


if __name__ == '__main__':
    sys.exit(main())
