"""Apply the Austrian campaign sequence and a resolvable British crown crisis."""
from copy import deepcopy
import json
from pathlib import Path
from hoi4_script import read, one, values, parse, dump, quoted

ROOT = Path(__file__).resolve().parents[1]


def save(path, doc):
    (ROOT / path).write_text(dump(doc)+'\n', encoding='utf-8', newline='\n')


def repair_austria():
    doc = read(ROOT/'common/national_focus/AUS_focuses.txt')
    fs = {one(f,'id'):f for f in values(one(doc,'focus_tree'),'focus')}
    gate = one(fs['AUS_war_with_croatia'],'available')
    if not any(k=='AUS_nww_can_prepare_croatia' for k,v,o in gate):
        gate += parse('AUS_nww_can_prepare_croatia = yes')
    save('common/national_focus/AUS_focuses.txt',doc)
    doc = read(ROOT/'common/scripted_effects/AUS_effects.txt')
    gate = one(one(one(doc,'nww_AUS_prepare_cro_campaign'),'if'),'limit')
    if not any(k=='AUS_nww_can_prepare_croatia' for k,v,o in gate):
        gate += parse('AUS_nww_can_prepare_croatia = yes')
    save('common/scripted_effects/AUS_effects.txt',doc)
    doc = read(ROOT/'common/on_actions/AUS_on_actions.txt')
    rules = values(one(one(one(doc,'on_actions'),'on_capitulation'),'effect'),'if')
    hun = next(r for r in rules if one(one(r,'limit'),'tag')=='HUN')
    effect = one(hun,'FROM')
    if not any(k=='set_country_flag' and isinstance(v,list) and one(v,'flag')=='AUS_nww_hungarian_recovery' for k,v,o in effect):
        effect += parse('set_country_flag = { flag = AUS_nww_hungarian_recovery days = 30 }')
    save('common/on_actions/AUS_on_actions.txt',doc)
    doc = read(ROOT/'history/units/AUS_1936_nww.txt')
    units = one(doc,'units');divs = values(units,'division')
    # Nine additional equipped infantry divisions; reuse the country's valid garrisons.
    if len(divs) in (12,18):
        infantry = next(d for d in divs if one(d,'division_template')=='Infanterie Division')
        for number in range(len(divs)+1,28):
            base=divs[(number-1)%len(divs)]
            d=deepcopy(infantry)
            d[:]=[(k,f'{number}. Infanterie Division' if k=='name' else one(base,'location') if k=='location' else v,o) for k,v,o in d]
            units.append(('division',d,'='))
    assert len(values(units,'division'))==27
    save('history/units/AUS_1936_nww.txt',doc)
    path=ROOT/'docs/1936_deployment_manifest.json'
    data=json.loads(path.read_text(encoding='utf-8'))
    data['AUS_1936_nww.txt']['divisions']=27
    data['AUS_1936_nww.txt']['positions']=len({one(d,'location') for d in values(units,'division')})
    path.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')


def repair_crown():
    path=ROOT/'events/ENG_events.txt'
    doc=read(path)
    event=next(e for k,e,o in doc if k=='country_event' and one(e,'id')=='nww_eng.31')
    options=values(event,'option')
    for option in options:
        name=one(option,'name')
        option[:]=parse('name = '+name+' ai_chance = { factor = '+('0 modifier = { add = 65 is_historical_focus_on = no }' if name.endswith('.a') else '100')+' } '+('remove_ideas = ENG_king_edward add_ideas = ENG_nww_constitutional_edward' if name.endswith('.a') else 'remove_ideas = ENG_king_edward add_ideas = ENG_george_vi')+' set_country_flag = ENG_nww_crown_settled add_stability = 0.05')
    trigger=one(event,'trigger')
    trigger[:]=parse('tag = ENG has_focus_tree = ENG_nww_focus date > 1936.12.1 has_idea = ENG_king_edward NOT = { has_government = communism }')
    save('events/ENG_events.txt',doc)
    # The revisit event deliberately has a new ID; fire_only_once event 31 cannot
    # reopen a crisis in old saves where the former keep-Edward option already ran.
    revisit=deepcopy(event)
    revisit[:]=[(k,'nww_eng_crown.1' if k=='id' else v,o) for k,v,o in revisit if k not in ('fire_only_once','trigger','mean_time_to_happen')]
    revisit += parse('is_triggered_only = yes trigger = { tag = ENG has_focus_tree = ENG_nww_focus has_idea = ENG_king_edward NOT = { has_government = communism } }')
    save('events/ENG_crown_events.txt',parse('add_namespace = nww_eng_crown')+[('country_event',revisit,'=')])
    # Remove the resolved royal spirit on the existing republican transition too.
    path=ROOT/'common/scripted_effects/ENG_effects.txt'
    text=path.read_text(encoding='utf-8-sig')
    if 'remove_ideas = ENG_nww_constitutional_edward' not in text:
        text=text.replace('remove_ideas = ENG_george_vi','remove_ideas = ENG_george_vi remove_ideas = ENG_nww_constitutional_edward')
    path.write_text(text,encoding='utf-8',newline='\n')


if __name__=='__main__':
    repair_austria()
    repair_crown()
