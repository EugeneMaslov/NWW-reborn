"""Export generated LTB national-spirit artwork to native 64x64 DDS sprites."""
from pathlib import Path
from PIL import Image, ImageDraw
from hoi4_script import parse, read, one, dump

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'docs/art/ltb_ideas'
OUTPUT = ROOT/'gfx/interface/ideas/LTB'
OUTPUT.mkdir(parents=True, exist_ok=True)
sprites = []
sources = sorted(SOURCE.glob('nww_ltb_*.png'))
preview = Image.new('RGBA',(6*120,150),(24,30,40,255))
draw = ImageDraw.Draw(preview)
for index, source in enumerate(sources):
    icon = Image.open(source).convert('RGBA')
    bounds = icon.getchannel('A').getbbox()
    if bounds:
        icon = icon.crop(bounds)
    icon.thumbnail((62,62),Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA',(64,64))
    canvas.alpha_composite(icon,((64-icon.width)//2,(64-icon.height)//2))
    relative = f'gfx/interface/ideas/LTB/idea_{source.stem}.dds'
    canvas.save(ROOT/relative,format='DDS')
    sprites.extend(parse(f'spriteType = {{ name = GFX_idea_{source.stem} texturefile = "{relative}" }}'))
    preview.alpha_composite(canvas,(index*120+28,15))
    draw.text((index*120+4,95),source.stem.replace('nww_ltb_',''),fill='white')
    print(relative)
(ROOT/'interface/nww_ltb_ideas.gfx').write_text(dump([('spriteTypes',sprites,'=')])+'\n',encoding='utf-8')
preview.save(ROOT/'docs/ltb_idea_icons_preview.png')

doc = read(ROOT/'common/ideas/nww_LTB_ideas.txt')
mapping = {
    'LTB_unresolved_national_question':'national_question',
    'LTB_vilnius_compromise':'union', 'LTB_kaunas_centralism':'army',
    'LTB_minsk_arsenal':'arsenal', 'LTB_union_army_tradition':'union',
    'LTB_disorganized_army':'army', 'LTB_depression_legacy':'depression',
    'LTB_depression_legacy_1':'depression',
    'LTB_constitutional_crown':'union', 'LTB_federal_democracy':'union',
    'LTB_national_mobilization':'arsenal', 'LTB_workers_federation':'arsenal'
}
for idea, body, op in one(one(doc,'ideas'),'country'):
    artwork = mapping.get(idea)
    if idea.startswith('LTB_semi_agrarian_economy'):
        artwork = 'agrarian'
    if artwork:
        body[:] = [(k,'nww_ltb_'+artwork if k=='picture' else v,o) for k,v,o in body]
(ROOT/'common/ideas/nww_LTB_ideas.txt').write_text(dump(doc)+'\n',encoding='utf-8')
