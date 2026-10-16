"""Validate the overhaul contract and execute actual frontier scripts."""
import argparse
from pathlib import Path
from collections import Counter
from itertools import product
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
    industry=__import__('json').loads((ROOT/'docs/MKN_unified_progression.json').read_text())['industry_changes']
    integration=__import__('json').loads((ROOT/'docs/MKN_ukraine_integration.json').read_text())['focuses']
    military={g['id'] for g in __import__('json').loads((ROOT/'docs/MKN_military_refactor.json').read_text())['groups']}
    horizons={fid for branch in __import__('json').loads((ROOT/'docs/MKN_horizons.json').read_text())['branches'].values() for fid in branch}
    for fid,node in registry.items():
        if fid.startswith('MKN_'):
            check(one(node,'cost') in ({'5','10'} if fid in industry or fid in integration or fid in military or fid in horizons else {'5'}),f'{fid}: invalid focus duration')
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
    leader_traits=one(read(ROOT/'common/country_leader/MKN_overhaul_traits.txt'),'leader_traits')
    for key,value in {'army_org_factor':'0.25','org_loss_when_moving':'-0.20','planning_speed':'0.20'}.items():
        check(one(one(leader_traits,'mkn_batko_advisor'),key)==value,'Makhno advisor '+key)
    legend=one(one(one(read(ROOT/'common/unit_leader/MKN_traits.txt'),'leader_traits'),'mkn_batko_legend'),'modifier')
    for key,value in {'army_speed_factor':'0.25','cavalry_attack_factor':'0.25','motorized_attack_factor':'0.25','breakthrough_factor':'0.20'}.items():
        check(one(legend,key)==value,'Legend of Batko '+key)
    staff_traits={'mkn_infantry_specialist','mkn_tachanka_expert','mkn_armored_train_commander','mkn_steppe_logistics_officer','mkn_entrenchment_specialist'}
    assigned={token for _,char,_ in chars for role in values(char,'advisor') if one(role,'slot')=='high_command' for _,token,_ in one(role,'traits',[])}
    check(staff_traits<=assigned,'Missing requested high command roles')
    economy=one(read(ROOT/'common/scripted_effects/nww_mkn_progression.txt'),'nww_mkn_rebuild_industry')
    chains=__import__('json').loads((ROOT/'docs/MKN_unified_progression.json').read_text())['steppe_recovery_v2']
    for chain in chains:
        score=-0.25
        for fid in chain:
            score+=sum(float(one(n,'MKN_unified_industrial_capacity_factory','0')) for n in values(one(registry[fid],'completion_reward'),'add_to_variable'))
        check(abs(score)<1e-9,'Five industrial milestones leave an output penalty')
    dyn=one(read(ROOT/'common/dynamic_modifiers/nww_dynamic_modifiers.txt'),'MKN_army_development')
    check(one(dyn,'conscription')=='MKN_army_conscription' and one(dyn,'recruitable_population') is None,'Army spirit still uses a state-only manpower modifier')
    for fid,focus in registry.items():
        if fid.startswith('MKN_'):
            for node in values(one(focus,'completion_reward',[]),'add_to_variable'):
                if one(node,'MKN_army_conscription') is not None:check(one(node,'MKN_army_conscription')=='0.02',fid+' does not give flat +2% manpower')
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
    # Cancellation and availability must respect the actual Soviet defender.
    sim=FrontierModel(effects,triggers);sim.border=True;sim.border_enemy='SOV'
    sim.countries['MKN']['variables'].update(mkn_ukr_attacking_state='196',mkn_ukr_defending_state='197')
    check(not sim.test(triggers['mkn_ukr_frontier_action_available']),'An active Soviet battle allows another frontier action')
    sim.run('mkn_ukr_stop_border_battle')
    check(not sim.border and sim.cancellations==[('196','197','yes')],'Soviet battle survives terminal cleanup')
    kyiv=one(read(ROOT/'common/scripted_triggers/MKN_kyiv_triggers.txt'),'MKN_kyiv_encircled')
    triggers['MKN_kyiv_encircled']=kyiv
    for owners in product(('UKR','MKN','SOV'),repeat=3):
        for controllers in product(('MKN','UKR'),repeat=3):
            sim=FrontierModel(effects,triggers)
            sim.countries['MKN']['wars'].add('UKR')
            sim.states['202']={'owner':'UKR','controller':'UKR','cores':{'UKR'},'flags':{},'damage':0,'neighbors':('601','602','603')}
            for sid,owner,controller in zip(('601','602','603'),owners,controllers):
                sim.states[sid]={'owner':owner,'controller':controller,'cores':{owner},'flags':{},'damage':0,'neighbors':('202',)}
            expected=all(owner!='UKR' or controller=='MKN' for owner,controller in zip(owners,controllers))
            check(sim.test(kyiv)==expected,'Kyiv neighbor ownership/control mismatch')
            if expected:
                ukrainian={sid for sid,s in sim.states.items() if s['owner']=='UKR'}
                sim.run('MKN_annex_encircled_ukraine')
                check(not sim.countries['UKR']['exists'] and all(sim.states[sid]['owner']=='MKN' for sid in ukrainian),'Kyiv capitulation leaves Ukrainian territory')
                check(sim.states['500']['cores']=={'LTB'},'Kyiv capitulation cores unrelated occupied land')
    # The news event is dispatched once by the funeral and broadcast by major=yes.
    funeral=next(n for n in values(read(ROOT/'events/MKN_events.txt'),'country_event') if one(n,'id')=='mkn_crisis.1')
    check(('date','1937.2.28','>') in one(funeral,'trigger'),'Makhno can die before March 1937')
    news=one(read(ROOT/'events/MKN_news_events.txt'),'news_event')
    check(one(news,'major')=='yes' and one(news,'trigger') is None and one(news,'fire_only_once') is None,'Funeral news is not broadcast to all audiences')
    check(one(one(one(funeral,'immediate'),'news_event'),'id')=='mkn_news.1','Funeral does not dispatch the global news')
    # Unit creation strings must parse as an actual template payload, with no orphan tokens.
    militia=one(read(ROOT/'common/scripted_effects/MKN_effects.txt'),'MKN_raise_communal_militias')
    from hoi4_script import parse
    for unit in values(militia,'create_unit'):
        check(all(k in ('division','owner') for k,v,o in unit),'Malformed militia create_unit arguments')
        check(one(parse(one(unit,'division')),'division_template')=='MKN_Commune_Guard','Militia has no valid division template')
    for path in (ROOT/'gfx/leaders/MKN').glob('*.dds'):
        with Image.open(path) as image:check(image.convert('RGBA').getchannel('A').getextrema()==(255,255),path.name+' remains transparent')
    native=set(re.findall(r'^## (\w+)',(game/'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig'),re.M))
    native |= {'production_speed_'+k+'_factor' for k,v,o in one(read(game/'common/buildings/00_buildings.txt'),'buildings')}
    native |= {p+'_drift' for p in ('fascism','communism','democratic','neutrality')}
    subunits={k for path in (game/'common/units').glob('*.txt') for k,v,o in one(read(path),'sub_units',[])}
    # Do not invent modifier names from subunit IDs: motorized_attack_factor is
    # registered, modifier_army_sub_unit_motorized_attack_factor is rejected.
    ideologies=one(read(game/'common/ideologies/00_ideologies.txt'),'ideologies')
    native|={party+'_drift' for party,_,_ in ideologies}
    traits=one(read(ROOT/'common/country_leader/MKN_overhaul_traits.txt'),'leader_traits')
    for name,node,op in traits:
        for key,value,operator in node:
            if key not in ('sprite','random','custom_modifier_tooltip'):check(key in native,f'Invalid trait modifier {name}/{key}')
    for folder in ('common','events'):
        for path in (ROOT/folder).rglob('MKN*.txt'):
            check(not list(engine_script_errors(read(path))),str(path)+' native syntax')
    print(f'PASS: MKN overhaul: {checks} checks; pacing, economy, 24 advisors, leaders, real-script 20/30-day actions, terminal cleanup and Soviet target callbacks')

if __name__=='__main__':main()
