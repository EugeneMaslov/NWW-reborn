"""Execute MKN militarist district, DLC, trait and rebuild regression scenarios.

Static source-script models do not verify engine combat, tooltips or peace UI.
"""
from copy import deepcopy
from decimal import Decimal
from itertools import product
from pathlib import Path
import random
import re

from hoi4_script import read, one, values, walk, tree_focuses, engine_script_errors
from validate_mkn_military import MilitaryModel


FOCUSES = {
    'MKN_field_counter_intelligence': (74, 5, 'MKN_arrest_demagogues'),
    'MKN_disarming_the_communes': (74, 6, 'MKN_field_counter_intelligence'),
    'MKN_tribunals_of_the_black_staff': (74, 7, 'MKN_disarming_the_communes'),
    'MKN_labor_armies': (80, 8, 'MKN_standardize_workshops'),
    'MKN_schools_of_young_insurgents': (80, 9, 'MKN_labor_armies'),
    'MKN_cult_of_fallen_atamans': (80, 10, 'MKN_schools_of_young_insurgents'),
    'MKN_military_districts': (74, 9, 'MKN_tribunals_of_the_black_staff'),
    'MKN_council_of_field_commanders': (74, 10, 'MKN_military_districts'),
    'MKN_the_supreme_warlord': (74, 11, 'MKN_council_of_field_commanders'),
    'MKN_preemptive_strike_doctrine': (78, 11, 'MKN_the_black_horde'),
    'MKN_military_marches': (78, 12, 'MKN_preemptive_strike_doctrine'),
    'MKN_black_banner_over_europe': (78, 13, 'MKN_military_marches'),
}


