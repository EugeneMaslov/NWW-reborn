"""Execute actual ENG script blocks at mandate, consent and save boundaries.

Strict source interpreter, not an emulation of engine scheduling, UI or combat.
Unsupported operations fail instead of being silently ignored.
"""
from copy import deepcopy
from datetime import date
from pathlib import Path
from hoi4_script import read,one,values,variable_check

ROOT=Path(__file__).resolve().parents[1]
P='ENG_nww_'
EFFECTS={k:v for k,v,o in read(ROOT/'common/scripted_effects/ENG_effects.txt')}
DECISIONS={k:v for _,items,_ in read(ROOT/'common/decisions/ENG_decisions.txt') for k,v,o in items}
FOCUSES={one(v,'id'):v for v in values(one(read(ROOT/'common/national_focus/ENG_focuses.txt'),'focus_tree'),'focus')}
EVENTS={one(v,'id'):v for k,v,o in read(ROOT/'events/ENG_events.txt') if k=='country_event'}


class Country:
    def __init__(self,exists=True):
        self.exists=exists;self.flags=set();self.vars={};self.ideas=set();self.dynamic=set()
        self.completed=set();self.missions=set();self.pp=300;self.capitulated=False
        self.war=False;self.civil=False;self.tree='ENG_nww_focus';self.subject=None
        self.pop={'democratic':0.97,'fascism':0.02,'communism':0.01,'neutrality':0}
        self.faction='commonwealth';self.access=set();self.convoys=1000;self.factories=20
        self.stability=0.60


