"""Validate LTB/MKN graphs and resources against an installed HOI4 copy.

Usage: python tools/validate_country_content.py --game "D:/Steam/steamapps/common/Hearts of Iron IV"
This is a static content check, not a substitute for an in-game campaign.
"""
import argparse
from functools import lru_cache
from pathlib import Path
import re
import sys
from PIL import Image
from hoi4_script import read, one, values, walk

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--game', required=True, type=Path)
args = parser.parse_args()
GAME = args.game
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def documents(root, glob):
    for path in root.glob(glob):
        try:
            yield path, read(path)
        except (ValueError, UnicodeError) as exc:
            # Only files under review are required to parse; unrelated base assets can contain shader syntax.
            if root == ROOT:
                errors.append(f'{path.relative_to(ROOT)}: {exc}')


def localization(lang):
    result = {}
    for root in (GAME, ROOT):
        for p in root.glob(f'localisation/**/*l_{lang}.yml'):
            text = p.read_text(encoding='utf-8-sig', errors='replace')
            for key, value in re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$', text, re.M):
                if root == ROOT and (p.name.lower().startswith('nww_ltb') or p.name.startswith('nww_MKN') or p.name.startswith('nww_country_expansion')):
                    check(p.read_bytes().startswith(b'\xef\xbb\xbf'), f'{p.name}: missing UTF-8 BOM')
                    check(key not in result or key not in custom_keys[lang], f'{p.name}: duplicate localization {key}')
                    check(not re.search(r'\?{2,}', value), f'{p.name}: damaged text encoding for {key}')
                    custom_keys[lang].add(key)
                result[key] = value
    return result


custom_keys = {'russian': set(), 'english': set()}
locales = {lang: localization(lang) for lang in custom_keys}
sprites = {}
resource_roots = [GAME, *sorted(GAME.glob('dlc/*')), ROOT]
for root in resource_roots:
    for p, doc in documents(root, 'interface/**/*.gfx'):
        names_in_file = set()
        for key, value, op in walk(doc):
            if key and key.lower() == 'spritetype':
                name = one(value, 'name')
                if root == ROOT and p.name in ('nww_companies.gfx', 'nww_ltb_ideas.gfx', 'ltb_portraits.gfx', 'nww_mkn_portraits.gfx'):
                    check(name not in names_in_file, f'{p.name}: duplicate sprite {name}')
                names_in_file.add(name)
                sprites[name] = one(value, 'texturefile')


def sprite(token, context):
    check(token in sprites, f'{context}: undefined sprite {token}')
    texture = sprites.get(token)
    if texture:
        check(any((root / texture).is_file() for root in resource_roots), f'{context}: missing texture {texture}')


def localized(key, context):
    for lang, entries in locales.items():
        check(key in entries, f'{context}: missing {lang} text {key}')


traits = set()
for root in (GAME, ROOT):
    for p, doc in documents(root, 'common/country_leader/*.txt'):
        traits.update(k for k, v, op in one(doc,'leader_traits',[]) if k and isinstance(v,list))
for p, doc in documents(GAME, 'common/unit_leader/*.txt'):
    traits.update(k for k, v, op in walk(doc) if k and isinstance(v, list))
categories = set()
for p, doc in documents(GAME, 'common/technology_tags/*.txt'):
    categories.update(v for k, v, op in walk(doc) if k is None)
templates = {k for p, doc in documents(GAME, 'common/military_industrial_organization/organizations/*.txt') for k, v, op in doc}
mio_traits = set()
for root in (GAME,ROOT):
    for p,doc in documents(root,'common/military_industrial_organization/organizations/*.txt'):
        for k,v,o in walk(doc):
            if k in ('trait','add_trait') and isinstance(v,list):
                mio_traits.add(one(v,'token'))
state_provinces = {}
for p, doc in documents(ROOT, 'history/states/*.txt'):
    state = one(doc, 'state')
    if state:
        state_provinces[one(state, 'id')] = {v for k, v, op in one(state, 'provinces', [])}

