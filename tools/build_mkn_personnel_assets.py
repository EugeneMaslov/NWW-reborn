"""Technical exports of approved MKN photographs and the generated advisor bust.

No painting, face editing, background generation or color grading is performed.
The vertical news photograph is fitted whole into a native landscape matte so
that all three faces remain visible. The source photographs stay untouched.
"""
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'docs/art'


def export_fitted(source, target, size, background):
    original = Image.open(ROOT / source).convert('RGBA')
    fitted = ImageOps.contain(original, size, Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', size, background)
    canvas.alpha_composite(fitted, ((size[0] - fitted.width) // 2,
                                  (size[1] - fitted.height) // 2))
    path = ROOT / target
    path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(path, format='DDS')
    return canvas


def main():
    outputs = []
    previews = []
    manifest = ART / 'MKN_personnel_assets.json'
    previous = {entry['target']: entry for entry in json.loads(
        manifest.read_text(encoding='utf-8'))} if manifest.is_file() else {}
    for source, target, size in (
        ('docs/for-gen/photo-eugen-general.jpg', 'gfx/leaders/MKN/eugen.dds', (156, 210)),
        ('docs/for-gen/dmitruk-tratishov-2.jpg', 'gfx/leaders/MKN/dmitruk_tratishov.dds', (156, 210)),
        ('docs/for-gen/man.jpg', 'gfx/event_pictures/MKN/eugen_rescue.dds', (397, 153)),
    ):
        old = previous.get(target, {})
        if not (ROOT / source).is_file():
            if not old.get('provenance') or not (ROOT / old.get('source', '')).is_file():
                raise FileNotFoundError(f'Missing original and recovered source for {target}')
            source = old['source']
        canvas = export_fitted(source, target, size, (37, 39, 36, 255))
        previews.append((Path(target).stem, canvas))
        entry = dict(source=source, target=target, size=size, preserve_full_frame=True)
        if source == old.get('source') and 'provenance' in old:
            for key in ('original_source', 'original_source_sha256', 'provenance'):
                entry[key] = old[key]
            entry['export_sha256'] = hashlib.sha256((ROOT / target).read_bytes()).hexdigest()
        outputs.append(entry)

    source = 'docs/art/MKN_eugen_advisor_painted.png'
    original = Image.open(ROOT / source).convert('RGBA')
    assert original.getchannel('A').getextrema()[0] == 0, 'Advisor must have real transparency'
    portrait = original.crop(original.getchannel('A').getbbox())
    portrait.thumbnail((57, 59), Image.Resampling.LANCZOS)
    card = Image.new('RGBA', (65, 67))
    card.alpha_composite(portrait, ((65 - portrait.width) // 2, 2))
    bounds = card.getchannel('A').getbbox()
    assert bounds and bounds[3] <= 61, bounds
    target = 'gfx/interface/ideas/nww_portraits/MKN_eugen.dds'
    card.save(ROOT / target, format='DDS')
    outputs.append(dict(source=source, target=target, size=[65, 67], alpha_bounds=bounds))
    previews.insert(1, ('Eugen advisor', card))
    for entry in outputs:
        entry['source_sha256'] = hashlib.sha256((ROOT / entry['source']).read_bytes()).hexdigest()
    (ART / 'MKN_personnel_assets.json').write_text(
        json.dumps(outputs, indent=2) + '\n', encoding='utf-8')

    preview = Image.new('RGBA', (1100, 740), (29, 32, 36, 255))
    draw = ImageDraw.Draw(preview)
    for (name, picture), position, scale in zip(
            previews, ((25, 32), (370, 52), (720, 32), (152, 425)), (1.7, 3, 1.7, 2)):
        shown = picture.resize((round(picture.width * scale), round(picture.height * scale)),
                               Image.Resampling.NEAREST)
        preview.alpha_composite(shown, position)
        draw.text((position[0], position[1] - 20), name, fill='white')
    preview.save(ROOT / 'docs/mkn_personnel_preview.png')
    print('Built two portraits with original backgrounds, a 65x67 advisor card '
          f'(alpha {bounds}), and the complete news photograph at 397x153.')


if __name__ == '__main__':
    main()
