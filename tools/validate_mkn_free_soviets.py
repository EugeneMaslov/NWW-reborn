"""Execute Volin's slot caps, territorial defense, diplomacy and save reconstruction.

This is a static source interpreter, not an engine combat or UI reproduction.
"""
from copy import deepcopy
from decimal import Decimal
from itertools import permutations, product
import re

from hoi4_script import read, one, values, walk, tree_focuses, engine_script_errors
from validate_mkn_ukraine import World
from validate_mkn_military import MilitaryModel


FOCUSES = {
    'MKN_ferrer_modern_schools': (82,5,'MKN_pact_of_free_communes'),
    'MKN_sanctuary_of_free_thought': (82,6,'MKN_ferrer_modern_schools'),
    'MKN_eradication_of_wage_labor': (82,7,'MKN_sanctuary_of_free_thought'),
    'MKN_imperative_mandate': (86,6,'MKN_abolish_general_staff'),
    'MKN_syndicalist_work_ethic': (86,7,'MKN_imperative_mandate'),
    'MKN_consumer_autonomy': (86,8,'MKN_syndicalist_work_ethic'),
    'MKN_elected_instructor_collegiums': (82,8,'MKN_arms_to_the_people'),
    'MKN_volost_signal_chains': (82,9,'MKN_elected_instructor_collegiums'),
    'MKN_hearth_defense_doctrine': (82,10,'MKN_volost_signal_chains'),
    'MKN_subversion_of_enemy_ranks': (84,10,'MKN_beacon_of_statelessness'),
    'MKN_autonomous_free_communes': (84,11,'MKN_subversion_of_enemy_ranks'),
    'MKN_world_federation_of_labor': (84,12,'MKN_autonomous_free_communes'),
}


