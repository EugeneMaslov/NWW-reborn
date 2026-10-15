"""Extend the Ottoman art snapshot to native designers and AAT organizations."""
from pathlib import Path
from collections import defaultdict
import json,math
from PIL import Image,ImageDraw,ImageFont
from hoi4_script import read,one,values
from prepare_tur_art import ROOT,GAME,ART

manifest=json.loads((ART/'manifest.json').read_text(encoding='utf-8'))
assert not any(j['kind']=='company' for j in manifest['jobs']), 'Companies already captured'
groups=defaultdict(list)
company_ideas=one(read(GAME/'common/ideas/turkey.txt'),'ideas')
for category,body,o in company_ideas:
    if category in ('country','hidden_ideas'):continue
    for key,n,o in body:
        if isinstance(n,list) and one(n,'picture'):
            groups['GFX_idea_'+one(n,'picture')].append('company_idea:'+key)
for key,n,o in read(GAME/'common/military_industrial_organization/organizations/TUR_organization.txt'):
    if isinstance(n,list) and one(n,'icon'):groups[one(n,'icon')].append('company_mio:'+key)
sprites={}
for base in (GAME,ROOT):
    for p in (base/'interface').glob('*.gfx'):
        try:doc=read(p)
        except ValueError:continue
        for group in values(doc,'spriteTypes'):
            for kind,n,o in group:
                if kind.lower()=='spritetype' and isinstance(n,list) and one(n,'texturefile'):
                    sprites[one(n,'name')]=(one(n,'texturefile'),int(one(n,'noOfFrames','1')))
jobs=[]
for i,(sprite,consumers) in enumerate(groups.items()):
    key='company_'+sprite.removeprefix('GFX_idea_')
    texture,frames=sprites[sprite]
    p=ROOT/texture
    if not p.exists():p=GAME/texture
    im=Image.open(p).convert('RGBA')
    if frames>1:im=im.crop((0,0,im.width//frames,im.height))
    ref=ART/'references'/f'{key}.png';im.save(ref)
    names=[c.split(':',1)[1].replace('TUR_','').replace('_organization','').replace('_',' ') for c in consumers]
    jobs.append(dict(key=key,kind='company',sprite=sprite,source_texture=texture,reference=ref.relative_to(ROOT).as_posix(),consumers=consumers,names=names,
                     reference_sheet='docs/art/TUR/company_references.png',reference_column=i%6+1,reference_row=i//6+1,reference_number=i+1))
sheet=Image.new('RGBA',(960,math.ceil(len(jobs)/6)*154),(29,32,37,255));draw=ImageDraw.Draw(sheet)
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',11)
for i,j in enumerate(jobs):
    x,y=i%6*160,i//6*154;im=Image.open(ROOT/j['reference']);im.thumbnail((110,100))
    sheet.alpha_composite(im,(x+(160-im.width)//2,y+4))
    label=f'{i+1}: '+j['names'][0]
    draw.text((x+5,y+108),label[:24],font=font,fill='white');draw.text((x+5,y+123),label[24:48],font=font,fill='white')
sheet.save(ART/'company_references.png')
manifest['jobs'].extend(jobs)
(ART/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Added',len(jobs),'company drawings for',sum(len(j['consumers']) for j in jobs),'designer/MIO definitions')
