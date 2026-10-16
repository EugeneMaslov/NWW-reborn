"""Technical export of project-owned imagegen portraits; no creative drawing."""
from pathlib import Path
import hashlib
import json
from PIL import Image, ImageOps, ImageStat

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT/'docs/art/mkn_successors'
assets = []
for key in ('osyp_tsebriy', 'communal_council'):
    source = ART/(key+'.png')
    with Image.open(source) as im:
        im = im.convert('RGB')
        # The council is a group: retain the full horizontal composition.
        portrait = ImageOps.fit(im, (156, 210), Image.Resampling.LANCZOS, centering=(0.5, 0.40))
    target = ROOT/'gfx/leaders/MKN'/(key+'.dds')
    portrait.convert('RGBA').save(target, pixel_format='DXT5')
    assets.append(dict(key=key, source=str(source.relative_to(ROOT)), prompt=str((ART/(key+'.prompt.txt')).relative_to(ROOT)),
        texture=str(target.relative_to(ROOT)), size=[156, 210], source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        export_sha256=hashlib.sha256(target.read_bytes()).hexdigest(), origin='built-in imagegen; fictional artistic interpretation without a verified likeness reference'))
    if key == 'osyp_tsebriy':
        thumbnail = ImageOps.fit(portrait, (57, 58), Image.Resampling.LANCZOS, centering=(0.5, 0.15))
        card = Image.new('RGBA', (65, 67), (0, 0, 0, 0)); card.paste(thumbnail, (4, 2))
        target = ROOT/'gfx/interface/ideas/nww_portraits/MKN_osyp_tsebriy.dds'
        # Use uncompressed RGBA for exact card bounds and bottom clearance.
        card.save(target)
        assert Image.open(target).convert('RGBA').getchannel('A').getbbox() == (4, 2, 61, 60)
        assets.append(dict(key='osyp_tsebriy_advisor', source=str(source.relative_to(ROOT)),
            texture=str(target.relative_to(ROOT)), size=[65, 67], alpha_bounds=[4, 2, 61, 60],
            export_sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
# A compact review sheet at actual leader/card sizes.
sheet = Image.new('RGB', (156*2+65+40, 235), (65, 60, 53))
for i, key in enumerate(('osyp_tsebriy','communal_council')):
    with Image.open(ROOT/'gfx/leaders/MKN'/(key+'.dds')) as im: sheet.paste(im.convert('RGB'), (10+i*166, 10))
with Image.open(ROOT/'gfx/interface/ideas/nww_portraits/MKN_osyp_tsebriy.dds') as im: sheet.paste(im, (342, 10), im)
sheet.save(ART/'preview.png')
(ART/'assets.json').write_text(json.dumps(assets, ensure_ascii=False, indent=2)+'\n')
print('PASS: two visible leader portraits, separate 65x67 advisor card, alpha bounds (4, 2, 61, 60)')
