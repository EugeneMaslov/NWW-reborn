"""Behavioral checks for Ottoman council reform and staged Balkan campaigns.

This evaluates the actual generated triggers/effects with representative worlds.
It is a static regression check, not an in-game AI or UI reproduction.
"""
import argparse
import copy
import datetime
import itertools
import json
from pathlib import Path

from hoi4_script import one, read, values, walk

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--game', default='D:/Steam/steamapps/common/Hearts of Iron IV')
args = parser.parse_args()
GAME = Path(args.game)
errors = []
scenarios = 0


def check(ok, message):
    global scenarios
    scenarios += 1
    if not ok:
        errors.append(message)


tree = one(read(ROOT / 'common/national_focus/TUR_focuses.txt'), 'focus_tree')
focuses = {one(f, 'id'): f for f in values(tree, 'focus')}
effects = dict((k, v) for k, v, _ in read(ROOT / 'common/scripted_effects/TUR_effects.txt'))
triggers = dict((k, v) for k, v, _ in read(ROOT / 'common/scripted_triggers/TUR_triggers.txt'))
hooks = one(read(ROOT / 'common/on_actions/TUR_on_actions.txt'), 'on_actions')
campaigns = json.loads((ROOT / 'docs/TUR_balkan_objectives.json').read_text(encoding='utf-8'))
strategies = read(ROOT / 'common/ai_strategy/TUR_balkans.txt')
plans = read(ROOT / 'common/ai_strategy_plans/TUR_historical.txt') + read(ROOT / 'common/ai_strategy_plans/TUR_alternatives.txt')
accords = {'NWW_TUR_officer_accord', 'NWW_TUR_ulema_accord', 'NWW_TUR_provincial_accord'}
active = 'NWW_TUR_council_negotiation_active'
crisis_ideas = ['NWW_TUR_imperial_crisis', 'NWW_TUR_imperial_crisis_1', 'NWW_TUR_imperial_crisis_2', 'NWW_TUR_imperial_compact']
states = {}
for path in (ROOT / 'history/states').glob('*.txt'):
    state = one(read(path), 'state')
    if state is not None:
        sid = int(one(state, 'id'))
        hist = one(state, 'history', [])
        owner = one(hist, 'owner')
        states[sid] = {'owner': owner, 'controller': one(hist, 'controller', owner), 'id': sid}


def country(tag):
    return {'tag': tag, 'original_tag': tag, 'exists': True, 'subject': False, 'is_ai': True,
            'focus_tree': 'turkish_focus' if tag == 'TUR' else 'other_tree',
            'focuses': set(), 'flags': set(), 'ideas': set(), 'allies': set(),
            'wars': set(), 'goals': set(), 'can_declare': set(campaigns),
            'war_support': 0.50, 'stability': 0.50, 'political_power': 250,
            'popularity': {'neutrality': 0.45, 'fascism': 0.14, 'democratic': 0.25, 'communism': 0.16},
            'government': 'neutrality'}


def world():
    countries = {tag: country(tag) for tag in set(campaigns) | {'TUR', 'GER', 'ENG'}}
    return {'countries': countries, 'root': countries['TUR'], 'from': countries['GER'],
            'giver': countries['BUL'], 'states': copy.deepcopy(states),
            'date': (1938, 1, 1), 'historical': True, 'rules': {'TUR_ai_behavior': 'DEFAULT'}, 'trace': []}


def target(value, w):
    return {'ROOT': w['root']['tag'], 'FROM': w['from']['tag']}.get(value, value)


def compare(actual, op, value):
    wanted = float(value)
    return {'=': actual == wanted, '==': actual == wanted, '!=': actual != wanted,
            '>': actual > wanted, '<': actual < wanted, '>=': actual >= wanted, '<=': actual <= wanted}[op]


