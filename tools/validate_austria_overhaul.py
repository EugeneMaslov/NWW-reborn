"""Execute Austrian crown-land and ultimatum scripts; audit the expanded tree."""
import argparse,re
from pathlib import Path
from copy import deepcopy
from collections import Counter
from math import isclose
from hoi4_script import read,one,values,walk,variable_check,engine_script_errors

ROOT=Path(__file__).resolve().parents[1]
class World:
    def __init__(self,effects,events):
        self.effects,self.events=effects,events
        self.root='AUS';self.pending=[]
        self.countries={tag:{'exists':tag!='CZE','flags':set(),'vars':{'AUS_bohemian_tension':2,'AUS_bohemian_investments':0},'missions':set(),'dynamic':set(),'focuses':set(),'stability':0.5,'subject':False,'wars':set(),'claims':set(),'cores':set()} for tag in ('AUS','CZE','GER','POL','ROM')}
        self.states={str(sid):{'owner':owner,'controller':owner,'cores':{owner}} for sid,owner in [(4,'AUS'),(9,'AUS'),(69,'AUS'),(72,'AUS'),(74,'AUS'),(75,'AUS'),(88,'POL'),(89,'POL'),(91,'POL'),(80,'ROM')]}
    def data(self,scope):return self.states[scope] if scope in self.states else self.countries[scope]
    def number(self,value,scope):
        try:return float(value)
        except ValueError:return self.countries[scope]['vars'].get(value,0)
    def compare(self,a,b,op):return {'=':a==b,'<':a<b,'>':a>b,'<=':a<=b,'>=':a>=b,'!=':a!=b}[op]
    def test(self,node,scope=None):
        scope=scope or self.root;out=[];data=self.data(scope)
        for key,value,op in node:
            if key in self.states or key in self.countries:result=self.test(value,key)
            elif key=='ROOT':result=self.test(value,self.root)
            elif key=='NOT':result=not self.test(value,scope)
            elif key=='OR':result=any(self.test([n],scope) for n in value)
            elif key=='AND':result=self.test(value,scope)
            elif key=='has_country_flag':result=value in data['flags']
            elif key=='has_variable':result=value in data['vars']
            elif key=='has_completed_focus':result=value in data['focuses']
            elif key=='has_active_mission':result=value in data['missions']
            elif key=='has_dynamic_modifier':result=one(value,'modifier') in data['dynamic']
            elif key=='has_focus_tree':result=value=='AUS_focus'
            elif key=='tag':result=scope==value
            elif key=='exists':result=data['exists']==(value=='yes')
            elif key=='is_subject':result=data['subject']==(value=='yes')
            elif key=='has_war_with':result=value in data['wars']
            elif key=='is_owned_by':result=data['owner']==(self.root if value=='ROOT' else value)
            elif key=='is_owned_and_controlled_by':result=data['owner']==data['controller']==(self.root if value=='ROOT' else value)
            elif key=='check_variable':
                var,operand,operator=variable_check(value);result=self.compare(self.number(var,scope),self.number(operand,scope),operator)
            elif key=='always':result=value=='yes'
            else:raise AssertionError('Unmodeled Austrian trigger '+str(key))
            out.append(result)
        return all(out)
    def apply(self,node,scope=None):
        scope=scope or self.root;matched=False
        for key,value,op in node:
            data=self.data(scope)
            if key in ('if','else_if'):
                if key=='if':matched=False
                if not matched and self.test(one(value,'limit'),scope):self.apply([n for n in value if n[0]!='limit'],scope);matched=True
            elif key=='else':
                if not matched:self.apply(value,scope)
                matched=True
            elif key in self.effects:self.apply(self.effects[key],scope)
            elif key in self.states or key in self.countries:self.apply(value,key)
            elif key=='ROOT':self.apply(value,self.root)
            elif key in ('set_variable','add_to_variable','subtract_from_variable','multiply_variable'):
                for var,operand,operator in value:
                    if var=='tooltip':continue
                    n=self.number(operand,scope);old=data['vars'].get(var,0)
                    data['vars'][var]={'set_variable':lambda:n,'add_to_variable':lambda:old+n,'subtract_from_variable':lambda:old-n,'multiply_variable':lambda:old*n}[key]()
            elif key=='clamp_variable':
                var=one(value,'var');data['vars'][var]=max(float(one(value,'min')),min(float(one(value,'max')),data['vars'].get(var,0)))
            elif key=='set_country_flag':data['flags'].add(value)
            elif key=='clr_country_flag':data['flags'].discard(value)
            elif key=='activate_mission':data['missions'].add(value)
            elif key=='remove_mission':data['missions'].discard(value)
            elif key=='add_dynamic_modifier':data['dynamic'].add(one(value,'modifier'))
            elif key=='remove_dynamic_modifier':data['dynamic'].discard(one(value,'modifier'))
            elif key=='country_event':self.pending.append((scope,one(value,'id')))
            elif key=='add_core_of':data['cores'].add(self.root if value=='ROOT' else value)
            elif key=='transfer_state_to':
                target=self.root if value=='ROOT' else value;data['owner']=data['controller']=target;self.countries[target]['exists']=True
            elif key=='add_claim_by':self.countries[value]['claims'].add(scope)
            elif key=='add_stability':data['stability']+=float(value)
            elif key=='set_stability':data['stability']=float(value)
            elif key=='set_cosmetic_tag':data['cosmetic']=value
            elif key=='set_politics':data['government']=one(value,'ruling_party')
            elif key=='create_wargoal':data.setdefault('goals',[]).append((one(value,'type'),one(value,'target')))
            else:raise AssertionError('Unmodeled Austrian effect '+str(key))

