"""Validate MKN personnel assets and execute the actual service timer script."""
import hashlib
import json
import re
from itertools import product

from PIL import Image

from hoi4_script import engine_script_errors, one, read, values, walk


def validate_personnel(root, game, check, localized):
    paths = (
        'common/characters/MKN_eugen.txt', 'common/country_leader/MKN_eugen_traits.txt',
        'common/unit_leader/MKN_eugen_traits.txt', 'common/ideas/MKN_eugen_ideas.txt',
        'common/scripted_effects/MKN_personnel_effects.txt',
        'common/on_actions/MKN_personnel_on_actions.txt', 'events/MKN_personnel_events.txt',
        'interface/MKN_personnel.gfx',
    )
    for filename in paths:
        for error in engine_script_errors(read(root / filename)):
            check(False, f'{filename}: {error}')
    character = one(one(read(root / paths[0]), 'characters'), 'NWW_MKN_eugen')
    check(bool(one(character, 'corps_commander')) and len(values(character, 'advisor')) == 1,
          'MKN: Eugen must be one character with two roles')
    advisor = one(character, 'advisor')
    check(one(advisor, 'slot') == 'high_command' and one(advisor, 'cost') == '200',
          'MKN: Eugen must occupy a paid army high-command slot')
    check(one(one(advisor, 'available'), 'has_completed_focus') == 'MKN_steppe_general_staff',
          'MKN: Eugen advisor bypasses staff preparation')
    for token in ('NWW_MKN_eugen', 'NWW_MKN_eugen_high_command', 'mkn_eugen_infantry_master',
                  'mkn_eugen_under_fire', 'MKN_eugen_under_fire_tt', 'MKN_dmitruk_tratishov'):
        localized(token, 'MKN personnel')

    native_modifiers = set(re.findall(r'^## (\w+)',
        (game / 'documentation/modifiers_documentation.md').read_text(), re.M))
    for filename in paths[1:4]:
        for key, node, _ in walk(read(root / filename)):
            if key == 'modifier':
                for name, _, _ in node:
                    check(name in native_modifiers, f'{filename}: unknown modifier {name}')
    trait = one(one(read(root / paths[1]), 'leader_traits'), 'mkn_eugen_infantry_master')
    for name in ('army_infantry_attack_factor', 'army_infantry_defence_factor', 'army_morale_factor'):
        check(name in native_modifiers, f'MKN advisor: unknown modifier {name}')
    check(one(trait, 'army_infantry_attack_factor') == '0.15'
          and one(trait, 'army_infantry_defence_factor') == '0.15', 'MKN: infantry master balance drift')

    effects = read(root / paths[4])
    repair = one(effects, 'MKN_repair_personnel')
    check(not any(k in ('set_politics', 'set_popularities', 'add_political_power',
                       'complete_national_focus', 'retire_character') for k, _, _ in walk(repair)),
          'MKN personnel repair changes politics, grants rewards or retires military characters')
    check(one(one(one(repair, 'if'), 'limit'), 'NOT') == [('has_country_flag', 'MKN_personnel_v1', '=')],
          'MKN personnel repair is not version guarded')
    history = read(root / 'history/countries/MKN - Makhnovists.txt')
    check(one(history, 'MKN_repair_personnel') == 'yes', 'MKN: new campaigns do not recruit Eugen')
    for leader in values(history, 'create_country_leader'):
        if one(leader, 'ideology') == 'fascism_ideology':
            check(one(leader, 'name') == 'MKN_dmitruk_tratishov', 'MKN: old starting fascist leader')
    successor = one(read(root / 'common/scripted_effects/MKN_effects.txt'), 'MKN_install_fascism_successor')
    check(one(one(successor, 'create_country_leader'), 'name') == 'MKN_dmitruk_tratishov',
          'MKN: funeral/civil-war successor still installs Belash')

    events = read(root / paths[6])
    event, news = one(events, 'country_event'), one(events, 'news_event')
    for node in (event, news):
        for suffix in ('.t', '.d'):
            localized(one(node, 'id') + suffix, 'MKN personnel event')
        for option in values(node, 'option'):
            localized(one(option, 'name'), 'MKN personnel event')
    check(one(event, 'fire_only_once') == 'yes' and one(news, 'major') == 'yes'
          and one(news, 'is_triggered_only') == 'yes', 'MKN: story/news can repeat or broadcast incorrectly')
    immediate = one(event, 'immediate')
    check(one(one(immediate, 'news_event'), 'id') == one(news, 'id'), 'MKN rescue news is disconnected')
    choices = values(event, 'option')
    for option in choices:
        reward = one(option, 'add_timed_idea')
        check(reward is not None and int(one(reward, 'days')) <= 180,
              'MKN: event must grant a temporary, bounded national spirit')
    check(one(choices[1], 'add_political_power') == '-50', 'MKN: instructor courses have no cost')

    def conditions(nodes, state):
        results = []
        for key, value, op in nodes:
            if key == 'NOT': answer = not conditions(value, state)
            elif key == 'OR': answer = any(conditions([item], state) for item in value)
            elif key == 'tag': answer = state.get('tag', 'MKN') == value
            elif key == 'date': answer = tuple(map(int, state.get('date', '1940.1.1').split('.'))) > tuple(map(int, value.split('.')))
            elif key == 'has_war': answer = state['war'] == (value == 'yes')
            elif key == 'has_character': answer = state['character']
            elif key == 'NWW_MKN_eugen': answer = conditions(value, state)
            elif key == 'is_leading_army': answer = state['assigned']
            elif key == 'political_power': answer = state['pp'] < float(value)
            elif key == 'has_country_flag':
                if isinstance(value, str): answer = value in state['flags']
                else:
                    flag = one(value, 'flag')
                    answer = flag in state['flags'] and state['day'] - state['flags'][flag] > int(one(value, 'days'))
            else: raise AssertionError(f'Unsupported personnel condition: {key}')
            results.append(answer)
        return all(results)

    def apply(nodes, state):
        matched = False
        for key, value, _ in nodes:
            if key == 'if':
                matched = conditions(one(value, 'limit'), state)
                if matched: apply([item for item in value if item[0] != 'limit'], state)
            elif key == 'else':
                if not matched: apply(value, state)
            elif key == 'set_country_flag': state['flags'][value] = state['day']
            elif key == 'clr_country_flag': state['flags'].pop(value, None)
            else: raise AssertionError(f'Unsupported personnel timer effect: {key}')

    service = one(effects, 'MKN_update_eugen_front_service')
    gate = one(event, 'trigger')
    cases = 0
    for war, assigned, character_exists, collapsed, happened in product((False, True), repeat=5):
        state = dict(war=war, assigned=assigned, character=character_exists, day=0, flags={})
        if collapsed: state['flags']['MKN_collapse_started'] = 0
        if happened: state['flags']['MKN_eugen_rescue_happened'] = 0
        apply(service, state)
        state['day'] = 31
        apply(service, state)
        check(conditions(gate, state) == (war and assigned and character_exists and not collapsed and not happened),
              f'MKN: invalid rescue eligibility for {state}')
        cases += 1
    state = dict(war=True, assigned=True, character=True, day=0, flags={})
    apply(service, state)
    state['day'] = 30
    check(not conditions(gate, state), 'MKN: rescue occurs before 30 days of service')
    state['day'] = 31
    check(conditions(gate, state), 'MKN: rescue never unlocks after continuous service')
    for interrupt in ('war', 'assigned'):
        state[interrupt] = False
        apply(service, state)
        check('MKN_eugen_front_service' not in state['flags'], f'MKN: {interrupt} does not reset service')
        state[interrupt] = True
        apply(service, state)
        check(not conditions(gate, state), 'MKN: interrupted service retains its previous timer')
    state['day'] = 62
    for date, expected in (('1936.5.31', False), ('1936.6.1', True)):
        state['date'] = date
        check(conditions(gate, state) == expected, 'MKN: rescue date gate is incorrect')
    for pp, expected in ((0, False), (49.9, False), (50, True), (200, True)):
        check(conditions(one(choices[1], 'trigger'), dict(pp=pp)) == expected,
              f'MKN: courses affordability is wrong at {pp} PP')

    assets = json.loads((root / 'docs/art/MKN_personnel_assets.json').read_text())
    for entry in assets:
        check(hashlib.sha256((root / entry['source']).read_bytes()).hexdigest() == entry['source_sha256'],
              f'MKN: source changed without rebuilding {entry["target"]}')
        with Image.open(root / entry['target']) as image:
            check(image.size == tuple(entry['size']) and image.format == 'DDS', 'MKN: invalid personnel texture')
            if 'alpha_bounds' in entry:
                bounds = image.convert('RGBA').getchannel('A').getbbox()
                check(image.size == (65, 67) and bounds is not None and bounds[3] <= 61,
                      'MKN: advisor artwork extends below its card')
            else:
                check(image.convert('RGBA').getchannel('A').getextrema() == (255, 255),
                      'MKN: general/leader/news must retain an opaque background')
    for node in values(one(read(root / paths[7]), 'spriteTypes'), 'spriteType'):
        texture = one(node, 'texturefile')
        check((root / texture).is_file() or (game / texture).is_file(), f'MKN: missing personnel texture {texture}')
    print(f'PASS: MKN personnel, {cases} service combinations, interruption/date/affordability gates, source hashes and native textures')
