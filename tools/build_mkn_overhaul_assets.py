"""Project-local Pillow artwork and technical portrait compositing."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
from patch_mkn_overhaul import ROOT, save, block, put
from hoi4_script import read, one, values
from copy import deepcopy

def icon(kind, size=128):
    im=Image.new('RGBA',(size,size))
    d=ImageDraw.Draw(im)
    d.ellipse((12,10,116,114),fill=(35,38,42),outline=(175,147,87),width=4)
    d.ellipse((19,17,109,107),outline=(90,79,56),width=2)
    color={'militarism':(177,76,58),'nabat':(108,152,175),'agrarian':(182,162,91),'revkom':(150,65,55),'workshops':(133,158,136)}[kind]
    if kind=='militarism':
        for x in (44,79):
            d.polygon([(x,32),(x+9,32),(x+9,78),(x+4,89),(x,78)],fill=color,outline=(220,207,170))
        d.line((33,61,92,61),fill=(207,181,122),width=5)
        d.rectangle((40,82,52,95),fill=(121,99,58));d.rectangle((75,82,87,95),fill=(121,99,58))
    elif kind=='nabat':
        d.polygon([(32,49),(59,43),(64,48),(69,43),(96,49),(96,89),(68,82),(64,87),(59,82),(32,89)],fill=color,outline=(221,213,189))
        d.line((64,50,64,83),fill=(228,215,179),width=2)
        for y in range(57,78,7):
            d.line((38,y,56,y-2),fill=(46,57,66),width=2);d.line((72,y-2,90,y),fill=(46,57,66),width=2)
    elif kind=='agrarian':
        for x in (43,64,85):
            d.line((x,34,x,94),fill=color,width=3)
            for y in (43,54,65,76):
                d.ellipse((x-11,y-9,x,y+1),fill=color);d.ellipse((x,y-9,x+11,y+1),fill=color)
    elif kind=='revkom':
        d.polygon([(39,34),(90,34),(90,94),(39,94)],fill=(184,173,145),outline=(215,204,167))
        for y in (46,55,64):d.line((48,y,82,y),fill=(53,51,47),width=3)
        d.ellipse((53,70,83,100),fill=color,outline=(210,164,114),width=2)
        d.polygon([(68,75),(71,83),(79,83),(73,89),(75,96),(68,91),(61,96),(63,89),(57,83),(65,83)],fill=(207,186,139))
    else:
        d.polygon([(30,95),(30,61),(51,49),(51,62),(72,49),(72,63),(91,51),(99,95)],fill=color,outline=(212,195,151))
        d.rectangle((36,34,45,68),fill=(132,143,137))
        for x in range(38,91,13):d.rectangle((x,75,x+7,86),fill=(42,44,43))
        d.ellipse((47,17,63,31),fill=(100,104,104));d.ellipse((59,12,84,26),fill=(80,83,86))
    # Soft relief shadow stays within the alpha canvas; no solid square backdrop.
    shadow=Image.new('RGBA',im.size)
    shadow.putalpha(im.getchannel('A').filter(ImageFilter.GaussianBlur(2)))
    return Image.alpha_composite(shadow,im)

def main():
    out=ROOT/'gfx/interface/goals';out.mkdir(parents=True,exist_ok=True)
    originals=ROOT/'gfx/generated_sources/MKN_overhaul';originals.mkdir(parents=True,exist_ok=True)
    sprites=[]
    for kind in ('militarism','nabat','agrarian','revkom','workshops'):
        artwork=icon(kind)
        artwork.save(originals/f'{kind}.png')
        artwork.save(out/f'MKN_{kind}.dds')
        sid='GFX_idea_MKN_free_workshops' if kind=='workshops' else 'GFX_focus_MKN_'+kind
        sprites.append(f'spriteType = {{ name = {sid} texturefile = "gfx/interface/goals/MKN_{kind}.dds" }}')
        if kind=='revkom':sprites.append('spriteType = { name = GFX_idea_MKN_revkom texturefile = "gfx/interface/goals/MKN_revkom.dds" }')
    save('interface/MKN_overhaul_icons.gfx',block('spriteTypes = { '+' '.join(sprites)+' }'))
    template=values(one(read(ROOT/'interface/MKN_focus_shine.gfx'),'spriteTypes'),'spriteType')[0]
    shine=[]
    for kind in ('militarism','nabat','agrarian','revkom','workshops'):
        node=deepcopy(template)
        sprite='GFX_idea_MKN_free_workshops' if kind=='workshops' else 'GFX_focus_MKN_'+kind
        texture='gfx/interface/goals/MKN_'+kind+'.dds'
        put(node,'name',sprite+'_shine');put(node,'texturefile',texture)
        for animation in values(node,'animation'):put(animation,'animationmaskfile',texture)
        shine.append(('spriteType',node,'='))
    save('interface/MKN_overhaul_shine.gfx',[('spriteTypes',shine,'=')])
    path='common/national_focus/MKN.txt';doc=read(ROOT/path)
    ids={'MKN_military_takes_charge':'militarism','MKN_triumph_of_free_soviets':'nabat','MKN_peasant_delegates':'agrarian','MKN_emergency_revkom':'revkom'}
    for f in values(one(doc,'focus_tree'),'focus'):
        if one(f,'id') in ids:put(f,'icon','GFX_focus_MKN_'+ids[one(f,'id')])
    save(path,doc)
    portrait_sources=originals/'portraits';portrait_sources.mkdir(exist_ok=True)
    for path in (ROOT/'gfx/leaders/MKN').glob('*'):
        if path.suffix.lower() not in ('.dds','.png','.tga'):continue
        with Image.open(path) as source:
            rgba=source.convert('RGBA')
        if rgba.getchannel('A').getextrema()[0] == 255:continue
        backup=portrait_sources/(path.stem+'.png')
        if not backup.exists():rgba.save(backup)
        w,h=rgba.size
        bg=Image.new('RGBA',(w,h),(53,56,61,255));p=bg.load()
        for y in range(h):
            for x in range(w):
                factor=max(0.65,1-0.20*(((x-w/2)/(w/2))**2+((y-h/2)/(h/2))**2))
                p[x,y]=(int(53*factor),int(56*factor),int(61*factor),255)
        Image.alpha_composite(bg,rgba).save(path)

if __name__=='__main__':main()