def condition(node, scope, w):
    answers = []
    for key, value, op in node:
        if key in ('tooltip', 'localization_key'):
            continue
        if key in ('AND', 'custom_trigger_tooltip'):
            answer = condition(value, scope, w)
        elif key in triggers:
            answer = condition(triggers[key], scope, w) == (value == 'yes')
        elif key == 'OR':
            answer = any(condition([entry], scope, w) for entry in value)
        elif key == 'NOT':
            answer = not condition(value, scope, w)
        elif key == 'ROOT':
            answer = condition(value, w['root'], w)
        elif key == 'FROM':
            answer = condition(value, w['from'], w)
        elif key == 'FROM.FROM':
            answer = condition(value, w['giver'], w)
        elif key in w['countries']:
            answer = condition(value, w['countries'][key], w)
        elif key and key.isdigit():
            answer = condition(value, w['states'][int(key)], w)
        elif key in ('tag', 'original_tag'):
            answer = scope[key] == target(value, w)
        elif key in ('exists', 'is_subject'):
            answer = scope['exists' if key == 'exists' else 'subject'] == (value == 'yes')
        elif key == 'is_ai':
            answer = scope['is_ai'] == (value == 'yes')
        elif key == 'has_focus_tree':
            answer = scope['focus_tree'] == value
        elif key == 'has_completed_focus':
            answer = value in scope['focuses']
        elif key == 'has_country_flag':
            answer = value in scope['flags']
        elif key == 'has_idea':
            answer = value in scope['ideas']
        elif key == 'has_government':
            answer = scope['government'] == value
        elif key == 'is_ally_with':
            answer = target(value, w) in scope['allies']
        elif key == 'has_war_with':
            answer = target(value, w) in scope['wars']
        elif key == 'has_wargoal_against':
            answer = target(value, w) in scope['goals']
        elif key == 'can_declare_war_on':
            answer = target(value, w) in scope['can_declare']
        elif key == 'is_owned_and_controlled_by':
            answer = scope['owner'] == target(value, w) and scope['controller'] == target(value, w)
        elif key == 'has_war_support':
            answer = compare(scope['war_support'], op, value)
        elif key == 'has_political_power':
            answer = compare(scope['political_power'], op, value)
        elif key in ('neutrality', 'fascism', 'communism', 'democratic'):
            answer = compare(scope['popularity'][key], op, value)
        elif key == 'date':
            wanted = tuple(int(part) for part in value.split('.'))
            answer = {'>': w['date'] > wanted, '<': w['date'] < wanted, '=': w['date'] == wanted}[op]
        elif key == 'is_historical_focus_on':
            answer = w['historical'] == (value == 'yes')
        elif key == 'has_game_rule':
            answer = w['rules'].get(one(value, 'rule')) == one(value, 'option')
        else:
            raise ValueError('Unsupported regression trigger: ' + str(key))
        answers.append(answer)
    return all(answers)


def execute(node, scope, w):
    """Execute the relevant country/state effects; record unrelated rewards."""
    branch_taken = False
    for key, value, _ in node:
        if key in ('if', 'else_if', 'else'):
            if key == 'if':
                branch_taken = False
            take = not branch_taken and (key == 'else' or condition(one(value, 'limit', []), scope, w))
            if take:
                execute([(k, v, op) for k, v, op in value if k != 'limit'], scope, w)
                branch_taken = True
        elif key in ('hidden_effect', 'effect'):
            execute(value, scope, w)
        elif key in effects:
            execute(effects[key], scope, w)
        elif key == 'random_list':
            # Exercise each finite outcome via random_branch; never assume a
            # particular random choice is guaranteed in the live game.
            execute(value[w.get('random_branch', 0)][1], scope, w)
        elif key in ('ROOT', 'FROM'):
            execute(value, w[key.lower()], w)
        elif key in w['countries']:
            execute(value, w['countries'][key], w)
        elif key and key.isdigit():
            execute(value, w['states'][int(key)], w)
        elif key == 'every_owned_state':
            for state in w['states'].values():
                if state['owner'] == scope['tag']:
                    execute(value, state, w)
        elif key in ('set_country_flag', 'clr_country_flag'):
            flag = one(value, 'flag') if isinstance(value, list) else value
            if key == 'set_country_flag':
                scope['flags'].add(flag)
            else:
                scope['flags'].discard(flag)
        elif key in ('add_ideas', 'remove_ideas'):
            items = [v for k, v, op in value] if isinstance(value, list) else [value]
            for idea in items:
                if key == 'add_ideas':
                    scope['ideas'].add(idea)
                else:
                    scope['ideas'].discard(idea)
        elif key == 'swap_ideas':
            scope['ideas'].discard(one(value, 'remove_idea'))
            scope['ideas'].add(one(value, 'add_idea'))
        elif key == 'set_politics':
            scope['government'] = one(value, 'ruling_party', scope['government'])
        elif key == 'create_wargoal':
            scope['goals'].add(target(one(value, 'target'), w))
            w['trace'].append((key, scope['tag'], target(one(value, 'target'), w)))
        elif key == 'annex_country':
            defeated = target(one(value, 'target'), w)
            w['countries'][defeated]['exists'] = False
            for state in w['states'].values():
                if state['owner'] == defeated:
                    state['owner'] = state['controller'] = scope['tag']
            w['trace'].append((key, scope['tag'], defeated))
        elif key in ('add_political_power', 'add_stability', 'add_war_support', 'army_experience'):
            field = {'add_political_power': 'political_power', 'add_stability': 'stability',
                     'add_war_support': 'war_support', 'army_experience': 'army_experience'}[key]
            scope[field] = scope.get(field, 0) + float(value)
        elif key == 'add_popularity':
            scope['popularity'][one(value, 'ideology')] += float(one(value, 'popularity'))
        else:
            w['trace'].append((key, scope.get('tag', scope.get('id')), value))


