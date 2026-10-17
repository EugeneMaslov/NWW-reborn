"""Replay MKN expropriation, timed factories and elite deployment from source ASTs.

This covers script scope and lifecycle, not the engine's espionage UI or combat.
Unknown commands in executed branches fail rather than silently passing.
"""
import argparse
from copy import deepcopy
from itertools import product
from pathlib import Path
import re
import json

from hoi4_script import read, one, values, walk, engine_script_errors

MAJOR_TARGETS = ('GER','ENG','FRA','ITA','AUS','LTB','POL','SOV','UKR','SWE')

class InternationalModel:
    def __init__(self, root, effects, triggers, ideas, focuses):
        self.root_path, self.effects, self.triggers = root, effects, triggers
        self.ideas, self.focuses = ideas, focuses
        self.origin, self.target, self.day, self.dlc = 'MKN', 'GER', 0, True
        self.network, self.intel, self.roll = 31, 0.21, 0
        self.events, self.news, self.units = [], [], []
        self.state_owner = self.state_controller = 'MKN'
        self.countries = {tag:dict(original=tag, subject=None, exists=True, pp=200,
            equipment=1000, flags=set(), ideas={}, techs=set(), focuses=set(), wars=set(),
            goals={}, factories={'industrial_complex':0,'arms_factory':0}, characters=set(),
            army_xp=0, navy_xp=0, manpower=0, bonuses=[], rebuilds=0, variables={},
            civ_factories=20, continent='europe', balance=None, stability=0.5,
            war_support=0.5, faction=None, faction_template=None)
            for tag in ('MKN','GER','ENG','FRA','ITA','AUS','LTB','POL','SOV','UKR','SWE','AFG','TUR','USA','JAP','D01')}
        self.countries['D01']['original'] = 'MKN'
        for tag,continent in (('AFG','asia'),('TUR','asia'),('USA','north_america'),('JAP','asia')):
            self.countries[tag]['continent']=continent

    def scope(self, token):
        return {'ROOT':self.origin,'FROM':self.target}.get(token, token)

    def test(self, nodes, actor='MKN', previous=None):
        results=[]
        s=self.countries.get(actor,{})
        for k,v,op in nodes or []:
            if k=='NOT': result=not self.test(v,actor,previous)
            elif k in ('AND','OR'):
                parts=[self.test([n],actor,previous) for n in v]
                result=all(parts) if k=='AND' else any(parts)
            elif k in self.triggers: result=self.test(self.triggers[k],actor)==(v=='yes')
            elif k=='custom_trigger_tooltip':result=self.test([n for n in v if n[0]!='tooltip'],actor)
            elif k=='capital_scope':result=self.test(v,actor)
            elif self.scope(k) in self.countries or k=='1082': result=self.test(v,self.scope(k),actor)
            elif k=='always': result=v=='yes'
            elif k=='exists': result=s['exists']==(v=='yes')
            elif k=='original_tag': result=s['original']==v
            elif k=='is_on_continent':result=s['continent']==v
            elif k=='tag': result=actor==v
            elif k=='has_dlc': result=self.dlc
            elif k=='is_subject_of': result=s['subject']==self.scope(v)
            elif k=='has_variable':result=v in s['variables']
            elif k=='check_variable':
                key,operand,compare=next(n for n in v if n[0]!='tooltip')
                actual=s['variables'].get(key,0);expected=float(operand)
                result={'=':actual==expected,'>':actual>expected,'<':actual<expected}[compare]
            elif k=='num_of_civilian_factories':
                result={'=':s['civ_factories']==float(v),'>':s['civ_factories']>float(v),'<':s['civ_factories']<float(v)}[op]
            elif k=='has_power_balance':result=s['balance'] is not None
            elif k=='power_balance_value':
                _,operand,compare=next(n for n in v if n[0]=='value');actual=s['balance'];expected=float(operand)
                result=actual is not None and {'=':actual==expected,'>':actual>expected if actual is not None else False,'<':actual<expected if actual is not None else False}[compare]
            elif k=='has_faction_template':result=s['faction_template']==v
            elif k=='is_faction_leader':result=(s['faction']==actor)==(v=='yes')
            elif k=='is_in_faction_with':
                target=previous if v=='PREV' else self.scope(v)
                result=s['faction'] is not None and s['faction']==self.countries[target]['faction']
            elif k in ('has_country_flag','has_idea','has_tech','has_completed_focus','has_character'):
                field={'has_country_flag':'flags','has_idea':'ideas','has_tech':'techs',
                       'has_completed_focus':'focuses','has_character':'characters'}[k]
                result=v in s[field]
            elif k in ('has_war_with','has_wargoal_against'):
                result=self.scope(v) in s['wars' if k=='has_war_with' else 'goals']
            elif k=='is_owned_and_controlled_by':
                result=self.state_owner==self.state_controller==self.scope(v)
            elif k in ('network_strength','intel_level_over'):
                name='value' if k=='network_strength' else 'civilian_intel'
                threshold=next(n for n in v if n[0]==name)
                assert threshold[2]=='>' and one(v,'target')=='FROM'
                result=(self.network if k=='network_strength' else self.intel)>float(threshold[1])
            else: raise AssertionError(f'Unhandled international trigger: {k}')
            results.append(result)
        return all(results)

    def grant_idea(self, token, actor, expiry=None):
        s=self.countries[actor]
        fresh=token not in s['ideas']
        s['ideas'][token]=expiry
        if fresh: self.apply(one(self.ideas[token],'on_add',[]),actor)

    def advance(self, days):
        self.day+=days
        for actor,s in self.countries.items():
            for token,expiry in list(s['ideas'].items()):
                if expiry is not None and expiry<=self.day:
                    del s['ideas'][token]
                    self.apply(one(self.ideas[token],'on_remove',[]),actor)
            s['goals']={k:v for k,v in s['goals'].items() if v is None or v>self.day}

    def apply(self, nodes, actor='MKN'):
        s=self.countries[actor];matched=False
        for k,v,op in nodes or []:
            if k in ('if','else_if','else'):
                if k=='if': matched=False
                if not matched and (k=='else' or self.test(one(v,'limit',[]),actor)):
                    self.apply([n for n in v if n[0]!='limit'],actor);matched=True
            elif k in self.effects: self.apply(self.effects[k],actor)
            elif self.scope(k) in self.countries: self.apply(v,self.scope(k))
            elif k=='random_list':
                total=0
                for weight,branch,_ in v:
                    total+=int(weight)
                    if self.roll<total: self.apply(branch,actor);break
            elif k in ('set_variable','add_to_variable','subtract_from_variable','multiply_variable'):
                for key,amount,_ in v:
                    value=s['variables'].get(amount,0) if not str(amount).replace('.','',1).replace('-','',1).isdigit() else float(amount)
                    old=s['variables'].get(key,0)
                    s['variables'][key]=(value if k=='set_variable' else old*value if k=='multiply_variable' else old+(value if k=='add_to_variable' else -value))
            elif k=='clear_variable':s['variables'].pop(v,None)
            elif k=='add_political_power': s['pp']+=int(v)
            elif k=='add_stability':s['stability']+=float(v)
            elif k=='add_war_support':s['war_support']+=float(v)
            elif k=='add_power_balance_value':s['balance']=max(-1,min(1,s['balance']+float(one(v,'value'))))
            elif k=='add_equipment_to_stockpile': s['equipment']+=int(one(v,'amount'))
            elif k=='add_timed_idea': self.grant_idea(one(v,'idea'),actor,self.day+int(one(v,'days')))
            elif k=='modify_timed_idea':s['ideas'][one(v,'idea')]+=int(one(v,'days'))
            elif k=='add_ideas': self.grant_idea(v,actor)
            elif k=='remove_ideas':
                if v in s['ideas']:
                    del s['ideas'][v];self.apply(one(self.ideas[v],'on_remove',[]),actor)
            elif k=='set_technology':
                for token,level,_ in v:
                    (s['techs'].add if level=='1' else s['techs'].discard)(token)
            elif k=='add_offsite_building': s['factories'][one(v,'type')]+=int(s['variables'].get(one(v,'level'),0) if not str(one(v,'level')).lstrip('-').isdigit() else one(v,'level'))
            elif k in ('set_country_flag','clr_country_flag'):
                (s['flags'].add if k=='set_country_flag' else s['flags'].discard)(v)
            elif k=='create_wargoal': s['goals'][self.scope(one(v,'target'))]=self.day+int(one(v,'expire'))
            elif k=='country_event': self.events.append((actor,one(v,'id')))
            elif k=='news_event': self.news.append(one(v,'id'))
            elif k=='recruit_character': s['characters'].add(v)
            elif k=='add_tech_bonus': s['bonuses'].append(v)
            elif k in ('add_manpower','army_experience','navy_experience'):
                s[{'add_manpower':'manpower','army_experience':'army_xp','navy_experience':'navy_xp'}[k]]+=int(v)
            elif k=='complete_national_focus':
                if v not in s['focuses']:
                    s['focuses'].add(v);self.apply(one(self.focuses[v],'completion_reward',[]),actor)
            elif k=='nww_mkn_rebuild_services': s['rebuilds']+=1  # Replay tested by validate_focus_redesign.
            elif k=='load_oob':
                oob=read(self.root_path/f'history/units/{v}.txt')
                self.units.extend(deepcopy(values(one(oob,'units',[]),'division')))
                self.apply(one(oob,'instant_effect',[]),actor)
            elif k=='leave_faction':s['faction']=s['faction_template']=None
            elif k=='dismantle_faction':
                faction=s['faction']
                for country in self.countries.values():
                    if country['faction']==faction:country['faction']=country['faction_template']=None
            elif k=='custom_effect_tooltip':pass
            else: raise AssertionError(f'Unhandled international effect: {k}')


