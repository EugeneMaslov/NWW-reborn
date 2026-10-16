"""Exercise actual FRA source effects at political/pressure/save boundaries.

This small strict interpreter checks script semantics; it does not emulate the
HOI4 UI, engine event queue, AI focus scheduling or combat.
"""
from copy import deepcopy
from itertools import product
from datetime import date,timedelta
from pathlib import Path
from hoi4_script import read, one, values, variable_check

ROOT=Path(__file__).resolve().parents[1]
EFFECTS={k:v for k,v,o in read(ROOT/'common/scripted_effects/FRA_effects.txt')}
DECISIONS={k:v for cat,items,o in read(ROOT/'common/decisions/FRA_decisions.txt') for k,v,o in items}
TREE=one(read(ROOT/'common/national_focus/FRA_focuses.txt'),'focus_tree')
FOCUSES={one(v,'id'):v for v in values(TREE,'focus')}

class Model:
    def __init__(self):
        self.flags=set();self.completed=set();self.variables={};self.pp=200
        self.pop={'democratic':0.50,'neutrality':0.15,'communism':0.25,'fascism':0.10}
        self.ideas=set();self.dynamic=set();self.missions=set();self.held=set();self.calls=[]
        self.capitulated=False;self.ai=False
        self.day=0;self.date=date(1936,1,1);self.expiries={};self.completed_missions=set()
    def numeric(self,a,op,b):
        return {'=':a==b,'>':a>b,'<':a<b,'>=':a>=b,'<=':a<=b,'!=':a!=b}[op]
    def test(self,nodes):
        out=[]
        for k,v,o in nodes:
            if k=='OR':out.append(any(self.test([n]) for n in v))
            elif k=='AND':out.append(self.test(v))
            elif k=='NOT':out.append(not self.test(v))
            elif k=='has_country_flag':out.append(v in self.flags)
            elif k=='has_completed_focus':out.append(v in self.completed)
            elif k=='check_variable':
                key,value,op=variable_check(v);out.append(self.numeric(self.variables.get(key,0),op,float(value)))
            elif k=='has_dynamic_modifier':out.append(one(v,'modifier') in self.dynamic)
            elif k=='has_political_power':out.append(self.numeric(self.pp,o,float(v)))
            elif k in self.pop:out.append(self.numeric(self.pop[k],o,float(v)))
            elif k=='has_capitulated':out.append(self.capitulated==(v=='yes'))
            elif k=='is_ai':out.append(self.ai==(v=='yes'))
            elif k=='has_focus_tree':out.append(v=='french_focus')
            elif k=='always':out.append(v=='yes')
            elif k.startswith('FRA_holds_'):out.append((k.removeprefix('FRA_holds_') in self.held)==(v=='yes'))
            elif k=='any_other_country':out.append(False)
            elif k=='date':out.append(self.numeric(self.date,o,date(*map(int,v.split('.')))))
            else:raise AssertionError('Unsupported test '+str(k))
        return all(out)
    def apply(self,nodes):
        branch=False
        for k,v,o in nodes:
            if k in ('if','else_if'):
                run=(k=='if' or not branch) and self.test(one(v,'limit',[]))
                if k=='if':branch=False
                if run:self.apply([(a,b,c) for a,b,c in v if a!='limit']);branch=True
            elif k=='else':
                if not branch:self.apply(v)
                branch=False
            elif k in EFFECTS:self.apply(EFFECTS[k])
            elif k=='set_country_flag':
                name=one(v,'flag') if isinstance(v,list) else v
                value=float(one(v,'value',0)) if isinstance(v,list) else 1
                if value>0:self.flags.add(name)
                else:self.flags.discard(name)
                if isinstance(v,list) and one(v,'days') is not None:self.expiries[name]=self.day+int(one(v,'days'))
            elif k=='clr_country_flag':self.flags.discard(v);self.expiries.pop(v,None)
            elif k in ('set_variable','add_to_variable'):
                name,value=next((a,b) for a,b,c in v)
                self.variables[name]=(self.variables.get(name,0) if k=='add_to_variable' else 0)+float(value)
            elif k=='clamp_variable':
                name=one(v,'var');self.variables[name]=max(float(one(v,'min')),min(float(one(v,'max')),self.variables.get(name,0)))
            elif k=='add_political_power':self.pp+=float(v)
            elif k=='add_popularity':
                ideology=one(v,'ideology');self.pop[ideology]+=float(one(v,'popularity'))
            elif k=='add_ideas':self.ideas.add(v)
            elif k=='remove_ideas':self.ideas.discard(v)
            elif k=='add_dynamic_modifier':self.dynamic.add(one(v,'modifier'))
            elif k=='activate_mission':self.missions.add(v)
            elif k=='remove_mission':self.missions.discard(v)
            elif k=='custom_effect_tooltip':pass
            elif k=='set_politics':self.calls.append(('politics',one(v,'ruling_party')))
            elif k=='create_country_leader':self.calls.append(('leader',one(v,'name')))
            elif k=='country_event':self.calls.append(('country_event',one(v,'id')))
            elif k in ('add_stability','add_war_support'):self.calls.append((k,v))
            else:raise AssertionError('Unsupported effect '+str(k))
    def run(self,name):self.apply(EFFECTS[name])
    def advance(self,days):
        for _ in range(days):
            self.day+=1;self.date+=timedelta(days=1)
            for flag,expiry in list(self.expiries.items()):
                if self.day>=expiry:self.flags.discard(flag);del self.expiries[flag]
            self.run('FRA_daily')
    def scan_missions(self):
        for name,body in DECISIONS.items():
            if not one(body,'days_mission_timeout'):continue
            # The engine does not use visible to prevent automatic activation.
            if name not in self.missions and self.test(one(body,'activation',[])):
                self.missions.add(name)
            if name in self.missions and self.test(one(body,'available',[])):
                self.missions.discard(name);self.completed_missions.add(name)