def can_focus(fid, w):
    focus = focuses[fid]
    completed = w['root']['focuses']
    for group in values(focus, 'prerequisite'):
        if not any(parent in completed for parent in values(group, 'focus')):
            return False
    exclusion = set(values(one(focus, 'mutually_exclusive', []), 'focus'))
    exclusion |= {other for other, node in focuses.items() if fid in values(one(node, 'mutually_exclusive', []), 'focus')}
    return not (exclusion & completed) and condition(one(focus, 'available', []), w['root'], w)


def claim_owned(w, tag):
    for state in w['states'].values():
        if state['owner'] == tag:
            state['owner'] = state['controller'] = 'TUR'
    w['countries'][tag]['exists'] = False


# Historical route is exercised using the actual prerequisite groups/exclusions.
historical = one(plans, 'NWW_TUR_historical')
order = [v for k, v, op in one(historical, 'ai_national_focuses')]
check(order[:2] == ['TUR_political_rw', 'TUR_not_fascism'], 'Historical AI does not first choose imperial neutrality')
w = world()
w['root']['flags'] |= accords
w['root']['ideas'] |= {'tur_silly_army_nowar', 'tur_agricultural_economic_1', crisis_ideas[0]}
for fid in order:
    check(fid in focuses, 'Historical plan references a missing or compatibility-only focus: ' + fid)
    if fid not in focuses:
        continue
    check(can_focus(fid, w), 'Historical route cannot reach ' + fid + ' with its preceding focuses')
    execute(one(focuses[fid], 'completion_reward', []), w['root'], w)
    w['root']['focuses'].add(fid)
    for tag, (war_focus, ids) in campaigns.items():
        if fid == war_focus:
            claim_owned(w, tag)
check(w['root']['government'] == 'neutrality', 'Historical route changes the Ottoman government away from neutrality')
check('NWW_TUR_balkan_mandate' in w['root']['focuses'], 'Historical plan never reaches the Balkan mandate')

# Preparation and all three negotiated accords are necessary, even when flags
# from unrelated systems are present. No mutual exclusion may bridge around them.
prepared = world()
prepared['root']['focuses'] |= {'TUR_proper_stoper'}
check(not can_focus('TUR_kosa_smerti', prepared), 'War ministry bypasses army reorganization')
prepared['root']['focuses'].add('TUR_Army_3')
check(can_focus('TUR_kosa_smerti', prepared), 'Modernized army cannot open war ministry')
for missing in [None] + sorted(accords):
    council = world()
    council['root']['flags'] |= accords - ({missing} if missing else set())
    council['root']['focuses'].add('tur_polos')
    check(can_focus('NWW_TUR_imperial_compact', council) == (missing is None), 'Council compact ignores missing accord: ' + str(missing))
council['root']['flags'] |= accords | {active}
check(not can_focus('NWW_TUR_imperial_compact', council), 'Compact can complete while council negotiation is active')

