"""Check GER's political content and replay its script lifecycle without running HOI4.

This small interpreter covers only the tested GER effects. Unknown operations fail;
it is not a substitute for a new campaign, event tooltips or an engine log.
"""
import argparse
from copy import deepcopy
from pathlib import Path
import re

from PIL import Image
from hoi4_script import read, one, values, walk, tree_focuses, engine_script_errors


class Scenario:
    def __init__(self, effects, events):
        self.effects, self.events = effects, events
        self.triggers = {k:v for k,v,o in read(Path(__file__).resolve().parents[1]/'common/scripted_triggers/GER_triggers.txt')}
        self.date, self.dlc, self.player, self.from_country = '1936.1.1', True, 'GER', 'GER'
        self.ai,self.historical=False,True
        self.flag_timers={}
        self.triggers.update({k:v for k,v,o in read(Path(__file__).resolve().parents[1]/'common/scripted_triggers/GER_pacing_triggers.txt')})
        self.triggers.update({k:v for k,v,o in read(Path(__file__).resolve().parents[1]/'common/scripted_triggers/GER_campaign_safety_triggers.txt')})
        self.triggers.update({k:v for k,v,o in read(Path(__file__).resolve().parents[1]/'common/scripted_triggers/GER_lategame_triggers.txt')})
        self.countries = {tag: dict(exists=True, subject=None, autonomy=None, flags=set(),
            focuses=set(), wars=set(), allies=set(), goals=set(), government='neutrality',
            balance=None, rules=set(), neutrality=0.65, democratic=0.20, fascism=0.10,
            communism=0.05, pp=200, leader='GER_wilhelm_ii', traits={'ger_aging_monarch'},
            original=tag, tree='GER_focus' if tag=='GER' else None, civil_war=False,
            capitulated=False, faction=None, factories=0, ideas=set(), guarantees=set(),
            variables={}, parties={}, dynamic_modifiers=set(), missions=set())
            for tag in ('GER','LTB','POL','AUS','MKN','UKR','SOV','FRA','ENG','CZE')}
        self.character_owner = {name:'GER' for name in ('GER_wilhelm_ii','GER_wilhelm_iii',
            'GER_hans_vogel','GER_wilhelm_pieck','GER_ernst_thalmann','GER_alfred_hugenberg')}
        self.queue, self.news, self.fired = [], [], set()

    @staticmethod
    def compare(actual, expected, op):
        return {'=': actual == expected, '<': actual < expected, '>': actual > expected}[op]

    def target(self, token, actor, root, stack=()):
        if token == 'ROOT': return root
        if token == 'FROM': return self.from_country
        if token == 'PREV': return stack[-1]
        if token == 'PREV.PREV': return stack[-2]
        return token

    def condition(self, node, actor='GER', root=None, stack=()):
        root = root or actor
        s, results = self.countries[actor], []
        for key,value,op in node:
            if key == 'NOT': result = not self.condition(value,actor,root,stack)
            elif key in ('OR','AND'):
                parts = [self.condition([e],actor,root,stack) for e in value]
                result = any(parts) if key=='OR' else all(parts)
            elif key == 'custom_trigger_tooltip':
                result = self.condition([e for e in value if e[0]!='tooltip'],actor,root,stack)
            elif key in self.triggers: result = self.condition(self.triggers[key],actor,root,stack)
            elif key in self.countries or key in ('ROOT','FROM','PREV'):
                result = self.condition(value,self.target(key,actor,root,stack),root,(*stack,actor))
            elif key == 'any_other_country':
                result = any(self.condition(value,tag,root,(*stack,actor)) for tag,state in self.countries.items() if tag!=actor and state['exists'])
            elif key == 'owns_state': result = value in s.get('owned_states',set())
            elif key == 'check_variable' and one(value,'num_owned_controlled_states') is not None:
                entry = next(e for e in value if e[0]=='num_owned_controlled_states')
                result = self.compare(s.get('controlled_states',2),int(entry[1]),entry[2])
            elif key == 'any_enemy_country':
                result = any(self.condition(value,tag,root,(*stack,actor)) for tag in s['wars'])
            elif key == 'date':
                as_date = lambda x: tuple(map(int,x.split('.')))
                result = self.compare(as_date(self.date),as_date(value),op)
            elif key=='is_ai':result=self.ai==(value=='yes')
            elif key=='is_historical_focus_on':result=self.historical==(value=='yes')
            elif key=='is_major':result=s.get('major',False)==(value=='yes')
            elif key=='has_guaranteed':result=self.target(value,actor,root,stack) in s.get('guarantees',set())
            elif key=='strength_ratio':
                operand=next(n for n in value if n[0]=='ratio');other=self.countries[self.target(one(value,'tag'),actor,root,stack)]
                own_strength=s.get('strength',100 if actor=='GER' else 30)
                enemy_strength=other.get('strength',100 if self.target(one(value,'tag'),actor,root,stack)=='GER' else 30)
                result=self.compare(own_strength/max(1,enemy_strength),float(operand[1]),operand[2])
            elif key=='surrender_progress':result=self.compare(s.get('surrender',0),float(value),op)
            elif key in ('has_stability','has_war_support'):result=self.compare(s.get('stability' if key=='has_stability' else 'war_support',0.5),float(value),op)
            elif key=='has_war_with_major':result=any(self.countries[t].get('major',False) for t in s['wars'])==(value=='yes')
            elif key in ('always','exists','is_subject','has_dlc','has_civil_war','has_capitulated','has_war','is_in_faction','is_faction_leader'):
                actual = {'always':True,'exists':s['exists'],'is_subject':s['subject'] is not None,
                    'has_dlc':self.dlc,'has_civil_war':s['civil_war'],'has_capitulated':s['capitulated'],
                    'has_war':bool(s['wars']),'is_in_faction':s['faction'] is not None,
                    'is_faction_leader':s['faction']==actor}[key]
                result = actual if key=='has_dlc' else actual==(value=='yes')
            elif key in ('tag','original_tag'): result = (actor if key=='tag' else s['original'])==value
            elif key == 'has_government': result = s['government']==value
            elif key == 'has_focus_tree': result = s['tree']==value
            elif key == 'has_country_flag': result = value in s['flags']
            elif key == 'has_completed_focus': result = value in s['focuses']
            elif key == 'has_power_balance': result = s['balance'] is not None
            elif key == 'power_balance_value':
                _,target,compare = next(e for e in value if e[0]=='value')
                result = s['balance'] is not None and self.compare(s['balance'],float(target),compare)
            elif key in ('neutrality','democratic','fascism','communism'): result = self.compare(s[key],float(value),op)
            elif key in ('has_war_with','is_ally_with','has_wargoal_against','is_in_faction_with'):
                target = self.target(value,actor,root,stack)
                same_faction = s['faction'] is not None and s['faction']==self.countries[target]['faction']
                field = {'has_war_with':'wars','is_ally_with':'allies','has_wargoal_against':'goals','is_in_faction_with':'allies'}[key]
                result = same_faction if key=='is_in_faction_with' else target in s[field] or (key=='is_ally_with' and same_faction)
            elif key == 'is_subject_of': result = s['subject']==self.target(value,actor,root,stack)
            elif key == 'has_autonomy_state': result = s['autonomy']==value
            elif key == 'has_character': result = self.character_owner.get(value)==actor
            elif key == 'has_dynamic_modifier': result = one(value,'modifier') in s['dynamic_modifiers']
            elif key == 'has_idea': result = value in s['ideas']
            elif key == 'has_active_mission': result = value in s['missions']
            else: raise AssertionError(f'Unsupported GER scenario trigger {key}')
            results.append(result)
        return all(results)

    def apply(self, node, actor='GER', root=None, stack=(), character=None):
        root = root or actor
        s, branch_taken = self.countries[actor], False
        for key,value,op in node:
            if key in ('if','else_if','else'):
                if key=='if': branch_taken=False
                if not branch_taken and (key=='else' or self.condition(one(value,'limit',[]),actor,root,stack)):
                    self.apply([e for e in value if e[0]!='limit'],actor,root,stack,character)
                    branch_taken=True
            elif key in self.countries or key in ('ROOT','FROM','PREV'):
                self.apply(value,self.target(key,actor,root,stack),root,(*stack,actor))
            elif key in self.character_owner:
                self.apply(value,actor,root,(*stack,actor),key)
            elif key in self.effects: self.apply(self.effects[key],actor,root,stack)
            elif key == 'hidden_effect': self.apply(value,actor,root,stack,character)
            elif key in ('set_country_flag','clr_country_flag','complete_national_focus'):
                field = 'focuses' if key=='complete_national_focus' else 'flags'
                flag=one(value,'flag') if isinstance(value,list) else value
                (s[field].discard if key=='clr_country_flag' else s[field].add)(flag)
                if isinstance(value,list):self.flag_timers[(actor,flag)]=int(one(value,'days'))
                if key=='clr_country_flag':self.flag_timers.pop((actor,flag),None)
            elif key == 'set_power_balance': s['balance']=float(one(value,'set_value','0'))
            elif key == 'remove_power_balance': s['balance']=None
            elif key == 'add_power_balance_value': s['balance']=round(max(-1,min(1,s['balance']+float(one(value,'value')))),6)
            elif key == 'add_relation_rule_override': s['rules'].add(('trigger',one(value,'trigger')) if one(value,'trigger') else one(value,'target'))
            elif key == 'remove_relation_rule_override': s['rules'].discard(('trigger',one(value,'trigger')) if one(value,'trigger') else one(value,'target'))
            elif key == 'create_wargoal': s['goals'].add(one(value,'target'))
            elif key == 'set_autonomy':
                target=self.target(one(value,'target'),actor,root,stack)
                self.countries[target]['subject']=None if one(value,'autonomy_state')=='autonomy_free' else actor
                self.countries[target]['autonomy']=one(value,'autonomy_state')
            elif key == 'country_event': self.queue.append((actor,one(value,'id')))
            elif key == 'news_event': self.news.append(one(value,'id'))
            elif key == 'remove_country_leader_trait': s['traits'].discard(value)
            elif key == 'retire_character':
                if s['leader']==value: s['leader']=None
            elif key == 'add_country_leader_role': s['leader']=character
            elif key == 'promote_character': s['leader']=character
            elif key == 'set_politics': s['government']=one(value,'ruling_party')
            elif key == 'add_political_power': s['pp']+=float(value)
            elif key == 'add_popularity': s[one(value,'ideology')]+=float(one(value,'popularity'))
            elif key == 'load_focus_tree':
                s['tree']=one(value,'tree')
                if one(value,'copy_completed_from'):
                    s['focuses']=deepcopy(self.countries[self.target(one(value,'copy_completed_from'),actor,root,stack)]['focuses'])
            elif key == 'start_civil_war':
                child='D01'
                self.countries[child]=deepcopy(s)
                rebel=self.countries[child]
                rebel.update(government=one(value,'ideology'),faction=None,wars={actor},civil_war=True)
                # The engine transfers the party leader; Thalmann is explicitly transferred in script.
                self.character_owner['GER_wilhelm_pieck']=child
                s['wars'].add(child);s['civil_war']=True
                config={'ideology','ruling_party','size','army_ratio','navy_ratio','air_ratio','keep_all_characters','keep_political_leader'}
                self.apply([e for e in value if e[0] not in config],child,root,(*stack,actor))
            elif key == 'change_tag_from':
                if self.player==self.target(value,actor,root,stack): self.player=actor
            elif key == 'set_nationality': self.character_owner[character]=self.target(value,actor,root,stack)
            elif key == 'recruit_character': self.character_owner[value]=actor
            elif key == 'set_party_name': s['parties'][one(value,'ideology')]=one(value,'name')
            elif key == 'set_cosmetic_tag': s['cosmetic']=value
            elif key == 'create_faction_from_template': s['faction']=actor
            elif key == 'add_to_faction': self.countries[self.target(value,actor,root,stack)]['faction']=s['faction']
            elif key == 'leave_faction': s['faction']=None
            elif key == 'annex_country': self.countries[self.target(one(value,'target'),actor,root,stack)]['exists']=False
            elif key == 'add_offsite_building': s['factories']+=int(one(value,'level'))
            elif key == 'give_guarantee': s['guarantees'].add(value)
            elif key == 'add_ideas': s['ideas'].add(value)
            elif key == 'remove_ideas': s['ideas'].discard(value)
            elif key == 'swap_ideas':
                s['ideas'].discard(one(value,'remove_idea'));s['ideas'].add(one(value,'add_idea'))
            elif key == 'remove_dynamic_modifier': s['dynamic_modifiers'].discard(one(value,'modifier'))
            elif key == 'remove_mission': s['missions'].discard(value)
            elif key == 'set_variable': s['variables'].update({k:float(v) for k,v,o in value})
            elif key in ('custom_effect_tooltip','army_experience','add_stability','add_war_support',
                         'remove_advisor_role','remove_country_leader_role','set_portraits',
                         'set_faction_name','set_faction_manifest','set_faction_rule'):
                pass  # Native UI/numeric operations validated statically, not engine-simulated.
            else: raise AssertionError(f'Unsupported GER scenario effect {key}')

    def event(self,eid,actor='GER',option=None,sender='GER'):
        event=self.events[eid]
        previous=self.from_country;self.from_country=sender
        try:
            if (actor,eid) in self.fired and one(event,'fire_only_once')=='yes': return False
            if not self.condition(one(event,'trigger',[]),actor): return False
            self.fired.add((actor,eid))
            self.apply(one(event,'immediate',[]),actor)
            if option is not None:
                chosen=values(event,'option')[option]
                if not self.condition(one(chosen,'trigger',[]),actor): return False
                self.apply([e for e in chosen if e[0] not in ('name','ai_chance','trigger')],actor)
            return True
        finally: self.from_country=previous