all_focus_ids = {v for p, doc in documents(ROOT, 'common/national_focus/*.txt') for k, v, op in walk(doc) if k == 'id' and isinstance(v, str)}
idea_ids = set()
for p, doc in documents(ROOT, 'common/ideas/*.txt'):
    for group, ideas, op in one(doc, 'ideas', []):
        if isinstance(ideas, list):
            idea_ids.update(k for k, v, op in ideas if isinstance(v, list))
characters = {k for p, doc in documents(ROOT, 'common/characters/*.txt') for k, v, op in one(doc, 'characters', [])}
organizations = {k for p, doc in documents(ROOT, 'common/military_industrial_organization/organizations/*.txt') for k, v, op in doc}
sharing_groups = {one(v, 'id') for root in (GAME, ROOT) for p, doc in documents(root, 'common/technology_sharing/*.txt') for k, v, op in doc if k == 'technology_sharing_group'}
event_ids = {v for p, doc in documents(ROOT, 'events/*.txt') for k, v, op in walk(doc) if k == 'id' and isinstance(v, str)}
opinion_ids = {k for p,doc in documents(ROOT,'common/opinion_modifiers/*.txt') for k,v,o in one(doc,'opinion_modifiers',[])}
counts = {}
scope_files = [
    *[ROOT / f'common/national_focus/{tag}_focus.txt' for tag in ('ltb', 'mkn')],
    *[ROOT / f'common/characters/nww_{tag}.txt' for tag in ('LTB', 'MKN')],
    *[ROOT / f'common/ideas/nww_{tag}_ideas.txt' for tag in ('LTB', 'MKN')],
    ROOT / 'common/ideas/nww_companies.txt',
    ROOT / 'common/military_industrial_organization/organizations/nww_organizations.txt',
    ROOT / 'interface/ltb_portraits.gfx', ROOT / 'interface/nww_mkn_portraits.gfx', ROOT / 'interface/nww_companies.gfx',
    ROOT / 'history/countries/LTB - Lithuania Belarus.txt', ROOT / 'history/countries/MKN - Makhnovists.txt',
    ROOT / 'events/nww_ltb.txt', ROOT / 'events/nww_mkn.txt',
    ROOT / 'events/nww_ltb_diplomacy.txt', ROOT / 'interface/nww_ltb_ideas.gfx',
    ROOT / 'events/nww_ltb_politics.txt',
    ROOT / 'common/opinion_modifiers/nww_ltb_diplomacy.txt',
    ROOT / 'common/country_leader/nww_industry_traits.txt', ROOT / 'common/technology_sharing/nww_ltb_research.txt',
    ROOT / 'common/on_actions/nww_ltb_on_actions.txt', ROOT / 'common/decisions/nww_ltb_decisions.txt',
    ROOT / 'common/decisions/categories/nww_ltb_categories.txt'
]
for path in scope_files:
    doc = read(path)
    context = str(path.relative_to(ROOT))
    for key, value, op in walk(doc):
        if isinstance(value, str):
            check(key != 'num_of_research_slots', f'{context}: use documented amount_research_slots trigger')
            if value.startswith('GFX_'):
                sprite(value, context)
            elif key == 'picture' and '/ideas/' in path.as_posix():
                sprite('GFX_idea_' + value, context)
            if key in ('has_completed_focus', 'complete_national_focus'):
                check(value in all_focus_ids, f'{context}: unknown focus {value}')
            if key == 'recruit_character':
                check(value in characters, f'{context}: unknown character {value}')
            if key in ('add_ideas', 'remove_ideas', 'idea', 'has_idea', 'show_ideas_tooltip', 'add_idea', 'remove_idea'):
                check(value in idea_ids, f'{context}: unknown idea {value}')
            if key == 'include':
                check(value in templates, f'{context}: unknown MIO template {value}')
            if key == 'show_mio_tooltip':
                check(value in organizations, f'{context}: unknown MIO {value}')
            if key == 'add_to_tech_sharing_group':
                check(value in sharing_groups, f'{context}: unknown technology sharing group {value}')
            if key in ('custom_effect_tooltip', 'custom_modifier_tooltip', 'idea_token'):
                localized(value, context)
        if key == 'traits' and isinstance(value, list):
            for k, trait, op in value:
                valid = mio_traits if '/military_industrial_organization/' in path.as_posix() else traits
                check(trait in valid, f'{context}: unknown trait {trait}')
        if key == 'custom_trigger_tooltip' and isinstance(value, list):
            localized(one(value, 'tooltip'), context)
        if key == 'unlock_mio_trait_tooltip' and isinstance(value,str):
            check(value in mio_traits, f'{context}: unlock tooltip points to unknown MIO trait {value}')
        if key and key.startswith('mio:'):
            check(key[4:] in organizations, f'{context}: unknown MIO scope {key}')
        if key == 'add_tech_bonus':
            for category in values(value, 'category'):
                check(category in categories, f'{context}: unknown technology category {category}')
                check(not category.endswith('_doctrine'), f'{context}: doctrine bonus incorrectly uses research effect')
        if key == 'add_opinion_modifier':
            check(one(value,'modifier') in opinion_ids, f'{context}: unknown opinion modifier {one(value,"modifier")}')
        if key in ('country_event', 'news_event') and isinstance(value, list) and one(value, 'days'):
            check(one(value, 'id') in event_ids, f'{context}: missing event {one(value, "id")}')
        if key and key.isdigit() and isinstance(value, list):
            check(key in state_provinces, f'{context}: unknown state {key}')
            for sk, construction, sop in walk(value):
                if sk == 'add_building_construction':
                    province = one(construction, 'province')
                    kind = one(construction, 'type')
                    if province:
                        check(province in state_provinces.get(key, set()), f'{context}: province {province} is outside state {key}')
                    if kind in ('bunker', 'coastal_bunker', 'naval_base'):
                        check(province is not None, f'{context}: {kind} needs an explicit province')
            def check_slots(block):
                shared = sum(int(one(b, 'level', '0')) for b in values(block, 'add_building_construction') if one(b, 'type') in ('industrial_complex', 'arms_factory', 'dockyard'))
                if shared:
                    check(sum(int(n) for n in values(block, 'add_extra_state_shared_building_slots')) >= shared, f'{context}: state {key} constructs more shared buildings than guaranteed slots')
                for bk, bv, bo in block:
                    if isinstance(bv, list):
                        check_slots(bv)
            check_slots(value)
    tree = one(doc, 'focus_tree')
    if tree:
        focuses = values(tree, 'focus')
        by_id = {one(f, 'id'): f for f in focuses}
        check(len(by_id) == len(focuses), f'{context}: duplicate focus IDs')
        counts[one(tree, 'id')] = len(focuses)
        continuous = one(tree,'continuous_focus_position')
        check(int(one(continuous,'y')) >= max(int(one(f,'y')) for f in focuses)*130+800, f'{context}: continuous panel has insufficient clearance below the tree')
        for index, f in enumerate(focuses):
            fid = one(f, 'id')
            for key, flag, op in walk(one(f, 'available', [])):
                if key == 'has_country_flag':
                    localized(flag, f'{fid} availability')
            for key, politics, op in walk(one(f,'completion_reward')):
                if key == 'set_politics':
                    if values(politics,'elections_allowed'):
                        check(bool(one(politics,'ruling_party')), f'{fid}: election tooltip lacks a ruling party in the same set_politics block')
                    check(len(values(politics,'ruling_party')) <= 1, f'{fid}: duplicated ruling party in political transition')
            localized(fid, context); localized(fid + '_desc', context)
            for g in focuses[index + 1:]:
                if one(f, 'y') == one(g, 'y'):
                    check(abs(int(one(f, 'x')) - int(one(g, 'x'))) >= 2, f'{context}: crowded row: {fid}, {one(g,"id")}')
            for group in values(f, 'prerequisite'):
                for parent in values(group, 'focus'):
                    check(parent in by_id, f'{fid}: unknown prerequisite {parent}')
                    if parent in by_id:
                        check(int(one(by_id[parent], 'y')) < int(one(f, 'y')), f'{fid}: prerequisite {parent} is not above the focus')
            for group in values(f, 'mutually_exclusive'):
                for other in values(group, 'focus'):
                    check(other in by_id, f'{fid}: unknown exclusive focus {other}')
                    if other in by_id:
                        reverse = [v for g in values(by_id[other], 'mutually_exclusive') for v in values(g, 'focus')]
                        check(fid in reverse, f'{fid}: exclusion with {other} is not reciprocal')
        # All nodes must be reachable if mutually exclusive choices are ignored.
        reached = set()
        while True:
            newly = {fid for fid, f in by_id.items() if fid not in reached and all(any(p in reached for p in values(g, 'focus')) for g in values(f, 'prerequisite'))}
            if not newly:
                break
            reached |= newly
        check(reached == set(by_id), f'{context}: cyclic/unreachable focuses {set(by_id)-reached}')
        if reached == set(by_id):
            pairs = {frozenset((fid, other)) for fid, f in by_id.items() for g in values(f, 'mutually_exclusive') for other in values(g, 'focus')}
            @lru_cache(None)
            def possible_paths(fid):
                paths = {frozenset((fid,))}
                for group in values(by_id[fid], 'prerequisite'):
                    alternatives = {p for parent in values(group, 'focus') for p in possible_paths(parent)}
                    paths = {a | b for a in paths for b in alternatives if not any(pair <= (a | b) for pair in pairs)}
                return paths
            for fid in by_id:
                check(bool(possible_paths(fid)), f'{fid}: prerequisites require mutually exclusive choices')
    if '/characters/' in path.as_posix():
        for token, char, op in one(doc, 'characters'):
            for role in values(char, 'advisor'):
                portraits = one(char, 'portraits', [])
                check(any(one(p, 'small') for k, p, op in portraits), f'{token}: advisor has no small portrait')
            for kind, portrait, op in one(char, 'portraits', []):
                small = one(portrait, 'small')
                texture = sprites.get(small)
                if texture:
                    asset = next((root/texture for root in reversed(resource_roots) if (root/texture).is_file()), None)
                    if asset:
                        with Image.open(asset) as portrait_image:
                            check(portrait_image.size == (65, 67), f'{token}: {kind} advisor portrait is {portrait_image.size}; expected native 65x67')
                            if 'nww_portraits' in str(asset):
                                bounds=portrait_image.getchannel('A').getbbox()
                                check(bounds is not None and bounds[3] <= 61, f'{token}: portrait artwork intrudes into the bottom card border')
    if '/events/' in path.as_posix():
        for kind, event, op in doc:
            if kind in ('country_event', 'news_event') and one(event, 'hidden') != 'yes':
                for field in ('title', 'desc'):
                    key = one(event, field)
                    if isinstance(key, str):
                        localized(key, context)
                for option in values(event, 'option'):
                    localized(one(option, 'name'), context)
    if '/military_industrial_organization/' in path.as_posix():
        for token, organization, op in doc:
            localized(token, context)
            for initial in values(organization,'initial_trait'):
                localized(one(initial,'name'),context)
            for trait in values(organization,'add_trait'):
                localized(one(trait,'name',one(trait,'token')),context)
    if '/country_leader/' in path.as_posix():
        for token,trait,op in one(doc,'leader_traits',[]):
            localized(token,context)
    if '/ideas/' in path.as_posix():
        for kind, group, op in one(doc, 'ideas', []):
            for token, idea, op in group:
                if isinstance(idea, list):
                    localized(one(idea, 'name', token), context)
                    if kind == 'country':
                        localized(token + '_desc', context)
    if '/opinion_modifiers/' in path.as_posix():
        for token, modifier, op in one(doc, 'opinion_modifiers', []):
            localized(token, context)
    if '/decisions/' in path.as_posix():
        for category, group, op in doc:
            localized(category, context)
            if '/categories/' not in path.as_posix():
                for token, decision, op in group:
                    if isinstance(decision, list):
                        localized(token, context)
                        localized(token + '_desc', context)
    if '/technology_sharing/' in path.as_posix():
        for group in values(doc, 'technology_sharing_group'):
            localized(one(group, 'name'), context)
            localized(one(group, 'desc'), context)
    if path.name == 'nww_ltb_ideas.gfx':
        for sprite_def in values(one(doc,'spriteTypes'),'spriteType'):
            with Image.open(ROOT/one(sprite_def,'texturefile')) as icon_image:
                check(icon_image.size == (64,64), f'{context}: generated spirit icon must be 64x64')
                check('A' in icon_image.getbands(), f'{context}: generated spirit icon is missing alpha')
                if 'A' in icon_image.getbands():
                    check(icon_image.getchannel('A').getextrema()[0] == 0, f'{context}: generated spirit icon has no transparent background')
    if '/history/countries/' in path.as_posix():
        recruits = values(doc, 'recruit_character')
        check(len(recruits) == len(set(recruits)), f'{context}: duplicate character recruitment')

