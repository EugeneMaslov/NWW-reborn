"""Snapshot all active Ottoman icon references and build image-generation catalogs."""
from pathlib import Path
from collections import defaultdict
import json,re,math,shutil
from PIL import Image,ImageDraw,ImageFont
from hoi4_script import read,one,values
ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')
ART=ROOT/'docs/art/TUR'

def main():
    ART.mkdir(parents=True,exist_ok=True)
    if (ART/'manifest.json').exists():
        raise SystemExit('Original references already captured. Keep this snapshot; do not replace it with installed generated art.')
    sprites={}
    for base in (GAME,ROOT):
        for p in (base/'interface').glob('*.gfx'):
            try:doc=read(p)
            except ValueError:continue
            for group in values(doc,'spriteTypes'):
                for kind,body,op in group:
                    if kind.lower()=='spritetype' and isinstance(body,list):
                        name,texture=one(body,'name'),one(body,'texturefile')
                        if name and texture:sprites[name]={'texture':texture,'frames':int(one(body,'noOfFrames','1'))}
    loc={}
    for path in (ROOT/'localisation').rglob('*TUR*_l_english.yml'):
        loc.update(re.findall(r'^ ([\w.]+):\d* "(.*)"',path.read_text(encoding='utf-8-sig'),re.M))
    groups=defaultdict(list)
    tree=one(read(ROOT/'common/national_focus/TUR_focuses.txt'),'focus_tree')
    for focus in values(tree,'focus'):
        groups[('focus',one(focus,'icon'))].append(one(focus,'id'))
    ideas=one(read(ROOT/'common/ideas/TUR_ideas.txt'),'ideas')
    # Split a generic reused picture when it represents different local programs.
    for category,body,op in ideas:
        for key,node,operator in body:
            if not isinstance(node,list):continue
            sprite='GFX_idea_'+one(node,'picture')
            concept=re.sub(r'_\d+$','',key)
            if concept.startswith('NWW_TUR_imperial_crisis'):concept='imperial_crisis'
            elif concept=='NWW_TUR_imperial_compact':concept='imperial_compact'
            groups[('idea',sprite,concept)].append(key)
    for category,node,op in read(ROOT/'common/decisions/TUR_decisions.txt'):
        for key,body,operator in node:
            if not isinstance(body,list):continue
            icon=one(body,'icon')
            if icon:groups[('decision',icon if icon.startswith('GFX_') else 'GFX_decision_'+icon)].append(key)
    for key,body,op in read(ROOT/'common/decisions/categories/TUR_categories.txt'):
        icon=one(body,'icon')
        if icon:groups[('category',icon if icon.startswith('GFX_') else 'GFX_decision_category_'+icon)].append(key)
    jobs=[]
    for group,consumers in groups.items():
        kind,sprite=group[:2]
        key=kind+'_'+(group[2] if len(group)>2 else consumers[0])
        source=sprites[sprite]
        p=ROOT/source['texture']
        if not p.exists():p=GAME/source['texture']
        im=Image.open(p).convert('RGBA')
        if source['frames']>1:im=im.crop((0,0,im.width//source['frames'],im.height))
        ref=ART/'references'/f'{key}.png';ref.parent.mkdir(exist_ok=True)
        im.save(ref)
        jobs.append({'key':key,'kind':kind,'sprite':sprite,'source_texture':source['texture'],'reference':ref.relative_to(ROOT).as_posix(),'consumers':consumers,'names':[loc.get(n,n) for n in consumers]})
    font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',11)
    for kind in ('focus','idea','decision','category'):
        subset=[j for j in jobs if j['kind']==kind]
        columns=7 if kind=='focus' else 6
        sheet=Image.new('RGBA',(columns*160,math.ceil(len(subset)/columns)*154),(29,32,37,255));draw=ImageDraw.Draw(sheet)
        for i,job in enumerate(subset):
            x,y=i%columns*160,i//columns*154
            im=Image.open(ROOT/job['reference']);im.thumbnail((110,100),Image.Resampling.LANCZOS)
            sheet.alpha_composite(im,(x+(160-im.width)//2,y+4))
            label=f'{i+1}: '+job['names'][0]
            draw.text((x+5,y+108),label[:24],font=font,fill='white')
            draw.text((x+5,y+123),label[24:48],font=font,fill='white')
            job.update(reference_sheet=f'docs/art/TUR/{kind}_references.png',reference_column=i%columns+1,reference_row=i//columns+1,reference_number=i+1)
        sheet.save(ART/f'{kind}_references.png')
    (ART/'manifest.json').write_text(json.dumps({'jobs':jobs},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('Jobs:',len(jobs),{kind:sum(j['kind']==kind for j in jobs) for kind in ('focus','idea','decision','category')})
    for job in jobs:
        if job['kind']!='focus':print(job['key'],job['names'][0])

if __name__=='__main__':main()
