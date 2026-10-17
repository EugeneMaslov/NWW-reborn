"""Build the offline NWW atlas from effective HOI4 provinces/state history.

No game mechanics are changed. Requires Pillow (already used by mod tools).
"""
import argparse
from collections import Counter, defaultdict
import csv
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re
import zipfile
from PIL import Image
from hoi4_script import read, one, values, walk

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'sites/nww-atlas'
FULL = {'LTB', 'MKN', 'UKR', 'SOV', 'AUS', 'TUR', 'GER', 'FRA', 'ENG'}
LEGACY = {'HUN', 'AFG'}
NAMES = {'LTB': 'Литовско-Белорусский Союз', 'MKN': 'Вольная территория Махно',
         'UKR': 'Советская Украина', 'SOV': 'Советская Россия', 'AUS': 'Австрийская империя',
         'TUR': 'Османская империя', 'GER': 'Германская империя', 'HUN': 'Венгрия',
         'AFG': 'Афганистан', 'BYE': 'Беларусь', 'LIT': 'Литва', 'LAT': 'Латвия',
         'EST': 'Эстония', 'CRO': 'Хорватия', 'FRA': 'Франция', 'ENG': 'Великобритания'}
DETAILS = {
    'LTB': 'Виленский компромисс, кризис и распад Союза, политические мандаты, предприятия и реорганизация штаба.',
    'MKN': 'Преемники Махно, вольные советы и штаб, гражданская война, коммуны и пограничная эскалация.',
    'UKR': 'Политические мандаты, промышленная реконструкция и дипломатия через согласие или отказ соседей.',
    'SOV': 'Последовательные реформы государства, экономики и армии; собственная система западного давления.',
    'AUS': 'Пять политических маршрутов, кризис Богемии, коронные земли и восстановление Австро-Венгрии.',
    'TUR': 'Платные последовательные переговоры с советами, политические мандаты и балканские кампании династии.',
    'GER': 'Кризис наследования, четыре политических пути, устройство империи и собственная промышленная политика.',
    'HUN': 'Адаптированное дерево старого NWW. Перенос и обновление синтаксиса не считаются полной новой переработкой.',
    'AFG': 'Адаптированное дерево старого NWW с обновлёнными эффектами и стартовой экономикой.',
    'FRA': 'Четыре основные политические ветки, мандат кабинета и уличная напряжённость, региональный заморский договор, модернизация промышленности и вооружённых сил.',
    'ENG': 'Содружество и федерация, авторитарные и социалистические маршруты, изоляционизм и ирландское урегулирование. Оплачиваемые имперские переговоры, морские артерии и отдельные программы армии, RAF и Royal Navy.',
}


def effective(game, folder):
    paths = {p.name: p for p in (game / folder).glob('*.txt')}
    paths.update({p.name: p for p in (ROOT / folder).glob('*.txt')})
    return sorted(paths.values())


def localization(game):
    result = {}
    for base in (game, ROOT):
        paths = sorted((base / 'localisation').rglob('*l_russian.yml'))
        paths.sort(key=lambda p: ('replace' in p.parts, str(p)))
        for p in paths:
            for line in p.read_text(encoding='utf-8-sig', errors='replace').splitlines():
                m = re.match(r'\s*([A-Za-z0-9_]+):\d*\s*"(.*)"', line)
                if m:
                    result[m[1]] = m[2]
    return result


def evaluate_limit(node):
    """All installed DLC enabled; reject unsupported ownership conditions."""
    tests = []
    for key, val, _ in node:
        if key == 'has_dlc':
            tests.append(True)
        elif key == 'always':
            tests.append(val == 'yes')
        elif key in ('OR', 'AND', 'NOT'):
            children = [evaluate_limit([entry]) for entry in val]
            tests.append(any(children) if key == 'OR' else not all(children) if key == 'NOT' else all(children))
        else:
            raise ValueError(f'Unsupported ownership condition: {key} = {val}')
    return all(tests)


def initial_owner(history):
    owner = None
    for key, val, _ in history:
        if key in ('owner', 'transfer_state_to'):
            owner = val
        elif key.lower() == 'if' and any(k in ('owner', 'transfer_state_to') for k, v, o in walk(val)):
            if evaluate_limit(one(val, 'limit', [])):
                owner = initial_owner(val) or owner
        elif re.fullmatch(r'\d+\.\d+\.\d+', key or ''):
            if tuple(map(int, key.split('.'))) <= (1936, 1, 1):
                owner = initial_owner(val) or owner
    return owner