# Crisis regression: after a successful settlement, instability must not trigger an unconditional split.
weekly = one(one(read(ROOT/'common/on_actions/nww_ltb_on_actions.txt'), 'on_actions'), 'on_weekly')
weekly_limit = one(one(one(weekly, 'effect'), 'if'), 'limit')
emergency = next(event for event in values(read(ROOT/'events/nww_ltb.txt'), 'country_event') if one(event, 'id') == 'ltb.112')
for context, conditions in [('on_weekly', weekly_limit), ('ltb.112', one(emergency, 'trigger'))]:
    check(any(one(negation, 'has_country_flag') == 'LTB_union_preserved' for negation in values(conditions, 'NOT')), f'{context}: preserved union is not protected from the emergency split')
    check(any(one(negation, 'has_completed_focus') == 'LTB_the_vilnius_compromise' for negation in values(conditions, 'NOT')), f'{context}: a completed compromise can split solely because settlement flags are missing')

bookmark = one(one(read(ROOT/'common/bookmarks/nww_1936.txt'), 'bookmarks'), 'bookmark')
major_entries = [key for key, value, op in bookmark if (len(key) == 3 and key.isupper()) and one(value, 'minor') != 'yes']
check(len(major_entries) <= 7, f'Selection screen has {len(major_entries)} major countries; vanilla has seven plus Other')
check(not values(bookmark, 'BYE'), 'Belarus is incorrectly offered as a starting country before the split')
check(one(bookmark, '---') is not None, 'Selection screen is missing Other')
startup = one(one(read(ROOT/'common/on_actions/nww_ltb_on_actions.txt'), 'on_actions'), 'on_startup')
check(any(k == 'activate_mission' and v == 'LTB_vilnius_compromise_deadline' for k,v,o in walk(startup)), 'Compromise timer is not explicitly activated on startup')
mission = one(one(read(ROOT/'common/decisions/nww_ltb_decisions.txt'), 'LTB_national_question'), 'LTB_vilnius_compromise_deadline')
check(one(mission, 'days_mission_timeout') == '210', 'Compromise deadline must remain 210 days')
check(one(one(mission, 'activation'), 'always') == 'no', 'Startup mission must not activate again automatically')

