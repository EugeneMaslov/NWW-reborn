"""Check effective map inputs, including sites required before campaign launch."""
from collections import Counter, defaultdict
import csv
from pathlib import Path

from PIL import Image
from hoi4_script import read, one, values, walk


def effective_files(root, game, folder):
    files = {p.name: p for p in (game / folder).glob('*.txt')}
    files.update({p.name: p for p in (root / folder).glob('*.txt')})
    return files.values()


def validate_map_initialization(root, game, check):
    failures = []
    report = check
    def check(condition, message):
        if not condition:
            failures.append(message)
        report(condition, message)
    definition = root / 'map/definition.csv'
    if not definition.exists():
        definition = game / 'map/definition.csv'
    with definition.open(encoding='utf-8-sig', newline='') as source:
        provinces = {r[0]: r for r in csv.reader(source, delimiter=';')
                     if r and r[0].isdigit() and r[0] != '0'}
    region_membership = Counter()
    region_ids = Counter()
    for path in effective_files(root, game, 'map/strategicregions'):
        region = one(read(path), 'strategic_region')
        region_ids[one(region, 'id')] += 1
        region_membership.update(v for k, v, op in one(region, 'provinces', []))
    check(all(n == 1 for n in region_ids.values()), 'Map: duplicate strategic-region IDs')
    missing_regions = [pid for pid in provinces if region_membership[pid] != 1]
    check(not missing_regions, f'Map: missing or overlapping strategic regions: {missing_regions[:20]}')
    check(not (region_membership.keys() - provinces.keys()), 'Map: strategic region references an unknown province')

    states, province_states = {}, defaultdict(list)
    for path in effective_files(root, game, 'history/states'):
        state = one(read(path), 'state')
        sid = one(state, 'id')
        check(sid not in states, f'Map: duplicate state ID {sid}')
        states[sid] = state
        for k, pid, op in one(state, 'provinces', []):
            province_states[pid].append(sid)
    check(all(len(sids) == 1 for sids in province_states.values()), 'Map: province belongs to multiple states')
    check(not (province_states.keys() - provinces.keys()), 'Map: state references an unknown province')
    for pid, definition_row in provinces.items():
        if definition_row[4] == 'land':
            check(len(province_states[pid]) == 1, f'Map: land province {pid} has no unique state')

    sites = defaultdict(list)
    buildings_path = root / 'map/buildings.txt'
    if not buildings_path.exists():
        buildings_path = game / 'map/buildings.txt'
    for number, line in enumerate(buildings_path.read_text().splitlines(), 1):
        line = line.split('#', 1)[0].strip()
        if not line:
            continue
        fields = line.split(';')
        check(len(fields) == 7, f'map/buildings.txt:{number}: expected seven fields')
        if len(fields) != 7:
            continue
        sid, building, x, height, z, rotation, port_sea = fields
        check(sid in states, f'map/buildings.txt:{number}: unknown state {sid}')
        sites[(sid, building)].append((number, float(x), float(z)))
        if building == 'naval_base_spawn' and port_sea != '0':
            check(port_sea in provinces and provinces[port_sea][4] == 'sea',
                  f'map/buildings.txt:{number}: invalid naval spawn sea province {port_sea}')

    # Native strategicair.cpp rejects a map with missing air/rocket/gun sites.
    # rocket_site and mega_gun_emplacement share rocket_site_spawn in 1.19.3.
    for sid, state in states.items():
        if one(state, 'impassable') == 'yes':
            continue
        for building in ('air_base', 'rocket_site_spawn'):
            check(bool(sites[(sid, building)]), f'Map: state {sid} lacks mandatory {building} position')

    bitmap_path = root / 'map/provinces.bmp'
    if not bitmap_path.exists():
        bitmap_path = game / 'map/provinces.bmp'
    colors = {tuple(map(int, row[1:4])): pid for pid, row in provinces.items()}
    with Image.open(bitmap_path) as source:
        bitmap = source.convert('RGB')
    categories = {key for path in effective_files(root, game, 'common/state_category')
                  for key, val, op in one(read(path), 'state_categories', [])}
    for sid in ('200', '1082'):
        state = states.get(sid, [])
        history = one(state, 'history', [])
        owned = {v for k, v, op in one(state, 'provinces', [])}
        check(one(history, 'owner') == 'MKN' and 'MKN' in values(history, 'add_core_of'), f'Map: {sid} lacks MKN ownership/core')
        check(float(one(state, 'manpower', '-1')) >= 0, f'Map: {sid} has invalid manpower')
        check(one(state, 'state_category') in categories, f'Map: {sid} has invalid state category')
        for key, val, op in walk(history):
            if key == 'victory_points':
                items = [v for k, v, o in val]
                check(len(items) % 2 == 0 and all(p in owned for p in items[::2]), f'Map: {sid} has a victory point outside the state')
            if key == 'buildings':
                for province, buildings, operator in val:
                    if province and province.isdigit():
                        check(province in owned, f'Map: {sid} has buildings outside its provinces')
                        if any(b in ('naval_base', 'coastal_bunker') for b, level, o in buildings):
                            check(province in provinces and provinces[province][5] == 'true', f'Map: coastal building on inland province {province}')
        for building in ('air_base', 'rocket_site_spawn'):
            for number, x, z in sites[(sid, building)]:
                pixel = (int(x), bitmap.height - 1 - int(z))
                check(0 <= pixel[0] < bitmap.width and 0 <= pixel[1] < bitmap.height, f'map/buildings.txt:{number}: position outside map')
                if 0 <= pixel[0] < bitmap.width and 0 <= pixel[1] < bitmap.height:
                    pid = colors.get(bitmap.getpixel(pixel))
                    check(pid in owned, f'map/buildings.txt:{number}: {sid} {building} position lies in province {pid}, outside its state')
    check({v for k, v, op in one(states.get('1082', []), 'provinces', [])} == {'429', '9571'}, 'Map: Huliaipole split changed unexpectedly')

    for filename in ('supply_nodes.txt', 'railways.txt'):
        path = root / 'map' / filename
        if not path.exists():
            path = game / 'map' / filename
        for number, line in enumerate(path.read_text().splitlines(), 1):
            fields = line.split('#', 1)[0].split()
            if not fields:
                continue
            ids = fields[1:] if filename == 'supply_nodes.txt' else fields[2:]
            if filename == 'railways.txt':
                check(len(ids) == int(fields[1]), f'map/{filename}:{number}: wrong route length')
            check(all(pid in provinces and len(province_states[pid]) == 1 for pid in ids), f'map/{filename}:{number}: invalid land province/state')
    if not failures:
        print('PASS: map initialization: unique states/strategic regions, mandatory air/rocket sites, 1082/200 placement, supply and railway province references')