def focus_inventory():
    trees = {}
    shared = {}
    for p in sorted((ROOT / 'common/national_focus').glob('*.txt')):
        for kind, node, _ in read(p):
            if kind == 'shared_focus' and isinstance(node, list):
                shared[one(node, 'id')] = (node, p)
            elif kind == 'focus_tree':
                tags = {v for k, v, o in walk(one(node, 'country', [])) if k == 'tag'}
                if len(tags) == 1 and values(node, 'focus'):
                    tag = tags.pop()
                    if tag in trees:
                        raise ValueError(f'Multiple active trees for {tag}')
                    trees[tag] = (node, p)
    result = {}
    for tag, (tree, p) in trees.items():
        focuses = [(f, p) for f in values(tree, 'focus')]
        pending = list(values(tree, 'shared_focus'))
        seen = set()
        while pending:
            fid = pending.pop()
            if fid in seen or fid not in shared:
                continue
            seen.add(fid)
            f, source = shared[fid]
            focuses.append((f, source))
            # Shared focus chains are explicitly linked, never recursively collected IDs.
            pending.extend(child for child, (node, _) in shared.items()
                           if any(fid in values(req, 'focus') for req in values(node, 'prerequisite')))
        visible = [(f, source) for f, source in focuses if one(one(f, 'allow_branch', []), 'always') != 'no']
        result[tag] = {'focuses': len({one(f, 'id') for f, _ in visible}),
                       'sources': sorted({str(source.relative_to(ROOT)).replace('\\', '/') for _, source in visible})}
    return result


def make_paths(data, width, height, tags):
    edges = defaultdict(lambda: defaultdict(list))
    stride = width + 1

    def edge(tag, a, b):
        if tag:
            edges[tag][a].append(b)

    for y in range(height + 1):
        above = data[(y - 1) * width:y * width] if y else bytes(width)
        below = data[y * width:(y + 1) * width] if y < height else bytes(width)
        for x, (a, b) in enumerate(zip(above, below)):
            if a != b:
                v = y * stride + x
                edge(b, v, v + 1)
                edge(a, v + 1, v)
    for y in range(height):
        row = data[y * width:(y + 1) * width]
        for x in range(width + 1):
            a = row[x - 1] if x else 0
            b = row[x] if x < width else 0
            if a != b:
                v = y * stride + x
                edge(a, v, v + stride)
                edge(b, v + stride, v)
    paths, boxes = {}, {}
    for idx, graph in edges.items():
        rings = []
        while graph:
            start = next(iter(graph))
            v = start
            ring = [v]
            while True:
                nxt = graph[v].pop()
                if not graph[v]:
                    del graph[v]
                v = nxt
                if v == start:
                    break
                ring.append(v)
            points = [(v % stride, v // stride) for v in ring]
            simple = []
            for i, p in enumerate(points):
                a, b = points[i - 1], points[(i + 1) % len(points)]
                if (p[0] - a[0]) * (b[1] - p[1]) != (p[1] - a[1]) * (b[0] - p[0]):
                    simple.append(p)
            if len(simple) >= 3:
                rings.append(simple)
        # Largest ring gives a useful mainland view for colonial countries.
        largest = max(rings, key=lambda pts: abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(pts, pts[1:]+pts[:1]))))
        boxes[tags[idx]] = [min(p[0] for p in largest), min(p[1] for p in largest),
                           max(p[0] for p in largest), max(p[1] for p in largest)]
        paths[tags[idx]] = ''.join('M' + 'L'.join(f'{x},{y}' for x,y in ring) + 'Z' for ring in rings)
    return paths, boxes