# Diplomacy regression: a completed request is not an accepted treaty.
ltb_focuses = {one(f,'id'):f for f in values(one(read(ROOT/'common/national_focus/ltb_focus.txt'),'focus_tree'),'focus')}
diplomatic_events = {one(e,'id'):e for e in values(read(ROOT/'events/nww_ltb_diplomacy.txt'),'country_event')}

# Crisis and politics regression: army reform waits for the compromise and
# crisis settlement; a new ruling party must have a genuine public mandate.
staff = ltb_focuses['LTB_union_general_staff']
check(any(k == 'has_completed_focus' and v == 'LTB_the_vilnius_compromise' for k,v,o in walk(one(staff, 'available', []))), 'General staff no longer requires the Vilnius compromise')
check(not values(staff, 'prerequisite'), 'General staff draws a connection across unrelated branches; use availability conditions for the crisis gates')
check('LTB_face_the_crisis' not in values(one(staff, 'available', []), 'has_completed_focus'), 'General staff still needs a redundant crisis focus after the peaceful settlement')

# The compromise must resolve the crisis itself: bypass skips completion rewards.
# In particular, a January settlement must not wait for the crisis's June availability.
crisis = ltb_focuses['LTB_face_the_crisis']
settlement = one(read(ROOT/'common/scripted_effects/nww_ltb_effects.txt'), 'nww_ltb_resolve_compromise', [])
settlement_branch = one(settlement, 'if', [])
settlement_limit = one(settlement_branch, 'limit', [])
check(one(one(ltb_focuses['LTB_the_vilnius_compromise'], 'completion_reward'), 'nww_ltb_resolve_compromise') == 'yes', 'Compromise does not settle the crisis in its own reward')
check({'LTB_union_preserved', 'LTB_deadline_resolved'} <= set(values(settlement_branch, 'set_country_flag')), 'Peaceful settlement leaves the Union or deadline unresolved')
check('LTB_deadline_active' in values(settlement_branch, 'clr_country_flag'), 'Peaceful settlement leaves the deadline active')
check(any(k == 'remove_mission' and v == 'LTB_vilnius_compromise_deadline' for k,v,o in walk(settlement)), 'Peaceful settlement does not stop the mission')
check(any(one(n, 'has_country_flag') == 'LTB_split_choice_available' for n in values(settlement_limit, 'NOT')), 'Peaceful settlement can override a dissolution already triggered')
check(not any(k in ('country_event', 'news_event', 'complete_national_focus') for k,v,o in walk(settlement)), 'Peaceful settlement executes crisis events or completion rewards')
bypass = one(crisis, 'bypass', [])
check(one(bypass, 'has_completed_focus') == 'LTB_the_vilnius_compromise' and any(one(n, 'has_country_flag') == 'LTB_split_choice_available' for n in values(bypass, 'NOT')), 'Crisis bypass is missing or bypasses an unresolved dissolution')
check(not any(k == 'date' for k,v,o in walk(bypass)), 'Peaceful crisis bypass still waits for June')
check(one(crisis, 'bypass_if_unavailable') != 'yes', 'Crisis could bypass solely because the June start date has not arrived')
check(one(one(crisis, 'bypass_effect', []), 'nww_ltb_resolve_compromise') == 'yes', 'Bypassed crisis does not preserve settlement flags')
startup_repairs = [branch for k,branch,o in walk(startup) if k == 'if' and one(branch, 'nww_ltb_resolve_compromise') == 'yes']
check(any(one(one(branch, 'limit', []), 'has_completed_focus') == 'LTB_the_vilnius_compromise' for branch in startup_repairs), 'Completed compromises are not reconciled on startup')
political_routes = [
    ('LTB_crown_the_regency', 'neutrality'), ('LTB_free_elections_now', 'democratic'),
    ('LTB_the_iron_wolf_calls', 'fascism'), ('LTB_red_dawn_over_minsk', 'communism')]
