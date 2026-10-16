"""Execute MKN HQ progression and project lifecycle scripts against the old reward baseline.

This is a static script model, not an HOI4 runtime reproduction.
"""
import argparse
from collections import Counter, defaultdict
from decimal import Decimal
from itertools import product
import json
from pathlib import Path
import re

from hoi4_script import read, one, values, walk, engine_script_errors, focus_registry, variable_check


class MilitaryModel:
    def __init__(self, effects, focuses=(), dlcs=()):
        self.effects = effects
        self.focuses = set(focuses)
        self.flags = set()
        self.variables = defaultdict(Decimal)
        self.dynamic = set()
        self.dlcs = set(dlcs)
        self.resources = {'army': Decimal(200), 'air': Decimal(200), 'navy': Decimal(200), 'cp': Decimal(100), 'pp': Decimal(200)}
        self.oneoffs = []
        self.state = {'owner': True, 'control': True, 'coastal': True, 'front': True, 'capital': False, 'rail': False, 'path': True, 'slots': True}
        self.buildings = defaultdict(Decimal)
        self.damage = Decimal(2)
        self.techs = {'radio_detection'}
        self.capitulated = False
        self.factories = 2

        self.ideas = {}
        self.offsite = 0

    def value(self, value):
        if value == 'damaged_building_level@infrastructure':
            return self.damage
        if value.startswith('building_level@'):
            return self.buildings[value.split('@')[1]]
        return self.variables[value]

    def test(self, nodes):
        result = []
        for key, val, op in nodes:
            if key == 'has_country_flag':
                ok = val in self.flags
            elif key == 'has_completed_focus':
                ok = val in self.focuses
            elif key == 'has_idea':
                ok = self.ideas.get(val, 0) > 0
            elif key in ('AND', 'hidden_trigger', 'limit', 'FROM', 'ROOT', 'capital_scope', 'custom_trigger_tooltip'):
                ok = self.test(val)
            elif key == 'tooltip':
                continue
            elif key == 'OR':
                ok = any(self.test([n]) for n in val)
            elif key == 'NOT':
                ok = not self.test(val)
            elif key == 'always':
                ok = val == 'yes'
            elif key == 'has_dynamic_modifier':
                ok = one(val, 'modifier') in self.dynamic
            elif key == 'has_dlc':
                ok = val in self.dlcs
            elif key == 'has_capitulated':
                ok = self.capitulated == (val == 'yes')
            elif key == 'has_tech':
                ok = val in self.techs
            elif key in ('has_army_experience', 'has_air_experience', 'has_navy_experience', 'command_power'):
                resource = 'cp' if key == 'command_power' else key.split('_')[1]
                ok = self.compare(self.resources[resource], Decimal(val), op)
            elif key == 'check_variable':
                var, value, operator = variable_check(val)
                ok = self.compare(self.value(var), Decimal(value), operator)
            elif key == 'is_owned_and_controlled_by':
                ok = self.state['owner'] and self.state['control']
            elif key == 'is_fully_controlled_by':
                ok = self.state['control']
            elif key in ('is_coastal', 'is_capital'):
                ok = self.state['coastal' if key == 'is_coastal' else 'capital'] == (val == 'yes')
            elif key == 'any_neighbor_state':
                ok = self.state['front']
            elif key == 'any_province_building_level':
                ok = self.state['coastal'] and self.compare(self.buildings[one(val, 'building')], Decimal(one(val, 'level')), next(o for k, v, o in val if k == 'level'))
            elif key == 'free_building_slots':
                ok = self.state['slots']
            elif key == 'can_build_railway':
                ok = self.state['path']
            elif key == 'has_railway_connection':
                ok = self.state['rail']
            elif key == 'num_of_civilian_factories_available_for_projects':
                ok = self.compare(Decimal(self.factories), Decimal(val), op)
            elif key in ('supply_node', 'radar_station', 'air_base', 'anti_air_building'):
                ok = self.compare(self.buildings[key], Decimal(val), op)
            else:
                raise AssertionError('Unmodelled military trigger: ' + str(key))
            result.append(ok)
        return all(result)

    @staticmethod
    def compare(left, right, op):
        return {'=': left == right, '!=': left != right, '>': left > right, '<': left < right, '>=': left >= right, '<=': left <= right}[op]

    def apply(self, nodes):
        conditional = None
        for key, val, op in nodes:
            if key == 'if':
                conditional = self.test(one(val, 'limit'))
                if conditional:
                    self.apply([n for n in val if n[0] != 'limit'])
            elif key == 'else':
                assert conditional is not None, 'Orphan else'
                if not conditional:
                    self.apply(val)
                conditional = None
            elif key in ('hidden_effect', 'FROM', 'ROOT', 'capital_scope'):
                self.apply(val)
            elif key and key.isdigit():
                self.apply(val)
            elif key == 'set_variable':
                for var, amount, _ in val:
                    self.variables[var] = Decimal(amount)
            elif key == 'add_to_variable':
                for var, amount, _ in val:
                    if var != 'tooltip':
                        self.variables[var] += Decimal(amount)
            elif key == 'set_country_flag':
                self.flags.add(val)
            elif key == 'add_timed_idea':
                self.ideas[one(val, 'idea')] = int(one(val, 'days'))
            elif key == 'clr_country_flag':
                self.flags.discard(val)
            elif key in self.effects:
                self.apply(self.effects[key])
            elif key in ('army_experience', 'air_experience', 'navy_experience'):
                self.resources[key.split('_')[0]] += Decimal(val)
                self.oneoffs.append((key, val))
            elif key in ('add_command_power', 'add_political_power'):
                self.resources['cp' if key == 'add_command_power' else 'pp'] += Decimal(val)
                self.oneoffs.append((key, val))
            elif key == 'add_dynamic_modifier':
                self.dynamic.add(one(val, 'modifier'))
            elif key == 'remove_ideas' or key in ('custom_effect_tooltip', 'set_state_flag'):
                pass
            elif key == 'damage_building':
                self.damage = max(Decimal(0), self.damage + Decimal(one(val, 'damage')))
                self.oneoffs.append((key, val))
            elif key == 'add_building_construction':
                self.buildings[one(val, 'type')] += Decimal(one(val, 'level'))
                self.oneoffs.append((key, val))
            elif key == 'add_offsite_building':
                self.offsite += int(one(val, 'level'))
            elif key == 'build_railway':
                self.state['rail'] = True
                self.oneoffs.append((key, val))
            elif key and key.startswith('mio:'):
                self.oneoffs.append((key, val))
            elif key in ('add_ace', 'add_equipment_to_stockpile', 'add_tech_bonus', 'add_doctrine_cost_reduction', 'add_mastery_bonus', 'add_extra_state_shared_building_slots'):
                self.oneoffs.append((key, val))
            else:
                raise AssertionError('Unmodelled military effect: ' + str(key))

    def rebuild(self):
        self.apply(self.effects['nww_mkn_rebuild_services'])


