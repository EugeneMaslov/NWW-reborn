"""Export generated manufacturer emblems to small transparent DDS assets."""
from pathlib import Path
from PIL import Image, ImageDraw
from hoi4_script import read, one, values, dump

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'docs/art/ltb_companies/generated'
path=ROOT/'interface/nww_companies.gfx'
doc=read(path)
sprites={one(s,'name'):s for s in values(one(doc,'spriteTypes'),'spriteType')}
sources=sorted(SOURCE.glob('*.png'))
preview=Image.new('RGBA',(len(sources)*115,110),(28,33,43,255));draw=ImageDraw.Draw(preview)
for i,source in enumerate(sources):
    image=Image.open(source).convert('RGBA')
    bounds=image.getchannel('A').getbbox()
    if bounds:image=image.crop(bounds)
    image.thumbnail((60,60),Image.Resampling.LANCZOS)
    canvas=Image.new('RGBA',(64,64))
    canvas.alpha_composite(image,((64-image.width)//2,(64-image.height)//2))
    relative=f'gfx/interface/ideas/LTB/idea_nww_company_{source.stem}.dds'
    canvas.save(ROOT/relative,format='DDS')
    sprite=sprites['GFX_idea_'+source.stem]
    sprite[:]=[(k,relative if k=='texturefile' else v,o) for k,v,o in sprite]
    preview.alpha_composite(canvas,(i*115+25,5));draw.text((i*115+3,80),source.stem,fill='white')
    print(relative)
path.write_text(dump(doc)+'\n',encoding='utf-8')
preview.save(ROOT/'docs/ltb_company_icons_preview.png')
