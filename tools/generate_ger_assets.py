"""Register native German UI artwork; never draw or generate raster icons.

The historical filename is retained for existing workflows. Existing custom
GFX tokens become compatibility aliases pointing at actual installed textures.
"""
import argparse
import json
from pathlib import Path
from hoi4_script import read,one,walk,dump

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game',type=Path,default=Path.home()/'.local/share/Steam/steamapps/common/Hearts of Iron IV')
    game=parser.parse_args().game
    mapping=json.loads((ROOT/'docs/GER_native_icons.json').read_text())
    sprites={};sources={}
    for base in (game,*sorted(game.glob('dlc/*'))):
        for path in (base/'interface').rglob('*.gfx'):
            try:doc=read(path)
            except (ValueError,UnicodeError):continue
            for k,v,o in walk(doc):
                if k and k.lower()=='spritetype':
                    sprites[one(v,'name')]=v;sources[one(v,'name')]=path.relative_to(game).as_posix()
    aliases=[];manifest=[]
    for focus,native in mapping.items():
        assert native in sprites and native+'_shine' in sprites,native
        texture=one(sprites[native],'texturefile')
        assert any((base/texture).is_file() for base in (game,*game.glob('dlc/*'))),texture
        for suffix in ('','_shine'):
            old='GFX_focus_'+focus+suffix
            if old in sprites:continue  # Never override an actual native sprite.
            aliases.append(('spriteType',[(k,old if k=='name' else v,o) for k,v,o in sprites[native+suffix]],'='))
        manifest.append(dict(focus=focus,native=native,texture=texture,definition=sources[native]))
    (ROOT/'interface/GER_goals.gfx').write_text('# Native texture compatibility aliases; no generated artwork.\n'+dump([('spriteTypes',aliases,'=')])+'\n')
    (ROOT/'docs/GER_native_icon_sources.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(f'PASS: {len(mapping)} political icons use installed German artwork; no raster generation')

if __name__=='__main__':main()
