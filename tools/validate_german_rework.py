"""Execute German/Bohemian source effects and audit industry, operations and pacing."""
import argparse,json,re,random
from copy import deepcopy
from pathlib import Path
from math import isclose
from hoi4_script import read,one,values,walk,engine_script_errors,tree_focuses
from validate_austria_overhaul import World
from validate_germany_politics import Scenario

ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--game',type=Path,required=True);game=p.parse_args().game
effects={k:v for name in ('AUS_overhaul_effects.txt','GER_bohemian_effects.txt','GER_industry_effects.txt') for k,v,o in read(ROOT/'common/scripted_effects'/name)}
events={one(v,'id'):v for k,v,o in read(ROOT/'events/AUS_overhaul_events.txt') if k=='country_event'}
op=one(read(ROOT/'common/operations/GER_bohemian_operations.txt'),'GER_nww_bohemian_autonomists')
assert one(op,'days')=='45' and one(op,'operatives')=='1' and one(op,'network_strength')=='35'
assert one(one(op,'operation_target'),'targets')==[(None,'AUS',None)]
for key in ('available','requirements'):
    assert one(one(one(op,key),'FROM'),'GER_nww_bohemian_target_open')=='yes'
assert one(op,'outcome_execute')==one(op,'outcome_extra_execute')
assert one(one(op,'outcome_execute'),'FROM')
assert one(one(op,'allowed'),'has_dlc')=='La Resistance'
native_phases={k for path in (game/'common/operation_phases').glob('*.txt') for k,v,o in read(path)}
for phase in values(op,'phases'):
    for name,body,operator in phase:assert name in native_phases,name
native_buildings=one(read(game/'common/buildings/00_buildings.txt'),'buildings')
assert one(native_buildings,'energy_infrastructure') is not None
def fresh(tension=2,pressure=0):
    w=World(effects,events)
    w.countries['AUS']['vars'].update(AUS_bohemian_tension=tension,AUS_bohemian_german_pressure=pressure)
    w.countries['GER']['focuses'].add('GER_nww_prague_network')
    return w
count=0
for start in range(10):
    for pressure in range(start+1):
        w=fresh(start,pressure)
        w.apply(one(one(op,'outcome_execute'),'FROM'))
        actual=min(2,10-start)
        v=w.countries['AUS']['vars']
        assert v['AUS_bohemian_tension']==start+actual
        assert v['AUS_bohemian_german_pressure']==pressure+actual
        assert isclose(v['AUS_bohemian_german_share'],100*(pressure+actual)/(start+actual))
        assert bool(w.pending)==(start+actual==10)
        count+=1
for blocked in ('settled','seceded','capital_occupied','capital_lost','war','GER_subject','GER_absent','CZE_exists','AUS_subject','allied','no_focus','ten'):
    w=fresh(5,2)
    a,g,c=w.countries['AUS'],w.countries['GER'],w.countries['CZE']
    if blocked=='settled':a['flags'].add('AUS_nww_bohemia_settled')
    if blocked=='seceded':a['flags'].add('AUS_nww_bohemia_seceded')
    if blocked=='capital_occupied':w.states['9']['controller']='GER'
    if blocked=='capital_lost':w.states['9']['owner']='GER'
    if blocked=='war':a['wars'].add('GER')
    if blocked=='GER_subject':g['subject']=True
    if blocked=='GER_absent':g['exists']=False
    if blocked=='CZE_exists':c['exists']=True
    if blocked=='AUS_subject':a['subject']=True
    if blocked=='allied':g['allies']={'AUS'}
    if blocked=='no_focus':g['focuses'].clear()
    if blocked=='ten':a['vars']['AUS_bohemian_tension']=10
    before=deepcopy(w.countries);w.apply(one(one(op,'outcome_execute'),'FROM'))
    assert w.countries==before and not w.pending,blocked
    count+=1
for tension in range(11):
    for pressure in range(tension+1):
        w=fresh(tension,pressure)
        w.apply(effects['AUS_nww_reduce_bohemian_tension'])
        v=w.countries['AUS']['vars'];expected=max(0,tension-2)
        assert v['AUS_bohemian_tension']==expected
        assert isclose(v['AUS_bohemian_german_pressure'],pressure*expected/tension if tension else 0,abs_tol=1e-9)
        assert 0<=v['AUS_bohemian_german_share']<=100
        count+=1
for pressure in (0,5,6,6.01,7,8,10):
    for blocked in (None,'existing_CZE','GER_subject','GER_absent','GER_war','CZE_war','CZE_faction','CZE_subject'):
        w=fresh(10,pressure);g=w.countries['GER'];c=w.countries['CZE']
        if blocked=='existing_CZE':c['exists']=True
        if blocked=='GER_subject':g['subject']=True
        if blocked=='GER_absent':g['exists']=False
        if blocked=='GER_war':g['wars'].add('AUS')
        if blocked=='CZE_war':c['wars'].add('GER')
        if blocked=='CZE_faction':c['faction']=True
        if blocked=='CZE_subject':c['subject']=True
        w.apply(effects['AUS_nww_release_bohemia'])
        assert (c.get('overlord')=='GER')==(pressure>6 and blocked is None),(pressure,blocked)
        assert 'AUS_nww_fresh_bohemian_secession' not in w.countries['AUS']['flags']
        # No delayed daily callback may subjugate an already released state.
        before=deepcopy(w.countries);w.apply(effects['GER_nww_settle_bohemian_influence'])
        assert w.countries==before
        count+=1
