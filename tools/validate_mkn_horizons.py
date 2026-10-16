"""Run source-script regressions for MKN progress gates, cooldown and new branches.

Static models do not reproduce HOI4 combat, UI tooltips or AI diplomacy.
"""
import argparse
from collections import defaultdict
from copy import deepcopy
from decimal import Decimal
from itertools import product
import json
from pathlib import Path
import re

from hoi4_script import read, one, values, walk, engine_script_errors
from validate_mkn_military import MilitaryModel
from validate_mkn_frontier import FrontierModel
from validate_mkn_ukraine import World

ROOT = Path(__file__).resolve().parents[1]


class InvitationModel(World):
    def test(self, nodes, current='MKN', previous=None):
        for key, val, op in nodes or []:
            country = self.data(current)
            if key == 'is_in_faction':
                ok = (country['faction'] is not None) == (val == 'yes')
            elif key == 'is_faction_leader':
                ok = (country['faction'] == current) == (val == 'yes')
            elif key == 'has_civil_war':
                ok = country.get('civil_war', False) == (val == 'yes')
            elif key in {'has_non_aggression_pact_with','has_war_with'}:
                target = self.scope(val, current, previous) or val
                ok = target in country['pacts' if key == 'has_non_aggression_pact_with' else 'wars']
            else:
                ok = super().test([(key, val, op)], current, previous)
            if not ok:
                return False
        return True

    def apply(self, nodes, current='MKN', previous=None):
        # Invitation options contain only faction admission and flag cleanup.
        for key, val, op in nodes:
            if key == 'add_to_faction':
                target = self.scope(val, current, previous) or val
                self.countries[target]['faction'] = self.countries[current]['faction']
            else:
                super().apply([(key, val, op)], current, previous)


class HorizonsModel(MilitaryModel):
    def __init__(self, effects, triggers, focuses=()):
        super().__init__(effects, focuses)
        self.triggers = triggers
        self.equipment = defaultdict(int, motorized_equipment=100, convoy=20)
        self.aircraft = defaultdict(int, fighter=50)
        self.techs.add('motorised_infantry')
        self.war_major = False
        self.surrender = Decimal('0.1')
        self.date = '1943.1.1'
        self.offsite = 0
        self.factories = 5
        self.state_id = '1082'

    def test(self, nodes):
        for key, val, op in nodes or []:
            if key in self.triggers:
                ok = self.test(self.triggers[key]) == (val == 'yes')
            elif key == 'has_equipment':
                ok = all(self.compare(self.equipment[k], int(v), o) for k, v, o in val)
            elif key == 'has_deployed_air_force_size':
                _, v, o = next(n for n in val if n[0] == 'size')
                ok = self.compare(self.aircraft[one(val, 'type')], int(v), o)
            elif key == 'has_war_with_major':
                ok = self.war_major == (val == 'yes')
            elif key == 'surrender_progress':
                ok = self.compare(self.surrender, Decimal(val), op)
            elif key == 'date':
                ok = self.compare(tuple(map(int, self.date.split('.'))), tuple(map(int, val.split('.'))), op)
            elif key and key.isdigit():
                ok = self.test(val)
            elif key == 'state':
                ok = self.state_id == val
            elif key == 'is_core_of':
                ok = True
            else:
                ok = super().test([(key, val, op)])
            if not ok:
                return False
        return True

