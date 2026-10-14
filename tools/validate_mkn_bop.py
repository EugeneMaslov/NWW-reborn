"""Native BoP references, political paths and old-save lifecycle regressions."""
from copy import deepcopy
from collections import Counter
import re

from hoi4_script import read, one, values, walk


def validate_bop(root, game, check, localized):
    balance = one(read(root / 'common/bop/MKN_bop.txt'), 'MKN_power_balance')
    localized('MKN_power_balance', 'MKN BoP')
    ranges = list(values(balance, 'range'))
    sides = values(balance, 'side')
    check({one(s, 'id') for s in sides} == {'MKN_military_command_side', 'MKN_free_soviets_side'}, 'MKN BoP: invalid sides')
    documented = set(re.findall(r'^## (\w+)', (game / 'documentation/modifiers_documentation.md').read_text(), re.M))
    for side in sides:
        localized(one(side, 'id'), 'MKN BoP side')
        ranges += values(side, 'range')
    ranges.sort(key=lambda r: float(one(r, 'min')))
    check(len(ranges) == 5, 'MKN BoP: expected five ranges')
    boundaries = [-1, -.6, -.1, .1, .6, 1]
    for i, span in enumerate(ranges):
        localized(one(span, 'id'), 'MKN BoP range')
        check(float(one(span, 'min')) == boundaries[i] and float(one(span, 'max')) == boundaries[i + 1], 'MKN BoP: gaps or incorrect control thresholds')
        for modifier, value, op in one(span, 'modifier'):
            check(modifier in documented, f'MKN BoP: undocumented modifier {modifier}')
    check(float(one(balance, 'initial_value')) == 0, 'MKN BoP: campaign should start balanced')
    check(float(one(one(ranges[0], 'modifier'), 'army_attack_factor')) > 0 and float(one(one(ranges[0], 'modifier'), 'stability_factor')) < 0, 'MKN BoP: military extreme lacks its tradeoff')
    check(float(one(one(ranges[-1], 'modifier'), 'army_core_defence_factor')) >= .25 and float(one(one(ranges[-1], 'modifier'), 'army_org_factor')) <= -.20, 'MKN BoP: soviet extreme lacks its tradeoff')
    # Native effects and triggers are checked against the actual executable's docs.
    for doc, tokens in {
        'effects': ('set_power_balance', 'remove_power_balance', 'add_power_balance_value', 'create_faction', 'add_to_faction', 'create_wargoal', 'set_rule'),
        'triggers': ('has_power_balance', 'power_balance_value', 'is_in_faction_with'),
    }.items():
        names = set(re.findall(r'^## (\w+)', (game / f'documentation/{doc}_documentation.md').read_text(), re.M))
        for name in tokens:
            check(name in names, f'MKN BoP: undocumented {doc} token {name}')
    files = ('common/bop/MKN_bop.txt', 'common/decisions/MKN_bop_decisions.txt', 'common/scripted_effects/MKN_bop_effects.txt', 'common/national_focus/MKN.txt')
    for filename in files:
        for k, v, op in walk(read(root / filename)):
            check(k != 'add_bop_power', f'{filename}: nonexistent add_bop_power effect')
            if k in ('set_power_balance', 'add_power_balance_value', 'remove_power_balance', 'has_power_balance', 'power_balance_value'):
                check(one(v, 'id') == 'MKN_power_balance', f'{filename}: wrong BoP reference')
            if k == 'add_power_balance_value':
                direction = float(one(v, 'value'))
                check(one(v, 'tooltip_side') == ('MKN_military_command_side' if direction < 0 else 'MKN_free_soviets_side'), f'{filename}: incorrect tooltip direction')

    decisions = one(read(root / 'common/decisions/MKN_bop_decisions.txt'), 'MKN_bop_category')
    check(len(decisions) >= 3, 'MKN BoP: fewer than three decisions')
    for token, decision, op in decisions:
        check(float(one(decision, 'cost')) > 0 and int(one(decision, 'days_re_enable')) > 0, f'{token}: missing PP cost or repeat cooldown')
        check(one(decision, 'fire_only_once') != 'yes', f'{token}: not repeatable')

    fs = {one(f, 'id'): f for f in values(one(read(root / 'common/national_focus/MKN.txt'), 'focus_tree'), 'focus')}
    check(values(one(fs['MKN_departure_of_batko'], 'prerequisite'), 'focus') == ['MKN_congress_1936'], 'MKN: invalid shared root')
    entries = {'MKN_black_hundreds': 'fascism', 'MKN_constituent_assembly': 'democratic', 'MKN_nestor_the_first': 'neutrality', 'MKN_red_banner_steppe': 'communism'}
    for fid, ideology in entries.items():
        excluded = {v for g in values(fs[fid], 'mutually_exclusive') for v in values(g, 'focus')}
        check(excluded == entries.keys() - {fid}, f'{fid}: four paths are not mutually exclusive')
        politics = one(one(fs[fid], 'completion_reward'), 'set_politics')
        check(one(politics, 'ruling_party') == ideology and one(politics, 'elections_allowed') == 'no', f'{fid}: incomplete government/election block')
    for fid in ('MKN_everlasting_makhnovshchina', 'MKN_council_communism'):
        check(values(one(fs[fid], 'prerequisite'), 'focus') == ['MKN_free_elections_steppe'], f'{fid}: legacy anarchist program escapes democratic branch')
    for fid in ('MKN_steppe_legions', 'MKN_ataman_directorate'):
        gate = one(one(fs[fid], 'available'), 'power_balance_value')
        check(('value', '-0.6', '<') in gate, f'{fid}: missing total military control gate')
    check(not any(k == 'add_to_faction' for f in fs.values() for k, v, op in walk(one(f, 'completion_reward'))), 'MKN: focus forces foreign alliance without consent')
    for f in fs.values():
        reward = one(f, 'completion_reward')
        check(not any(k == 'add_ideas' and isinstance(v, str) and v in {'MKN_planned_economy', 'MKN_communal_federation', 'MKN_federal_republic', 'MKN_imperial_administration', 'MKN_military_directory'} for k, v, o in walk(reward)), 'MKN: political path creates a second persistent development spirit')

    # Compare every economic focus parameter to its real migration replay.
    rebuild = one(read(root / 'common/scripted_effects/nww_mkn_progression.txt'), 'nww_mkn_rebuild_industry')
    expected, replay = {}, {}
    for fid, f in fs.items():
        changes = Counter()
        for b in values(one(f, 'completion_reward'), 'add_to_variable'):
            changes.update({k: float(v) for k, v, o in b if k.startswith('MKN_unified_')})
        if changes: expected[fid] = changes
    for node in values(rebuild, 'if'):
        fid = one(one(node, 'limit'), 'has_completed_focus')
        changes = Counter()
        for b in values(node, 'add_to_variable'):
            changes.update({k: float(v) for k, v, o in b if k.startswith('MKN_unified_')})
        if changes: replay[fid] = changes
    check(replay == expected, 'MKN: economic migration does not reproduce political focus parameters')
    scripts = values(read(root / 'common/scripted_localisation/MKN_ideology_names.txt'), 'defined_text')
    helpers = {one(d, 'name') for d in scripts}
    for node in scripts:
        for text in values(node, 'text'):
            localized(one(text, 'localization_key'), 'MKN ideology display')
    for lang in ('english', 'russian'):
        loc = (root / f'localisation/replace/{lang}/MKN_ideologies_l_{lang}.yml').read_text(encoding='utf-8-sig')
        for helper in re.findall(r'\[(\w+)\]', loc):
            check(helper in helpers, f'MKN: missing dynamic ideology selector {helper}')

    # Evaluate the real repair script. Unsupported syntax fails rather than being ignored.
    initialize = one(read(root / 'common/scripted_effects/MKN_bop_effects.txt'), 'nww_mkn_initialize_bop')

    def triggers(nodes, state):
        result = []
        for key, val, op in nodes:
            if key == 'NOT': result.append(not triggers(val, state))
            elif key == 'OR': result.append(any(triggers([item], state) for item in val))
            elif key == 'has_completed_focus': result.append(val in state['done'])
            elif key == 'has_country_flag': result.append(val in state['flags'])
            elif key == 'has_power_balance': result.append(state['value'] is not None)
            else: raise AssertionError(f'Unhandled repair trigger {key}')
        return all(result)

    def apply(nodes, state):
        matched = False
        for key, val, op in nodes:
            if key in ('if', 'else_if'):
                eligible = key == 'if' or not matched
                if key == 'if': matched = False
                if eligible and triggers(one(val, 'limit'), state):
                    apply([(k, v, o) for k, v, o in val if k != 'limit'], state)
                    matched = True
            elif key == 'set_power_balance': state['value'] = float(one(val, 'set_value'))
            elif key == 'remove_power_balance': state['value'] = None
            elif key == 'set_country_flag': state['flags'].add(val)
            else: raise AssertionError(f'Unsafe or unhandled repair effect {key}')

    cases = [(set(), 0), ({'MKN_black_hundreds'}, -.65), ({'MKN_red_banner_steppe'}, .35), ({'MKN_constituent_assembly'}, .65), ({'MKN_everlasting_makhnovshchina'}, .65), ({'MKN_council_communism'}, .65), ({'MKN_nestor_the_first'}, None)]
    for done, expected in cases:
        for initial in (None, -.91, .28):
            state = {'done': done, 'flags': set(), 'value': initial}
            apply(initialize, state)
            wanted = None if 'MKN_nestor_the_first' in done else expected if initial is None else initial
            check(state['value'] == wanted, f'MKN BoP repair: incorrect old-save state {done}/{initial}')
            before = deepcopy(state)
            apply(initialize, state)
            check(state == before, 'MKN BoP repair: repeated repair changes player balance')
    state = {'done': set(), 'flags': {'MKN_bop_abandoned'}, 'value': None}
    apply(initialize, state)
    check(state['value'] is None, 'MKN BoP repair: resurrects abandoned balance')
    events = {one(e, 'id'): e for e in values(read(root / 'events/MKN_bop_events.txt'), 'country_event')}
    options = values(events['mkn_bop.1'], 'option')
    check(len(options) == 3, 'MKN: Moscow must be able to accept, betray or decline')
    check(one(options[0], 'add_to_faction') == 'MKN' and one(options[1], 'create_wargoal') is not None, 'MKN: invalid diplomatic outcomes')
    check(not any(k in ('add_to_faction', 'create_wargoal', 'declare_war_on') for k, v, o in walk(options[2])), 'MKN: decline causes alliance or war')
    for option in options:
        check(any(k == 'clr_country_flag' and v == 'MKN_moscow_request_pending' for k, v, o in walk(option)), 'MKN: diplomatic response leaves pending request')
    for hook in ('on_startup', 'on_daily_MKN'):
        on = one(one(read(root / 'common/on_actions/nww_mkn_progression.txt'), 'on_actions'), hook)
        check(any(k == 'nww_mkn_initialize_bop' for k, v, o in walk(on)), f'MKN: no {hook} BoP repair')
    print('PASS: MKN native BoP ranges, decisions, four political paths, consent-based diplomacy and 22 idempotent repair scenarios')