class MilitaristModel:
    def __init__(self, dlc=False, seed=0):
        self.cp = Decimal(100)
        self.pp = 0
        self.gov = 'fascism'
        self.capitulated = False
        self.flags, self.ideas, self.focuses = set(), set(), {'MKN_military_districts', 'MKN_military_marches'}
        self.dlc = dlc
        self.leader_traits = {'mkn_iron_warlord'}
        self.tech = []
        self.rng = random.Random(seed)
        self.leaders = [{'army': i < 6, 'traits': set(), 'skill': [2,6,5,5,3,1,10,10][i]} for i in range(8)]
        self.effects = {k:v for k,v,o in read(Path(__file__).resolve().parents[1]/'common/scripted_effects/MKN_gameplay_effects.txt')}
        self.state = {'owned': True, 'controlled': True, 'fully': True, 'core': True,
                      'infrastructure': 2, 'flags': set(), 'modifiers': []}
        self.subject = {'subject': True, 'gov': 'fascism', 'autonomy': 'autonomy_puppet'}
        self.target = self.state
        self.active = None

    def test(self, nodes, scope=None):
        scope = self if scope is None else scope
        checks = []
        for k, v, op in nodes:
            if k == 'tooltip': continue
            if k in ('AND', 'custom_trigger_tooltip'): ok = self.test(v, scope)
            elif k == 'OR': ok = any(self.test([n], scope) for n in v)
            elif k == 'NOT': ok = not self.test(v, scope)
            elif k in ('ROOT', 'OVERLORD'): ok = self.test(v, self)
            elif k == 'FROM': ok = self.test(v, self.target)
            elif k == 'original_tag': ok = v == 'MKN'
            elif k == 'has_completed_focus': ok = v in self.focuses
            elif k == 'has_government': ok = (self.gov if scope is self else scope['gov']) == v
            elif k == 'has_capitulated': ok = self.capitulated == (v == 'yes')
            elif k == 'has_country_flag': ok = v in self.flags
            elif k == 'has_state_flag': ok = v in scope['flags']
            elif k == 'has_country_leader_with_trait': ok = v in self.leader_traits
            elif k == 'has_dlc': ok = self.dlc and v == 'La Resistance'
            elif k == 'is_army_leader': ok = scope['army'] == (v == 'yes')
            elif k == 'has_trait': ok = v in scope['traits']
            elif k == 'any_unit_leader': ok = any(self.test(v,leader) for leader in self.leaders)
            elif k == 'skill': ok = {'>':scope['skill']>int(v),'<':scope['skill']<int(v),'=':scope['skill']==int(v)}[op]
            elif k == 'is_owned_and_controlled_by': ok = scope['owned'] and scope['controlled']
            elif k == 'is_fully_controlled_by': ok = scope['fully']
            elif k == 'is_core_of': ok = scope['core']
            elif k == 'is_subject_of': ok = scope['subject']
            elif k == 'has_autonomy_state': ok = scope['autonomy'] == v
            elif k in ('command_power', 'infrastructure'):
                left = self.cp if k == 'command_power' else scope[k]
                right = Decimal(v)
                ok = {'<': left < right, '>': left > right, '=': left == right}[op]
            elif k == 'always': ok = v == 'yes'
            else: raise AssertionError('Unmodelled militarist trigger: '+str(k))
            checks.append(ok)
        return all(checks)

    def apply(self, nodes, scope=None):
        scope = self if scope is None else scope
        branch = None
        for k, v, _ in nodes:
            if k == 'if':
                branch = self.test(one(v, 'limit'), scope)
                if branch: self.apply([n for n in v if n[0] != 'limit'], scope)
            elif k == 'else_if':
                assert branch is not None
                if not branch and self.test(one(v,'limit'),scope):
                    self.apply([n for n in v if n[0]!='limit'],scope);branch=True
            elif k == 'else':
                assert branch is not None
                if not branch: self.apply(v, scope)
                branch = None
            elif k == 'FROM': self.apply(v, self.target)
            elif k == 'hidden_effect': self.apply(v,scope)
            elif k == 'custom_effect_tooltip': pass
            elif k == 'NWW_MKN_eugen': self.apply(v,self.leaders[0])
            elif k in self.effects: self.apply(self.effects[k],scope)
            elif k == 'add_command_power': self.cp += Decimal(v)
            elif k == 'add_political_power': self.pp += int(v)
            elif k == 'set_country_flag': self.flags.add(v)
            elif k == 'clr_country_flag': self.flags.discard(v)
            elif k == 'set_state_flag': scope['flags'].add(v)
            elif k == 'add_building_construction': scope[one(v, 'type')] += int(one(v, 'level'))
            elif k == 'add_dynamic_modifier': scope['modifiers'].append(v)
            elif k == 'add_ideas': self.ideas.add(v)
            elif k == 'add_tech_bonus': self.tech.append(v)
            elif k == 'custom_effect_tooltip': pass
            elif k == 'remove_country_leader_trait': self.leader_traits.discard(v)
            elif k == 'add_country_leader_trait': self.leader_traits.add(v)
            elif k == 'random_unit_leader':
                eligible = [x for x in self.leaders if self.test(one(v, 'limit'), x)]
                if eligible: self.apply([n for n in v if n[0] != 'limit'], self.rng.choice(eligible))
            elif k == 'add_unit_leader_trait': scope['traits'].add(v)
            elif k == 'set_autonomy':
                assert one(v, 'target') == 'FROM'
                assert one(v, 'end_wars') == one(v, 'end_civil_wars') == 'no'
                self.target['autonomy'] = one(v, 'autonomy_state')
            else: raise AssertionError('Unmodelled militarist effect: '+str(k))

    def can_start(self, decision):
        return self.active is None and all(self.test(one(decision, k, [])) for k in
            ('target_root_trigger', 'target_trigger', 'visible', 'available', 'custom_cost_trigger'))

    def start(self, decision):
        assert self.can_start(decision)
        self.apply(one(decision, 'complete_effect'))
        self.active = [int(one(decision, 'days_remove')), decision]

    def advance(self, days):
        for _ in range(days):
            if self.active is None: return
            self.active[0] -= 1
            _, d = self.active
            if self.test(one(d, 'cancel_trigger')):
                self.apply(one(d, 'cancel_effect')); self.active = None
            elif self.active[0] == 0:
                self.apply(one(d, 'remove_effect')); self.active = None


