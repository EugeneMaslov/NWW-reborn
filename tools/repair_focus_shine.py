"""Register missing focus highlight sprites using the installed game's animation template."""
import copy
from pathlib import Path
from hoi4_script import read,one,values,walk,dump
ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')
sprites={}
for root in (GAME,*sorted(GAME.glob('dlc/*')),ROOT):
    for p in root.glob('interface/**/*.gfx'):
        try:doc=read(p)
        except ValueError:continue
        for k,node,o in walk(doc):
            if k and k.lower()=='spritetype':sprites[one(node,'name')]=node
template=sprites['GFX_focus_generic_diplomatic_treaty_shine']
def replace(doc,key,value):
    doc[:]=[(k,v,o) for k,v,o in doc if k!=key];doc.append((key,value,'='))
count=0
for p in ROOT.glob('common/national_focus/*.txt'):
    doc=read(p)
    for tree in values(doc,'focus_tree'):
        country=one(one(one(tree,'country',[]),'modifier',[]),'tag')
        if not country:continue
        missing=[]
        for f in values(tree,'focus'):
            icon=one(f,'icon')
            if not isinstance(icon,str) or icon+'_shine' in sprites:continue
            if icon not in sprites:raise ValueError('Unknown focus icon '+icon)
            sprite=copy.deepcopy(template);texture=one(sprites[icon],'texturefile')
            replace(sprite,'name',icon+'_shine');replace(sprite,'texturefile',texture)
            for anim in values(sprite,'animation'):replace(anim,'animationmaskfile',texture)
            missing.append(('spriteType',sprite,'='));sprites[icon+'_shine']=sprite
        if missing:
            target=ROOT/f'interface/{country}_focus_shine.gfx'
            existing=one(read(target),'spriteTypes',[]) if target.exists() else []
            existing.extend(missing);target.write_text(dump([('spriteTypes',existing,'=')])+'\n',encoding='utf-8');count+=len(missing)
print(f'Registered {count} missing focus shine sprites.')