settlements = {'afg_bolgi': campaigns['BUL'][1], 'NWW_TUR_greek_settlement': campaigns['GRE'][1],
               'NWW_TUR_balkan_mandate': campaigns['BUL'][1] + campaigns['GRE'][1],
               'NWW_TUR_rumelian_governorates': campaigns['BUL'][1] + campaigns['GRE'][1]}
for fid, ids in settlements.items():
    full = world()
    for sid in ids:
        full['states'][sid]['owner'] = full['states'][sid]['controller'] = 'TUR'
    gate = one(focuses[fid], 'available', [])
    check(condition(gate, full['root'], full), fid + ': full ownership cannot settle province')
    for sid, field in itertools.product(ids, ('owner', 'controller')):
        bad = copy.deepcopy(full)
        bad['states'][sid][field] = 'GER'
        check(not condition(gate, bad['root'], bad), f'{fid}: ignores foreign {field} of state {sid}')
    check(one(focuses[fid], 'cancel_if_invalid') == 'yes', fid + ': can continue after losing required territory')
check(not any(k in ('add_state_core', 'add_core_of') for k, v, op in walk(tree)), 'TUR branch grants immediate Balkan cores')

cap_rules = values(one(one(hooks, 'on_capitulation'), 'effect'), 'if')
check(len(cap_rules) == 6, 'Expected six distinct Balkan capitulation hooks')
for tag, (fid, ids) in campaigns.items():
    starting = {sid for sid, st in states.items() if st['owner'] == tag}
    check(set(ids) == starting, tag + ': campaign omits starting country territory')
    helper_name = 'nww_TUR_prepare_' + tag.lower() + '_campaign'
    helper = effects[helper_name]
    goals = [v for k, v, op in walk(helper) if k == 'create_wargoal']
    check(len(goals) == 1 and one(goals[0], 'type') == 'annex_everything' and one(goals[0], 'target') == tag and not values(goals[0], 'expire'), tag + ': campaign goal is not permanent full annexation')
    check(not any(k == 'annex_country' for k, v, op in walk(helper)), tag + ': peacetime preparation annexes a country')
    for exists, subject, allied, war, goal in itertools.product((False, True), repeat=5):
        case = world()
        case['countries'][tag]['exists'] = exists
        case['root']['subject'] = subject
        case['root']['allies'] = {tag} if allied else set()
        case['root']['wars'] = {tag} if war else set()
        case['root']['goals'] = {tag} if goal else set()
        execute(helper, case['root'], case)
        generated = any(act[0] == 'create_wargoal' for act in case['trace'])
        check(generated == (exists and not subject and not allied and not war and not goal), f'{tag}: unsafe/duplicate campaign goal {exists, subject, allied, war, goal}')
    for hook in ('on_startup', 'on_daily_TUR'):
        for done in (False, True):
            old = world()
            if done:
                old['root']['focuses'].add(fid)
            execute(one(one(hooks, hook), 'effect'), old['root'], old)
            check((tag in old['root']['goals']) == done, f'{tag}: {hook} renewal ignores completed campaign focus')
            check(not any(act[0] == 'annex_country' for act in old['trace']), tag + ': old-save renewal annexes at peace')
    rule = next(node for node in cap_rules if one(one(node, 'limit'), 'tag') == tag)
    for defeated, victor, done, tree_ok, exists in itertools.product(tuple(campaigns) + ('GER',), ('TUR', 'GER'), (False, True), (False, True), (False, True)):
        cap = world()
        cap['root'] = cap['countries'][defeated]
        cap['root']['exists'] = exists
        cap['from'] = cap['countries'][victor]
        cap['from']['focus_tree'] = 'turkish_focus' if tree_ok else 'other_tree'
        if done:
            cap['from']['focuses'].add(fid)
        execute([('if', rule, '=')], cap['root'], cap)
        annexed = any(act[0] == 'annex_country' for act in cap['trace'])
        check(annexed == (defeated == tag and victor == 'TUR' and done and tree_ok and exists), f'{tag}: wrong-victor capitulation annexation {defeated, victor, done, tree_ok, exists}')
        if annexed:
            check(('annex_country', 'TUR', tag) in cap['trace'], tag + ': victor/defeated annex scope is reversed')
    ai = one(strategies, 'NWW_TUR_' + tag + '_campaign')
    check(one(ai, 'abort_when_not_enabled') == 'yes', tag + ': AI keeps stale declaration strategies')
    check({one(strategy, 'type') for strategy in values(ai, 'ai_strategy')} >= {'prepare_for_war', 'conquer', 'declare_war'}, tag + ': AI lacks declaration or preparation guidance')
    for done, allied, war, goal, legal in itertools.product((False, True), repeat=5):
        case = world()
        case['root']['focuses'] = {fid} if done else set()
        case['root']['allies'] = {tag} if allied else set()
        case['root']['wars'] = {tag} if war else set()
        case['root']['goals'] = {tag} if goal else set()
        case['root']['can_declare'] = {tag} if legal else set()
        check(condition(one(ai, 'enable'), case['root'], case) == (done and not allied and not war and goal and legal), f'{tag}: unsafe declaration eligibility {done, allied, war, goal, legal}')

