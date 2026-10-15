"""Export saved imagegen MKN artwork; perform technical asset conversion only.

Creative masters and exact prompts live in docs/art/MKN_hoi4_art.json.
This exporter never procedurally redraws focus subjects or country flags.
"""
from copy import deepcopy
import argparse
import hashlib
import json
from pathlib import Path
import re

from PIL import Image, ImageDraw, ImageFont, ImageOps
from hoi4_script import read, one, values, dump

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'docs/art/MKN_hoi4_art.json'


def put(node, key, value):
    node[:] = [entry for entry in node if entry[0] != key]
    node.append((key, value, '='))


def save_script(path, node):
    (ROOT / path).write_text(dump(node) + '\n', encoding='utf-8')


def load_master(asset, transparent):
    source = ROOT / asset['source']
    assert source.is_file(), f'Missing generated master: {source}'
    assert (ROOT / asset['prompt']).is_file(), f'Missing exact prompt: {asset["prompt"]}'
    with Image.open(source) as opened:
        image = opened.convert('RGBA' if transparent else 'RGB')
    asset['source_sha256'] = hashlib.sha256(source.read_bytes()).hexdigest()
    asset['source_size'] = list(image.size)
    if transparent:
        assert image.getchannel('A').getextrema()[0] == 0, f'No real transparency: {source}'
    return image


