"""Execute crown-charter source scripts, cached clicks and old-save reconciliation."""
from pathlib import Path
from itertools import product
from copy import deepcopy
from hoi4_script import read,one,values,variable_check

ROOT=Path(__file__).resolve().parents[1]
TRIGGERS=dict((k,v) for k,v,o in read(ROOT/'common/scripted_triggers/AUS_crownland_triggers.txt'))
EFFECTS=dict((k,v) for k,v,o in read(ROOT/'common/scripted_effects/AUS_crownlands_effects.txt'))
DECISION=one(one(read(ROOT/'common/decisions/AUS_crownland_development.txt'),'AUS_nww_crownland_development'),'AUS_nww_grant_crownland')
FLAG='AUS_nww_crownland_charter'

class World:
    def __init__(self):
        self.country={'flags':set(),'pp':150,'vars':{'AUS_bohemian_tension':0}}
        self.states={sid:{'owner':'AUS','controller':'AUS','flags':set(),'dynamic':set()} for sid in (4,9,152,153,848,976)}
        self.target=9
        self.timers={}
    def test(self,node,scope='country'):
        data=self.country if scope=='country' else self.states[scope]
        results=[]
        for k,v,o in node:
            if k=='FROM': result=self.test(v,self.target)
            elif k in TRIGGERS: result=self.test(TRIGGERS[k],scope)==(v=='yes')
            elif k=='NOT': result=not self.test(v,scope)
            elif k=='OR': result=any(self.test([n],scope) for n in v)
            elif k=='is_owned_and_controlled_by': result=data['owner']==data['controller']=='AUS'
            elif k=='has_state_flag' or k=='has_country_flag': result=v in data['flags']
            elif k=='has_dynamic_modifier': result=one(v,'modifier') in data['dynamic']
            elif k=='state': result=scope==int(v)
            elif k=='check_variable':
                var,val,op=variable_check(v); a=data['vars'][var]; b=float(val)
                result={'=':a==b,'>=':a>=b,'<=':a<=b,'<':a<b,'>':a>b}[op]
            else: raise AssertionError('Unmodeled trigger '+str(k))
            results.append(result)
        return all(results)
    def apply(self,node,scope='country'):
        data=self.country if scope=='country' else self.states[scope]
        matched=False
        for k,v,o in node:
            if k=='if':
                matched=self.test(one(v,'limit'),scope)
                if matched:self.apply([n for n in v if n[0]!='limit'],scope)
            elif k=='else':
                if not matched:self.apply(v,scope)
            elif k=='FROM':self.apply(v,self.target)
            elif k in EFFECTS:self.apply(EFFECTS[k],scope)
            elif k=='every_owned_state':
                for sid,s in self.states.items():
                    if s['owner']=='AUS' and self.test(one(v,'limit'),sid):self.apply([n for n in v if n[0]!='limit'],sid)
            elif k=='set_state_flag':data['flags'].add(v)
            elif k=='set_country_flag':
                flag=one(v,'flag') if isinstance(v,list) else v
                data['flags'].add(flag)
                if isinstance(v,list):self.timers[flag]=int(one(v,'days'))
            elif k=='add_dynamic_modifier':data['dynamic'].add(one(v,'modifier'))
            elif k=='add_political_power':data['pp']+=int(v)
            else:raise AssertionError('Unmodeled effect '+str(k))
    def click(self):
        self.country['pp']-=int(one(DECISION,'cost'))
        self.apply(one(DECISION,'complete_effect'))
    def days(self,count):
        for flag in list(self.timers):
            self.timers[flag]-=count
            if self.timers[flag]<=0:self.country['flags'].discard(flag);del self.timers[flag]

count=0
for flag,modifier,foreign_owner,foreign_control,cooldown in product((False,True),repeat=5):
    w=World();s=w.states[9]
    if flag:s['flags'].add(FLAG)
    if modifier:s['dynamic'].add(FLAG)
    if foreign_owner:s['owner']='GER'
    if foreign_control:s['controller']='GER'
    if cooldown:w.country['flags'].add('AUS_nww_charter_cooldown')
    valid=not any((flag,modifier,foreign_owner,foreign_control,cooldown))
    assert w.test(one(DECISION,'available'))==valid
    assert w.test(one(DECISION,'visible'))==(not any((flag,modifier,foreign_owner,foreign_control)))
    # A stale map target must refund the paid cost and must not grant a charter.
    before=deepcopy(s);w.click()
    assert w.country['pp']==(75 if valid else 150)
    if valid:assert FLAG in s['flags'] and FLAG in s['dynamic']
    else:assert before==s
    count+=1

w=World();w.click();assert not w.test(one(DECISION,'available'))
w.target=152;w.days(29);assert not w.test(one(DECISION,'available'))
w.days(1);assert w.test(one(DECISION,'available'));w.click();assert w.country['pp']==0
for flag,modifier in product((False,True),repeat=2):
    w=World();w.country['flags'].add('AUS_nww_charters_initialized')
    if flag:w.states[9]['flags'].add(FLAG)
    if modifier:w.states[9]['dynamic'].add(FLAG)
    w.apply(EFFECTS['AUS_nww_repair_charters'])
    assert (FLAG in w.states[9]['flags'])==(flag or modifier)
    assert (FLAG in w.states[9]['dynamic'])==(flag or modifier)
    snapshot=deepcopy((w.country,w.states));w.apply(EFFECTS['AUS_nww_repair_charters'])
    assert snapshot==(w.country,w.states)
w=World();w.apply(EFFECTS['AUS_nww_repair_charters'])
assert all(FLAG in w.states[s]['dynamic'] for s in (4,152,153,848,976))
assert FLAG not in w.states[9]['dynamic']
ui=one(one(read(ROOT/'common/scripted_guis/AUS_bohemian_gui.txt'),'scripted_gui'),'AUS_bohemian_ui')
for tension in range(11):
    w.country['vars']['AUS_bohemian_tension']=tension
    triggers=one(ui,'triggers')
    seals=[name for name,body,op in triggers if '_seal_' in name and w.test(body)]
    stages=[name for name,body,op in triggers if '_stage_' in name and w.test(body)]
    assert len(seals)==tension+1
    assert len(stages)==1
print(f'PASS: {count} source-script charter/cached-target combinations; shared 30-day timer, repeat click, 4 idempotent save repairs, hereditary setup and all 11 UI levels')
