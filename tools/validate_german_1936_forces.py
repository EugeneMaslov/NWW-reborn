"""Check imperial force completeness, DLC parity, carrier decks and technology parity."""
from collections import Counter
import itertools
import json
from pathlib import Path

from hoi4_script import engine_script_errors, one, read, values, walk

ROOT = Path(__file__).resolve().parents[1]
GAME = Path('D:/Steam/steamapps/common/Hearts of Iron IV')
errors = []


def check(ok, message):
    if not ok:
        errors.append(message)


def effective(folder):
    result = {p.name: p for p in (GAME / folder).glob('*.txt')}
    result.update({p.name: p for p in (ROOT / folder).glob('*.txt')})
    return result.values()


provinces, states = {}, {}
for path in effective('history/states'):
    state = one(read(path), 'state')
    sid = one(state, 'id')
    states[sid] = state
    for _, pid, _ in one(state, 'provinces', []):
        provinces[pid] = (sid, one(one(state, 'history', []), 'owner'))
manifest = json.loads((ROOT / 'docs/GER_1936_forces.json').read_text())
effects = dict((k, v) for k, v, _ in read(ROOT / 'common/scripted_effects/GER_military_setup_effects.txt'))


def condition(node, dlcs):
    results = []
    for key, value, op in node:
        if key.lower() == 'not':
            results.append(not condition(value, dlcs))
        elif key.lower() == 'or':
            results.append(any(condition([entry], dlcs) for entry in value))
        elif key.lower() == 'and':
            results.append(condition(value, dlcs))
        elif key == 'has_dlc':
            results.append(value in dlcs)
        elif key == 'always':
            results.append(value == 'yes')
        else:
            results.append(False)
    return all(results)


def initial_technologies(doc, dlcs):
    result = set()
    for key, value, op in doc:
        if key == 'set_technology':
            result.update(k for k, v, _ in value if v == '1')
        elif key in effects:
            result.update(initial_technologies(effects[key], dlcs))
        elif key.lower() == 'if':
            if condition(one(value, 'limit', []), dlcs):
                result.update(initial_technologies([entry for entry in value if entry[0] not in {'else', 'else_if'}], dlcs))
            else:
                for name, branch, _ in value:
                    if name == 'else' or (name == 'else_if' and condition(one(branch, 'limit', []), dlcs)):
                        result.update(initial_technologies(branch, dlcs))
                        break
    return result


tech_definitions, equipment = {}, set()
for path in effective('common/technologies'):
    try:
        tech_definitions.update({k: v for k, v, _ in one(read(path), 'technologies', [])})
    except ValueError:
        continue
for path in effective('common/units/equipment'):
    try:
        equipment.update(k for k, v, _ in walk(read(path)) if isinstance(v, list) or
                         (isinstance(v, str) and ('airframe' in str(k))))
    except ValueError:
        continue
for filename in ['GER_1936.txt', 'GER_1936_nsb.txt']:
    doc = read(ROOT / 'history/units' / filename)
    templates = {one(t, 'name') for t in values(doc, 'division_template')}
    divisions = values(one(doc, 'units'), 'division')
    check(len(divisions) == 84, filename + ': wrong army size')
    check(Counter(one(d, 'division_template') for d in divisions) == manifest['divisions'],
          filename + ': incorrect army composition')
    for division in divisions:
        check(one(division, 'division_template') in templates, filename + ': missing template')
        check(one(division, 'start_equipment_factor') == '1', filename + ': unequipped division')
        check(provinces[one(division, 'location')][1] == 'GER', filename + ': division abroad')

navies = []
for filename in ['GER_1936_naval_mtg.txt', 'GER_1936_naval.txt']:
    doc = read(ROOT / 'history/units' / filename)
    ships = [node for key, node, _ in walk(doc) if key == 'ship']
    roster = {one(ship, 'name'): one(ship, 'definition') for ship in ships}
    navies.append(roster)
    check(len(roster) == len(ships) == 163, filename + ': duplicate/missing ships')
    check(Counter(roster.values()) == manifest['ships'], filename + ': wrong fleet composition')
    for key, value, _ in walk(doc):
        if key in {'naval_base', 'location'}:
            check(provinces[value][1] == 'GER', filename + ': foreign fleet base')
    for fleet in values(one(doc, 'units'), 'fleet'):
        for group in values(fleet, 'task_force'):
            composition = Counter(one(ship, 'definition') for ship in values(group, 'ship'))
            if composition['carrier']:
                screens = composition['destroyer'] + composition['light_cruiser']
                capitals = sum(composition[t] for t in ['carrier', 'battleship', 'battle_cruiser', 'heavy_cruiser'])
                check(screens >= capitals * 3, filename + ': carrier group lacks screens')