def validate_germany(root, game, check):
    focuses_doc = read(root / 'common/national_focus/GER_political.txt')
    political = {one(f, 'id'): f for f in values(focuses_doc, 'shared_focus')}
    tree = one(read(root / 'common/national_focus/GER_focuses.txt'), 'focus_tree')
    fs = {one(f, 'id'): f for f in tree_focuses(tree, root / 'common/national_focus')}
    effects = {k:v for filename in ('GER_effects.txt','GER_lategame_effects.txt') for k,v,op in read(root/'common/scripted_effects'/filename)}
    events = {one(v, 'id'): v for k, v, op in read(root / 'events/GER_events.txt') if k.endswith('_event')}
    decisions = one(read(root / 'common/decisions/GER_bop_decisions.txt'), 'GER_bop_decisions_category')
    history = read(root / 'history/countries/GER - Germany.txt')
    on_actions = one(read(root / 'common/on_actions/GER_on_actions.txt'), 'on_actions')
    check(len(political) == 40 and len(fs) == 76, 'GER: expected forty political and thirty-six industrial/military/intelligence focuses')
    check(set(political) <= fs.keys() and values(tree, 'shared_focus') == ['GER_the_gilded_colossus'],
          'GER: shared political root must import the entire branch exactly once')
    rows = {}
    for fid, focus in fs.items():
        x, y = int(one(focus, 'x')), int(one(focus, 'y'))
        rows.setdefault(y, []).append(x)
        for parent in [p for group in values(focus, 'prerequisite') for p in values(group, 'focus')]:
            check(parent in fs and int(one(fs[parent], 'y')) < y, f'{fid}: invalid parent {parent}')
        check(float(one(focus, 'cost')) > 0 or (fid == 'GER_end_of_an_era' and one(one(focus, 'available'), 'always') == 'no'),
              f'{fid}: only the event-completed focus may have zero cost')
    check(all(b-a >= 2 for row in rows.values() for a,b in zip(sorted(row), sorted(row)[1:])), 'GER: overlapping focus positions')
    check(int(one(one(tree, 'continuous_focus_position'), 'y')) > max(rows)*130+800, 'GER: continuous panel overlaps the tree')
    check(one(tree, 'id') == 'GER_focus', 'GER: compatibility tree ID changed')
    native = read(game/'common/national_focus/germany.txt')
    native_ids = {one(f,'id') for t in values(native,'focus_tree') for f in values(t,'focus')}
    native_ids |= {one(f,'id') for f in values(native,'shared_focus')}
    compatibility = read(root/'common/national_focus/GER_native_compatibility.txt')
    hidden = {one(f,'id'): f for f in values(compatibility,'shared_focus')}
    check(set(hidden) == native_ids - fs.keys(), 'GER: native registry lost IDs or collected nested event/province IDs')
    check(all(one(one(f,'allow_branch'),'always') == 'no' and one(f,'completion_reward') == [] for f in hidden.values()),
          'GER: detached native focuses can appear or grant rewards')
    check(not read(root/'common/national_focus/germany.txt'), 'GER: native tree still competes with NWW definitions')

    docs = {kind: set(re.findall(r'^## (\w+)', (game / f'documentation/{kind}_documentation.md').read_text(), re.M))
            for kind in ('effects', 'triggers', 'modifiers')}
    docs['modifiers'] |= {'production_speed_'+kind+'_factor' for kind,node,o in one(read(game/'common/buildings/00_buildings.txt'),'buildings')}
    generated_modifiers = {'political_advisor_cost_factor', 'trade_laws_cost_factor'}
    # These generated modifiers are verified against installed DLC definitions.
    for name in generated_modifiers:
        check(name in (game / 'common/dynamic_modifiers/TAOG_dynamic_modifiers.txt').read_text(),
              f'GER: generated modifier {name} absent from installed DLC')
    for kind, tokens in {
        'effects': ('set_power_balance', 'add_power_balance_value', 'add_relation_rule_override',
                    'remove_relation_rule_override', 'add_country_leader_role', 'remove_advisor_role', 'set_autonomy'),
        'triggers': ('has_power_balance', 'power_balance_value', 'has_autonomy_state'),
    }.items():
        check(set(tokens) <= docs[kind], f'GER: undocumented {kind} tokens')
    country_ideas = one(one(read(root / 'common/ideas/GER_ideas.txt'), 'ideas'), 'country')
    expected_ideas = {
        'GER_imperial_overstretch': {'political_power_gain': -0.25, 'consumer_goods_factor': 0.30, 'war_support_factor': -0.30, 'army_org_factor': -0.20, 'training_time_army_factor': 0.40, 'planning_speed': -0.30},
        'GER_master_of_mitteleuropa': {'trade_laws_cost_factor': -0.20, 'master_ideology_drift': 0.05},
        'GER_prussian_martial_spirit': {'army_org_factor': 0.10, 'planning_speed': 0.15},
        'GER_gott_mit_uns': {'army_core_defence_factor': 0.15, 'army_attack_factor': 0.10, 'breakthrough_factor': 0.10},
        'GER_constitutional_monarchy': {'stability_factor': 0.15, 'political_power_gain': 0.20},
        'GER_arsenal_of_democracy': {'stability_factor': 0.15, 'political_power_gain': 0.20, 'industrial_capacity_factory': 0.20, 'army_defence_factor': 0.10},
        'GER_the_new_reich': {'army_attack_factor': 0.15, 'breakthrough_factor': 0.20, 'army_speed_factor': 0.10},
        'GER_workers_militias': {'conscription': 0.05, 'army_morale_factor': 0.10},
    }
    for token, expected in expected_ideas.items():
        actual = {k: float(v) for k,v,o in one(one(country_ideas,token),'modifier')}
        check(actual == expected, f'{token}: requested spirit parameters changed')
    aging = one(one(read(root/'common/country_leader/GER_traits.txt'),'leader_traits'),'ger_aging_monarch')
    check(one(aging,'stability_factor') == '-0.10' and one(aging,'political_advisor_cost_factor') == '0.25',
          'GER: aging monarch trait has incorrect effects')
    for filename in ('common/ideas/GER_ideas.txt', 'common/bop/GER_bop.txt', 'common/country_leader/GER_traits.txt'):
        for key, value, op in walk(read(root / filename)):
            if key == 'modifier' or (filename.endswith('GER_traits.txt') and key == 'ger_aging_monarch'):
                for modifier, v, _ in value:
                    if modifier not in ('random',):
                        check(modifier in docs['modifiers'] | generated_modifiers, f'{filename}: unknown modifier {modifier}')
    starting = {v for k,v,op in walk(history) if k is None and isinstance(v,str)}
    check({'GER_imperial_overstretch','GER_master_of_mitteleuropa','GER_prussian_martial_spirit'} <= starting,
          'GER: missing starting spirits')
    check(not values(history, 'create_country_leader'), 'GER: anonymous duplicate monarchs in history')
    check(bool(one(history, 'GER_wilhelm_ii')) and not one(history, 'GER_wilhelm_iii'), 'GER: Wilhelm II must start alone')

    balance = one(read(root / 'common/bop/GER_bop.txt'), 'GER_kaiser_vs_reichstag')
    ranges = values(balance, 'range') + [r for side in values(balance,'side') for r in values(side,'range')]
    ranges.sort(key=lambda r: float(one(r,'min')))
    boundaries = [-1, -0.80, -0.55, -0.45, 0.45, 0.55, 0.80, 1]
    check(len(ranges) == 7 and all(float(one(r,'min')) == boundaries[i] and float(one(r,'max')) == boundaries[i+1]
                                 for i,r in enumerate(ranges)), 'GER: BoP ranges have gaps or incorrect thresholds')
    check(float(one(balance, 'initial_value')) == 0, 'GER: BoP must start balanced')
    check(one(events['ger_crisis.1'],'fire_only_once') == 'yes' and one(one(events['ger_crisis.1'],'mean_time_to_happen'),'days') == '60',
          'GER: succession must be once-only with a 60-day MTTH')

    # Check every project-owned GER reference, including UI paths and both languages.
    files = [p for directory in ('common','events','interface') for p in (root/directory).rglob('GER*') if p.is_file()]
    locales = {}
    for lang in ('english','russian'):
        path = root / f'localisation/{lang}/GER_l_{lang}.yml'
        data = path.read_text(encoding='utf-8-sig')
        party_data = (root/f'localisation/{lang}/GER_parties_l_{lang}.yml').read_text(encoding='utf-8-sig')
        locales[lang] = set(re.findall(r'^ ([\w.]+):', data + party_data, re.M))
        check(path.read_bytes().startswith(b'\xef\xbb\xbf') and data.startswith('l_'+lang+':\n'), f'GER: invalid {lang} localization header')
        check(len(locales[lang]) == len(re.findall(r'^ ([\w.]+):',data + party_data,re.M)), f'GER: duplicate {lang} keys')
    check(locales['english'] == locales['russian'], 'GER: English/Russian key mismatch')
    required = set(political) | {k+'_desc' for k in political} | {one(r,'id') for r in ranges}
    required |= {k for k,v,o in decisions} | {k+'_desc' for k,v,o in decisions}
    required |= {'ger_aging_monarch','GER_kaiser_vs_reichstag','GER_ohl_and_crown_side','GER_reichstag_side'}
    required |= {k for k,v,o in country_ideas if k != 'NWW_GER_quality'}
    required |= {k+'_desc' for k,v,o in country_ideas if k != 'NWW_GER_quality'}
    required |= {v for event in events.values() for k,v,o in walk(event) if k in ('title','desc','name')}
    check(required <= locales['english'], f'GER: missing localization {required-locales["english"]}')
    sprites = {}
    native_sprites = {}
    for base in (game, *sorted(game.glob('dlc/*')), root):
        for path in (base/'interface').rglob('*.gfx'):
            try:
                doc = read(path)
            except ValueError:
                check(base != root, f'{path.name}: invalid interface script')
                continue  # A few unrelated installed native files have unmatched braces.
            for key, value, op in walk(doc):
                if key and key.lower() == 'spritetype':
                    sprites[one(value,'name')] = one(value,'texturefile')
                    if base != root:
                        native_sprites[one(value,'name')] = one(value,'texturefile')
    check(all('GFX_idea_'+one(node,'picture') in sprites for k,node,o in country_ideas), 'GER: undefined idea picture')
    for path in files:
        doc = read(path)
        check(not list(engine_script_errors(doc)), f'{path.name}: engine syntax errors')
        for key,value,op in walk(doc):
            if key == 'set_politics':
                check({'ruling_party','elections_allowed','election_frequency'} <= {k for k,v,o in value}, f'{path.name}: incomplete set_politics')
            if key == 'add_power_balance_value':
                side = 'GER_ohl_and_crown_side' if float(one(value,'value')) < 0 else 'GER_reichstag_side'
                check(one(value,'tooltip_side') == side, f'{path.name}: wrong BoP tooltip direction')
            if isinstance(value,str) and value.startswith('GFX_'):
                check(value in sprites, f'{path.name}: missing sprite {value}')
                texture = sprites.get(value)
                check(texture and any((base/texture).is_file() for base in (root,game,*sorted(game.glob('dlc/*')))), f'{path.name}: missing texture for {value}')
    for focus in political.values():
        icon = one(focus,'icon')
        check(icon+'_shine' in sprites, f'{icon}: missing shine')
        check(icon in native_sprites and sprites.get(icon)==native_sprites.get(icon), f'{icon}: political icon must use native artwork without overrides')
        image_path = next((base/sprites[icon] for base in (game,*sorted(game.glob('dlc/*')),root) if (base/sprites[icon]).is_file()), None)
        with Image.open(image_path) as img:
            bounds = img.convert('RGBA').getchannel('A').getbbox()
            check(img.width > 0 and img.height > 0 and bounds, f'{icon}: invalid native texture')

    scenarios = 0
    def fresh():
        w = Scenario(effects, events)
        w.apply(effects['nww_GER_initialize_politics'])
        return w

    # Both repeatable decisions change the actual meter in the intended direction.
    for token,node,op in decisions[:2]:
        w = fresh()
        check(one(node,'cost') == '50' and int(one(node,'days_re_enable')) > 0 and one(node,'fire_only_once') != 'yes', f'{token}: invalid repeatable cost/cooldown')
        for _ in range(2):
            check(w.condition(one(node,'available')), f'{token}: decision cannot repeat')
            w.apply(one(node,'complete_effect'))
        check(w.countries['GER']['balance'] == (-0.20 if token.endswith('general_staff') else 0.20), f'{token}: wrong shift')
        w.countries['GER']['flags'].update(('ger_bop_frozen','ger_iron_kaiserreich'))
        check(not w.condition(one(node,'available')) and not w.condition(one(node,'visible')), f'{token}: available after dissolution')
        scenarios += 1

    # Boundary values, preparation and the exact 40% mandate are evaluated from script.
    coup = one(political['GER_the_potsdam_coup'],'available')
    for bop in (-1, -0.11, -0.10, 0, 0.5):
        for popularity in (0.39, 0.40):
            w = fresh(); s = w.countries['GER']
            s['balance'], s['neutrality'] = bop, popularity
            s['flags'].add('ger_wilhelm_ii_dead')
            s['focuses'].update(('GER_the_gilded_colossus','GER_fund_the_reichswehr'))
            check(w.condition(coup) == (bop < -0.10 and popularity >= 0.40), 'GER: wrong coup boundary/mandate')
            scenarios += 1
    w = fresh(); s = w.countries['GER']; s['balance'] = -0.2
    check(not w.condition(coup), 'GER: coup available without death/preparation')
    s['focuses'].add('GER_dissolve_the_reichstag')
    w.apply(one(political['GER_dissolve_the_reichstag'],'completion_reward'))
    s['balance'] = 0.5
    w.apply(effects['nww_GER_initialize_politics']); first = deepcopy(s)
    w.apply(effects['nww_GER_initialize_politics'])
    check(s['balance'] == -1 and s == first, 'GER: locked BoP repair is not idempotent')
    scenarios += 2

    # Succession cannot occur early, occurs by the hard deadline, and fires once.
    w = fresh(); w.date = '1936.8.1'
    check(not w.event('ger_crisis.1'), 'GER: succession can occur before August 2')
    w.date = '1936.12.31'
    daily = one(one(on_actions,'on_daily_GER'),'effect')
    w.apply([('if', one(daily,'if'), '=')])
    check(('GER','ger_crisis.1') in w.queue, 'GER: missing deterministic succession deadline')
    check(w.event('ger_crisis.1') and not w.event('ger_crisis.1'), 'GER: succession is not once-only')
    s = w.countries['GER']
    check(s['leader'] == 'GER_wilhelm_iii' and 'ger_aging_monarch' not in s['traits'] and 'GER_end_of_an_era' in s['focuses'] and w.news == ['ger_news.1'], 'GER: succession did not settle leader, trait, focus and news')
    scenarios += 2

    # War prevention and pending refusals across the year boundary and old-save loads.
    for date in ('1936.1.1','1938.12.31','1939.1.1','1939.1.2'):
        w = fresh(); w.date = date
        w.countries['GER']['focuses'].add('GER_reign_in_mitteleuropa')
        w.countries['LTB']['flags'].add('ger_mitteleuropa_refused')
        w.apply(effects['nww_GER_initialize_politics'])
        w.apply(effects['nww_GER_mitteleuropa_refusal_wargoals'])
        s = w.countries['GER']; early = date.startswith(('1936','1938'))
        check(('LTB' in s['rules']) == early and ('LTB' in s['goals']) != early, f'GER: LTB date guard fails on {date}')
        first = deepcopy(w.countries)
        w.apply(effects['nww_GER_initialize_politics']); w.apply(effects['nww_GER_mitteleuropa_refusal_wargoals'])
        check(w.countries == first, 'GER: daily/save repair repeats rewards or wargoals')
        scenarios += 1

    # Independent acceptance, refusal, third-party subjection, war and DLC fallback.
    for recipient,eid,focus in (('AUS','ger_crisis.10','GER_the_austrian_question'),
                                ('LTB','ger_crisis.20','GER_reign_in_mitteleuropa'),
                                ('POL','ger_crisis.20','GER_reign_in_mitteleuropa')):
        for option in (0,1):
            for blocked in (None,'subject','war','ger_subject','ger_absent','ger_democratic'):
                w = fresh(); w.date = '1939.1.1'; w.countries['GER']['focuses'].add(focus)
                if blocked == 'subject': w.countries[recipient]['subject'] = 'SOV'
                if blocked == 'war': w.countries[recipient]['wars'].add('GER')
                if blocked == 'ger_subject': w.countries['GER']['subject'] = 'SOV'
                if blocked == 'ger_absent': w.countries['GER']['exists'] = False
                if blocked == 'ger_democratic': w.countries['GER']['government'] = 'democratic'
                accepted = w.event(eid,recipient,option)
                check(accepted == (blocked is None), f'GER: invalid diplomatic state allowed for {recipient}')
                if blocked is None:
                    check((w.countries[recipient]['subject'] == 'GER') == (option == 0), f'GER: {recipient} consent ignored')
                    if option == 1:
                        check((recipient in w.countries['GER']['goals']) == True, f'GER: wrong refusal war goal for {recipient}')
                scenarios += 1
        # Replies are selected after delivery: third-party events can change the world meanwhile.
        for blocked in ('subject','war','ger_subject','ger_absent','ger_democratic'):
            w = fresh(); w.date = '1939.1.1'; w.countries['GER']['focuses'].add(focus)
            check(w.event(eid,recipient), 'GER: valid demand was not delivered')
            if blocked == 'subject': w.countries[recipient]['subject'] = 'SOV'
            if blocked == 'war': w.countries[recipient]['wars'].add('GER')
            if blocked == 'ger_subject': w.countries['GER']['subject'] = 'SOV'
            if blocked == 'ger_absent': w.countries['GER']['exists'] = False
            if blocked == 'ger_democratic': w.countries['GER']['government'] = 'democratic'
            before = deepcopy(w.countries)
            for option in values(events[eid],'option'):
                w.apply([e for e in option if e[0] not in ('name','ai_chance')],recipient)
            check(w.countries == before, f'GER: stale {recipient} reply changes invalid diplomatic state')
            scenarios += 1
    for dlc in (False,True):
        w = fresh(); w.date = '1939.1.1'; w.dlc = dlc
        w.countries['LTB']['subject'] = 'GER'
        w.countries['LTB']['autonomy'] = 'autonomy_dominion'
        w.apply(effects['nww_GER_mitteleuropa_demand'],'LTB')
        check(w.countries['LTB']['autonomy'] == ('autonomy_integrated_puppet' if dlc else 'autonomy_puppet'), 'GER: autonomy/DLC fallback failed')
        scenarios += 1
    for target in ('MKN','UKR'):
        for blocked in (None,'absent','subject','allied','war'):
            w = fresh(); w.date = '1939.1.1'
            if blocked == 'absent': w.countries[target]['exists'] = False
            if blocked == 'subject': w.countries[target]['subject'] = 'SOV'
            if blocked == 'allied': w.countries['GER']['allies'].add(target)
            if blocked == 'war': w.countries['GER']['wars'].add(target)
            w.apply(effects['nww_GER_eastern_wargoals'])
            check((target in w.countries['GER']['goals']) == (blocked is None), f'GER: invalid eastern war goal against {target}')
            scenarios += 1
    # The four entry paths have reciprocal exclusions, preparation and exact mandates.
    entries = {
        'GER_the_potsdam_coup': ('neutrality','GER_fund_the_reichswehr','ger_iron_kaiserreich'),
        'GER_parliamentary_spring': ('democratic','GER_empower_the_chancellor','ger_parliamentary_spring'),
        'GER_the_pan_germanic_triumph': ('fascism','GER_pan_german_leagues','ger_pan_germanic_path'),
        'GER_the_spartacist_uprising': ('communism','GER_organize_ruhr_workers','ger_spartacist_civil_war_started'),
    }
    for fid,(ideology,prep,flag) in entries.items():
        excluded = {v for group in values(political[fid],'mutually_exclusive') for v in values(group,'focus')}
        check(excluded == entries.keys()-{fid}, f'{fid}: exclusions are not complete and reciprocal')
        for bop in (-0.31,-0.30,-0.11,0,0.10,0.11,0.30,0.31):
            for popularity in (0.39,0.40):
                w=fresh();s=w.countries['GER']
                s['balance'],s[ideology]=bop,popularity
                s['flags'].add('ger_wilhelm_ii_dead')
                s['focuses'].update(('GER_the_gilded_colossus',prep))
                correct_balance = {'neutrality':bop < -0.10,'democratic':bop > 0.10,
                                   'fascism':-0.30 <= bop <= 0.30,'communism':True}[ideology]
                check(w.condition(one(political[fid],'available')) == (popularity >= 0.40 and correct_balance),
                      f'{fid}: incorrect preparation, BoP or mandate boundary')
                s['focuses'].discard(prep)
                check(not w.condition(one(political[fid],'available')), f'{fid}: preparation can be skipped')
                scenarios+=1
        for other,(_,_,selected_flag) in entries.items():
            w=fresh();s=w.countries['GER']
            s['focuses'].update(('GER_the_gilded_colossus',prep));s[ideology]=0.50
            s['flags'].update(('ger_wilhelm_ii_dead',selected_flag));s['balance']=0.2 if ideology=='democratic' else -0.2
            check(not w.condition(one(political[fid],'available')), f'{fid}: selectable after {other}')
            scenarios+=1

    # Source preparation and repeatable decisions can actually reach every political mandate.
    support = {'GER_parliamentary_spring':'GER_concede_to_parliament',
               'GER_the_pan_germanic_triumph':'GER_rally_pan_german_leagues',
               'GER_the_spartacist_uprising':'GER_organize_workers_councils'}
    for fid,decision_id in support.items():
        ideology,prep,_=entries[fid];w=fresh();s=w.countries['GER']
        s['focuses'].add(prep);w.apply(one(political[prep],'completion_reward'))
        decision=one(decisions,decision_id)
        for _ in range(8):
            if s[ideology] >= 0.40: break
            check(w.condition(one(decision,'visible',[])) and w.condition(one(decision,'available')), f'{fid}: support decision inaccessible')
            w.apply(one(decision,'complete_effect'))
        check(s[ideology] >= 0.40, f'{fid}: no viable path to the mandate')
        scenarios+=1

    # All eastern targets stay protected for every ideology and for dynamic German tags.
    eastern={'LTB','POL','MKN','UKR','SOV'}
    for government in ('neutrality','democratic','fascism','communism'):
        for actor in ('GER','D01'):
            for date in ('1938.12.31','1939.1.1'):
                w=fresh();w.date=date
                if actor=='D01': w.countries[actor]=deepcopy(w.countries['GER'])
                s=w.countries[actor];s['government']=government
                w.apply(effects['nww_GER_initialize_politics'],actor)
                check(s['rules']==(eastern if date=='1938.12.31' else set()), f'GER: eastern rule leak for {government}/{actor}/{date}')
                scenarios+=1
    for fid in ('GER_reign_in_mitteleuropa','GER_crush_eastern_syndicates','GER_lebensraum_in_the_east'):
        gate=one(political[fid],'available')
        check(('date','1938.12.31','>') in gate, f'{fid}: missing explicit eastern date gate')
        check(any(one(node,'tooltip')=='GER_eastern_1939_gate_tt' for node in values(gate,'custom_trigger_tooltip')),f'{fid}: no visible date tooltip')
        for date in ('1938.12.31','1939.1.1'):
            w=fresh();w.date=date;w.countries['GER']['government']='fascism' if fid=='GER_lebensraum_in_the_east' else 'neutrality'
            check(w.condition(gate)==(date=='1939.1.1'), f'{fid}: incorrect year boundary')
            scenarios+=1
    for date in ('1938.12.31','1939.1.1'):
        for target in ('LTB','POL'):
            w=fresh();w.date=date;w.countries['GER']['focuses'].add('GER_reign_in_mitteleuropa')
            w.apply(effects['nww_GER_mitteleuropa_demand'],target)
            check(((target,'ger_crisis.20') in w.queue)==(date=='1939.1.1'),'GER: subjugation demand before 1939')
            check(w.event('ger_crisis.20',target,0)==(date=='1939.1.1'),'GER: early queued ultimatum accepted')
            scenarios+=1
        for helper,government,targets in (('nww_GER_eastern_wargoals','neutrality',{'MKN','UKR'}),
                                          ('nww_GER_pan_german_eastern_wargoals','fascism',{'LTB','POL'})):
            w=fresh();w.date=date;w.countries['GER']['government']=government
            w.apply(effects[helper])
            check(w.countries['GER']['goals']==(targets if date=='1939.1.1' else set()), f'{helper}: bypasses year gate')
            scenarios+=1

    # Constitutional / abolished BoP states survive startup repair without recreating the old regime.
    for focus,flag,expected in (('GER_parliamentary_spring','ger_parliamentary_spring',1),
                                ('GER_abolish_the_hohenzollerns','ger_bop_removed',None),
                                ('GER_the_spartacist_uprising','ger_spartacist_side',None)):
        w=fresh();s=w.countries['GER'];s['focuses'].add(focus);s['flags'].add(flag)
        s['balance']=-0.4;w.apply(effects['nww_GER_initialize_politics']);before=deepcopy(s)
        w.apply(effects['nww_GER_initialize_politics'])
        check(s['balance']==expected and s==before, 'GER: path-specific BoP repair regresses or repeats rewards')
        scenarios+=1

    # Real-script civil-war setup: player transfer, copied progress, character transfer and actual victory.
    w=fresh();s=w.countries['GER'];s['focuses'].update(('GER_the_gilded_colossus','GER_end_of_an_era','GER_organize_ruhr_workers','GER_the_spartacist_uprising'))
    war_definition = one(effects['nww_GER_start_spartacist_civil_war'],'start_civil_war')
    check(one(war_definition,'ideology') == 'communism' and float(one(war_definition,'size')) == 0.40, 'GER: wrong civil-war ideology or size')
    check(one(one(war_definition,'load_focus_tree'),'copy_completed_from') == 'ROOT', 'GER: civil war does not copy completed focuses without rewards')
    w.apply(effects['nww_GER_start_spartacist_civil_war'])
    rebel=w.countries['D01']
    check(w.player=='D01' and rebel['original']=='GER' and rebel['government']=='communism', 'GER: player does not control the communist uprising')
    check(rebel['focuses']==s['focuses'] and rebel['pp']==s['pp'],'GER: civil-war focus copying repeats rewards or drops progress')
    check(w.character_owner['GER_ernst_thalmann']=='D01','GER: Thalmann not transferred to the revolt')
    check(rebel['rules']==eastern and rebel['balance'] is None, 'GER: uprising loses date protection or inherits OHL')
    republic_gate=one(political['GER_german_soviet_republic'],'available')
    check(not w.condition(republic_gate,'D01'), 'GER: republic available during civil war')
    s['exists']=False;rebel['civil_war']=False;rebel['wars'].clear()
    w.apply(effects['nww_GER_spartacist_victory_repair'],'D01')
    check(not w.condition(republic_gate,'D01'), 'GER: disappearance of the loyalists is treated as a communist victory')
    w.apply(one(one(on_actions,'on_civil_war_end'),'effect'),'D01')
    check(w.condition(republic_gate,'D01'),'GER: actual communist civil-war victory does not unlock the republic')
    w.apply(one(political['GER_german_soviet_republic'],'completion_reward'),'D01')
    check(rebel['leader']=='GER_ernst_thalmann','GER: victorious republic did not install Thalmann')
    scenarios+=6
    for winner in ('GER','SOV'):
        lost=fresh();lost.countries['GER']['flags'].add('ger_spartacist_loyalists')
        lost.apply(one(one(on_actions,'on_civil_war_end'),'effect'),winner)
        check('ger_spartacist_victory' not in lost.countries[winner]['flags'],'GER: loyalist/foreign victory counts as Spartacist victory')
        scenarios+=1

    # The native ideology file differs only by four explicitly nonrandom GER subtypes.
    ideology_doc=read(root/'common/ideologies/00_ideologies.txt')
    native_ideologies=read(game/'common/ideologies/00_ideologies.txt')
    for group,subtype in {'fascism':'GER_pan_germanism','democratic':'GER_social_democracy','communism':'GER_spartacism','neutrality':'GER_imperial_autocracy'}.items():
        types=one(one(one(ideology_doc,'ideologies'),group),'types')
        check(one(one(types,subtype),'can_be_randomly_selected')=='no',f'{subtype}: affects random leaders outside GER')
        types[:]=[e for e in types if e[0]!=subtype]
        check(subtype in locales['english'] and subtype+'_desc' in locales['russian'],f'{subtype}: unlocalized ideology')
    check(ideology_doc==native_ideologies,'GER: native ideology groups/rules changed')

    # Voluntary economic integration frees only German subjects and awards no repeated factories.
    for target in ('LTB','POL'):
        for overlord in ('GER','SOV',None):
            w=fresh();s=w.countries['GER'];s['government']='democratic'
            s['focuses'].add('GER_mitteleuropa_economic_community');w.countries[target]['subject']=overlord
            w.apply(one(political['GER_mitteleuropa_economic_community'],'completion_reward'))
            check(w.countries[target]['subject']==('SOV' if overlord=='SOV' else None),'GER: emancipation steals another overlords subject')
            accepted=w.event('ger_crisis.50',target,0)
            check(accepted==(overlord!='SOV'),'GER: economic offer ignores third-party subjection')
            check(s['factories']==(1 if accepted else 0),'GER: wrong integration factory reward')
            w.event('ger_crisis.50',target,0)
            check(s['factories']==(1 if accepted else 0),'GER: economic agreement can farm factories')
            scenarios+=1
        w=fresh();s=w.countries['GER'];s['government']='democratic';s['faction']='GER'
        s['focuses'].add('GER_mitteleuropa_economic_community')
        check(w.event('ger_crisis.50',target,1),'GER: partner cannot decline economic integration')
        check(w.countries[target]['faction'] is None and not s['factories'] and not s['goals'],'GER: economic refusal forces membership or war')
        scenarios+=1
    w=fresh();s=w.countries['GER'];s['ideas'].add('GER_constitutional_monarchy');s['government']='democratic'
    w.apply(one(political['GER_arsenal_of_democracy'],'completion_reward'))
    check(s['ideas']=={'GER_arsenal_of_democracy'} and s['guarantees']=={'LTB','POL'},'GER: democratic capstone duplicates institutions or lacks guarantees')
    scenarios+=1

    # Austria chooses: democratic unification, sovereign alliance, refusal or resisting annexation.
    for eid,focus,government,options in (('ger_crisis.30','GER_the_austrian_referendum','democratic',range(3)),
                                        ('ger_crisis.40','GER_anschluss_by_force','fascism',range(2))):
        for option in options:
            w=fresh();s=w.countries['GER'];s['government']=government;s['focuses'].add(focus)
            w.countries['AUS']['government']='democratic'
            check(w.event(eid,'AUS',option),'GER: Austrian choice not available')
            if option==0: check(not w.countries['AUS']['exists'],'GER: consenting Austria did not unify')
            elif eid=='ger_crisis.40': check(s['goals']=={'AUS'},'GER: Austrian resistance lacks annexation goal')
            elif option==1: check(w.countries['AUS']['faction']=='GER','GER: Austria cannot form a sovereign alliance')
            else: check(not s['goals'] and w.countries['AUS']['exists'],'GER: referendum refusal creates military consequences')
            scenarios+=1
    for existing_faction in (None,'SOV'):
        for option in (0,1):
            w=fresh();w.countries['D01']=deepcopy(w.countries['GER']);g=w.countries['D01']
            g['government']='communism';g['focuses'].add('GER_berlin_moscow_axis')
            sov=w.countries['SOV'];sov['government']='communism';sov['faction']=existing_faction
            check(w.event('ger_crisis.60','SOV',option,sender='D01'),'GER: dynamic communist Germany cannot contact Moscow')
            check((g['faction']=='SOV')==(option==0),'GER: Soviet faction consent ignored')
            scenarios+=1

    # Every accepted annexation/invitation rechecks live diplomacy after delivery.
    for eid,focus,government,recipient in (
        ('ger_crisis.30','GER_the_austrian_referendum','democratic','AUS'),
        ('ger_crisis.40','GER_anschluss_by_force','fascism','AUS'),
        ('ger_crisis.50','GER_mitteleuropa_economic_community','democratic','LTB'),
        ('ger_crisis.60','GER_berlin_moscow_axis','communism','SOV')):
        for blocked in ('recipient_subject','sender_subject','war','sender_absent','wrong_government'):
            w=fresh();g=w.countries['GER'];g['government']=government;g['focuses'].add(focus)
            if eid=='ger_crisis.50': g['faction']='GER'
            w.countries[recipient]['government']='communism' if recipient=='SOV' else 'democratic'
            check(w.event(eid,recipient),'GER: valid diplomatic offer could not be delivered')
            if blocked=='recipient_subject': w.countries[recipient]['subject']='UKR'
            if blocked=='sender_subject': g['subject']='UKR'
            if blocked=='war': w.countries[recipient]['wars'].add('GER')
            if blocked=='sender_absent': g['exists']=False
            if blocked=='wrong_government': g['government']='neutrality'
            before=deepcopy(w.countries)
            for opt in values(events[eid],'option'):
                w.apply([e for e in opt if e[0] not in ('name','ai_chance','trigger')],recipient)
            check(w.countries==before,f'{eid}: stale reply changes invalid diplomatic state')
            scenarios+=1

    print(f'PASS: GER political graph, native tokens, BoP/UI/localization and {scenarios} source-script lifecycle scenarios')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', type=Path, default=Path.home()/'.local/share/Steam/steamapps/common/Hearts of Iron IV')
    args = parser.parse_args()
    if not args.game.is_dir(): parser.error(f'Installed HOI4 directory does not exist: {args.game}')
    errors = []
    validate_germany(Path(__file__).resolve().parents[1], args.game,
                     lambda ok, message: errors.append(message) if not ok else None)
    for error in errors: print('ERROR:',error)
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
