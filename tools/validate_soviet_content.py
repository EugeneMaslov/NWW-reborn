"""Validate NWW Soviet institutions, save repair, campaign dates and diplomacy."""
import copy
import itertools
import json
import re
from datetime import date, timedelta
from pathlib import Path
from hoi4_script import read, one, values, walk, parse, dump, engine_script_errors
import validate_country_content as base

ROOT, GAME = base.ROOT, base.GAME
errors = []
checks = 0


def check(ok, message):
    global checks
    checks += 1
    if not ok:
        errors.append(message)


report = json.loads((ROOT / 'docs/SOV_overhaul.json').read_text(encoding='utf-8'))
tree = one(read(ROOT / 'common/national_focus/SOV_focuses.txt'), 'focus_tree')
focuses = {one(f, 'id'): f for f in values(tree, 'focus')}
effects = {k: v for k, v, o in read(ROOT / 'common/scripted_effects/SOV_effects.txt')}
ideas = one(one(read(ROOT / 'common/ideas/SOV_ideas.txt'), 'ideas'), 'country')
events = values(read(ROOT / 'events/SOV_events.txt'), 'country_event')
known_modifiers = set(re.findall(r'^## (\w+)', (GAME / 'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig'), re.M))
known_effects = set(re.findall(r'^## (\w+)', (GAME / 'documentation/effects_documentation.md').read_text(encoding='utf-8-sig'), re.M))
known_triggers = set(re.findall(r'^## (\w+)', (GAME / 'documentation/triggers_documentation.md').read_text(encoding='utf-8-sig'), re.M))
check(len(focuses) == report['focus_count'] == 53, 'SOV focus count mismatch')
check(set(report['preserved_focus_ids']) <= focuses.keys(), 'An original NWW focus ID was lost')
check(one(one(one(tree, 'country'), 'modifier'), 'add') == '100', 'New tree does not outrank vanilla')
check(int(one(one(tree, 'continuous_focus_position'), 'y')) > max(int(one(f, 'y')) for f in focuses.values()) * 130 + 800, 'Continuous panel overlaps focuses')
check(not values(read(ROOT / 'common/national_focus/soviet.txt'), 'focus_tree'), 'Vanilla Soviet tree is still selectable')
for f in focuses.values():
    fid = one(f, 'id')
    for lang, entries in base.locales.items():
        check(fid in entries and fid + '_desc' in entries, f'{fid}: missing {lang} localization')
    check(one(f, 'icon') in base.sprites, f'{fid}: unknown focus icon {one(f, "icon")}')
    for group in values(f, 'prerequisite'):
        for parent in values(group, 'focus'):
            check(parent in focuses and int(one(focuses[parent], 'y')) < int(one(f, 'y')), f'{fid}: missing/crossing parent {parent}')
    for group in values(f, 'mutually_exclusive'):
        for other in values(group, 'focus'):
            check(any(fid in values(g, 'focus') for g in values(focuses[other], 'mutually_exclusive')), f'{fid}: one-way exclusion')
    for key, value, op in walk(one(f, 'completion_reward', [])):
        if key == 'add_tech_bonus':
            check(one(value, 'category') in base.categories and not one(value, 'category').endswith('_doctrine'), f'{fid}: unknown/obsolete category {one(value, "category")}')
        if key == 'add_research_slot':
            check(any(k == 'amount_research_slots' and v == '5' and op == '<' for k, v, op in walk(one(f, 'completion_reward'))), f'{fid}: uncapped slot')
        if key == 'random_owned_controlled_state':
            check(one(one(value, 'limit', []), 'is_core_of') == 'PREV', f'{fid}: wrong construction country scope')
            buildings = values(value, 'add_building_construction')
            for building in buildings:
                if one(building, 'type') in ('dockyard', 'arms_factory', 'industrial_complex'):
                    check(sum(int(s) for s in values(value, 'add_extra_state_shared_building_slots')) >= sum(int(one(b, 'level')) for b in buildings), f'{fid}: buildings without slots')
                if one(building, 'type') == 'dockyard':
                    check(one(one(value, 'limit'), 'is_coastal') == 'yes', f'{fid}: inland dockyard')
for y in {one(f, 'y') for f in focuses.values()}:
    xs = sorted(int(one(f, 'x')) for f in focuses.values() if one(f, 'y') == y)
    check(all(b - a >= 2 for a, b in zip(xs, xs[1:])), 'Crowded SOV row ' + y)
for token, node, op in ideas:
    check('GFX_idea_' + one(node, 'picture') in base.sprites, token + ': missing idea icon')
    for stat, value, op in one(node, 'modifier', []):
        check(stat in known_modifiers or stat.startswith('production_speed_'), token + ': unknown modifier ' + stat)
    for lang, entries in base.locales.items():
        check(token in entries and token + '_desc' in entries, token + ': missing spirit localization')