campaigns = one(read(ROOT/'common/decisions/nww_ltb_decisions.txt'), 'LTB_political_mandate')

# Evaluate the actual condition blocks against the reported old-save state.
# This deliberately implements only the Boolean/country primitives used here,
# not the HOI4 engine. Unsupported conditions fail instead of being ignored.
def settlement_conditions(block, completed, flags, missions=frozenset(), tag='LTB'):
    results = []
    for key, value, op in block:
        if key == 'tooltip':
            continue
        if key == 'has_completed_focus':
            result = value in completed
        elif key == 'has_country_flag':
            result = value in flags
        elif key == 'has_active_mission':
            result = value in missions
        elif key == 'tag':
            result = value == tag
        elif key in ('AND', 'NOT'):
            result = settlement_conditions(value, completed, flags, missions, tag)
            if key == 'NOT':
                result = not result
        elif key == 'OR':
            result = any(settlement_conditions([entry], completed, flags, missions, tag) for entry in value)
        else:
            raise ValueError(f'Unsupported settlement condition: {key}')
        results.append(result)
    return all(results)

daily = one(one(read(ROOT/'common/on_actions/nww_ltb_on_actions.txt'), 'on_actions'), 'on_daily_LTB', [])
daily_repair = one(one(daily, 'effect', []), 'if', [])
check(one(daily_repair, 'nww_ltb_resolve_compromise') == 'yes', 'Old-save settlement is not repaired on the daily country tick')
cases = [
    ('reported missing Union flag', {'LTB_the_vilnius_compromise'}, {'LTB_deadline_resolved'}, True, True),
    ('fully reconciled settlement', {'LTB_the_vilnius_compromise'}, {'LTB_deadline_resolved', 'LTB_union_preserved'}, True, False),
    ('no compromise', set(), {'LTB_deadline_resolved'}, False, False),
    ('dissolution already triggered', {'LTB_the_vilnius_compromise'}, {'LTB_split_choice_available'}, False, False),
]
peaceful_ids = {'LTB_union_general_staff', 'LTB_the_union_endures', 'LTB_balance_between_giants', 'LTB_professional_contract_army', 'LTB_national_resilience', *[route for route, ideology in political_routes]}
for token, entity in [(fid, ltb_focuses[fid]) for fid in peaceful_ids] + [(k,v) for k,v,o in campaigns]:
    available = one(entity, 'available', [])
    gates = [g for g in values(available, 'custom_trigger_tooltip') if one(g, 'tooltip') == 'LTB_union_preserved']
    check(len(gates) == 1, f'{token}: missing verified-compromise gate')
    check(not any(k == 'has_country_flag' and v in ('LTB_union_preserved', 'LTB_deadline_resolved') for k,v,o in walk(available)), f'{token}: auxiliary settlement flags can block a completed compromise')
    for scenario, completed, flags, expected, repair in cases:
        if gates:
            check(settlement_conditions(gates[0], completed, flags) == expected, f'{token}: incorrect access in scenario {scenario}')
