"""MKN/UKR frontier references and source-script lifecycle regressions.

The interpreter executes the actual effects for country/state ownership, flags,
variables and diplomatic outcomes. It cannot reproduce combat or the game UI.
Unsupported commands in an executed branch fail instead of being ignored.
"""
from copy import deepcopy
from itertools import product
import re

from PIL import Image

from hoi4_script import read, one, values, walk, variable_check, engine_script_errors


class FrontierModel:
    def __init__(self, effects, triggers):
        self.effects, self.triggers = effects, triggers
        self.day = 0
        self.root = 'MKN'
        self.froms = ('196', 'UKR', '197')
        self.border = False
        self.border_states = {'196', '197'}
        self.events, self.declarations, self.relations = [], [], []
        self.cancellations = []
        self.countries = {
            tag: {'flags': {}, 'variables': {}, 'ideas': set(), 'focuses': set(),
                  'wars': set(), 'allies': set(), 'pacts': set(), 'missions': set(),
                  'exists': True, 'subject': False, 'equipment': 1000,
                  'stability': 0.5, 'war_support': 0.5}
            for tag in ('MKN', 'UKR', 'SOV', 'LTB')
        }
        self.states = {
            sid: {'owner': owner, 'controller': owner, 'cores': {owner},
                  'flags': {}, 'damage': 0}
            for sid, owner in (('196', 'MKN'), ('197', 'UKR'), ('203', 'UKR'), ('500', 'MKN'))
        }
        # An unrelated occupied state must never become an automatic frontier core.
        self.states['500']['cores'] = {'LTB'}
        for sid, state in self.states.items():
            state['neighbors'] = {'196': ('197', '203'), '197': ('196',), '203': ('196',), '500': ()}[sid]

    def scope(self, name, current, previous):
        if name in self.countries or name in self.states:
            return name
        if name == 'ROOT':
            return self.root
        if name == 'PREV':
            return previous
        if name.startswith('FROM') and all(p == 'FROM' for p in name.split('.')):
            index = len(name.split('.')) - 1
            return self.froms[index] if index < len(self.froms) else None
        return None

    def data(self, scope):
        return self.countries[scope] if scope in self.countries else self.states[scope]

    def flag(self, scope, token):
        expiry = self.data(scope)['flags'].get(token)
        return expiry is not None and (expiry == -1 or self.day < expiry)

    def number(self, token, current, previous):
        resolved = self.scope(token, current, previous)
        if resolved is not None:
            return resolved
        try:
            return float(token)
        except ValueError:
            return self.data(current)['variables'].get(token, 0)

    @staticmethod
    def compare(left, right, operator):
        return {'=': lambda: left == right, '==': lambda: left == right,
                '>': lambda: left > right, '>=': lambda: left >= right,
                '<': lambda: left < right, '<=': lambda: left <= right,
                '!=': lambda: left != right}[operator]()

    def test(self, nodes, current='MKN', previous=None):
        answers = []
        for key, value, operator in nodes or []:
            data = self.data(current)
            scoped = self.scope(key, current, previous)
            if key == 'NOT':
                answer = not self.test(value, current, previous)
            elif key == 'OR':
                answer = any(self.test([item], current, previous) for item in value)
            elif key == 'AND':
                answer = self.test(value, current, previous)
            elif scoped is not None:
                answer = self.test(value, scoped, current)
            elif key in self.triggers:
                answer = self.test(self.triggers[key], current, previous) == (value == 'yes')
            elif key == 'custom_trigger_tooltip':
                answer = self.test([item for item in value if item[0] != 'tooltip'], current, previous)
            elif key == 'always':
                answer = value == 'yes'
            elif key == 'tag':
                answer = current == value
            elif key == 'state':
                answer = current == value
            elif key == 'exists':
                answer = data['exists'] == (value == 'yes')
            elif key == 'is_subject':
                answer = data['subject'] == (value == 'yes')
            elif key in ('has_country_flag', 'has_state_flag'):
                answer = self.flag(current, value)
            elif key == 'has_completed_focus':
                answer = value in data['focuses']
            elif key == 'has_variable':
                answer = value in data['variables']
            elif key == 'has_idea':
                answer = value in data['ideas']
            elif key == 'has_war':
                answer = bool(data['wars']) == (value == 'yes')
            elif key == 'has_war_with':
                answer = value in data['wars']
            elif key == 'has_border_war_with':
                answer = self.border and value == 'UKR'
            elif key == 'has_border_war':
                participating = self.border and (current in self.countries or current in self.border_states)
                answer = participating == (value == 'yes')
            elif key == 'is_ally_with':
                answer = value in data['allies']
            elif key == 'has_non_aggression_pact_with':
                answer = value in data['pacts']
            elif key == 'is_owned_by':
                answer = data['owner'] == value
            elif key == 'is_controlled_by':
                answer = data['controller'] == (self.scope(value, current, previous) or value)
            elif key == 'is_owned_and_controlled_by':
                answer = data['owner'] == value and data['controller'] == value
            elif key == 'check_variable':
                var, operand, comparator = variable_check(value)
                left = sum(s['owner'] == current for s in self.states.values()) if var == 'num_owned_states' else data['variables'].get(var, 0)
                answer = self.compare(left, self.number(operand, current, previous), comparator)
            elif key == 'has_equipment':
                answer = all(self.compare(data['equipment'], float(v), op) for k, v, op in value)
            elif key == 'any_neighbor_state':
                answer = any(self.test(value, sid, current) for sid in data['neighbors'])
            else:
                raise AssertionError(f'Unhandled frontier regression trigger {key}')
            answers.append(answer)
        return all(answers)

    def apply(self, nodes, current='MKN', previous=None):
        matched = False
        for key, value, operator in nodes or []:
            data = self.data(current)
            scoped = self.scope(key, current, previous)
            if key in ('if', 'else_if'):
                if key == 'if':
                    matched = False
                if not matched and self.test(one(value, 'limit'), current, previous):
                    self.apply([item for item in value if item[0] != 'limit'], current, previous)
                    matched = True
            elif key == 'else':
                if not matched:
                    self.apply(value, current, previous)
                matched = True
            elif key in self.effects:
                self.apply(self.effects[key], current, previous)
            elif scoped is not None:
                self.apply(value, scoped, current)
            elif key in ('set_variable', 'add_to_variable', 'subtract_from_variable', 'multiply_variable'):
                for name, token, op in value:
                    number = self.number(token, current, previous)
                    old = data['variables'].get(name, 0)
                    data['variables'][name] = {'set_variable': lambda: number,
                        'add_to_variable': lambda: old + number,
                        'subtract_from_variable': lambda: old - number,
                        'multiply_variable': lambda: old * number}[key]()
            elif key == 'clamp_variable':
                name = one(value, 'var')
                data['variables'][name] = min(float(one(value, 'max')), max(float(one(value, 'min')), data['variables'].get(name, 0)))
            elif key in ('set_country_flag', 'set_state_flag'):
                name = one(value, 'flag') if isinstance(value, list) else value
                days = one(value, 'days') if isinstance(value, list) else None
                data['flags'][name] = self.day + int(days) if days else -1
            elif key in ('clr_country_flag', 'clr_state_flag'):
                data['flags'].pop(value, None)
            elif key == 'add_core_of':
                data['cores'].add(value)
            elif key == 'transfer_state_to':
                data['owner'] = data['controller'] = self.scope(value, current, previous) or value
            elif key == 'every_owned_state':
                for sid, state in self.states.items():
                    if state['owner'] == current and self.test(one(value, 'limit'), sid, current):
                        self.apply([item for item in value if item[0] != 'limit'], sid, current)
            elif key == 'every_neighbor_state':
                for sid in data['neighbors']:
                    if self.test(one(value, 'limit'), sid, current):
                        self.apply([item for item in value if item[0] != 'limit'], sid, current)
            elif key == 'add_war_support':
                data['war_support'] += float(value)
            elif key == 'add_stability':
                data['stability'] += float(value)
            elif key == 'country_event':
                self.events.append((current, one(value, 'id'), int(one(value, 'days', 0))))
            elif key == 'diplomatic_relation':
                target = one(value, 'country')
                active = one(value, 'active', 'yes') == 'yes'
                assert one(value, 'relation') == 'non_aggression_pact'
                self.relations.append((current, target, active))
                for owner, partner in ((current, target), (target, current)):
                    if active:
                        self.countries[owner]['pacts'].add(partner)
                    else:
                        self.countries[owner]['pacts'].discard(partner)
            elif key == 'declare_war_on':
                target = one(value, 'target')
                self.declarations.append((current, target))
                data['wars'].add(target)
                self.countries[target]['wars'].add(current)
            elif key in ('add_ideas', 'remove_ideas'):
                tokens = [v for k, v, op in value] if isinstance(value, list) else [value]
                for token in tokens:
                    if key == 'add_ideas':
                        data['ideas'].add(token)
                    else:
                        data['ideas'].discard(token)
            elif key == 'add_timed_idea':
                data['ideas'].add(one(value, 'idea'))
            elif key in ('activate_mission', 'remove_mission'):
                if key == 'activate_mission':
                    data['missions'].add(value)
                else:
                    data['missions'].discard(value)
            elif key == 'add_equipment_to_stockpile':
                data['equipment'] += float(one(value, 'amount'))
            elif key == 'damage_building':
                data['damage'] += float(one(value, 'damage'))
            elif key == 'cancel_border_war':
                attacker = one(value, 'attacker')
                defender = one(value, 'defender')
                if attacker.startswith('var:'):
                    attacker = data['variables'].get(attacker[4:], 0)
                if defender.startswith('var:'):
                    defender = data['variables'].get(defender[4:], 0)
                self.cancellations.append((attacker, defender, one(value, 'dont_fire_events')))
                self.border = False
            elif key == 'custom_effect_tooltip':
                pass  # Presentation only; it cannot alter modeled game state.
            elif key == 'complete_national_focus':
                data['focuses'].add(value)
            else:
                raise AssertionError(f'Unhandled frontier regression effect {key}')

    def run(self, token):
        self.apply(self.effects[token])


