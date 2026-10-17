"""Replay FRA's paid colonial decisions and live German declaration rule.

Decision scheduling here is a bounded scenario model, not the game's AI.
"""
from copy import deepcopy
from datetime import date, timedelta
from pathlib import Path

from hoi4_script import one, read, values, walk
from test_france_lifecycle import Model, EFFECTS, DECISIONS, FOCUSES
from validate_germany_politics import Scenario

ROOT = Path(__file__).resolve().parents[1]
TRIGGERS = {k: v for path in (ROOT / 'common/scripted_triggers').glob('FRA*.txt') for k, v, _ in read(path)}
EVENTS = {one(event, 'id'): event for event in values(read(ROOT / 'events/FRA_events.txt'), 'country_event')}
PLANS = {k: v for k, v, _ in read(ROOT / 'common/ai_strategy_plans/FRA_plans.txt')}
REGIONS = ['algeria', 'maghreb', 'west_africa', 'equatorial', 'indochina', 'islands']


class France(Model):
    def __init__(self):
        super().__init__()
        self.ai = True
        self.historical, self.rule = True, 'DEFAULT'
        self.queue, self.running, self.mission_deadlines = [], {}, {}
        self.released, self.factories = set(), 0
        self.spent, self.settlement_day = 0, {}

    def test(self, nodes):
        result = []
        for key, value, op in nodes:
            if key in TRIGGERS and not key.startswith(('FRA_holds_', 'FRA_can_release_')):
                result.append(self.test(TRIGGERS[key]) == (value == 'yes'))
            elif key.startswith('FRA_can_release_'):
                result.append((key.removeprefix('FRA_can_release_') in self.held) == (value == 'yes'))
            elif key == 'original_tag':
                result.append(value == 'FRA')
            elif key == 'has_game_rule':
                result.append(one(value, 'rule') == 'FRA_ai_behavior' and one(value, 'option') == self.rule)
            elif key == 'is_historical_focus_on':
                result.append(self.historical == (value == 'yes'))
            else:
                result.append(super().test([(key, value, op)]))
        return all(result)

    def apply(self, nodes):
        branch = False
        for key, value, op in nodes:
            if key in ('if', 'else_if'):
                run = (key == 'if' or not branch) and self.test(one(value, 'limit', []))
                if key == 'if':
                    branch = False
                if run:
                    self.apply([entry for entry in value if entry[0] != 'limit'])
                    branch = True
            elif key == 'else':
                if not branch:
                    self.apply(value)
                branch = False
            elif key == 'country_event':
                self.queue.append((self.day + int(one(value, 'days', '0')), one(value, 'id')))
            elif key == 'random_owned_controlled_state':
                self.factories += 1
            elif key.startswith('FRA_release_') or key.startswith('FRA_war_release_') or key.startswith('FRA_autonomy_'):
                region = key.split('_', 2)[2]
                self.released.add(region)
                self.held.discard(region)
            else:
                super().apply([(key, value, op)])

    def score(self, block):
        factor = float(one(block, 'factor', '1'))
        for mod in values(block, 'modifier'):
            if self.test([entry for entry in mod if entry[0] != 'factor']):
                factor *= float(one(mod, 'factor', '1'))
        return factor

    def choose_event(self, eid):
        choices = [option for option in values(EVENTS[eid], 'option') if self.test(one(option, 'trigger', []))]
        choice = max(choices, key=lambda option: self.score(one(option, 'ai_chance', [])))
        self.apply([entry for entry in choice if entry[0] not in {'name', 'trigger', 'ai_chance'}])

    def start(self, name):
        body = DECISIONS[name]
        assert self.test(one(body, 'visible', [])) and self.test(one(body, 'available', [])), name
        cost = float(one(body, 'cost', '0'))
        assert self.pp >= cost, name
        self.pp -= cost
        self.spent += cost
        self.apply(one(body, 'complete_effect', []))
        self.running[name] = self.day + int(one(body, 'days_remove', '0'))

    def tick(self, income=0.5):
        self.day += 1
        self.date += timedelta(days=1)
        self.pp += income
        for flag, expiry in list(self.expiries.items()):
            if self.day >= expiry:
                self.flags.discard(flag)
                del self.expiries[flag]
        self.run('FRA_daily')
        for name, end in list(self.running.items()):
            if self.day >= end:
                self.apply(one(DECISIONS[name], 'remove_effect', []))
                del self.running[name]
        due = [entry for entry in self.queue if entry[0] <= self.day]
        self.queue = [entry for entry in self.queue if entry[0] > self.day]
        for _, eid in due:
            self.choose_event(eid)
        for name in list(self.missions):
            body = DECISIONS[name]
            self.mission_deadlines.setdefault(name, self.day + int(one(body, 'days_mission_timeout')))
            if self.test(one(body, 'cancel_trigger', [])):
                self.apply(one(body, 'cancel_effect', []))
                self.missions.discard(name)
                del self.mission_deadlines[name]
            elif self.day >= self.mission_deadlines[name]:
                self.apply(one(body, 'timeout_effect', []))
                self.missions.discard(name)
                del self.mission_deadlines[name]
        for region in REGIONS:
            if 'FRA_' + region + '_represented' in self.flags:
                self.settlement_day.setdefault(region, self.day)


