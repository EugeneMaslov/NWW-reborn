"""Install six generated LTB focus emblems as native DDS icons with animated highlights."""
import copy,json,shutil
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from hoi4_script import read,one,values,parse,dump
ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')
spec=json.loads((ROOT/'docs/art/LTB_focus_generation.json').read_text(encoding='utf-8'))
mapping={
 'consolidate_union':('LTB_consolidate_the_union','Укрепить Союз'),
 'vilnius_compromise':('LTB_the_vilnius_compromise','Виленский компромисс'),
 'face_crisis':('LTB_face_the_crisis','Встретить кризис'),
 'general_staff':('LTB_union_general_staff','Генеральный штаб'),
 'rebuild_bridge':('LTB_rebuild_the_bridge','Восстановить мост'),
 'union_endures':('LTB_the_union_endures','Союз выстоял')}
template=next(n for k,n,o in one(read(GAME/'interface/goals_shine.gfx'),'spriteTypes') if one(n,'name')=='GFX_focus_generic_diplomatic_treaty_shine')
def setv(node,k,v):
    node[:]=[(key,val,o) for key,val,o in node if key!=k];node.append((k,v,'='))
sprites=[];preview=Image.new('RGBA',(6*160,190),(24,30,40,255));draw=ImageDraw.Draw(preview)
font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',13)
tree_path=ROOT/'common/national_focus/ltb_focus.txt';tree=read(tree_path);focuses={one(f,'id'):f for f in values(one(tree,'focus_tree'),'focus')}
for i,job in enumerate(spec['assets']):
    key=job['key'];source=Path(job['source']);saved=ROOT/f'docs/art/ltb_focuses/{key}.png'
    saved.parent.mkdir(parents=True,exist_ok=True)
    if source.exists():shutil.copyfile(source,saved)
    elif not saved.exists():raise FileNotFoundError(source)
    (saved.with_suffix('.prompt.txt')).write_text(job['prompt']+'\n',encoding='utf-8')
    image=Image.open(saved).convert('RGBA');alpha=image.getchannel('A');bounds=alpha.point(lambda a:255 if a>8 else 0).getbbox()
    if not bounds or alpha.getextrema()[0]!=0:raise ValueError(key+': expected transparent generated artwork')
    image=image.crop(bounds);image.thumbnail((83,83),Image.Resampling.LANCZOS)
    canvas=Image.new('RGBA',(95,95));canvas.alpha_composite(image,((95-image.width)//2,(95-image.height)//2))
    relative=f'gfx/interface/goals/LTB/focus_{key}.dds';target=ROOT/relative;target.parent.mkdir(parents=True,exist_ok=True);canvas.save(target,format='DDS')
    sprite='GFX_focus_NWW_LTB_'+key
    sprites.extend(parse(f'spriteType = {{ name = {sprite} texturefile = "{relative}" }}'))
    shine=copy.deepcopy(template);setv(shine,'name',sprite+'_shine');setv(shine,'texturefile',relative)
    for anim in values(shine,'animation'):setv(anim,'animationmaskfile',relative)
    sprites.append(('spriteType',shine,'='))
    fid,label=mapping[key];setv(focuses[fid],'icon',sprite)
    preview.alpha_composite(canvas,(i*160+32,20));draw.text((i*160+7,130),label,fill='white',font=font)
    job['saved_source']=str(saved.relative_to(ROOT)).replace('\\','/');job['texture']=relative;job['focus']=fid;job['sprite']=sprite
(ROOT/'interface/LTB_focus_icons.gfx').write_text(dump([('spriteTypes',sprites,'=')])+'\n',encoding='utf-8')
tree_path.write_text(dump(tree)+'\n',encoding='utf-8');preview.save(ROOT/'docs/ltb_focus_icons_preview.png')
(ROOT/'docs/art/LTB_focus_generation.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Installed six 95x95 LTB focus icons, originals, prompts and six animated highlights.')