cases=0
def check(ok,msg):
    global cases
    assert ok,msg
    cases+=1

# Initialization, repeated daily repair and one persistent spirit per system.
m=Model();m.run('FRA_initialize');snapshot=deepcopy((m.variables,m.flags,m.pp,m.ideas,m.dynamic,m.calls))
m.run('FRA_initialize')
check(snapshot==(m.variables,m.flags,m.pp,m.ideas,m.dynamic,m.calls),'Initialization must be idempotent')
check(len(m.dynamic)==6,'Expected exactly six persistent reform systems')

# Reproduce the screenshot's first 69 days; monthly changes must never become daily.
m=Model();m.run('FRA_initialize');m.held={r[0] for r in __import__('json').loads((ROOT/'docs/FRA_content.json').read_text(encoding='utf-8'))['regions']}
for days,mandate,pressure in [(29,35,35),(1,33,37),(29,33,37),(1,31,39),(9,31,39)]:
    m.advance(days)
    check(m.variables['FRA_mandate']==mandate,f'Day {m.day}: monthly mandate cadence failed')
    check(all(m.variables['FRA_'+r+'_pressure']==pressure for r in m.held),f'Day {m.day}: monthly pressure cadence failed')
check(m.variables['FRA_tension']==40,'Normal early campaign must not change street tension')
m.scan_missions();check(not m.missions and not m.completed_missions,'Inactive missions must not start or appear completed')
m.completed.add('FRA_nww_session');m.variables['FRA_mandate']=24;m.run('FRA_daily');m.scan_missions()
check('FRA_nww_confidence_vote' in m.missions and not m.completed_missions,'A real confidence vote must count down, not auto-complete')

# The reported empty focus must grant its actual +10 and universal +1 mandate.
m=Model();m.run('FRA_initialize');m.apply(one(FOCUSES['FRA_nww_accounts'],'completion_reward'))
check(m.variables['FRA_mandate']==46,'Publishing accounts must give 11 total mandate')
check(any(k=='custom_effect_tooltip' and 'mandate_gain_10' in v for k,v,o in one(FOCUSES['FRA_nww_accounts'],'completion_reward')),'Publishing accounts needs a visible reward tooltip')

# Strict, one-off recovery of the early 0/100 save shown by the user.
m=Model();m.flags.add('FRA_nww_initialized');m.date=date(1936,3,10);m.completed.add('FRA_nww_session')
m.variables={'FRA_mandate':0,**{'FRA_'+r+'_pressure':100 for r in ['algeria','maghreb','west_africa','equatorial','indochina','islands']}}
m.run('FRA_initialize')
check(m.variables['FRA_mandate']==32 and m.variables['FRA_algeria_pressure']==39,'Damaged March save repair must preserve completed focus gains')
check(m.pp==200 and not m.calls,'Counter repair must not replay PP, government changes or events')
m.variables['FRA_mandate']=20;m.run('FRA_initialize');check(m.variables['FRA_mandate']==20,'Migration must not reset counters twice')
m=Model();m.flags.add('FRA_nww_initialized');m.date=date(1937,1,1)
m.variables={'FRA_mandate':0,**{'FRA_'+r+'_pressure':100 for r in ['algeria','maghreb','west_africa','equatorial','indochina','islands']}}
m.run('FRA_initialize');check(m.variables['FRA_mandate']==0 and m.variables['FRA_algeria_pressure']==100,'Migration must not erase a genuine late-game crisis')