def validate_horizons(root, game, check, localized):
    effects = {k: v for name in ('nww_mkn_progression', 'MKN_horizons_effects', 'MKN_militarist_effects', 'MKN_soviet_effects', 'MKN_communist_effects')
               for k, v, o in read(root/f'common/scripted_effects/{name}.txt')}
    triggers = {k: v for k, v, o in read(root/'common/scripted_triggers/MKN_horizons_triggers.txt')}
    native_triggers = set(re.findall(r'^## (\w+)', (game/'documentation/triggers_documentation.md').read_text(), re.M))
    country_scopes = {p.name[:3] for p in (root/'history/countries').glob('*.txt')}
    def native_trigger_tree(nodes):
        for key, val, op in nodes:
            if key in triggers or key in native_triggers:
                continue
            check(key in {'FROM','ROOT','PREV','OR','AND','NOT'} | country_scopes, 'MKN horizons: unknown native trigger '+str(key))
            if isinstance(val,list): native_trigger_tree(val)
    for node in triggers.values(): native_trigger_tree(node)
    fs = {one(f, 'id'): f for f in values(one(read(root/'common/national_focus/MKN.txt'), 'focus_tree'), 'focus')}
    new = {one(f, 'id'): f for f in values(read(root/'common/national_focus/MKN_horizons_focuses.txt'), 'shared_focus')}
    manifest = json.loads((root/'docs/MKN_horizons.json').read_text())['branches']
    check(len(new) == 18 and all(len(ids) == 6 for ids in manifest.values()), 'MKN: expected three new six-focus branches')
    for fid in new:
        localized(fid, fid); localized(fid+'_desc', fid)
    techs = {k for p in (game/'common/technologies').glob('*.txt') for k, v, o in one(read(p), 'technologies', [])}
    for nodes in [*fs.values(), *new.values()]:
        for key, val, op in walk(nodes):
            if key == 'has_tech':
                check(val in techs, 'MKN: undefined installed technology '+val)
    for path in root.glob('common/**/MKN_horizons*.txt'):
        check(not list(engine_script_errors(read(path))), str(path)+': invalid engine script')
    for fid, f in new.items():
        check(one(f, 'cost') in {'5', '10'}, fid+': wrong cost')

    def model():
        return HorizonsModel(effects, triggers)
    cases = 0
    def gate(fid, sim, expected):
        nonlocal cases
        check(sim.test(one(fs.get(fid, new.get(fid)), 'available')) == expected, fid+': incorrect boundary')
        cases += 1

    for stock, tech, expected in ((99, True, False), (100, False, False), (100, True, True)):
        sim = model(); sim.equipment['motorized_equipment'] = stock
        if not tech: sim.techs.clear()
        gate('MKN_motorized_vanguard', sim, expected)
    for fid, resource, minimum in [('MKN_free_army_compact','army',35), ('MKN_mechanized_compact','army',35), ('MKN_free_sky_compact','air',25), ('MKN_air_support_compact','air',25)]:
        for xp in (minimum-1, minimum):
            sim = model(); sim.resources[resource] = xp
            gate(fid, sim, xp == minimum)
    for fid in ('MKN_interceptor_cooperatives', 'MKN_flying_artillery_focus'):
        for role, count in product(('fighter', 'cas'), (49, 50)):
            sim = model(); sim.aircraft.clear(); sim.aircraft[role] = count
            gate(fid, sim, count == 50)
    for fid in ('MKN_sea_escort_service', 'MKN_torpedo_artels_focus'):
        for stock, xp in product((19, 20), (14, 15)):
            sim = model(); sim.equipment['convoy'] = stock; sim.resources['navy'] = xp
            gate(fid, sim, stock == 20 and xp == 15)
    groups = json.loads((root/'docs/MKN_military_refactor.json').read_text())
    major = [g['id'] for g in groups['groups'] if g['id'] not in groups['roots'].values()]
    check(len(major) == 30, 'MKN: wrong major-reform count')
    for source in major:
        sim = model()
        # Execute the real reward to ensure every route imposes the shared lock.
        sim.apply(one(fs[source], 'completion_reward'))
        check(sim.ideas['MKN_military_reform_cooldown'] == 90, source+': missing 90-day cooldown')
        for target in major:
            gate(target, sim, False)
        sim.ideas['MKN_military_reform_cooldown'] -= 89
        gate(source, sim, False)
        sim.ideas['MKN_military_reform_cooldown'] -= 1
        gate(source, sim, True)
    for fid in manifest['defence']:
        for major_war, progress in product((False, True), ('0.1', '0.1001')):
            sim = model(); sim.war_major = major_war; sim.surrender = Decimal(progress)
            gate(fid, sim, major_war and progress == '0.1001')
    for day, radar, tools, expected in [('1936.1.1',False,False,True), ('1943.1.1',False,False,True), ('1940.1.1',False,True,True), ('1942.1.1',True,True,True)]:
        sim = model(); sim.date = day
        if radar: sim.techs.add('centimetric_radar')
        if tools: sim.techs.add('advanced_machine_tools')
        gate('MKN_free_science_network', sim, expected)
    stats = {
        'MKN_fund_the_underground': {'MKN_army_army_non_core_attack_factor':'0.1', 'MKN_army_army_non_core_defence_factor':'0.1'},
        'MKN_global_syndicalist_pact': {'MKN_army_send_volunteer_size':'3'},
        'MKN_death_or_freedom': {'MKN_army_conscription':'0.05'},
        'MKN_marusya_womens_battalions': {'MKN_army_army_org_regain':'0.1'},
        'MKN_shadows_in_the_forests': {'MKN_army_resistance_damage_to_garrison_on_our_occupied_states':'1'},
        'MKN_dnieper_jet_falcons': {'MKN_air_air_agility_factor':'0.05'},
    }
    for done in [set(), set(stats), *[{fid} for fid in stats]]:
        sim = model(); sim.focuses = done; sim.rebuild(); before = dict(sim.variables)
        for fid in done:
            for key, amount in stats[fid].items():
                check(sim.variables[key] == Decimal(amount), fid+': wrong persistent stat')
        sim.rebuild(); sim.rebuild()
        check(before == dict(sim.variables) and not sim.oneoffs, 'MKN: rebuild repeats rewards or compounds stats')
        cases += 1
    ideas = one(one(read(root/'common/ideas/MKN_horizons_ideas.txt'), 'ideas'), 'country')
    native_modifiers = set(re.findall(r'^## (\w+)', (game/'documentation/modifiers_documentation.md').read_text(), re.M))
    for name, idea, op in ideas:
        for key, val, op in one(idea,'modifier',[]):
            check(key in native_modifiers, name+': unknown installed modifier '+key)
    workshop = one(ideas, 'MKN_hidden_workshops'); sim = model()
    sim.apply(one(workshop, 'on_add')); sim.apply(one(workshop, 'on_add'))
    check(sim.offsite == 3, 'MKN: offsite factories stack')
    sim.apply(one(workshop, 'on_remove')); sim.apply(one(workshop, 'on_remove'))
    check(sim.offsite == 0, 'MKN: offsite removal stacks or leaves factories')
    ds = read(root/'common/decisions/MKN_horizons_decisions.txt')
    reactor = one(one(ds, 'MKN_economic_congress_category'), 'MKN_huliaipole_reactor_project')
    for owner, control, slots in product((False, True), repeat=3):
        sim = model(); sim.focuses.add('MKN_the_absolute_argument'); sim.techs.add('nuclear_reactor')
        sim.state.update(owner=owner, control=control, slots=slots)
        before = sim.resources['pp']; sim.resources['pp'] -= 100
        sim.apply(one(reactor, 'complete_effect'))
        cancel = sim.test(one(reactor, 'cancel_trigger'))
        sim.apply(one(reactor, 'cancel_effect' if cancel else 'remove_effect'))
        valid = owner and control and slots
        check(bool(sim.buildings['nuclear_reactor']) == valid, 'MKN: reactor built without its state')
        check(sim.resources['pp'] == before-(100 if valid else 0), 'MKN: reactor refund is incorrect')
        check('MKN_huliaipole_reactor_active' not in sim.flags, 'MKN: reactor project lock persists')
        if valid: check(not sim.test(one(reactor, 'visible')), 'MKN: completed reactor project can repeat')
        cases += 1
    ef = dict((k,v) for k,v,o in read(root/'common/scripted_effects/MKN_ukr_border_effects.txt'))
    tr = dict((k,v) for k,v,o in read(root/'common/scripted_triggers/MKN_ukr_border_triggers.txt'))
    for level, incident, allied, pact, border in product(range(1,6), (False,True), (False,True), (False,True), (False,True)):
        world = FrontierModel(ef,tr); world.run('mkn_ukr_initialize_frontier')
        c = world.countries['MKN']; c['variables']['mkn_ukr_escalation_level'] = level
        if incident: c['flags']['mkn_ukr_incident_fired'] = -1
        if allied: c['allies'].add('UKR')
        if pact: c['pacts'].add('UKR')
        world.border = border
        world.run('mkn_ukr_conclude_total_war'); world.run('mkn_ukr_conclude_total_war')
        expected = level == 5 and incident and not (allied or pact or border)
        check(world.declarations == ([('UKR','MKN')] if expected else []), 'MKN: premature, allied or duplicate Ukrainian attack')
        check(world.flag('UKR','UKR_mkn_offensive_limited') == expected, 'MKN: limited-war policy missing before attack')
        cases += 1
    # Legacy events must use the central gate rather than a second declaration path.
    legacy = read(root/'events/nww_mkn.txt')
    for e in values(legacy, 'country_event'):
        if one(e,'id') in {'mkn.2','mkn.4'}:
            check(not any(k == 'declare_war_on' for k,v,o in walk(e)), 'MKN: obsolete event bypasses escalation')
    event = next(e for e in values(read(root/'events/MKN_horizons_events.txt'), 'country_event') if one(e,'id') == 'mkn_horizons.1')
    accept, refuse = values(event, 'option')
    for existing_faction, subject, war, government in product((False,True), (False,True), (False,True), ('communism','democratic','fascism')):
        world = InvitationModel(); world.root = 'LTB'; world.froms = ('MKN','MKN','MKN')
        mkn, target = world.countries['MKN'], world.countries['LTB']
        mkn['faction'] = 'MKN'; mkn['flags']['MKN_black_international_founded'] = -1
        target['flags']['MKN_congress_invitation_pending'] = -1
        target.update(subject=subject, government=government, faction='SOV' if existing_faction else None)
        if war: target['wars'].add('MKN')
        permitted = not (existing_faction or subject or war) and government != 'fascism'
        check(world.test(one(accept,'trigger'),'LTB') == permitted, 'MKN: invitation can pull an ineligible recipient into the faction')
        # Refusal never changes a recipient's faction.
        before = target['faction']
        world.apply([n for n in refuse if n[0] not in {'name','ai_chance'}], 'LTB')
        check(target['faction'] == before, 'MKN: refusal changes faction')
        if permitted:
            target['flags']['MKN_congress_invitation_pending'] = -1
            world.apply([n for n in accept if n[0] not in {'name','ai_chance','trigger'}], 'LTB')
            check(target['faction'] == 'MKN', 'MKN: accepted invitation does not admit recipient')
        cases += 1
    # This verifies installed AI policy structure, not engine diplomacy behaviour.
    policies = read(root/'common/ai_strategy/MKN_ukr_limited_war.txt')
    outgoing = one(policies, 'UKR_mkn_do_not_call_allies')
    check(one(outgoing,'reversed') == 'yes' and one(outgoing,'abort_when_not_enabled') == 'yes', 'UKR: call policy has wrong relation direction/lifecycle')
    check(one(one(outgoing,'ai_strategy'),'target') == 'call_allies' and int(one(one(outgoing,'ai_strategy'),'value')) <= -1000, 'UKR: outgoing ally calls are not suppressed')
    for name, policy, op in policies:
        check(any(k == 'has_country_flag' and v == 'UKR_mkn_offensive_limited' for k,v,o in walk(one(policy,'enable'))), name+': policy is not restricted to the Ukrainian offensive campaign')
    for relation in ('none','ally','faction','pact','subject'):
        world = InvitationModel(); world.root = 'MKN'; world.froms = ('LTB','LTB','LTB')
        if relation == 'ally': world.countries['MKN']['allies'].add('LTB'); world.countries['LTB']['allies'].add('MKN')
        if relation == 'faction': world.faction('MKN','LTB')
        if relation == 'pact': world.countries['LTB']['pacts'].add('MKN')
        if relation == 'subject': world.countries['LTB']['subject'] = True
        check(world.test(world.triggers['MKN_horizons_hostile_target']) == (relation == 'none'), 'MKN: underground support targets protected countries')
        cases += 1
    for civil_war, government in product((False,True), ('communism','democratic','fascism','neutrality')):
        world = InvitationModel(); world.root = 'MKN'; world.froms = ('LTB','LTB','LTB')
        world.countries['MKN']['focuses'].add('MKN_global_syndicalist_pact')
        world.countries['LTB'].update(civil_war=civil_war, government=government)
        blocked = world.test(world.triggers['MKN_horizons_ineligible_volunteer_target'])
        check(blocked != (civil_war and government in {'communism','democratic'}), 'MKN: pact volunteer restriction has wrong recipients')
        cases += 1
    border_events = {one(e,'id'):e for e in values(read(root/'events/MKN_horizons_events.txt'),'country_event')}
    for sid, owned, allied in product(('80','89','90','500'), (False,True), (False,True)):
        world = InvitationModel(); world.countries['AUS'] = deepcopy(world.countries['LTB'])
        owner = 'AUS' if owned else 'SOV'
        world.states[sid] = dict(owner=owner,controller=owner,cores={owner},flags={},damage=0)
        world.froms = ('196','AUS',sid)
        world.countries['MKN']['flags']['MKN_galician_border_active'] = -1
        if allied: world.countries['MKN']['allies'].add('AUS')
        world.apply(one(border_events['mkn_horizons.10'],'immediate'))
        expected = 'MKN' if sid != '500' and owned and not allied else owner
        check(world.states[sid]['owner'] == expected, 'MKN: Austrian border victory transfers an unrelated, allied or third-party state')
        check(world.states[sid]['cores'] == {owner}, 'MKN: Austrian border victory grants an unsolicited core')
        cases += 1
    print(f'PASS: MKN horizons: 18 focuses, 30 reform locks and {cases} source-script boundary/lifecycle scenarios; no runtime AI/combat claim')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__); p.add_argument('--game',type=Path,required=True); args = p.parse_args()
    def check(ok,message):
        if not ok: raise AssertionError(message)
    def localized(key,context):
        for lang in ('russian','english'):
            check(any(re.search(r'^\s+'+re.escape(key)+r':\d*\s+"',path.read_text(encoding='utf-8-sig'),re.M) for path in (ROOT/'localisation').rglob('*l_'+lang+'.yml')), context+': missing '+lang+' '+key)
    validate_horizons(ROOT,args.game,check,localized)