def build(game, snapshot_date=None):
    snapshot_date = snapshot_date or datetime.now(timezone(timedelta(hours=3))).date().isoformat()
    loc = localization(game)
    focus = focus_inventory()
    owners, states, provenance = {}, Counter(), []
    state_owner = {}
    for p in effective(game, 'history/states'):
        state = one(read(p), 'state')
        owner = initial_owner(one(state, 'history', []))
        if not owner:
            continue
        sid = int(one(state, 'id'))
        assert sid not in state_owner, f'Duplicate state {sid}'
        state_owner[sid] = owner
        states[owner] += 1
        provenance.append({'state': sid, 'owner': owner, 'source': str(p.relative_to(ROOT) if p.is_relative_to(ROOT) else p.relative_to(game)).replace('\\', '/')})
        for _, pid, _ in one(state, 'provinces', []):
            assert int(pid) not in owners, f'Duplicate province {pid}'
            owners[int(pid)] = owner
    tags = [''] + sorted(states)
    assert len(tags) < 256
    indices = {tag: i for i, tag in enumerate(tags)}
    definition = ROOT / 'map/definition.csv'
    if not definition.exists():
        definition = game / 'map/definition.csv'
    colors = {}
    with definition.open(encoding='utf-8-sig') as stream:
        for row in csv.reader(stream, delimiter=';'):
            if row and row[0].isdigit():
                colors[tuple(map(int, row[1:4]))] = indices.get(owners.get(int(row[0])), 0) if row[4] == 'land' else 0
    bitmap = ROOT / 'map/provinces.bmp'
    if not bitmap.exists():
        bitmap = game / 'map/provinces.bmp'
    image = Image.open(bitmap).convert('RGB')
    width, height = image.size
    print(f'Reading {width}x{height} province map...', flush=True)
    pixels = bytes(colors.get(rgb, 0) for rgb in image.get_flattened_data())
    paths, boxes = make_paths(pixels, width, height, tags)
    countries = []
    for tag in sorted(set(tags[1:]) | set(focus)):
        info = focus.get(tag, {})
        status = 'full' if tag in FULL else 'legacy' if tag in LEGACY else 'partial' if info else 'none'
        name = NAMES.get(tag, loc.get(tag, loc.get(tag + '_DEF', loc.get(tag + '_neutrality', tag))))
        name = re.sub(r'§.|\[[^]]+\]', '', name)
        countries.append(dict(tag=tag, name=name, status=status, states=states[tag],
                              focuses=info.get('focuses', 0), sources=info.get('sources', []),
                              box=boxes.get(tag), description=DETAILS.get(tag,
                              'Небольшое новое дерево. Это не Legacy и не полная переработка с собственными механиками.' if info else
                              'В текущем моде нет собственного дерева NWW. Стандартные деревья игры и DLC не считаются уникальным контентом мода.')))
    svg = ''.join(f'<path id="country-{tag}" data-tag="{tag}" d="{path}"/>' for tag, path in sorted(paths.items()))
    dataset = dict(width=width, height=height, countries=countries, date='1936-01-01',
                   snapshotDate=snapshot_date, dlc='all', states=provenance)
    template = (SITE / 'src/index.html').read_text(encoding='utf-8')
    html = template.replace('/*__STYLE__*/', (SITE / 'src/style.css').read_text(encoding='utf-8'))
    html = html.replace('<!--__MAP__-->', svg).replace('/*__DATA__*/', 'const DATA=' + json.dumps(dataset, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';')
    html = html.replace('/*__APP__*/', (SITE / 'src/app.js').read_text(encoding='utf-8'))
    html = html.replace('__SNAPSHOT_DATE__', '.'.join(reversed(snapshot_date.split('-'))))
    html = html.replace('__FULL_TAGS__', ', '.join(sorted(FULL)))
    out = SITE / 'dist'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(html, encoding='utf-8')
    (SITE / 'classification.json').write_text(json.dumps(countries, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    assert all(state_owner[t['state']] == 'GER' for t in json.loads((ROOT / 'docs/GER_overseas_setup.json').read_text())['territories'])
    assert state_owner[656] == 'TUR'
    with zipfile.ZipFile(SITE / 'NWW-Reborn-Atlas.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.write(out / 'index.html', 'NWW-Reborn-Atlas.html')
        archive.writestr('README.txt',
                         'NWW Reborn — интерактивный атлас\n\n'
                         'Откройте NWW-Reborn-Atlas.html в браузере. Интернет и сервер не нужны.\n'
                         'Поиск — название или тег, колесо — масштаб, перетаскивание — перемещение.\n'
                         'Описание источников и классификации — кнопка «О карте».\n'
                         f'Срез исходников: {snapshot_date}. Карта кампании: 1 января 1936 года.\n')
    print(json.dumps({'countries_on_map': len(paths), 'statuses': dict(Counter(c['status'] for c in countries)),
                      'file': str(out / 'index.html'), 'bytes': len(html.encode('utf-8'))}, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', type=Path, default=Path('D:/Steam/steamapps/common/Hearts of Iron IV'))
    parser.add_argument('--snapshot-date', type=lambda value: datetime.strptime(value, '%Y-%m-%d').date().isoformat())
    args = parser.parse_args()
    build(args.game, args.snapshot_date)
