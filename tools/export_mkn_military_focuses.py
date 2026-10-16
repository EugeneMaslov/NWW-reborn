"""Export current MKN military focuses, HQ decisions and supporting definitions."""
import argparse
from decimal import Decimal
from hashlib import sha256
import json
from pathlib import Path
import re

from export_mkn_industrial_focuses import script
from hoi4_script import read, one, values, walk, tree_focuses

ROOT = Path(__file__).resolve().parents[1]


def export(output):
    sources = set()
    def load(path):
        sources.add(path)
        return read(ROOT/path)
    def fence(doc):
        return ['```pdx', script(doc), '```', '']
    loc = {}
    for lang in ('russian', 'english'):
        loc[lang] = {}
        for path in sorted(ROOT.glob(f'localisation/**/*l_{lang}.yml')):
            pairs = re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$',path.read_text(encoding='utf-8-sig'),re.M)
            loc[lang].update(pairs)
            if any(key.startswith('MKN_') for key,_ in pairs):
                sources.add(path.relative_to(ROOT).as_posix())
    ru,en = loc['russian'],loc['english']
    tree = one(load('common/national_focus/MKN.txt'),'focus_tree')
    fs = {one(f,'id'):f for f in tree_focuses(tree,ROOT/'common/national_focus')}
    parents = {fid:[values(p,'focus') for p in values(f,'prerequisite')] for fid,f in fs.items()}
    def descendants(fid):
        found = {fid}
        while True:
            expanded = found | {fid for fid,groups in parents.items() if any(p in found for g in groups for p in g)}
            if expanded == found:
                return found
            found = expanded
    services = {
        'Армия':descendants('MKN_steppe_general_staff') | {'MKN_memory_of_atamansha_marusya','MKN_the_black_guard_battalions'},
        'Авиация':descendants('MKN_steppe_hawks_and_schools'),
        'Флот':descendants('MKN_black_sea_flotilla_and_yards'),
    }
    primary = set.union(*services.values())
    assert sum(map(len,services.values())) == len(primary)
    supplemental = set()
    for fid,f in fs.items():
        reward = list(walk(one(f,'completion_reward',[])))
        if any(k and k.startswith(('MKN_army_','MKN_air_','MKN_navy_')) for k,v,_ in reward) or any(k in ('army_experience','air_experience','navy_experience','add_manpower','add_equipment_to_stockpile','load_oob','add_doctrine_cost_reduction','add_command_power','add_ace') for k,v,_ in reward):
            supplemental.add(fid)
    supplemental -= primary
    selected = primary | supplemental
    context = set(selected)
    while True:
        expanded = context | {p for fid in context for g in parents[fid] for p in g}
        expanded.update(v for fid in context for k,v,_ in walk(one(fs[fid],'available',[])) if k=='has_completed_focus' and v in fs)
        if expanded == context:
            break
        context = expanded
    origins = {}
    for path in sorted((ROOT/'common/national_focus').glob('*.txt')):
        doc = read(path)
        nodes = values(doc,'shared_focus') + [f for t in values(doc,'focus_tree') for f in values(t,'focus')]
        for f in nodes:
            fid = one(f,'id')
            if fid in context and f == fs[fid]:
                origins[fid] = path.relative_to(ROOT).as_posix()
    assert context <= origins.keys()
    assert all(fid in ru and fid+'_desc' in ru and fid in en and fid+'_desc' in en for fid in selected)
    def ordered(ids):
        return sorted(ids,key=lambda fid:(int(one(fs[fid],'y','0')),int(one(fs[fid],'x','0')),fid))
    out = ['# MKN: обновлённые военные фокусы и полевые штабы', '',
           'Снимок действующих скриптов NWW Reborn на 16 октября 2026 года. Самодостаточный файл для передачи другой нейросети: названия RU/EN, описания, точные награды, зависимости, ограничения, решения, общие духи и вспомогательные эффекты.', '',
           f'Военные деревья: **{len(primary)} фокусов** ('+', '.join(f'{name.lower()}: {len(ids)}' for name,ids in services.items())+f'). Отдельно: {len(supplemental)} связанных фокусов с прямыми военными наградами; {len(context-selected)} дополнительных определений предпосылок.', '',
           '## Что изменилось относительно старого пакета', '',
           'Прежние 130 военных фокусов переработаны в 30 институтов. Часть постоянных бонусов перенесена в тактические решения, строительство — в штабные проекты; поэтому оценивать баланс только по completion_reward фокусов недостаточно. Архивные ID используются для миграции сохранений и не означают отдельные игровые фокусы.', '',
           '## Правила анализа', '',
           '- Первая мировая война не происходила. Сохранять существующий лор, ID и монарха Махно с его портретом.',
           '- cost измеряется неделями: 5 = 35 дней, 10 = 70 дней. Несколько блоков prerequisite соединяются И; focus в одном блоке — ИЛИ. available добавляет ограничения, mutually_exclusive исключает альтернативную программу.',
           '- Один развиваемый постоянный дух на службу: MKN_army_development, MKN_air_development, MKN_navy_development. Параметры add_to_variable складываются; восстановление сохранений пересчитывает фактические ступени.',
           '- MKN_marusyas_legacy — отдельное памятное исключение. Фокусы Маруси сохраняют общий доступ после штаба и требования технологий/Гуляйполя для дивизий.',
           '- В наградах числовые параметры приведены в сырых единицах движка. Фактор 0.05 обычно означает 5 процентных пунктов; опыт, manpower и количество техники — абсолютные величины.',
           '- if/limit/else, DLC, флаги, владение и контроль могут ограничивать выдачу. Перечень эффектов не означает безусловную сумму наград. Проверять полное определение.',
           '- custom_effect_tooltip/show_mio_tooltip/unlock_mio_trait_tooltip только отображают информацию. Доступ к MIO, предприятиям и чертам определяется их собственными allowed/available.',
           '- Тактики и проекты имеют собственные цены, сроки, ограничения и отмену. Не переносить их награды обратно в фокусы без пересчёта баланса.',
           '- Миграция старых сохранений не должна повторно выдавать дивизии, опыт, технику или постройки. Старые флаги могут уже учитывать часть постоянных бонусов.',
           '- Статический снимок не подтверждает работу в новой кампании. После изменений проверять текущие игровые документацию и DLC-примеры, tooltips и свежий лог.', '',
           '## Сводка фокусов', '', '| Раздел | Название | ID | Дней |', '| --- | --- | --- | --- |']
    for name,ids in services.items():
        for fid in ordered(ids):
            out += [f'| {name} | {ru[fid]} | `{fid}` | {Decimal(one(fs[fid],"cost","10"))*7} |']
    out += ['']
    for name,ids in [*services.items(),('Связанные военные награды вне основных деревьев',supplemental),('Контекст предпосылок',context-selected)]:
        out += [f'## {name}', '']
        for fid in ordered(ids):
            f = fs[fid]; source = origins[fid]; sources.add(source)
            text = (ROOT/source).read_text(encoding='utf-8-sig')
            match = re.search(r'\bid\s*=\s*'+re.escape(fid)+r'\b',text)
            line = text[:match.start()].count('\n')+1
            out += [f'### {ru.get(fid,fid)} — `{fid}`', '', f'EN: {en.get(fid,fid)}.', '',
                    f'Описание RU: {ru.get(fid+"_desc","нет локализации")}', '',f'Описание EN: {en.get(fid+"_desc","нет локализации")}', '',
                    f'Источник: `{source}:{line}`. Стоимость: {one(f,"cost","10")} ({Decimal(one(f,"cost","10"))*7} дней). Координаты: x={one(f,"x")}, y={one(f,"y")}.', '',
                    'Предпосылки: '+(' И '.join('('+' ИЛИ '.join(f'{ru.get(p,p)} [{p}]' for p in g)+')' for g in parents[fid]) or 'нет нарисованной предпосылки; см. available')+'.', '',
                    'Взаимоисключения: '+(', '.join(p for g in values(f,'mutually_exclusive') for p in values(g,'focus')) or 'нет')+'.', '',
                    'Прямые продолжения: '+(', '.join(other for other,groups in parents.items() if any(fid in g for g in groups)) or 'нет')+'.', '',
                    'Точные награды (completion_reward), доступность, обход, AI и остальные поля:', '']+fence([('focus',f,'=')])
    decisions = load('common/decisions/MKN_military_decisions.txt')
    out += ['## Тактики и штабные проекты', '']
    decision_count = 0
    for category,body,_ in decisions:
        if not isinstance(body,list):
            continue
        out += [f'### {ru.get(category,category)} — `{category}`','']
        for did,decision,op in body:
            if not isinstance(decision,list):
                continue
            decision_count += 1
            out += [f'#### {ru.get(did,did)} — `{did}`','',f'EN: {en.get(did,did)}.','',ru.get(did+'_desc',''),'','Оплата, сроки, focus-gates, награды, возврат при отмене и правила региона:','']+fence([(did,decision,op)])
    all_docs = [fs[fid] for fid in context]+[decisions]
    out += ['## Опорные определения механик', '']
    supporting = ['common/decisions/categories/MKN_military_categories.txt','common/dynamic_modifiers/nww_dynamic_modifiers.txt','common/scripted_effects/nww_mkn_progression.txt','common/on_actions/nww_mkn_progression.txt','common/on_actions/MKN_international_on_actions.txt','common/ideas/MKN_ideas.txt','common/ideas/MKN_international_ideas.txt','history/countries/MKN - Makhnovists.txt','history/units/MKN_1936.txt','history/units/MKN_black_guard.txt','history/units/MKN_black_guard_oob.txt']
    supporting += [p.relative_to(ROOT).as_posix() for p in (ROOT/'common/technologies').glob('*MKN*') if p.is_file()]
    for path in supporting:
        if not (ROOT/path).is_file():
            continue
        doc = load(path)
        if path.startswith('common/dynamic_modifiers'):
            doc = [(k,v,o) for k,v,o in doc if k and k.startswith('MKN_')]
        all_docs.append(doc)
        out += [f'### `{path}`','']+fence(doc)
    out += ['## Предприятия, MIO, советники и характеристики', '']
    for folder in ('common/military_industrial_organization/organizations','common/ideas','common/country_leader','common/characters'):
        for path in sorted((ROOT/folder).glob('*.txt')):
            rel = path.relative_to(ROOT).as_posix()
            if rel in supporting or ('mkn' not in path.name.lower() and path.name not in ('nww_organizations.txt','nww_companies.txt')):
                continue
            doc = read(path)
            if path.name in ('nww_organizations.txt','nww_companies.txt'):
                candidates = list(doc)
                for group in values(doc,'ideas'):
                    candidates += [item for _,entries,_ in group if isinstance(entries,list) for item in entries]
                doc = [(k,v,o) for k,v,o in candidates if k and k.startswith('MKN_')]
            if not doc:
                continue
            sources.add(rel); all_docs.append(doc)
            out += [f'### `{rel}`','']+fence(doc)
    helpers = {}
    for path in (ROOT/'common/scripted_effects').glob('*.txt'):
        if 'mkn' in path.name.lower():
            helpers.update({k:(path.relative_to(ROOT).as_posix(),[(k,v,o)]) for k,v,o in read(path)})
    for path in (ROOT/'common/scripted_triggers').glob('*.txt'):
        if 'mkn' in path.name.lower():
            helpers.update({k:(path.relative_to(ROOT).as_posix(),[(k,v,o)]) for k,v,o in read(path)})
    done = {k for doc in all_docs for k,v,o in doc if k in helpers}
    out += ['## Вызываемые scripted effects и triggers','']
    while True:
        needed = {k for doc in all_docs for k,v,o in walk(doc) if k in helpers}-done
        if not needed:
            break
        for key in sorted(needed):
            path,doc = helpers[key]; done.add(key); sources.add(path); all_docs.append(doc)
            out += [f'### `{key}` — `{path}`','']+fence(doc)
    out += ['## Структура программ и примечания к переработке','']
    for path in ('docs/MKN_military_programs.json','docs/MKN_military_refactor.md'):
        sources.add(path)
        out += [f'### `{path}`','', '```'+('json' if path.endswith('.json') else 'text'),(ROOT/path).read_text().rstrip(),'```','']
    referenced = {v for doc in all_docs for k,v,o in walk(doc) if isinstance(v,str) and v in ru}
    referenced.update(k for doc in all_docs for k,v,o in walk(doc) if k in ru)
    out += ['## Локализация подсказок, духов и решений','', '```json',json.dumps({k:{'ru':ru[k],'en':en.get(k)} for k in sorted(referenced) if k not in fs},ensure_ascii=False,indent=2),'```','',
            '## Воспроизводимость','', 'Обновление: `python tools/export_mkn_military_focuses.py`. Источником истины служат текущие скрипты. Текст change notes приведён как контекст; при расхождении приоритет у определений. SHA-256 исходников:','', '```text']
    sources.update({'tools/export_mkn_military_focuses.py','tools/export_mkn_industrial_focuses.py','tools/hoi4_script.py'})
    out += [f'{sha256((ROOT/p).read_bytes()).hexdigest()}  {p}' for p in sorted(sources)]+['```','']
    output.write_text('\n'.join(out),encoding='utf-8')
    print(f'{output}: '+', '.join(f'{name}={len(ids)}' for name,ids in services.items())+f'; related={len(supplemental)}; prerequisites={len(context-selected)}; decisions={decision_count}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'docs/MKN_MILITARY_FOCUSES_FOR_AI.md')
    export(parser.parse_args().output)
