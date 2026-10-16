"""Export current MKN politics and their supporting mechanics for external review."""
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
        return ['```pdx',script(doc),'```','']
    locales = {}
    for lang in ('russian','english'):
        locales[lang] = {}
        for path in sorted(ROOT.glob(f'localisation/**/*l_{lang}.yml')):
            pairs = re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$',path.read_text(encoding='utf-8-sig'),re.M)
            locales[lang].update(pairs)
            if any(k.lower().startswith(('mkn_','mkn.')) for k,_ in pairs):
                sources.add(path.relative_to(ROOT).as_posix())
    ru,en = locales['russian'],locales['english']
    tree = one(load('common/national_focus/MKN.txt'),'focus_tree')
    fs = {one(f,'id'):f for f in tree_focuses(tree,ROOT/'common/national_focus')}
    parents = {fid:[values(p,'focus') for p in values(f,'prerequisite')] for fid,f in fs.items()}
    def descendants(entry):
        found = {entry}
        while True:
            expanded = found | {fid for fid,groups in parents.items() if any(p in found for g in groups for p in g)}
            if expanded == found:
                return found
            found = expanded
    primary = descendants('MKN_congress_1936')
    groups = {}
    for name,entry in (
        ('Милитаристы','MKN_military_takes_charge'),
        ('Вольные советы / синдикалисты','MKN_triumph_of_free_soviets'),
        ('Аграрии','MKN_peasant_delegates'),
        ('Ревком / коммунисты','MKN_emergency_revkom'),
        ('Общий Чёрный интернационал и внешняя политика','MKN_black_international'),
    ):
        groups[name] = descendants(entry)
    covered = set.union(*groups.values())
    groups = {'Общее начало и преемственность':primary-covered,**groups}
    integration = descendants('MKN_ukrainian_communes_congress') if 'MKN_ukrainian_communes_congress' in fs else set()
    if integration:
        groups['Связанное послевоенное устройство украинских коммун'] = integration
    selected = primary | integration
    context = set(selected)
    while True:
        expanded = context | {p for fid in context for g in parents[fid] for p in g}
        expanded.update(v for fid in context for k,v,_ in walk(one(fs[fid],'available',[])) if k=='has_completed_focus' and v in fs)
        if expanded == context:
            break
        context = expanded
    if context-selected:
        groups['Контекст внешних предпосылок'] = context-selected
    origins = {}
    for path in sorted((ROOT/'common/national_focus').glob('*.txt')):
        doc = read(path)
        nodes = values(doc,'shared_focus')+[f for t in values(doc,'focus_tree') for f in values(t,'focus')]
        for f in nodes:
            fid = one(f,'id')
            if fid in context and f == fs[fid]:
                origins[fid] = path.relative_to(ROOT).as_posix()
    assert set.union(*groups.values()) == context
    assert sum(map(len,groups.values())) == len(context),'Duplicate focus cards'
    assert all(fid in ru and fid+'_desc' in ru and fid in en and fid+'_desc' in en for fid in selected),'Missing focus localization'
    def ordered(ids):
        return sorted(ids,key=lambda fid:(int(one(fs[fid],'y','0')),int(one(fs[fid],'x','0')),fid))
    out = ['# MKN: политические фокусы — пакет для другой нейросети','',
           'Снимок текущих файлов NWW Reborn на 16 октября 2026 года. Содержит названия и описания RU/EN, условия, точные награды, взаимоисключения, события, решения, баланс сил и восстановление сохранений. Документ описывает действующее содержимое и не меняет механику.','',
           f'Основной политический блок: **{len(primary)} фокусов**, включая общий конгресс, четыре политических пути и Чёрный интернационал. Отдельный связанный блок устройства украинских коммун: **{len(integration)}**. Контекст внешних предпосылок: **{len(context-selected)}**.','',
           '## Контекст для анализа','',
           '- Первая мировая война не происходила. Сохранять существующие focus/event IDs, компромисс и преемников LTB, действующий лор. Архивные и скрытые совместимые фокусы не считаются отдельными доступными путями.','- cost — недели: 5 = 35 дней, 10 = 70 дней. Несколько prerequisite-блоков соединяются И; несколько focus в одном блоке — ИЛИ. available добавляет условия; mutually_exclusive исключает другой путь.','- Условия allow_branch, bypass, отмены и продолжения фокуса приведены в полном определении. has_completed_focus в available не рисует стрелку, но остаётся игровым ограничением.','- Дата смерти Махно, кризис, дедлайн и гражданская война определяются событиями и миссией, а не суммой длительностей дерева. Событийный фокус нельзя считать обычным выбираемым узлом.','- Политические входы требуют мандата популярности и подготовительных условий; способы набора поддержки находятся в решениях. Точные пороги и затраты читать в коде, не переносить из старых описаний.','- Национальные ideology groups и их локализованные названия для MKN различаются. Проверять реальные ruling_party и party_popularity, а не только название в интерфейсе.','- Сохранять единые постоянные экономический и служебные духи; значения add_to_variable складываются с прежними ступенями. Сырые факторы 0.05 обычно означают 5 процентных пунктов; политическая власть в день — плоская величина.','- if/limit/else, DLC, поддержка партии, субъектность, контроль и согласие адресата могут ограничивать выдачу. Внешнее предложение не означает автоматического принятия. custom_effect_tooltip сам не выдаёт награду.','- Баланс сил имеет нативную шкалу от −1 до +1. Модификаторы диапазона, блокировка, удаление и восстановление BoP описаны в соответствующих определениях ниже.','- Монарх Махно и его портрет сохраняются для соответствующего контента и сохранений. Коммунистическое ограничение его военных ролей не следует переносить на монархическую роль. Событийная смена лидера после смерти имеет отдельную логику.','- Восстановление сохранений не должно повторять фабрики, смену режима, дипломатию или запуск кризисного таймера. Текущее восстановление включено ниже.','- Это статический экспорт. Окончательная проверка изменений требует новой кампании, проверки tooltip и свежего game log.','',
           '## Сводный список','', '| Раздел | Фокус | ID | Дней |','| --- | --- | --- | --- |']
    for title,ids in groups.items():
        for fid in ordered(ids):
            out += [f'| {title} | {ru.get(fid,fid)} | `{fid}` | {Decimal(one(fs[fid],"cost","10"))*7} |']
    out += ['']
    all_docs = [fs[fid] for fid in context]
    for title,ids in groups.items():
        out += [f'## {title} — {len(ids)} фокусов','']
        for fid in ordered(ids):
            f = fs[fid]; path = origins[fid]; sources.add(path)
            source = (ROOT/path).read_text(encoding='utf-8-sig')
            match = re.search(r'\bid\s*=\s*'+re.escape(fid)+r'\b',source)
            line = source[:match.start()].count('\n')+1
            out += [f'### {ru.get(fid,fid)} — `{fid}`','',f'EN: {en.get(fid,fid)}.','',f'Описание RU: {ru.get(fid+"_desc","")}','',f'Описание EN: {en.get(fid+"_desc","")}','',
                    f'Источник: `{path}:{line}`. Стоимость: {one(f,"cost","10")} ({Decimal(one(f,"cost","10"))*7} дней). Координаты: x={one(f,"x")}, y={one(f,"y")}.','',
                    'Предпосылки: '+(' И '.join('('+' ИЛИ '.join(f'{ru.get(p,p)} [{p}]' for p in g)+')' for g in parents[fid]) or 'нет нарисованной предпосылки; см. available')+'.','',
                    'Взаимоисключения: '+(', '.join(p for g in values(f,'mutually_exclusive') for p in values(g,'focus')) or 'нет')+'.','',
                    'Прямые продолжения: '+(', '.join(other for other,ps in parents.items() if any(fid in g for g in ps)) or 'нет')+'.','',
                    'Обзор наград (может быть условным; точная область действия и ограничения — в коде):','']
            facts = []
            for k,v,_ in walk(one(f,'completion_reward',[])):
                if k=='add_to_variable':
                    facts += [f'Параметр `{var}`: {amount}' for var,amount,_ in v if var!='tooltip']
                elif k in ('set_politics','add_tech_bonus','add_timed_idea','country_event','news_event','create_wargoal','add_building_construction','add_offsite_building','add_power_balance_value','set_power_balance_value') and isinstance(v,list):
                    facts.append(f'`{k}`: '+script(v).replace('\n','; '))
                elif k in ('add_political_power','add_stability','add_war_support','army_experience','add_manpower','add_ideas','remove_power_balance','set_country_flag') and isinstance(v,str):
                    facts.append(f'`{k}`: {v}')
            out += [f'- {fact}' for fact in facts or ['Вызываемые эффекты и полная награда приведены ниже.']]+['','Полное определение:','']+fence([('focus',f,'=')])
    supporting = [
        'common/characters/nww_MKN.txt','common/characters/MKN_eugen.txt','common/ideas/MKN_horizons_ideas.txt','common/ideas/nww_MKN_ideas.txt',
        'common/bop/MKN_bop.txt','common/decisions/MKN_decisions.txt','common/decisions/MKN_bop_decisions.txt','common/decisions/MKN_international_decisions.txt','common/decisions/MKN_foreign_decisions.txt','common/decisions/MKN_horizons_decisions.txt','common/decisions/MKN_ukraine_integration_decisions.txt',
        'common/ideas/MKN_ideas.txt','common/ideas/MKN_international_ideas.txt','common/dynamic_modifiers/nww_dynamic_modifiers.txt','common/scripted_effects/nww_mkn_progression.txt','common/on_actions/nww_mkn_progression.txt','common/characters/MKN.txt','history/countries/MKN - Makhnovists.txt','common/ai_strategy_plans/MKN_historical.txt','common/scripted_localisation/MKN_ideology_names.txt',
    ]
    for folder in ('common/decisions/categories','common/on_actions'):
        supporting += [p.relative_to(ROOT).as_posix() for p in sorted((ROOT/folder).glob('*MKN*')) if p.is_file() and (folder.endswith('categories') and any(t in p.name.lower() for t in ('bop','international','foreign','horizons','ukraine','mkn_categories')) or folder.endswith('on_actions') and any(t in p.name.lower() for t in ('overhaul','diplomacy','international','horizons','intervention','ukraine','flag','ai')))]
    out += ['## Баланс сил, решения, стартовая политика и автоматические события','', 'Полные определения сохраняют стоимость, видимость, доступность, сроки миссий и периодичность. Стартовые идеи и переменные даны как контекст; не все описанные здесь эффекты выдаются политическими фокусами.','']
    for path in dict.fromkeys(supporting):
        if not (ROOT/path).is_file():
            continue
        doc = load(path)
        if path.startswith('common/dynamic_modifiers'):
            doc = [(k,v,o) for k,v,o in doc if k and k.startswith('MKN_')]
        all_docs.append(doc)
        out += [f'### `{path}`','']+fence(doc)
    # Follow script calls and event chains to a fixed point, preserving duplicate keys.
    definitions = {}
    for folder in ('common/scripted_effects','common/scripted_triggers'):
        for path in sorted((ROOT/folder).glob('*.txt')):
            if 'mkn' not in path.name.lower():
                continue
            definitions.update({k:(path.relative_to(ROOT).as_posix(),[(k,v,o)]) for k,v,o in read(path)})
    for path in sorted((ROOT/'events').glob('*.txt')):
        for key,body,op in read(path):
            if key in ('country_event','news_event'):
                definitions[one(body,'id')] = (path.relative_to(ROOT).as_posix(),[(key,body,op)])
    done = {k for doc in all_docs for k,v,o in doc if k in definitions}
    out += ['## События, выборы ответа, scripted effects и triggers','', 'Цепочки включают предложения другим странам и их ответы. Не считать награду предложения гарантированным положительным ответом.','']
    while True:
        needed = {k for doc in all_docs for k,v,o in walk(doc) if k in definitions}
        needed.update(one(v,'id') for doc in all_docs for k,v,o in walk(doc) if k in ('country_event','news_event') and isinstance(v,list))
        needed = (needed & definitions.keys())-done
        if not needed:
            break
        for key in sorted(needed):
            path,doc = definitions[key]; sources.add(path); done.add(key); all_docs.append(doc)
            out += [f'### `{key}` — `{path}`','']+fence(doc)
    referenced = {v for doc in all_docs for k,v,o in walk(doc) if isinstance(v,str) and v in ru}
    referenced.update(k for doc in all_docs for k,v,o in walk(doc) if k in ru)
    # Include localized descriptions for ideas, event text, choices, and decision IDs.
    referenced.update(k+'_desc' for k in tuple(referenced) if k+'_desc' in ru)
    out += ['## Локализация духов, решений, событий и ответов','', '```json',json.dumps({k:{'ru':ru[k],'en':en.get(k)} for k in sorted(referenced) if k not in fs},ensure_ascii=False,indent=2),'```','',
            '## Воспроизводимость','', 'Обновить файл: `python tools/export_mkn_political_focuses.py`. Разворачиваются только действующие direct/shared_focus; ID событий и провинций не превращаются в фокусы. SHA-256 источников:','', '```text']
    sources.update({'tools/export_mkn_political_focuses.py','tools/export_mkn_industrial_focuses.py','tools/hoi4_script.py'})
    out += [f'{sha256((ROOT/p).read_bytes()).hexdigest()}  {p}' for p in sorted(sources)]+['```','']
    output.write_text('\n'.join(out),encoding='utf-8')
    print(f'{output}: core={len(primary)}, integration={len(integration)}, prerequisite context={len(context-selected)}, linked definitions={len(done)}')


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'docs/MKN_POLITICAL_FOCUSES_FOR_AI.md')
    export(parser.parse_args().output)