for scenario, completed, flags, access, expected_repair in cases:
    check(settlement_conditions(one(daily_repair, 'limit', []), completed, flags) == expected_repair, f'Daily reconciliation: incorrect behaviour in scenario {scenario}')

for route, ideology in political_routes:
    focus = ltb_focuses[route]
    gates = one(focus, 'available', [])
    check(any((ideology, '0.40', '<') in negation for negation in values(gates, 'NOT')), f'{route}: ruling-party change does not require at least 40% popularity')
    check(any('LTB_public_political_debate' in values(group, 'focus') for group in values(focus, 'prerequisite')), f'{route}: political preparation is bypassed')
    check(one(focus, 'cancel_if_invalid') == 'yes' and one(focus, 'continue_if_invalid') == 'no', f'{route}: support can fall below the mandate during the focus')
    check(not values(one(focus, 'completion_reward'), 'add_popularity'), f'{route}: transition still supplies its own party popularity')
    campaign = one(campaigns, 'LTB_campaign_' + ideology, [])
    check(one(campaign, 'days_remove') == '60' and one(campaign, 'cost') == '50', f'{ideology}: campaign duration/cost has changed')
    check(not any(k == 'add_popularity' for k,v,o in walk(one(campaign, 'complete_effect', []))), f'{ideology}: popularity is granted immediately instead of after campaigning')
    check(one(one(one(campaign, 'remove_effect', []), 'add_popularity', []), 'popularity') == '0.10', f'{ideology}: campaign completion has no popularity reward')
    check(any(one(n, 'has_country_flag') == 'LTB_political_campaign_active' for n in values(one(campaign, 'available', []), 'NOT')), f'{ideology}: campaigns can run simultaneously')