def main():
    p=argparse.ArgumentParser();p.add_argument('--game',type=Path,required=True);game=p.parse_args().game
    count=0
    def check(ok,message):
        nonlocal count
        count+=1
        if not ok:raise AssertionError(message)
    tree=one(read(ROOT/'common/national_focus/AUS_focuses.txt'),'focus_tree');fs={one(f,'id'):f for f in values(tree,'focus')}
    check(100<=len(fs)<=200,'Playability count outside requested 100–200')
    effects=dict((k,v) for k,v,o in read(ROOT/'common/scripted_effects/AUS_overhaul_effects.txt'))
    events={one(e,'id'):e for e in values(read(ROOT/'events/AUS_overhaul_events.txt'),'country_event')}
    decisions=one(read(ROOT/'common/decisions/AUS_decisions.txt'),'AUS_nww_crown_lands')
    native_decision_sprites=set(re.findall(r'name\s*=\s*"(GFX_decision_[^"]+)"',(game/'interface/decisions.gfx').read_text(encoding='utf-8-sig')))
    for category,items,op in read(ROOT/'common/decisions/AUS_decisions.txt'):
        for token,decision,operator in items:
            icon=one(decision,'icon')
            if icon:check((icon if icon.startswith('GFX_') else 'GFX_decision_'+icon) in native_decision_sprites,token+' uses an unknown decision icon')
    drift=one(decisions,'AUS_nww_bohemian_drift');talks=one(decisions,'AUS_nww_prague_negotiations')
    check(one(drift,'days_mission_timeout')=='60','Bohemian 60-day period')
    check(one(drift,'selectable_mission')=='no' and one(one(drift,'available'),'always')=='no','Bohemian mission manually completable')
    check(one(talks,'days_remove')=='20' and one(talks,'days_re_enable')=='0','Negotiations take more than twenty days per cycle')
    for start in range(10):
        w=World(effects,events);w.countries['AUS']['vars']['AUS_bohemian_tension']=start
        w.apply(one(drift,'timeout_effect'))
        check(w.countries['AUS']['vars']['AUS_bohemian_tension']==start+1,'Wrong drift increment')
        check(bool(w.pending)==(start==9),'Secession dispatched below threshold / omitted at threshold')
    for start in range(11):
        w=World(effects,events);w.countries['AUS']['vars']['AUS_bohemian_tension']=start
        w.apply(one(talks,'complete_effect',[]));check(w.countries['AUS']['vars']['AUS_bohemian_tension']==start,'Negotiations grant their reward immediately')
        w.apply(one(talks,'remove_effect'));check(w.countries['AUS']['vars']['AUS_bohemian_tension']==max(0,start-2),'Wrong completed negotiation reward')
    for terminal in ('AUS_nww_bohemia_settled','AUS_nww_bohemia_seceded'):
        w=World(effects,events);w.countries['AUS']['flags'].add(terminal);w.countries['AUS']['vars']['AUS_bohemian_tension']=9
        w.apply(one(drift,'timeout_effect'));check(not w.pending and w.countries['AUS']['vars']['AUS_bohemian_tension']==9,'Terminal crisis restarts')
        w.countries['AUS']['flags'].add('AUS_nww_overhaul_v1');w.countries['AUS']['missions'].add('AUS_nww_bohemian_drift');w.apply(effects['AUS_nww_initialize'])
        check('AUS_nww_bohemian_drift' not in w.countries['AUS']['missions'],'Settlement leaves a running timer')
    for occupied in (False,True):
        w=World(effects,events);w.countries['AUS']['vars']['AUS_bohemian_tension']=10
        if occupied:w.states['9']['controller']='GER'
        check(w.test(one(events['nww_aus_overhaul.1'],'trigger'))==(not occupied),'Secession transfers occupied capital')
    w=World(effects,events);w.states['69']['owner']=w.states['69']['controller']='GER';before=deepcopy(w.states)
    w.apply(effects['AUS_nww_release_bohemia'])
    check(all(w.states[str(s)]['owner']=='CZE' for s in (9,72,74,75)),'Bohemia does not receive its Austrian-held crown lands')
    check(w.states['69']==before['69'] and w.states['88']==before['88'] and w.states['4']==before['4'],'Secession takes third-party or unrelated territory')
    check('AUS' in w.states['9']['cores'] and 'CZE' in w.states['9']['cores'],'Secession destroys cores')
    entries=['AUS_reinstate_the_imperial_council','AUS_hold_elections','AUS_nww2_fascist_settlement','AUS_nww2_communist_settlement','AUS_nww2_alternative_settlement']
    for fid in entries:
        rivals={v for n in values(fs[fid],'mutually_exclusive') for v in values(n,'focus')}
        check(rivals==set(entries)-{fid},fid+' does not exclude all rival settlements')
        w=World(effects,events);w.countries['AUS']['focuses'].add(fid)
        check(w.test(one(fs['AUS_not_germany'],'available')),fid+' cannot reach the Hungarian path')
        check(one(one(fs[fid],'prerequisite'),'focus') in fs,fid+' lacks preparation')
    # The accepting recipient can only cede its own controlled land.
    for event_id,tag,states in [('nww_aus_overhaul.10','POL',(88,89,91)),('nww_aus_overhaul.11','ROM',(80,))]:
        w=World(effects,events);w.root=tag
        if len(states)>1:w.states[str(states[-1])]['owner']=w.states[str(states[-1])]['controller']='GER'
        before=deepcopy(w.states);accept=values(events[event_id],'option')[0]
        check(w.test(one(accept,'trigger')),event_id+' has no valid acceptance option')
        w.apply([n for n in accept if n[0] not in ('name','ai_chance','trigger')])
        for sid in states:
            s=str(sid);check(w.states[s]['owner']==('AUS' if before[s]['owner']==tag else before[s]['owner']),event_id+' transfers a foreign state')
    rebuild=effects['AUS_nww_rebuild_development'];initial={k:float(v) for n in values(rebuild,'set_variable') for k,v,o in n}
    expected={one(f,'id'):Counter({k:float(v) for n in values(one(f,'completion_reward',[]),'add_to_variable') for k,v,o in n if k in initial}) for f in values(tree,'focus')}
    replay={one(one(n,'limit'),'has_completed_focus'):Counter({k:float(v) for bonus in values(n,'add_to_variable') for k,v,o in bonus if k in initial}) for n in values(rebuild,'if') if one(one(n,'limit',[]),'has_completed_focus')}
    check({k:v for k,v in expected.items() if v}==replay,'Old-save replay loses/duplicates focus modifiers')
    check(not any(k in ('add_building_construction','create_unit','country_event','annex_country') for k,v,o in walk(rebuild)),'Save repair replays one-off rewards')
    native=set(re.findall(r'^## (\w+)',(game/'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig'),re.M))
    techs={k for path in (game/'common/technologies').glob('*.txt') for k,v,o in one(read(path),'technologies',[]) if isinstance(v,list)}
    for f in fs.values():
        for k,node,o in walk(one(f,'completion_reward',[])):
            if k=='set_technology':
                for technology,value,operator in node:check(technology in techs,'Invalid granted technology '+technology)
    for token,node,op in read(ROOT/'common/dynamic_modifiers/AUS_modifiers.txt'):
        for key,value,operator in node:
            if key not in ('enable','icon'):check(key in native,token+' unknown modifier '+key)
    for folder in ('common','events'):
        for path in (ROOT/folder).rglob('AUS*.txt'):check(not list(engine_script_errors(read(path))),str(path)+' contains unsupported native syntax')
    print(f'PASS: Austria overhaul: {len(fs)} playable focuses, {count} checks; five routes, source-script Bohemian drift/negotiations/secession, recipient-scoped ultimatums and reward-free save repair')

if __name__=='__main__':main()
