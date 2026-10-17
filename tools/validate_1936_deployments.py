"""Check scenario deployment ownership across native DLC OOB variants."""
import argparse
import hashlib
import json
from pathlib import Path

from hoi4_script import one, parse, read, values, walk

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--game', default='D:/Steam/steamapps/common/Hearts of Iron IV')
GAME = Path(parser.parse_args().game)
errors = []


def check(ok, message):
    if not ok:
        errors.append(message)


def effective(folder):
    result = {p.name: p for p in (GAME / folder).glob('*.txt')}
    result.update({p.name: p for p in (ROOT / folder).glob('*.txt')})
    return result


states, provinces = {}, {}
for path in effective('history/states').values():
    state = one(read(path), 'state')
    sid = one(state, 'id')
    states[sid] = state
    owner = one(one(state, 'history', []), 'owner')
    for _, pid, _ in one(state, 'provinces', []):
        provinces[pid] = (sid, owner)

manifest = json.loads((ROOT / 'docs/1936_deployment_manifest.json').read_text())
units = effective('history/units')
for filename, expected in manifest.items():
    tag = filename[:3]
    doc = read(units[filename])
    divisions = values(one(doc, 'units', []), 'division')
    locations = [one(d, 'location') for d in divisions]
    check(len(divisions) == expected['divisions'], f'{filename}: changed army size')
    check(len(set(locations)) == expected['positions'], f'{filename}: changed deployment coverage')
    for location in locations:
        check(provinces.get(location, (None, None))[1] == tag,
              f'{filename}: division outside its country at {location}')
    if tag == 'AUS':
        check(len(divisions) == 18, 'Austria: expected 12 + 50% = 18 divisions')
        check(all(one(d, 'start_equipment_factor') == '1' for d in divisions),
              'Austria: starting divisions must be equipped')
        templates = {one(t, 'name') for t in values(doc, 'division_template')}
        check(all(one(d, 'division_template') in templates for d in divisions),
              'Austria: missing division template')
    if tag == 'FRA':
        source = (GAME / 'history/units' / filename).read_text(encoding='utf-8-sig')
        # These installed French OOBs omit the final instant_effect brace.
        original = values(one(parse(source + '\n}'), 'units', []), 'division')
        border = json.loads((ROOT / 'docs/1936_french_border.json').read_text())['provinces']
        for before, after in zip(original, divisions):
            if provinces.get(one(before, 'location'), (None, None))[0] == '28':
                check(one(after, 'location') in border,
                      f'{filename}: former Alsace division is away from the border')

# Check fleets embedded in old land OOBs as well as the separate MTG files.
for filename, path in units.items():
    tag = filename[:3]
    if tag not in {'ENG', 'FRA', 'ITA'} or not filename.startswith(tag + '_1936'):
        continue
    if 'african_oob' in filename:
        continue
    doc = read(path)
    for key, value, _ in walk(doc):
        if key in {'location', 'naval_base'}:
            sid, owner = provinces.get(value, (None, None))
            check(owner not in {'TUR', 'AUS', 'GER'},
                  f'{filename}: foreign deployment at {value} ({owner})')
            check(not (tag == 'ITA' and sid == '164'), f'{filename}: Italian fleet on Rhodes')
    for sid, _, _ in one(doc, 'air_wings', []):
        if sid in states:
            owner = one(one(states[sid], 'history', []), 'owner')
            check(owner not in {'TUR', 'AUS', 'GER'}, f'{filename}: foreign air base in {sid}')

dodecanese = one(states['164'], 'history', [])
check(one(dodecanese, 'owner') == 'TUR', 'Dodecanese: wrong starting owner')
check('GRE' in values(dodecanese, 'add_core_of'), 'Dodecanese: lost indigenous core')
balkans = {'YUG', 'ROM', 'GRE', 'BUL', 'TUR', 'CRO', 'SER', 'MNT', 'BOS', 'MAC', 'SLV', 'KOS'}
albanian_guarantee = False
for path in effective('history/countries').values():
    tag = path.name[:3]
    if 'give_guarantee' not in path.read_text(encoding='utf-8-sig'):
        continue
    for key, target, _ in walk(read(path)):
        if key == 'give_guarantee':
            check(target == 'ALB' or (tag not in balkans and target not in balkans),
                  f'{path.name}: inherited Balkan guarantee to {target}')
            albanian_guarantee |= tag == 'ITA' and target == 'ALB'
check(albanian_guarantee, 'Albania: Italian guarantee must remain')

for size in ['', 'medium', 'small']:
    reference = (GAME / 'gfx/flags' / size / 'AUS_austrian_empire_neutrality.tga').read_bytes()
    for filename in ['AUS.tga', 'AUS_neutrality.tga']:
        current = (ROOT / 'gfx/flags' / size / filename).read_bytes()
        check(hashlib.sha256(current).digest() == hashlib.sha256(reference).digest(),
              f'Austria: incorrect imperial flag {size}/{filename}')

tree = one(read(ROOT / 'common/national_focus/TUR_focuses.txt'), 'focus_tree')
focuses = {one(f, 'id'): f for f in values(tree, 'focus')}
for fid, year, factories, prerequisite in [
    ('TUR_research_1', '1937.1.1', '29', 'TUR_Factory_1'),
    ('TUR_research_2', '1939.1.1', '49', 'TUR_civ_factory_2'),
]:
    focus = focuses[fid]
    available = one(focus, 'available', [])
    check(one(focus, 'cost') == '10', f'{fid}: expected 70-day research focus')
    for condition in [('date', year, '>'), ('num_of_factories', factories, '>'),
                      ('has_completed_focus', prerequisite, '='),
                      ('amount_research_slots', '5', '<')]:
        check(condition in available, f'{fid}: missing progression gate {condition}')
    rewards = one(focus, 'completion_reward', [])
    check(('amount_research_slots', '5', '<') in list(walk(rewards)),
          f'{fid}: missing reward cap')

if errors:
    print('\n'.join('FAIL: ' + error for error in errors))
    raise SystemExit(1)
print(f'PASS: {len(manifest)} army variants, fleet/air bases, Balkan guarantees, imperial flags and TUR research gates')