concerns = one(one(read(ROOT/'common/ideas/nww_companies.txt'), 'ideas'), 'industrial_concern')
for base, advanced, gate in [
    ('LTB_minsk_industry_company', 'LTB_minsk_industry_company_advanced', 'LTB_precision_engineering'),
    ('LTB_vilnius_university_concern_company', 'LTB_vilnius_university_concern_company_advanced', 'LTB_minsk_university')]:
    basic_visible = one(one(concerns, base), 'visible', [])
    upgraded_visible = one(one(concerns, advanced), 'visible', [])
    check(any(one(n, 'has_completed_focus') == gate for n in values(basic_visible, 'NOT')) and one(upgraded_visible, 'has_completed_focus') == gate, f'{base}: both concern tiers can appear together')

# Enterprise regression: a focus-gated trait needs the matching focus reward,
# and the second local tier must actually depend on the first one.
for organization_id, organization, op in read(ROOT/'common/military_industrial_organization/organizations/nww_organizations.txt'):
    upgrades = values(organization, 'add_trait')
    local_tokens = {one(trait, 'token') for trait in upgrades}
    positions = []
    for trait in upgrades:
        token = one(trait, 'token')
        position = one(trait, 'position', [])
        positions.append((one(position, 'x'), one(position, 'y')))
        gates = values(one(one(trait, 'available', []), 'FROM', []), 'has_completed_focus')
        check(bool(gates), f'{token}: local enterprise upgrade has no country focus gate')
        for gate in gates:
            reward = one(ltb_focuses.get(gate, []), 'completion_reward', [])
            scopes = [value for key, value, op in walk(reward) if key == 'mio:' + organization_id]
            check(any(one(scope, 'unlock_mio_trait_tooltip') == token and int(one(scope, 'add_mio_size', '0')) > 0 for scope in scopes), f'{token}: {gate} does not announce and fund this enterprise upgrade')
        if token.endswith('_2'):
            parents = {value for key, value, op in one(one(trait, 'parent', []), 'traits', [])}
            check(token[:-1] + '1' in parents and parents <= local_tokens, f'{token}: second upgrade lacks its local first-tier prerequisite')
    check(len(positions) == len(set(positions)), f'{organization_id}: overlapping local enterprise upgrades')

