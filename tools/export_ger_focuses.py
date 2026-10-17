"""Export every playable NWW German focus and linked mechanics for external review."""
import argparse
from decimal import Decimal
from hashlib import sha256
import json
from pathlib import Path
import re

from export_mkn_industrial_focuses import script
from hoi4_script import read, one, values, walk, tree_focuses

ROOT = Path(__file__).resolve().parents[1]


def export(output, snapshot_date):
    sources = set()
    def load(path):
        sources.add(path)
        return read(ROOT/path)
    def fence(doc):
        return ['```pdx',script(doc),'```','']
    locales = {}
    for lang in ('russian','english'):
        entries = {}
        paths = sorted(ROOT.glob(f'localisation/**/*l_{lang}.yml'))
        # replace overrides ordinary localisation; retain its actual precedence.
        paths.sort(key=lambda p: ('replace' in p.relative_to(ROOT).parts,p.as_posix()))
        for path in paths:
            pairs = re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$',path.read_text(encoding='utf-8-sig'),re.M)
            entries.update(pairs)
            if any(k.lower().startswith(('ger_','ger.','ger_crisis','ger_news','nww_ger')) for k,_ in pairs):
                sources.add(path.relative_to(ROOT).as_posix())
        locales[lang] = entries
    ru,en = locales['russian'],locales['english']
    tree = one(load('common/national_focus/GER_focuses.txt'),'focus_tree')
    expanded = tree_focuses(tree,ROOT/'common/national_focus')
    fs = {one(f,'id'):f for f in expanded}
    assert len(fs)==len(expanded),'Duplicate playable focus IDs'
    parents = {fid:[values(p,'focus') for p in values(f,'prerequisite')] for fid,f in fs.items()}
    origins = {}
    for path in sorted((ROOT/'common/national_focus').glob('*.txt')):
        doc = read(path)
        direct = values(doc,'shared_focus')+[f for t in values(doc,'focus_tree') for f in values(t,'focus')]
        for f in direct:
            fid = one(f,'id')
            if fid in fs and f==fs[fid]:
                origins[fid] = path.relative_to(ROOT).as_posix()
    assert origins.keys()==fs.keys()
    missing = {lang:[k for fid in fs for k in (fid,fid+'_desc') if k not in locales[lang]] for lang in locales}
    assert not any(missing.values()),missing
    industry_path = 'docs/GER_industry_rework.json'
    sources.add(industry_path)
    industry = set(json.loads((ROOT/industry_path).read_text())['focuses'])
    assert industry <= fs.keys()
    political = {fid for fid,path in origins.items() if path.endswith('/GER_political.txt')}
    def descendants(entry):
        found = {entry}
        while True:
            new = found | {fid for fid,groups in parents.items() if any(p in found for g in groups for p in g)}
            if new==found:
                return found & political
            found=new
    paths = {
        'Авторитарный путь / Железный кайзеррейх':descendants('GER_the_potsdam_coup'),
        'Демократический путь / Парламентская весна':descendants('GER_parliamentary_spring'),
        'Пангерманский путь':descendants('GER_the_pan_germanic_triumph'),
        'Спартакистский путь':descendants('GER_the_spartacist_uprising'),
    }
    groups = {'Общее политическое начало':political-set.union(*paths.values()),**paths,
              'Промышленность, наука, торговля и разведка':industry,
              'Прочие военные и государственные фокусы':fs.keys()-political-industry}
    assert set.union(*(set(ids) for ids in groups.values()))==fs.keys()
    assert sum(map(len,groups.values()))==len(fs)
    compatibility = load('common/national_focus/GER_native_compatibility.txt')
    compat_ids = [one(f,'id') for f in values(compatibility,'shared_focus')]
    def ordered(ids):
        return sorted(ids,key=lambda fid:(int(one(fs[fid],'y','0')),int(one(fs[fid],'x','0')),fid))
    out = ['# Германия (GER): все фокусы NWW Reborn — пакет для другой нейросети','',
           f'Дата снимка: **{snapshot_date}**. Источник — текущие игровые скрипты проекта. Самодостаточный файл содержит названия и описания RU/EN, награды, условия, зависимости, взаимоисключения, события, решения, духи, BoP и восстановление сохранений. Игровые файлы при экспорте не меняются.','',
           f'Игровое дерево `{one(tree,"id")}`: **{len(fs)} фокуса** — {len(political)} политических, {len(industry)} промышленных/научных/разведывательных и {len(fs)-len(political)-len(industry)} прочих военных/государственных. Число direct-focus: {len(values(tree,"focus"))}; импортированных shared-focus: {len(fs)-len(values(tree,"focus"))}.','',
           '## Контекст и правила для улучшения','',
           '- Первая мировая война не происходила. Германия 1936 года — старая имперская гегемония с внутренним застоем и внешними обязательствами. Не возвращать ванильную историю послевоенной Германии.','- Сохранять существующие focus/event IDs, компромисс LTB и его преемников. GER_1–GER_10 — действующие импортированные фокусы, включённые в каталог, а не удалённые заглушки.','- cost — недели: 5 = 35 дней, 10 = 70 дней; cost=0 у событийного узла не означает свободный обычный фокус. available/bypass и событие определяют его выполнение.','- prerequisite: разные блоки соединяются И; несколько focus внутри одного блока — ИЛИ. available добавляет ограничения; mutually_exclusive исключает альтернативу. Полные allow_branch, bypass и AI-поля сохранены ниже.','- До 1 января 1939 года сохранять универсальные восточные ограничения против LTB, POL, UKR, MKN и SOV, включая события, решения и объявления войны. Исторические AI-ограничения могут быть строже общих; проверять оба уровня.','- Исторические даты из старых заметок — расчётные ориентиры, не наблюдение игры. Текущие условия и планы AI ниже являются источником для анализа.','- Кайзерский австрийский ультиматум имеет отдельный нижний временной порог. Не считать отсутствие восточного тега разрешением игнорировать австрийские условия.','- Германия не должна начинать с Осью. Не активировать MEFO, conquest-economy debt, продление векселей и штрафы погашения. Старые сохранения имеют защищённую очистку.','- Промышленность развивает один постоянный динамический дух GER_nww_industrial_program. Повторный пересчёт параметров не должен повторять фабрики, ресурсы, технику и слоты исследований.','- Параметры приведены в сырых единицах движка: factor=0.05 обычно означает 5 процентных пунктов; political_power_gain — плоский прирост в сутки. Не переводить все числа автоматически в проценты.','- if/limit/else, DLC, контроль/владение, субъектность и согласие получателя ограничивают выдачу. Не суммировать альтернативные награды как гарантированные. custom_effect_tooltip и show_mio_tooltip сами не выдают награду.','- Колониальные награды требуют фактического владения/контроля. Сохранять 19 заморских регионов из GER_overseas_setup.json и местные ядра; не выдавать германские колониальные ядра.','- Родные ванильные заглушки совместимости не импортированы и не входят в число игровых фокусов. Контент для Германии принадлежит GER; двусторонние богемские определения имеют документированного владельца GER.','- Это статический снимок. Проверки синтаксиса не заменяют новую кампанию, фактические tooltips и свежий лог игры.','',
           '## Сводный список','', '| Раздел | Название | ID | Дней |','| --- | --- | --- | --- |']
    for title,ids in groups.items():
        for fid in ordered(ids):
            out += [f'| {title} | {ru[fid]} | `{fid}` | {Decimal(one(fs[fid],"cost","10"))*7} |']
    out += ['']
    all_docs = list(fs.values())
    for title,ids in groups.items():
        out += [f'## {title} — {len(ids)}','']
        for fid in ordered(ids):
            f=fs[fid]; path=origins[fid]; sources.add(path)
            text=(ROOT/path).read_text(encoding='utf-8-sig')
            match=re.search(r'\bid\s*=\s*'+re.escape(fid)+r'\b',text)
            line=text[:match.start()].count('\n')+1
            gates={v for k,v,_ in walk(one(f,'available',[])) if k=='has_completed_focus'}
            out += [f'### {ru[fid]} — `{fid}`','',f'EN: {en[fid]}.','',f'Описание RU: {ru[fid+"_desc"]}','',f'Описание EN: {en[fid+"_desc"]}','',
                    f'Источник: `{path}:{line}`. Стоимость: {one(f,"cost","10")} ({Decimal(one(f,"cost","10"))*7} дней). Координаты: x={one(f,"x")}, y={one(f,"y")}. Иконка: `{one(f,"icon")}`.','',
                    'Предпосылки: '+(' И '.join('('+' ИЛИ '.join(f'{ru.get(p,p)} [{p}]' for p in g)+')' for g in parents[fid]) or 'нет нарисованной предпосылки; см. available')+'.','',
                    'Взаимоисключения: '+(', '.join(p for g in values(f,'mutually_exclusive') for p in values(g,'focus')) or 'нет')+'.','',
                    'Дополнительные focus-gates в available (полная логика OR/NOT ниже): '+(', '.join(sorted(gates)) or 'нет')+'.','',
                    'Прямые продолжения: '+(', '.join(other for other,ps in parents.items() if any(fid in g for g in ps)) or 'нет')+'.','',
                    'Обзор возможной награды; условия и области действия сохранены в полном коде:','']
            facts=[]
            for k,v,_ in walk(one(f,'completion_reward',[])):
                if k=='add_to_variable':
                    facts += [f'Параметр `{var}`: {amount}' for var,amount,_ in v if var!='tooltip']
                elif k in ('set_politics','add_tech_bonus','add_timed_idea','country_event','news_event','create_wargoal','add_building_construction','add_offsite_building','add_power_balance_value','set_power_balance_value','add_resource','start_civil_war','add_dynamic_modifier') and isinstance(v,list):
                    facts.append(f'`{k}`: '+script(v).replace('\n','; '))
                elif k in ('add_political_power','add_stability','add_war_support','army_experience','navy_experience','air_experience','add_manpower','add_ideas','remove_ideas','remove_power_balance','set_country_flag','add_research_slot') and isinstance(v,str):
                    facts.append(f'`{k}`: {v}')
            out += [f'- {fact}' for fact in facts or ['Награда вызывает вспомогательные эффекты: см. completion_reward и раздел определений.']]+['','Полное определение фокуса:','']+fence([('focus',f,'=')])
    out += ['## Настройка дерева и непрерывных фокусов','']+fence([('focus_tree',[(k,v,o) for k,v,o in tree if k!='focus'],'=')])
    out += ['## Связанные системы Германии','', 'Стартовые и автоматические эффекты приведены как контекст; их нельзя считать наградой каждого фокуса.','']
    supporting=[]
    for folder in ('common/bop','common/decisions','common/decisions/categories','common/ideas','common/dynamic_modifiers','common/country_leader','common/characters','common/on_actions','common/scripted_effects','common/scripted_triggers','common/operations','common/ai_strategy','common/ai_strategy_plans','common/factions/templates','common/diplomatic_actions','common/country_rules','events','history/countries'):
        supporting += [p.relative_to(ROOT).as_posix() for p in sorted((ROOT/folder).glob('*.txt')) if p.name.lower().startswith(('ger','nww_ger'))]
    for path in dict.fromkeys(supporting):
        doc=load(path); all_docs.append(doc)
        out += [f'### `{path}`','']+fence(doc)
    # Resolve project helpers and bilateral event chains outside country-owned files.
    definitions={}
    for folder in ('common/scripted_effects','common/scripted_triggers'):
        for path in sorted((ROOT/folder).glob('*.txt')):
            definitions.update({k:(path.relative_to(ROOT).as_posix(),[(k,v,o)]) for k,v,o in read(path)})
    for path in sorted((ROOT/'events').glob('*.txt')):
        for k,v,o in read(path):
            if k in ('country_event','news_event'):
                definitions[one(v,'id')]=(path.relative_to(ROOT).as_posix(),[(k,v,o)])
    for path in sorted((ROOT/'common/ideas').glob('*.txt')):
        for groups_node in values(read(path),'ideas'):
            for _,group,_ in groups_node:
                if isinstance(group,list):
                    for k,v,o in group:
                        if isinstance(v,list):
                            definitions.setdefault(k,(path.relative_to(ROOT).as_posix(),[(k,v,o)]))
    done={k for doc in all_docs for k,v,o in doc if k in definitions}
    done.update(one(v,'id') for doc in all_docs for k,v,o in doc if k in ('country_event','news_event'))
    done.update(k for doc in all_docs for group in values(doc,'ideas') for _,items,_ in group if isinstance(items,list) for k,v,o in items if k in definitions)
    out += ['## Вызываемые внешние эффекты, события и духи','']
    while True:
        needed={k for doc in all_docs for k,v,o in walk(doc) if k in definitions}
        needed.update(v for doc in all_docs for k,v,o in walk(doc) if isinstance(v,str) and v in definitions and (k in ('has_idea','add_ideas','remove_ideas','swap_ideas','add_idea','remove_idea') or k is None))
        needed.update(one(v,'id') for doc in all_docs for k,v,o in walk(doc) if k in ('country_event','news_event') and isinstance(v,list))
        needed.update(one(v,'idea') for doc in all_docs for k,v,o in walk(doc) if k=='add_timed_idea' and isinstance(v,list))
        needed=(needed & definitions.keys())-done
        if not needed:
            break
        for key in sorted(needed):
            path,doc=definitions[key]; sources.add(path); done.add(key); all_docs.append(doc)
            out += [f'### `{key}` — `{path}`','']+fence(doc)
    out += ['## Регионы, используемые наградами, и заморский старт','', 'История региона содержит начальные и датированные записи. Условная награда в регионе не означает, что Германия владеет им в начале игры.','']
    state_ids={k for fid in fs for k,v,o in walk(one(fs[fid],'completion_reward',[])) if k and k.isdigit() and isinstance(v,list)}
    state_ids.update(k for doc in all_docs for k,v,o in walk(doc) if k and k.isdigit() and isinstance(v,list) and len(k)<5)
    for path in sorted((ROOT/'history/states').glob('*.txt')):
        state=one(read(path),'state')
        if one(state,'id') in state_ids:
            rel=path.relative_to(ROOT).as_posix(); sources.add(rel)
            out += [f'### `{rel}`','']+fence([('state',state,'=')])
    for path in ('docs/GER_overseas_setup.json','docs/GER_industry_rework.json'):
        sources.add(path)
        out += [f'### `{path}`','', '```json',(ROOT/path).read_text().rstrip(),'```','']
    out += ['## Неигровая совместимость с ванильными ID','',
            f'В `GER_native_compatibility.txt` определено {len(compat_ids)} неимпортированных shared_focus. Это заглушки для внешних ссылок, не дополнительные ветки. В дереве GER_focus их нет.','', '```text','\n'.join(compat_ids),'```','']
    referenced={v for doc in all_docs for k,v,o in walk(doc) if isinstance(v,str) and v in ru}
    referenced.update(k for doc in all_docs for k,v,o in walk(doc) if k in ru)
    referenced.update(k+'_desc' for k in tuple(referenced) if k+'_desc' in ru)
    out += ['## Локализация духов, диапазонов BoP, решений, событий и ответов','', '```json',json.dumps({k:{'ru':ru[k],'en':en.get(k)} for k in sorted(referenced) if k not in fs},ensure_ascii=False,indent=2),'```','',
            '## Воспроизводимость','', 'Повторный экспорт: `python tools/export_ger_focuses.py --snapshot-date YYYY-MM-DD`. В каталоге фокусов только прямые definitions и shared_focus, действительно импортированные в GER_focus. SHA-256 источников:','', '```text']
    sources.update({'tools/export_ger_focuses.py','tools/export_mkn_industrial_focuses.py','tools/hoi4_script.py'})
    out += [f'{sha256((ROOT/p).read_bytes()).hexdigest()}  {p}' for p in sorted(sources)]+['```','']
    output.write_text('\n'.join(out),encoding='utf-8')
    print(f'{output}: {len(fs)} focuses; political={len(political)}, industry/intelligence={len(industry)}, other={len(fs)-len(political)-len(industry)}')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'docs/GER_ALL_FOCUSES_FOR_AI.md')
    parser.add_argument('--snapshot-date',default='2026-10-17')
    args=parser.parse_args()
    export(args.output,args.snapshot_date)
