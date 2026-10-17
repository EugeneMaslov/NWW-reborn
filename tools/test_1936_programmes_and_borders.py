"""Run service-repair, paid intervention, campaign-order and crown regressions.

This executes source effects with strict interpreters. It does not simulate the
game's AI scheduler, battles or map loading.
"""
from collections import Counter
from copy import deepcopy
from datetime import date
import json, random, re
from pathlib import Path

from hoi4_script import read, one, values, walk, parse, tree_focuses, engine_script_errors
from validate_austria_overhaul import World as BohemiaWorld
from validate_germany_politics import Scenario
from test_britain_lifecycle import World as BritainWorld
from validate_map_initialization import validate_map_initialization

ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')


def main():
    count=0
    def check(ok,message):
        nonlocal count
        count+=1
        assert ok,message
    meta=json.loads((ROOT/'docs/GER_services_expansion.json').read_text(encoding='utf-8'))
    tree=one(read(ROOT/'common/national_focus/GER_focuses.txt'),'focus_tree')
    fs={one(f,'id'):f for f in tree_focuses(tree,ROOT/'common/national_focus')}
    check(len(fs)==130 and len(meta['new_focuses'])==54,'Expanded German focus graph')
    sprites=set()
    for base in (GAME,ROOT):
        for p in (base/'interface').glob('*.gfx'):
            sprites.update(re.findall(r'\bname\s*=\s*"([^"]+)"',p.read_text(encoding='utf-8-sig',errors='replace')))
    categories=set()
    for base in (GAME,ROOT):
        for p in (base/'common/technology_tags').glob('*.txt'):
            categories.update(v for k,v,o in one(read(p),'technology_categories',[]) if isinstance(v,str))
    modifiers=set(re.findall(r'^## (\w+)',(GAME/'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig'),re.M))
    known_effects=set(re.findall(r'^## (\w+)',(GAME/'documentation/effects_documentation.md').read_text(encoding='utf-8-sig'),re.M))
    effect_ids={k for p in (ROOT/'common/scripted_effects').glob('*.txt') for k,v,o in read(p)}
    for s in meta['new_focuses']:
        focus=fs[s['id']]
        check(one(focus,'icon') in sprites,s['id']+' icon')
        for k,v,o in walk(one(focus,'completion_reward')):
            if k=='category':check(v in categories,s['id']+' research category '+v)
        for k,v,o in one(focus,'completion_reward'):
            check(k in known_effects or k in effect_ids,s['id']+' unknown reward '+k)
    for name,body,o in read(ROOT/'common/dynamic_modifiers/GER_services_modifiers.txt'):
        check(one(body,'icon') in sprites,name+' icon')
        for k,v,o in body:
            check(k in ('icon','enable') or k in modifiers,name+' native modifier '+k)
    # Reach both economic policies and both tactical schools; all common
    # capstones must remain attainable after either mutually exclusive choice.
    for policy in ('civil_investment','defence_procurement'):
        for school in ('mission_command','deliberate_battle'):
            blocked={'GER_nww_'+('civil_investment' if policy=='defence_procurement' else 'defence_procurement'),
                     'GER_nww_'+('mission_command' if school=='deliberate_battle' else 'deliberate_battle')}
            done=set()
            for _ in range(30):
                before=len(done)
                for fid,f in fs.items():
                    if fid in blocked:continue
                    groups=[values(g,'focus') for g in values(f,'prerequisite')]
                    if not all(set(g)&done for g in groups):continue
                    extra=[v for k,v,o in one(f,'available',[]) if k=='has_completed_focus']
                    if not set(extra)<=done:continue
                    if any(v in done for g in values(f,'mutually_exclusive') for v in values(g,'focus')):continue
                    done.add(fid)
                if len(done)==before:break
            for fid in ('imperial_army_readiness','aeronautical_institutes','high_seas_readiness',
                        'investment_dividend' if policy=='civil_investment' else 'procurement_continuity'):
                check('GER_nww_'+fid in done,'Unreachable capstone '+fid)
    effects={k:v for k,v,o in read(ROOT/'common/scripted_effects/GER_services_effects.txt')}
    rng=random.Random(1936)
    for _ in range(120):
        w=BohemiaWorld(effects,{})
        w.root='GER';g=w.countries['GER']
        g['focuses']={fid for fid in fs if rng.randrange(2)}
        g['vars'].update({f'GER_service_{s}_{k}':999 for s,params in meta['service_modifiers'].items() for k in params})
        w.apply(effects['GER_nww_refresh_services'])
        for service,params in meta['service_modifiers'].items():
            for key in params:
                expected=sum(s['spirit'].get(service,{}).get(key,0) for s in meta['new_focuses'] if s['id'] in g['focuses'])
                check(abs(g['vars'][f'GER_service_{service}_{key}']-expected)<1e-8,'Service replay drift')
        before=deepcopy(g);w.apply(effects['GER_nww_refresh_services'])
        check(g==before,'Service repair is not idempotent')
    check(not any(k in ('add_building_construction','add_research_slot','army_experience','navy_experience','air_experience') for k,v,o in walk(effects['GER_nww_refresh_services'])),'Repair repeats one-off rewards')

    PaidWorld=BohemiaWorld
    effects={k:v for name in ('GER_bohemian_effects.txt','AUS_overhaul_effects.txt') for k,v,o in read(ROOT/'common/scripted_effects'/name)}
    decision=one(one(read(ROOT/'common/decisions/GER_bohemian_decisions.txt'),'GER_bop_decisions_category'),'GER_nww_bohemian_civic_support')
    for reason in (None,'settled','lost_capital','war','allied','subject','seceded'):
        w=PaidWorld(effects,{});w.root='GER';g=w.countries['GER'];a=w.countries['AUS']
        g['focuses'].add('GER_nww_prague_network');g['pp']=100
        check(w.test(one(decision,'available')),'Intervention unavailable before payment')
        g['pp']-=float(one(decision,'cost'));w.apply(one(decision,'complete_effect'))
        check(not w.test(one(decision,'available')),'Concurrent paid intervention')
        if reason=='settled':a['flags'].add('AUS_nww_bohemia_settled')
        elif reason=='lost_capital':w.states['9']['controller']='GER'
        elif reason=='war':a['wars'].add('GER')
        elif reason=='allied':g['allies']={'AUS'}
        elif reason=='subject':g['subject']=True
        elif reason=='seceded':a['flags'].add('AUS_nww_bohemia_seceded')
        before=a['vars']['AUS_bohemian_tension']
        if reason:
            check(w.test(one(decision,'cancel_trigger')),'Invalidated intervention not cancelled')
            w.apply(one(decision,'cancel_effect'))
            check(g['pp']==100 and a['vars']['AUS_bohemian_tension']==before,'Cancellation/refund changed crisis')
        else:
            w.apply(one(decision,'remove_effect'))
            check(g['pp']==25 and a['vars']['AUS_bohemian_tension']==before+2,'Paid intervention reward/cost')
            check(a['vars']['AUS_bohemian_german_pressure']==2,'Contribution not credited')
        check('GER_nww_bohemian_support_busy' not in g['flags'],'Intervention lock remains')

    # Cached Croatian goals must disappear while Hungary is still independent;
    # being at war or in recovery blocks any second offensive declaration.
    CampaignWorld=Scenario
    effects={k:v for k,v,o in read(ROOT/'common/scripted_effects/AUS_campaign_effects.txt')}
    triggers={k:v for k,v,o in read(ROOT/'common/scripted_triggers/AUS_campaign_triggers.txt')}
    for state in ('independent','war','recovery','annexed','subject','allied','human'):
        w=CampaignWorld(effects,{});w.ai=state!='human';w.triggers.update(triggers)
        w.countries['HUN']=deepcopy(w.countries['AUS']);w.countries['CRO']=deepcopy(w.countries['AUS'])
        a=w.countries['AUS'];a['tree']='AUS_focus';a['goals'].add('CRO')
        if state in ('annexed','recovery'):w.countries['HUN']['exists']=False
        if state=='war':a['wars'].add('HUN')
        if state=='recovery':a['flags'].add('AUS_nww_hungarian_recovery')
        if state=='subject':w.countries['HUN']['subject']='AUS'
        if state=='allied':a['allies'].add('HUN')
        ready=state in ('annexed','subject','allied')
        check(w.condition(triggers['AUS_nww_croatian_campaign_ready'],'AUS')==ready,'Hungarian sequence '+state)
        w.apply(effects['AUS_nww_install_campaign_order'],'AUS')
        check(('CRO' in a['goals'])==(ready or state=='human'),'Cached Croatian goal '+state)
        check((('country','can_not_declare_war') in a['rules'])==(state in ('war','recovery')),'Second offensive guard '+state)
        before=deepcopy(a);w.apply(effects['AUS_nww_install_campaign_order'],'AUS');check(a==before,'Campaign guard repeat')
        w.ai=False;w.apply(effects['AUS_nww_install_campaign_order'],'AUS')
        check(('country','can_not_declare_war') not in a['rules'],'Human inherited AI declaration ban')

    crown_events={one(v,'id'):v for name in ('ENG_events.txt','ENG_crown_events.txt') for k,v,o in read(ROOT/'events'/name) if k=='country_event'}
    for eid in ('nww_eng.31','nww_eng_crown.1'):
        for option in values(crown_events[eid],'option'):
            for government in ('democratic','neutrality','fascism','communism'):
                w=BritainWorld();c=w.country('ENG');c.ideas.add('ENG_king_edward')
                c.pop={k:float(k==government) for k in c.pop};w.now=date(1937,1,1)
                check(w.test(one(crown_events[eid],'trigger'))==(government!='communism'),'Crown event route gate')
                if government=='communism':continue
                w.apply([e for e in option if e[0] not in ('name','ai_chance','trigger')])
                check('ENG_king_edward' not in c.ideas,'Weekly penalty survives crown settlement')
                check(bool(c.ideas&{'ENG_george_vi','ENG_nww_constitutional_edward'}),'Crown disappeared without successor')
    idea=one(one(one(read(ROOT/'common/ideas/ENG_crown_ideas.txt'),'ideas'),'country'),'ENG_nww_constitutional_edward')
    check(one(one(idea,'modifier'),'stability_weekly') is None,'Resolved Edward retains weekly loss')
    # Map initialization validates air/rocket points against the actual bitmap.
    validate_map_initialization(ROOT,GAME,check)
    old=one(read(ROOT/'history/states/184-Thrace.txt'),'state')
    new=one(read(ROOT/'history/states/1083-Dedeagach.txt'),'state')
    check({v for k,v,o in one(old,'provinces')}|{v for k,v,o in one(new,'provinces')}=={'9791','9930','11774','11905'},'Thrace province conservation')
    check(sum(int(one(s,'manpower')) for s in (old,new))==382500,'Thrace population conservation')
    check(sum(int(one(one(s,'resources'),'chromium')) for s in (old,new))==11,'Thrace resources conservation')
    for state in (old,new):
        check(one(one(state,'history'),'owner')=='BUL','1913 Thracian ownership')
        check('GRE' in values(one(state,'history'),'add_core_of'),'Indigenous Greek core removed')
    for folder in ('common','events'):
        for pattern in ('GER_services*.txt','AUS_campaign*.txt','ENG_crown*.txt'):
            for path in (ROOT/folder).rglob(pattern):check(not list(engine_script_errors(read(path))),str(path))
    print(f'PASS: {count} service/native-registry, four programme routes, paid Bohemian intervention/refund, Austrian campaign/cached-goal, crown and Thracian map checks; no engine scheduling/combat claim')


if __name__=='__main__':main()