def focus_export(master):
    # Discard imperceptible alpha noise, then fit the actual painted silhouette.
    image = master.copy()
    image.putalpha(image.getchannel('A').point(lambda a: 0 if a < 16 else a))
    bounds = image.getchannel('A').getbbox()
    assert bounds is not None
    image = image.crop(bounds)
    image.thumbnail((84, 84), Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', (96, 96))
    canvas.alpha_composite(image, ((96 - image.width) // 2, (96 - image.height) // 2))
    bounds = canvas.getchannel('A').getbbox()
    assert bounds and min(bounds[:2]) >= 6 and max(bounds[2:]) <= 90, bounds
    return canvas, list(bounds)


def render_preview(rows, destination, columns=5, flag=False):
    cell_w, cell_h = (260, 200) if flag else (220, 295)
    height = ((len(rows) + columns - 1) // columns) * cell_h + 36
    preview = Image.new('RGB', (columns * cell_w, height), (26, 29, 35))
    pen = ImageDraw.Draw(preview)
    font_path = Path('/usr/share/fonts/TTF/DejaVuSans.ttf')
    if not font_path.exists():
        candidates = list(Path('/usr/share/fonts').rglob('DejaVuSans.ttf'))
        candidates += list(Path('/usr/share/fonts').rglob('LiberationSans-Regular.ttf'))
        font_path = next(iter(candidates), None)
    font = ImageFont.truetype(str(font_path), 12) if font_path else ImageFont.load_default()
    pen.text((12, 10), 'Махновщина / рисованные иконки HOI4' if not flag else 'Махновщина / знамя Махно и флаги преемников', fill='white', font=font)
    for i, (label, image) in enumerate(rows):
        x = (i % columns) * cell_w
        y = (i // columns) * cell_h + 36
        if flag:
            enlarged = image.resize((246, 156), Image.Resampling.NEAREST)
            preview.paste(enlarged, (x + 7, y))
        else:
            enlarged = image.resize((144, 144), Image.Resampling.NEAREST)
            preview.paste(enlarged, (x + 38, y), enlarged)
            preview.paste(image, (x + 62, y + 155), image)
        lines, current = [], ''
        for word in label.split():
            candidate = (current + ' ' + word).strip()
            if current and pen.textlength(candidate, font=font) > cell_w - 16:
                lines.append(current)
                current = word
            else:
                current = candidate
        if current:
            lines.append(current)
        for line_index, line in enumerate(lines[:2]):
            pen.text((x + 8, y + (162 if flag else 260) + line_index * 14), line, fill=(228, 223, 211), font=font)
    preview.save(ROOT / destination)


def export_icons(spec, game):
    focus_sprites, idea_sprites, shines, preview = [], [], [], []
    labels = {}
    for path in (ROOT / 'localisation/russian').glob('MKN*.yml'):
        labels.update(re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$', path.read_text(encoding='utf-8-sig'), re.M))
    template = values(one(read(ROOT / 'interface/MKN_focus_shine.gfx'), 'spriteTypes'), 'spriteType')[0]
    for asset in spec['assets']:
        canvas, bounds = focus_export(load_master(asset, True))
        destination = ROOT / asset['texture']
        destination.parent.mkdir(parents=True, exist_ok=True)
        canvas.save(destination, format='DDS')
        asset['occupied_alpha_bounds'] = bounds
        asset['size'] = [96, 96]
        sprite = [('name', asset['sprite'], '='), ('texturefile', asset['texture'], '=')]
        (idea_sprites if asset['key'] == 'workshops' else focus_sprites).append(('spriteType', sprite, '='))
        if asset['key'] == 'revkom':
            idea_sprites.append(('spriteType', [('name', 'GFX_idea_MKN_revkom', '='), ('texturefile', asset['texture'], '=')], '='))
        shine = deepcopy(template)
        put(shine, 'name', asset['sprite'] + '_shine')
        put(shine, 'texturefile', asset['texture'])
        for animation in values(shine, 'animation'):
            put(animation, 'animationmaskfile', asset['texture'])
        shines.append(('spriteType', shine, '='))
        preview.append((labels.get(asset['focus'], asset['key']), canvas))
    save_script('interface/MKN_overhaul_icons.gfx', [('spriteTypes', focus_sprites, '=')])
    save_script('interface/MKN_overhaul_shine.gfx', [('spriteTypes', shines, '=')])
    # Preserve reviewed fixes in the mod's native registry across asset rebuilds.
    # This interface loader treats a BOM as part of the first spriteTypes token.
    registry = ROOT / 'interface/ideas.gfx'
    marker = '\n# MKN painted ideas; sources: docs/art/MKN_hoi4_art.json.'
    native = (registry if registry.is_file() else game / 'interface/ideas.gfx').read_text(encoding='utf-8-sig').split(marker, 1)[0]
    native = '\n'.join(re.sub(r'^[ \t]+', lambda m: m.group().expandtabs(4), line).rstrip() for line in native.splitlines())
    registry.write_text(native + marker + '\n' + dump([('spriteTypes', idea_sprites, '=')]) + '\n', encoding='utf-8')
    render_preview(preview, 'docs/mkn_overhaul_icons_preview.png')


def export_flags(spec):
    masters = {asset['key']: load_master(asset, False) for asset in spec['flags']}
    preview = []
    labels = {'historical': 'Знамя при Махно', 'fascism': 'Анархо-милитаризм',
              'democratic': 'Набат / вольные советы', 'neutrality': 'Крестьянский совет',
              'communism': 'Государственный синдикализм'}
    for key, master in masters.items():
        # Flag masters are full-frame rectangular designs, never focus emblems.
        flag = ImageOps.fit(master, (820, 520), Image.Resampling.LANCZOS)
        names = ['MKN_batko', *['MKN_batko_' + p for p in ('fascism', 'democratic', 'neutrality', 'communism')], 'MKN'] if key == 'historical' else ['MKN_' + key, 'MKN_cw_' + key]
        for folder, size in (('', (82, 52)), ('medium', (41, 26)), ('small', (10, 7))):
            directory = ROOT / 'gfx/flags' / folder
            directory.mkdir(exist_ok=True)
            texture = flag.resize(size, Image.Resampling.LANCZOS).convert('RGBA')
            for name in names:
                texture.save(directory / (name + '.tga'), format='TGA')
        preview.append((labels[key], flag.resize((82, 52), Image.Resampling.LANCZOS)))
    render_preview(preview, 'docs/mkn_flags_preview.png', columns=3, flag=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', type=Path, required=True)
    parser.add_argument('--only', choices=('icons', 'flags'))
    args = parser.parse_args()
    spec = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if args.only != 'flags':
        export_icons(spec, args.game)
    if args.only != 'icons':
        export_flags(spec)
    MANIFEST.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('PASS: imagegen originals exported with native dimensions and inspected alpha clearance')


if __name__ == '__main__':
    main()