for request, event_id, accepted_flag, rejected_flag, continuation in [
    ('LTB_overture_to_moscow','ltb.130','LTB_moscow_agreement','LTB_moscow_rejected','LTB_dvina_border_commission'),
    ('LTB_the_polish_question','ltb.131','LTB_polish_agreement','LTB_polish_rejected','LTB_polish_defense_protocol'),
    ('LTB_german_engineers','ltb.132','LTB_german_agreement','LTB_german_rejected','LTB_german_machine_tools')]:
    reward = one(ltb_focuses[request],'completion_reward')
    check(not any(k in ('add_tech_bonus','add_timed_idea','add_building_construction') for k,v,o in walk(reward)), f'{request}: request grants agreement rewards before the foreign reply')
    options = values(diplomatic_events[event_id],'option')
    accepted = {v for k,v,o in walk(options[0]) if k == 'set_country_flag'}
    rejected = {v for k,v,o in walk(options[1]) if k == 'set_country_flag'}
    check(accepted_flag in accepted and accepted_flag not in rejected, f'{event_id}: rejected proposal can mark agreement accepted')
    check(rejected_flag in rejected, f'{event_id}: rejection cannot unlock independent neutrality')
    check(accepted_flag in values(one(ltb_focuses[continuation],'available'),'has_country_flag'), f'{continuation}: foreign consent is not required')

for message in dict.fromkeys(errors):
    print('ERROR:', message)
if errors:
    print(f'FAILED: {len(set(errors))} distinct errors')
    sys.exit(1)
print('PASS:', ', '.join(f'{key}: {value} focuses' for key, value in counts.items()))
print('PASS: prerequisites/exclusive paths, spacing and panel clearance, localization and unique sprites, portrait bounds, traits and recruitment, concern tier visibility, MIO upgrades, technology sharing, construction, selection menu, startup mission, army crisis gate, 40% political mandates, timed campaigns and diplomatic acceptance/refusal gates')
