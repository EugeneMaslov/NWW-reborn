"""Static MKN succession checks and execution of the real collapse arithmetic.

The tiny interpreter is intentionally strict: unsupported commands fail instead
of being silently ignored. It models fractional armed forces; actual game units
and geography still require a fresh-campaign reproduction.
"""
from collections import Counter
from copy import deepcopy
from math import isclose
from pathlib import Path
import re

from hoi4_script import read, one, values, walk


def validate_crisis(root, game, check, localized):
    effects = dict((k, v) for k, v, o in read(root / 'common/scripted_effects/MKN_effects.txt'))
    tree = one(read(root / 'common/national_focus/MKN.txt'), 'focus_tree')
    focuses = {one(f, 'id'): f for f in values(tree, 'focus')}
    events = {one(e, 'id'): e for e in values(read(root / 'events/MKN_events.txt'), 'country_event')}
    news = one(read(root / 'events/MKN_news_events.txt'), 'news_event')
    decisions = read(root / 'common/decisions/MKN_decisions.txt')
    mission = one(one(decisions, 'MKN_succession_crisis_category'), 'MKN_civil_war_timer_mission')
    routes = {
        'fascism': ['military_takes_charge', 'arrest_demagogues', 'abolish_election_of_commanders', 'militarize_communes', 'standardize_workshops', 'iron_fist_trains', 'black_expansionism', 'the_black_horde'],
        'democratic': ['triumph_of_free_soviets', 'pact_of_free_communes', 'abolish_general_staff', 'arms_to_the_people', 'black_international', 'propaganda_by_deed', 'autonomous_rail_crews', 'beacon_of_statelessness'],
        'neutrality': ['peasant_delegates', 'grain_ultimatum', 'sever_urban_ties', 'every_farm_a_fortress', 'steppe_snipers', 'railway_sabotage', 'cavalry_ambush', 'impregnable_granary'],
        'communism': ['emergency_revkom', 'purge_irreconcilables', 'embassy_to_kharkov', 'integrate_steel_lines', 'red_military_specialists', 'tractors_for_grain', 'anti_imperialist_front', 'the_fatal_plenum'],
    }
    entries = {'MKN_' + route[0] for route in routes.values()}
    for ideology, route in routes.items():
        for i, token in enumerate(route):
            fid = 'MKN_' + token
            f = focuses[fid]
            localized(fid, 'MKN crisis'); localized(fid + '_desc', 'MKN crisis')
            parent = 'MKN_' + route[i - 1] if i else 'MKN_departure_of_batko'
            check(values(one(f, 'prerequisite'), 'focus') == [parent], f'{fid}: succession chain is broken')
            if not i:
                excluded = {v for n in values(f, 'mutually_exclusive') for v in values(n, 'focus')}
                check(excluded == entries - {fid}, f'{fid}: incomplete mutual exclusion')
                check(any((ideology, '0.40', '<') in n for n in values(one(f, 'available'), 'NOT')), f'{fid}: missing 40% mandate')
                check(one(one(one(f, 'completion_reward'), 'set_politics'), 'ruling_party') == ideology, f'{fid}: wrong government')
                check(one(one(one(f, 'completion_reward'), 'set_politics'), 'elections_allowed') == 'no', f'{fid}: incomplete election tooltip')
            if i == 1:
                check(one(one(f, 'completion_reward'), 'MKN_resolve_succession_crisis') == 'yes', f'{fid}: does not stop the crisis')
    departure = focuses['MKN_departure_of_batko']
    check(one(departure, 'cost') == '0' and one(one(departure, 'available'), 'always') == 'no', 'MKN: funeral must be event-completed')
    check(not one(departure, 'completion_reward'), 'MKN: funeral focus replays a political reward')
    funeral = events['mkn_crisis.1']
    check(one(one(funeral, 'mean_time_to_happen'), 'days') == '75', 'MKN: wrong funeral MTTH')
    guaranteed = one(one(funeral, 'mean_time_to_happen'), 'modifier')
    check(one(guaranteed, 'factor') == '0' and ('date', '1936.12.30', '>') in guaranteed, 'MKN: missing MTTH hard deadline')
    check(one(one(funeral, 'immediate'), 'activate_mission') == 'MKN_civil_war_timer_mission', 'MKN: funeral does not start the deadline')
    check(one(one(funeral, 'immediate'), 'complete_national_focus') == 'MKN_departure_of_batko', 'MKN: funeral does not complete its focus')
    # No other script may activate this mission: loading a save must not reset it.
    activations = []
    for folder in ('common', 'events', 'history'):
        for p in (root / folder).rglob('*.txt'):
            try:
                doc = read(p)
            except (ValueError, UnicodeError):
                continue
            activations.extend(p for k, v, o in walk(doc) if k == 'activate_mission' and v == 'MKN_civil_war_timer_mission')
    check(activations == [root / 'events/MKN_events.txt'], 'MKN: timer activation is not exclusive to the funeral event')
    check(one(mission, 'days_mission_timeout') == '180' and one(one(mission, 'activation'), 'always') == 'no', 'MKN: deadline auto-activates or has wrong duration')
    check(one(one(one(mission, 'timeout_effect'), 'if'), 'country_event') == [('id', 'mkn_crisis.100', '=')], 'MKN: timeout does not invoke collapse')
    repair = effects['MKN_repair_succession_crisis']
    check(not any(k == 'activate_mission' for k, v, o in walk(repair)), 'MKN: save repair resets the deadline')
    resolve = effects['MKN_resolve_succession_crisis']
    check(one(resolve, 'remove_mission') == 'MKN_civil_war_timer_mission' and one(resolve, 'set_country_flag') == 'MKN_crisis_settled', 'MKN: lifesaver leaves active mission')
    check(one(news, 'major') == 'yes' and len(values(news, 'option')) == 4, 'MKN: funeral news requires four exclusive audiences')
    rail_gates = one(focuses['MKN_integrate_steel_lines'], 'available')
    check(one(rail_gates, 'has_country_flag') == 'MKN_soviet_trade_accepted' and one(rail_gates, 'has_military_access_to') == 'SOV', 'MKN: rail link lacks Soviet consent')
    check(not values(rail_gates, 'is_in_faction_with'), 'MKN: rail link is blocked by its descendant alliance focus')
    plenum = events['mkn_crisis.40']
    outcomes = values(plenum, 'option')
    check(any(k == 'set_country_flag' and v == 'MKN_equal_autonomy' for k, v, o in walk(outcomes[0])), 'MKN: plenum cannot grant equal autonomy')
    check(any(k == 'declare_war_on' for k, v, o in walk(outcomes[1])) and any(k == 'add_timed_idea' and one(v, 'idea') == 'MKN_betrayed_twice' for k, v, o in walk(outcomes[1])), 'MKN: betrayal has no actual war/protective spirit')

    # Fail on misspelled native commands, including rewards absent from the older validator.
    native_effects = set(re.findall(r'^## (\w+)', (game / 'documentation/effects_documentation.md').read_text(), re.M))
    command_files = ('common/scripted_effects/MKN_effects.txt', 'events/MKN_events.txt', 'events/MKN_news_events.txt', 'common/decisions/MKN_decisions.txt')
    native_arguments = {'start_state', 'add_namespace', 'set_value'}
    for filename in command_files:
        for key, value, op in walk(read(root / filename)):
            if key and re.match(r'^(add_|set_|clr_|remove_|create_|start_|retire_|activate_|damage_|build_)', key):
                check(key in native_effects or key in native_arguments, f'{filename}: undocumented native command {key}')
    for route in routes.values():
        for token in route:
            for key, value, op in walk(one(focuses['MKN_' + token], 'completion_reward')):
                if key and re.match(r'^(add_|set_|clr_|remove_|create_|start_|retire_|activate_|damage_|build_)', key):
                    check(key in native_effects or key in native_arguments, f'MKN_{token}: undocumented native reward {key}')
    # Check modifier names against actual executable docs and installed definitions.
    known = set(re.findall(r'^## (\w+)', (game / 'documentation/modifiers_documentation.md').read_text(), re.M))
    buildings = {k for k, v, o in one(read(game / 'common/buildings/00_buildings.txt'), 'buildings')}
    known |= {'production_speed_' + b + '_factor' for b in buildings}
    ideas = one(one(read(root / 'common/ideas/MKN_ideas.txt'), 'ideas'), 'country')
    for name, idea, o in ideas:
        for k, v, op in one(idea, 'modifier', []):
            check(k in known, f'{name}: unregistered modifier {k}')
    trains = one(one(ideas, 'MKN_cult_of_railways'), 'equipment_bonus')
    check(one(one(trains, 'train_equipment_3'), 'build_cost_ic') == '-0.35' and one(one(trains, 'railway_gun_equipment'), 'build_cost_ic') == '-0.25', 'MKN: train cost bonuses use the wrong equipment/stat')
    check(one(one(one(ideas, 'MKN_steppes_freedom'), 'equipment_bonus'), 'motorized_equipment') is not None, 'MKN: motorized speed has no valid equipment bonus')
    # Check map integrity against both mod and installed state definitions.
    state_files = {one(one(read(p), 'state'), 'id'): p for p in (game / 'history/states').glob('*.txt')}
    state_files.update({one(one(read(p), 'state'), 'id'): p for p in (root / 'history/states').glob('*.txt')})
    owners, provinces = {}, Counter()
    for sid, p in state_files.items():
        state = one(read(p), 'state')
        owners[sid] = one(one(state, 'history'), 'owner')
        provinces.update(v for k, v, o in one(state, 'provinces', []))
    check(all(provinces[p] == 1 for p in ('429', '9571')), 'MKN: Huliaipole provinces duplicated or missing')
    check(owners.get('1082') == 'MKN' and sum(v == 'MKN' for v in owners.values()) >= 4, 'MKN: fewer than four starting owned states')
    z = one(read(root / 'history/states/200-Rivne.txt'), 'state')
    h = one(read(root / 'history/states/1082-Huliaipole.txt'), 'state')
    check(int(one(z, 'manpower')) + int(one(h, 'manpower')) == 1294082, 'MKN: state split creates/destroys population')

    class Interpreter:
        """Evaluate the actual script, including flags, allocation and native split ratios."""
        def __init__(self, popularity, ruling, count):
            self.root = {'vars': {}, 'flags': {'MKN_crisis_active'}, 'government': ruling,
                         'support': dict(zip(routes, popularity)), 'army': 1.0, 'name': 'MKN', 'bop': True}
            self.countries = [self.root]
            self.states = [{'id': n, 'owner': self.root, 'flags': set()} for n in range(count)]
            self.targets = {}
            self.wars = set()
            self.removed = []
        def number(self, val, country):
            if val.startswith('var:'): val = val[4:]
            if val.startswith('party_popularity@'): return country['support'][val.split('@')[1]]
            try: return float(val)
            except ValueError: return country['vars'][val]
        def compare(self, left, right, op):
            return {'=': left == right, '>': left > right, '<': left < right,
                    'equals': left == right, 'greater_than': left > right,
                    'greater_than_or_equals': left >= right}[op]
        def triggers(self, nodes, scope):
            answers = []
            for k, v, op in nodes:
                if k == 'NOT': answers.append(not self.triggers(v, scope))
                elif k == 'OR': answers.append(any(self.triggers([n], scope) for n in v))
                elif k == 'has_government': answers.append(scope['government'] == v)
                elif k == 'has_state_flag': answers.append(v in scope['flags'])
                elif k == 'has_country_flag': answers.append(v in scope['flags'])
                elif k == 'is_controlled_by':
                    assert v == 'ROOT'
                    answers.append(scope['owner'] is self.root)
                elif k == 'has_power_balance': answers.append(scope['bop'])
                elif k == 'has_war_with': answers.append(frozenset((scope['name'], self.targets[v]['name'])) in self.wars)
                elif k == 'exists': answers.append(v in self.targets)
                elif k == 'any_owned_state': answers.append(any(self.triggers(v, s) for s in self.states if s['owner'] is scope))
                elif k == 'check_variable':
                    if one(v, 'var') is not None:
                        a = self.number(one(v, 'var'), scope); b = self.number(one(v, 'value'), scope); comparison = one(v, 'compare')
                    else:
                        key, value, comparison = v[0]; a = self.number(key, scope); b = self.number(value, scope)
                    answers.append(self.compare(a, b, comparison))
                else: raise AssertionError(f'Unsupported collapse trigger {k}')
            return all(answers)
        def apply(self, nodes, scope):
            matched = False
            for k, v, op in nodes:
                if k in ('if', 'else_if'):
                    if k == 'if': matched = False
                    if not matched and self.triggers(one(v, 'limit'), scope):
                        self.apply([n for n in v if n[0] != 'limit'], scope); matched = True
                elif k == 'else':
                    if not matched: self.apply(v, scope)
                elif k == 'while_loop_effect':
                    iterations = 0
                    while self.triggers(one(v, 'limit'), scope):
                        self.apply([n for n in v if n[0] != 'limit'], scope)
                        iterations += 1
                        assert iterations < 1000, 'Unbounded collapse loop'
                elif k in ('set_variable', 'add_to_variable', 'subtract_from_variable', 'multiply_variable', 'divide_variable'):
                    name, val, ignored = v[0]; val = self.number(val, scope)
                    previous = scope['vars'].get(name, 0)
                    if k == 'set_variable': result = val
                    elif k == 'add_to_variable': result = previous + val
                    elif k == 'subtract_from_variable': result = previous - val
                    elif k == 'multiply_variable': result = previous * val
                    else: result = previous / val
                    scope['vars'][name] = result
                elif k == 'clamp_variable':
                    name = one(v, 'var'); scope['vars'][name] = max(float(one(v, 'min')), min(float(one(v, 'max')), scope['vars'][name]))
                elif k == 'round_variable': scope['vars'][v] = int(scope['vars'][v] + .5)
                elif k in ('set_state_flag', 'set_country_flag'): scope['flags'].add(v)
                elif k in ('clr_state_flag', 'clr_country_flag'): scope['flags'].discard(v)
                elif k == 'ROOT': self.apply(v, self.root)
                elif k in ('every_owned_state', 'random_owned_state'):
                    owned = [s for s in self.states if s['owner'] is scope and self.triggers(one(v, 'limit', []), s)]
                    for s in owned if k == 'every_owned_state' else owned[:1]:
                        self.apply([n for n in v if n[0] != 'limit'], s)
                elif k == 'capital_scope': self.apply(v, self.states[0])
                elif k == 'remove_mission': self.removed.append((scope['name'], v))
                elif k == 'remove_power_balance': scope['bop'] = False
                elif k in effects: self.apply(effects[k], scope)
                elif k == 'start_civil_war':
                    ratio = self.number(one(v, 'army_ratio'), scope)
                    for field in ('size', 'air_ratio', 'navy_ratio'): assert isclose(ratio, self.number(one(v, field), scope))
                    land = [s for s in self.states if s['owner'] is scope and self.triggers(one(v, 'states_filter'), s)]
                    assert land and len(land) < sum(s['owner'] is scope for s in self.states)
                    child = {'vars': deepcopy(scope['vars']), 'flags': set(scope['flags']), 'government': one(v, 'ideology'), 'support': deepcopy(scope['support']), 'army': scope['army'] * ratio, 'name': 'D' + str(len(self.countries)), 'bop': scope['bop']}
                    scope['army'] *= 1 - ratio
                    for s in land: s['owner'] = child
                    self.countries.append(child)
                    self.wars.add(frozenset((scope['name'], child['name'])))
                    arguments = {'ideology', 'size', 'army_ratio', 'navy_ratio', 'air_ratio', 'states', 'states_filter', 'keep_all_characters'}
                    self.apply([n for n in v if n[0] not in arguments], child)
                elif k == 'set_politics': scope['government'] = one(v, 'ruling_party')
                elif k == 'set_popularities': scope['support'] = {key: float(val) / 100 for key, val, o in v}
                elif k == 'set_cosmetic_tag': scope['cosmetic'] = v
                elif k == 'save_event_target_as': self.targets['event_target:' + v] = scope
                elif k == 'retire_ideology_leader': scope.setdefault('retired', []).append(v)
                elif k == 'create_country_leader': scope['leader'] = one(v, 'name')
                elif k.startswith('event_target:'): self.apply(v, self.targets[k])
                elif k == 'declare_war_on': self.wars.add(frozenset((scope['name'], self.targets[one(v, 'target')]['name'])))
                else: raise AssertionError(f'Unsupported collapse effect {k}')

    cases = 0
    shares = [(.25, .25, .25, .25), (.70, .10, .10, .10), (.01, .01, .01, .97), (1, 0, 0, 0), (.17, .23, .29, .31), (.333, .333, .333, .001)]
    for ruling in routes:
        for popularity in shares:
            for count in (4, 5, 7, 12, 43):
                model = Interpreter(popularity, ruling, count)
                model.apply(effects['MKN_execute_four_way_collapse'], model.root)
                check(len(model.countries) == 4 and len(model.wars) == 6, 'MKN: collapse is not a four-way war')
                check(model.root['government'] == ruling and model.states[0]['owner'] is model.root, 'MKN: player loses ideology or capital')
                check(all(not c['bop'] for c in model.countries), 'MKN: collapse preserves or resurrects BoP')
                support = list(popularity); total = sum(support)
                for c in model.countries:
                    index = list(routes).index(c['government'])
                    check(isclose(c['army'], support[index] / total, abs_tol=1e-8), f'MKN: sequential military share incorrect for {ruling}/{popularity}/{c["government"]}')
                    land = sum(s['owner'] is c for s in model.states)
                    check(land == model.root['vars']['MKN_cw_quota_' + c['government']], 'MKN: actual territory differs from apportioned quota')
                check(isclose(sum(c['army'] for c in model.countries), 1), 'MKN: collapse creates/destroys military resources')
                cases += 1
    # Reduced territory must terminate safely and must never give away the last state.
    for count in (1, 2, 3):
        model = Interpreter((.25, .25, .25, .25), 'communism', count)
        model.apply(effects['MKN_execute_four_way_collapse'], model.root)
        check(len(model.countries) == count and model.states[0]['owner'] is model.root, 'MKN: reduced-land collapse fails safely')
        cases += 1
    print(f'PASS: MKN funeral/mission lifecycle, 32 political focuses, Soviet consent, native modifiers, map conservation and {cases} real-script collapse scenarios')