check(navies[0] == navies[1], 'Fleet differs with and without MTG')
variants = {one(node, 'name'): node for key, node, _ in walk(
            read(ROOT / 'common/scripted_effects/GER_military_setup_effects.txt')) if key == 'create_equipment_variant'}
for name in ['NWW Europa', 'NWW Flugzeugtraeger']:
    design = variants[name]
    check(sum(value == 'ship_deck_space' for key, value, _ in one(design, 'modules')) == 3,
          name + ': expected three deck modules (60 planes)')
legacy_equipment = one(read(GAME / 'common/units/equipment/ship_hull_carrier.txt'), 'equipments')
legacy_upgrade = one(variants['NWW Europa Legacy'], 'upgrades')
for ship in [node for key, node, _ in walk(read(ROOT / 'history/units/GER_1936_naval.txt'))
             if key == 'ship' and one(node, 'definition') == 'carrier']:
    kind, design, _ = one(ship, 'equipment')[0]
    capacity = int(one(one(legacy_equipment, kind), 'carrier_size'))
    if one(design, 'version_name') == 'NWW Europa Legacy':
        capacity += int(one(legacy_upgrade, 'ship_deckspace_upgrade'))
    check(capacity * 10 >= 60, one(ship, 'name') + ': legacy carrier deck overloaded')
for suffix in ['bba', 'legacy']:
    doc = read(ROOT / f'history/units/GER_1936_air_{suffix}.txt')
    wings = one(doc, 'air_wings')
    total = sum(int(v) for k, v, _ in walk(wings) if k == 'amount')
    check(total == 2160, suffix + ': wrong aircraft total')
    by_state = Counter()
    for location, group, _ in wings:
        amount = sum(int(v) for k, v, _ in walk(group) if k == 'amount')
        if location in states:
            check(one(one(states[location], 'history'), 'owner') == 'GER', suffix + ': foreign air base')
            by_state[location] += amount
        else:
            check(navies[0].get(location) == 'carrier' and amount == 60,
                  suffix + ': deck wing missing carrier or exceeding capacity')
    for sid, amount in by_state.items():
        capacity = int(one(one(one(states[sid], 'history'), 'buildings'), 'air_base', '0')) * 200
        check(amount <= capacity, suffix + ': overloaded air base ' + sid)

ger = read(ROOT / 'history/countries/GER - Germany.txt')
text = (ROOT / 'history/countries/GER - Germany.txt').read_text(encoding='utf-8-sig')
check(text.index('GER_nww_1936_military_technology = yes') > text.index('name = Bismarck'),
      'Custom variants are created before native starting designs/research')
eng = read(ROOT / 'history/countries/ENG - Britain.txt')
counts = []
dlc_names = ['Man the Guns', 'No Step Back', 'By Blood Alone', 'La Resistance', 'Battle for the Bosporus']
for bits in itertools.product([False, True], repeat=len(dlc_names)):
    dlcs = {name for name, enabled in zip(dlc_names, bits) if enabled}
    german, british = initial_technologies(ger, dlcs), initial_technologies(eng, dlcs)
    counts.append((len(german), len(british)))
    check(len(german) >= len(british), f'Technology parity failed: {dlcs}: {len(german)} < {len(british)}')
    check(not (german - tech_definitions.keys()), 'Unknown German technology: ' + str(german - tech_definitions.keys()))
for name, variant in variants.items():
    check(one(variant, 'type') in equipment, name + ': unknown equipment type')
for path in [ROOT / 'common/scripted_effects/GER_military_setup_effects.txt',
             *sorted((ROOT / 'history/units').glob('GER_1936*.txt'))]:
    check(not list(engine_script_errors(read(path))), str(path) + ': engine script error')
if errors:
    print('\n'.join('FAIL: ' + error for error in errors))
    raise SystemExit(1)
print(f'PASS: 84 equipped divisions, 163 ships with DLC parity, three screened 60-plane carriers, '
      f'2160 aircraft within base capacity; technology parity in {len(counts)} DLC combinations '
      f'(GER {min(n for n, _ in counts)}–{max(n for n, _ in counts)}, ENG '
      f'{min(n for _, n in counts)}–{max(n for _, n in counts)})')