class World:
    def __init__(self):
        self.countries={t:Country() for t in ['ENG','CAN','AST','SAF','NZL','RAJ','IRE','MAL','BRM','OMA','TUR','USA','GER']}
        for tag in ['CAN','AST','SAF','NZL','RAJ','MAL','BRM','OMA']:self.countries[tag].subject='ENG'
        self.countries['NIR']=Country(False)
        self.states={'119':('ENG','ENG'),'132':('ENG','ENG'),'453':('ENG','ENG'),'681':('SAF','SAF'),'336':('MAL','MAL')}
        self.now=date(1938,2,1);self.rule='DEFAULT';self.historical=True;self.dlc=True;self.calls=[]
    def country(self,tag):return self.countries.setdefault(tag,Country(False))
    def num(self,a,op,b):
        return {'=':a==b,'>':a>b,'<':a<b,'>=':a>=b,'<=':a<=b,'!=':a!=b}[op]
    def test(self,node,ctx='ENG',root=None):
        root=root or ctx;c=self.country(ctx) if not ctx.isdigit() else None
        result=[]
        for k,v,o in node:
            if k=='OR':ok=any(self.test([n],ctx,root) for n in v)
            elif k=='AND':ok=self.test(v,ctx,root)
            elif k=='NOT':ok=not self.test(v,ctx,root)
            elif k in self.countries or (k and len(k)==3 and k.isupper()):ok=self.test(v,k,root)
            elif k and k.isdigit():ok=self.test(v,k,root)
            elif k=='controller':ok=self.test(v,self.states[ctx][1],root)
            elif k in ('is_owned_by','is_controlled_by','is_owned_and_controlled_by'):
                target=root if v=='ROOT' else v
                own,control=self.states[ctx]
                ok=(own==target if k=='is_owned_by' else control==target if k=='is_controlled_by' else own==control==target)
            elif k=='has_country_flag':ok=v in c.flags
            elif k=='has_completed_focus':ok=v in c.completed
            elif k=='has_dynamic_modifier':ok=one(v,'modifier') in c.dynamic
            elif k=='has_idea':ok=v in c.ideas
            elif k=='check_variable':
                key,value,op=variable_check(v);ok=self.num(c.vars.get(key,0),op,float(value))
            elif k in c.pop if c else False:ok=self.num(c.pop[k],o,float(v))
            elif k in ('has_capitulated','has_war','has_civil_war','exists','is_subject','is_in_faction'):
                value={'has_capitulated':c.capitulated,'has_war':c.war,'has_civil_war':c.civil,'exists':c.exists,'is_subject':c.subject is not None,'is_in_faction':c.faction is not None}[k]
                ok=value==(v=='yes')
            elif k=='has_war_with':ok=c.war and self.country(root if v=='ROOT' else v).war
            elif k=='is_subject_of':ok=c.subject==v
            elif k=='is_in_faction_with':ok=c.faction is not None and c.faction==self.country(v).faction
            elif k=='gives_military_access_to':ok=v in c.access
            elif k=='has_focus_tree':ok=c.tree==v
            elif k=='has_game_rule':ok=one(v,'option')==self.rule
            elif k=='has_government':ok=max(c.pop,key=c.pop.get)==v
            elif k=='has_dlc':ok=self.dlc
            elif k=='is_historical_focus_on':ok=self.historical==(v=='yes')
            elif k=='has_navy_size':
                size=next(n for n in v if n[0]=='size');ok=self.num(c.convoys,size[2],float(size[1]))
            elif k=='num_of_available_civilian_factories':ok=self.num(c.factories,o,float(v))
            elif k=='stability':ok=self.num(c.stability,o,float(v))
            elif k=='date':ok=self.num(self.now,o,date(*map(int,v.split('.'))))
            elif k in ('tag','original_tag'):ok=ctx==v
            elif k=='always':ok=v=='yes'
            else:raise AssertionError('Unsupported trigger '+str(k))
            result.append(ok)
        return all(result)
    def apply(self,node,ctx='ENG',root=None,params=None):
        root=root or ctx;params=params or {};branch=False
        for k,v,o in node:
            if isinstance(v,str):
                for key,value in params.items():v=v.replace('$'+key+'$',value)
            c=self.country(ctx) if not ctx.isdigit() else None
            if k in ('if','else_if'):
                if k=='if':branch=False
                if not branch and self.test(one(v,'limit',[]),ctx,root):
                    self.apply([n for n in v if n[0]!='limit'],ctx,root,params);branch=True
            elif k=='else':
                if not branch:self.apply(v,ctx,root,params)
                branch=False
            elif k in ('hidden_effect',):self.apply(v,ctx,root,params)
            elif k in self.countries or (k and len(k)==3 and k.isupper()):self.apply(v,k,root,params)
            elif k and k.isdigit():self.apply(v,k,root,params)
            elif k in EFFECTS:self.apply(EFFECTS[k],ctx,root,{a:b for a,b,_ in v} if isinstance(v,list) else params)
            elif k in ('set_variable','add_to_variable'):
                name,value,_=v[0]
                for key,val in params.items():value=value.replace('$'+key+'$',val)
                c.vars[name]=(c.vars.get(name,0) if k=='add_to_variable' else 0)+float(value)
            elif k=='clamp_variable':
                name=one(v,'var');c.vars[name]=max(float(one(v,'min')),min(float(one(v,'max')),c.vars.get(name,0)))
            elif k=='set_country_flag':c.flags.add(one(v,'flag') if isinstance(v,list) else v)
            elif k=='clr_country_flag':c.flags.discard(v)
            elif k=='add_dynamic_modifier':c.dynamic.add(one(v,'modifier'))
            elif k=='add_ideas':c.ideas.update([x for _,x,_ in v] if isinstance(v,list) else [v])
            elif k=='remove_ideas':c.ideas.discard(v)
            elif k=='add_timed_idea':c.ideas.add(one(v,'idea'))
            elif k=='add_political_power':c.pp+=float(v)
            elif k=='add_popularity':c.pop[one(v,'ideology')]+=float(one(v,'popularity'))
            elif k=='add_stability':c.stability+=float(v)
            elif k=='activate_mission':c.missions.add(v)
            elif k=='set_autonomy':self.country(one(v,'target')).subject=None if one(v,'autonomy_state')=='autonomy_free' else ctx
            elif k=='transfer_state_to':self.states[ctx]=(v,v);self.calls.append(('transfer',ctx,v))
            elif k=='load_focus_tree':c.tree=one(v,'tree')
            elif k=='random_list':
                self.calls.append(('random_list',ctx,None));self.apply(v[0][1],ctx,root,params)
            elif k in ('add_to_tech_sharing_group','remove_from_tech_sharing_group','add_opinion_modifier','country_event','random_owned_controlled_state','add_equipment_to_stockpile','declare_war_on','load_oob','start_civil_war','create_country_leader','promote_character','set_politics','recruit_character'):
                self.calls.append((k,ctx,deepcopy(v)))
            elif k in ('name','trigger','ai_chance','custom_effect_tooltip'):pass
            else:raise AssertionError('Unsupported effect '+str(k))
    def run(self,key):self.apply(EFFECTS[P+key])


