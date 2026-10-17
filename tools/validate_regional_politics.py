"""Regress the spectator audit against actual source scripts and installed definitions.

No engine scheduling, battles, rendering or army growth is simulated here.
"""
import argparse
from copy import deepcopy
from itertools import product
from pathlib import Path
import re
from hoi4_script import read, one, values, walk, tree_focuses, engine_script_errors
from validate_germany_politics import Scenario
from validate_mkn_ukraine import World as StateWorld

ROOT = Path(__file__).resolve().parents[1]


def validate_regional_politics(root, game, check):
    effects={k:v for p in (root/'common/scripted_effects').glob('*.txt') if p.name.startswith(('GER','POL')) for k,v,o in read(p)}
    events={one(v,'id'):v for p in (root/'events').glob('*.txt') if p.name in ('GER_events.txt','POL_events.txt','POL_political_events.txt') for k,v,o in read(p) if k=='country_event'}
    german={one(f,'id'):f for f in values(read(root/'common/national_focus/GER_political.txt'),'shared_focus')}
    tree=one(read(root/'common/national_focus/POL_focus.txt'),'focus_tree')
    polish={one(f,'id'):f for f in values(tree,'focus')}

    class World(Scenario):
        def __init__(self):
            super().__init__(effects,events)
            self.option,self.pick='DEFAULT',0
            self.triggers.update(dict((k,v) for k,v,o in read(root/'common/scripted_triggers/POL_triggers.txt')))
            self.countries['POL'].update(tree='POL_focus',original='POL')
        def condition(self,node,actor='GER',root=None,stack=()):
            for key,v,op in node:
                if key=='has_game_rule':answer=one(v,'option')==self.option
                elif key=='has_political_power':answer=self.compare(self.countries[actor]['pp'],float(v),op)
                elif key=='has_any_controlled_coastal_state':answer=False
                else:answer=super().condition([(key,v,op)],actor,root,stack)
                if not answer:return False
            return True
        # Do not split if/else chains: delegate the entire list to the base interpreter.
        def apply(self,node,actor='GER',root=None,stack=(),character=None):
            branch=False
            for key,v,op in node:
                if key in ('if','else_if','else'):
                    if key=='if':branch=False
                    if not branch and (key=='else' or self.condition(one(v,'limit',[]),actor,root,stack)):
                        self.apply([e for e in v if e[0]!='limit'],actor,root,stack,character);branch=True
                elif key=='random_list':self.apply([body for k,body,o in v if k and k.isdigit()][self.pick],actor,root,stack,character)
                elif key=='add_to_variable':
                    for k,amount,o in v:self.countries[actor]['variables'][k]=self.countries[actor]['variables'].get(k,0)+float(amount)
                elif key=='add_dynamic_modifier':self.countries[actor]['dynamic_modifiers'].add(one(v,'modifier'))
                else:super().apply([(key,v,op)],actor,root,stack,character)

    cases=0
    # Independence is not mistaken for recipient military readiness. Both AI countries may be weak.
    for target in ('POL','LTB'):
        w=World();w.ai=True;w.date='1939.1.1'
        w.countries['GER']['focuses'].add('GER_reign_in_mitteleuropa')
        w.countries[target].update(stability=0.1,war_support=0.1)
        w.countries[target]['wars'].add('SOV')
        w.apply(effects['nww_GER_mitteleuropa_demand'],target)
        check((target,'ger_crisis.20') in w.queue,'GER: recipient readiness still swallows the ultimatum')
        before=deepcopy(w.queue);w.apply(effects['nww_GER_mitteleuropa_demand'],target)
        check(w.queue==before,'GER: diplomatic retry spams a delivered demand')
        # Preserve the refusal through a recovery window, then actually issue the goal.
        w.countries[target]['wars'].clear();w.countries[target]['flags'].add('ger_mitteleuropa_refused')
        w.countries['GER']['flags'].add('NWW_GER_campaign_recovery')
        w.apply(effects['nww_GER_mitteleuropa_refusal_wargoals'])
        check(target not in w.countries['GER']['goals'] and 'ger_mitteleuropa_refused' in w.countries[target]['flags'],'GER: unsafe refusal is lost or awards a premature objective')
        w.countries['GER']['flags'].clear();w.apply(effects['nww_GER_mitteleuropa_refusal_wargoals'])
        check(target in w.countries['GER']['goals'],'GER: deferred refusal never becomes an objective')
        w.countries['GER']['goals'].clear();w.apply(effects['nww_GER_mitteleuropa_refusal_wargoals'])
        check(target in w.countries['GER']['goals'],'GER: expired objective cannot be restored')
        cases+=5
    for date,pressure,eastern in [('1938.12.31',False,False),('1939.1.1',True,False),('1940.1.1',True,True)]:
        w=World();w.ai=True;w.date=date
        check(w.condition(one(german['GER_reign_in_mitteleuropa'],'available'))==pressure,'GER: contradictory historical pressure date')
        check(w.condition(one(german['GER_crush_eastern_syndicates'],'available'))==eastern,'GER: contradictory historical eastern date')
        cases+=2
    # Diplomacy/army reform must remain selectable when another country has a stronger army.
    w=World();w.ai=True;w.date='1939.1.1';w.countries['GER'].update(strength=10)
    check(w.condition(one(german['GER_the_austrian_question'],'available')),'GER: military safety still blocks diplomatic preparation')
    w.countries['GER']['flags'].add('NWW_GER_campaign_recovery');w.date='1940.1.1'
    check(w.condition(one(german['GER_crush_eastern_syndicates'],'available')),'GER: recovery prevents the reform capstone prerequisite')
    cases+=2
    # Explicit paths work in either history mode; uncommitted random selection is stable.
    expected={'KAISER':'authoritarian','DEMOCRATIC':'democratic','FASCIST':'fascist','GER_ALT_FASCIST':'fascist','GER_COMMUNIST_STALINIST':'communist','GER_COMMUNIST_SPARTACUS':'communist'}
    for option,history in product(expected,(False,True)):
        w=World();w.ai=True;w.option=option;w.historical=history
        w.apply(effects['GER_nww_initialize_ai_route']);flags=w.countries['GER']['flags']
        check('GER_nww_ai_'+expected[option] in flags,'GER: explicit AI setting ignored')
        before=deepcopy(flags);w.option='RANDOM';w.apply(effects['GER_nww_initialize_ai_route'])
        check(flags==before,'GER: AI route changes after save reload');cases+=2
    for history,pick in product((False,True),range(4)):
        w=World();w.ai=True;w.option='RANDOM';w.historical=history;w.pick=pick
        w.apply(effects['GER_nww_initialize_ai_route'])
        check('GER_nww_ai_'+('authoritarian','democratic','fascist','communist')[pick] in w.countries['GER']['flags'],'GER: random AI route is biased by historical mode');cases+=1
    w=World();w.ai=True;w.apply(effects['GER_nww_initialize_ai_route'])
    check('GER_nww_ai_authoritarian' in w.countries['GER']['flags'],'GER: default history abandoned the Kaiser')
    decisions=one(read(root/'common/decisions/GER_bop_decisions.txt'),'GER_bop_decisions_category')
    w=World();w.countries['GER']['balance']=0;w.countries['GER']['flags'].add('GER_nww_ai_democratic')
    w.countries['GER']['focuses'].add('GER_empower_the_chancellor')
    decision=one(decisions,'GER_concede_to_parliament')
    for _ in range(5):
        check(w.condition(one(decision,'available')),'GER: parliamentary campaigning unavailable')
        w.countries['GER']['pp']-=50;w.apply(one(decision,'complete_effect'))
    check(w.countries['GER']['democratic']>=0.40 and w.countries['GER']['balance']>0.10,'GER: AI cannot build democratic mandate and BoP')
    cases+=2
    # A victorious dynamic-tag revolution must release its inherited readiness rule
    # and assess western targets against its own army, not the vanished loyalists.
    w=World();w.ai=True;w.date='1941.1.1'
    w.countries['D01']=deepcopy(w.countries['GER']);g=w.countries['D01']
    g.update(original='GER',government='communism',strength=100,stability=0.6,war_support=0.6)
    g['focuses'].add('GER_world_revolution');g['flags'].add('NWW_GER_declaration_rule_owned');g['rules'].add(('country','can_not_declare_war'))
    w.countries['GER']['exists']=False
    w.countries['FRA'].update(strength=100,faction='ENG',major=True)
    w.countries['ENG'].update(strength=100,faction='ENG',major=True)
    w.apply(effects['nww_GER_ai_refresh_declaration_rule'],'D01')
    check(('country','can_not_declare_war') not in g['rules'],'GER: dynamic successor retains the prewar declaration ban')
    check(w.condition(w.triggers['nww_GER_ai_can_target_FRA'],'D01'),'GER: dynamic successor still compares target strength to the vanished GER')
    w.apply(effects['GER_nww_refresh_western_wargoals'],'D01')
    check(g['goals']=={'FRA','ENG'},'GER: dynamic revolution loses its western objectives')
    cases+=3
    # Only the political opening is initially selectable. All other roots have an explicit gate.
    w=World();starting=[fid for fid,f in polish.items() if not values(f,'prerequisite') and w.condition(one(f,'available',[]),'POL')]
    check(starting==['POL_aftermath_of_the_marshal'],'POL: non-political roots bypass the opening')
    check(len({one(f,'icon') for f in polish.values()})>=30,'POL: focus art remains uniform')
    for lang in ('russian','english'):
        text=(root/f'localisation/{lang}/POL_nww_l_{lang}.yml').read_text(encoding='utf-8-sig')
        for f in polish.values():
            for k,v,o in walk(one(f,'completion_reward')):
                if k=='custom_effect_tooltip':check(re.search(r'^ '+re.escape(v)+':',text,re.M),f'POL: missing visible reward {v}/{lang}')
    # Opposed policies, real PP payment, delayed decisions and deterministic saved-program repair.
    policies=one(read(root/'common/decisions/POL_institution_decisions.txt'),'POL_institutional_politics')
    for route,eid,inst in [('sanation',50,'professional_civil_service'),('endecja',51,'national_bloc'),('german',52,'customs_commission'),('communist',53,'council_republic')]:
        for option in (0,1):
            w=World();s=w.countries['POL'];s['flags'].add('POL_path_'+route);s['focuses'].add('POL_'+inst)
            check(w.event('nww_pol.'+str(eid),'POL',option,sender='POL'),'POL: missing institutional event choice')
            check(s['pp']==150 and sum(flag.startswith('POL_policy_') for flag in s['flags'])==1,'POL: policy choice is unpaid or stacks both alternatives')
            before=deepcopy(s['variables']);w.apply(effects['POL_refresh_programs'],'POL');w.apply(effects['POL_refresh_programs'],'POL')
            check(s['variables']==before,'POL: repeated policy save repair stacks bonuses')
            groups={key.split('_')[1] for key,value in s['variables'].items() if abs(value)>0.00001}
            check({'POL_'+group+'_program' for group in groups}<=s['dynamic_modifiers'],'POL: policy promises a modifier before its service spirit exists')
            alternate=values(events['nww_pol.'+str(eid)],'option')[1-option]
            check(not w.condition(one(alternate,'trigger'),'POL'),'POL: opposed institutional option remains available')
            cases+=3
    for name,decision,o in policies:
        w=World();s=w.countries['POL']
        visible=one(decision,'visible');inst=one(visible,'has_completed_focus');route=one(visible,'has_country_flag')
        s['focuses'].add(inst);s['flags'].add(route)
        check(w.condition(visible,'POL') and w.condition(one(decision,'available'),'POL'),name+': not selectable after its institutions')
        s['pp']-=float(one(decision,'cost'));w.apply(one(decision,'complete_effect'),'POL')
        check(name not in s['flags'] and 'POL_institutional_project_active' in s['flags'],name+': timed project resolves immediately')
        w.apply(one(decision,'remove_effect'),'POL')
        check(name in s['flags'] and s['pp']==150 and 'POL_institutional_project_active' not in s['flags'],name+': paid completion failed')
        cases+=2
    # Paid LTB reserve law keeps the Vilnius settlement and date/war-support gates.
    reserve=one(one(read(root/'common/decisions/LTB_defence_decisions.txt'),'LTB_union_defence_category'),'LTB_expand_reserve_register')
    for problem in (None,'early','no_compromise','no_staff','dissolution','low_support','higher_law'):
        w=World();w.date='1938.1.1';state=w.countries['LTB']
        state['focuses'].update(('LTB_union_general_staff','LTB_the_vilnius_compromise'));state['ideas'].add('volunteer_only');state['war_support']=0.5
        if problem=='early':w.date='1937.12.31'
        if problem=='no_compromise':state['focuses'].discard('LTB_the_vilnius_compromise')
        if problem=='no_staff':state['focuses'].discard('LTB_union_general_staff')
        if problem=='dissolution':state['flags'].add('LTB_split_choice_available')
        if problem=='low_support':state['war_support']=0.25
        if problem=='higher_law':state['ideas']={'extensive_conscription'}
        ready=w.condition(one(reserve,'visible'),'LTB') and w.condition(one(reserve,'available'),'LTB')
        check(ready==(problem is None),'LTB: reserve law prerequisite failed: '+str(problem))
        if problem is None:
            state['pp']-=float(one(reserve,'cost'));w.apply(one(reserve,'remove_effect'),'LTB')
            check('limited_conscription' in state['ideas'] and state['pp']==125,'LTB: reserve law must be paid')
        cases+=1
    # Former MKN states are neither annexed nor cored merely by having a core claim.
    class IntegrationWorld(StateWorld):
        def __init__(self):
            super().__init__();self.root='UKR';self.froms=('1082',)
            self.triggers.update(dict((k,v) for k,v,o in read(root/'common/scripted_triggers/UKR_integration_triggers.txt')))
            self.states['1082'].update(compliance=50,resistance=10)
        def test(self,nodes,current='UKR',previous=None):
            for key,v,op in nodes or []:
                if key in ('compliance','resistance'):answer=self.compare(self.states[current].get(key,0),float(v),op)
                elif key=='is_core_of':answer=(self.scope(v,current,previous) or v) in self.states[current]['cores']
                elif key=='is_owned_and_controlled_by':answer=self.states[current]['owner']==self.states[current]['controller']==(self.scope(v,current,previous) or v)
                else:answer=super().test([(key,v,op)],current,previous)
                if not answer:return False
            return True
    d=one(one(read(root/'common/decisions/UKR_integration_decisions.txt'),'UKR_makhnovist_integration_category'),'UKR_integrate_makhnovist_region')
    for problem in (None,'MKN_exists','occupation_only','lost_control','already_core','war','low_compliance','resistance'):
        w=IntegrationWorld();s=w.states['1082'];c=w.countries['UKR'];s.update(owner='UKR',controller='UKR');w.countries['MKN']['exists']=False
        if problem=='MKN_exists':w.countries['MKN']['exists']=True
        if problem=='occupation_only':s['owner']='MKN'
        if problem=='lost_control':s['controller']='GER'
        if problem=='already_core':s['cores'].add('UKR')
        if problem=='war':c['wars'].add('SOV')
        if problem=='low_compliance':s['compliance']=30
        if problem=='resistance':s['resistance']=25
        available=w.test(one(d,'visible'),'UKR') and w.test(one(d,'available'),'UKR')
        check(available==(problem is None),'UKR: integration prerequisite failed: '+str(problem))
        if problem is None:
            c['pp']-=75;w.apply(one(d,'complete_effect'),'UKR');check('UKR' not in s['cores'],'UKR: no timed integration delay')
            w.day+=90;w.apply(one(d,'remove_effect'),'UKR');check('UKR' in s['cores'] and c['pp']==425,'UKR: paid integration failed')
        cases+=1
    for problem in ('MKN_exists','lost_control','war','resistance'):
        w=IntegrationWorld();s=w.states['1082'];c=w.countries['UKR'];s.update(owner='UKR',controller='UKR');w.countries['MKN']['exists']=False
        c['pp']-=75;w.apply(one(d,'complete_effect'),'UKR')
        if problem=='MKN_exists':w.countries['MKN']['exists']=True
        if problem=='lost_control':s['controller']='GER'
        if problem=='war':c['wars'].add('SOV')
        if problem=='resistance':s['resistance']=30
        if problem!='resistance':check(w.test(one(d,'cancel_trigger'),'UKR'),'UKR: interrupted project does not cancel')
        w.apply(one(d,'cancel_effect' if problem!='resistance' else 'remove_effect'),'UKR')
        check('UKR' not in s['cores'] and c['pp']==500 and not w.flag('UKR','UKR_makhnovist_integration_active'),'UKR: interrupted integration not refunded');cases+=1
    # Unique role ownership and affordable initial targets, with bounded training desires.
    generic=read(root/'common/ai_templates/generic.txt')
    native=read(game/'common/ai_templates/generic.txt');copy=deepcopy(generic)
    blocked=one(one(copy,'infantry_generic'),'blocked_for');blocked[:]=[e for e in blocked if e[1] not in ('LTB','MKN')]
    check(copy==native,'LTB/MKN: generic AI override changes unrelated countries')
    for tag,size,maximum in [('LTB',9,32),('MKN',3,16)]:
        templates=read(root/f'common/ai_templates/{tag}_templates.txt');infantry=one(templates,'infantry_'+tag+'_nww')
        start=one(infantry,tag+'_infantry_start');target=one(start,'target_template')
        check(one(one(target,'regiments'),'infantry')==str(size) and not one(target,'support'),'AI: starting target demands unaffordable battalions/companies '+tag)
        strategies=read(root/f'common/ai_strategy/{tag}_army.txt');recruit=one(strategies,tag+'_nww_recruit_field_army')
        check(('num_divisions',str(maximum),'<') in one(recruit,'enable'),'AI: unbounded recruiting '+tag)
        check(one(one(recruit,'enable'),'has_manpower')=='10000','AI: no manpower reserve for '+tag)
        check(not any(k in ('create_unit','add_equipment_to_stockpile','add_manpower') for k,v,o in walk(strategies)),'AI: free army workaround '+tag)
    # Validate changed country-owned scripts with strict engine syntax checks.
    for directory in ('common/decisions','common/scripted_effects','common/scripted_triggers','common/ai_strategy','common/ai_templates','events'):
        for path in (root/directory).glob('*.txt'):
            if path.name.startswith(('GER','POL','LTB','UKR','TUR_campaign')):
                for err in engine_script_errors(read(path)):check(False,path.name+': '+err)
    print(f'PASS: regional political audit: {cases} source-script scope/date/AI-route/policy/integration scenarios; Polish opening/art and bounded LTB/MKN template/recruitment definitions (not engine behaviour)')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--game',type=Path,required=True);a=p.parse_args();errors=[]
    validate_regional_politics(ROOT,a.game,lambda ok,msg:None if ok else errors.append(msg))
    for error in errors:print('ERROR:',error)
    raise SystemExit(bool(errors))