class SovietWorld(World):
    def __init__(self):
        super().__init__()
        self.targets, self.timed = {}, {}
        for tag in ('GER','AUS','ALB'):
            self.countries[tag] = deepcopy(self.countries['LTB'])
        self.countries['ALB']['exists'] = False
        self.countries['MKN']['government'] = 'democratic'
        self.countries['MKN']['focuses'] = {'MKN_autonomous_free_communes'}
        self.neighbors = {'MKN': {'UKR','LTB'}}
        self.states['9000'] = dict(owner='MKN',controller='MKN',cores={'ALB'},flags={},neighbors=(),dynamic={})
        self.states['9001'] = dict(owner='GER',controller='GER',cores={'GER'},flags={},neighbors=(),continent='europe',dynamic={})
        self.countries['GER']['capital'] = '9001'
        self.countries['AUS']['capital'] = '9001'
        self.countries['GER']['government'] = 'fascism'
        self.countries['AUS']['government'] = 'neutrality'

    def scope(self, token, current, previous):
        if token and token.startswith('event_target:'):
            return self.targets.get(token.split(':',1)[1])
        return super().scope(token,current,previous)

    def test(self, nodes, current='MKN', previous=None):
        for key,val,op in nodes or []:
            data = self.data(current)
            target = self.scope(val,current,previous) if isinstance(val,str) else None
            if key == 'has_dynamic_modifier':
                pair = (one(val,'modifier'),self.scope(one(val,'scope'),current,previous))
                expiry = data.get('dynamic',{}).get(pair)
                ok = expiry is not None and (expiry == -1 or expiry > self.day)
            elif key == 'any_core_state':
                ok = any(current in s['cores'] and self.test(val,sid,current) for sid,s in self.states.items())
            elif key == 'capital_scope':
                ok = data['capital'] is not None and self.test(val,data['capital'],current)
            elif key == 'is_on_continent': ok = data.get('continent','europe') == val
            elif key == 'is_core_of': ok = target in data['cores']
            elif key == 'is_owned_by': ok = data['owner'] == target
            elif key == 'is_owned_and_controlled_by': ok = data['owner'] == data['controller'] == target
            elif key == 'is_fully_controlled_by': ok = data['controller'] == target and not data.get('contested',False)
            elif key == 'is_neighbor_of': ok = current in self.neighbors.get(target,set())
            elif key == 'is_in_faction': ok = (data['faction'] is not None) == (val == 'yes')
            elif key == 'is_faction_leader': ok = (data['faction'] == current) == (val == 'yes')
            elif key == 'is_subject_of': ok = data.get('overlord') == target
            elif key == 'tag': ok = current == (target or val)
            else: ok = super().test([(key,val,op)],current,previous)
            if not ok: return False
        return True

    def apply(self, nodes, current='MKN', previous=None):
        matched = False
        for key,val,op in nodes:
            data = self.data(current)
            if key in {'if','else_if'}:
                if key == 'if': matched = False
                if not matched and self.test(one(val,'limit'),current,previous):
                    self.apply([n for n in val if n[0] != 'limit'],current,previous); matched = True
            elif key == 'else':
                if not matched: self.apply(val,current,previous)
                matched = True
            elif key == 'hidden_effect': self.apply(val,current,previous)
            elif key == 'every_country':
                for tag,c in self.countries.items():
                    if c['exists'] and self.test(one(val,'limit',[]),tag,current):
                        self.apply([n for n in val if n[0] != 'limit'],tag,current)
            elif key == 'save_event_target_as': self.targets[val] = current
            elif key in {'add_dynamic_modifier','remove_dynamic_modifier'}:
                pair = (one(val,'modifier'),self.scope(one(val,'scope'),current,previous))
                dynamic = data.setdefault('dynamic',{})
                if key == 'remove_dynamic_modifier': dynamic.pop(pair,None)
                else: dynamic[pair] = self.day + int(one(val,'days')) if one(val,'days') else -1
            elif key == 'add_opinion_modifier':
                data.setdefault('opinions',set()).add((self.scope(one(val,'target'),current,previous),one(val,'modifier')))
            elif key == 'add_timed_idea':
                idea = one(val,'idea'); data['ideas'].add(idea)
                self.timed[(current,idea)] = self.day + int(one(val,'days'))
            elif key == 'release':
                target = self.scope(val,current,previous)
                c = self.countries[target]
                c.update(exists=True,subject=True,overlord=current,faction=data['faction'])
                for sid,s in self.states.items():
                    if s['owner'] == current and target in s['cores']: s['owner'] = s['controller'] = target
            elif key == 'set_autonomy':
                assert one(val,'autonomy_state') == 'autonomy_free'
                assert one(val,'end_wars') == one(val,'end_civil_wars') == 'no'
                c = self.countries[self.scope(one(val,'target'),current,previous)]
                c.update(subject=False,overlord=None)
            elif key == 'remove_from_faction': self.countries[self.scope(val,current,previous)]['faction'] = None
            elif key == 'set_popularities': data['popularity'] = {k:float(v)/100 for k,v,o in val}
            elif key == 'set_politics':
                assert one(val,'ruling_party') and one(val,'elections_allowed') in {'yes','no'}
                data['government'] = one(val,'ruling_party')
            elif key == 'create_faction': data['faction'] = current
            elif key == 'add_to_faction':
                assert data['faction'] == current, 'Invite attempted by a faction member'
                self.countries[self.scope(val,current,previous)]['faction'] = current
            elif key == 'set_rule': data['rules'].update(k for k,v,o in val if v == 'yes')
            elif key == 'add_to_variable':
                for k,v,o in val:
                    if k != 'tooltip': data['variables'][k] = data['variables'].get(k,0) + float(v)
            else: super().apply([(key,val,op)],current,previous)

    def advance(self, days):
        self.day += days
        for pair,deadline in self.timed.items():
            if self.day >= deadline: self.countries[pair[0]]['ideas'].discard(pair[1])