def validate_military(root, game, check, localized):
    check(game.is_dir(), 'Installed HOI4 directory is unavailable: '+str(game))
    manifest = json.loads((root/'docs/MKN_military_refactor.json').read_text())
    groups, tactics, projects = (manifest[k] for k in ('groups', 'tactics', 'projects'))
    originals = manifest['old_rewards']
    fs = {one(f, 'id'): f for f in values(one(read(root/'common/national_focus/MKN.txt'), 'focus_tree'), 'focus')}
    effects = dict((k, v) for k, v, o in read(root/'common/scripted_effects/nww_mkn_progression.txt'))
    effects.update((k, v) for k, v, o in read(root/'common/scripted_effects/MKN_horizons_effects.txt'))
    effects.update((k, v) for k, v, o in read(root/'common/scripted_effects/MKN_militarist_effects.txt'))
    effects.update((k, v) for k, v, o in read(root/'common/scripted_effects/MKN_soviet_effects.txt'))
    effects.update((k, v) for k, v, o in read(root/'common/scripted_effects/MKN_communist_effects.txt'))
    decisions = {k: v for cat, ds, o in read(root/'common/decisions/MKN_military_decisions.txt') for k, v, o in ds}
    native_buildings = {k for k, v, o in one(read(game/'common/buildings/00_buildings.txt'), 'buildings')}
    for k, v, o in walk(list((name, node, '=') for name, node in decisions.items())):
        if k in ('add_building_construction', 'damage_building'):
            check(one(v, 'type') in native_buildings, 'MKN project: undefined installed building '+str(one(v, 'type')))
    technology = one(read(game/'common/technologies/electronic_mechanical_engineering.txt'), 'technologies')
    radar_tech = one(technology, 'radio_detection', [])
    check(any(one(n, 'building') == 'radar_station' and one(n, 'level') == '1' for n in values(radar_tech, 'enable_building')), 'Installed radio_detection no longer unlocks the first radar level')

    def baseline(ids):
        result = defaultdict(Decimal)
        for fid in ids:
            if fid in originals:
                for node in values(originals[fid], 'add_to_variable'):
                    for key, amount, _ in node:
                        if key != 'tooltip':
                            result[key] += Decimal(amount)
            else:
                for key, amount in manifest['political_stats'].get(fid, {}).items():
                    result[key] += Decimal(amount)
            for key, amount in manifest.get('final_adjustments', {}).get(fid, {}).items():
                result[key] += Decimal(amount)
        return result

    def exact(model, ids, context):
        expected = baseline(ids)
        check(all(model.variables[k] == expected[k] for k in model.variables.keys() | expected.keys()), context)

    def rebuilt(model, context):
        before = dict(model.variables)
        rewards = list(model.oneoffs)
        model.rebuild()
        model.rebuild()
        check(dict(model.variables) == before, context + ': repeated rebuild changes stats')
        check(model.oneoffs == rewards, context + ': rebuild replays one-off rewards')

    focus_ids = {g['id'] for g in groups} | set(manifest['memorials'])
    check(len(focus_ids) == 35 and manifest['old_focus_count'] == 130, 'MKN: expected 35 military focuses including three roots and two memorials')
    check(Counter(g['service'] for g in groups) == {'army': 11, 'air': 11, 'navy': 11}, 'MKN: each service needs a root and two five-focus programmes')
    check(len(tactics) == 30 and Counter(t['service'] for t in tactics) == {'army': 10, 'air': 10, 'navy': 10}, 'MKN: expected 30 HQ tactics')
    assigned = [s for g in groups+tactics for s in g['sources']]
    check(len(assigned) == len(set(assigned)) and set(assigned) == originals.keys(), 'MKN: a legacy bonus was lost or duplicated')
    registry = focus_registry(root/'common/national_focus')
    check(originals.keys() <= registry.keys(), 'MKN: removed focus tokens are not registered for old saves')
    check(not (originals.keys()-focus_ids) & fs.keys(), 'MKN: retired military focuses remain playable')
    for g in groups:
        fid = g['id']; f = fs[fid]
        check(one(f, 'cost') in ('5', '10'), fid+': wrong duration')
        for p in values(f, 'prerequisite'):
            check(set(values(p, 'focus')) <= focus_ids, fid+': prerequisite references a retired focus')
        if g['opposite']:
            check(g['opposite'] in values(one(f, 'mutually_exclusive'), 'focus'), fid+': lost program exclusion')
        # Every original one-off reward must be present exactly, with its own persistent credit.
        reward = one(f, 'completion_reward')
        reward_grants = {}
        for n in values(reward, 'if'):
            limit = one(n, 'limit', [])
            limit = one(limit, 'hidden_trigger', limit)
            reward_grants[one(one(limit, 'NOT', []), 'has_country_flag')] = n
        for source in g['reward_sources']:
            credit = 'MKN_military_reward_'+source[4:]
            n = reward_grants.get(credit, [])
            wanted = [(k, v, o) for k, v, o in originals[source] if k != 'add_to_variable' and not (k == 'if' and any(a == 'add_dynamic_modifier' for a, b, c in walk(v)))]
            actual = [(k, v, o) for k, v, o in n if k not in ('limit', 'set_country_flag')]
            # JSON baseline stores arrays; normalize tuples without changing script content.
            check(json.loads(json.dumps(actual)) == json.loads(json.dumps(wanted)), fid+': missing/changed one-off source '+source)
        for key, val, _ in walk(reward):
            if key == 'add_to_variable' and one(val, 'tooltip'):
                localized(one(val, 'tooltip'), fid)
            if key == 'add_ideas':
                check(False, fid+': creates a second permanent service spirit')
    for fid in manifest['memorials']:
        check(fid in fs, 'MKN: missing Marusya focus '+fid)
    check(one(one(fs['MKN_memory_of_atamansha_marusya'], 'completion_reward'), 'add_ideas') == 'MKN_marusyas_legacy', 'Marusya memorial spirit lost')
    check(one(one(fs['MKN_memory_of_atamansha_marusya'], 'prerequisite'), 'focus') == manifest['roots']['army'], 'Marusya no longer requires the staff')
    check(one(one(fs['MKN_the_black_guard_battalions'], 'completion_reward'), 'MKN_raise_black_guard_battalions') == 'yes', 'Marusya battalions reward changed')
    for fid, f in fs.items():
        if fid not in focus_ids:
            refs = {v for k, v, o in walk(f) if k in ('has_completed_focus', 'focus', 'relative_position_id')}
            check(not refs & (originals.keys()-focus_ids), fid+': political gate still points at retired military content')

    # Every individual historical completion and partial historical route must repair exactly.
    scenarios = [set(), set(originals)] + [{s} for s in originals]
    for p in manifest['old_programs']:
        scenarios.extend(set(p['focuses'][:n]) for n in range(1, len(p['focuses'])+1))
    scenarios.extend({fid} for fid in manifest['political_stats'])
    for done in scenarios:
        model = MilitaryModel(effects, done)
        model.rebuild()
        exact(model, done, 'MKN: incorrect partial old-save replay '+str(sorted(done)))
        check(not model.oneoffs, 'MKN: migration grants experience/equipment/buildings/MIO rewards')
        rebuilt(model, 'MKN old-save repair')

    # Completing each bundle after an arbitrary partial save must not double its earned bonuses.
    for g in groups:
        for bits in product((False, True), repeat=len(g['sources'])):
            prior = {s for s, done in zip(g['sources'], bits) if done}
            model = MilitaryModel(effects, prior, ['Arms Against Tyranny', 'Man the Guns', 'By Blood Alone'])
            model.rebuild()
            model.focuses.add(g['id'])
            model.apply(one(fs[g['id']], 'completion_reward'))
            exact(model, set(g['sources']) | ({g['id']} if g.get('new_reform') else set()), g['id']+': partial bundle repeats/loses source stats')
            rebuilt(model, g['id'])

    # All eight combinations of exclusive programs, with and without AAT.
    programs = json.loads((root/'docs/MKN_military_programs.json').read_text())
    for aat, choices in product((False, True), product((0, 1), repeat=3)):
        selected = [programs[service*2+choice] for service, choice in enumerate(choices)]
        chosen = {fid for p in selected for fid in p['focuses']} | set(manifest['roots'].values())
        model = MilitaryModel(effects, dlcs=['Arms Against Tyranny', 'Man the Guns', 'By Blood Alone'] if aat else [])
        model.rebuild()
        for g in sorted((g for g in groups if g['id'] in chosen), key=lambda g: g['y']):
            if g['parent']:
                check(g['parent'] in model.focuses, g['id']+': inaccessible parent')
            model.focuses.add(g['id'])
            model.apply(one(fs[g['id']], 'completion_reward'))
        for t in tactics:
            if t['route'] in model.focuses:
                model.apply(one(decisions[t['id']], 'complete_effect'))
        old_done = {s for g in groups if g['id'] in chosen for s in g['sources']} | {s for t in tactics if t['route'] in chosen for s in t['sources']} | {g['id'] for g in groups if g['id'] in chosen and g.get('new_reform')}
        exact(model, old_done, 'MKN: full program total differs from baseline')
        rebuilt(model, 'MKN full program')
        check(aat or not any(k.startswith('mio:') for k, v in model.oneoffs), 'MKN: AAT MIO effect runs without AAT')

    for t in tactics:
        fid = t['id']; d = decisions[fid]
        localized(fid, fid); localized(fid+'_desc', fid)
        localized(one(d, 'custom_cost_text'), fid)
        check(one(d, 'fire_only_once') == 'yes' and one(d, 'days_remove') == '1', fid+': tactic is repeatable')
        check(not values(one(d, 'remove_effect', []), 'add_to_variable'), fid+': tactic reward repeated at expiry')
        for xp, cp, allowed in ((20, 10, True), (19, 10, False), (20, 9, False)):
            model = MilitaryModel(effects, [t['route']])
            model.resources[t['service']] = Decimal(xp); model.resources['cp'] = Decimal(cp)
            check(model.test(one(d, 'custom_cost_trigger')) == allowed, fid+': wrong XP/CP threshold')
        model = MilitaryModel(effects, [t['route']]);model.rebuild()
        before = dict(model.resources)
        model.apply(one(d, 'complete_effect'))
        check(model.resources[t['service']] == before[t['service']]-20 and model.resources['cp'] == before['cp']-10, fid+': wrong resource deduction')
        check(not model.test(one(d, 'visible')), fid+': tactic remains purchasable after completion')
        exact(model, t['sources'], fid+': wrong tactic bonuses')
        rebuilt(model, fid)
        for source in t['sources']:
            old = MilitaryModel(effects, [t['route'], source]);old.rebuild()
            old.apply(one(d, 'complete_effect'))
            exact(old, t['sources'], fid+': partial old tactic bonus repeated')

    for p in projects:
        fid = p['id']; d = decisions[fid]
        localized(fid, fid); localized(fid+'_desc', fid)
        localized(fid+'_unlock_tt', fid)
        check(one(d, 'fire_only_once') == 'yes' and one(d, 'state_target') == 'yes', fid+': project is not one-off on-map')
        check(one(d, 'target_array') == 'ROOT.owned_states', fid+': project targets foreign states')
        check(one(d, 'days_remove') == str(p['days']), fid+': wrong project duration')
        check(one(one(d, 'modifier', []), 'civilian_factory_use', '0') == str(p.get('civ', 0)), fid+': wrong factory reservation')
        for owner, control in product((False, True), repeat=2):
            model = MilitaryModel(effects, [p['focus']]);model.state.update(owner=owner, control=control)
            check(model.test(one(d, 'available')) == (owner and control), fid+': incorrect ownership/control requirement')
        for interrupted in ('none', 'cancel', 'expiry'):
            model = MilitaryModel(effects, [p['focus']]); before = dict(model.resources)
            check(model.test(one(d, 'available')), fid+': project cannot start')
            model.resources['pp'] -= Decimal(one(d, 'cost'))
            model.apply(one(d, 'complete_effect'))
            check(not any(model.buildings.values()) and not model.state['rail'], fid+': project builds immediately')
            check(not model.test(one(d, 'available')), fid+': project can be started twice')
            # The shared lock prevents any second project from starting concurrently.
            for other in projects:
                model.focuses.add(other['focus'])
                check(not model.test(one(decisions[other['id']], 'available')), fid+': concurrent map project allowed')
            if interrupted != 'none':
                model.state['control'] = False
                check(model.test(one(d, 'cancel_trigger')), fid+': lost state does not cancel')
                model.apply(one(d, 'cancel_effect' if interrupted == 'cancel' else 'remove_effect'))
                check(dict(model.resources) == before, fid+': interrupted project not refunded')
                check(not any(model.buildings.values()) and not model.state['rail'], fid+': builds in a lost state')
            else:
                model.apply(one(d, 'remove_effect'))
                check(fid+'_done' in model.flags, fid+': completion not recorded')
                check(sum(model.buildings.values()) == 1 or model.state['rail'] or model.damage == 0, fid+': completion grants no construction/repair')
                check(model.resources['pp'] == before['pp']-p.get('pp', 0) and model.resources['cp'] == before['cp']-p.get('cp', 0), fid+': wrong project cost')
            check('MKN_military_project_active' not in model.flags, fid+': project leaves global lock')
            model.state['control'] = True
            check(not model.test(one(d, 'available')), fid+': finished/cancelled project can be repeated')
        for key, val, _ in walk(one(d, 'remove_effect')):
            if key == 'add_building_construction' and one(val, 'type') == 'supply_node':
                check(one(one(val, 'province', []), 'all_provinces') == 'no', fid+': supply hub lacks a single-province selector')
            if key == 'add_building_construction' and one(val, 'type') in ('coastal_bunker', 'naval_base'):
                check(one(one(val, 'province'), 'all_provinces') == 'no' and one(one(val, 'province'), 'limit_to_coastal') == 'yes', fid+': coastal project does not select one coastal province')
    radar = decisions['MKN_project_observation_posts']
    model = MilitaryModel(effects, ['MKN_communal_aa_defense_focus']);model.techs.clear()
    check(not model.test(one(radar, 'available')), 'Radar project available without radar research')
    model.flags.update({'MKN_project_observation_posts_spent', 'MKN_military_project_active'})
    check(model.test(one(radar, 'cancel_trigger')), 'Radar research not rechecked during construction')
    model.apply(one(radar, 'remove_effect'))
    check(not any(model.buildings.values()), 'Radar project builds without radar research at expiry')
    model = MilitaryModel(effects, ['MKN_communal_aa_defense_focus']);model.factories = 1
    check(not model.test(one(radar, 'available')), 'Radar project does not require two available civilian factories')
    model = MilitaryModel(effects, ['MKN_communal_aa_defense_focus']);model.buildings['radar_station'] = 1
    check(not model.test(one(radar, 'available')), 'Level-one radar project can overfill researched cap')

    for hook in ('on_startup', 'on_daily_MKN'):
        nodes = one(one(read(root/'common/on_actions/nww_mkn_progression.txt'), 'on_actions'), hook)
        check(any(k == 'has_country_flag' and v == 'MKN_services_redesign_v5' for k, v, o in walk(nodes)), hook+': missing v5 save repair')
    for relative in ('common/national_focus/MKN.txt', 'common/decisions/MKN_military_decisions.txt', 'common/scripted_effects/nww_mkn_progression.txt'):
        check(not list(engine_script_errors(read(root/relative))), relative+': invalid native script syntax')
    print(f'PASS: MKN HQ: 35 focuses, six five-focus programmes, 30 one-off tactics, 9 one-off projects; {len(scenarios)} legacy saves, preserved bonuses plus explicit additions, DLC guards, XP/CP, radar research and project cancellation')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    def check(ok, message):
        if not ok:
            raise AssertionError(message)
    def localized(key, context):
        for lang in ('english', 'russian'):
            pattern = re.compile(r'^\s+'+re.escape(key)+r':\d*\s+"', re.M)
            check(any(pattern.search(p.read_text(encoding='utf-8-sig')) for p in (root/'localisation').rglob('*l_'+lang+'.yml')), context+': missing '+lang+' '+key)
    validate_military(root, args.game, check, localized)
