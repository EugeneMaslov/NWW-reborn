"""Build native 65x67 advisor DDS assets; keep large leader portraits intact."""
from pathlib import Path
from PIL import Image
from hoi4_script import read, one, walk, dump

ROOT = Path(__file__).resolve().parents[1]
GAME = Path('D:/Steam/steamapps/common/Hearts of Iron IV')
SIZE = (65, 67)
VISIBLE_SIZE = (57, 59)

for relative in ('interface/ltb_portraits.gfx', 'interface/nww_mkn_portraits.gfx'):
    path = ROOT / relative
    doc = read(path)
    for key, sprite, op in walk(doc):
        if not key or key.lower() != 'spritetype':
            continue
        token = one(sprite, 'name', '')
        if not token.startswith('GFX_idea_'):
            continue
        # Always build from the large sprite, never a previous thumbnail.
        large_token = token.replace('GFX_idea_', 'GFX_Portrait_', 1)
        large_sprite = next((v for k, v, o in walk(doc) if k and k.lower() == 'spritetype' and one(v, 'name') == large_token), None)
        source = one(large_sprite or sprite, 'texturefile')
        src = ROOT / source
        if not src.is_file():
            src = GAME / source
        image = Image.open(src).convert('RGBA')
        # Crop the lower torso, then leave the slot's bottom edge unobstructed.
        image = image.crop((0, 0, image.width, round(image.height * 0.90)))
        image.thumbnail(VISIBLE_SIZE, Image.Resampling.LANCZOS)
        canvas = Image.new('RGBA', SIZE)
        canvas.alpha_composite(image, ((SIZE[0]-image.width)//2, 2))
        relative_asset = 'gfx/interface/ideas/nww_portraits/' + token[9:] + '.dds'
        target = ROOT / relative_asset
        target.parent.mkdir(parents=True, exist_ok=True)
        canvas.save(target, format='DDS')
        sprite[:] = [(k, relative_asset if k == 'texturefile' else v, o) for k, v, o in sprite]
        print(target.relative_to(ROOT))
    path.write_text(dump(doc) + '\n', encoding='utf-8')
