"""Technical alpha-preserving DDS exports from imagegen originals; code-drawn UI panels."""
from pathlib import Path
import copy
import json
import base64
import html
from PIL import Image, ImageDraw, ImageFont
from hoi4_script import read, one, values, dump

ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')
KEYS='republic crown leagues labour cabinet industry army air navy science overseas'.split()

def setv(node,key,value):
    node[:]=[(k,v,o) for k,v,o in node if k!=key]
    node.append((key,value,'='))

def main():
    sprites=[]; manifest=[]; previews=[]
    template=next(v for k,v,o in one(read(GAME/'interface/goals_shine.gfx'),'spriteTypes') if one(v,'name')=='GFX_focus_generic_diplomatic_treaty_shine')
    for key in KEYS:
        source=ROOT/f'gfx/generated_sources/FRA/{key}.png'
        with Image.open(source) as im: original=im.convert('RGBA')
        # Threshold only for occupied bounds; preserve original alpha in the crop.
        bounds=original.getchannel('A').point(lambda a:255 if a>12 else 0).getbbox()
        if bounds is None: raise ValueError('Empty artwork '+key)
        cropped=original.crop(bounds)
        for suffix,size,occupied,folder in [('',(95,85),(79,75),'goals'),('_idea',(64,64),(56,53),'ideas')]:
            art=cropped.copy();art.thumbnail(occupied,Image.Resampling.LANCZOS)
            canvas=Image.new('RGBA',size)
            canvas.alpha_composite(art,((size[0]-art.width)//2,(size[1]-art.height)//2-1))
            path=f'gfx/interface/{folder}/FRA/{key}.dds'
            out=ROOT/path;out.parent.mkdir(parents=True,exist_ok=True);canvas.save(out,format='DDS')
            # Idea loader requests GFX_idea_<picture>; dynamic modifiers use an explicit sprite.
            names=[f'GFX_FRA_nww_{key}{suffix}'] if not suffix else [f'GFX_FRA_nww_{key}_idea',f'GFX_idea_FRA_nww_{key}']
            for name in names: sprites.append(('spriteType',[('name',name,'='),('texturefile',path,'=')],'='))
            if not suffix:
                shine=copy.deepcopy(template);setv(shine,'name',names[0]+'_shine');setv(shine,'texturefile',path)
                for animation in values(shine,'animation'):setv(animation,'animationmaskfile',path)
                sprites.append(('spriteType',shine,'='));previews.append((key,canvas))
            manifest.append({'key':key,'kind':'idea' if suffix else 'focus','source':str(source.relative_to(ROOT)).replace('\\','/'),'texture':path,'size':size,'alpha_bounds':canvas.getchannel('A').getbbox()})
    ui=ROOT/'gfx/interface/FRA';ui.mkdir(parents=True,exist_ok=True)
    # Native GUI elements and generated emblem artwork, no raster synthesis of new artwork.
    for panel,height,emblem in [('mandate',240,'republic'),('overseas',410,'overseas')]:
        im=Image.new('RGBA',(440,height),(24,32,42,245));d=ImageDraw.Draw(im)
        d.rounded_rectangle((2,2,437,height-3),radius=9,outline=(160,133,80,255),width=2)
        d.line((14,44,426,44),fill=(160,133,80,255),width=1)
        for x,color in [(18,(45,74,128,255)),(23,(218,216,194,255)),(28,(151,46,46,255))]:d.rectangle((x,15,x+4,32),fill=color)
        with Image.open(ROOT/f'gfx/interface/ideas/FRA/{emblem}.dds') as src:badge=src.convert('RGBA')
        badge.thumbnail((34,34));im.alpha_composite(badge,(392,8))
        path=f'gfx/interface/FRA/{panel}_panel.dds';im.save(ROOT/path,format='DDS')
        sprites.append(('spriteType',[('name',f'GFX_FRA_{panel}_panel','='),('texturefile',path,'=')],'='))
    for key,color in [('socket',(37,42,48,255)),('gold',(187,150,72,255)),('red',(164,64,56,255))]:
        im=Image.new('RGBA',(32,12));d=ImageDraw.Draw(im);d.rounded_rectangle((0,0,31,11),radius=2,fill=color,outline=(122,112,90,255))
        path=f'gfx/interface/FRA/meter_{key}.dds';im.save(ROOT/path,format='DDS')
        sprites.append(('spriteType',[('name',f'GFX_FRA_meter_{key}','='),('texturefile',path,'=')],'='))
    (ROOT/'interface/FRA_art.gfx').write_text(dump([('spriteTypes',sprites,'=')]),encoding='utf-8',newline='\n')
    docs=ROOT/'docs/art/FRA';docs.mkdir(parents=True,exist_ok=True)
    (docs/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    sheet=Image.new('RGB',(660,230),(24,32,42));d=ImageDraw.Draw(sheet)
    for i,(key,im) in enumerate(previews):
        x=(i%6)*110;y=(i//6)*115
        sheet.paste(im,(x+7,y+2),im);d.text((x+7,y+91),key,fill=(224,215,183))
    sheet.save(docs/'icons_preview.png')
    # Static preview uses the same geometry and values as the scripted GUI.
    for panel,rows in [('mandate',[('Mandate',35),('Street tension',40)]),('overseas',[(k,35) for k in ['Algeria','Maghreb','West Africa','Equatorial Africa','Indochina','Islands']])]:
        with Image.open(ui/f'{panel}_panel.dds') as src:im=src.convert('RGBA')
        d=ImageDraw.Draw(im);d.text((70,20),'FRENCH '+panel.upper(),fill=(228,215,185))
        for i,(name,value) in enumerate(rows):
            y=62+i*77 if panel=='mandate' else 54+i*54
            d.text((20,y),f'{name}: {value}/100',fill=(228,215,185))
            for j in range(10):
                kind='red' if panel=='mandate' and i==1 else 'gold'
                with Image.open(ui/f'meter_{kind if value >= (j+1)*10 else "socket"}.dds') as src:tile=src.convert('RGBA')
                im.alpha_composite(tile,(30+j*38,y+27))
        im.save(docs/f'{panel}_panel_preview.png')
    # Review artifact derived from the actual game graph, not a separate concept diagram.
    tree=one(read(ROOT/'common/national_focus/FRA_focuses.txt'),'focus_tree')
    nodes=values(tree,'focus');by_id={one(n,'id'):n for n in nodes}
    labels=dict(__import__('re').findall(r'^\s+([\w.]+):0 "(.*)"$',(ROOT/'localisation/russian/FRA_nww_l_russian.yml').read_text(encoding='utf-8-sig'),__import__('re').M))
    positions={fid:((int(one(n,'x'))+13)*96+80,int(one(n,'y'))*116+100) for fid,n in by_id.items()}
    width=max(x for x,y in positions.values())+160;height=max(y for x,y in positions.values())+160
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',f'<rect width="{width}" height="{height}" fill="#18202a"/>','<style>text{font-family:Arial,sans-serif;fill:#e0d7b7;font-size:12px}</style>']
    for fid,n in by_id.items():
        x,y=positions[fid]
        for block in values(n,'prerequisite'):
            for parent in values(block,'focus'):
                px,py=positions[parent];dash='stroke-dasharray="5 5"' if len(values(block,'focus'))>1 else ''
                svg.append(f'<path d="M{px},{py+36} L{x},{y-38}" fill="none" stroke="#887959" {dash}/>')
    for fid,n in by_id.items():
        x,y=positions[fid];key=one(n,'icon').removeprefix('GFX_FRA_nww_')
        with Image.open(ROOT/f'gfx/interface/goals/FRA/{key}.dds') as src:
            import io
            buff=io.BytesIO();src.save(buff,format='PNG');encoded=base64.b64encode(buff.getvalue()).decode()
        svg.append(f'<image x="{x-47}" y="{y-42}" width="95" height="85" href="data:image/png;base64,{encoded}"/>')
        title=html.escape(labels.get(fid,fid));svg.append(f'<text x="{x}" y="{y+54}" text-anchor="middle"><title>{title} — {int(one(n,"cost"))*7} дней</title>{title[:29]}</text>')
    svg.append('</svg>');(docs/'focus_tree.svg').write_text('\n'.join(svg),encoding='utf-8',newline='\n')
    print(f'France: {len(KEYS)} original emblems, {len(manifest)} DDS exports, two decision panels, focus shine definitions.')

if __name__=='__main__':main()