def validate_frontier(root, game, check, localized):
    files = {
        'effects': 'common/scripted_effects/MKN_ukr_border_effects.txt',
        'triggers': 'common/scripted_triggers/MKN_ukr_border_triggers.txt',
        'events': 'events/MKN_ukr_border_events.txt',
        'decisions': 'common/decisions/MKN_ukr_border_decisions.txt',
        'focuses': 'common/national_focus/MKN_frontier_focuses.txt',
        'ideas': 'common/ideas/MKN_ukr_border_ideas.txt',
        'on_actions': 'common/on_actions/MKN_ukr_border_on_actions.txt',
    }
    parsed = {name: read(root / filename) for name, filename in files.items()}
    for filename in files.values():
        for error in engine_script_errors(read(root / filename)):
            check(False, f'{filename}: {error}')
    effects = {k: v for k, v, op in parsed['effects']}
    triggers = {k: v for k, v, op in parsed['triggers']}
    events = {one(e, 'id'): e for e in values(parsed['events'], 'country_event')}
    decisions = one(parsed['decisions'], 'MKN_ukr_border_category')
    focuses = {one(f, 'id'): f for f in values(parsed['focuses'], 'shared_focus')}
    ideas = one(one(parsed['ideas'], 'ideas'), 'country')
    mission_id = 'MKN_frontier_year_countdown_mission'
    native = {kind: set(re.findall(r'^## (\w+)', (game / f'documentation/{kind}_documentation.md').read_text(), re.M))
              for kind in ('effects', 'triggers', 'modifiers')}
    for token in ('has_border_war_with', 'has_equipment', 'has_country_flag', 'is_owned_and_controlled_by', 'is_owned_by', 'has_non_aggression_pact_with'):
        check(token in native['triggers'], f'MKN frontier: undocumented native trigger {token}')

    # Verify actual engine commands, avoiding unsupported inline callbacks/stat inventions.
    for filename in files.values():
        for key, value, op in walk(read(root / filename)):
            if key and re.match(r'^(add_|set_|clr_|remove_|create_|start_|activate_|damage_|declare_|clamp_|subtract_|multiply_)', key):
                check(key in native['effects'] or key in ('add_namespace', 'remove_effect'), f'{filename}: undocumented command {key}')
            if key == 'add_core_of':
                check(value != 'UKR', f'{filename}: grants a new UKR core')
            if key == 'custom_effect_tooltip':
                localized(value, 'MKN frontier tooltip')
            if key == 'custom_trigger_tooltip':
                localized(one(value, 'tooltip'), 'MKN frontier availability')
    for token, idea, op in ideas:
        localized(token, 'MKN frontier spirit')
        localized(token + '_desc', 'MKN frontier spirit')
        for modifier, value, op in one(idea, 'modifier'):
            check(modifier in native['modifiers'], f'{token}: undocumented modifier {modifier}')
    check(one(one(one(ideas, 'MKN_war_for_the_steppe'), 'modifier'), 'army_core_attack_factor') == '0.10', 'MKN frontier: permanent war spirit lacks +10% core attack')
    for token, decision, op in decisions:
        localized(token, 'MKN frontier decision')
        localized(token + '_desc', 'MKN frontier decision')
    for token in ('mkn_raid_soviet_depots', 'mkn_launch_border_battle'):
        target = one(one(decisions, token), 'target_trigger')
        entered = one(target,'FROM',[])
        check(one(entered,'MKN_valid_frontier_target') == 'yes' if token == 'mkn_launch_border_battle' else one(entered,'is_owned_and_controlled_by') == 'UKR', f'{token}: country-scope target_trigger does not enter the target state through FROM')
    fury = one(one(decisions, 'mkn_escalate_steppe_alarm'), 'complete_effect')
    pullback = one(decisions, 'mkn_deescalate_pull_back')
    relaxation = one(one(pullback, 'remove_effect'), 'if')
    check(one(pullback,'days_remove') == '20' and one(pullback,'days_re_enable') == '0', 'MKN frontier: pullback is not a repeatable 20-day action')
    check(not one(pullback,'complete_effect'), 'MKN frontier: pullback reduces tension before its 20 days expire')
    check(one(one(fury, 'add_timed_idea'), 'days') == '14', 'MKN frontier: fury has wrong duration')
    check(one(one(relaxation, 'add_timed_idea'), 'days') == '90', 'MKN frontier: relaxation has wrong duration')
    for event in events.values():
        if one(event, 'hidden') == 'yes':
            continue
        localized(one(event, 'title'), 'MKN frontier event')
        for description in values(event, 'desc'):
            localized(one(description, 'text') if isinstance(description, list) else description, 'MKN frontier event')
        for option in values(event, 'option'):
            localized(one(option, 'name'), 'MKN frontier event choice')
    for fid, focus in focuses.items():
        localized(fid, 'MKN frontier focus')
        localized(fid + '_desc', 'MKN frontier focus')
        if fid not in ('MKN_conclude_total_war', 'MKN_conclude_kharkiv_treaty'):
            check(one(one(focus, 'cancel'), 'has_country_flag') == 'mkn_ukr_frontier_concluded', f'{fid}: peace does not cancel unfinished preparations')
    check(len(focuses) == 8, 'MKN frontier: expected eight shared focuses')
    disruption = one(read(root / 'common/dynamic_modifiers/MKN_ukr_border_modifiers.txt'), 'MKN_ukr_miners_state_disruption')
    check(one(disruption, 'local_factories') == '-0.10' and 'local_factories' in native['modifiers'], 'MKN frontier: miners lack a valid state factory-capacity penalty')
    check(one(disruption, 'industrial_capacity_factory') is None, 'MKN frontier: miners apply a country-only factory-output modifier to a state')
    for filename in ('interface/MKN_frontier_gui.gfx', 'interface/MKN_frontier_focus_icons.gfx'):
        sprites = [v for k, v, op in walk(read(root / filename)) if k and k.lower() == 'spritetype']
        for sprite in sprites:
            texture = root / one(sprite, 'texturefile')
            check(texture.is_file(), f'{filename}: missing texture {texture.name}')
            if texture.is_file():
                with Image.open(texture) as image:
                    image.load()
                    check(image.format == 'DDS' and image.width > 0 and image.height > 0, f'{filename}: invalid DDS {texture.name}')
        if filename.endswith('focus_icons.gfx'):
            names = {one(sprite, 'name') for sprite in sprites}
            check(all(one(focus, 'icon') in names and one(focus, 'icon') + '_shine' in names for focus in focuses.values()), 'MKN frontier: generated focus icon/shine registration is incomplete')
    category = one(read(root / 'common/decisions/categories/MKN_ukr_border_categories.txt'), 'MKN_ukr_border_category')
    gui = one(one(read(root / 'common/scripted_guis/MKN_frontier_gui.txt'), 'scripted_gui'), 'MKN_frontier_decision_ui')
    check(one(category, 'scripted_gui') == 'MKN_frontier_decision_ui' and one(gui, 'context_type') == 'decision_category', 'MKN frontier: display is not embedded in its decision category')
    for node in (one(category, 'visible'), one(gui, 'visible')):
        check(not any(k == 'has_country_flag' and v in ('mkn_ukr_frontier_concluded', 'mkn_frontier_frozen') for k, v, op in walk(node)), 'MKN frontier: settled/war/frozen status removes the permanently visible display')
    for level in range(1, 6):
        localized(f'MKN_frontier_stage_{level}', 'MKN frontier display')
        marker = one(one(gui, 'triggers'), f'MKN_frontier_marker_{level}_visible')
        check(one(one(marker, 'check_variable'), 'mkn_ukr_escalation_level') == str(level), f'MKN frontier: marker {level} has an invalid variable threshold')
    tree = one(read(root / 'common/national_focus/MKN.txt'), 'focus_tree')
    imports = set(values(tree, 'shared_focus'))
    check({'MKN_ukrainian_frontier_root', 'MKN_conclude_total_war', 'MKN_conclude_kharkiv_treaty'} <= imports, 'MKN frontier: disconnected shared roots are not imported')
    root_gate = one(focuses['MKN_ukrainian_frontier_root'], 'available')
    check(one(root_gate, 'always') == 'no', 'MKN frontier: incident root must be event-completed')
    for a, b in (('MKN_conclude_total_war', 'MKN_conclude_kharkiv_treaty'), ('MKN_conclude_kharkiv_treaty', 'MKN_conclude_total_war')):
        check(one(one(focuses[a], 'mutually_exclusive'), 'focus') == b, f'{a}: endings are not exclusive')

    battles = [v for k, v, op in walk(one(one(decisions, 'mkn_launch_border_battle'), 'complete_effect')) if k == 'start_border_war']
    check(len(battles) == 2, 'MKN frontier: missing normal/first-shot battle variants')
    for battle in battles:
        check(one(battle, 'change_state_after_war') == 'no', 'MKN frontier: native auto-transfer bypasses exact callback integration')
        attacker = one(battle, 'attacker')
        for token, expected in (('on_win', 'mkn_ukr_border.20'), ('on_lose', 'mkn_ukr_border.21'), ('on_cancel', 'mkn_ukr_border.23')):
            check(one(attacker, token) == expected, f'MKN frontier: wrong native {token} callback')
        for side in ('attacker', 'defender'):
            check(all(isinstance(one(one(battle, side), token), str) for token in ('on_win', 'on_lose', 'on_cancel')), 'MKN frontier: inline native callback block is unsupported')
    for suffix, helper in ((20, 'mkn_ukr_border_victory'), (21, 'mkn_ukr_border_defeat'), (23, 'mkn_ukr_border_cancelled')):
        event = events[f'mkn_ukr_border.{suffix}']
        check(one(event, 'hidden') == 'yes' and one(one(event, 'immediate'), helper) == 'yes', f'MKN frontier: callback {suffix} waits for an event choice')
    integration = effects['mkn_ukr_integrate_won_state']
    check(one(integration, 'add_core_of') == 'MKN' and one(integration, 'transfer_state_to') == 'MKN', 'MKN frontier: won state lacks immediate core and ownership/controller transfer')
    legacy = {one(e, 'id'): e for e in values(read(root / 'events/nww_mkn.txt'), 'country_event')}
    check(one(one(legacy['mkn.5'], 'immediate'), 'mkn_ukr_border_victory') == 'yes', 'MKN frontier: old-save victory bypasses exact callback integration')
    check(not any(k == 'every_owned_state' for k, v, op in walk(legacy['mkn.5'])), 'MKN frontier: legacy victory cores unrelated conquered territory')
    mission = one(decisions, mission_id)
    check(one(mission, 'days_mission_timeout') == '365' and one(one(mission, 'activation'), 'always') == 'no', 'MKN frontier: annual mission has wrong duration or auto-activation')
    check(one(one(mission, 'timeout_effect'), 'mkn_ukr_year_timeout') == 'yes', 'MKN frontier: annual timeout does not freeze the border')
    funeral = next(e for e in values(read(root / 'events/MKN_events.txt'), 'country_event') if one(e, 'id') == 'mkn_crisis.1')
    queued = [v for k, v, op in walk(one(funeral, 'immediate')) if k == 'country_event' and one(v, 'id') == 'mkn_ukr_border.10']
    check(len(queued) == 1 and one(queued[0], 'days') == '7', 'MKN frontier: incident is not scheduled seven days after the Batko departs')
    hooks = one(parsed['on_actions'], 'on_actions')
    check(any(k == 'mkn_ukr_frontier_daily' for k, v, op in walk(one(hooks, 'on_daily_MKN'))), 'MKN frontier: missing daily lifecycle hook')
    localized('MKN_ukr_border_category', 'MKN frontier category')
    for lang in ('english', 'russian'):
        path = root / f'localisation/{lang}/MKN_frontier_l_{lang}.yml'
        check(path.is_file(), f'MKN frontier: missing {lang} localization file')
        if path.is_file():
            text = path.read_text(encoding='utf-8-sig')
            check(path.read_bytes().startswith(b'\xef\xbb\xbf'), f'MKN frontier: missing {lang} UTF-8 BOM')
            if lang == 'russian':
                check('Регион немедленно интегрируется в Федерацию Вольных Советов и становится национальным.' in text, 'MKN frontier: Russian integration tooltip changed or missing')

    def model():
        result = FrontierModel(effects, triggers)
        result.run('mkn_ukr_initialize_frontier')
        return result

    cases = 0
    # Exercise both actual callback branches for every three-battle outcome sequence.
    for outcomes in product((20, 21), repeat=3):
        sim = model()
        for index, suffix in enumerate(outcomes, 1):
            sim.states['196']['owner'] = sim.states['196']['controller'] = 'MKN'
            sim.states['197']['owner'] = sim.states['197']['controller'] = 'UKR'
            original_cores = deepcopy(sim.states['196']['cores'])
            sim.apply(one(events[f'mkn_ukr_border.{suffix}'], 'immediate'))
            check(sim.countries['MKN']['variables']['mkn_consecutive_border_wars'] == index, 'MKN frontier: completed win/loss was not counted exactly once')
            if suffix == 20:
                check(sim.states['197']['owner'] == 'MKN' and 'MKN' in sim.states['197']['cores'], 'MKN frontier: victory did not immediately integrate its contested state')
            else:
                check(sim.states['196']['owner'] == 'UKR' and sim.states['196']['cores'] == original_cores, 'MKN frontier: defeat adds/removes cores while returning territory')
            check(sim.states['500']['cores'] == {'LTB'}, 'MKN frontier: callback cores unrelated territory')
            if index < 3:
                check(not sim.flag('MKN', 'mkn_ukr_war_pending'), 'MKN frontier: full war starts before the third completed battle')
        check(sim.flag('MKN', 'mkn_ukr_war_pending') and sim.countries['MKN']['variables']['mkn_ukr_escalation_level'] == 5, 'MKN frontier: third completed battle does not reach level five')
        sim.border = True
        sim.run('mkn_ukr_frontier_daily')
        check(not any(event[1] == 'mkn_ukr_border.1' for event in sim.events), 'MKN frontier: full war is dispatched during native border combat')
        sim.border = False
        sim.run('mkn_ukr_frontier_daily')
        check(any(event[1] == 'mkn_ukr_border.1' for event in sim.events), 'MKN frontier: pending full war is never dispatched after combat')
        sim.apply(one(events['mkn_ukr_border.1'], 'immediate'))
        sim.run('mkn_ukr_conclude_total_war')
        check(sim.declarations == [('UKR', 'MKN')], 'MKN frontier: full war is missing, reversed, or declared twice')
        check('MKN_war_for_the_steppe' in sim.countries['MKN']['ideas'], 'MKN frontier: full war lacks its permanent spirit')
        cases += 1
    for day, ongoing, expected in ((179, False, 2), (180, False, 0), (400, False, 0), (180, True, 2), (400, True, 2)):
        sim = model()
        sim.run('mkn_ukr_record_border_battle')
        sim.run('mkn_ukr_record_border_battle')
        sim.day, sim.border = day, ongoing
        sim.run('mkn_ukr_frontier_daily')
        check(sim.countries['MKN']['variables']['mkn_consecutive_border_wars'] == expected, f'MKN frontier: wrong 180-day cooling result at day {day}, ongoing={ongoing}')
        cases += 1
    for owner, opponent, root_tag in product(('UKR', 'MKN', 'LTB'), ('UKR', 'SOV'), ('MKN', 'LTB')):
        sim = model()
        sim.root, sim.froms = root_tag, ('196', opponent, '197')
        sim.states['197']['owner'] = sim.states['197']['controller'] = owner
        before = deepcopy(sim.states)
        sim.apply(one(events['mkn_ukr_border.20'], 'immediate'), root_tag)
        valid = root_tag == 'MKN' and opponent == 'UKR' and owner in ('UKR', 'MKN')
        check((sim.states['197']['owner'] == 'MKN' and 'MKN' in sim.states['197']['cores']) if valid else sim.states == before, 'MKN frontier: victory accepts unrelated country/state scope or rejects valid old-save transfer')
        cases += 1
    # Preserve old active border wars without reintroducing blanket coring.
    for state_owner, count_expected in (('MKN', 0), ('UKR', 1)):
        sim = model()
        sim.states['196']['owner'] = sim.states['196']['controller'] = state_owner
        sim.apply(one(legacy['mkn.6'], 'immediate'))
        check(sim.countries['MKN']['variables']['mkn_consecutive_border_wars'] == count_expected, 'MKN frontier: legacy cancellation is counted or an already transferred legacy defeat is lost')
        cases += 1
    sim = model()
    sim.run('mkn_ukr_record_border_battle')
    before = deepcopy(sim.states)
    count = sim.countries['MKN']['variables']['mkn_consecutive_border_wars']
    sim.apply(one(events['mkn_ukr_border.23'], 'immediate'))
    check(sim.states == before and sim.countries['MKN']['variables']['mkn_consecutive_border_wars'] == count, 'MKN frontier: cancelled clash transfers territory or increments completed battles')
    for stock in (0, 399, 400, 1000):
        sim = model()
        sim.froms = ('197',)
        sim.countries['UKR']['equipment'] = stock
        initial = sim.countries['MKN']['equipment'] + stock
        sim.apply(one(one(decisions, 'mkn_raid_soviet_depots'), 'complete_effect'))
        check(sim.countries['MKN']['equipment'] + sim.countries['UKR']['equipment'] == initial, 'MKN frontier: depot raid manufactures equipment instead of conserving stockpiles')
        check(sim.countries['UKR']['equipment'] == stock - (400 if stock >= 400 else 0), 'MKN frontier: depot raid steals from an insufficient stockpile')
        cases += 1
    for discounted in (False, True):
        sim = model()
        if discounted:
            sim.countries['MKN']['flags']['mkn_ukr_recon_discount'] = -1
        sim.run('mkn_ukr_update_decision_costs')
        expected = {'alarm': 30, 'pullback': 25, 'depot': 25, 'battle': 50, 'pact': 50}
        check(all(sim.countries['MKN']['variables'][f'mkn_ukr_{name}_cost'] == cost * (0.5 if discounted else 1) for name, cost in expected.items()), 'MKN frontier: reconnaissance does not halve every decision cost')
        before = deepcopy(sim.countries['MKN']['variables'])
        sim.run('mkn_ukr_update_decision_costs')
        check(sim.countries['MKN']['variables'] == before, 'MKN frontier: daily cost repair repeatedly compounds the discount')
        cases += 1
    sim = model()
    sim.countries['MKN']['flags']['mkn_ukr_pact_pending'] = -1
    for sid in ('197', '203'):
        sim.states[sid]['owner'] = sim.states[sid]['controller'] = 'MKN'
    sim.states['197']['flags']['mkn_ukr_integrated_frontier_state'] = -1
    sim.countries['MKN']['missions'].add(mission_id)
    sim.countries['MKN']['flags']['mkn_frontier_year_running'] = -1
    sim.run('mkn_ukr_finalize_pact')
    check(sim.flag('MKN', 'mkn_ukr_pact_signed') and 'UKR' in sim.countries['MKN']['pacts'], 'MKN frontier: valid consent fails to establish the treaty')
    check('MKN' in sim.states['197']['cores'] and sim.states['500']['cores'] == {'LTB'}, 'MKN frontier: treaty does not repair won-state cores or cores unrelated territory')
    check(mission_id in sim.countries['MKN']['missions'], 'MKN frontier: early voluntary treaty prematurely cancels the fixed annual deadline')
    before = deepcopy((sim.countries, sim.states, sim.relations))
    sim.run('mkn_ukr_finalize_pact')
    sim.run('mkn_ukr_conclude_total_war')
    check((sim.countries, sim.states, sim.relations) == before and not sim.declarations, 'MKN frontier: terminal treaty is overwritten or renewed by repeated finalization')
    sim.day = 729
    sim.run('mkn_ukr_frontier_daily')
    check('UKR' in sim.countries['MKN']['pacts'], 'MKN frontier: pact expires before 730 days')
    sim.day = 730
    sim.run('mkn_ukr_frontier_daily')
    check('UKR' not in sim.countries['MKN']['pacts'] and not sim.flag('MKN', 'mkn_ukr_frontier_pact_owned'), 'MKN frontier: 730-day pact never expires')
    removals = len([relation for relation in sim.relations if not relation[2]])
    sim.run('mkn_ukr_frontier_daily')
    check(len([relation for relation in sim.relations if not relation[2]]) == removals, 'MKN frontier: repeated daily cleanup removes unrelated future pacts')
    cases += 1
    for opponent in ('UKR', 'SOV'):
        sim = model()
        sim.countries['MKN']['wars'].add(opponent)
        sim.countries['MKN']['missions'].add(mission_id)
        sim.countries['MKN']['flags']['mkn_frontier_year_running'] = -1
        sim.run('mkn_ukr_frontier_daily')
        check(sim.flag('MKN', 'mkn_ukr_frontier_concluded') and mission_id not in sim.countries['MKN']['missions'], f'MKN frontier: {opponent} war does not terminate border operations/timer')
        check(not sim.test(triggers['mkn_ukr_frontier_action_available']), f'MKN frontier: decisions remain usable during {opponent} war')
        cases += 1
    for fighting in (False, True):
        sim = model()
        sim.border = fighting
        sim.border_states = {'196', '203'}
        sim.states['197']['owner'] = sim.states['197']['controller'] = 'MKN'
        sim.states['197']['flags']['mkn_ukr_integrated_frontier_state'] = -1
        sim.run('mkn_ukr_year_timeout')
        check(sim.flag('MKN', 'mkn_frontier_frozen') and sim.flag('MKN', 'mkn_ukr_frontier_concluded'), 'MKN frontier: annual timeout fails to freeze the frontier')
        check(sim.states['197']['owner'] == 'MKN' and 'MKN' in sim.states['197']['cores'], 'MKN frontier: annual settlement gives back won territory or loses integration')
        check(not sim.test(triggers['mkn_ukr_frontier_action_available']), 'MKN frontier: frozen border still permits escalation')
        check(not sim.border and len(sim.cancellations) == int(fighting), 'MKN frontier: hard annual ceasefire leaves the native battle running')
        check(all(cancel[2] == 'yes' for cancel in sim.cancellations), 'MKN frontier: annual cancellation fires capture callbacks after freezing the border')
        check(all(cancel[:2] == ('196', '203') for cancel in sim.cancellations), 'MKN frontier: old-save cancellation fails to discover the exact active MKN/UKR state pair')
        cases += 1
    for saved_pair in (False, True):
        sim = model()
        sim.border = True
        sim.border_states = {'196', '197'}
        if saved_pair:
            sim.countries['MKN']['variables'].update({'mkn_ukr_attacking_state': '196', 'mkn_ukr_defending_state': '197'})
        sim.run('mkn_ukr_stop_border_battle')
        check(not sim.border and sim.cancellations == [('196', '197', 'yes')], 'MKN frontier: stored/legacy active battle is not cancelled exactly once without callbacks')
        cases += 1
    for concluded in (False, True):
        sim = model()
        if concluded:
            sim.countries['MKN']['flags']['mkn_ukr_frontier_concluded'] = -1
            sim.countries['MKN']['variables']['mkn_ukr_escalation_level'] = 5
        sim.apply(one(events['mkn_ukr_border.10'], 'immediate'))
        check(sim.flag('MKN', 'mkn_ukr_incident_fired'), 'MKN frontier: initial incident is not marked as fired')
        check((mission_id in sim.countries['MKN']['missions']) == (not concluded), 'MKN frontier: initial incident fails to start the annual mission or reopens a terminal frontier')
        check(sim.countries['MKN']['variables']['mkn_ukr_escalation_level'] == (5 if concluded else 2), 'MKN frontier: initial incident overwrites a terminal escalation level')
        cases += 1
    sim = model()
    sim.countries['MKN']['flags']['mkn_batko_departed'] = -1
    sim.run('mkn_ukr_schedule_old_save_incident')
    before = list(sim.events)
    sim.run('mkn_ukr_schedule_old_save_incident')
    check(sim.events == before and sim.events == [('MKN', 'mkn_ukr_border.10', 7)], 'MKN frontier: old-save startup duplicates or reschedules the incident')
    check(not any(k == 'mkn_ukr_schedule_old_save_incident' for k, v, op in walk(effects['mkn_ukr_frontier_daily'])), 'MKN frontier: daily repair postpones the incident delay')
    cases += 1
    print(f'PASS: MKN/UKR native frontier callbacks, exact-state cores, localization and {cases} source-script lifecycle scenarios')