for key in ('has_country_leader', 'has_country_leader_with_trait', 'has_active_mission', 'has_dynamic_modifier', 'is_coastal'):
    check(key in known_triggers, 'Unknown engine trigger ' + key)
for key in ('remove_mission', 'remove_dynamic_modifier', 'add_claim_by', 'remove_country_leader_trait', 'add_country_leader_trait'):
    check(key in known_effects, 'Unknown engine effect ' + key)


def world():
    def country(tag):
        return {'tag': tag, 'focuses': set(), 'flags': set(), 'ideas': set(), 'allies': set(),
                'wars': set(), 'goals': set(), 'exists': True, 'subject': False,
                'government': 'communism', 'tree': 'SOV_focus' if tag == 'SOV' else 'other', 'war_support': 0.5}
    w = {tag: country(tag) for tag in ('SOV', 'MKN', 'LTB')}
    w['date'] = (1940, 6, 1)
    w['trace'] = []
    return w


def condition(node, scope, w):
    results = []
    for key, value, op in node:
        if key == 'tooltip':
            continue
        if key in ('AND', 'custom_trigger_tooltip'):
            result = condition(value, scope, w)
        elif key == 'OR':
            result = any(condition([entry], scope, w) for entry in value)
        elif key == 'NOT':
            result = not condition(value, scope, w)
        elif key in ('SOV', 'MKN', 'LTB'):
            result = condition(value, w[key], w)
        elif key == 'tag':
            result = scope['tag'] == value
        elif key == 'has_completed_focus':
            result = value in scope['focuses']
        elif key == 'has_country_flag':
            result = value in scope['flags']
        elif key == 'has_idea':
            result = value in scope['ideas']
        elif key == 'has_focus_tree':
            result = scope['tree'] == value
        elif key == 'has_government':
            result = scope['government'] == value
        elif key == 'is_subject':
            result = scope['subject'] == (value == 'yes')
        elif key == 'exists':
            result = scope['exists'] == (value == 'yes')
        elif key == 'is_ally_with':
            result = value in scope['allies']
        elif key == 'has_war_with':
            result = value in scope['wars']
        elif key == 'has_wargoal_against':
            result = value in scope['goals']
        elif key == 'has_war_support':
            result = scope['war_support'] > float(value)
        elif key == 'date':
            result = w['date'] > tuple(int(n) for n in value.split('.'))
        else:
            raise AssertionError('Unsupported test trigger: ' + str(key))
        results.append(result)
    return all(results)


def execute(node, scope, w):
    matched = False
    for key, value, op in node:
        if key == 'if':
            matched = condition(one(value, 'limit', []), scope, w)
            if matched:
                execute([(k, v, o) for k, v, o in value if k != 'limit'], scope, w)
        elif key == 'else_if':
            if not matched and condition(one(value, 'limit', []), scope, w):
                matched = True
                execute([(k, v, o) for k, v, o in value if k != 'limit'], scope, w)
        elif key == 'else':
            if not matched:
                execute(value, scope, w)
        elif key in effects:
            execute(effects[key], scope, w)
        elif key == 'add_ideas':
            scope['ideas'].add(value)
        elif key == 'remove_ideas':
            scope['ideas'].discard(value)
        elif key == 'set_country_flag':
            scope['flags'].add(value)
        elif key == 'clr_country_flag':
            scope['flags'].discard(value)
        elif key in ('SOV', 'LTB', 'MKN'):
            execute(value, w[key], w)
        elif key == 'create_wargoal':
            scope['goals'].add(one(value, 'target'))
            w['trace'].append(('goal', one(value, 'target')))
        elif key == 'every_owned_state':
            w['trace'].append(('claims', scope['tag']))
        elif key in ('add_stability', 'add_political_power', 'add_manpower', 'army_experience', 'air_experience', 'navy_experience', 'add_building_construction'):
            w['trace'].append((key, value))
        else:
            raise AssertionError('Unsupported test effect: ' + str(key))


# All combinations and repeated save repairs preserve the exact intended stage.
milestones = [fid for area in report['stage_milestones'].values() for fid in area]
for flags in itertools.product((False, True), repeat=len(milestones)):
    w = world()
    completed = {fid for fid, done in zip(milestones, flags) if done}
    w['SOV']['focuses'] = completed
    w['SOV']['ideas'] = {f'NWW_SOV_{area}_0' for area in report['stage_milestones']}
    execute(effects['nww_SOV_update_reconstruction'], w['SOV'], w)
    expected = {f'NWW_SOV_{area}_{len(completed & set(fids))}' for area, fids in report['stage_milestones'].items()}
    check(w['SOV']['ideas'] == expected, 'Reconstruction combination failed: ' + str(completed))
    execute(effects['nww_SOV_update_reconstruction'], w['SOV'], w)
    check(w['SOV']['ideas'] == expected and not w['trace'], 'Save repair duplicated a reward or spirit')