def main():
    cases=0
    def check(ok,label):
        nonlocal cases
        cases+=1
        if not ok:raise AssertionError(label)
    # Four mandate boundaries, including values that a >0.39 approximation admits.
    for key,party in [('blackshirts','fascism'),('directory','neutrality'),('social_republic','communism'),('labour_election','democratic')]:
        for support,expected in [(0.39,False),(0.395,False),(0.40,True),(0.65,True)]:
            w=World();w.country('ENG').pop[party]=support;w.country('ENG').vars[P+'labour_mandate']=40
            check(w.test(one(FOCUSES[P+key],'available'))==expected,f'{key}: support {support}')
    # Explicit AI rules take priority over the historical setting.
    for rule,plan in [('DEFAULT','continuity'),('DEMOCRATIC_ALTERNATE','federal'),('FASCIST','fascist'),('NEUTRALITY','directory'),('COMMUNIST','republic'),('SOCIALIST','social'),('ISOLATION','island')]:
        w=World();w.rule=rule;w.run('choose_ai_plan')
        check(P+'plan_'+plan in w.country('ENG').flags,'Explicit AI rule '+rule)
    w=World();w.rule='RANDOM';w.run('choose_ai_plan')
    check(any(c[0]=='random_list' for c in w.calls),'Explicit RANDOM overrides historical mode')
    w=World();w.historical=False;w.run('choose_ai_plan')
    check(any(c[0]=='random_list' for c in w.calls),'Nonhistorical DEFAULT uses random plans')
    # Derived spirits reconstruct actual stages without granting anything twice.
    for route in [('industrial_survey','machine_tools','electric_grid','civil_reconstruction'),('blackshirts','corporate_chambers'),('expeditionary','overseas_supply'),('continental','reserve_act'),('escort','ocean_watch'),('strike','naval_strike_control')]:
        w=World();c=w.country('ENG');c.completed.update(P+k for k in route)
        w.run('rebuild_spirits');first=deepcopy(c.vars);c.dynamic.clear();w.run('rebuild_spirits')
        check(c.vars==first and len(c.dynamic)==6 and not w.calls,'Idempotent derived stage repair '+str(route))
    w=World();w.run('initialize');c=w.country('ENG');c.vars[P+'trust_CAN']=17
    w.run('initialize');check(c.vars[P+'trust_CAN']==17,'Initialization must not reset trust')
    w=World();w.run('initialize');c=w.country('ENG');c.completed.update({P+'machine_tools',P+'scientific_exchange',P+'colonial_review'})
    c.dynamic.clear();w.calls.clear();w.run('daily');first=deepcopy(c.vars);w.run('daily')
    check(c.vars==first and c.pp==300 and not any(call[0] in ('transfer','set_politics','random_owned_controlled_state','add_equipment_to_stockpile') for call in w.calls),'Daily repair replays no grants or politics')
    check(P+'science_unlocked' in c.flags and P+'decolonisation_unlocked' in c.flags,'Daily repair restores focus unlocks')
    # Starting routes and real access: enemy occupation cannot count as friendly.
    w=World();w.run('update_routes');check(w.country('ENG').vars[P+'open_routes']==3,'Starting sea arteries')
    w.states['453']=('ENG','GER');w.country('GER').faction=None;w.run('update_routes')
    check(w.country('ENG').vars[P+'route_suez']==0,'Occupied Suez blocks the route')
    w.country('GER').access.add('ENG');w.run('update_routes');check(w.country('ENG').vars[P+'route_suez']==1,'Negotiated access opens the route')
    w.country('GER').war=True;w.country('ENG').war=True;w.run('update_routes');check(w.country('ENG').vars[P+'route_suez']==0,'Enemy access cannot keep the route open')
    w=World();w.country('ENG').convoys=99;w.run('update_routes');check(w.country('ENG').vars[P+'open_routes']==0,'Transport threshold')
    # Every project refunds the paid cost and releases both the slot and factories.
    for key,d in DECISIONS.items():
        start=one(d,'complete_effect',[]);cancel=one(d,'cancel_effect',[])
        if not any(k=='set_country_flag' and v==P+'project_busy' for k,v,o in start):continue
        w=World();c=w.country('ENG');original=c.pp;c.pp-=float(one(d,'cost'));w.apply(start)
        check(P+'project_busy' in c.flags,key+': lock')
        w.apply(cancel)
        check(c.pp==original and P+'project_busy' not in c.flags and P+'project_cost' not in c.ideas,key+': refund')
    # Refusal never annexes or changes a government; acceptance needs a live offer.
    for index,tag in enumerate(['CAN','AST','SAF','NZL','RAJ']):
        for offset,mode in enumerate(['compact','federal','independence','investment']):
            ev=EVENTS['nww_eng.'+str(100+index*10+offset)]
            accept,refuse=values(ev,'option')
            w=World();check(not w.test(one(accept,'trigger'),tag),tag+mode+': no unsolicited acceptance')
            w.country('ENG').flags.add(P+'request_'+mode+'_'+tag)
            check(w.test(one(accept,'trigger'),tag),tag+mode+': valid consent')
            w.apply(refuse,tag);check(w.country(tag).subject=='ENG' and not any(c[0] in ('transfer','set_politics') for c in w.calls),tag+mode+': refusal leaves status')
            w=World();w.country('ENG').flags.add(P+'request_'+mode+'_'+tag);w.country(tag).subject='GER'
            check(not w.test(one(accept,'trigger'),tag),tag+mode+': third-party subject')
    # Independence can never be granted to a third country's dependency.
    accept=values(EVENTS['nww_eng.100'],'option')[0]
    w=World();w.country('ENG').flags.add(P+'request_compact_CAN');w.apply(accept,'CAN')
    check(P+'compact_CAN' in w.country('ENG').flags and not w.test(one(accept,'trigger'),'CAN'),'Offer consumed exactly once')
    # Irish agreement stops pressure regardless of focus order.
    w=World();w.country('ENG').flags.add(P+'irish_offer');opt=values(EVENTS['nww_eng.21'],'option')[0]
    check(w.test(one(opt,'trigger'),'IRE'),'Irish agreement can be accepted')
    w.apply(opt,'IRE');w.run('monthly');check(w.country('ENG').vars[P+'irish_pressure']==0,'Agreement stops Irish pressure')
    for pressure,expected in [(66,False),(67,True),(90,True)]:
        w=World();w.country('ENG').vars[P+'irish_pressure']=pressure;w.run('monthly')
        check((P+'irish_deadline' in w.country('ENG').missions)==expected,'Irish crisis activation boundary')
    for final in [False,True]:
        w=World();c=w.country('ENG');c.vars[P+'irish_pressure']=99
        if final:c.flags.add(P+'irish_final')
        w.run('monthly');check((P+'irish_deadline' in c.missions)==(not final),'Settled crisis never restarts')
    # A separatist warning is distinct from actual independence.
    w=World();c=w.country('ENG');c.vars[P+'trust_CAN']=24;w.run('monthly')
    check(P+'deadline_CAN' in c.missions and w.country('CAN').subject=='ENG','Warning must precede sovereignty demand')
    # Parliament needs two real ratifications, with surviving eligible signatories.
    w=World();c=w.country('ENG');c.flags.update({P+'federal_CAN',P+'federal_AST'});w.run('recount_partners')
    check(w.test(one(FOCUSES[P+'federal_parliament'],'available')),'Two ratifications open parliament')
    w.country('AST').exists=False;w.run('recount_partners')
    check(not w.test(one(FOCUSES[P+'federal_parliament'],'available')),'Missing signatory cannot count')
    print(f'PASS: ENG {cases} source-script mandate, AI-rule, save, consent, cancellation, route and crisis checks; no engine/runtime claim')


if __name__=='__main__':main()
