"""Regression checks for Ukrainian choices and military save migration."""
from itertools import product
from math import isclose
from collections import Counter
import json

from hoi4_script import read, one, values, walk


def validate_redesign(root, game, check, localized):
    trees = {
        tag: {one(f, 'id'): f for f in values(one(read(root / ('common/national_focus/MKN.txt' if tag == 'MKN' else f'common/national_focus/{tag.lower()}_focus.txt')), 'focus_tree'), 'focus')}
        for tag in ('UKR', 'MKN')
    }
    uf = trees['UKR']
    choices = [
        ('UKR_grain_exports', 'UKR_domestic_grain', 'UKR_balanced_economic_compact'),
        ('UKR_defence_in_depth', 'UKR_mobile_reserves', 'UKR_prepared_defence'),
        ('UKR_interceptor_command', 'UKR_assault_aviation', 'UKR_integrated_air_service'),
        ('UKR_merchant_escorts', 'UKR_sea_denial', 'UKR_safe_trade_routes'),
    ]
    political = [
        ['UKR_council_mandate', 'UKR_cooperative_land', 'UKR_elected_factory_boards', 'UKR_council_courts', 'UKR_social_republic'],
        ['UKR_constituent_mandate', 'UKR_land_titles', 'UKR_elected_municipalities', 'UKR_independent_courts', 'UKR_federal_republic'],
        ['UKR_state_mandate', 'UKR_rural_compact', 'UKR_professional_civil_service', 'UKR_state_arbitration', 'UKR_constitutional_directory'],
    ]

    def focus_conditions(nodes, done):
        # Evaluate focus gates, including negated legacy paths. Other game state
        # (popularity, flags, BoP, diplomacy) remains unknown to this graph check.
        results = []
        for key, value, op in nodes:
            if key == 'has_completed_focus':
                results.append(value in done)
            elif key in ('NOT', 'AND', 'OR', 'custom_trigger_tooltip'):
                children = [focus_conditions([item], done) for item in value]
                if key == 'OR':
                    result = True if True in children else None if None in children else False
                else:
                    result = False if False in children else None if None in children else True
                    if key == 'NOT' and result is not None:
                        result = not result
                results.append(result)
            else:
                results.append(None)
        return False if False in results else None if None in results else True

    def gates_ready(f, done):
        groups = values(f, 'prerequisite')
        return all(set(values(g, 'focus')) & done for g in groups) and focus_conditions(one(f, 'available', []), done) is not False

    def reachable(fs, excluded):
        done = set()
        while True:
            ready = {fid for fid, f in fs.items() if fid not in excluded | done and gates_ready(f, done)}
            if not ready:
                return done
            done |= ready

    scenarios = {'UKR': [set()], 'MKN': [set()]}
    political_ids = set(sum(political, []))
    for path, picks in product(political, product((0, 1), repeat=4)):
        excluded = political_ids - set(path)
        excluded |= {pair[1 - pick] for pair, pick in zip(choices, picks)}
        done = reachable(uf, excluded)
        check(done == uf.keys() - excluded, f'UKR: inaccessible focuses for {path[0]} / {picks}: {uf.keys() - excluded - done}')
        scenarios['UKR'].append(done)
    for left, right, end in choices:
        for fid, other in ((left, right), (right, left)):
            excluded = {p for g in values(uf[fid], 'mutually_exclusive') for p in values(g, 'focus')}
            check(other in excluded, f'{fid}: specialization exclusion is not reciprocal')
        check(one(uf[left], 'completion_reward') != one(uf[right], 'completion_reward'), f'{end}: choice has identical rewards')
    check(len({one(f, 'icon') for f in uf.values()}) >= 45, 'UKR: insufficient icon variety')
    check(len({str(one(f, 'completion_reward')) for f in uf.values()}) >= 70, 'UKR: insufficient reward variety')
    for fid in ('UKR_friends_in_moscow', 'UKR_polish_trade', 'UKR_the_makhno_question'):
        check(not values(uf[fid], 'prerequisite'), f'{fid}: another neighbour blocks diplomacy')

    programs = json.loads((root / 'docs/MKN_military_programs.json').read_text())
    for picks in product((0, 1), repeat=3):
        selected = [programs[service * 2 + pick] for service, pick in enumerate(picks)]
        excluded = {fid for p in programs if p not in selected for fid in p['focuses']}
        scenarios['MKN'].append(reachable(trees['MKN'], excluded))
    # Each partially developed branch must migrate accurately, including old saves
    # which completed optional focuses before the new core capstone existed.
    for p in programs:
        for count in range(1, len(p['focuses']) + 1):
            scenarios['MKN'].append(set(p['focuses'][:count]))
    for fid in uf:
        scenarios['UKR'].append({fid})

    equipment = {k for path in (game / 'common/units/equipment').glob('*.txt')
                 for k, v, o in one(read(path), 'equipments', [])}
    tracks = {k for path in (game / 'common/doctrines/tracks').glob('*.txt') for k, v, o in read(path)}
    for fs in trees.values():
        for fid, f in fs.items():
            for k, v, o in walk(one(f, 'completion_reward')):
                if k == 'add_equipment_to_stockpile':
                    check(one(v, 'type') in equipment, f'{fid}: nonexistent equipment {one(v, "type")}')
                if k == 'add_mastery_bonus':
                    check(one(v, 'track') in tracks, f'{fid}: unknown doctrine mastery track')
                    localized(one(v, 'name'), fid)
                if k == 'add_to_variable':
                    localized(one(v, 'tooltip'), fid)

    # Each new succession program and every intermediate institution must replay exactly.
    crisis_routes = (
        ('military_takes_charge', 'arrest_demagogues', 'abolish_election_of_commanders', 'militarize_communes', 'standardize_workshops', 'iron_fist_trains', 'black_expansionism', 'the_black_horde'),
        ('triumph_of_free_soviets', 'pact_of_free_communes', 'abolish_general_staff', 'arms_to_the_people', 'black_international', 'propaganda_by_deed', 'autonomous_rail_crews', 'beacon_of_statelessness'),
        ('peasant_delegates', 'grain_ultimatum', 'sever_urban_ties', 'every_farm_a_fortress', 'steppe_snipers', 'railway_sabotage', 'cavalry_ambush', 'impregnable_granary'),
        ('emergency_revkom', 'purge_irreconcilables', 'embassy_to_kharkov', 'integrate_steel_lines', 'red_military_specialists', 'tractors_for_grain', 'anti_imperialist_front', 'the_fatal_plenum'),
    )
    for route in crisis_routes:
        for count in range(1, len(route) + 1):
            scenarios['MKN'].append({'MKN_congress_1936', 'MKN_departure_of_batko', 'MKN_question_of_supply'} | {'MKN_' + token for token in route[:count]})
    for tag, fs in trees.items():
        file = f'common/scripted_effects/nww_{tag.lower()}_progression.txt'
        effect = 'nww_mkn_rebuild_services' if tag == 'MKN' else 'nww_ukr_rebuild_progression'
        rebuild = one(read(root / file), effect)
        initial = {k: float(v) for b in values(rebuild, 'set_variable') for k, v, o in b}
        prefix = tag + '_'
        # A migration must never replay buildings, equipment, politics or mastery.
        safe = {'set_variable', 'add_to_variable', 'if', 'limit', 'has_completed_focus', 'always',
                'NOT', 'has_dynamic_modifier', 'modifier', 'add_dynamic_modifier', 'remove_ideas', 'set_country_flag'}
        for k, v, o in walk(rebuild):
            check(k is None or k in safe or (k.startswith(prefix) and not isinstance(v, list)), f'{effect}: migration replays unsupported effect {k}')
        replay = {}
        for node in values(rebuild, 'if'):
            fid = one(one(node, 'limit'), 'has_completed_focus')
            for b in values(node, 'add_to_variable'):
                check(fid in fs, f'{effect}: missing source focus {fid}')
                replay.setdefault(fid, Counter()).update({k: float(v) for k, v, o in b})
        rewards = {}
        for fid, f in fs.items():
            changes = Counter()
            for b in values(one(f, 'completion_reward'), 'add_to_variable'):
                changes.update({k: float(v) for k, v, o in b if k != 'tooltip' and k in initial})
            if changes:
                rewards[fid] = changes
        check(replay == rewards, f'{effect}: replay does not match current focus bonuses')
        for done in scenarios[tag]:
            expected = dict(initial)
            migrated = dict(initial)
            for table, result in ((rewards, expected), (replay, migrated)):
                for fid in done:
                    for var, amount in table.get(fid, {}).items():
                        result[var] += amount
            check(all(isclose(expected[k], migrated[k], abs_tol=1e-9) for k in initial), f'{effect}: incorrect old-save scenario')
            # Rebuilding starts with assignments, so repeated repair is idempotent.
            again = dict(initial)
            for fid in done:
                for var, amount in replay.get(fid, {}).items():
                    again[var] += amount
            check(all(isclose(again[k], migrated[k], abs_tol=1e-9) for k in initial), f'{effect}: repeated repair stacks bonuses')
        on = one(read(root / f'common/on_actions/nww_{tag.lower()}_progression.txt'), 'on_actions')
        flag = 'MKN_services_redesign_v4' if tag == 'MKN' else 'UKR_focus_redesign_v1'
        for hook in ('on_startup', 'on_daily_' + tag):
            node = one(on, hook, [])
            check(any(k == effect for k, v, o in walk(node)), f'{tag}: missing {hook} migration')
            check(any(k == 'has_country_flag' and v == flag for k, v, o in walk(node)), f'{tag}: unguarded {hook} migration')
        print(f'PASS: {tag}: {len(scenarios[tag])} migration scenarios, exact parameter replay, no repeated one-off rewards')
    print('PASS: 48 Ukraine political/program combinations, independent diplomacy, equipment and doctrine mastery references')