def validate_free_soviets(root, game, check, localized):
    fs = {one(f,'id'):f for f in tree_focuses(one(read(root/'common/national_focus/MKN.txt'),'focus_tree'),root/'common/national_focus')}
    for fid,(x,y,parent) in FOCUSES.items():
        f = fs[fid]
        check((one(f,'x'),one(f,'y'),one(f,'cost')) == (str(x),str(y),'5'),fid+': incorrect coordinates/duration')
        available = one(f,'available')
        check(one(available,'has_government') == 'democratic',fid+': missing ideology gate')
        check(parent in values(one(f,'prerequisite',[]),'focus') + values(available,'has_completed_focus'),fid+': missing predecessor')
        localized(fid,fid);localized(fid+'_desc',fid)
    known = set(re.findall(r'^## (\w+)',(game/'documentation/modifiers_documentation.md').read_text(),re.M))
    # Ideology drift modifiers are generated from the installed ideology groups.
    known.update(k+'_drift' for k,v,o in one(read(game/'common/ideologies/00_ideologies.txt'),'ideologies'))
    ideas = one(one(read(root/'common/ideas/MKN_soviet_ideas.txt'),'ideas'),'country')
    for token,node,o in ideas:
        localized(token,token);localized(token+'_desc',token)
        check(all(k in known or k == 'custom_modifier_tooltip' for k,v,o in one(node,'modifier')),token+': unregistered modifier')
    for path in root.glob('common/**/MKN_soviet*.txt'):
        check(not list(engine_script_errors(read(path))),str(path)+': engine syntax error')
    cases = 0
    for initial in (3,4,5,6):
        for order in permutations(('MKN_ferrer_modern_schools','MKN_free_science_network','MKN_communal_research_network')):
            w = SovietWorld(); c=w.countries['MKN'];c['slots']=initial
            for fid in order:
                c['focuses'].add(fid);w.apply(one(fs[fid],'completion_reward'))
            check(c['slots'] == max(initial,5),'MKN schools: reward order exceeds five slots or removes earned slots')
            before = (c['slots'],c['pp'],deepcopy(w.states))
            w.run('MKN_repair_research_capacity');w.run('MKN_repair_research_capacity')
            check(before == (c['slots'],c['pp'],w.states),'MKN schools: slot repair replays rewards')
            cases += 1
    w=SovietWorld();w.apply(one(fs['MKN_eradication_of_wage_labor'],'completion_reward'))
    w.advance(119);check('MKN_voucher_transition_idea' in w.countries['MKN']['ideas'],'MKN vouchers: adaptation ends prematurely')
    w.advance(1);check('MKN_voucher_transition_idea' not in w.countries['MKN']['ideas'] and 'MKN_labor_vouchers_idea' in w.countries['MKN']['ideas'],'MKN vouchers: wrong temporary/permanent lifecycle')
    cases += 1
    for continent,government in product(('europe','asia'),('fascism','neutrality','democratic','communism')):
        w=SovietWorld();w.states['9001']['continent']=continent;w.countries['GER']['government']=government
        w.apply(one(fs['MKN_sanctuary_of_free_thought'],'completion_reward'))
        actual=('MKN','MKN_sanctuary_hostility') in w.countries['GER'].get('opinions',set())
        check(actual == (continent == 'europe' and government in {'fascism','neutrality'}),'MKN sanctuary: hostility applied to the wrong continent/regime')
        cases += 1
    # The damage-taken modifier must be attached to the enemy, never MKN.
    w=SovietWorld();c=w.countries['MKN']
    c['focuses'].update({'MKN_volost_signal_chains','MKN_subversion_of_enemy_ranks'})
    c['ideas'].add('MKN_enemy_subversion_idea');c['wars'].add('GER');w.countries['GER']['wars'].add('MKN')
    w.run('MKN_sync_people_defense');w.run('MKN_sync_people_defense')
    for sid,s in w.states.items():
        active=s['owner']==s['controller']=='MKN' and 'MKN' in s['cores']
        modifiers=s.get('dynamic',{})
        check((('MKN_people_defense_subversion','GER') in modifiers) == active,'MKN defense: hostile modifier escapes homeland or is missing')
        check(('MKN_people_defense_subversion','MKN') not in modifiers,'MKN defense: organization damage applied to own troops')
    signals=one(read(root/'common/dynamic_modifiers/MKN_soviet_modifiers.txt'),'MKN_people_defense_signals')
    for owned,controlled,core,government in product((False,True),(False,True),(False,True),('democratic','fascism')):
        w.states['9000'].update(owner='MKN' if owned else 'GER',controller='MKN' if controlled else 'GER',cores={'MKN'} if core else set())
        c['government']=government
        check(w.test(one(signals,'enable'),'9000') == (owned and controlled and core and government=='democratic'),'MKN defense: recovery enabled outside defended cores')
        cases += 1
    c['government']='democratic';c['wars'].clear();w.countries['GER']['wars'].clear();w.run('MKN_sync_people_defense')
    check(not any(('MKN_people_defense_subversion','GER') in s.get('dynamic',{}) for s in w.states.values() if s['owner']=='MKN'),'MKN defense: hostile modifier survives peace on owned land')
    for neighbor,war,exists,government in product((False,True),(False,True),(False,True),('democratic','fascism')):
        w=SovietWorld();m=w.countries['MKN'];m['exists']=exists;m['government']=government;m['ideas'].add('MKN_world_federation_idea')
        w.neighbors['MKN']={'LTB'} if neighbor else set()
        if war:w.countries['LTB']['wars'].add('MKN')
        w.countries['LTB']['ideas'].add('MKN_federation_influence_idea')
        w.run('MKN_sync_federation_influence');w.run('MKN_sync_federation_influence')
        check(('MKN_federation_influence_idea' in w.countries['LTB']['ideas']) == (neighbor and not war and exists and government=='democratic'),'MKN federation: influence survives lost eligibility')
        cases += 1
    decisions=one(read(root/'common/decisions/MKN_soviet_decisions.txt'),'MKN_free_communes_category')
    release=one(decisions,'MKN_release_free_commune')
    event=values(read(root/'events/MKN_soviet_events.txt'),'country_event')[0]
    for shared,occupied,war in product((False,True),repeat=3):
        w=SovietWorld();w.froms=('ALB','ALB','ALB')
        if shared:w.states['9000']['cores'].add('MKN')
        if occupied:w.states['9000']['controller']='GER'
        if war:w.countries['MKN']['wars'].add('GER')
        before=deepcopy(w.states)
        w.apply(one(release,'complete_effect'))
        eligible=not(shared or occupied or war)
        check(w.countries['ALB']['exists']==eligible,'MKN communes: illegal or missing release')
        if not eligible:check(w.states==before,'MKN communes: failed release changes ownership')
        cases += 1
    for accept,leader in product((False,True),repeat=2):
        w=SovietWorld();w.froms=('ALB','ALB','ALB')
        if leader:w.countries['MKN']['faction']='MKN'
        protected={sid:deepcopy(s) for sid,s in w.states.items() if 'MKN' in s['cores']}
        w.apply(one(release,'complete_effect'))
        check(w.countries['ALB']['government']=='democratic' and not w.countries['ALB']['subject'] and w.countries['ALB']['faction'] is None,'MKN communes: release is not sovereign/neutral before reply')
        check(all(w.states[sid]==s for sid,s in protected.items()),'MKN communes: release transfers an MKN core')
        w.root='ALB'
        option=values(event,'option')[0 if accept else 1]
        w.apply([n for n in option if n[0] not in {'name','trigger','ai_chance'}],'ALB')
        check((w.countries['ALB']['faction']=='MKN')==accept,'MKN communes: refusal ignored or consent not honored')
        check(not w.countries['ALB']['subject'],'MKN communes: consent makes a puppet')
        cases += 1
    for invalid in ('war','government','faction','expiry','source_government','source_subject','source_faction','source_war','source_capitulated','source_gone'):
        w=SovietWorld();w.froms=('ALB','ALB','ALB');w.apply(one(release,'complete_effect'));w.root='ALB'
        c=w.countries['ALB']
        if invalid=='war':c['wars'].add('GER')
        elif invalid=='government':c['government']='fascism'
        elif invalid=='faction':c['faction']='GER'
        elif invalid=='expiry':w.advance(30)
        elif invalid=='source_government':w.countries['MKN']['government']='fascism'
        elif invalid=='source_subject':w.countries['MKN']['subject']=True
        elif invalid=='source_faction':w.countries['MKN']['faction']='GER'
        elif invalid=='source_war':w.countries['MKN']['wars'].add('GER')
        elif invalid=='source_capitulated':w.countries['MKN']['capitulated']=True
        elif invalid=='source_gone':w.countries['MKN']['exists']=False
        before=c['faction']
        w.apply([n for n in values(event,'option')[0] if n[0] not in {'name','trigger','ai_chance'}],'ALB')
        check(c['faction']==before,'MKN communes: stale acceptance bypasses '+invalid)
        cases += 1
    effects={k:v for name in ('nww_mkn_progression','MKN_horizons_effects','MKN_militarist_effects','MKN_soviet_effects','MKN_communist_effects') for k,v,o in read(root/f'common/scripted_effects/{name}.txt')}
    for supply,signals in product((False,True),repeat=2):
        base=MilitaryModel(effects);base.apply(effects['nww_mkn_rebuild_industry']);base.rebuild()
        sim=MilitaryModel(effects,({'MKN_consumer_autonomy'} if supply else set())|({'MKN_volost_signal_chains'} if signals else set()))
        sim.apply(effects['nww_mkn_rebuild_industry']);sim.rebuild()
        check(sim.variables['MKN_unified_supply_consumption_factor']-base.variables['MKN_unified_supply_consumption_factor']==Decimal('-0.20')*supply,'MKN consumers: lost supply bonus')
        check(sim.variables['MKN_army_land_reinforce_rate']-base.variables['MKN_army_land_reinforce_rate']==Decimal('0.10')*signals,'MKN signals: lost reinforcement bonus')
        before=(dict(sim.variables),deepcopy(sim.oneoffs));sim.apply(effects['MKN_repair_soviet_progression']);sim.apply(effects['MKN_repair_soviet_progression'])
        check(before==(dict(sim.variables),sim.oneoffs),'MKN councils: save repair repeats rewards or stacks stats')
        cases += 1
    print(f'PASS: MKN Free Soviets: 12 focuses, research cap, territorial defense, sovereign release/consent and {cases} source-script cases; no engine combat claim')