cases = 0


def check(ok, message):
    global cases
    assert ok, message
    cases += 1


# Read the actual focus order and rewards; retain mandate / PP costs and 30-day ticks.
plan = [fid for _, fid, _ in one(PLANS['FRA_nww_plan_REPUBLIC'], 'ai_national_focuses')]
for income in [0.5, 0.75, 1.0]:
    for decision_lag in [1, 7, 14]:
        m = France()
        m.pp = 0
        m.held = set(REGIONS)
        m.run('FRA_initialize')
        next_focus, deadline = 0, int(one(FOCUSES[plan[0]], 'cost')) * 7
        for _ in range(1000):
            m.tick(income)
            if m.day == deadline and next_focus < len(plan):
                focus = FOCUSES[plan[next_focus]]
                check(m.test(one(focus, 'available', [])), f'Historical focus unavailable: {plan[next_focus]}, day={m.day}')
                for group in values(focus, 'prerequisite'):
                    check(bool(set(values(group, 'focus')) & m.completed), 'Missing historical focus prerequisite')
                m.completed.add(plan[next_focus])
                m.apply(one(focus, 'completion_reward'))
                next_focus += 1
                if next_focus < len(plan):
                    deadline += int(one(FOCUSES[plan[next_focus]], 'cost')) * 7
            if m.day % decision_lag == 0:
                candidates = []
                for name, body in DECISIONS.items():
                    if one(body, 'days_mission_timeout') or name in m.running:
                        continue
                    if not (name.startswith('FRA_nww_invest_') or name.startswith('FRA_nww_negotiate_') or
                            name in {'FRA_nww_coalition', 'FRA_nww_inquiry', 'FRA_nww_social_arbitration',
                                     'FRA_nww_decree'} or name.startswith('FRA_nww_campaign_')):
                        continue
                    if not m.test(one(body, 'visible', [])) or not m.test(one(body, 'available', [])):
                        continue
                    score = m.score(one(body, 'ai_will_do', []))
                    if score > 0 and m.pp >= float(one(body, 'cost', '0')):
                        candidates.append((score, name))
                if candidates:
                    m.start(max(candidates)[1])
            check(not m.released, f'Historical colonies lost with income={income}, lag={decision_lag}, day={m.day}')
        check(len(m.settlement_day) == 6, f'Not all six settlements completed: {m.settlement_day}')
        check(m.spent >= 300, 'Settlements were not paid')
        check(m.score(one(DECISIONS['FRA_nww_campaign_republic'], 'ai_will_do')) == 0,
              'Democratic popularity campaign loops after mandate is viable')

# A conference holds its serialization lock for the full 35 + 1 + 7-day lifecycle.
for region in REGIONS:
    m = France()
    m.held = {region}
    m.flags.add('FRA_policy_representation')
    m.completed.add('FRA_nww_overseas_conference')
    m.variables['FRA_' + region + '_pressure'] = 70
    m.start('FRA_nww_negotiate_' + region)
    m.apply(one(DECISIONS['FRA_nww_negotiate_' + region], 'remove_effect'))
    check('FRA_negotiation_busy' in m.flags, 'Conference freed its lock before the reply')
    m.choose_event('nww_fra.' + str(100 + REGIONS.index(region)))
    check('FRA_negotiation_busy' in m.flags, 'Offer freed its lock before regional consent')
    m.choose_event('nww_fra.' + str(140 + REGIONS.index(region)))
    check('FRA_negotiation_busy' not in m.flags, 'Reply leaked its busy flag')
    check('FRA_' + region + '_represented' in m.flags and not m.released, 'Paid representation released land')
    for pressure in [79, 80, 100]:
        for pp in [49, 50]:
            x = France()
            x.held = {region}
            x.flags.add('FRA_policy_representation')
            x.variables['FRA_' + region + '_pressure'] = pressure
            x.pp = pp
            offer = values(EVENTS['nww_fra.' + str(100 + REGIONS.index(region))], 'option')[0]
            check(x.test(one(offer, 'trigger')) == (pressure < 80 or pp >= 50), 'Emergency affordability boundary')
            if x.test(one(offer, 'trigger')):
                x.choose_event('nww_fra.' + str(100 + REGIONS.index(region)))
                check(x.pp == pp - (50 if pressure >= 80 else 0), 'Emergency guarantees charged incorrectly')
                x.choose_event('nww_fra.' + str(140 + REGIONS.index(region)))
                check('FRA_' + region + '_represented' in x.flags and not x.released, 'Emergency negotiations failed')


