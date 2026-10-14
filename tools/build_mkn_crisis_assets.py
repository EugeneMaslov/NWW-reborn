"""Export the saved MKN crisis artwork, connect sprites and render a contact sheet.

Only technical alpha-bounds cropping, resizing and DDS conversion happen here.
New artwork and background extraction are supplied by built-in imagegen.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps
from hoi4_script import read, one, values, dump


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'docs/art/mkn_crisis/assets.json'
spec = json.loads(MANIFEST.read_text(encoding='utf-8'))
custom_path = ROOT / 'interface/MKN_custom.gfx'
custom = read(custom_path)
sprites = {one(s, 'name'): s for s in values(one(custom, 'spriteTypes'), 'spriteType')}
shine_path = ROOT / 'interface/MKN_focus_shine.gfx'
shine = read(shine_path)
shine_group = one(shine, 'spriteTypes')
shine_sprites = {one(s, 'name'): s for s in values(shine_group, 'spriteType')}
template = deepcopy(next(iter(shine_sprites.values())))
focuses = {one(f, 'id'): f for f in values(one(read(ROOT / 'common/national_focus/MKN.txt'), 'focus_tree'), 'focus')}


def replace(node, key, value):
    node[:] = [(k, value if k == key else v, o) for k, v, o in node]


def save_texture(image, relative):
    target = ROOT / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target, format='DDS')
    with Image.open(target) as exported:
        assert exported.size == image.size
        assert exported.mode == 'RGBA'


native = []
events = []
for asset in spec['assets']:
    source = ROOT / asset['source']
    assert source.is_file() and (ROOT / asset['prompt']).is_file()
    with Image.open(source) as opened:
        image = opened.convert('RGBA')
    asset['source_sha256'] = hashlib.sha256(source.read_bytes()).hexdigest()
    asset['source_size'] = list(image.size)
    if 'focus' in asset:
        assert one(focuses[asset['focus']], 'icon') == asset['sprite']
        assert image.getchannel('A').getextrema()[0] == 0
        bounds = image.getchannel('A').getbbox()
        assert bounds is not None
        image = image.crop(bounds)
        image.thumbnail(tuple(asset['occupied']), Image.Resampling.LANCZOS)
        canvas = Image.new('RGBA', tuple(asset['size']))
        canvas.alpha_composite(image, ((canvas.width - image.width) // 2, (canvas.height - image.height) // 2))
        bounds = canvas.getchannel('A').getbbox()
        assert bounds and bounds[0] >= 6 and bounds[1] >= 6 and bounds[2] <= 90 and bounds[3] <= 90, (asset['key'], bounds)
        save_texture(canvas, asset['texture'])
        asset['occupied_alpha_bounds'] = list(bounds)
        replace(sprites[asset['sprite']], 'texturefile', asset['texture'])
        highlight_name = asset['sprite'] + '_shine'
        if highlight_name not in shine_sprites:
            highlight = deepcopy(template)
            replace(highlight, 'name', highlight_name)
            shine_group.append(('spriteType', highlight, '='))
            shine_sprites[highlight_name] = highlight
        highlight = shine_sprites[highlight_name]
        replace(highlight, 'texturefile', asset['texture'])
        for animation in values(highlight, 'animation'):
            replace(animation, 'animationmaskfile', asset['texture'])
        native.append((asset['key'], canvas))
        print(asset['focus'], '96x96', 'alpha:', bounds)
    else:
        for event in asset['events']:
            canvas = ImageOps.fit(image, tuple(event['size']), Image.Resampling.LANCZOS, centering=tuple(event['centering']))
            save_texture(canvas, event['texture'])
            replace(sprites[event['sprite']], 'texturefile', event['texture'])
            events.append((event['sprite'], canvas))
            print(event['sprite'], canvas.size)

for reference in spec['references']:
    source = ROOT / reference['original']
    archived = ROOT / reference['archive']
    assert source.read_bytes() == archived.read_bytes(), 'User reference was changed'
    reference['sha256'] = hashlib.sha256(source.read_bytes()).hexdigest()

custom_path.write_text('# Project-bound MKN artwork; sources and prompts: docs/art/mkn_crisis/.\n' + dump(custom) + '\n', encoding='utf-8')
shine_path.write_text(dump(shine) + '\n', encoding='utf-8')
MANIFEST.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Preview the actual exported textures at native size and at 2x for inspection.
preview = Image.new('RGB', (1100, 740), (22, 28, 38))
draw = ImageDraw.Draw(preview)
fonts = list(Path('/usr/share/fonts').rglob('DejaVuSans.ttf')) or list(Path('/usr/share/fonts').rglob('LiberationSans-Regular.ttf'))
font = ImageFont.truetype(str(fonts[0]), 15) if fonts else ImageFont.load_default()
draw.text((20, 15), 'MKN: five focus icons / native 96x96 and 2x preview', fill='white', font=font)
for i, (key, canvas) in enumerate(native):
    x = 20 + i * 216
    draw.rounded_rectangle((x, 50, x + 198, 386), radius=8, fill=(33, 42, 57), outline=(87, 100, 119))
    preview.paste(canvas.resize((192, 192), Image.Resampling.NEAREST), (x + 3, 59), canvas.resize((192, 192), Image.Resampling.NEAREST))
    draw.text((x + 7, 258), key.replace('_', ' '), fill='white', font=font)
    preview.paste(canvas, (x + 50, 283), canvas)
draw.text((20, 408), 'Actual country-event crop: 210x176', fill='white', font=font)
draw.text((280, 408), 'Actual news crop: 397x153', fill='white', font=font)
preview.paste(events[0][1], (20, 438), events[0][1])
preview.paste(events[1][1], (280, 438), events[1][1])
draw.text((20, 645), 'Sources and exact imagegen prompts: docs/art/mkn_crisis/', fill=(185, 200, 218), font=font)
preview.save(ROOT / 'docs/mkn_crisis_art_preview.png')