# Actual completed focuses restore stage values even if completion flags are lost.
for state,economy,army in product([False,True],repeat=3):
    m=Model()
    if state:m.completed.add('FRA_nww_renewal')
    if economy:m.completed.add('FRA_nww_internal_market')
    if army:m.completed.add('FRA_nww_signals_supply')
    m.run('FRA_initialize');m.run('FRA_update_spirits')
    check(m.variables['FRA_state_political_power_factor']==(0.05 if state else -0.15),'State repair stage')
    check(m.variables['FRA_economy_production_speed_buildings_factor']==(0.10 if economy else -0.10),'Economy repair stage')
    check(m.variables['FRA_army_land_doctrine_cost_factor']==(0 if army else 0.10),'Army repair stage')
    check(m.pp==200 and not m.calls,'Save repair must never repeat rewards or change government')

# 40% political mandates, including two neutrality routes and two communist routes.
for fid,ideology in [('crown_law','neutrality'),('league_state','fascism'),('social_republic','democratic'),('councils','communism'),('central_plan','communism'),('military_cabinet','neutrality')]:
    for support,expected in [(0.39,False),(0.395,False),(0.40,True),(0.65,True)]:
        m=Model();m.pop[ideology]=support;m.variables['FRA_mandate']=50
        check(m.test(one(FOCUSES['FRA_nww_'+fid],'available'))==expected,f'{fid}: mandate boundary at {support}')

# Crisis activation and negotiated settlement use the source's exact 80/60 boundaries.
for pressure,crisis in [(79,False),(80,True),(100,True)]:
    m=Model();m.run('FRA_initialize');m.flags.add('FRA_regime_settled');m.flags.add('FRA_algeria_investment');m.held.add('algeria')
    m.variables['FRA_algeria_pressure']=pressure+3
    m.run('FRA_monthly_tick')
    check(('FRA_nww_algeria_ultimatum' in m.missions)==crisis,'Regional crisis boundary')
for pressure,cancel in [(59,True),(60,False),(80,False)]:
    m=Model();m.held.add('algeria');m.variables['FRA_algeria_pressure']=pressure
    check(m.test(one(DECISIONS['FRA_nww_algeria_ultimatum'],'cancel_trigger'))==cancel,'Regional cancellation boundary')

# Paid negotiations lock simultaneously with other political campaigns; refunds clear the lock.
m=Model();m.run('FRA_initialize');d=DECISIONS['FRA_nww_coalition'];m.pp-=float(one(d,'cost'));m.apply(one(d,'complete_effect'))
check(not m.test(one(d,'available')),'Concurrent negotiations must be blocked')
m.capitulated=True;check(m.test(one(d,'cancel_trigger')),'Capitulation must cancel negotiations')
m.apply(one(d,'cancel_effect'));check(m.pp==200 and 'FRA_negotiation_busy' not in m.flags,'Cancellation must refund and unlock')

# Confidence votes cancel at 40, not at 39; low mandate activates exactly one mission.
for mandate,expected in [(39,False),(40,True)]:
    m=Model();m.variables['FRA_mandate']=mandate
    check(m.test(one(DECISIONS['FRA_nww_confidence_vote'],'cancel_trigger'))==expected,'Confidence restoration threshold')
m=Model();m.run('FRA_initialize');m.completed.add('FRA_nww_session');m.variables['FRA_mandate']=24;m.run('FRA_daily')
check('FRA_nww_confidence_vote' in m.missions,'Low mandate must activate confidence mission')

# All counters stay within 0..100, including imported damaged save values.
for value in [-500,500]:
    m=Model();m.variables={k:value for k in ['FRA_mandate','FRA_tension','FRA_algeria_pressure']};m.run('FRA_clamp_meters')
    check(all(0<=v<=100 for v in m.variables.values()),'Meter clamp failed')

# A coalition promise gets its own full deadline, not the remainder of a monthly tick.
m=Model();m.run('FRA_initialize');m.apply(one(DECISIONS['FRA_nww_coalition'],'remove_effect'))
check('FRA_coalition_deadline' in m.flags,'Coalition promise needs a separate 30-day grace period')
before=m.variables['FRA_mandate'];m.run('FRA_monthly_tick')
check(m.variables['FRA_mandate']==before-2,'Monthly tick must not shorten a new promise deadline')
m.flags.discard('FRA_coalition_deadline');m.run('FRA_daily')
check('FRA_coalition_promise' not in m.flags and m.variables['FRA_mandate']==before-7,'Expired promise must apply its penalty once')
snapshot=deepcopy(m.variables);m.run('FRA_daily');check(m.variables==snapshot,'Daily repair must not repeat a broken promise penalty')