# Missing old-save contribution means zero; sanitization never invents pressure.
w=fresh(7);del w.countries['AUS']['vars']['AUS_bohemian_german_pressure']
w.apply(effects['GER_nww_update_bohemian_influence']);assert w.countries['AUS']['vars']['AUS_bohemian_german_share']==0

class IndustryWorld(World):
    def __init__(self):
        super().__init__(effects,events)
        self.root='GER';self.countries['GER']['ideas']=set()
    def test(self,node,scope=None):
        for entry in node:
            if entry[0]=='has_idea':
                if entry[1] not in self.countries[scope or self.root]['ideas']:return False
            elif not super().test([entry],scope):return False
        return True
    def apply(self,node,scope=None):
        for entry in node:
            if entry[0]=='remove_ideas':self.countries[scope or self.root]['ideas'].discard(entry[1])
            else:super().apply([entry],scope)
meta=json.loads((ROOT/'docs/GER_industry_rework.json').read_text())
bonuses=meta['persistent_bonuses']
rng=random.Random(1939)
for _ in range(60):
    w=IndustryWorld();s=w.countries['GER']
    s['focuses']={fid for fid in bonuses if rng.randrange(2)}
    s['vars'].update({f'GER_industry_{k}':99 for k in meta['modifiers']})
    w.apply(effects['GER_nww_refresh_industry'])
    for key in meta['modifiers']:
        assert isclose(s['vars']['GER_industry_'+key],sum(v.get(key,0) for f,v in bonuses.items() if f in s['focuses']),abs_tol=1e-9)
    before=deepcopy(s);w.apply(effects['GER_nww_refresh_industry']);assert s==before
assert not any(k in ('add_building_construction','add_resource','add_research_slot','create_wargoal') for k,v,o in walk(effects['GER_nww_refresh_industry']))
native=set(re.findall(r'^## (\w+)',(game/'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig'),re.M))
for key in meta['modifiers'].values():assert key in native,key
tree=one(read(ROOT/'common/national_focus/GER_focuses.txt'),'focus_tree')
fs={one(f,'id'):f for f in tree_focuses(tree,ROOT/'common/national_focus')}
assert len(fs)==json.loads((ROOT/'docs/GER_services_expansion.json').read_text(encoding='utf-8'))['total_playable']
assert all(one(fs[f],'cost') in ('5','10') for f in meta['focuses'])
plan=one(read(ROOT/'common/ai_strategy_plans/GER_historical.txt'),'NWW_GER_historical')
order=[v for k,v,o in one(plan,'ai_national_focuses')]
assert order.index('GER_dissolve_the_reichstag')<order.index('GER_reign_in_mitteleuropa')<order.index('GER_crush_eastern_syndicates')
assert order.index('GER_dissolve_the_reichstag')<order.index('GER_the_austrian_question')
# Dated foreign objectives yield to the industrial tail; do not postpone institutions behind ten unrelated projects.
assert len([f for f in order if f in meta['focuses']])>=10
# Use the established GER interpreter to check human/history boundaries and stale replies.
ger_effects={k:v for filename in ('GER_effects.txt','GER_lategame_effects.txt') for k,v,o in read(ROOT/'common/scripted_effects'/filename)}
ger_events={one(e,'id'):e for k,e,o in read(ROOT/'events/GER_events.txt') if k.endswith('_event')}
for year in range(1936,1942):
    for ai,historical in ((False,True),(True,True),(True,False)):
        s=Scenario(ger_effects,ger_events);s.date=f'{year}.1.1';s.ai=ai;s.historical=historical
        for fid,minimum in [('GER_the_austrian_question',1939),('GER_reign_in_mitteleuropa',1939),('GER_crush_eastern_syndicates',1940 if ai and historical else 1939)]:
            assert s.condition(one(fs[fid],'available'))==(year>=minimum),(fid,year,ai,historical)
    s=Scenario(ger_effects,ger_events);s.date=f'{year}.1.1';s.countries['GER']['focuses'].add('GER_the_austrian_question')
    s.apply(ger_effects['GER_nww_dispatch_austrian_demand'])
    assert bool(s.queue)==(year>=1939)
    queue=deepcopy(s.queue);s.apply(ger_effects['GER_nww_dispatch_austrian_demand']);assert s.queue==queue
    for option in values(ger_events['ger_crisis.10'],'option'):
        before=deepcopy(s.countries);s.apply([e for e in option if e[0] not in ('name','ai_chance')],'AUS')
        if year<1939:assert before==s.countries
for folder in ('common','events'):
    for path in (ROOT/folder).rglob('GER*.txt'):assert not list(engine_script_errors(read(path))),path
print(f'PASS: {count} source-script Bohemian operation/reform/secession cases, strict 60% boundary and protected existing countries; 60 idempotent industry repairs; native modifiers and 1939 pressure / 1940 historical eastern gates')
