"""Regression checks for German colonies/MEFO, LTB focus artwork and runtime log compatibility."""
import json,re,sys
from pathlib import Path
from PIL import Image
from hoi4_script import read,one,values,walk,TOKEN
ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')
errors=[]
def check(ok,message):
    if not ok:errors.append(message)
report=json.loads((ROOT/'docs/GER_overseas_setup.json').read_text(encoding='utf-8'))
check(report['total_states']==19,'Expected all 19 overseas states on the current map')
for territory in report['territories']:
    state=one(read(ROOT/territory['file']),'state');history=one(state,'history')
    check(one(history,'owner')=='GER',f'{territory["state"]}: overseas owner is not GER')
    check('GER' not in values(history,'add_core_of'),f'{territory["state"]}: colony wrongly became a German national core')
    check(all(v=='GER' for k,v,o in walk(history) if k in ('owner','controller')),f'{territory["state"]}: later bookmark overwrites German ownership')
for sid in (523,1073,1072,638,669,1057):
    file=next(p for p in (ROOT/'history/states').glob('*.txt') if int(one(one(read(p),'state'),'id'))==sid)
    check(one(one(one(read(file),'state'),'history'),'owner')!='GER',f'{sid}: British/Dutch Papuan or American island territory was wrongly transferred')
history=read(ROOT/'history/countries/GER - Germany.txt')
check(not any(k=='add_dynamic_modifier' and one(v,'modifier') in ('GER_mefo_bills_modifier','GER_economy_of_conquest_modifier') for k,v,o in walk(history)),'MEFO or conquest debt is still activated in German history')
check(one(history,'nww_GER_disable_mefo')=='yes','German setup does not clear the complete debt system')
effect=one(read(ROOT/'common/scripted_effects/GER_effects.txt'),'nww_GER_disable_mefo')
check({v for k,v,o in walk(effect) if k=='remove_dynamic_modifier'}=={'GER_mefo_bills_modifier','GER_economy_of_conquest_modifier'},'German cleanup misses a debt modifier')
check(any(k=='remove_mission' and v=='GER_mefo_bills_mission' for k,v,o in walk(effect)),'MEFO mission is not removed safely')
check(not any(k in ('GER_pay_back_mefo_bills','GER_remove_mefo_bills','add_political_power','add_timed_idea') for k,v,o in walk(effect)),'MEFO cleanup creates a repayment or reward')
check(set(report['mefo_ideas'])=={v for k,v,o in walk(effect) if k=='remove_ideas'},'German cleanup does not cover every registered MEFO idea')
on_actions=one(read(ROOT/'common/on_actions/GER_on_actions.txt'),'on_actions')
check(bool(one(on_actions,'on_startup')) and bool(one(on_actions,'on_daily_GER')),'MEFO cleanup lacks startup/old-save hooks')

spec=json.loads((ROOT/'docs/art/LTB_focus_generation.json').read_text(encoding='utf-8'))
check(len(spec['assets'])==6,'Expected six significant LTB focus icons')
focuses={one(f,'id'):f for f in values(one(read(ROOT/'common/national_focus/ltb_focus.txt'),'focus_tree'),'focus')}
sprites={one(v,'name'):v for k,v,o in one(read(ROOT/'interface/LTB_focus_icons.gfx'),'spriteTypes')}
for job in spec['assets']:
    check(one(focuses[job['focus']],'icon')==job['sprite'],job['key']+': focus does not use its generated icon')
    check(job['sprite'] in sprites and job['sprite']+'_shine' in sprites,job['key']+': normal/highlight sprite is missing')
    image=Image.open(ROOT/job['texture']).convert('RGBA');bounds=image.getchannel('A').getbbox()
    check(image.size==(95,95) and bounds and bounds[0]>=5 and bounds[1]>=5 and bounds[2]<=90 and bounds[3]<=90,job['key']+': focus artwork exceeds the UI clearance')
    check((ROOT/job['saved_source']).exists(),job['key']+': generated original is not project-local')

doc=read(ROOT/'common/scripted_effects/operation_strat_effects.txt')
operations={k for p in (GAME/'common/operations').glob('*.txt') for k,v,o in read(p) if isinstance(v,list)}
for k,v,o in walk(doc):
    if k in ('is_preparing_operation','num_finished_operations'):
        check(one(v,'operation') in operations,f'{k}: still uses a missing or variable operation token')
sov=one(read(ROOT/'common/on_actions/SOV_on_actions.txt'),'on_actions')
for key in ('on_startup','on_daily_SOV'):
    check(any(k=='has_focus_tree' and v=='SOV_focus' for k,v,o in walk(one(sov,key))),key+': purge suspension is not restricted to the NWW Soviet tree')
raid=one(one(read(ROOT/'common/decisions/nww_mkn_decisions.txt'),'MKN_border_raids'),'MKN_border_raid')
for gate in (one(raid,'available'),one(one(one(raid,'complete_effect'),'if'),'limit')):
    check(any(one(n,'is_ally_with')=='UKR' for n in values(gate,'NOT')),'MKN raid lacks a live alliance guard')
    check(any(one(n,'has_country_flag')=='UKR_MKN_border_settled' for n in values(gate,'NOT')),'MKN raid ignores a settled border')
    check(bool(one(gate,'OR')),'MKN raid ignores actual border ownership/control')
for k,node,o in walk(one(raid,'complete_effect')):
    if k in ('if','else_if') and values(node,'start_border_war'):
        checks={v for field,v,op in walk(one(node,'limit')) if field=='is_owned_and_controlled_by'}
        check(checks=={'MKN','UKR'},'MKN raid can use a border controlled by third parties')
events=read(ROOT/'events/nww_mkn.txt')
for event in values(events,'country_event'):
    if one(event,'id') not in ('mkn.2','mkn.4'):continue
    for key,node,op in walk(event):
        if key=='if' and values(node,'declare_war_on'):
            check(any(one(n,'is_ally_with')=='MKN' for n in values(one(node,'limit'),'NOT')),'Ukraine can declare war on an ally through an old event')
for folder in ('common','events','history','interface'):
    for p in (ROOT/folder).rglob('*.txt'):
        check(not any(re.fullmatch(r'-?\.\d+',m.group()) for m in TOKEN.finditer(p.read_text(encoding='utf-8-sig'))),f'{p.relative_to(ROOT)}: bare decimal without a leading zero')
if errors:
    for error in errors:print('ERROR:',error)
    raise SystemExit(1)
print('PASS: 19 German colonies, excluded foreign territories, MEFO removal without repayment, old-save hooks, six transparent LTB icons/highlights, operation IDs, scoped purge suspension and decimal syntax')
