"""Static MKN succession checks and execution of the real collapse arithmetic.

The tiny interpreter is intentionally strict: unsupported commands fail instead
of being silently ignored. It models fractional armed forces; actual game units
and geography still require a fresh-campaign reproduction.
"""
from collections import Counter
from copy import deepcopy
from itertools import product
from math import isclose
from pathlib import Path
import re

from hoi4_script import read, one, values, walk, variable_check


def validate_crisis(root, game, check, localized):
    effects = dict((k, v) for k, v, o in read(root / 'common/scripted_effects/MKN_effects.txt'))
    effects.update((k, v) for k, v, o in read(root / 'common/scripted_effects/MKN_intervention_effects.txt'))
    effects.update((k, v) for k, v, o in read(root / 'common/scripted_effects/MKN_ukr_border_effects.txt'))
    tree = one(read(root / 'common/national_focus/MKN.txt'), 'focus_tree')
    focuses = {one(f, 'id'): f for f in values(tree, 'focus')}
    events = {one(e, 'id'): e for e in values(read(root / 'events/MKN_events.txt'), 'country_event')}
    news = one(read(root / 'events/MKN_news_events.txt'), 'news_event')
    decisions = read(root / 'common/decisions/MKN_decisions.txt')
    mission = one(one(decisions, 'MKN_succession_crisis_category'), 'MKN_civil_war_timer_mission')
    routes = {
        'fascism': ['military_takes_charge', 'arrest_demagogues', 'abolish_election_of_commanders', 'militarize_communes', 'standardize_workshops', 'iron_fist_trains', 'black_expansionism', 'the_black_horde'],
        'democratic': ['triumph_of_free_soviets', 'pact_of_free_communes', 'abolish_general_staff', 'arms_to_the_people', 'propaganda_by_deed', 'autonomous_rail_crews', 'beacon_of_statelessness'],
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
    international = focuses['MKN_black_international']
    localized('MKN_black_international', 'MKN shared International')
    localized('MKN_black_international_desc', 'MKN shared International')
    check(not values(international, 'prerequisite'), 'MKN International: shared gate must avoid cross-branch connectors')
    prepared = set(values(one(one(international, 'available'), 'OR'), 'has_completed_focus'))
    check(prepared == {'MKN_arms_to_the_people', 'MKN_every_farm_a_fortress'}, 'MKN International: missing syndicalist/agrarian preparation')
    departure = focuses['MKN_departure_of_batko']
    check(one(departure, 'cost') == '5' and one(one(departure, 'available'), 'always') == 'no', 'MKN: funeral must be event-completed and preserve uniform focus costs')
    check(not one(departure, 'completion_reward'), 'MKN: funeral focus replays a political reward')
    funeral = events['mkn_crisis.1']
    check(one(one(funeral, 'mean_time_to_happen'), 'days') == '75', 'MKN: wrong funeral MTTH')
    guaranteed = one(one(funeral, 'mean_time_to_happen'), 'modifier')
    check(('date', '1937.2.28', '>') in one(funeral, 'trigger'), 'MKN: death can occur before March 1937')
    check(one(guaranteed, 'factor') == '0' and ('date', '1938.1.30', '>') in guaranteed, 'MKN: missing January 1938 hard deadline')
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
    command_files = ('common/scripted_effects/MKN_effects.txt', 'common/scripted_effects/MKN_intervention_effects.txt', 'events/MKN_events.txt', 'events/MKN_news_events.txt', 'common/decisions/MKN_decisions.txt')
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
                         'support': dict(zip(routes, popularity)), 'army': 1.0, 'name': 'MKN',
                         'original_tag': 'MKN', 'bop': True, 'missions': set()}
            self.countries = [self.root]
            self.states = [{'id': n, 'owner': self.root, 'flags': set()} for n in range(count)]
            self.targets = {}
            self.wars = set()
            self.removed = []
            self.activated = []
            self.global_flags = set()
            self.border_wars = set()
            self.cancelled_border_wars = []
            self.focus_completions = []
        def number(self, val, country):
            if val.startswith('var:'): val = val[4:]
            if val == 'num_owned_states': return sum(s['owner'] is country for s in self.states)
            if val.startswith('party_popularity@'): return country['support'][val.split('@')[1]]
            try: return float(val)
            except ValueError: return country['vars'][val]
        def compare(self, left, right, op):
            return {'=': left == right, '>': left > right, '<': left < right,
                    '>=': left >= right, '<=': left <= right, '!=': left != right,
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
                elif k == 'has_completed_focus': answers.append(v in scope.get('focuses', set()))
                elif k == 'has_global_flag': answers.append(v in self.global_flags)
                elif k == 'has_variable': answers.append(v in scope['vars'])
                elif k == 'has_border_war_with': answers.append(v in self.border_wars)
                elif k == 'original_tag': answers.append(scope['original_tag'] == v)
                elif k in ('any_country', 'any_other_country'):
                    answers.append(any(self.triggers(v, c) for c in self.countries if k == 'any_country' or c is not scope))
                elif k == 'is_controlled_by':
                    assert v == 'ROOT'
                    answers.append(scope['owner'] is self.root)
                elif k == 'has_power_balance': answers.append(scope['bop'])
                elif k == 'has_war_with': answers.append(frozenset((scope['name'], self.targets[v]['name'])) in self.wars)
                elif k == 'exists': answers.append((scope in self.countries) == (v == 'yes'))
                elif k == 'is_ai': answers.append(v == 'no')
                elif k == 'has_event_target': answers.append('event_target:' + v in self.targets)
                elif k == 'any_owned_state': answers.append(any(self.triggers(v, s) for s in self.states if s['owner'] is scope))
                elif k == 'check_variable':
                    key, value, comparison = variable_check(v)
                    a = self.number(key, scope); b = self.number(value, scope)
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
                elif k == 'set_global_flag': self.global_flags.add(v)
                elif k == 'clr_global_flag': self.global_flags.discard(v)
                elif k == 'ROOT': self.apply(v, self.root)
                elif k == 'every_country':
                    for country in self.countries:
                        if self.triggers(one(v, 'limit', []), country):
                            self.apply([n for n in v if n[0] != 'limit'], country)
                elif k in ('every_owned_state', 'random_owned_state'):
                    owned = [s for s in self.states if s['owner'] is scope and self.triggers(one(v, 'limit', []), s)]
                    for s in owned if k == 'every_owned_state' else owned[:1]:
                        self.apply([n for n in v if n[0] != 'limit'], s)
                elif k == 'capital_scope': self.apply(v, self.states[0])
                elif k == 'activate_mission':
                    scope['missions'].add(v)
                    self.activated.append((scope['name'], v))
                elif k == 'remove_mission':
                    scope['missions'].discard(v)
                    self.removed.append((scope['name'], v))
                elif k == 'remove_power_balance': scope['bop'] = False
                elif k == 'cancel_border_war':
                    assert one(v, 'dont_fire_events') == 'yes', 'MKN: ending the frontier replays victory callbacks'
                    self.cancelled_border_wars.append((self.number(one(v, 'attacker'), scope), self.number(one(v, 'defender'), scope)))
                    self.border_wars.clear()
                elif k in effects: self.apply(effects[k], scope)
                elif k == 'start_civil_war':
                    ratio = self.number(one(v, 'army_ratio', one(v, 'size')), scope)
                    for field in ('size', 'air_ratio', 'navy_ratio'): assert isclose(ratio, self.number(one(v, field, str(ratio)), scope))
                    owned = [s for s in self.states if s['owner'] is scope]
                    land = [s for s in owned if self.triggers(one(v, 'states_filter'), s)] if one(v,'states_filter') else owned[1:1+max(1,len(owned)//2)]
                    assert land and len(land) < sum(s['owner'] is scope for s in self.states)
                    child = {'vars': deepcopy(scope['vars']), 'flags': set(scope['flags']), 'government': one(v, 'ideology'), 'support': deepcopy(scope['support']), 'army': scope['army'] * ratio, 'name': 'D' + str(len(self.countries)), 'original_tag': scope['original_tag'], 'bop': scope['bop'], 'missions': set(scope['missions'])}
                    scope['army'] *= 1 - ratio
                    for s in land: s['owner'] = child
                    self.countries.append(child)
                    self.wars.add(frozenset((scope['name'], child['name'])))
                    arguments = {'ideology', 'size', 'army_ratio', 'navy_ratio', 'air_ratio', 'states', 'states_filter', 'keep_all_characters'}
                    self.apply([n for n in v if n[0] not in arguments], child)
                elif k == 'set_politics': scope['government'] = one(v, 'ruling_party')
                elif k == 'set_popularities': scope['support'] = {key: float(val) / 100 for key, val, o in v}
                elif k == 'set_cosmetic_tag': scope['cosmetic'] = v
                elif k in ('save_event_target_as', 'save_global_event_target_as'): self.targets['event_target:' + v] = scope
                elif k == 'load_focus_tree': scope['tree'] = one(v,'tree')
                elif k == 'add_ideas': scope.setdefault('ideas',set()).add(v)
                elif k == 'remove_ideas': scope.setdefault('ideas',set()).discard(v)
                elif k == 'complete_national_focus':
                    scope.setdefault('focuses',set()).add(v)
                    self.focus_completions.append(v)
                    self.apply(one(focuses[v], 'completion_reward', []), scope)
                elif k == 'uncomplete_national_focus':
                    focus = one(v, 'focus')
                    removed = {focus}
                    while True:
                        children = {fid for fid, f in focuses.items() if any(parent in removed for group in values(f, 'prerequisite') for parent in values(group, 'focus'))}
                        if children <= removed: break
                        removed |= children
                    scope.setdefault('focuses',set()).difference_update(removed)
                elif k == 'add_stability': scope['stability'] = scope.get('stability', 0) + float(v)
                elif k in ('nww_mkn_rebuild_industry', 'nww_mkn_rebuild_services'):
                    # Parameter replay is executed separately by validate_redesign.
                    scope.setdefault('rebuilds', []).append(k)
                elif k == 'mark_focus_tree_layout_dirty': scope['layout_dirty'] = True
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
                check(len(model.countries) == 2 and len(model.wars) == 1, 'MKN: collapse is not a two-way duel')
                strongest = max((p for p in routes if p != ruling), key=lambda p: popularity[list(routes).index(p)])
                check(model.countries[1]['government'] == strongest, 'MKN: challenger is not strongest opposition')
                check(model.root['government'] == ruling and model.states[0]['owner'] is model.root, 'MKN: player loses ideology or capital')
                check(all(not c['bop'] for c in model.countries), 'MKN: collapse preserves or resurrects BoP')
                check(all('MKN_soviet_intervention_mission' not in c['missions'] for c in model.countries), 'MKN: new duel inherits obsolete intervention')
                check(all('MKN_collapse_participant' in c['flags'] for c in model.countries), 'MKN: collapse faction lacks intervention enrollment')
                check(not model.activated, 'MKN: duel starts obsolete intervention timers')
                support = list(popularity); total = sum(support)
                for c in model.countries:
                    check(isclose(c['army'], 0.5, abs_tol=1e-8), f'MKN: duel military split incorrect for {ruling}/{popularity}')
                    land = sum(s['owner'] is c for s in model.states)
                    check(land > 0, 'MKN: duel participant has no territory')
                check(isclose(sum(c['army'] for c in model.countries), 1), 'MKN: collapse creates/destroys military resources')
                cases += 1
    # Reduced territory must terminate safely and must never give away the last state.
    for count in (2, 3):
        model = Interpreter((.25, .25, .25, .25), 'communism', count)
        model.apply(effects['MKN_execute_four_way_collapse'], model.root)
        check(len(model.countries) == 2 and model.states[0]['owner'] is model.root, 'MKN: reduced-land duel fails safely')
        cases += 1
    # Collapse interrupts an active frontier battle before child countries inherit
    # the annual timer. Suppressed callbacks must not transfer or core a state.
    model = Interpreter((0.25, 0.25, 0.25, 0.25), 'fascism', 4)
    model.root['flags'].update({'mkn_frontier_year_running', 'mkn_ukr_border_battle_active', 'mkn_ukr_war_pending', 'mkn_ukr_pact_pending'})
    model.root['missions'].add('MKN_frontier_year_countdown_mission')
    model.root['vars'].update(mkn_ukr_attacking_state=1, mkn_ukr_defending_state=99)
    model.border_wars.add('UKR')
    model.apply(effects['MKN_execute_four_way_collapse'], model.root)
    check(not model.border_wars and model.cancelled_border_wars == [(1, 99)], 'MKN: collapse leaves its native border battle running')
    check(all('MKN_frontier_year_countdown_mission' not in c['missions'] for c in model.countries), 'MKN: collapse factions inherit the frontier deadline')
    pending = {'mkn_frontier_year_running', 'mkn_ukr_border_battle_active', 'mkn_ukr_war_pending', 'mkn_ukr_pact_pending'}
    check(all(not pending & c['flags'] for c in model.countries), 'MKN: collapse factions inherit active frontier negotiations or countdown flags')
    check(all({'mkn_ukr_frontier_concluded', 'mkn_ukr_frontier_aborted'} <= c['flags'] for c in model.countries), 'MKN: collapse does not close the frontier for every faction')
    cases += 1
    # Execute recovery for both winners on every path. Focus completion executes
    # its real reward, and repeated repair must not repeat its political reward.
    for party, route in routes.items():
        for rebel_wins in (False, True):
            model = Interpreter((0.25, 0.25, 0.25, 0.25), party, 4)
            model.apply(effects['MKN_execute_four_way_collapse'], model.root)
            winner = model.countries[int(rebel_wins)]
            winner['focuses'] = {'MKN_congress_1936', 'MKN_departure_of_batko'}
            model.wars.clear()
            model.apply(effects['MKN_recover_duel_winner'], winner)
            first = 'MKN_' + routes[winner['government']][0]
            check(first in winner['focuses'], 'MKN: winner does not complete its first political focus')
            check(not {'mkn_collapsed', 'MKN_collapse_started', 'MKN_duel_choice_pending'} & winner['flags'], 'MKN: winner remains locked by collapse flags')
            check(not winner['bop'], 'MKN: victory resurrects the removed balance of power')
            before = list(model.focus_completions)
            model.apply(effects['MKN_recover_duel_winner'], winner)
            check(model.focus_completions == before, 'MKN: repeated recovery repeats focus rewards')
            cases += 1
    print(f'PASS: MKN funeral/mission lifecycle, 32 political focuses, Soviet consent, native modifiers, map conservation and {cases} real-script collapse scenarios')
    validate_intervention(root, check, localized)


def validate_intervention(root, check, localized):
    """Execute real mission/event/effects scripts with strict country diplomacy."""
    effects = dict((k, v) for k, v, o in read(root / 'common/scripted_effects/MKN_intervention_effects.txt'))
    events = {one(e, 'id'): e for e in values(read(root / 'events/MKN_events.txt'), 'country_event')}
    event = events['mkn_crisis.200']
    decisions = read(root / 'common/decisions/MKN_decisions.txt')
    mission = one(one(decisions, 'MKN_soviet_intervention_category'), 'MKN_soviet_intervention_mission')
    check(one(mission, 'days_mission_timeout') == '100', 'MKN: wrong Soviet intervention deadline')
    check(one(one(mission, 'activation'), 'always') == 'no', 'MKN: Soviet intervention mission auto-starts')
    check(one(mission, 'fire_only_once') == 'yes', 'MKN: Soviet intervention mission can restart')
    check(not any(k == 'activate_mission' for k, v, o in walk(effects['MKN_repair_soviet_intervention'])), 'MKN: daily intervention repair resets its deadline')
    for key in ('MKN_soviet_intervention_category', 'MKN_soviet_intervention_category_desc',
                'MKN_soviet_intervention_mission', 'MKN_soviet_intervention_mission_desc',
                'mkn_crisis.200.t', 'mkn_crisis.200.d', 'mkn_crisis.200.a', 'MKN_soviet_intervention_tt'):
        localized(key, 'MKN Soviet intervention')
    daily = one(one(read(root / 'common/on_actions/MKN_intervention_on_actions.txt'), 'on_actions'), 'on_daily')
    check(one(one(daily, 'effect'), 'every_country') is not None, 'MKN: intervention daily repair omits dynamic civil-war tags')
    class Model:
        def __init__(self):
            self.cs = [dict(name=n, origin='MKN', states=1, flags={'MKN_collapse_started'},
                            faction=None, leader=False, subject=False, alive=True, mission=False)
                       for n in ('MKN', 'D01', 'D02', 'D03')]
            self.cs += [dict(name=n, origin=n, states=10, flags=set(), faction=None,
                             leader=False, subject=False, alive=True, mission=False)
                        for n in ('SOV', 'UKR', 'GER')]
            self.globals, self.targets, self.queue = set(), {}, []
            self.wars, self.goals, self.displayed, self.activations = set(), set(), 0, []
            for c in self.cs[:4]: self.apply(effects['MKN_initialize_soviet_intervention'], c)
        def ref(self, s):
            if s.startswith('event_target:'): return self.targets[s.split(':', 1)[1]]
            return next(c for c in self.cs if c['name'] == s)
        def allied(self, a, b):
            return a is b or bool(a['faction'] and a['faction'] == b['faction']) or a.get('master') is b or b.get('master') is a
        def trig(self, nodes, c):
            results = []
            for k, v, op in nodes:
                if k == 'NOT': q = not self.trig(v, c)
                elif k == 'OR': q = any(self.trig([n], c) for n in v)
                elif k == 'original_tag': q = c['origin'] == v
                elif k == 'has_country_flag': q = v in c['flags']
                elif k == 'has_global_flag': q = v in self.globals
                elif k == 'check_variable':
                    variable, value, comparator = variable_check(v)
                    assert variable == 'num_owned_states'
                    n = float(value); q = {'>': c['states'] > n, '<': c['states'] < n, '=': c['states'] == n}[comparator]
                elif k in ('any_country', 'any_other_country'):
                    q = any(self.trig(v, d) for d in self.cs if d['alive'] and (k == 'any_country' or d is not c))
                elif k == 'exists': q = c['alive'] == (v == 'yes')
                elif k == 'is_subject': q = c['subject'] == (v == 'yes')
                elif k == 'is_faction_leader': q = c['leader'] == (v == 'yes')
                elif k == 'is_ally_with': q = self.allied(c, self.ref(v))
                elif k == 'is_in_faction_with':
                    d = self.ref(v); q = bool(c['faction'] and c['faction'] == d['faction'])
                elif k == 'has_war_with': q = frozenset((c['name'], self.ref(v)['name'])) in self.wars
                elif k == 'always': q = v == 'yes'
                elif k in ('SOV', 'UKR'): q = self.trig(v, self.ref(k))
                else: raise AssertionError(('unsupported trigger', k))
                results.append(q)
            return all(results)
        def apply(self, nodes, c):
            matched = False
            for k, v, op in nodes:
                if k in ('if', 'else_if'):
                    if k == 'if': matched = False
                    if not matched and self.trig(one(v, 'limit', []), c):
                        self.apply([n for n in v if n[0] != 'limit'], c); matched = True
                elif k == 'else':
                    if not matched: self.apply(v, c)
                elif k == 'every_country':
                    for d in self.cs:
                        if d['alive'] and self.trig(one(v, 'limit', []), d):
                            self.apply([n for n in v if n[0] != 'limit'], d)
                elif k == 'set_country_flag': c['flags'].add(v)
                elif k == 'set_global_flag': self.globals.add(v)
                elif k == 'clr_global_flag': self.globals.discard(v)
                elif k == 'activate_mission':
                    c['mission'] = True; self.activations.append(c['name'])
                elif k == 'remove_mission': c['mission'] = False
                elif k == 'save_event_target_as': self.targets[v] = c
                elif k == 'country_event':
                    assert one(v, 'id') == 'mkn_crisis.200'; self.queue.append(c)
                elif k == 'remove_from_faction':
                    d = self.ref(v); assert c['leader'] and c['faction'] == d['faction']
                    d['faction'], d['leader'] = None, False
                elif k == 'faction_leader':
                    d = next(d for d in self.cs if d['faction'] == c['faction'] and d['leader'])
                    self.apply(v, d)
                elif k == 'create_wargoal':
                    assert one(v, 'type') == 'annex_everything'; self.goals.add((c['name'], self.ref(one(v, 'target'))['name']))
                elif k == 'declare_war_on':
                    d = self.ref(one(v, 'target')); assert not self.allied(c, d)
                    self.wars.add(frozenset((c['name'], d['name'])))
                elif k in effects: self.apply(effects[k], c)
                elif k.startswith('event_target:') or k in ('SOV', 'UKR'): self.apply(v, self.ref(k))
                else: raise AssertionError(('unsupported effect', k))
        def timeout(self, c): self.apply(one(mission, 'timeout_effect'), c)
        def repair(self):
            for c in self.cs[:4]:
                if c['alive']: self.apply(effects['MKN_repair_soviet_intervention'], c)
        def flush(self):
            queued, self.queue = self.queue, []
            for c in queued:
                if c['alive'] and self.trig(one(event, 'trigger'), c):
                    self.displayed += 1; self.apply(one(event, 'immediate'), c)

    checks = 0
    for active in product((False, True), repeat=4):
        m = Model()
        for c, alive in zip(m.cs[:4], active): c['states'] = int(alive)
        m.repair()
        for c in m.cs[:4]: m.timeout(c)
        m.flush()
        if sum(active) < 2:
            assert not m.wars and m.displayed == 0
            assert ('MKN_collapse_reunified' in m.globals) == (sum(active) == 1)
        else:
            assert m.displayed == 1 and len(m.wars) == 2 * sum(active)
        assert not any(c['mission'] for c in m.cs[:4])
        assert m.activations == ['MKN', 'D01', 'D02', 'D03']
        checks += 1

    # Reunification between queued timeout and event execution wins the deadline race.
    m = Model()
    for c in m.cs[:4]: m.timeout(c)
    for c in m.cs[1:4]: c['states'] = 0
    m.flush()
    assert not m.wars and not m.displayed
    m.repair()
    assert not any(c['mission'] for c in m.cs[:4])
    assert m.activations == ['MKN', 'D01', 'D02', 'D03']
    checks += 1

    # The first dispatch owner can die; the surviving tags resume the same deadline.
    m = Model(); m.timeout(m.cs[0]); m.cs[0]['states'] = 0; m.cs[0]['alive'] = False
    m.flush(); m.repair(); m.flush()
    assert m.displayed == 1 and len(m.wars) == 6
    assert m.activations == ['MKN', 'D01', 'D02', 'D03']
    checks += 1

    # Shared faction cases: Soviet leader, MKN participant leader, foreign leader.
    for leader in ('SOV', 'MKN', 'GER'):
        m = Model()
        for c in m.cs: c['faction'], c['leader'] = 'test', c['name'] == leader
        m.timeout(m.cs[0]); m.flush()
        assert m.displayed == 1 and len(m.wars) == 8 and len(m.goals) == 8
        checks += 1

    # An unavailable aggressor does not affect declarations by the other actor.
    for inactive in ('dead', 'subject'):
        m = Model(); u = m.ref('UKR')
        if inactive == 'dead': u['alive'] = False
        else: u['subject'] = True
        m.timeout(m.cs[0]); m.flush()
        assert len(m.wars) == 4 and all('SOV' in w for w in m.wars)
        checks += 1

    # Old generic tags lacking participant enrollment cannot count as an heir.
    m = Model()
    extra = dict(m.cs[1], name='D99', flags={'MKN_collapse_started'})
    m.cs.append(extra)
    for c in m.cs[1:4]: c['states'] = 0
    m.repair(); m.timeout(m.cs[0]); m.flush()
    assert not m.wars and 'MKN_collapse_reunified' in m.globals
    checks += 1
    print(f'PASS: MKN 100-day intervention, sole-survivor races, faction splits, once-only dispatch and {checks} real-script scenarios')
