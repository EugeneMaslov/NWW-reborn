"""Convert project-bound generated MKN originals to native game textures."""
from pathlib import Path
import json
from PIL import Image, ImageDraw
from hoi4_script import read, one, values, dump
ROOT=Path(__file__).resolve().parents[1]
people=json.loads((ROOT/'docs/MKN_personnel.json').read_text())
path=ROOT/'interface/nww_mkn_portraits.gfx';gfx=read(path)
sprites={one(s,'name'):s for s in values(one(gfx,'spriteTypes'),'spriteType')}
commanders=[p for p in people if p['prompt_subject']]
preview=Image.new('RGBA',(len(commanders)*175,320),(26,31,41,255));draw=ImageDraw.Draw(preview)
for i,person in enumerate(commanders):
 key=person['key'];image=Image.open(ROOT/f'docs/art/mkn_commanders/{key}.png').convert('RGBA')
 image=image.crop(image.getchannel('A').getbbox())
 # Technical framing: trim only outer shoulder width, preserving the full head.
 width=min(image.width,round(image.height*156/210));left=(image.width-width)//2
 image=image.crop((left,0,left+width,image.height))
 large=image.copy();large.thumbnail((148,202),Image.Resampling.LANCZOS)
 canvas=Image.new('RGBA',(156,210));canvas.alpha_composite(large,((156-large.width)//2,4))
 asset=f'gfx/leaders/MKN/{key}.dds';canvas.save(ROOT/asset,format='DDS')
 large_sprite=sprites['GFX_Portrait_MKN_'+key]
 large_sprite[:]=[(k,asset if k=='texturefile' else v,o) for k,v,o in large_sprite]
 # Cut lower torso before fitting the advisor slot. Last six rows stay transparent.
 small=image.crop((0,0,image.width,round(image.height*.78)))
 small.thumbnail((57,59),Image.Resampling.LANCZOS)
 card=Image.new('RGBA',(65,67));card.alpha_composite(small,((65-small.width)//2,2))
 bounds=card.getchannel('A').getbbox();assert bounds and bounds[3]<=61,bounds
 asset=f'gfx/interface/ideas/nww_portraits/MKN_{key}.dds';card.save(ROOT/asset,format='DDS')
 small_sprite=sprites['GFX_idea_MKN_'+key]
 small_sprite[:]=[(k,asset if k=='texturefile' else v,o) for k,v,o in small_sprite]
 preview.alpha_composite(canvas,(i*175+8,8));preview.alpha_composite(card,(i*175+52,229))
 draw.text((i*175+3,303),key,fill='white')
path.write_text(dump(gfx)+'\n');preview.save(ROOT/'docs/mkn_commander_portraits_preview.png')
print('Built',len(commanders),'large commander portraits and native advisor cards with alpha clearance')
for source in sorted((ROOT/'docs/art/mkn_companies').glob('*.png')):
    for prefix, size, occupied in [('company',(65,67),(53,53)),('focus',(96,96),(88,88))]:
        image=Image.open(source).convert('RGBA')
        image=image.crop(image.getchannel('A').getbbox())
        image.thumbnail(occupied,Image.Resampling.LANCZOS)
        canvas=Image.new('RGBA',size)
        offset=((size[0]-image.width)//2,4 if prefix=='company' else (size[1]-image.height)//2)
        canvas.alpha_composite(image,offset)
        if prefix=='company':assert canvas.getchannel('A').getbbox()[3]<=61
        canvas.save(ROOT/f'gfx/interface/ideas/MKN/{prefix}_{source.stem}.dds',format='DDS')
print('Rebuilt company emblems with native card clearance and selected focus icons')
