"""Convert built-in imagegen originals into native HOI4 focus textures.

Only technical alpha cropping, resizing and DDS conversion occur here.
The source images and exact generation prompts remain in the project.
"""
from copy import deepcopy
import argparse
import hashlib
import json
from pathlib import Path
import re

from PIL import Image, ImageDraw, ImageFont
from hoi4_script import read, one, values, dump


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'docs/art/mkn_political_expansions/assets.json'


def replace(node, key, value):
    node[:] = [(k, value if k == key else v, o) for k,v,o in node]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path,default=MANIFEST)
    manifest = parser.parse_args().manifest
    spec = json.loads(manifest.read_text(encoding='utf-8'))
    count = len(spec['assets'])
    template = values(one(read(ROOT/'interface/MKN_focus_shine.gfx'),'spriteTypes'),'spriteType')[0]
    sprites, previews = [], []
    focus_path = ROOT/'common/national_focus/MKN.txt'
    focus_text = focus_path.read_text(encoding='utf-8-sig')
    for asset in spec['assets']:
        source = ROOT/asset['source']
        assert source.is_file() and (ROOT/asset['prompt']).is_file(), asset['focus']
        with Image.open(source) as opened:
            image = opened.convert('RGBA')
        assert image.getchannel('A').getextrema()[0] == 0, 'Missing transparency: '+asset['focus']
        asset['source_sha256'] = hashlib.sha256(source.read_bytes()).hexdigest()
        asset['source_size'] = list(image.size)
        bounds = image.getchannel('A').getbbox()
        assert bounds, asset['focus']
        image = image.crop(bounds)
        image.thumbnail((84,84), Image.Resampling.LANCZOS)
        canvas = Image.new('RGBA',(96,96))
        canvas.alpha_composite(image,((96-image.width)//2,(96-image.height)//2))
        bounds = canvas.getchannel('A').getbbox()
        assert bounds[0]>=6 and bounds[1]>=6 and bounds[2]<=90 and bounds[3]<=90
        target = ROOT/asset['texture']
        target.parent.mkdir(parents=True,exist_ok=True)
        canvas.save(target,format='DDS')
        with Image.open(target) as exported:
            assert exported.mode=='RGBA' and exported.size==(96,96)
        asset['occupied_alpha_bounds'] = list(bounds)
        asset['texture_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
        normal = [('name',asset['sprite'],'='),('texturefile',asset['texture'],'=')]
        sprites.append(('spriteType',normal,'='))
        shine = deepcopy(template)
        replace(shine,'name',asset['sprite']+'_shine')
        replace(shine,'texturefile',asset['texture'])
        for animation in values(shine,'animation'):
            replace(animation,'animationmaskfile',asset['texture'])
        sprites.append(('spriteType',shine,'='))
        # Change only the icon immediately following this focus's id.
        pattern = r'(\bid\s*=\s*'+re.escape(asset['focus'])+r'\s+icon\s*=\s*)\S+'
        focus_text, replacements = re.subn(pattern,lambda m:m[1]+asset['sprite'],focus_text)
        assert replacements == 1, (asset['focus'],replacements)
        previews.append((asset,canvas))
    assert len({a['source_sha256'] for a in spec['assets']})==count
    (ROOT/spec.get('sprite_file','interface/MKN_political_expansions.gfx')).write_text(
        '# Sources and prompts: '+str(manifest.parent)+'\n'+dump([('spriteTypes',sprites,'=')])+'\n',encoding='utf-8')
    focus_path.write_text(focus_text,encoding='utf-8')
    manifest.write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fonts=list(Path('/usr/share/fonts').rglob('DejaVuSans.ttf'))
    font=ImageFont.truetype(str(fonts[0]),13) if fonts else ImageFont.load_default()
    large=ImageFont.truetype(str(fonts[0]),18) if fonts else font
    for scale in (1,2):
        cell_w,cell_h=228,96*scale+66
        sheet=Image.new('RGB',(cell_w*6,cell_h*((count+5)//6)+55),(24,31,42))
        draw=ImageDraw.Draw(sheet)
        draw.text((14,12),f'MKN: {count} focus icons / actual DDS textures / {scale}x',font=large,fill='white')
        for n,(asset,canvas) in enumerate(previews):
            x=(n%6)*cell_w;y=55+(n//6)*cell_h
            icon=canvas.resize((96*scale,96*scale),Image.Resampling.NEAREST)
            sheet.paste(icon,(x+(cell_w-icon.width)//2,y),icon)
            label=asset['focus'].removeprefix('MKN_')
            words=label.split('_');lines=['']
            for word in words:
                if len(lines[-1])+len(word)>27:lines.append('')
                lines[-1]+=(' ' if lines[-1] else '')+word
            draw.text((x+8,y+96*scale+3),f'{n+1:02} '+asset['branch'],font=font,fill=(214,180,103))
            draw.text((x+8,y+96*scale+20),'\n'.join(lines),font=font,fill='white',spacing=2)
        prefix=spec.get('preview_prefix','mkn_political_expansions_preview')
        sheet.save(ROOT/f'docs/{prefix}_{scale}x.png')
    print(f'Built {count} distinct RGBA DDS icons, {count*2} sprites and native/2x previews.')


if __name__ == '__main__':
    main()
