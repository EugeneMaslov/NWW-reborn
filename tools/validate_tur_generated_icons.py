"""Check Ottoman artwork coverage, game texture wiring and unchanged gameplay."""
import json
from pathlib import Path
from PIL import Image
from hoi4_script import read, one, values, walk
from build_tur_generated_icons import ROOT, ART, FILES, digest

def main():
    source=json.loads((ART/'manifest.json').read_text(encoding='utf-8'))['jobs']
    jobs=json.loads((ART/'installation.json').read_text(encoding='utf-8'))['jobs']
    assert {j['key'] for j in source} == {j['key'] for j in jobs}, 'Incomplete artwork coverage'
    sprites={one(n,'name'):n for k,n,o in one(read(ROOT/'interface/TUR_generated_icons.gfx'),'spriteTypes')}
    definitions={}
    for kind,path in FILES.items():
        doc=read(ROOT/path)
        if kind=='focus': nodes=[(one(n,'id'),n) for n in values(one(doc,'focus_tree'),'focus')]
        elif kind in ('idea','company_idea'):
            nodes=[(k,n) for category,body,o in one(doc,'ideas') for k,n,o in body if isinstance(n,list)
                   and (kind=='idea' or category not in ('country','hidden_ideas')) and one(n,'picture')]
        elif kind=='decision': nodes=[(k,n) for category,body,o in doc for k,n,o in body if isinstance(n,list) and one(n,'icon')]
        else: nodes=[(k,n) for k,n,o in doc if isinstance(n,list) and one(n,'icon')]
        definitions[kind]=dict(nodes)
    baseline=json.loads((ART/'mechanics_baseline.json').read_text())
    for kind,path in FILES.items(): assert digest(ROOT/path)==baseline[kind], path+': gameplay changed'
    for job in jobs:
        key=job['key']; kind=job['kind']; sprite=job['generated_sprite']; texture=job['texture']
        assert one(sprites[sprite],'texturefile')==texture, key+': wrong sprite texture'
        im=Image.open(ROOT/texture).convert('RGBA'); alpha=im.getchannel('A')
        assert list(im.size)==job['canvas'] and alpha.getextrema()[0]==0, key+': invalid canvas/alpha'
        bounds=alpha.point(lambda a:255 if a>8 else 0).getbbox()
        assert bounds and min(bounds[:2])>=4 and bounds[2]<=im.width-4 and bounds[3]<=im.height-4, key+': art clipped'
        original=ROOT/job['saved_source']
        assert original.exists() and original.with_suffix('.prompt.txt').stat().st_size>100, key+': missing source/prompt'
        for consumer in job['consumers']:
            target_kind,consumer=consumer.split(':',1) if kind=='company' else (kind,consumer)
            expected=sprite.removeprefix('GFX_idea_') if target_kind in ('idea','company_idea') else sprite
            assert one(definitions[target_kind][consumer],'picture' if target_kind in ('idea','company_idea') else 'icon')==expected, consumer+': wrong icon'
        if kind=='focus':
            shine=sprites[sprite+'_shine']
            assert one(shine,'texturefile')==texture
            assert one(shine,'effectFile')=='gfx/FX/buttonstate.lua'
            assert len(values(shine,'animation'))==2
            assert all(one(a,'animationmaskfile')==texture for a in values(shine,'animation'))
    for kind,nodes in definitions.items():
        mapped={c for j in jobs if j['kind']==kind for c in j['consumers']}
        mapped|={c.split(':',1)[1] for j in jobs if j['kind']=='company' for c in j['consumers'] if c.startswith(kind+':')}
        assert mapped==nodes.keys(), kind+': unmapped active definitions'
    print(f'PASS: {len(jobs)} original drawings; '+', '.join(f'{len(v)} {k} consumers' for k,v in definitions.items())+'; focus highlights, alpha, sources, prompts and gameplay preservation.')

if __name__=='__main__': main()
