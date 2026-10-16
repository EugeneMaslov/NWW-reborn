"""Export a self-contained, source-derived MKN industry dossier for external review."""
from collections import Counter
from decimal import Decimal
from hashlib import sha256
from pathlib import Path
import argparse
import re

from hoi4_script import read, one, values, walk, tree_focuses, quoted

ROOT = Path(__file__).resolve().parents[1]


def script(node, depth=0):
    lines = []
    for key, value, op in node:
        prefix = '    ' * depth
        head = '' if key is None else f'{key} {op} '
        if isinstance(value, list):
            lines.extend([prefix + head + '{', script(value, depth + 1), prefix + '}'])
        else:
            token = quoted(value) if not value or re.search(r'[\s{}#"]', value) else value
            lines.append(prefix + head + token)
    return '\n'.join(lines)


def export(output):
    sources = set()
    def load(path):
        sources.add(path)
        return read(ROOT / path)
    locales = {}
    for lang in ('russian', 'english'):
        loc = {}
        for path in sorted(ROOT.glob(f'localisation/**/*l_{lang}.yml')):
            pairs = re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$', path.read_text(encoding='utf-8-sig'), re.M)
            loc.update(pairs)
            if any(k.startswith('MKN_') for k, _ in pairs):
                sources.add(str(path.relative_to(ROOT)))
        locales[lang] = loc
    ru, en = locales['russian'], locales['english']
    label = lambda fid: ru.get(fid, fid)
    focus_dir = ROOT / 'common/national_focus'
    tree = one(load('common/national_focus/MKN.txt'), 'focus_tree')
    focuses = {one(f, 'id'): f for f in tree_focuses(tree, focus_dir)}
    origins = {}
    for path in sorted(focus_dir.glob('*.txt')):
        doc = read(path)
        nodes = values(doc, 'shared_focus') + [f for t in values(doc, 'focus_tree') for f in values(t, 'focus')]
        for f in nodes:
            fid = one(f, 'id')
            if fid in focuses and f == focuses[fid]:
                origins[fid] = str(path.relative_to(ROOT))
    parents = {fid: [values(p, 'focus') for p in values(f, 'prerequisite')] for fid, f in focuses.items()}
    branches = {}
    for root in ('MKN_dneprostroi', 'MKN_free_cooperatives'):
        branch = {root}
        while True:
            expanded = branch | {fid for fid, groups in parents.items() if any(p in branch for g in groups for p in g)}
            if expanded == branch:
                break
            branch = expanded
        assert 10 <= len(branch) <= 12, (root, len(branch))
        branches[root] = branch
    core = set.union(*branches.values())
    producer_paths = ['common/military_industrial_organization/organizations/nww_organizations.txt', 'common/military_industrial_organization/organizations/MKN_organizations.txt', 'common/ideas/nww_companies.txt', 'common/ideas/nww_MKN_ideas.txt', 'common/country_leader/nww_mkn_industry_traits.txt']
    producers = {}
    producer_gates = set()
    for path in producer_paths:
        doc = load(path)
        # Top-level MIOs, or direct ideas under designer/concern groups.
        candidates = list(doc)
        for group in values(doc, 'ideas'):
            candidates += [entry for _, entries, _ in group if isinstance(entries, list) for entry in entries]
        selected = [(k, v, o) for k, v, o in candidates if k and k.startswith('MKN_')]
        if not selected and 'traits' in path:
            selected = doc
        producers[path] = selected
        producer_gates.update(v for k, v, _ in walk(selected) if k == 'has_completed_focus' and v in focuses)
    reasons = {}
    economic_commands = {'add_building_construction', 'add_resource', 'add_research_slot', 'add_offsite_building', 'add_extra_state_shared_building_slots', 'build_railway'}
    economic_categories = {'industry', 'construction_tech', 'electronics', 'excavation_tech', 'fuel_silos', 'synthetic_oil', 'production', 'industry_folder'}
    for fid, f in focuses.items():
        reward = one(f, 'completion_reward', [])
        commands = {k for k, _, _ in walk(reward)}
        why = []
        if commands & economic_commands:
            why.append('Строительство, ресурсы или исследовательская мощность')
        if any(k and k.startswith('MKN_unified_') for k, _, _ in walk(reward)):
            why.append('Изменяет общий экономический дух MKN')
        if any(k in ('category', 'technology') and v in economic_categories for k, v, _ in walk(reward)):
            why.append('Бонус промышленным технологиям')
        if fid in producer_gates or fid == 'MKN_free_workshops_focus':
            why.append('Открывает/развивает предприятие или MIO')
        if fid in core:
            why = ['Основная промышленная ветка']
        if why:
            reasons[fid] = why
    selected = set(reasons)
    ancestors = set(selected)
    while True:
        expanded = ancestors | {p for fid in ancestors for g in parents[fid] for p in g}
        if expanded == ancestors:
            break
        ancestors = expanded
    assert all(fid in ru and fid + '_desc' in ru and fid in en and fid + '_desc' in en for fid in selected)
    for fid in ancestors:
        sources.add(origins[fid])
    out = ['# MKN: промышленность — пакет для анализа другой нейросетью', '',
           'Этот файл самодостаточен: содержит названия, описания, награды, условия, исходные определения и связанные системы. Это снимок текущих файлов мода, а не проект новых наград.', '',
           f'Основная промышленность: **{len(core)} фокусов**, по 10 на взаимоисключающих путях; пять решений конгресса и девять региональных проектов. Дополнительно: **{len(selected-core)}** связанных фокусов науки, политики, предприятий и военной инфраструктуры. Всего карточек: **{len(selected)}**. Чисто боевые фокусы без промышленного эффекта не включены; их необходимые предки приведены отдельно.', '',
           '## Контекст и правила интерпретации', '',
           '- Первая мировая война не происходила. Сохранять действующие ID и лор, монарха Махно и совместимость сохранений.',
           '- Стоимость focus.cost измеряется неделями: 5 = 35 дней, 10 = 70 дней. Несколько блоков prerequisite соединяются И; focus внутри одного блока — ИЛИ. Условия available добавляются к prerequisites. Ветви с mutually_exclusive одновременно пройти нельзя.',
           '- Награды в if/limit и random_owned_controlled_state условны. Числа построек в обзоре — потенциальные суммы по коду, а не обещание фактической выдачи. Проверять владение, контроль, ядра, регион и строительные слоты.',
           '- Общий постоянный экономический дух — MKN_free_industry_modifier. Развивать его через MKN_unified_*; не заменять каждую ступень отдельным духом. Военные, авиационные и морские программы имеют собственные общие духи.',
           '- Значения ниже даны в сырых единицах движка. political_power_gain — плоский прирост в сутки; фактор 0.05 обычно означает 5 процентных пунктов. Не интерпретировать все числовые значения как проценты.',
           '- custom_effect_tooltip/show_mio_tooltip/unlock_mio_trait_tooltip описывают интерфейс, сами по себе ничего не выдают. Реальные разблокировки предприятий находятся в available у предприятия/черты.',
           '- Сохранять паритет Arms Against Tyranny MIO и обычных конструкторов без DLC. Не копировать огромные награды из старого мода. Проверять ресурсную/энергетическую систему установленной версии.',
           '- Восстановление общих переменных в сохранении не должно повторно выдавать заводы, ресурсы, политическую власть или технику. Полный код восстановления включён ниже.',
           '- Эти данные извлечены статически. Реальные сроки кампании, отображение подсказок и выдача наград требуют проверки в игре.', '',
           '## Основные ветки', '']
    def ordered(ids):
        return sorted(ids, key=lambda fid: (int(one(focuses[fid], 'y', '0')), int(one(focuses[fid], 'x', '0')), fid))
    for root, ids in branches.items():
        counts = Counter()
        for fid in ids:
            for k, v, _ in walk(one(focuses[fid], 'completion_reward', [])):
                if k == 'add_building_construction':
                    counts[one(v, 'type')] += int(one(v, 'level', '1'))
        out += [f'### {label(root)} — `{root}`', '',
                f'{len(ids)} фокусов; сумма их длительностей: {sum(Decimal(one(focuses[f], "cost", "10"))*7 for f in ids)} дней. Это сумма всей ветки, а не кратчайший путь к отдельной награде. Проекты выполняются отдельно от национальных фокусов.', '',
                'Потенциальные постройки при выполнении всех внутренних условий: ' + ', '.join(f'`{k}`: +{v}' for k, v in sorted(counts.items())) + '.', '']
        out += [f'- {label(fid)} — `{fid}`' for fid in ordered(ids)] + ['']
    out += ['## Карточки фокусов', '']
    order = ordered(branches['MKN_dneprostroi']) + ordered(branches['MKN_free_cooperatives']) + ordered(selected-core)
    for fid in order:
        f = focuses[fid]
        source = origins[fid]
        text = (ROOT/source).read_text(encoding='utf-8-sig')
        match = re.search(r'\bid\s*=\s*' + re.escape(fid) + r'\b', text)
        line = text[:match.start()].count('\n') + 1
        children = [other for other, groups in parents.items() if any(fid in g for g in groups)]
        out += [f'### {label(fid)} — `{fid}`', '',
                f'Английское название: {en[fid]}. Категория: {"; ".join(reasons[fid])}.', '',
                f'Описание RU: {ru[fid+"_desc"]}', '', f'Описание EN: {en[fid+"_desc"]}', '',
                f'Источник: `{source}:{line}`. Стоимость: {one(f,"cost","10")} ({Decimal(one(f,"cost","10"))*7} дней). Координаты: x={one(f,"x")}, y={one(f,"y")}.', '',
                'Предпосылки: ' + (' И '.join('(' + ' ИЛИ '.join(f'{label(p)} [{p}]' for p in group) + ')' for group in parents[fid]) or 'нет нарисованной предпосылки; см. available') + '.', '',
                'Непосредственные продолжения: ' + (', '.join(children) or 'нет') + '.', '']
        reward = one(f, 'completion_reward', [])
        facts = []
        for k, v, _ in walk(reward):
            if k == 'add_political_power':
                facts.append(f'Политическая власть: {v}')
            elif k == 'add_building_construction':
                facts.append(f'Потенциальная постройка: {one(v,"type")} +{one(v,"level","1")}')
            elif k == 'add_resource':
                facts.append(f'Потенциальный ресурс: {one(v,"type")} +{one(v,"amount")}')
            elif k == 'add_to_variable':
                facts.extend(f'Изменение параметра: {n} {amount}' for n, amount, _ in v if n != 'tooltip')
            elif k in ('add_ideas', 'add_research_slot', 'add_stability', 'add_war_support') and not isinstance(v, list):
                facts.append(f'{k}: {v}')
        out += ['Обзор награды (условия и остальные эффекты полностью в коде ниже):', ''] + [f'- {s}' for s in facts or ['См. полную награду в completion_reward.']]
        out += ['', 'Полное определение; включает точные награды, условия, взаимоисключения и AI:', '', '```pdx', script([('focus', f, '=')]), '```', '']
    out += ['## Необходимые предки вне промышленного каталога', '', 'Для проверки достижимости, политических и военных ограничений. Эти фокусы не входят в число промышленных карточек.', '']
    for fid in ordered(ancestors-selected):
        out += [f'### {label(fid)} — `{fid}`', '', ru.get(fid+'_desc', ''), '', '```pdx', script([('focus', focuses[fid], '=')]), '```', '']
    out += ['## Общая экономика: исходные значения и восстановление', '']
    related = ['common/dynamic_modifiers/nww_dynamic_modifiers.txt', 'common/scripted_effects/nww_mkn_progression.txt', 'common/on_actions/nww_mkn_progression.txt', 'history/countries/MKN - Makhnovists.txt', 'common/ideas/MKN_ideas.txt', 'common/decisions/MKN_economic_decisions.txt', 'common/decisions/categories/MKN_economic_categories.txt', 'common/ideas/MKN_economic_ideas.txt']
    related += ['common/scripted_triggers/MKN_ukraine_integration_triggers.txt', 'common/scripted_effects/MKN_ukraine_integration_effects.txt', 'common/on_actions/MKN_ukraine_integration_on_actions.txt', 'events/MKN_ukraine_integration_events.txt']
    related += ['common/decisions/MKN_ukraine_integration_decisions.txt', 'common/decisions/categories/MKN_ukraine_integration_categories.txt']
    # Include full country-owned progression and starting setup; select only MKN dynamic modifiers.
    for path in related:
        doc = load(path)
        if path.startswith('common/dynamic_modifiers'):
            doc = [(k,v,o) for k,v,o in doc if k and k.startswith('MKN_')]
        out += [f'### `{path}`', '', '```pdx', script(doc), '```', '']
    out += ['## Предприятия и производственные организации', '']
    for path, doc in producers.items():
        out += [f'### `{path}`', '', '```pdx', script(doc), '```', '']
    out += ['## Локализация новых хозяйственных решений, проектов и предприятий', '']
    for lang in ('russian', 'english'):
        path = f'localisation/MKN_economic_l_{lang}.yml'
        sources.add(path)
        out += [f'### `{path}`', '', '```yaml', (ROOT/path).read_text(encoding='utf-8-sig').rstrip(), '```', '']
    # Capture referenced country-owned helper effects recursively.
    helpers = {}
    for path in sorted((ROOT/'common/scripted_effects').glob('*.txt')):
        if 'mkn' in path.name.lower():
            helpers.update({k:(str(path.relative_to(ROOT)),v) for k,v,_ in read(path)})
    needed = {k for fid in ancestors for k,v,_ in walk(one(focuses[fid],'completion_reward',[])) if k in helpers}
    included = set()
    while needed-included:
        for key in sorted(needed-included):
            path, body = helpers[key]
            sources.add(path)
            out += [f'### Вспомогательный эффект `{key}` (`{path}`)', '', '```pdx', script([(key,body,'=')]), '```', '']
            included.add(key)
            needed.update(k for k,v,_ in walk(body) if k in helpers)
    out += ['## Регионы, затронутые наградами / стартовая территория', '', 'Полные определения модифицированных регионов: исходный владелец, ядра, постройки, ресурсы и население. Датированные записи history не равны стартовому состоянию.', '']
    state_ids = {k for fid in selected for k,v,_ in walk(one(focuses[fid],'completion_reward',[])) if k and k.isdigit() and isinstance(v,list)}
    state_ids.update(v for fid in selected for k,node,_ in walk(one(focuses[fid],'completion_reward',[])) if k=='prioritize' and isinstance(node,list) for _,v,_ in node)
    for path in sorted((ROOT/'history/states').glob('*.txt')):
        state = one(read(path),'state')
        if one(state,'id') in state_ids or one(one(state,'history',[]),'owner') == 'MKN':
            rel = str(path.relative_to(ROOT)); sources.add(rel)
            out += [f'### `{rel}`', '', '```pdx', script([('state',state,'=')]), '```', '']
    referenced = {v for fid in ancestors for k,v,_ in walk(focuses[fid]) if isinstance(v,str) and v in ru}
    out += ['## Локализация подсказок, духов и бонусов из определений', '', '```json']
    import json
    out += [json.dumps({key:{'ru':ru[key], 'en':en.get(key)} for key in sorted(referenced) if key not in focuses}, ensure_ascii=False, indent=2), '```', '', '## Проверяемость снимка', '',
            'Генератор: `python tools/export_mkn_industrial_focuses.py`. Источником наград являются текущие скрипты, не старые проектные JSON. Хеши позволяют обнаружить устаревание после правок.', '', '```text']
    out += [f'{sha256((ROOT/p).read_bytes()).hexdigest()}  {p}' for p in sorted(sources)] + ['```', '']
    output.write_text('\n'.join(out), encoding='utf-8')
    print(f'{output.relative_to(ROOT)}: {len(core)} main + {len(selected-core)} related focuses; {len(ancestors-selected)} prerequisite context focuses')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'docs/MKN_INDUSTRIAL_FOCUSES_FOR_AI.md')
    export(parser.parse_args().output)
