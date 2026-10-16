"""Validate the consolidated economy and execute project/cancellation/save lifecycles.

This source-script model covers decisions and economic variables, not engine UI,
rail pathfinding, production, or combat. Unknown executed commands fail loudly.
"""
from collections import Counter
from copy import deepcopy
from itertools import product
from pathlib import Path
import argparse
import csv
import json
import re

from hoi4_script import read, one, values, walk, engine_script_errors, tree_focuses, focus_registry


class EconomyModel:
    def __init__(self, root, effects):
        self.effects = effects
        self.focuses, self.flags, self.ideas, self.dynamic = set(), set(), set(), set()
        self.variables, self.offmap, self.resources = {}, Counter(), Counter()
        self.pp, self.cp, self.stability, self.manpower, self.xp = 500, 25, 0.5, 0, 0
        self.capitulated, self.free_civs = False, 2
        self.events, self.railways, self.active = [], [], {}
        self.day, self.target = 0, None
        self.states = {}
        for path in (root / 'history/states').glob('*.txt'):
            state = one(read(path), 'state')
            sid = one(state, 'id')
            if sid not in {'196', '200', '226', '1082'}:
                continue
            history = one(state, 'history')
            self.states[sid] = dict(owner=one(history, 'owner'), controller=one(history, 'owner'),
                core='MKN' in values(history, 'add_core_of'), slots=0,
                buildings=Counter({k: int(v) for k, v, o in one(history, 'buildings') if not isinstance(v, list)}))

    def test(self, nodes, scope=None):
        def evaluate(key, value, op):
            if key == 'NOT': return not self.test(value, scope)
            if key == 'OR': return any(self.test([item], scope) for item in value)
            if key == 'AND': return self.test(value, scope)
            if key == 'FROM': return self.test(value, self.target)
            if key in self.states: return self.test(value, key)
            if key == 'has_completed_focus': return value in self.focuses
            if key == 'has_country_flag': return value in self.flags
            if key == 'has_idea': return value in self.ideas
            if key == 'has_capitulated': return self.capitulated == (value == 'yes')
            if key == 'is_owned_and_controlled_by':
                assert value == 'ROOT'
                return self.states[scope]['owner'] == self.states[scope]['controller'] == 'MKN'
            if key == 'is_controlled_by': return self.states[scope]['controller'] == 'MKN'
            if key == 'is_core_of': return self.states[scope]['core']
            if key == 'any_owned_state':
                return any(s['owner'] == 'MKN' and self.test(value, sid) for sid, s in self.states.items())
            if key == 'free_building_slots':
                kind, province = one(value, 'building'), one(value, 'province')
                cap = {'naval_base': 10, 'supply_node': 1}[kind]
                return self.states[scope]['buildings'][kind + ':' + province] < cap
            actual = {'command_power': self.cp, 'num_of_civilian_factories_available_for_projects': self.free_civs}.get(key)
            if key in {'infrastructure', 'anti_air_building'}: actual = self.states[scope]['buildings'][key]
            if actual is not None:
                return {'<': actual < float(value), '>': actual > float(value), '=': actual == float(value)}[op]
            raise AssertionError('Unhandled economy trigger: ' + str(key))
        return all(evaluate(*item) for item in nodes)

    def apply(self, nodes, scope=None):
        matched = False
        for key, value, op in nodes:
            if key in {'if', 'else_if'}:
                if key == 'if': matched = False
                if not matched and self.test(one(value, 'limit'), scope):
                    self.apply([n for n in value if n[0] != 'limit'], scope)
                    matched = True
            elif key == 'else':
                if not matched: self.apply(value, scope)
                matched = True
            elif key in self.effects: self.apply(self.effects[key], scope)
            elif key == 'FROM': self.apply(value, self.target)
            elif key in self.states: self.apply(value, key)
            elif key == 'random_owned_controlled_state':
                sid = next(sid for sid, s in self.states.items() if s['owner'] == s['controller'] == 'MKN' and self.test(one(value, 'limit'), sid))
                self.apply([n for n in value if n[0] not in {'limit', 'prioritize'}], sid)
            elif key in {'set_variable', 'add_to_variable'}:
                for stat, amount, o in value:
                    if stat != 'tooltip':
                        self.variables[stat] = (self.variables.get(stat, 0) if key == 'add_to_variable' else 0) + float(amount)
            elif key == 'set_country_flag': self.flags.add(value)
            elif key == 'add_building_construction':
                kind = one(value, 'type')
                if one(value, 'province'): kind += ':' + one(value, 'province')
                self.states[scope]['buildings'][kind] += int(one(value, 'level'))
            elif key == 'add_extra_state_shared_building_slots': self.states[scope]['slots'] += int(value)
            elif key == 'add_resource': self.resources[(scope, one(value, 'type'))] += int(one(value, 'amount'))
            elif key == 'add_offsite_building': self.offmap[one(value, 'type')] += int(one(value, 'level'))
            elif key == 'build_railway': self.railways.append(value)
            elif key == 'add_dynamic_modifier': self.dynamic.add(one(value, 'modifier'))
            elif key == 'remove_ideas': self.ideas -= {v for k, v, o in value}
            elif key == 'add_timed_idea': self.ideas.add(one(value, 'idea'))
            elif key == 'country_event': self.events.append(one(value, 'id'))
            elif key == 'custom_effect_tooltip': pass
            elif key in {'add_political_power', 'add_command_power', 'add_stability', 'add_manpower', 'army_experience'}:
                attr = {'add_political_power': 'pp', 'add_command_power': 'cp', 'add_stability': 'stability', 'add_manpower': 'manpower', 'army_experience': 'xp'}[key]
                setattr(self, attr, getattr(self, attr) + float(value))
            else: raise AssertionError('Unhandled economy effect: ' + str(key))

    def can_start(self, name, decision):
        self.target = one(decision, 'targets', [(None, None, None)])[0][1]
        return name not in self.active and self.pp >= float(one(decision, 'cost', '0')) and all(self.test(one(decision, field, [])) for field in ('visible', 'target_root_trigger', 'target_trigger', 'available', 'custom_cost_trigger'))

    def start(self, name, decision):
        assert self.can_start(name, decision)
        self.pp -= float(one(decision, 'cost', '0'))
        self.apply(one(decision, 'complete_effect', []))
        if one(decision, 'days_remove'):
            self.active[name] = (self.day + int(one(decision, 'days_remove')), self.target, decision)

    def advance(self, days):
        for _ in range(days):
            self.day += 1
            for name, (deadline, target, decision) in list(self.active.items()):
                self.target = target
                cancel = one(decision, 'cancel_trigger')
                if cancel and self.test(cancel):
                    self.apply(one(decision, 'cancel_effect', [])); del self.active[name]
                elif self.day >= deadline:
                    self.apply(one(decision, 'remove_effect', [])); del self.active[name]


