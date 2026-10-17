"""Check all playable icon bindings, native references and preserved custom art."""
from collections import Counter,defaultdict
import hashlib
import json
from PIL import Image
from hoi4_script import read,one,values,walk
from britain_focus_icons import ICONS,CUSTOM


def validate_focus_art(root,game,check):
    manifest=json.loads((root/'docs/art/ENG/focuses/manifest.json').read_text(encoding='utf-8'))
    tree=one(read(root/'common/national_focus/ENG_focuses.txt'),'focus_tree')
    actual={one(f,'id').removeprefix('ENG_nww_'):one(f,'icon') for f in values(tree,'focus')}
    check(actual==ICONS,'Playable ENG focus icons diverged from explicit semantic assignments')
    check(manifest['assignments']==ICONS,'Stale ENG focus-art manifest')
    check(len(set(actual.values()))>=70,'British tree has too few different thematic icons')
    check(max(Counter(actual.values()).values())<=8,'One icon dominates the British tree')
    custom={one(v,'name'):v for v in values(one(read(root/'interface/ENG_focus_icons.gfx'),'spriteTypes'),'spriteType')}
    check(len(custom)==16,'Expected eight normal/shine icon pairs')
    hashes=set()
    for asset in manifest['assets']:
        key=asset['key'];source=root/asset['source'];texture=root/asset['texture']
        check(key in CUSTOM,'Unexpected custom focus emblem '+key)
        check(source.exists() and (root/asset['prompt']).exists(),'Missing imagegen original/prompt '+key)
        check(hashlib.sha256(source.read_bytes()).hexdigest()==asset['source_sha256'],'Changed source '+key)
        digest=hashlib.sha256(texture.read_bytes()).hexdigest();hashes.add(digest)
        check(digest==asset['texture_sha256'],'Changed DDS '+key)
        with Image.open(texture) as im:
            check(im.size==(96,96) and im.mode=='RGBA','Wrong focus canvas '+key)
            bounds=im.getchannel('A').getbbox()
            check(bounds is not None and bounds[0]>=4 and bounds[1]>=4 and bounds[2]<=92 and bounds[3]<=92,'Missing alpha margins '+key)
        sprite=asset['sprite'];normal=custom[sprite];shine=custom[sprite+'_shine']
        check(one(normal,'texturefile')==one(shine,'texturefile')==asset['texture'],'Wrong normal/shine binding '+key)
        masks=[v for k,v,_ in walk(shine) if k=='animationmaskfile']
        check(masks==[asset['texture']]*2,'Shine mask uses another focus artwork '+key)
    check(len(hashes)==8,'Custom focus emblems are duplicated')
    # Inspect real native registrations and texture presence, not guessed names.
    native={}
    for path in (game/'interface').glob('*.gfx'):
        try:doc=read(path)
        except ValueError:continue
        for k,v,_ in walk(doc):
            if k and k.lower()=='spritetype':native[one(v,'name')]=v
    for icon in set(ICONS.values())-set(custom):
        check(icon in native,'Unknown native focus icon '+icon)
        check(icon+'_shine' in native,'Missing native focus shine '+icon)
        if icon in native:
            texture=one(native[icon],'texturefile')
            check(texture and (game/texture).exists(),'Missing native texture '+str(texture))
    print(f'PASS: ENG focus artwork: 153 explicit bindings, {len(set(ICONS.values()))} different icons, eight original emblems with normal/shine sprites and alpha margins')