class Diplomacy(Scenario):
    def __init__(self):
        effects = {k: v for k, v, _ in read(ROOT / 'common/scripted_effects/FRA_ai_effects.txt')}
        super().__init__(effects, {})
        self.triggers.update(TRIGGERS)
        self.ai, self.historical, self.rule = True, False, 'MONARCHY'
        self.date = '1940.1.1'
        self.countries['FRA'].update(tree='french_focus', strength=130, stability=0.7, war_support=0.7)
        self.countries['FRA']['focuses'] |= {'FRA_nww_signals_supply', 'FRA_nww_officer_corps', 'FRA_nww_rhine_preparations'}
        self.countries['GER']['strength'] = 100
        self.apply(self.effects['FRA_install_ai_campaign_guard'], 'FRA')

    def condition(self, nodes, actor='FRA', root=None, stack=()):
        for entry in nodes:
            if entry[0] == 'has_game_rule':
                result = one(entry[1], 'rule') == 'FRA_ai_behavior' and one(entry[1], 'option') == self.rule
            else:
                result = super().condition([entry], actor, root, stack)
            if not result:
                return False
        return True

    def permitted(self, actor='FRA', target='GER'):
        self.from_country = target
        return not any(rule[0] == 'trigger' and self.condition(self.triggers[rule[1]], actor, actor)
                       for rule in self.countries[actor]['rules'] if isinstance(rule, tuple))


check(Diplomacy().permitted(), 'Prepared strong nonhistorical France cannot declare war')
w = Diplomacy()
w.historical = True
check(w.permitted(), 'Explicit monarchy rule lost to historical DEFAULT policy')
for fault in ['historical', 'strength', 'stability', 'war_support', 'army', 'preparation',
              'early', 'war', 'civil_war', 'capitulated', 'subject', 'faction', 'guarantee']:
    w = Diplomacy()
    s = w.countries['FRA']
    if fault == 'historical':
        w.historical, w.rule = True, 'DEFAULT'
    elif fault == 'strength':
        s['strength'] = 125  # Target/FRA = 0.80 is insufficient at the strict boundary.
    elif fault in {'stability', 'war_support'}:
        s[fault] = 0.50
    elif fault == 'army':
        s['focuses'].discard('FRA_nww_officer_corps')
    elif fault == 'preparation':
        s['focuses'].discard('FRA_nww_rhine_preparations')
    elif fault == 'early':
        w.date = '1939.12.31'
    elif fault == 'war':
        s['wars'].add('AUS')
    elif fault in {'civil_war', 'capitulated'}:
        s[fault] = True
    elif fault == 'subject':
        s['subject'] = 'ENG'
    elif fault == 'faction':
        w.countries['GER']['faction'] = w.countries['AUS']['faction'] = 'GER'
    elif fault == 'guarantee':
        w.countries['ENG'].update(major=True, guarantees={'GER'})
    check(not w.permitted(), 'Unsafe French attack permitted: ' + fault)
    w.countries['FRA']['goals'].add('GER')
    check(not w.permitted(), 'Cached war goal bypassed the live declaration guard: ' + fault)
    check(w.permitted(target='AUS'), 'German guard blocked an unrelated target')
    w.ai = False
    check(w.permitted(), 'AI restriction applied to a human')
w = Diplomacy()
before = deepcopy(w.countries['FRA']['rules'])
w.apply(w.effects['FRA_install_ai_campaign_guard'], 'FRA')
check(before == w.countries['FRA']['rules'], 'Guard installation accumulates rules on reload')
front = one(read(ROOT / 'common/ai_strategy/FRA_nww_strategy.txt'), 'FRA_nww_careful_GER_front')
for strength in [50, 100, 125, 126, 200]:
    w = Diplomacy()
    w.countries['FRA']['strength'] = strength
    w.countries['FRA']['wars'].add('GER')
    check(w.condition(one(front, 'enable'), 'FRA') == (strength <= 125),
          'German-front caution has incorrect strength boundary')
    w.ai = False
    check(not w.condition(one(front, 'enable'), 'FRA'), 'AI front restraint affected the player')
control = next(node for node in values(front, 'ai_strategy') if one(node, 'type') == 'front_control')
check(set(values(control, 'state')) == {'28', '42', '51', '978'}, 'Cautious front uses obsolete borders')
check(one(control, 'execute_order') == one(control, 'manual_attack') == 'no', 'Weak AI still executes attacks')
w = Diplomacy()
w.countries['FRA'].update(strength=200, surrender=0.3)
w.countries['FRA']['wars'].add('GER')
check(not w.condition(one(front, 'enable'), 'FRA'), 'Territorial losses permanently blocked a strong counterattack')
print(f'PASS: {cases} French AI source-script checks; paid 1000-day colonial routes, conference serialization, '
      'emergency affordability, historical restraint, live strength/coalition rules and human control. No engine AI claim.')