def validate_economy(root, game, check, localized):
    fs = {one(f, 'id'): f for f in tree_focuses(one(read(root/'common/national_focus/MKN.txt'), 'focus_tree'), root/'common/national_focus')}
    meta = json.loads((root/'docs/MKN_unified_progression.json').read_text())
    industry = set(meta['industry_changes'])
    effects = {k: v for k, v, o in read(root/'common/scripted_effects/nww_mkn_progression.txt')}
    physical_rewards = {'add_building_construction', 'add_resource', 'add_offsite_building', 'build_railway',
        'add_extra_state_shared_building_slots', 'add_political_power', 'add_command_power', 'army_experience',
        'add_manpower', 'add_research_slot', 'add_equipment_to_stockpile', 'country_event', 'add_mio_size'}
    check(not any(k in physical_rewards or (k and k.startswith('mio:')) for k, v, o in walk(effects['nww_mkn_rebuild_industry'])), 'MKN economy: save repair replays one-off rewards')
    decisions = read(root/'common/decisions/MKN_economic_decisions.txt')
    projects = dict((k, v) for k, v, o in one(decisions, 'MKN_economic_projects_category'))
    congress = dict((k, v) for k, v, o in one(decisions, 'MKN_economic_congress_category'))
    check(len(industry) == 20 and len(projects) == 9 and len(congress) == 5, 'MKN economy: expected 20 focuses, nine projects, five congress decisions')
    for name, d in projects.items():
        check(one(d, 'state_target') == 'yes' and one(d, 'on_map_mode') == 'map_and_decisions_view', name + ': missing map interaction')
        check(one(d, 'days_remove') == '60' and not one(d, 'complete_effect'), name + ': project pays before day 60')
        check(one(d, 'fire_only_once') != 'yes', name + ': cancellation prevents retry')
        check(not list(engine_script_errors([(name, d, '=')])), name + ': engine syntax error')
        check(float(one(d, 'cost')) > 0 or one(one(d, 'modifier', []), 'civilian_factory_use') == '2', name + ': project has no cost')
    for name, d in {**projects, **congress}.items():
        localized(name, name); localized(name+'_desc', name)
        for k, v, o in walk(d):
            if k in {'has_completed_focus'}: check(v in fs, name + ': missing focus ' + v)
            if k == 'add_to_variable': localized(one(v, 'tooltip'), name)
    categories = read(root/'common/decisions/categories/MKN_economic_categories.txt')
    congress_gate = one(one(one(categories, 'MKN_economic_congress_category'), 'visible'), 'OR')
    check(set(values(congress_gate, 'has_completed_focus')) == {'MKN_artel_register', 'MKN_the_absolute_argument'}, 'MKN: congress requires its register or the reactor project; earlier economic decisions retain their individual gates')
    for k, v, o in categories: localized(k, k); localized(k+'_desc', k)
    ideas = one(one(read(root/'common/ideas/MKN_economic_ideas.txt'), 'ideas'), 'country')
    native_modifiers = set(re.findall(r'^## (\w+)', (game/'documentation/modifiers_documentation.md').read_text(), re.M))
    for name, idea, o in ideas:
        localized(name, name); localized(name+'_desc', name)
        for stat, value, o in one(idea, 'modifier'):
            check(stat in native_modifiers, name + ': unknown native modifier ' + stat)
    for path in ['common/decisions/MKN_economic_decisions.txt', 'common/decisions/categories/MKN_economic_categories.txt', 'common/ideas/MKN_economic_ideas.txt', 'common/military_industrial_organization/organizations/MKN_organizations.txt']:
        check(not list(engine_script_errors(read(root/path))), path + ': engine syntax error')
    cases = 0
    def model():
        m = EconomyModel(root, effects); m.focuses |= industry
        return m
    def snapshot(m): return deepcopy((m.states, m.offmap, m.resources, m.variables, m.stability, m.manpower, m.xp, m.railways))
    for name, d in projects.items():
        gate = one(one(d, 'visible'), 'has_completed_focus')
        m = model(); m.focuses.remove(gate)
        check(not m.can_start(name, d), name + ': missing focus does not hide project')
        m.focuses.add(gate); baseline = snapshot(m); m.start(name, d); m.advance(59)
        check(snapshot(m) == baseline, name + ': premature reward')
        m.advance(1)
        check(snapshot(m) != baseline and name+'_done' in m.flags, name + ': missing completion reward')
        check(not m.can_start(name, d), name + ': completed project can repeat')
        once = snapshot(m); m.apply(one(d, 'remove_effect'))
        check(snapshot(m) == once, name + ': reward guard allows duplicate callback')
        # Existing buildings, factories and resources survive variable repair.
        before = deepcopy((m.states, m.offmap, m.resources, m.pp, m.manpower))
        m.apply(effects['nww_mkn_rebuild_industry']); first = dict(m.variables)
        m.apply(effects['nww_mkn_rebuild_industry'])
        check(m.variables == first and before == (m.states, m.offmap, m.resources, m.pp, m.manpower), name + ': repair repeats rewards or stacks bonuses')
        for sid in [one(d, 'targets')[0][1]] + (['196'] if name == 'MKN_project_dnieper_waterways' else []):
            for attr in ('owner', 'controller', 'core'):
                if sid != one(d, 'targets')[0][1] and attr == 'core':
                    continue
                m = model(); before = snapshot(m); pp = m.pp; m.start(name, d)
                original = m.states[sid][attr]; m.states[sid][attr] = False if attr == 'core' else 'UKR'
                m.advance(30)
                check(name not in m.active and name+'_done' not in m.flags and m.pp == pp, name + ': loss does not cancel/refund')
                m.states[sid][attr] = original
                check(snapshot(m) == before, name + ': cancelled work grants reward')
                check(m.can_start(name, d), name + ': cancelled work cannot restart')
                m.start(name, d); m.advance(60)
                check(name+'_done' in m.flags, name + ': restarted project fails')
                cases += 1
        m = model(); m.start(name, d); m.capitulated = True; m.advance(1)
        check(name not in m.active and name+'_done' not in m.flags, name + ': capitulation does not cancel')
        if one(d, 'modifier'):
            m = model(); m.free_civs = 1
            check(not m.can_start(name, d), name + ': can reserve two unavailable factories')
        cases += 1
    cp_name = 'MKN_congress_recallable_commanders'; cp = congress[cp_name]
    for amount in (24, 24.5, 25, 26):
        m = model(); m.cp = amount
        check(m.can_start(cp_name, cp) == (amount >= 25), 'MKN congress: incorrect CP threshold')
        if amount >= 25:
            m.start(cp_name, cp)
            check(m.cp == amount - 25 and m.xp == 10 and 'MKN_congress_elected_commanders' in m.ideas, 'MKN congress: CP reward/cost')
            check(not m.can_start(cp_name, cp), 'MKN congress: CP initiative repeats')
        cases += 1
    for name, d in congress.items():
        m = model(); m.start(name, d)
        if one(d, 'days_remove'): m.advance(int(one(d, 'days_remove')))
        check(not m.can_start(name, d), name + ': congress initiative repeats')
    # Every prefix of both economic routes reconstructs exactly the live variables.
    for entry, finale, duration in [('MKN_dneprostroi', 'MKN_steel_volnitsa', 525), ('MKN_free_cooperatives', 'MKN_communal_compact', 490)]:
        branch = {entry}
        while True:
            more = branch | {fid for fid in industry if any(one(n, 'focus') in branch for n in values(fs[fid], 'prerequisite'))}
            if more == branch: break
            branch = more
        order = sorted(branch, key=lambda fid: (int(one(fs[fid], 'y')), int(one(fs[fid], 'x'))))
        check(sum(int(one(fs[fid], 'cost'))*7 for fid in branch) == duration, entry + ': pacing changed')
        check(finale in branch and len(branch) == 10, entry + ': invalid branch')
        # Condensation must preserve the factory budget across focuses,
        # regional projects and congress initiatives, including off-map lines.
        paid_projects = [d for d in projects.values() if one(one(d, 'visible'), 'has_completed_focus') in branch]
        rewards = [one(fs[fid], 'completion_reward') for fid in branch]
        rewards += [one(d, 'remove_effect') for d in paid_projects]
        if entry == 'MKN_free_cooperatives':
            rewards += [one(d, 'remove_effect', []) for d in congress.values()]
        factories = Counter()
        for reward in rewards:
            for k, v, o in walk(reward):
                if k in {'add_building_construction', 'add_offsite_building'}:
                    kind = one(v, 'type')
                    if kind in {'industrial_complex', 'arms_factory'}:
                        factories[kind] += int(one(v, 'level'))
        expected = (6, 7) if entry == 'MKN_dneprostroi' else (7, 4)
        check((factories['industrial_complex'], factories['arms_factory']) == expected, entry + ': consolidated factory budget differs')
        counts = Counter(one(one(d, 'visible'), 'has_completed_focus') for d in paid_projects)
        check(all(n == 3 for n in counts.values()), entry + ': project groups must have three sites')
        for count in range(11):
            m = EconomyModel(root, effects); m.apply(effects['nww_mkn_rebuild_industry'])
            for fid in order[:count]:
                m.apply([(k, v, o) for k, v, o in one(fs[fid], 'completion_reward') if k == 'add_to_variable'])
                m.focuses.add(fid)
            live = dict(m.variables); m.apply(effects['nww_mkn_rebuild_industry'])
            check(all(abs(live[k]-m.variables[k]) < 1e-9 for k in live), entry + ': prefix repair mismatch')
            cases += 1
    # Validate the coastal port and province-level hub against the installed map.
    definition = root/'map/definition.csv'
    if not definition.exists(): definition = game/'map/definition.csv'
    provinces = {r[0]: r for r in csv.reader(definition.open(), delimiter=';') if r}
    check(provinces['721'][5] == 'true', 'MKN waterways: naval base is inland')
    for name, d in projects.items():
        for k, v, o in walk(one(d, 'remove_effect')):
            if k == 'add_building_construction' and one(v, 'type') in {'supply_node', 'naval_base'}:
                check(one(v, 'province') in {'429', '721'}, name + ': provincial building lacks a valid province')
    for hook in ('on_startup', 'on_daily_MKN'):
        n = one(one(read(root/'common/on_actions/nww_mkn_progression.txt'), 'on_actions'), hook)
        check(any(k == 'has_country_flag' and v == 'MKN_industry_integration_v4' for k, v, o in walk(n)), 'MKN: missing v4 save repair guard')
    # Combined project flags survive repeated repair without returning resources.
    for energy, trade in product((False, True), repeat=2):
        m = EconomyModel(root, effects)
        if energy: m.flags.add('MKN_project_dnieper_turbines_done')
        if trade: m.flags.add('MKN_project_kherson_terminals_done')
        m.apply(effects['nww_mkn_rebuild_industry']); once = dict(m.variables)
        m.apply(effects['nww_mkn_rebuild_industry'])
        check(m.variables == once and m.variables['MKN_unified_energy_gain_factor'] == (0.10 if energy else 0) and m.variables['MKN_unified_convoy_retreat_speed'] == (0.10 if trade else 0), 'MKN: combined project flag repair')
        check(not m.resources and not m.offmap, 'MKN: repair repeats physical project rewards')
        cases += 1
    # Live gates require playable focuses. The v5 military importer may read
    # registered, hidden legacy tokens to restore earned bonuses in old saves.
    military = json.loads((root/'docs/MKN_military_refactor.json').read_text())
    retired = set(military['old_rewards']) - set(fs)
    registered = focus_registry(root/'common/national_focus')
    for path in [root/'common/scripted_effects/nww_mkn_progression.txt', root/'common/ideas/nww_MKN_ideas.txt']:
        for k, v, o in walk(read(path)):
            if k == 'has_completed_focus':
                check(v in fs or (path.name == 'nww_mkn_progression.txt' and v in retired and v in registered), str(path.name) + ': deleted focus ' + v)
    print(f'PASS: MKN economy: 20 focuses, 5 congress decisions, 9 map projects, {cases} source-script lifecycle/repair cases')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--game', type=Path, required=True)
    args = parser.parse_args(); root = Path(__file__).resolve().parents[1]; errors = []
    def check(ok, message):
        if not ok: errors.append(message)
    locales = {lang: {k for p in (root/'localisation').rglob(f'*l_{lang}.yml') for k in re.findall(r'^\s+(\w+):', p.read_text(encoding='utf-8-sig'), re.M)} for lang in ('russian', 'english')}
    def localized(key, context):
        for lang, keys in locales.items(): check(key in keys, f'{context}: missing {lang} {key}')
    validate_economy(root, args.game, check, localized)
    for error in errors: print('ERROR:', error)
    raise SystemExit(bool(errors))