for area, fids in report['stage_milestones'].items():
    for fid in fids:
        w = world()
        w['SOV']['flags'].add(fid + '_reform_done')
        execute(effects['nww_SOV_update_reconstruction'], w['SOV'], w)
        check(f'NWW_SOV_{area}_1' in w['SOV']['ideas'], 'Completion callback does not advance immediately: ' + fid)

# Ally, treaty, autonomy, date and genuine refusal all restrict war-goal replay.
for target, helper, flag in [('LTB', 'litbel', 'NWW_SOV_LTB_rejected'), ('MKN', 'steppe', 'NWW_SOV_MKN_rejected')]:
    for early, ally, settled, refused, subject, missing, prepared in itertools.product((False, True), repeat=7):
        w = world()
        s = w['SOV']
        w['date'] = (1939, 1, 1) if early else (1940, 6, 1)
        s['allies'] = {target} if ally else set()
        s['subject'] = subject
        w[target]['exists'] = not missing
        if settled:
            s['flags'].add('NWW_SOV_' + target + '_settlement')
        if refused:
            s['flags'].add(flag)
        if prepared:
            s['focuses'].update(['NWW_SOV_civil_peace', 'NWW_SOV_army_maneuvers'])
        execute(effects['nww_SOV_prepare_' + helper + '_campaign'], s, w)
        expected = not (early or ally or settled or subject or missing) and refused and prepared
        check((target in s['goals']) == expected, 'Campaign guard failed: ' + str((target, early, ally, settled, refused, subject, missing, prepared)))
        before = len([entry for entry in w['trace'] if entry[0] == 'goal'])
        execute(effects['nww_SOV_prepare_' + helper + '_campaign'], s, w)
        check(len([entry for entry in w['trace'] if entry[0] == 'goal']) == before, 'Campaign repair duplicates a war goal')
    w = world()
    w['SOV']['flags'].add(flag)
    w['SOV']['focuses'].update(['NWW_SOV_civil_peace', 'NWW_SOV_army_maneuvers'])
    w['SOV']['wars'].add(target)
    execute(effects['nww_SOV_prepare_' + helper + '_campaign'], w['SOV'], w)
    check(not w['SOV']['goals'], 'An ongoing war created a second goal')
w = world()
w['SOV']['flags'].add('NWW_SOV_MKN_rejected')
w['SOV']['focuses'].update(['NWW_SOV_civil_peace', 'NWW_SOV_army_maneuvers'])
w['MKN']['flags'].add('MKN_equal_autonomy')
execute(effects['nww_SOV_prepare_steppe_campaign'], w['SOV'], w)
check(not w['SOV']['goals'], 'Soviet campaign betrays the accepted MKN charter')

cleanup = effects['nww_SOV_suspend_detached_purges']
check(set(report['native_spirits']) <= {v for k, v, o in walk(cleanup) if k == 'remove_ideas'}, 'Native spirit cleanup incomplete')
check(set(report['native_dynamic_modifiers']) <= {one(v, 'modifier') for k, v, o in walk(cleanup) if k == 'remove_dynamic_modifier' and isinstance(v, list)}, 'Native dynamic modifier cleanup incomplete')
check({v for k, v, o in walk(cleanup) if k == 'remove_unit_leader_trait'} == {'trait_SOV_cowed_by_stalin_army', 'trait_SOV_cowed_by_stalin_navy'}, 'Old-save purge scars remain on commanders, or unrelated traits are removed')
for helper in ('nww_SOV_prepare_litbel_campaign', 'nww_SOV_prepare_steppe_campaign'):
    check({v for k, v, o in walk(effects[helper]) if k == 'add_claim_by'} == {'SOV'}, 'Claims depend on ambiguous global startup ROOT scope')
