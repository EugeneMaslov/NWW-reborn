"""Source-script regressions for MKN alliances, Odessa, political AI and integration.

Models script branches and persistent data. It does not reproduce game rendering,
AI scheduling, combat or peace conferences; unknown executed commands fail.
"""
import argparse
from collections import Counter
from copy import deepcopy
from itertools import product
from pathlib import Path
import hashlib
import json
import re
from PIL import Image, ImageStat
from hoi4_script import read, one, values, walk, tree_focuses, parse, engine_script_errors
from validate_mkn_frontier import FrontierModel

ROOT = Path(__file__).resolve().parents[1]


class World(FrontierModel):
    def __init__(self):
        effects = {k: v for p in (ROOT/'common/scripted_effects').glob('*.txt') if 'mkn' in p.name.lower() for k, v, o in read(p)}
        triggers = {k: v for p in (ROOT/'common/scripted_triggers').glob('MKN*.txt') for k, v, o in read(p)}
        super().__init__(effects, triggers)
        self.historical, self.rule, self.pick, self.layout = True, 'DEFAULT', 0, 0
        for tag, c in self.countries.items():
            c.update(ai=tag == 'MKN', government='communism', tree='MKN_focus' if tag == 'MKN' else 'other',
                     faction=None, traits=set(), portraits={'neutrality': 'GFX_Portrait_makhno'}, rules=set(), slots=3,
                     capital='1082' if tag == 'MKN' else '202' if tag == 'UKR' else None, capitulated=False,
                     popularity=dict(communism=0.6, democratic=0.2, neutrality=0.1, fascism=0.1), pp=500, cores=set())
        self.states = {}
        for path in (ROOT/'history/states').glob('*.txt'):
            s = one(read(path), 'state'); h = one(s, 'history', [])
            if one(h, 'owner') not in {'MKN', 'UKR'}: continue
            sid, owner = one(s, 'id'), one(h, 'owner')
            self.states[sid] = dict(owner=owner, controller=owner, cores=set(values(h, 'add_core_of')),
                                    flags={}, damage=0, neighbors=(), buildings=Counter(), slots=0)
        self.states['500'] = dict(owner='SOV', controller='SOV', cores={'SOV'}, flags={}, damage=0, neighbors=(), buildings=Counter(), slots=0)
        self.states['202']['neighbors'] = ('203', '193')

    def faction(self, *tags):
        for tag in tags: self.countries[tag]['faction'] = tags[0]

    def test(self, nodes, current='MKN', previous=None):
        for key, value, op in nodes or []:
            c = self.data(current)
            if key in {'is_ally_with', 'is_in_faction_with'}:
                target = self.scope(value, current, previous) or value
                answer = target in c['allies'] or (c['faction'] is not None and c['faction'] == self.countries[target]['faction'])
            elif key == 'is_ai': answer = c['ai'] == (value == 'yes')
            elif key == 'original_tag': answer = current == value
            elif key == 'has_government': answer = c['government'] == value
            elif key == 'has_focus_tree': answer = c['tree'] == value
            elif key == 'has_game_rule': answer = self.rule == one(value, 'option')
            elif key == 'is_historical_focus_on': answer = self.historical == (value == 'yes')
            elif key == 'has_capitulated': answer = c['capitulated'] == (value == 'yes')
            elif key == 'war_length_with':
                target=one(value,'tag');v,op=next((v,o) for k,v,o in value if k=='months')
                answer=self.compare(c.get('war_months',{}).get(target,0),float(v),op)
            elif key == 'has_full_control_of_state': answer = self.states[value]['controller'] == current and not self.states[value].get('contested', False)
            elif key == 'is_capital': answer = any(country['exists'] and country['capital'] == current for country in self.countries.values()) == (value == 'yes')
            elif key == 'has_country_leader_with_trait': answer = value in c['traits']
            elif key == 'amount_research_slots': answer = self.compare(c['slots'], float(value), op)
            elif key in {'communism', 'democratic', 'fascism', 'neutrality'}: answer = self.compare(c['popularity'][key], float(value), op)
            else: answer = super().test([(key, value, op)], current, previous)
            if not answer: return False
        return True

    def apply(self, nodes, current='MKN', previous=None):
        matched = False
        for key, value, op in nodes:
            c = self.data(current)
            if key in {'if', 'else_if'}:
                if key == 'if': matched = False
                if not matched and self.test(one(value, 'limit'), current, previous):
                    self.apply([n for n in value if n[0] != 'limit'], current, previous); matched = True
            elif key == 'else':
                if not matched: self.apply(value, current, previous)
                matched = True
            elif key == 'random_list':
                branches = [v for k,v,o in value if k and k.isdigit()]
                self.apply(branches[self.pick], current, previous)
            elif key in {'add_relation_rule_override', 'remove_relation_rule_override'}:
                rule = one(value, 'trigger')
                (c['rules'].add if key == 'add_relation_rule_override' else c['rules'].discard)(rule)
            elif key == 'mark_focus_tree_layout_dirty': self.layout += 1
            elif key == 'set_capital': c['capital'] = one(value, 'state')
            elif key == 'add_dynamic_modifier': c.setdefault('dynamic', set()).add(one(value, 'modifier'))
            elif key in {'set_rule','clear_rule'}:
                for rule,state,o in value:
                    (c['rules'].add if key=='set_rule' else c['rules'].discard)(rule)
            elif key == 'add_political_power': c['pp'] += float(value)
            elif key == 'add_popularity': c['popularity'][one(value, 'ideology')] += float(one(value, 'popularity'))
            elif key == 'add_manpower': c['manpower'] = c.get('manpower', 0) + int(value)
            elif key == 'add_research_slot': c['slots'] += int(value)
            elif key == 'set_research_slots': c['slots'] = int(value)
            elif key == 'add_tech_bonus': c['tech_bonus'] = c.get('tech_bonus', 0) + int(one(value, 'uses'))
            elif key == 'add_extra_state_shared_building_slots': c['slots'] += int(value)
            elif key == 'add_building_construction': c['buildings'][one(value, 'type')] += int(one(value, 'level'))
            elif key == 'set_country_leader_portrait': c['portraits'][one(value, 'ideology')] = one(value, 'portrait')
            elif key == 'remove_from_faction': self.countries[value]['faction'] = None
            else: super().apply([(key, value, op)], current, previous)

    def protected(self, actor, target):
        self.root, self.froms = actor, (target, target, target)
        return self.test(self.triggers['MKN_protected_diplomatic_relation'], actor)


