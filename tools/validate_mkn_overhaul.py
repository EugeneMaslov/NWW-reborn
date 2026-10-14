"""Validate the overhaul contract and execute actual frontier scripts."""
import argparse
from pathlib import Path
from collections import Counter
import re
from PIL import Image
from hoi4_script import read, one, values, walk, focus_registry, engine_script_errors
from validate_mkn_frontier import FrontierModel

ROOT=Path(__file__).resolve().parents[1]
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--game',type=Path,required=True);game=parser.parse_args().game
    checks=0
    def check(ok,message):
        nonlocal checks
        checks+=1
        if not ok:raise AssertionError(message)
    registry=focus_registry(ROOT/'common/national_focus')
    for fid,node in registry.items():
        if fid.startswith('MKN_'):check(one(node,'cost')=='5',f'{fid}: not 35 days')
        if fid.startswith('UKR_'):check(float(one(node,'cost','0'))>=10,f'{fid}: below 70 days')
    history=read(ROOT/'history/countries/MKN - Makhnovists.txt')
    check(one(history,'capital')=='1082','Wrong MKN capital')
    totals=Counter()
    for path in (ROOT/'history/states').glob('*.txt'):
        state=one(read(path),'state');h=one(state,'history',[])
        if one(h,'owner')=='MKN':
            buildings=one(h,'buildings',[])
            for k in ('industrial_complex','arms_factory'):totals[k]+=int(one(buildings,k,'0'))
    check(totals['industrial_complex']>=5 and totals['arms_factory']>=3,'Starting factory totals')
    buildings=one(one(one(read(ROOT/'history/states/1082-Huliaipole.txt'),'state'),'history'),'buildings')
    for k,v in {'industrial_complex':'3','arms_factory':'2','infrastructure':'3'}.items():check(one(buildings,k)==v,'Huliaipole '+k)
    chars=one(read(ROOT/'common/characters/nww_MKN.txt'),'characters')
    parties=Counter()
    for name,char,op in chars:
        for advisor in values(char,'advisor'):
            if one(advisor,'slot')=='political_advisor':parties[one(one(advisor,'available'),'has_government')]+=1
    check(parties==Counter({p:6 for p in ('fascism','democratic','neutrality','communism')}),'Advisor roster is not six per party')
    makhno=one(chars,'NWW_MKN_makhno');general=one(makhno,'corps_commander')
    for k,v in {'skill':'6','attack_skill':'6','defense_skill':'5','planning_skill':'5','logistics_skill':'5'}.items():check(one(general,k)==v,'Makhno '+k)
    check({v for k,v,o in one(general,'traits')}=={'trickster','cavalry_officer','skirmisher','mkn_batko_legend'},'Makhno traits')
    check(one(one(one(makhno,'field_marshal'),'visible'),'has_government')=='communism','Field marshal restriction lost')
    effects=dict((k,v) for k,v,o in read(ROOT/'common/scripted_effects/MKN_ukr_border_effects.txt'))
    triggers=dict((k,v) for k,v,o in read(ROOT/'common/scripted_triggers/MKN_ukr_border_triggers.txt'))
    decisions=one(read(ROOT/'common/decisions/MKN_ukr_border_decisions.txt'),'MKN_ukr_border_category')
    mission=one(decisions,'MKN_passive_escalation_drift')
    check(one(mission,'days_mission_timeout')=='30','Passive tick period')
    check(one(one(mission,'available'),'always')=='no','Passive mission can be manually completed')
    check(one(mission,'selectable_mission')=='no','Passive mission is selectable')
    pullback=one(decisions,'mkn_deescalate_pull_back')
    check(one(pullback,'days_remove')=='20' and one(pullback,'days_re_enable')=='0','De-escalation cooldown doubles the action period')
    sim=FrontierModel(effects,triggers);sim.run('mkn_ukr_initialize_frontier')
    sim.countries['MKN']['variables']['mkn_ukr_escalation_level']=3
    sim.apply(one(pullback,'complete_effect'))
    check(sim.countries['MKN']['variables']['mkn_ukr_escalation_level']==3,'De-escalation grants reward immediately')
    sim.day=20;sim.apply(one(pullback,'remove_effect'))
    check(sim.countries['MKN']['variables']['mkn_ukr_escalation_level']==2,'De-escalation does not reduce exactly one after twenty days')
    sim.apply(one(mission,'timeout_effect'))
    check(sim.countries['MKN']['variables']['mkn_ukr_escalation_level']==3,'Passive tick is not +1')
    check('MKN_passive_escalation_drift' in sim.countries['MKN']['missions'],'Passive mission failed to restart')
    sim.countries['MKN']['flags']['mkn_ukr_frontier_concluded']=-1
    sim.apply(one(mission,'timeout_effect'))
    check(sim.countries['MKN']['variables']['mkn_ukr_escalation_level']==3,'Concluded crisis still escalates')
    sim.run('mkn_ukr_frontier_daily')
    check('MKN_passive_escalation_drift' not in sim.countries['MKN']['missions'],'Terminal cleanup leaves passive mission active')
    events={one(e,'id'):e for e in values(read(ROOT/'events/MKN_ukr_border_events.txt'),'country_event')}
    for unlocked in (False,True):
        for sid in ('227','221','137','220','240','202'):
            sim=FrontierModel(effects,triggers)
            owner='UKR' if sid=='202' else 'SOV'
            sim.states[sid]={'owner':owner,'controller':owner,'cores':{owner},'flags':{},'damage':0,'neighbors':('196',)}
            if unlocked:sim.countries['MKN']['focuses'].add('MKN_donbas_miners_agitation')
            sim.froms=('196',owner,sid)
            allowed=sim.test(triggers['MKN_valid_frontier_target'],sid)
            check(allowed==(unlocked and sid in ('227','221','137')),f'Wrong border eligibility {sid}/{unlocked}')
            before={k:set(s['cores']) for k,s in sim.states.items()}
            sim.apply(one(events['mkn_ukr_border.20'],'immediate'))
            check((sim.states[sid]['owner']=='MKN')==allowed,f'Wrong SOV victory transfer {sid}/{unlocked}')
            check(sim.states['500']['cores']==before['500'],'Frontier cores unrelated territory')
    sim=FrontierModel(effects,triggers);sim.froms=('196','SOV','197')
    sim.apply(one(events['mkn_ukr_border.21'],'immediate'))
    check(sim.states['196']['owner']=='SOV','SOV victory hands attacker territory to UKR')
    for path in (ROOT/'gfx/leaders/MKN').glob('*.dds'):
        with Image.open(path) as image:check(image.convert('RGBA').getchannel('A').getextrema()==(255,255),path.name+' remains transparent')
    native=set(re.findall(r'^## (\w+)',(game/'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig'),re.M))
    native |= {'production_speed_'+k+'_factor' for k,v,o in one(read(game/'common/buildings/00_buildings.txt'),'buildings')}
    subunits={k for path in (game/'common/units').glob('*.txt') for k,v,o in one(read(path),'sub_units',[])}
    native|={'modifier_army_sub_unit_'+u+'_'+stat+'_factor' for u in subunits for stat in ('attack','defence','speed','max_org')}
    traits=one(read(ROOT/'common/country_leader/MKN_overhaul_traits.txt'),'leader_traits')
    for name,node,op in traits:
        for key,value,operator in node:
            if key not in ('sprite','random'):check(key in native,f'Invalid trait modifier {name}/{key}')
    for folder in ('common','events'):
        for path in (ROOT/folder).rglob('MKN*.txt'):
            check(not list(engine_script_errors(read(path))),str(path)+' native syntax')
    print(f'PASS: MKN overhaul: {checks} checks; pacing, economy, 24 advisors, leaders, real-script 20/30-day actions, terminal cleanup and Soviet target callbacks')

if __name__=='__main__':main()