def validate_militarists(root, game, check, localized):
    tree = one(read(root/'common/national_focus/MKN.txt'), 'focus_tree')
    fs = {one(f, 'id'): f for f in tree_focuses(tree, root/'common/national_focus')}
    for fid, (x, y, parent) in FOCUSES.items():
        f = fs[fid]
        check((one(f, 'x'), one(f, 'y'), one(f, 'cost')) == (str(x), str(y), '5'), fid+': position/cost mismatch')
        check(values(one(f, 'prerequisite'), 'focus') == [parent], fid+': broken prerequisite')
        check(one(one(f, 'available'), 'has_government') == 'fascism', fid+': missing fascist gate')
        check(one(f, 'cancel_if_invalid') == 'yes', fid+': can continue after regime change')
        localized(fid, fid); localized(fid+'_desc', fid)
    check(one(one(fs['MKN_military_districts'], 'available'), 'has_completed_focus') == 'MKN_iron_fist_trains', 'MKN districts: missing second AND gate')
    for fid in ('MKN_pact_of_free_communes', 'MKN_grain_ultimatum', 'MKN_purge_irreconcilables'):
        gates = one(one(fs[fid], 'available'), 'custom_trigger_tooltip')
        sim = MilitaristModel()
        check(sim.test(gates), fid+': civil settlement is blocked before labor armies')
        sim.focuses.add('MKN_labor_armies')
        check(not sim.test(gates), fid+': labor armies do not block civil settlement')

    native_modifiers = set(re.findall(r'^## (\w+)', (game/'documentation/modifiers_documentation.md').read_text(), re.M))
    native_modifiers.update('production_speed_'+k+'_factor' for k, v, o in one(read(game/'common/buildings/00_buildings.txt'), 'buildings'))
    ideas = one(one(read(root/'common/ideas/MKN_militarist_ideas.txt'), 'ideas'), 'country')
    for iid, idea, _ in ideas:
        localized(iid, iid); localized(iid+'_desc', iid)
        check(all(k in native_modifiers or k == 'custom_modifier_tooltip' for k, v, o in one(idea, 'modifier')), iid+': unknown modifier')
    for file in ('common/unit_leader/MKN_militarist_traits.txt', 'common/country_leader/MKN_militarist_traits.txt'):
        for tid, _, _ in one(read(root/file), 'leader_traits'):
            localized(tid, file); localized(tid+'_desc', file)
    for path in root.glob('common/**/MKN_militarist*.txt'):
        check(not list(engine_script_errors(read(path))), str(path)+': engine syntax error')

    cases = 0
    for dlc in (False, True):
        sim = MilitaristModel(dlc)
        sim.apply(one(fs['MKN_field_counter_intelligence'], 'completion_reward'))
        check((sim.pp, len(sim.tech)) == ((0, 1) if dlc else (100, 0)), 'MKN counterintelligence: incorrect DLC fallback')
        check(sim.ideas == {('MKN_field_counter_intelligence_idea' if dlc else 'MKN_field_counter_intelligence_reserve_idea')}, 'MKN counterintelligence: inactive DLC spirit')
        cases += 1
    for seed in range(20):
        sim = MilitaristModel(seed=seed)
        sim.apply(one(fs['MKN_council_of_field_commanders'], 'completion_reward'))
        chosen = [x for x in sim.leaders if 'mkn_council_member_trait' in x['traits']]
        check(len(chosen) == 3 and all(x['army'] for x in chosen) and sim.leaders[0] in chosen and sorted(x['skill'] for x in chosen)==[2,5,6], 'MKN council: Eugen missing, lower-skilled commander/admiral or repeated draw')
        cases += 1
    sim = MilitaristModel()
    sim.apply(one(fs['MKN_the_supreme_warlord'], 'completion_reward'))
    check(sim.leader_traits == {'mkn_supreme_warlord'}, 'MKN supreme warlord: old trait remains')

    decisions = read(root/'common/decisions/MKN_military_decisions.txt')
    district = one(one(decisions, 'MKN_military_districts_decisions'), 'MKN_fortify_military_district')
    for owned, controlled, core, gov, infra, cp in product((False, True), (False, True), (False, True), ('fascism', 'communism'), (4, 5), (19, 20)):
        sim = MilitaristModel(); sim.gov = gov; sim.cp = Decimal(cp)
        sim.state.update(owned=owned, controlled=controlled, core=core, infrastructure=infra)
        expected = owned and controlled and core and gov == 'fascism' and infra < 5 and cp >= 20
        check(sim.can_start(district) == expected, 'MKN districts: invalid start boundary')
        cases += 1
    sim = MilitaristModel(); sim.start(district)
    check(sim.cp == 80, 'MKN districts: CP not paid immediately')
    sim.advance(29)
    check(sim.state['infrastructure'] == 2 and not sim.state['modifiers'], 'MKN districts: rewards arrive before day 30')
    sim.advance(1)
    check(sim.cp == 80 and sim.state['infrastructure'] == 4 and 'MKN_district_fortified' in sim.state['flags'], 'MKN districts: missing completion reward')
    check(one(sim.state['modifiers'][0], 'scope') == 'ROOT', 'MKN districts: defense granted to an occupier')
    check(not sim.can_start(district), 'MKN districts: repeatable infrastructure reward')
    for infrastructure in (0, 1, 3, 4):
        sim = MilitaristModel(); sim.state['infrastructure'] = infrastructure
        sim.start(district); sim.advance(30)
        check(sim.state['infrastructure'] == min(infrastructure + 2, 5), 'MKN districts: wrong doubled construction reward or infrastructure cap exceeded')
        cases += 1
    for change in ('owned', 'controlled', 'fully', 'core', 'gov', 'capitulated', 'infrastructure'):
        sim = MilitaristModel(); sim.start(district)
        if change == 'gov': sim.gov = 'communism'
        elif change == 'capitulated': sim.capitulated = True
        else: sim.state[change] = 5 if change == 'infrastructure' else False
        sim.advance(1)
        check(sim.cp == 100 and not sim.state['modifiers'] and not sim.flags, 'MKN districts: failed cancellation/refund at '+change)
        cases += 1
    sim = MilitaristModel(); sim.start(district)
    # Another target remains blocked even when its state has no project flag.
    sim.active = None
    check(not sim.can_start(district), 'MKN districts: concurrent projects allowed')

    march = one(one(decisions, 'MKN_military_marches_decisions'), 'MKN_establish_military_march')
    for subject, gov, overlord_gov in product((False, True), ('fascism', 'communism'), ('fascism', 'communism')):
        sim = MilitaristModel(); sim.target = sim.subject; sim.gov = overlord_gov
        sim.subject.update(subject=subject, gov=gov)
        check(sim.can_start(march) == (subject and gov == overlord_gov == 'fascism'), 'MKN marches: independent or nonfascist target')
        cases += 1
    sim = MilitaristModel(); sim.target = sim.subject
    sim.apply(one(march, 'complete_effect'))
    check(not sim.can_start(march), 'MKN marches: repeated conversion')
    autonomy = one(read(root/'common/autonomous_states/MKN_military_march.txt'), 'autonomy_state')
    check(one(autonomy, 'default') == 'yes', 'MKN marches: missing native default subject selection')
    mods = one(autonomy, 'modifier')
    check([Decimal(one(mods, k)) for k in ('cic_to_overlord_factor', 'mic_to_overlord_factor', 'autonomy_manpower_share')] == [Decimal('0.9'), Decimal('0.9'), Decimal(1)], 'MKN marches: incorrect contributions')
    check(one(one(autonomy, 'rule'), 'can_not_declare_war') == 'yes', 'MKN marches: independent war declarations allowed')
    for gov, overlord_gov, focus in product(('fascism', 'communism'), ('fascism', 'communism'), (False, True)):
        sim = MilitaristModel(); sim.gov = overlord_gov; sim.subject['gov'] = gov
        if not focus: sim.focuses.remove('MKN_military_marches')
        check(sim.test(one(autonomy, 'allowed'), sim.subject) == (gov == overlord_gov == 'fascism' and focus), 'MKN marches: autonomy bypasses political/focus gates')
        cases += 1
    district_modifier = one(read(root/'common/dynamic_modifiers/MKN_militarist_modifiers.txt'), 'MKN_fortified_district_modifier')
    check(Decimal(one(district_modifier, 'army_defence_factor')) == Decimal('0.20'), 'MKN districts: incorrect defense bonus')
    for owned, controlled, core, fortified in product((False, True), repeat=4):
        sim = MilitaristModel(); sim.state.update(owned=owned, controlled=controlled, core=core)
        if fortified: sim.state['flags'].add('MKN_district_fortified')
        check(sim.test(one(district_modifier, 'enable'), sim.state) == (owned and controlled and core and fortified), 'MKN districts: defense active outside a fortified owned/controlled core')
        cases += 1

    # Compare actual shared-spirit rebuilds with/without new focuses and rebuild twice.
    effects = {k: v for name in ('nww_mkn_progression', 'MKN_horizons_effects', 'MKN_militarist_effects', 'MKN_soviet_effects', 'MKN_communist_effects')
               for k, v, _ in read(root/f'common/scripted_effects/{name}.txt')}
    def rebuild(completed):
        sim = MilitaryModel(effects, completed)
        sim.apply(effects['nww_mkn_rebuild_industry']); sim.rebuild()
        return sim
    base = rebuild({'MKN_the_black_horde'})
    for schools, cult, districts in product((False, True), repeat=3):
        completed = {'MKN_the_black_horde'} | ({'MKN_schools_of_young_insurgents'} if schools else set()) | ({'MKN_cult_of_fallen_atamans'} if cult else set()) | ({'MKN_military_districts'} if districts else set())
        sim = rebuild(completed)
        for var, delta in [('MKN_army_conscription', Decimal('0.06') * schools), ('MKN_army_casualty_trickleback', Decimal('0.10') * cult), ('MKN_unified_training_time_army_factor', Decimal('-0.20') * schools), ('MKN_unified_research_speed_factor', Decimal('-0.16') * schools), ('MKN_army_supply_consumption_factor', Decimal('0.16') * districts)]:
            check(sim.variables[var] - base.variables[var] == delta, 'MKN militarists: lost/doubled reconstructed bonus '+var)
        before = (dict(sim.variables), deepcopy(sim.oneoffs))
        sim.apply(effects['nww_mkn_rebuild_industry']); sim.rebuild()
        check(before == (dict(sim.variables), sim.oneoffs), 'MKN militarists: save repair changes bonuses or repeats rewards')
        # Reconstruct both original saves and the later spartan-debuff revision.
        # Each has half the recruitment/training/recovery now awarded by v3.
        for version in ('v1', 'v2'):
            sim = rebuild(completed)
            sim.flags.add('MKN_militarist_progression_'+version)
            sim.variables['MKN_army_conscription'] -= Decimal('0.03') * schools
            sim.variables['MKN_army_casualty_trickleback'] -= Decimal('0.05') * cult
            sim.variables['MKN_unified_training_time_army_factor'] += Decimal('0.10') * schools
            missing_debuff = Decimal('0.16' if version == 'v1' else '0.08')
            sim.variables['MKN_unified_research_speed_factor'] += missing_debuff * schools
            sim.variables['MKN_army_supply_consumption_factor'] -= missing_debuff * districts
            sim.apply(effects['MKN_repair_militarist_progression'])
            sim.apply(effects['MKN_repair_militarist_progression'])
            check(before == (dict(sim.variables), sim.oneoffs), 'MKN militarists: '+version+' save is not repaired or rewards replay')
            check('MKN_militarist_progression_v3' in sim.flags, 'MKN militarists: missing v3 repair marker')
        cases += 1
    live = rebuild({'MKN_the_black_horde'})
    for fid in ('MKN_schools_of_young_insurgents', 'MKN_military_districts'):
        live.apply(one(fs[fid], 'completion_reward'))
        live.focuses.add(fid)
    before = (dict(live.variables), deepcopy(live.oneoffs))
    live.apply(effects['nww_mkn_rebuild_industry']); live.rebuild()
    check(before == (dict(live.variables), live.oneoffs), 'MKN militarists: focus reward and save reconstruction disagree')
    cases += 1
    print(f'PASS: MKN militarists: 12 focuses, DLC/traits, districts, marches and {cases} source-script scenarios; no runtime claim')