# Sequential conquest must not advance merely because the war goal was awarded.
sequence = world()
sequence['root']['focuses'] |= {'TUR_war_with_bulgaria'}
check(not can_focus('afg_bolgi', sequence), 'Bulgaria settlement unlocks before actual conquest')
claim_owned(sequence, 'BUL')
check(can_focus('afg_bolgi', sequence), 'Full Bulgarian victory cannot advance')
sequence['root']['focuses'].add('afg_bolgi')
check(can_focus('TUR_snova_copi', sequence), 'Bulgarian settlement does not unlock Greek war goal')
sequence['root']['focuses'].add('TUR_snova_copi')
check(not can_focus('NWW_TUR_greek_settlement', sequence), 'Greek settlement unlocks before actual conquest')
claim_owned(sequence, 'GRE')
check(can_focus('NWW_TUR_greek_settlement', sequence), 'Full Greek victory cannot advance')
sequence['root']['focuses'].add('NWW_TUR_greek_settlement')
check(can_focus('NWW_TUR_balkan_mandate', sequence), 'Both settlements cannot unlock Balkan mandate')

# Crisis tiers change once, remain idempotent, and settlement cannot regress.
for accord_mask, settled in itertools.product(itertools.product((False, True), repeat=3), (False, True)):
    crisis = world()
    crisis['root']['flags'] = {flag for flag, present in zip(sorted(accords), accord_mask) if present}
    if settled:
        crisis['root']['flags'].add('NWW_TUR_council_settled')
    crisis['root']['ideas'] = {crisis_ideas[0]}
    expected = crisis_ideas[3 if settled else min(sum(accord_mask), 2)]
    execute(effects['nww_TUR_update_imperial_crisis'], crisis['root'], crisis)
    check(crisis['root']['ideas'] & set(crisis_ideas) == {expected}, 'Crisis tier disagrees with settled council/accord count')
    before = set(crisis['root']['ideas'])
    execute(effects['nww_TUR_update_imperial_crisis'], crisis['root'], crisis)
    check(crisis['root']['ideas'] == before, 'Repeating crisis maintenance duplicates or downgrades its spirit')
for helper, terminal in [('nww_legacy_TUR_army_step', 'tur_perfect_army_4'), ('nww_legacy_TUR_industry_step', 'tur_industry_economic_1')]:
    done = world()
    done['root']['ideas'] = {terminal, crisis_ideas[-1]}
    execute(effects[helper], done['root'], done)
    check(done['root']['ideas'] == {terminal, crisis_ideas[-1]}, 'Terminal modernization helper downgrades or resets other spirits')

