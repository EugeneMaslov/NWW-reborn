"""Technically crop/resize imagegen originals and export native ENG DDS icons.

Creative artwork is generated with the built-in image_gen tool. This script
preserves those originals and performs only authorized technical preparation.
"""
from pathlib import Path
import hashlib
import json
import math
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
ART=ROOT/'docs/art/ENG/icons'


def main():
    manifest=json.loads((ART/'manifest.json').read_text(encoding='utf-8'))
    assets=manifest['assets']
    missing=[a['source'] for a in assets if not (ROOT/a['source']).is_file()]
    if missing:raise SystemExit('Missing imagegen originals: '+', '.join(missing))
    sprites=[]
    preview=Image.new('RGBA',(1000,math.ceil(len(assets)/4)*210),(31,36,43,255))
    draw=ImageDraw.Draw(preview)
    font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',13)
    small=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',11)
    for index,asset in enumerate(assets):
        source=ROOT/asset['source']
        original=Image.open(source).convert('RGBA')
        assert min(original.size)>=512,asset['key']
        alpha=original.getchannel('A')
        assert alpha.getextrema()[0]==0 and alpha.getextrema()[1]>200,(asset['key'],'Missing genuine transparency')
        bounds=alpha.getbbox()
        assert bounds,asset['key']
        # No painting, recolouring, background synthesis or AI replacement.
        cutout=original.crop(bounds)
        width,height=asset['size']
        cutout.thumbnail((width-6,height-8 if asset['kind']=='spirit' else height-6),Image.Resampling.LANCZOS)
        canvas=Image.new('RGBA',(width,height),(0,0,0,0))
        canvas.alpha_composite(cutout,((width-cutout.width)//2,(height-cutout.height)//2))
        target=ROOT/asset['texture'];target.parent.mkdir(parents=True,exist_ok=True)
        canvas.save(target,format='DDS')
        asset['source_sha256']=hashlib.sha256(source.read_bytes()).hexdigest()
        asset['texture_sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
        asset['source_size']=list(original.size)
        asset['occupied_alpha_bounds']=list(canvas.getchannel('A').getbbox())
        sprites.append(f'\tspriteType = {{ name = {asset["sprite"]} texturefile = "{asset["texture"]}" }}')
        x,y=index%4*250,index//4*210
        # Large technical preview plus the exact native canvas beside it.
        large=original.crop(bounds)
        large.thumbnail((132,132),Image.Resampling.LANCZOS)
        preview.alpha_composite(large,(x+(150-large.width)//2,y+10+(132-large.height)//2))
        preview.alpha_composite(canvas,(x+166+(60-width)//2,y+43+(68-height)//2))
        draw.text((x+167,y+118),f'{width} x {height}',font=small,fill=(181,190,201))
        label=asset['ru']
        if len(label)>27:
            parts=label.split();line='';lines=[]
            for word in parts:
                if len(line+' '+word)>27:lines.append(line);line=word
                else:line=(line+' '+word).strip()
            lines.append(line)
        else:lines=[label]
        for n,line in enumerate(lines):draw.text((x+10,y+151+n*16),line,font=font,fill=(230,226,214))
        draw.text((x+10,y+189),asset['key'],font=small,fill=(154,164,179))
    (ROOT/'interface/ENG_icons.gfx').write_text('# Imagegen artwork, owner ENG. See docs/art/ENG/icons/manifest.json.\nspriteTypes = {\n'+'\n'.join(sprites)+'\n}\n',encoding='utf-8',newline='\n')
    preview.convert('RGB').save(ART/'preview.png')
    (ART/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f'Exported {len(assets)} distinct RGBA DDS icons; 60x68 spirits and 52x40 categories.')


if __name__=='__main__':main()