def validate_international(root, game, check, localized):
    files=[*root.glob('common/operations/MKN*.txt'),*root.glob('common/operation_phases/MKN*.txt'),
           *root.glob('common/*/MKN_international*.txt'),root/'common/characters/MKN.txt',
           root/'common/decisions/categories/MKN_international_categories.txt',
           root/'common/technologies/MKN_technologies.txt',root/'events/MKN_espionage_events.txt',
           root/'history/units/MKN_black_guard.txt',root/'history/units/MKN_black_guard_oob.txt']
    native={kind:set(re.findall(r'^## (\w+)',(game/f'documentation/{kind}_documentation.md').read_text(),re.M))
            for kind in ('effects','triggers','modifiers')}
    native['modifiers'] |= {'production_speed_'+kind+'_factor' for kind,node,o in one(read(game/'common/buildings/00_buildings.txt'),'buildings')}
    for path in files:
        for error in engine_script_errors(read(path)): check(False,f'{path.name}: {error}')
        for k,v,op in walk(read(path)):
            if k and re.match(r'^(add_|set_|clr_|create_|recruit_|load_|complete_)',k):
                check(k in native['effects'] or k in ('add_namespace','complete_effect'),f'{path.name}: undocumented effect {k}')
            if k in ('custom_effect_tooltip','custom_modifier_tooltip'): localized(v,path.name)
    for k in ('network_strength','intel_level_over','is_subject_of','is_owned_and_controlled_by'):
        check(k in native['triggers'],f'MKN international: undocumented trigger {k}')
    effects=dict((k,v) for k,v,o in read(root/'common/scripted_effects/MKN_international_effects.txt'))
    triggers=dict((k,v) for k,v,o in read(root/'common/scripted_triggers/MKN_international_triggers.txt'))
    ideas=dict((k,v) for k,v,o in one(one(read(root/'common/ideas/MKN_international_ideas.txt'),'ideas'),'country'))
    ideas.update((k,v) for k,v,o in one(one(read(root/'common/ideas/MKN_gameplay_ideas.txt'),'ideas'),'country'))
    tree=one(read(root/'common/national_focus/MKN.txt'),'focus_tree')
    focuses={one(f,'id'):f for f in values(tree,'focus')}
    op=one(read(root/'common/operations/MKN_operations.txt'),'mkn_expropriate_funds_operation')
    for k,v in {'days':'45','operatives':'1','network_strength':'30','return_on_complete':'no','cost_multiplier':'0'}.items():
        check(one(op,k)==v,f'MKN expropriation: incorrect {k}')
    check(one(one(op,'equipment'),'infantry_equipment')=='200','MKN expropriation: equipment cost changed')
    check(not {'on_success','on_fail'} & {k for k,v,o in op},'MKN expropriation: unsupported callback')
    make=lambda: InternationalModel(root,effects,triggers,ideas,focuses)
    cases=0
    for network,intel,dlc,subject,target,expected in (
        (30,0.21,True,None,'GER',False),(31,0.20,True,None,'GER',False),
        (31,0.21,True,None,'GER',True),(31,0.21,False,None,'GER',False),
        (31,0.21,True,'MKN','GER',False),(31,0.21,True,'SOV','GER',True),
        (31,0.21,True,None,'MKN',False),(31,0.21,True,None,'D01',False),
        (31,0.21,True,None,'AFG',False),(31,0.21,True,None,'USA',False),
        (31,0.21,True,None,'JAP',False),(31,0.21,True,None,'TUR',True)):
        m=make();m.network,m.intel,m.dlc,m.target=network,intel,dlc,target
        m.countries[target]['subject']=subject
        check((m.test(one(op,'allowed')) and m.test(one(op,'available')))==expected,f'MKN operation: bad eligibility {network,intel,dlc,subject,target}')
        cases+=1
    for callback in ('MKN_expropriation_success','MKN_expropriation_failure'):
        for dlc,target,subject in ((False,'GER',None),(True,'MKN',None),(True,'GER','MKN')):
            m=make();m.dlc,m.target=dlc,target;m.countries[target]['subject']=subject
            before=deepcopy(m.countries);m.apply(effects[callback])
            check(m.countries==before and not m.events and not m.news,f'{callback}: bypasses DLC/target guards')
            cases+=1
    for target in (*MAJOR_TARGETS,'TUR'):
        for roll in (0,79,80,99):
            m=make();m.target,m.roll=target,roll
            m.apply(one(op,'on_start'));m.apply(one(op,'outcome_execute'));s=m.countries['MKN'];t=m.countries[target]
            good=roll<80
            check(s['pp']==(250 if good else 150) and s['equipment']==(1500 if good else 1000),f'{target}: misplaced operation rewards')
            check(m.events==[(target,'mkn_espionage.1' if good else 'mkn_espionage.2')],f'{target}: wrong notification recipient')
            expected_news=[f'mkn_news.{10+MAJOR_TARGETS.index(target)}'] if good and target in MAJOR_TARGETS else []
            check(m.news==expected_news,f'{target}: incorrect world news dispatch')
            check(t['goals']==({} if good else {'MKN':60}),f'{target}: incorrect reprisal target/expiry')
            check(t['ideas'].get('MKN_bank_raid_aftermath')==(180 if good else None),f'{target}: missing or unearned 180-day bank penalty')
            check('MKN_bank_raid_aftermath' not in s['ideas'],f'{target}: robbery penalty applied to MKN')
            check(not m.test(one(op,'visible')),f'{target}: attempted operation remains visible')
            m.advance(179)
            check(('MKN_bank_raid_aftermath' in t['ideas'])==good,f'{target}: bank penalty expires early')
            m.advance(1)
            check('MKN_bank_raid_aftermath' not in t['ideas'] and s['factories']['industrial_complex']==0,f'{target}: bank penalty or leased factories survive expiry')
            cases+=1
    # Every wealth boundary is tested from launch, including later economic changes.
    for factories,pp,equipment,leased in ((0,25,300,1),(14,25,300,1),(15,50,500,2),(39,50,500,2),(40,75,750,3),(150,75,750,3)):
        m=make();m.countries['GER']['civ_factories']=factories
        m.apply(one(op,'on_start'))
        check(not m.test(one(op,'available')) and m.test(one(op,'requirements')),'Reservation cancels its own operation or permits a second attempt')
        m.countries['GER']['civ_factories']=1000
        m.apply(one(op,'on_start'))  # A second launch must not replace the snapshot.
        m.apply(one(op,'outcome_execute'));before=deepcopy(m.countries)
        m.apply(one(op,'outcome_execute'))
        q=m.countries['MKN']
        check(m.countries==before,'Duplicate completion grants rewards again')
        check(q['pp']==200+pp and q['equipment']==1000+equipment and q['factories']['industrial_complex']==leased,'Wealth snapshot/boundary reward incorrect')
        check(not m.test(one(op,'available')),'Resolved target becomes available again')
        cases+=1
    m=make();m.countries['GER']['civ_factories']=40
    m.apply(one(op,'on_start'));m.apply(one(op,'outcome_execute'));m.advance(100)
    m.target='POL';m.countries['POL']['civ_factories']=14
    m.apply(one(op,'on_start'));m.apply(one(op,'outcome_execute'))
    q=m.countries['MKN']
    check(q['factories']['industrial_complex']==4 and q['ideas']['MKN_expropriated_funds']==270,'Different targets do not stack or do not extend remaining time by exactly 90')
    m.advance(169);check(q['factories']['industrial_complex']==4,'Lease expires before the extended deadline')
    m.advance(1);check(q['factories']['industrial_complex']==0,'Aggregated factories survive expiry')
    m.apply(effects['MKN_repair_international_content']);m.apply(effects['MKN_repair_international_content'])
    check(q['factories']['industrial_complex']==0,'Factory repair subtracts twice')
    m.target='ENG';m.apply(one(op,'on_start'));m.apply(one(op,'outcome_execute'))
    check(q['factories']['industrial_complex']==2 and q['ideas']['MKN_expropriated_funds']==450,'New lease after expiry does not restart at 180 days')
    cases+=1
    # A cancelled launch consumes the attempt, even without an outcome callback.
    m=make();m.apply(one(op,'on_start'));m.advance(365)
    check(not m.test(one(op,'available')) and m.countries['MKN']['pp']==200,'Cancelled operation can be relaunched or grants rewards')
    cases+=1
    for flag,building,amount in (('MKN_expropriation_factories_active','industrial_complex',2),('MKN_spartacist_factory_active','arms_factory',1)):
        m=make();s=m.countries['MKN'];s['flags'].add(flag);s['factories'][building]=amount
        m.apply(effects['MKN_repair_international_content']);m.apply(effects['MKN_repair_international_content'])
        check(s['factories'][building]==0 and flag not in s['flags'],'Interrupted factory expiry repair subtracts incorrectly')
        cases+=1
    m=make();q=m.countries['MKN'];q['flags'].add('MKN_expropriation_factories_active')
    q['ideas']['MKN_expropriated_funds']=180;q['factories']['industrial_complex']=2
    m.apply(effects['MKN_repair_international_content']);before=deepcopy(q)
    m.apply(effects['MKN_repair_international_content'])
    check(q==before and q['variables'].get('MKN_expropriation_factories')==2,'Active old lease is re-awarded or loses its visible counter')
    m.advance(180);check(q['factories']['industrial_complex']==0,'Old fixed lease survives expiry')
    cases+=1
    for war,existing in product((False,True),repeat=2):
        m=make();target=m.countries['GER']
        if war: target['wars'].add('MKN')
        if existing: target['goals']['MKN']=None
        m.apply(one(op,'on_start'));m.apply(effects['MKN_expropriation_failure'])
        check(target['goals']==({'MKN':None} if existing else {} if war else {'MKN':60}),'Reprisal replaces an existing goal or grants a redundant one')
        if not existing and not war:
            m.advance(60);check(not target['goals'],'Reprisal remains after day 60')
        cases+=1
    decisions=one(read(root/'common/decisions/MKN_international_decisions.txt'),'mkn_black_international_category')
    check(len(decisions)==4,'MKN international: expected exactly four decisions')
    for token,decision,_ in decisions:
        localized(token,token);localized(token+'_desc',token)
        check(one(decision,'cost')=='50' and one(decision,'fire_only_once')=='yes',f'{token}: not once-only 50 PP')
        m=make()
        check(not m.test(one(decision,'available')),'International decision is available on day one')
        m.countries['MKN']['pp']-=50;m.apply(one(decision,'complete_effect'))
        check(m.countries['MKN']['pp']==200,'Locked invitation does not refund its PP')
        m.countries['MKN']['focuses'].add('MKN_black_international')
        check(m.test(one(decision,'available')),'International focus does not unlock the decision')
        m.countries['MKN']['pp']-=50;m.apply(one(decision,'complete_effect'))
        check(not m.test(one(decision,'available')),f'{token}: remains available')
        before=deepcopy(m.countries['MKN']);m.countries['MKN']['pp']-=50;m.apply(one(decision,'complete_effect'))
        check(m.countries['MKN']==before,f'{token}: repeated completion duplicates reward')
        m.advance(180)
        check(m.countries['MKN']['factories']['arms_factory']==0,f'{token}: temporary factory persists')
        if token=='MKN_welcome_cnt_fai_exiles':check(before['characters']=={'MKN_buenaventura_durruti'},'Durruti not recruited')
        if token=='MKN_harbor_spartacist_engineers':check(before['factories']['arms_factory']==1,'Engineers do not grant one factory')
        if token=='MKN_accept_italian_mechanics':
            b=before['bonuses'];check(len(b)==1 and one(b[0],'bonus')=='1.0' and one(b[0],'uses')=='1' and one(b[0],'category')=='motorized_equipment','Mechanics bonus is not shared and single-use')
        if token=='MKN_smuggle_kronstadt_sailors':check(before['manpower']==10000 and before['navy_xp']==15,'Sailor rewards changed')
        cases+=1
    memorial='MKN_memory_of_atamansha_marusya';elite='MKN_the_black_guard_battalions'
    check('MKN_black_guard_veterans' not in focuses,'Legacy focus still playable')
    check(one(one(focuses[memorial],'prerequisite'),'focus')=='MKN_steppe_general_staff','Memorial must connect directly to the common staff')
    for programme in ('MKN_steel_horses','MKN_batko_cavalry'):
        ancestors={memorial}
        while True:
            more={v for fid in ancestors for group in values(focuses[fid],'prerequisite') for v in values(group,'focus')}-ancestors
            if not more:break
            ancestors|=more
        check(programme not in ancestors,'Common memorial depends on an exclusive army programme')
    check(one(one(focuses['MKN_black_international'],'prerequisite'),'focus')=='MKN_departure_of_batko','International must follow Batko departure for every successor')
    check(not one(focuses['MKN_black_international'],'available') and not values(focuses['MKN_black_international'],'allow_branch'),'International still restricted to a political programme')

    check(one(one(focuses[elite],'prerequisite'),'focus')==memorial,'Elite focus disconnected from memorial')
    for ownership,engineers,recon,hospital in product((False,True),repeat=4):
        m=make()
        if not ownership:m.state_controller='UKR'
        m.countries['MKN']['techs']={t for t,yes in zip(('tech_engineers','tech_recon','tech_field_hospital'),(engineers,recon,hospital)) if yes}
        expected=ownership and engineers and recon and hospital
        check(m.test(one(focuses[elite],'available'))==expected,'Elite focus permits missing state/support tech')
        m.apply(one(focuses[elite],'completion_reward'));m.apply(one(focuses[elite],'completion_reward'))
        check(len(m.units)==(2 if expected else 0) and m.countries['MKN']['army_xp']==(20 if expected else 0),'Elite deployment duplicates or bypasses gates')
        cases+=1
    m=make();s=m.countries['MKN'];s['focuses'].add('MKN_black_guard_veterans')
    m.apply(effects['MKN_repair_international_content']);before=deepcopy(s)
    m.apply(effects['MKN_repair_international_content'])
    check(s==before and memorial in s['focuses'] and 'MKN_marusyas_legacy' in s['ideas'] and 'MKN_marusya_assault_training' in s['techs'],'Old-save memorial repair is not idempotent')
    check(not m.units and s['army_xp']==0,'Old-save repair repeats deployment/XP')
    cases+=1
    template=one(read(root/'history/units/MKN_black_guard.txt'),'division_template')
    check(one(template,'is_locked')=='yes' and one(template,'force_allow_recruiting')=='no' and one(template,'division_cap')=='2','Elite template is editable/recruitable')
    regiments=one(template,'regiments')
    check(len(values(regiments,'infantry'))==9 and len(values(regiments,'artillery_brigade'))==2 and len(regiments)==11,'Wrong elite line battalions')
    check({k for k,v,o in one(template,'support')}=={'engineer','recon','field_hospital'},'Wrong elite support companies')
    state=one(read(root/'history/states/1082-Huliaipole.txt'),'state')
    provinces={v for k,v,o in one(state,'provinces')}
    units=values(one(read(root/'history/units/MKN_black_guard.txt'),'units'),'division')
    check(len(units)==2,'Not exactly two elite divisions')
    for unit in units:
        check(one(unit,'location')=='429' and '429' in provinces,'Elite division outside Huliaipole')
        check(one(unit,'division_template')==one(template,'name') and one(unit,'start_experience_factor')=='1.0' and one(unit,'start_equipment_factor')=='1.0','Elite equipment/experience/template incorrect')
        check(not one(unit,'name').startswith('MKN_'),'Elite division displays a localization token')
    check(not one(template,'name').startswith('MKN_'),'Elite template displays a localization token')
    starting=read(root/'history/units/MKN_1936.txt')
    templates={one(t,'name') for t in values(starting,'division_template')}
    check(templates=={'Повстанческая дивизия','Конный отряд'},'Starting templates have no literal display names')
    for unit in values(one(starting,'units'),'division'):
        check(one(unit,'division_template') in templates,'Starting unit references a missing template')
    tech=one(one(read(root/'common/technologies/MKN_technologies.txt'),'technologies'),'MKN_marusya_assault_training')
    effective={p.name:p for p in (game/'common/units').glob('*.txt')};effective.update({p.name:p for p in (root/'common/units').glob('*.txt')})
    expected={token for p in effective.values() for token,node,_ in one(read(p),'sub_units',[])
              if 'category_army' in {v for k,v,o in one(node,'categories',[])} and float(one(node,'combat_width','0'))>0}
    actual={k for k,v,o in tech if isinstance(v,list) and one(v,'urban') is not None}
    check(actual==expected,'Urban training misses combat battalions or adds support stacking')
    for token in actual:check(one(one(one(tech,token),'urban'),'attack')=='0.15',f'{token}: wrong urban bonus')
    check(one(one(tech,'allow'),'always')=='no' and not values(tech,'folder'),'Memorial technology can be researched normally')
    for token,idea in ideas.items():
        localized(token,token);localized(token+'_desc',token)
        for k,v,o in one(idea,'modifier',[]):
            # Native idea metadata, used in common/ideas/ethiopia.txt, is not a stat.
            check(k in native['modifiers'] or k=='custom_modifier_tooltip',f'{token}: unsupported modifier {k}')
    char=one(one(read(root/'common/characters/MKN.txt'),'characters'),'MKN_buenaventura_durruti')
    commander=one(char,'corps_commander');localized(one(char,'name'),'Durruti')
    check(one(commander,'skill')=='4' and {v for k,v,o in one(commander,'traits')}=={'urban_assault_specialist','commando','trait_mountaineer'},'Durruti skill/traits changed')
    for path,kind in ((root/'events/MKN_espionage_events.txt','country_event'),(root/'events/MKN_news_events.txt','news_event')):
        evs={one(e,'id'):e for e in values(read(path),kind)}
        for token,event in evs.items():
            localized(one(event,'title'),token);localized(one(event,'desc'),token)
            for option in values(event,'option'):localized(one(option,'name'),token)
            if token.startswith('mkn_news.') and token!='mkn_news.1':check(one(event,'major')=='yes' and one(event,'is_triggered_only')=='yes',f'{token}: not major triggered news')
        if kind=='news_event':check({f'mkn_news.{i}' for i in range(10,20)}<=evs.keys(),'Missing heist news')
    for phase,node,_ in read(root/'common/operation_phases/MKN_operation_phases.txt'):
        for k in ('name','desc','outcome'):localized(one(node,k),phase)
        check(not values(node,'equipment'),'Operation phase adds hidden equipment costs')
    localized(one(op,'name'),'operation');localized(one(op,'desc'),'operation')
    for hook in ('on_startup','on_daily'):
        hooks=one(read(root/'common/on_actions/MKN_international_on_actions.txt'),'on_actions')
        check(any(k=='MKN_repair_international_content' for k,v,o in walk(one(hooks,hook))),f'{hook}: missing repair')
    # New BoP actions execute their real effects, expire, refund invalid queued
    # actions and respect frozen/removed meters on both countries.
    plans=json.loads((root/'docs/GER_MKN_bop_decisions.json').read_text())
    all_ideas=dict(ideas)
    for relative in ('common/ideas/GER_ideas.txt','common/ideas/MKN_ideas.txt'):
        all_ideas.update((k,v) for k,v,o in one(one(read(root/relative),'ideas'),'country'))
    for tag,specs in plans.items():
        category=one(read(root/('common/decisions/GER_bop_decisions.txt' if tag=='GER' else 'common/decisions/MKN_decisions.txt')),tag+'_bop_decisions_category')
        frozen='ger_bop_frozen' if tag=='GER' else 'MKN_bop_locked'
        for token,cost,cooldown,days,direction,icon,spirit,direct,stats in specs:
            decision=one(category,token);localized(token,token);localized(token+'_desc',token)
            localized(spirit,token);localized(spirit+'_desc',token)
            check(int(one(decision,'cost'))==cost and int(one(decision,'days_re_enable'))==cooldown and cooldown>=days,'BoP cost/cooldown shorter than its spirit')
            for modifier,value,operator in one(all_ideas[spirit],'modifier'):
                check(modifier in native['modifiers'],f'{spirit}: unsupported modifier {modifier}')
            for balance in (-0.4,0.4):
                m=make();m.origin=tag;m.ideas=all_ideas;q=m.countries[tag];q['balance']=balance
                check(m.test(one(decision,'available'),tag),f'{token}: ordinary use inaccessible')
                q['pp']-=cost;m.apply(one(decision,'complete_effect'),tag)
                check(q['pp']==200-cost and spirit in q['ideas'] and q['ideas'][spirit]==days,'BoP action fails to charge/grant the timed spirit')
                if direction=='center':check(abs(q['balance'])<abs(balance),'BoP compromise increases polarization')
                elif direction.startswith('left'):check(q['balance']<balance,'BoP action moves the wrong way')
                else:check(q['balance']>balance,'BoP action moves the wrong way')
                check(not m.test(one(decision,'available'),tag),'Same temporary programme can stack')
                m.advance(days);check(spirit not in q['ideas'],'Temporary BoP spirit never expires')
                cases+=1
            for balance,locked in ((None,False),(0.4,True)):
                m=make();m.origin=tag;m.ideas=all_ideas;q=m.countries[tag];q['balance']=balance
                if locked:q['flags'].add(frozen)
                before=deepcopy(q);q['pp']-=cost
                check(not m.test(one(decision,'available'),tag),'Frozen or absent meter permits new action')
                m.apply(one(decision,'complete_effect'),tag)
                check(q==before,'Invalid queued BoP action consumes PP or grants buffs')
                cases+=1
    # Only the obsolete Axis template is removed; accepted later factions survive.
    diplomacy=read(root/'common/scripted_effects/GER_diplomacy_effects.txt')
    for template,leader in ((None,True),('faction_template_axis',True),('faction_template_axis',False),('faction_template_GER_mitteleuropa',True)):
        m=make();m.effects.update((k,v) for k,v,o in diplomacy);q=m.countries['GER']
        q['faction_template']=template;q['faction']='GER' if leader else 'ITA'
        m.countries['POL']['faction']=q['faction'];m.countries['POL']['faction_template']=template
        m.apply(one(diplomacy,'nww_GER_remove_starting_axis'),'GER')
        removed=template=='faction_template_axis'
        check((q['faction'] is None)==removed,'GER Axis repair removes an unrelated faction or leaves Axis')
        check((m.countries['POL']['faction'] is None)==(removed and leader),'Axis cleanup removes unrelated members')
        before=deepcopy(m.countries);m.apply(one(diplomacy,'nww_GER_remove_starting_axis'),'GER')
        check(m.countries==before,'Axis cleanup is not idempotent')
        cases+=1
    history=read(root/'history/countries/GER - Germany.txt')
    for economic,austrian,accepted in ((True,False,False),(False,True,True),(False,True,False)):
        m=make();m.effects.update((k,v) for k,v,o in diplomacy);q=m.countries['GER']
        q['faction_template']='faction_template_axis';q['faction']='GER'
        if economic:q['focuses'].add('GER_mitteleuropa_economic_community')
        if austrian:q['focuses'].add('GER_the_austrian_referendum')
        if accepted:m.countries['AUS']['faction']='GER'
        m.apply(one(diplomacy,'nww_GER_remove_starting_axis'),'GER')
        check((q['faction']=='GER')==(economic or accepted),'Axis cleanup destroys a renamed old-save Mitteleuropa or preserves a refused alliance')
        cases+=1
    check(not values(history,'create_faction_from_template') and not values(history,'add_to_faction'),'GER still creates a starting faction')
    # Every newly added economic factory has its own guaranteed slot and is
    # confined to an owned, controlled core by the native iterator.
    factory_plan=json.loads((root/'docs/MKN_additional_factories.json').read_text())
    check(len(factory_plan)==5,'Expected five consolidated focuses with random core factory rewards')
    for fid,allocation in factory_plan.items():
        rewards=values(one(focuses[fid],'completion_reward'),'random_owned_controlled_state')
        selected=[b for b in rewards if one(one(b,'limit',[]),'is_core_of')=='ROOT']
        check(len(selected)==1 and one(selected[0],'add_extra_state_shared_building_slots')==str(allocation['slots']),f'{fid}: factory lacks guaranteed owned-core slots')
        if not selected:
            continue
        construction=values(selected[0],'add_building_construction')
        check({one(b,'type'):int(one(b,'level')) for b in construction}=={k:v for k,v in allocation.items() if k!='slots'} and all(one(b,'instant_build')=='yes' for b in construction),f'{fid}: factory reward differs')
    print(f'PASS: MKN expropriation/International/Marusya: {cases} source-script scenarios, timed factories, 10 news dispatches, two locked veteran divisions and {len(actual)} urban-trained battalions')


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--game',required=True,type=Path)
    args=parser.parse_args();root=Path(__file__).resolve().parents[1];errors=[]
    check=lambda ok,msg: errors.append(msg) if not ok else None
    locales={lang:{k for p in (root/f'localisation/{lang}').glob('*.yml') for k in re.findall(r'^\s+([\w.]+):',p.read_text(encoding='utf-8-sig'),re.M)} for lang in ('english','russian')}
    def localized(key,context):
        for lang,keys in locales.items():check(key in keys,f'{context}: missing {lang} {key}')
    validate_international(root,args.game,check,localized)
    for error in errors:print('ERROR:',error)
    raise SystemExit(bool(errors))


if __name__=='__main__':main()