decisions = read(ROOT / 'common/decisions/TUR_decisions.txt')
council_decisions = one(decisions, 'NWW_TUR_imperial_councils')
check(len(council_decisions) == 3, 'Council has other than three institutional negotiations')
for did, decision, _ in council_decisions:
    expected_flag = {'NWW_TUR_negotiate_officers': 'NWW_TUR_officer_accord', 'NWW_TUR_negotiate_ulema': 'NWW_TUR_ulema_accord', 'NWW_TUR_negotiate_provinces': 'NWW_TUR_provincial_accord'}[did]
    current = world()
    current['root']['flags'].add(active)
    check(not condition(one(decision, 'available'), current['root'], current), did + ': permits concurrent negotiation')
    execute(one(decision, 'remove_effect'), current['root'], current)
    check(expected_flag in current['root']['flags'] and active not in current['root']['flags'], did + ': successful negotiation does not settle institution')
    for tag, subject in [('TUR', True), ('GER', False)]:
        invalid = world()
        invalid['root'] = invalid['countries'][tag]
        invalid['root']['subject'] = subject
        invalid['root']['flags'].add(active)
        before = copy.deepcopy(invalid['root'])
        check(condition(one(decision, 'cancel_trigger'), invalid['root'], invalid), did + ': invalid negotiation is not canceled')
        execute(one(decision, 'remove_effect'), invalid['root'], invalid)
        check(expected_flag not in invalid['root']['flags'] and active not in invalid['root']['flags'], did + ': invalid removal grants accord or leaves lock')
        check(invalid['root']['political_power'] == before['political_power'] + float(one(decision, 'cost')), did + ': invalid removal does not refund cost')
        check(invalid['root']['stability'] == before['stability'] and invalid['root']['war_support'] == before['war_support'] and not invalid['root'].get('army_experience'), did + ': invalid removal grants successful negotiation buffs')
        canceled = copy.deepcopy(before)
        canceled_world = world()
        canceled_world['root'] = canceled
        execute(one(decision, 'cancel_effect'), canceled, canceled_world)
        check(expected_flag not in canceled['flags'] and active not in canceled['flags'] and canceled['political_power'] == before['political_power'] + float(one(decision, 'cost')), did + ': cancellation is not clean/refunded')

native_rules = one(read(GAME / 'common/game_rules/00_game_rules.txt'), 'TUR_ai_behavior')
options = {one(option, 'name') for option in values(native_rules, 'option')} | {'DEFAULT'}
for key, value, op in walk(decisions + plans + [(k, v, '=') for k, v in triggers.items()]):
    if key == 'has_game_rule':
        check(one(value, 'rule') == 'TUR_ai_behavior' and one(value, 'option') in options, 'TUR AI references unregistered game rule or option')
for option in options - {'RANDOM', 'DEFAULT'}:
    rule_world = world()
    rule_world['rules']['TUR_ai_behavior'] = option
    enabled = [name for name, plan, op in plans if condition(one(plan, 'allowed', []), rule_world['root'], rule_world) and condition(one(plan, 'enable', []), rule_world['root'], rule_world)]
    check(len(enabled) == 1, 'Explicit TUR AI option lacks a unique adapted plan: ' + option)

# Explicit rules override stale random flags; nonhistorical/default and RANDOM
# map every native assignment into exactly one real NWW plan. Without BFT, the
# fallback still chooses one path and remains stable on daily maintenance.
native_paths = {
    'TUR_AI_RANDOM_NEUTRALITY_HISTORICAL': 'NWW_TUR_historical',
    'TUR_AI_RANDOM_OTTOMAN': 'NWW_TUR_historical',
    'TUR_AI_RANDOM_ALT_KEMALIST': 'NWW_TUR_neutrality_alternative',
    'TUR_AI_RANDOM_BALKAN_ENTENTE': 'NWW_TUR_neutrality_alternative',
    'TUR_AI_RANDOM_DEMOCRATIC': 'NWW_TUR_democratic_alternative',
    'TUR_AI_RANDOM_DEMOCRATIC_ALTERNATE': 'NWW_TUR_democratic_alternative',
    'TUR_AI_RANDOM_COMMUNISM': 'NWW_TUR_communism_alternative',
    'TUR_AI_RANDOM_COMMUNISM_ALTERNATE': 'NWW_TUR_communism_alternative',
    'TUR_AI_RANDOM_FASCISM': 'NWW_TUR_fascism_alternative',
    'TUR_AI_RANDOM_FASCISM_ALTERNATE': 'NWW_TUR_fascism_alternative',
}


def enabled_plans(w):
    return {name for name, plan, op in plans if condition(one(plan, 'allowed', []), w['root'], w) and condition(one(plan, 'enable', []), w['root'], w)}


