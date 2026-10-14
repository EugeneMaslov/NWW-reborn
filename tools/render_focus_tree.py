"""Export the actual LTB/MKN coordinates and prerequisites as readable SVGs."""
from pathlib import Path
from html import escape
import argparse
import re
import textwrap
from hoi4_script import read, one, values, walk

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--tag', choices=('LTB', 'MKN', 'UKR'), help='Render only the selected country')
args = parser.parse_args()
labels = {}
for path in ROOT.glob('localisation/*l_russian.yml'):
    labels.update(re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$', path.read_text(encoding='utf-8-sig'), re.M))

for tag in ((args.tag,) if args.tag else ('LTB', 'MKN', 'UKR')):
    tree = one(read(ROOT/f'common/national_focus/{tag.lower()}_focus.txt'), 'focus_tree')
    focuses = values(tree, 'focus')
    positions = {one(f, 'id'): (int(one(f, 'x'))*90+140, int(one(f, 'y'))*95+130) for f in focuses}
    width = max(x for x, y in positions.values())+150
    height = max(y for x, y in positions.values())+120
    result = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
              '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#e4edf7}.label{font-size:12px}.small{font-size:10px;fill:#acbbce}</style>',
              f'<rect width="{width}" height="{height}" fill="#111925"/>',
              f'<text x="32" y="38" font-size="24">{tag}: {len(focuses)} фокусов</text>',
              '<text x="32" y="64" font-size="13">Координаты и связи из кода • пунктир: альтернативные предпосылки • красные линии: взаимоисключение</text>']
    if tag == 'LTB':
        for column, title in [(7,'Политика'),(18,'Дипломатия'),(24,'Гражданская промышленность'),(28,'Сельское хозяйство и сырьё'),(32,'Военная промышленность'),(36,'Наука'),(42,'Армия'),(50,'Авиация'),(56,'Флот')]:
            result.append(f'<text x="{column*90+140}" y="90" font-size="14" text-anchor="middle">{title}</text>')
    elif tag == 'MKN':
        for column, title in [(4,'Днепрострой: 24 фокуса'),(16,'Вольные кооперативы: 24 фокуса'),(27,'Наука'),(34,'Политика'),(46,'Механизация: 20'),(54,'Вольные колонны: 20'),(62,'Защита неба: 20'),(70,'Авиация поддержки: 20'),(78,'Эскорты: 20'),(86,'Рейдеры: 20')]:
            result.append(f'<text x="{column*90+140}" y="90" font-size="14" text-anchor="middle">{title}</text>')
    else:
        for column, title in [(6,'Политические мандаты'),(22,'Хозяйство'),(34,'Армия'),(44,'Авиация'),(54,'Флот'),(62,'Дипломатия')]:
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
        for i,line in enumerate(textwrap.wrap(title,width=22)[:2]):
            result.append(f'<text class="label" x="{x}" y="{y-9+i*16}" text-anchor="middle">{escape(line)}</text>')
        cost = int(one(f, 'cost'))*7
        rewards = (' • развитие духа' if 'add_to_variable' in keys else ' • реформа духа' if 'swap_ideas' in keys else ' • исследовательская ячейка' if 'add_research_slot' in keys else ' • строительство' if 'add_building_construction' in keys else ' • решение съезда' if 'country_event' in keys else '')
        result.append(f'<text class="small" x="{x}" y="{y+22}" text-anchor="middle">{cost} дней{escape(rewards)}</text></g>')
    result.append('</svg>')
    dest=ROOT/f'docs/{tag.lower()}_focus_tree.svg';dest.parent.mkdir(exist_ok=True)
    dest.write_text('\n'.join(result)+'\n',encoding='utf-8')
    print(dest.relative_to(ROOT))