check(not any(k in ('annex_country', 'transfer_state_to', 'add_political_power', 'add_stability', 'add_manpower', 'add_building_construction', 'complete_national_focus') for k, v, o in walk(cleanup)), 'Cleanup steals land or repeats a reward')
history = read(ROOT / 'history/countries/SOV - Soviet union.txt')
check(not any(k == 'add_dynamic_modifier' and one(v, 'modifier', '').startswith('SOV_') for k, v, o in walk(history)), 'History still starts a native modifier')
check(not any(k == 'country_event' and one(v, 'id', '').startswith('NSB_') for k, v, o in walk(history)), 'History still schedules native purges')
check(not any(k == 'complete_national_focus' for k, v, o in walk(history)), 'History still force-completes vanilla focuses')
check(one(history, 'nww_SOV_update_reconstruction') == 'yes', 'New campaign lacks its three starting spirits')
for relative in ['common/decisions/SOV.txt', 'common/decisions/categories/SOV_decision_categories.txt', 'common/scripted_guis/SOV_paranoia_system_scripted_gui.txt', 'common/scripted_guis/SOV_propaganda_campaigns_scripted_gui.txt']:
    check(not read(ROOT / relative), 'Detached Soviet subsystem still active: ' + relative)
for relative in ['events/NSB_Soviet.txt', 'events/SovietUnion.txt', 'events/WTT_Soviet.txt']:
    for kind, event, op in read(ROOT / relative):
        if kind in ('country_event', 'news_event'):
            check(any(one(one(gate, 'AND', []), 'has_focus_tree') == 'SOV_focus' for gate in values(one(event, 'trigger'), 'NOT')), 'Native event not guarded: ' + one(event, 'id'))
for eid, tag in [('nww_sov.10', 'LTB'), ('nww_sov.20', 'MKN')]:
    event = next(e for e in events if one(e, 'id') == eid)
    accepted, rejected = values(event, 'option')
    check(any(k == 'set_country_flag' and v == 'NWW_SOV_' + tag + '_settlement' for k, v, o in walk(accepted)), 'Accepted treaty not recorded')
    check(any(k == 'set_country_flag' and v == 'NWW_SOV_' + tag + '_rejected' for k, v, o in walk(rejected)), 'Refusal not recorded')
    check(not any(k in ('annex_country', 'puppet', 'set_autonomy', 'set_politics', 'transfer_state_to', 'declare_war_on') for k, v, o in walk(event)), 'Diplomatic choice silently annexes, puppets or changes a government')
    check(one(accepted, 'trigger') == one(event, 'trigger'), 'Diplomatic consent lacks a live participant guard')
    for option in (accepted, rejected):
        check(one(one(option, 'if'), 'limit') == one(event, 'trigger'), 'Reply can alter a vanished, conquered or warring participant')
registered = {k: v for k, v, o in one(read(ROOT / 'common/decisions/SOV_compatibility.txt'), 'NWW_SOV_disabled_subsystems')}
check(set(report['inactive_native_missions']) <= registered.keys(), 'Cleanup references an unregistered native mission')
for token, decision in registered.items():
    check(one(one(decision, 'allowed'), 'always') == 'no' and one(one(decision, 'visible'), 'always') == 'no', 'Native decision is playable: ' + token)

plan = read(ROOT / 'common/ai_strategy_plans/SOV_historical.txt')[0][1]
order = [v for k, v, o in one(plan, 'ai_national_focuses')]
completed = set()
for fid in order:
    check(fid in focuses, 'Historical AI references a missing focus ' + fid)
    for group in values(focuses[fid], 'prerequisite'):
        check(bool(set(values(group, 'focus')) & completed), 'Historical order precedes prerequisites for ' + fid)
    completed.add(fid)
war_date = date.fromisoformat(report['uninterrupted_historical_war_goal_date'])
check(date(1939, 1, 1) <= war_date <= date(1940, 12, 31), 'Historical route misses the 1939–1940 campaign window')
duration = sum(int(one(focuses[f], 'cost')) * 7 for f in order[:order.index('NWW_SOV_litbel_campaign') + 1])
check(date(1936, 1, 1) + timedelta(days=duration) == war_date, 'Historical date does not match actual focus costs')
# The shared parser must preserve unnamed equipment-asset blocks.
sample = parse('optional_assets = { { icon = GFX_ship model = SOV_ship_entity } }')
check(parse(dump(sample)) == sample, 'Anonymous equipment asset blocks were lost')
for relative in report['files']:
    if relative.endswith('.txt'):
        doc = read(ROOT / relative)
        check(not list(engine_script_errors(doc)), 'Engine syntax errors in ' + relative + ': ' + '; '.join(engine_script_errors(doc)))
        check(not any(k == 'remove_dynamic_modifier' and not isinstance(v, list) for k, v, o in walk(doc)), 'Legacy scalar dynamic-modifier removal in ' + relative)

if errors:
    for error in errors:
        print('ERROR:', error)
    raise SystemExit(1)
print(f'PASS: {checks} Soviet checks; 53 focuses, 14 preserved IDs, staged recovery, repeat-safe save repair, native purge isolation, consent/refusal, protected MKN autonomy and 1939–1940 campaign timing')
