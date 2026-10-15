"""Technical previews from actual GUI positions, sprite textures and localized text."""
from pathlib import Path
import re, math, json
from PIL import Image,ImageDraw,ImageFont
from hoi4_script import read,one,values,variable_check
ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')
OUT=ROOT/'docs/art/AUS'
local=dict(re.findall(r'^ (\w+):\d+ "(.*)"',(ROOT/'localisation/replace/AUS_crownlands_l_russian.yml').read_text(encoding='utf-8-sig'),re.M))
window=one(one(read(ROOT/'interface/AUS_bohemian_gui.gui'),'guiTypes'),'containerWindowType')
triggers=dict((k,v) for k,v,o in one(one(one(read(ROOT/'common/scripted_guis/AUS_bohemian_gui.txt'),'scripted_gui'),'AUS_bohemian_ui'),'triggers'))
sprites={}
for base in (GAME,ROOT):
    for p in (base/'interface').glob('*.gfx'):
        try:parsed=read(p)
        except ValueError:continue
        for block in values(parsed,'spriteTypes'):
            for kind,body,op in block:
                if kind.lower()=='spritetype' and isinstance(body,list):
                    name,texture=one(body,'name'),one(body,'texturefile')
                    if name and texture:sprites[name]=texture
def texture(sprite):
    p=ROOT/sprites[sprite]
    if not p.exists():p=GAME/sprites[sprite]
    return Image.open(p).convert('RGBA')
def visible(name,tension):
    for key,node,op in triggers.get(name+'_visible',[]):
        assert key=='check_variable'
        var,val,comparison=variable_check(node);val=float(val)
        if not {'=':tension==val,'>=':tension>=val,'<=':tension<=val}[comparison]:return False
    return True
column_width=502  # countrydecisionview.gui native decision-list slot width.
sheet=Image.new('RGBA',(column_width*2,256),(26,25,23,255))
for column,tension in enumerate((2,8)):
    panel=Image.new('RGBA',(column_width,228))
    draw=ImageDraw.Draw(panel)
    for kind,body,op in window:
        if kind not in ('iconType','instantTextBoxType'):continue
        if not visible(one(body,'name'),tension):continue
        pos=one(body,'position');x,y=int(one(pos,'x')),int(one(pos,'y'))
        if one(body,'orientation')=='center_up':x+=column_width//2
        if kind=='iconType':panel.alpha_composite(texture(one(body,'spriteType')),(x,y))
        else:
            text=local[one(body,'text')].replace('[?AUS_bohemian_tension|0]',str(tension))
            color=(230,220,193,255)
            if '§G' in text:color=(125,203,134,255)
            if '§Y' in text:color=(235,206,98,255)
            if '§R' in text:color=(232,112,96,255)
            text=re.sub('§.', '',text)
            font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18 if one(body,'font')=='hoi_18mbs' else 16)
            width=int(one(body,'maxWidth')); actual=draw.textlength(text,font=font)
            assert actual<=width,(text,actual,width)
            draw.text((x+width/2,y),text,font=font,fill=color,anchor='mt',stroke_width=0)
    sheet.alpha_composite(panel,(column*column_width,16))
sheet.convert('RGB').save(OUT/'bohemian_panel_preview.png')
mapping=json.loads((OUT/'focus_icon_map.json').read_text())
sheet=Image.new('RGBA',(1100,math.ceil(len(mapping)/10)*124),(36,36,33,255))
d=ImageDraw.Draw(sheet);font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',10)
for i,(fid,icon) in enumerate(mapping.items()):
    x,y=i%10*110,i//10*124
    im=texture(icon);im.thumbnail((96,96),Image.Resampling.LANCZOS)
    sheet.alpha_composite(im,(x+(110-im.width)//2,y))
    label=fid.removeprefix('AUS_nww2_').removeprefix('AUS_')
    d.text((x+55,y+97),label[:20],font=font,fill='white',anchor='mt')
    if len(label)>20:d.text((x+55,y+109),label[20:40],font=font,fill='white',anchor='mt')
sheet.convert('RGB').save(OUT/'focus_icons_preview.png')
print('Saved technical previews: bohemian_panel_preview.png and focus_icons_preview.png')