for flag, expected in native_paths.items():
    for rule in ('DEFAULT', 'RANDOM', None):
        selected = world()
        selected['historical'] = False
        selected['rules'] = {} if rule is None else {'TUR_ai_behavior': rule}
        selected['root']['flags'].add(flag)
        execute(effects['nww_TUR_select_ai_path'], selected['root'], selected)
        check(selected['root']['flags'] == {flag}, 'Native randomized selection is overwritten: ' + flag)
        check(enabled_plans(selected) == {expected}, 'Native randomized flag fails to select its adapted plan: ' + flag)
        selected['rules'] = {'TUR_ai_behavior': 'HISTORICAL'}
        check(enabled_plans(selected) == {'NWW_TUR_historical'}, 'Explicit historical rule does not override stale alternative flag: ' + flag)
for rule, historical_on, is_ai, branch in itertools.product(('DEFAULT', 'RANDOM', None), (False, True), (False, True), range(5)):
    fallback = world()
    fallback['rules'] = {} if rule is None else {'TUR_ai_behavior': rule}
    fallback['historical'] = historical_on
    fallback['root']['is_ai'] = is_ai
    fallback['random_branch'] = branch
    execute(effects['nww_TUR_select_ai_path'], fallback['root'], fallback)
    random_mode = rule == 'RANDOM' or not historical_on
    chosen = fallback['root']['flags'] & set(native_paths)
    check(len(chosen) == (1 if random_mode and is_ai else 0), 'Random fallback reroutes player or fails to pick one AI path')
    if chosen:
        before = set(fallback['root']['flags'])
        execute(effects['nww_TUR_select_ai_path'], fallback['root'], fallback)
        check(fallback['root']['flags'] == before, 'Daily random fallback changes an already selected path')
        check(enabled_plans(fallback) == {native_paths[next(iter(chosen))]}, 'Fallback selection has zero or competing AI plans')

# Every adapted alternative has reachable institutional follow-up after its
# required popularity has been earned through the matching timed campaign.
for name, plan, op in plans:
    if name == 'NWW_TUR_historical':
        continue
    alternative = world()
    alternative['root']['flags'] |= accords
    for ideology in alternative['root']['popularity']:
        alternative['root']['popularity'][ideology] = 0.45
    for fid in [v for k, v, op in one(plan, 'ai_national_focuses')]:
        check(fid in focuses and can_focus(fid, alternative), name + ': institutions/campaign cannot reach ' + fid)
        if fid not in focuses:
            continue
        execute(one(focuses[fid], 'completion_reward', []), alternative['root'], alternative)
        alternative['root']['focuses'].add(fid)
        for tag, (war_focus, ids) in campaigns.items():
            if fid == war_focus:
                claim_owned(alternative, tag)
for native_name in ('TUR_historical_strategy_plan.txt', 'TUR_alternate_strategy_plan.txt'):
    check(not read(ROOT / 'common/ai_strategy_plans' / native_name), 'Native TUR plan override still competes with adapted tree: ' + native_name)

kuwait = one(read(ROOT / 'history/states/656-Kuwait.txt'), 'state')
kh = one(kuwait, 'history')
check(one(kh, 'owner') == 'TUR' and one(kh, 'controller', 'TUR') == 'TUR', 'Kuwait is not initially Ottoman-owned and controlled')
check('KUW' in values(kh, 'add_core_of') and 'TUR' not in values(kh, 'add_core_of'), 'Kuwait loses local core or gains a free imperial core')
check(not any(k == 'transfer_state_to' and v != 'TUR' for k, v, op in walk(kh)), 'Kuwait is transferred away after history ownership')
eng = read(ROOT / 'history/countries/ENG - Britain.txt')
check(not any((k == 'puppet' and v == 'KUW') or (k == 'set_autonomy' and one(v, 'target') == 'KUW') for k, v, op in walk(eng)), 'British history still establishes a Kuwaiti puppet')
panel = int(one(one(tree, 'continuous_focus_position'), 'y'))
check(panel > max(int(one(focus, 'y')) for focus in focuses.values()) * 130 + 300, 'Continuous-focus panel overlaps extended TUR rows')

if errors:
    for error in errors:
        print('ERROR:', error)
    print(f'FAIL: {len(errors)} errors in {scenarios} Ottoman campaign/council scenarios')
    raise SystemExit(1)
print(f'PASS: {scenarios} Ottoman campaign/council scenarios; historical reachability, sequential controlled conquest, true-victor annexation, permanent goals and renewals, six declaration strategies, council cancellation and Kuwait setup')
