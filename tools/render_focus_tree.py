"""Export the actual LTB/MKN coordinates and prerequisites as readable SVGs."""
from pathlib import Path
from html import escape
import argparse
import re
import textwrap
import json
import base64
import io
from PIL import Image
from hoi4_script import read, one, values, walk, tree_focuses

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
targets={tag:f'common/national_focus/{tag.lower()}_focus.txt' for tag in ('LTB','MKN','UKR')}
if (ROOT/'common/national_focus/SOV_focuses.txt').exists():targets['SOV']='common/national_focus/SOV_focuses.txt'
if (ROOT/'common/national_focus/MKN.txt').exists():targets['MKN']='common/national_focus/MKN.txt'
if (ROOT/'docs/legacy_import.json').exists():
    targets.update({tag:c['destination'] for tag,c in json.loads((ROOT/'docs/legacy_import.json').read_text(encoding='utf-8'))['countries'].items()})
parser.add_argument('--tag', choices=tuple(targets), help='Render only the selected country')
parser.add_argument('--game', type=Path, help='Include actual focus illustrations from this installed copy')
args = parser.parse_args()
labels = {}
for path in ROOT.glob('localisation/**/*l_russian.yml'):
    labels.update(re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$', path.read_text(encoding='utf-8-sig'), re.M))

selected_tags = (args.tag,) if args.tag else tuple(targets)
def visible_focuses(tag):
    return [f for f in tree_focuses(one(read(ROOT / targets[tag]), 'focus_tree'), ROOT / 'common/national_focus')
            if one(f, 'x') is not None and one(f, 'y') is not None
            and one(one(f, 'allow_branch', []), 'always') != 'no']
illustrations = {}
if args.game:
    needed = {one(f, 'icon') for tag in selected_tags
              for f in visible_focuses(tag)}
    roots = [args.game, *sorted(args.game.glob('dlc/*')), ROOT]
    for root in roots:
        for path in root.glob('interface/**/*.gfx'):
            try:
                nodes = read(path)
            except (ValueError, UnicodeError):
                continue
            for key, node, op in walk(nodes):
                if key and key.lower() == 'spritetype':
                    name = one(node, 'name')
                    texture = one(node, 'texturefile')
                    if name in needed and texture:
                        illustrations[name] = (texture, int(one(node, 'noOfFrames', '1')))
    for name, (texture, frames) in list(illustrations.items()):
        path = next((root / texture for root in reversed(roots) if (root / texture).is_file()), None)
        if not path:
            del illustrations[name]
            continue
        # `needed` already contains only actual focus references. Some country
        # trees deliberately reuse an idea sprite, e.g. MKN's Free Workshops.
        with Image.open(path) as source:
            img = source.convert('RGBA')
            if frames > 1:
                img = img.crop((0, 0, img.width // frames, img.height))
            img.thumbnail((64, 64))
            output = io.BytesIO()
            img.save(output, format='PNG')
            illustrations[name] = base64.b64encode(output.getvalue()).decode()

for tag in selected_tags:
    tree = one(read(ROOT/targets[tag]), 'focus_tree')
    focuses = visible_focuses(tag)
    positions = {one(f, 'id'): (int(one(f, 'x'))*90+140, int(one(f, 'y'))*95+130) for f in focuses}
    width = max(x for x, y in positions.values())+150
    height = max(y for x, y in positions.values())+120
    result = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
              '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#e4edf7}.label{font-size:12px}.small{font-size:10px;fill:#acbbce}</style>',
              f'<rect width="{width}" height="{height}" fill="#111925"/>',
              f'<text x="32" y="38" font-size="24">{tag}: {len(focuses)} фокусов</text>',
              '<text x="32" y="64" font-size="13">Координаты и связи из кода • пунктир: альтернативные предпосылки • красные линии: взаимоисключение</text>']
    if tag == 'SOV':
        for column, title in [(8,'Союзный договор'),(22,'Хозяйственный план'),(32,'Наука'),(42,'Регулярная армия'),(54,'Авиация'),(64,'Флот'),(77,'Запад и вольная степь')]:
            result.append(f'<text x="{column*90+140}" y="90" font-size="14" text-anchor="middle">{title}</text>')
    elif tag == 'TUR':
        for column, title in [(8, 'Политика и имперский совет'), (6, 'Балканские кампании — ниже политики'), (22, 'Промышленность'), (34, 'Наука'), (42, 'Армия'), (50, 'Авиация')]:
            result.append(f'<text x="{column*90+140}" y="{90 if column != 6 else height-20}" font-size="14" text-anchor="middle">{title}</text>')
    elif tag == 'LTB':
        for column, title in [(7,'Политика'),(18,'Дипломатия'),(24,'Гражданская промышленность'),(28,'Сельское хозяйство и сырьё'),(32,'Военная промышленность'),(36,'Наука'),(42,'Армия'),(50,'Авиация'),(56,'Флот')]:
            result.append(f'<text x="{column*90+140}" y="90" font-size="14" text-anchor="middle">{title}</text>')
    elif tag == 'MKN':
        for column, title in [(4,'Днепрострой: 24 фокуса'),(16,'Вольные кооперативы: 24 фокуса'),(27,'Наука'),(34,'Подготовка и архив'),(46,'Механизация: 10 + 10 доп.'),(54,'Вольные колонны: 10 + 10 доп.'),(62,'Защита неба: 10 + 10 доп.'),(70,'Авиация поддержки: 10 + 10 доп.'),(78,'Эскорты: 10 + 10 доп.'),(86,'Рейдеры: 10 + 10 доп.'),(108,'Кризис 1936 года: четыре пути'),(131,'Украинский рубеж')]:
            result.append(f'<text x="{column*90+140}" y="90" font-size="14" text-anchor="middle">{title}</text>')
    elif tag == 'UKR':
        for column, title in [(6,'Политические мандаты'),(22,'Хозяйство'),(34,'Армия'),(44,'Авиация'),(54,'Флот'),(64,'Дипломатия')]:
            result.append(f'<text x="{column*90+140}" y="90" font-size="14" text-anchor="middle">{title}</text>')
    elif tag == 'AUS':
        for column,title in [(4,'Политика и Дунайская монархия'),(10,'Внешние связи'),(16,'Армия'),(24,'Промышленность')]:
            result.append(f'<text x="{column*90+140}" y="90" font-size="14" text-anchor="middle">{title}</text>')
    # Prerequisite edges underneath the cards.
    for f in focuses:
        fid = one(f, 'id'); x, y = positions[fid]
        for group in values(f, 'prerequisite'):
            parents = values(group, 'focus')
            dashed = 'stroke-dasharray="6 4"' if len(parents)>1 else ''
            for parent in parents:
                px, py = positions[parent]
                mid = (py+y)/2
                result.append(f'<path d="M {px} {py+30} V {mid} H {x} V {y-30}" fill="none" stroke="#68809a" stroke-width="1.4" {dashed}/>')
    drawn = set()
    for f in focuses:
        fid=one(f,'id');x,y=positions[fid]
        for group in values(f,'mutually_exclusive'):
            for other in values(group,'focus'):
                pair=tuple(sorted((fid,other)))
                if pair in drawn:continue
                drawn.add(pair);ox,oy=positions[other]
                result.append(f'<path d="M {x} {y-35} Q {(x+ox)/2} {min(y,oy)-65} {ox} {oy-35}" stroke="#be6066" stroke-width="1" fill="none" opacity="0.45"/>')
    for f in focuses:
        fid=one(f,'id');x,y=positions[fid]
        keys={k for k,v,o in walk(one(f,'completion_reward'))}
        color='#327a65' if 'add_building_construction' in keys else '#6655a2' if 'add_research_slot' in keys or 'add_tech_bonus' in keys else '#416487'
        title=labels.get(fid,fid)
        tooltip=title+'\n'+labels.get(fid+'_desc','')+'\n'+fid
        gates = [value for key, value, op in walk(one(f, 'available', [])) if key == 'has_completed_focus']
        if gates:
            tooltip += '\nДополнительные условия: ' + ', '.join(labels.get(gate, gate) for gate in gates)
        result.append(f'<g><title>{escape(tooltip)}</title><rect x="{x-80}" y="{y-31}" width="160" height="62" rx="8" fill="#1c2a3a" stroke="{color}" stroke-width="2"/>')
        illustration = illustrations.get(one(f, 'icon'))
        if illustration:
            result.append(f'<image x="{x-77}" y="{y-28}" width="44" height="44" href="data:image/png;base64,{illustration}"/>')
        label_x = x + 20 if illustration else x
        for i,line in enumerate(textwrap.wrap(title,width=17 if illustration else 22)[:2]):
            result.append(f'<text class="label" x="{label_x}" y="{y-9+i*16}" text-anchor="middle">{escape(line)}</text>')
        cost = int(one(f, 'cost'))*7
        rewards = (' • строительство' if 'add_building_construction' in keys else ' • наука' if 'add_research_slot' in keys else ' • подготовка' if 'add_mastery_bonus' in keys else ' • исследования' if 'add_tech_bonus' in keys else ' • развитие духа' if 'add_to_variable' in keys else ' • реформа духа' if 'swap_ideas' in keys else ' • решение съезда' if 'country_event' in keys else '')
        result.append(f'<text class="small" x="{x}" y="{y+22}" text-anchor="middle">{cost} дней{escape(rewards)}</text></g>')
    result.append('</svg>')
    dest=ROOT/f'docs/{tag.lower()}_focus_tree.svg';dest.parent.mkdir(exist_ok=True)
    dest.write_text('\n'.join(result)+'\n',encoding='utf-8',newline='\n')
    print(dest.relative_to(ROOT))