class TerritoryModel:
    """Strict country/state scopes for the actual secession/autonomy effects."""
    def __init__(self,states,existing=(),dlc=True):
        self.states=deepcopy(states);self.existing=set(existing)|{'FRA','GER'}
        self.dlc=dlc;self.flags={};self.variables={};self.wars=set();self.subjects={}
    def test(self,nodes,scope='FRA'):
        result=[]
        for k,v,o in nodes:
            if k=='OR':result.append(any(self.test([n],scope) for n in v))
            elif k=='AND':result.append(self.test(v,scope))
            elif k=='NOT':result.append(not self.test(v,scope))
            elif k=='any_owned_state':result.append(any(s['owner']=='FRA' and self.test(v,i) for i,s in enumerate(self.states)))
            elif k=='is_controlled_by':result.append(self.states[scope]['controller']=='FRA')
            elif k=='is_core_of':result.append(v in self.states[scope]['cores'])
            elif k=='exists':result.append((scope in self.existing)==(v=='yes'))
            elif k=='has_dlc':result.append(self.dlc)
            elif len(k)==3 and k.isupper():result.append(self.test(v,k))
            else:raise AssertionError('Unhandled territorial trigger '+k)
        return all(result)
    def apply(self,nodes,scope='FRA'):
        matched=False
        for k,v,o in nodes:
            if k in ('if','else_if'):
                if k=='if':matched=False
                if not matched and self.test(one(v,'limit',[]),scope):
                    self.apply([(a,b,c) for a,b,c in v if a!='limit'],scope);matched=True
            elif k=='else':
                if not matched:self.apply(v,scope)
                matched=True
            elif k=='every_owned_state':
                for i,s in list(enumerate(self.states)):
                    if s['owner']=='FRA' and self.test(one(v,'limit',[]),i):self.apply([(a,b,c) for a,b,c in v if a!='limit'],i)
            elif k=='transfer_state_to':self.states[scope]['owner']=self.states[scope]['controller']=v;self.existing.add(v)
            elif k=='declare_war_on':self.wars.add(('FRA',one(v,'target')))
            elif k=='set_autonomy':self.subjects[one(v,'target')]='FRA'
            elif k=='puppet':self.subjects[v]='FRA'
            elif k=='set_country_flag':self.flags.setdefault(scope,set()).add(v)
            elif k=='set_variable':self.variables.update({a:float(b) for a,b,c in v})
            elif len(k)==3 and k.isupper():self.apply(v,k)
            else:raise AssertionError('Unhandled territorial effect '+k)

regions=__import__('json').loads((ROOT/'docs/FRA_content.json').read_text(encoding='utf-8'))['regions']
for region,ru,en,tags in regions:
    target=tags[0]
    for owner,controller,existing in product(['FRA','GER'],['FRA','GER'],[False,True]):
        initial=[{'owner':owner,'controller':controller,'cores':{target}},
                 {'owner':'GER','controller':'GER','cores':{target}},
                 {'owner':'FRA','controller':'GER','cores':{target}}]
        eligible=owner==controller=='FRA' and not existing
        for programme in ['release','war_release','autonomy']:
            m=TerritoryModel(initial,[target] if existing else [])
            m.apply(EFFECTS['FRA_'+programme+'_'+region])
            check(m.states[0]['owner']==(target if eligible else owner),f'{programme}: wrong transfer eligibility')
            check(m.states[1:]==initial[1:],f'{programme}: transferred foreign or occupied territory')
            check(bool(m.wars)==(eligible and programme=='war_release'),f'{programme}: declared war on an unrelated existing state')
            check(bool(m.subjects)==(eligible and programme=='autonomy'),f'{programme}: involuntary puppet or failed autonomy')
            snapshot=deepcopy((m.states,m.wars,m.subjects))
            m.apply(EFFECTS['FRA_'+programme+'_'+region])
            check(snapshot==(m.states,m.wars,m.subjects),f'{programme}: repeated territorial reward')

print(f'PASS: France {cases} real-script lifecycle checks: save repair, no replayed rewards, mandates, crisis boundaries, negotiation refunds and guarded territorial transfers/war/autonomy.')
