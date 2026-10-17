"""Technical DDS conversion of eight imagegen originals; native shine bindings."""
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import math
import re
from PIL import Image, ImageDraw, ImageFont
from hoi4_script import read,one,walk,dump
from britain_focus_icons import ICONS,CUSTOM

ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')
ART=ROOT/'docs/art/ENG/focuses'


def main():
    native={}
    for file in (GAME/'interface').glob('*.gfx'):
        try:doc=read(file)
        except ValueError:continue
        for k,v,_ in walk(doc):
            if k and k.lower()=='spritetype':native[one(v,'name')]=v
    sprites=[];assets=[]
    for key in CUSTOM:
        source=ART/'originals'/f'{key}.png'
        original=Image.open(source).convert('RGBA');alpha=original.getchannel('A')
        assert alpha.getextrema()[0]==0 and alpha.getextrema()[1]>200,key+': no transparency'
        art=original.crop(alpha.getbbox());art.thumbnail((86,86),Image.Resampling.LANCZOS)
        canvas=Image.new('RGBA',(96,96),(0,0,0,0));canvas.alpha_composite(art,((96-art.width)//2,(96-art.height)//2))
        texture=f'gfx/interface/goals/ENG/ENG_nww_{key}.dds';target=ROOT/texture
        target.parent.mkdir(parents=True,exist_ok=True);canvas.save(target,format='DDS')
        sprite=ICONS[key]
        sprites.append(('spriteType',[('name',sprite,'='),('texturefile',texture,'=')],'='))
        shine=deepcopy(native['GFX_goal_generic_alliance_shine'])
        for i,(k,v,o) in enumerate(shine):
            if k=='name':shine[i]=(k,sprite+'_shine',o)
            elif k=='texturefile':shine[i]=(k,texture,o)
            elif k=='animation':shine[i]=(k,[(a,texture if a=='animationmaskfile' else b,c) for a,b,c in v],o)
        sprites.append(('spriteType',shine,'='))
        assets.append({'key':key,'sprite':sprite,'texture':texture,'source':source.relative_to(ROOT).as_posix(),
                       'prompt':(ART/'prompts'/f'{key}.txt').relative_to(ROOT).as_posix(),'size':[96,96],
                       'alpha_bounds':list(canvas.getchannel('A').getbbox()),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                       'texture_sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
    (ROOT/'interface/ENG_focus_icons.gfx').write_text('# Owner ENG. Imagegen originals/prompts: docs/art/ENG/focuses.\n'+dump([('spriteTypes',sprites,'=')])+'\n',encoding='utf-8',newline='\n')
    manifest={'assets':assets,'assignments':ICONS,'unique_sprites':len(set(ICONS.values())),
              'reference_files':['interface/goals.gfx','interface/MTG_goals.gfx','common/national_focus/uk.txt']}
    (ART/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    native.update({one(v,'name'):v for _,v,_ in sprites})
    labels=dict(re.findall(r'^\s+(\w+):\d+ "(.*)"$',(ROOT/'localisation/russian/ENG_nww_l_russian.yml').read_text(encoding='utf-8-sig'),re.M))
    # Review sheet uses the same DDS textures as the game, with technical scaling.
    sheet=Image.new('RGB',(1120,635),(24,30,40));draw=ImageDraw.Draw(sheet)
    font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',15)
    draw.text((20,14),'NWW REBORN · КЛЮЧЕВЫЕ ФОКУСЫ ВЕЛИКОБРИТАНИИ',font=font,fill=(230,211,163))
    for i,key in enumerate(CUSTOM):
        x=20+i%4*275;y=52+i//4*280
        im=Image.open(ROOT/next(a['texture'] for a in assets if a['key']==key)).convert('RGBA')
        large=im.resize((192,192),Image.Resampling.NEAREST);sheet.paste(large,(x+29,y),large)
        label=labels['ENG_nww_'+key];parts=label.split();line='';lines=[]
        for word in parts:
            if draw.textlength((line+' '+word).strip(),font=font)>250:lines.append(line);line=word
            else:line=(line+' '+word).strip()
        if line:lines.append(line)
        for j,line in enumerate(lines):draw.text((x,y+200+j*21),line,font=font,fill=(224,226,228))
    sheet.save(ART/'preview.png')
    foci=json.loads((ROOT/'docs/ENG_focus_manifest.json').read_text(encoding='utf-8'))
    contact=Image.new('RGB',(1440,70+math.ceil(len(foci)/8)*158),(24,30,40));d=ImageDraw.Draw(contact)
    small=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',12)
    d.text((20,14),f'Все 153 фокуса · {len(set(ICONS.values()))} разных значков · 8 собственных эмблем',font=font,fill=(230,211,163))
    for i,f in enumerate(foci):
        x=i%8*180;y=60+i//8*158;node=native[ICONS[f['key']]];texture=one(node,'texturefile')
        path=next((base/texture for base in [ROOT,GAME] if (base/texture).exists()),None)
        assert path,texture
        im=Image.open(path).convert('RGBA');im.thumbnail((96,92),Image.Resampling.LANCZOS)
        contact.paste(im,(x+(180-im.width)//2,y),im)
        text=labels[f['id']];words=text.split();lines=[];line=''
        for word in words:
            if d.textlength((line+' '+word).strip(),font=small)>168:lines.append(line);line=word
            else:line=(line+' '+word).strip()
        if line:lines.append(line)
        for j,line in enumerate(lines[:3]):d.text((x+6,y+96+j*17),line,font=small,fill=(224,226,228))
    contact.save(ART/'all_focuses.png')
    print(f'Exported eight 96x96 focus emblems, 16 normal/shine sprites and {len(set(ICONS.values()))} unique focus icons across all 153 focuses.')


if __name__=='__main__':main()