def validate_ukraine(root, game, check, localized):
    cases = 0
    events = {one(e, 'id'): e for p in ['events/nww_ukr_diplomacy.txt', 'events/MKN_events.txt'] for e in values(read(root/p), 'country_event')}
    fs = {one(f, 'id'): f for f in tree_focuses(one(read(root/'common/national_focus/MKN.txt'), 'focus_tree'), root/'common/national_focus')}
    integration = json.loads((root/'docs/MKN_ukraine_integration.json').read_text())
    ai_plans = read(root/'common/ai_strategy_plans/MKN_historical.txt')
    def weight(w, node, current='MKN'):
        result = float(one(node, 'factor', one(node, 'base', '0')))
        for m in values(node, 'modifier'):
            if w.test([x for x in m if x[0] not in {'factor', 'add'}], current):
                result = (result + float(one(m, 'add', '0'))) * float(one(m, 'factor', '1'))
        return result
    # Every actor/target direction, explicit alliances, shared blocs, and pact promises.
    for actor, target in [('UKR','MKN'), ('MKN','UKR'), ('SOV','MKN'), ('MKN','SOV')]:
        for allied in (False, True):
            w = World()
            if allied: w.faction('SOV', 'UKR', 'MKN')
            check(w.protected(actor, target) == allied, f'{actor}->{target}: native allied declaration guard')
            w.root = 'MKN'
            if allied:
                w.countries['MKN']['flags'].update(mkn_ukr_war_pending=-1, mkn_frontier_conflict_active=-1)
                w.run('mkn_ukr_conclude_total_war')
                check(not w.declarations, 'MKN: stale escalation declares on an ally')
                w.run('MKN_close_allied_frontier')
                check('mkn_ukr_war_pending' not in w.countries['MKN']['flags'] and not w.countries['MKN']['missions'], 'MKN: allied frontier stays armed')
            cases += 1
    for flag_owner, flag in [('MKN','MKN_equal_autonomy'), ('SOV','NWW_SOV_MKN_settlement')]:
        w = World(); w.countries[flag_owner]['flags'][flag] = -1
        check(w.protected('SOV','MKN') and w.protected('MKN','SOV'), 'MKN: an accepted settlement can be broken by a declaration')
        refusal = values(events['mkn_crisis.40'], 'option')[1]
        w.root = 'SOV'; w.faction('SOV','MKN')
        check(not w.test(one(refusal, 'trigger'), 'SOV'), 'MKN: accepted autonomy still offers a betrayal')
        w.apply([n for n in refusal if n[0] not in {'name','trigger','ai_chance'}], 'SOV')
        check(not w.declarations and w.countries['MKN']['faction'] == 'SOV', 'MKN: queued betrayal ignores accepted autonomy')
        cases += 1
    for historic in (False, True):
        w = World(); w.historical = historic
        yes, no = values(events['ukr.50'], 'option')
        a, b = weight(w, one(yes, 'ai_chance')), weight(w, one(no, 'ai_chance'))
        check(abs(a/(a+b)-(0.01 if historic else 0.5)) < 1e-9, 'MKN: Ukrainian proposal AI acceptance')
        w.apply([n for n in yes if n[0] not in {'name','trigger','ai_chance'}])
        check(w.states['192']['owner'] == 'MKN' and w.states['203']['owner'] == 'UKR', 'MKN: agreement transfers Cherkasy instead of Odesa')
        refusal = values(events['mkn_crisis.40'], 'option')[1]
        check((weight(w, one(refusal, 'ai_chance'), 'SOV') == 0) == historic, 'SOV: historical AI can betray MKN at the plenum')
        cases += 1
    w = World(); w.historical = False; w.rule = 'HISTORICAL'
    refusal = values(events['mkn_crisis.40'], 'option')[1]
    check(weight(w, one(refusal, 'ai_chance'), 'SOV') == 0, 'MKN: explicit historical rule does not secure the plenum')
    yes = values(events['ukr.50'], 'option')[0]
    for owner, controller in [('SOV','SOV'), ('UKR','SOV')]:
        w = World(); w.states['192']['owner'], w.states['192']['controller'] = owner, controller
        before = deepcopy(w.states)
        w.apply([n for n in yes if n[0] not in {'name','trigger','ai_chance'}])
        check(w.states == before and 'UKR_MKN_border_settled' not in w.countries['MKN']['flags'], 'MKN: stale Odessa acceptance transfers foreign territory')
        cases += 1
    hooks = one(read(root/'common/on_actions/MKN_diplomacy_on_actions.txt'), 'on_actions')
    for actor in ('MKN','UKR','SOV'):
        w = World(); w.apply(w.effects['MKN_install_allied_war_guard'], actor); w.apply(w.effects['MKN_install_allied_war_guard'], actor)
        check(not any(k in {'add_relation_rule_override','remove_relation_rule_override'} for k,v,o in walk(w.effects['MKN_install_allied_war_guard'])), actor+': unsupported declaration relation override remains')
        startup = one(one(hooks,'on_startup'),'effect')
        check(any(k == 'MKN_install_allied_war_guard' for k,v,o in walk(one(startup,actor))), actor + ': protection is not installed on load')
        cases += 1
    # Pin one route per campaign; explicit rules override the global checkbox.
    campaigns = one(read(root/'common/decisions/nww_mkn_mandate.txt'), 'MKN_public_mandate')
    route_entries = dict(fascism='MKN_military_takes_charge', democratic='MKN_triumph_of_free_soviets', neutrality='MKN_peasant_delegates', communism='MKN_emergency_revkom')
    for historic, rule in product((False, True), ('DEFAULT','HISTORICAL','RANDOM','FASCISM','DEMOCRATIC','NEUTRALITY','COMMUNISM')):
        random_mode = rule in {'RANDOM', 'DEFAULT'}
        for pick in (range(4) if random_mode else [0]):
            w = World(); w.historical, w.rule, w.pick = historic, rule, pick
            w.run('MKN_initialize_ai_route'); flags = w.countries['MKN']['flags']
            selected = [i for i in route_entries if 'MKN_ai_route_'+i in flags]
            expected = (list(route_entries)[pick] if random_mode else (rule.lower() if rule.lower() in route_entries else 'communism'))
            check(selected == [expected], 'MKN: AI route randomization or explicit rule precedence')
            w.pick = (pick+1)%4; w.run('MKN_initialize_ai_route')
            check([i for i in route_entries if 'MKN_ai_route_'+i in flags] == selected, 'MKN: daily repair rerolls political route')
            c = w.countries['MKN']; c['popularity'] = {i: 0.1 for i in route_entries}
            weights = {i: weight(w, one(one(campaigns,'MKN_campaign_'+i), 'ai_will_do')) for i in route_entries}
            check(weights[expected] > 0 and all(v == 0 for i,v in weights.items() if i != expected), 'MKN: AI campaigns for a different political mandate')
            plan = next(p for k,p,o in ai_plans if one(one(p,'enable'),'has_country_flag') == 'MKN_ai_route_'+expected)
            for other, entry in route_entries.items():
                if other != expected: check(one(one(plan,'focus_factors'),entry) == '0', 'MKN: plan allows an unrelated political entry')
            check(any(k=='NOT' and (expected,'0.40','<') in v for k,v,o in walk(one(fs[route_entries[expected]],'available'))), 'MKN: initial mandate gates missing')
            cases += 1
    # Previously completed real political choices outrank a new rule on old saves.
    for ideology, fid in route_entries.items():
        w = World(); w.countries['MKN']['focuses'].add(fid); w.run('MKN_initialize_ai_route')
        check('MKN_ai_route_'+ideology in w.countries['MKN']['flags'], 'MKN: old-save AI ignores actual completed path'); cases += 1
    # Every starting Ukrainian state matters, with separate ownership/control tests.
    starting = {one(one(read(p),'state'),'id') for p in (root/'history/states').glob('*.txt') if one(one(one(read(p),'state'),'history',[]),'owner') == 'UKR'}
    check(starting == {str(s) for s in integration['states']}, 'MKN: integration list differs from actual starting Ukraine')
    def won():
        w = World(); w.countries['UKR']['exists'] = False
        for s in integration['states']: w.states[str(s)]['owner'] = w.states[str(s)]['controller'] = 'MKN'
        return w
    for sid, attr in product(integration['states'], ('owner','controller')):
        w = won(); w.states[str(sid)][attr] = 'SOV'; w.run('MKN_observe_ukrainian_integration')
        check('MKN_ukraine_integration_unlocked' not in w.countries['MKN']['flags'], 'MKN: integration opens without whole-country ownership/control'); cases += 1
    w = won(); w.countries['UKR']['exists'] = True; w.run('MKN_observe_ukrainian_integration')
    check(not w.layout, 'MKN: annexation objective opens while UKR survives')
    w = won(); w.countries['MKN']['wars'].add('SOV'); w.run('MKN_observe_ukrainian_integration')
    check(not w.layout, 'MKN: reconstruction opens during war')
    w = won(); before = deepcopy(w.states); w.run('MKN_observe_ukrainian_integration'); w.run('MKN_observe_ukrainian_integration')
    check(w.layout == 1 and len(w.events) == 1 and before == w.states, 'MKN: unlock repeats or annexes territory')
    # Moving the capital needs only the former Ukrainian capital, not the
    # entire integration programme; invalid queued actions must do nothing.
    category = one(read(root/'common/decisions/MKN_ukraine_integration_decisions.txt'), 'MKN_ukrainian_administration_category')
    move = one(category, 'MKN_move_capital_to_kyiv')
    check(one(move, 'cost') == '50' and one(move, 'fire_only_once') == 'yes', 'MKN: capital decision price/one-time contract')
    localized('MKN_ukrainian_administration_category', 'MKN capital')
    localized('MKN_ukrainian_administration_category_desc', 'MKN capital')
    localized('MKN_move_capital_to_kyiv', 'MKN capital')
    localized('MKN_move_capital_to_kyiv_desc', 'MKN capital')
    for condition in ('valid', 'ukr_survives', 'foreign_owner', 'occupied', 'contested', 'already_capital', 'capitulated'):
        trial = World(); trial.countries['UKR']['exists'] = False
        trial.states['202']['owner'] = trial.states['202']['controller'] = 'MKN'
        if condition == 'ukr_survives': trial.countries['UKR']['exists'] = True
        elif condition == 'foreign_owner': trial.states['202']['owner'] = 'SOV'
        elif condition == 'occupied': trial.states['202']['controller'] = 'SOV'
        elif condition == 'contested': trial.states['202']['contested'] = True
        elif condition == 'already_capital': trial.countries['MKN']['capital'] = '202'
        elif condition == 'capitulated': trial.countries['MKN']['capitulated'] = True
        check(trial.test(one(move, 'available')) == (condition == 'valid'), 'MKN capital: incorrect availability ' + condition)
        old_capital, land = trial.countries['MKN']['capital'], deepcopy(trial.states)
        trial.apply(one(move, 'complete_effect'))
        check(trial.countries['MKN']['capital'] == ('202' if condition == 'valid' else old_capital), 'MKN capital: invalid queued relocation ' + condition)
        check(trial.states == land, 'MKN capital: relocation changes land or cores')
        if condition == 'valid':
            check(not trial.test(one(move, 'visible')), 'MKN capital: relocation can repeat')
            trial.run('nww_mkn_rebuild_industry')
            check(trial.countries['MKN']['capital'] == '202', 'MKN capital: economy repair restores the old capital')
        cases += 1
    w.countries['MKN']['focuses'].update({'MKN_communal_research_network','MKN_free_science_network'})
    w.countries['MKN']['slots'] = 5
    for fid in integration['focuses']:
        f = fs[fid]; localized(fid, fid); localized(fid+'_desc', fid)
        check(w.test(one(f,'available')), fid + ': full control does not unlock integration')
        w.apply(one(f,'completion_reward')); w.countries['MKN']['focuses'].add(fid)
    check(all('MKN' in w.states[str(s)]['cores'] for s in integration['states']), 'MKN: regional charters miss Ukrainian cores')
    check(w.states['500']['owner'] == 'SOV' and w.states['500']['cores'] == {'SOV'}, 'MKN: integration takes Soviet land')
    physical = deepcopy((w.states, w.countries['MKN']['slots'], w.countries['MKN']['pp']))
    w.run('nww_mkn_rebuild_industry'); first = dict(w.countries['MKN']['variables']); w.run('nww_mkn_rebuild_industry')
    check(first == w.countries['MKN']['variables'] and physical == (w.states, w.countries['MKN']['slots'], w.countries['MKN']['pp']), 'MKN: integration repair stacks bonuses or repeats physical rewards')
    research = one(fs['MKN_kyiv_scientific_exchange'], 'completion_reward')
    for slots in (5,6,7):
        w = won(); w.countries['MKN']['slots'] = slots; w.apply(research)
        check(w.countries['MKN']['slots'] == (slots+1 if slots<6 else slots), 'MKN: integration research exceeds six slots')
        check(w.countries['MKN'].get('tech_bonus',0) == (2 if slots>=6 else 0), 'MKN: missing capped research alternative'); cases += 1
    # Native portraits must contain visible artwork, with exact advisor clearance.
    assets = json.loads((root/'docs/art/mkn_successors/assets.json').read_text())
    for asset in assets:
        p = root/asset['texture']
        check(hashlib.sha256(p.read_bytes()).hexdigest() == asset['export_sha256'], 'MKN: portrait manifest hash mismatch')
        with Image.open(p) as im:
            check(list(im.size) == asset['size'] and max(ImageStat.Stat(im.convert('RGB')).mean) > 15, 'MKN: black/invalid successor portrait')
            if 'alpha_bounds' in asset: check(list(im.convert('RGBA').getchannel('A').getbbox()) == asset['alpha_bounds'], 'MKN: advisor portrait lacks bottom clearance')
    effects = read(root/'common/scripted_effects/MKN_effects.txt')
    check(one(one(one(effects,'MKN_install_tsebriy'),'create_country_leader'),'picture') == 'GFX_Portrait_MKN_osyp_tsebriy', 'MKN: Tsebriy still uses collective portrait')
    # Repair replaces the known successor's art, never the monarch.
    w = World(); w.countries['MKN']['flags']['MKN_overhaul_v4'] = -1; w.countries['MKN']['traits'].add('mkn_syndicalist_organizer')
    w.run('MKN_repair_overhaul')
    check(w.countries['MKN']['portraits']['communism'] == 'GFX_Portrait_MKN_osyp_tsebriy' and w.countries['MKN']['portraits']['neutrality'] == 'GFX_Portrait_makhno', 'MKN: portrait repair changes the monarch')
    for k, plan, o in ai_plans:
        for _, fid, _ in one(plan,'ai_national_focuses'): check(fid in fs, k + ': unknown planned focus ' + fid)
    print(f'PASS: MKN Ukraine: {cases} source-script cases; allied war guards, Odessa, 1% historical truce, four AI routes, eight integration focuses and visible portraits')


if __name__ == '__main__':
    p=argparse.ArgumentParser();p.add_argument('--game',type=Path,required=True);a=p.parse_args();errors=[]
    def check(ok,msg):
        if not ok: errors.append(msg)
    locales={l:{k for p in (ROOT/'localisation').rglob(f'*l_{l}.yml') for k in re.findall(r'^\s+([\w.]+):',p.read_text(encoding='utf-8-sig'),re.M)} for l in ('russian','english')}
    def localized(key,context):
        for lang, keys in locales.items(): check(key in keys, f'{context}: missing {lang} {key}')
    validate_ukraine(ROOT,a.game,check,localized)
    for e in errors: print('ERROR:',e)
    raise SystemExit(bool(errors))
