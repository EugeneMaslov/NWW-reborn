"""Install generated Ottoman art without changing gameplay or shared vanilla sprites."""
import argparse, copy, hashlib, json, math, re, shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from hoi4_script import read, one, values, parse, dump, TOKEN

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'docs/art/TUR'
FILES = {
    'focus': 'common/national_focus/TUR_focuses.txt',
    'idea': 'common/ideas/TUR_ideas.txt',
    'decision': 'common/decisions/TUR_decisions.txt',
    'category': 'common/decisions/categories/TUR_categories.txt',
    'company_idea': 'common/ideas/turkey.txt',
    'company_mio': 'common/military_industrial_organization/organizations/TUR_organization.txt',
}

def mechanics(node):
    return [(k, mechanics(v) if isinstance(v, list) else v, o)
            for k, v, o in node if k not in ('icon', 'picture')]

def digest(path):
    return hashlib.sha256(json.dumps(mechanics(read(path)), ensure_ascii=False).encode()).hexdigest()

def replace_fields(text, mapping, kind):
    """Replace direct icon fields in named blocks; preserve comments and formatting."""
    tokens = [m for m in TOKEN.finditer(text) if not m.group().isspace() and not m.group().startswith('#')]
    replacements = []
    def block(start, end):
        i = start
        direct = []
        while i < end:
            if i + 2 < end and tokens[i+1].group() == '=':
                key, val = tokens[i].group().strip('"'), tokens[i+2].group()
                if val == '{':
                    depth, j = 1, i+3
                    while depth:
                        depth += (tokens[j].group() == '{') - (tokens[j].group() == '}')
                        j += 1
                    children = block(i+3, j-1)
                    owner = next((v for k,v,t in children if k == 'id'), None) if kind == 'focus' else key
                    if owner in mapping:
                        field = 'picture' if kind in ('idea','company_idea') else 'icon'
                        matches = [(v,t) for k,v,t in children if k == field]
                        if len(matches) != 1: raise ValueError(f'{owner}: expected one {field}')
                        old, token = matches[0]
                        replacements.append((token.start(), token.end(), mapping[owner]))
                    i = j
                else:
                    direct.append((key,val.strip('"'),tokens[i+2])); i += 3
            else: i += 1
        return direct
    block(0,len(tokens))
    if len(replacements) != len(mapping): raise ValueError(f'{kind}: replaced {len(replacements)} of {len(mapping)}')
    for a,b,value in sorted(replacements,reverse=True): text = text[:a]+value+text[b:]
    return text

def setv(node,key,value):
    node[:] = [(k,v,o) for k,v,o in node if k != key]
    node.append((key,value,'='))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game',default='D:/Steam/steamapps/common/Hearts of Iron IV')
    parser.add_argument('--preview-only',action='store_true')
    args = parser.parse_args()
    manifest = json.loads((ART/'manifest.json').read_text(encoding='utf-8'))
    records = {j['key']:j for j in json.loads((ART/'generation_jobs.json').read_text(encoding='utf-8'))['jobs']}
    for p in (ART/'jobs').glob('*.json'):
        j=json.loads(p.read_text(encoding='utf-8')); records[j['key']]=j
    jobs=manifest['jobs']
    if not args.preview_only and len(records) != len(jobs):
        raise ValueError(f'Generation incomplete: {len(records)}/{len(jobs)}')
    paths={kind:ROOT/path if (ROOT/path).exists() else Path(args.game)/path for kind,path in FILES.items()}
    baseline = {kind:digest(path) for kind,path in paths.items()}
    baseline_path=ART/'mechanics_baseline.json'
    if not baseline_path.exists(): baseline_path.write_text(json.dumps(baseline,indent=2)+'\n',encoding='utf-8',newline='\n')
    else:
        prior=json.loads(baseline_path.read_text())
        assert all(baseline[k]==v for k,v in prior.items()), 'Gameplay changed since art baseline'
        baseline_path.write_text(json.dumps(baseline,indent=2)+'\n',encoding='utf-8',newline='\n')
    template = next(n for k,n,o in one(read(Path(args.game)/'interface/goals_shine.gfx'),'spriteTypes')
                    if one(n,'name') == 'GFX_focus_generic_diplomatic_treaty_shine')
    sprites=[]; installed=[]; maps={kind:{} for kind in FILES}; canvases={kind:[] for kind in ('focus','idea','decision','category','company')}
    for j in jobs:
        if j['key'] not in records: continue
        job=records[j['key']]; key=j['key']; kind=j['kind']
        source=ART/'generated'/f'{key}.png'; source.parent.mkdir(exist_ok=True)
        if not source.exists(): shutil.copyfile(job['generated_path'],source)
        source.with_suffix('.prompt.txt').write_text(job['prompt']+'\n',encoding='utf-8',newline='\n')
        im=Image.open(source).convert('RGBA'); alpha=im.getchannel('A')
        bounds=alpha.point(lambda a:255 if a>8 else 0).getbbox()
        if not bounds or alpha.getextrema()[0] != 0: raise ValueError(key+': missing transparent background')
        size,occupied=(95,83) if kind=='focus' else (64,58)
        im=im.crop(bounds); im.thumbnail((occupied,occupied),Image.Resampling.LANCZOS)
        canvas=Image.new('RGBA',(size,size)); canvas.alpha_composite(im,((size-im.width)//2,(size-im.height)//2))
        folder={'focus':'goals','idea':'ideas','decision':'decisions','category':'decisions','company':'ideas'}[kind]
        texture=f'gfx/interface/{folder}/TUR/{key}.dds'
        sprite=f'GFX_{"idea" if kind in ("idea","company") else "focus" if kind=="focus" else "decision"}_NWW_TUR_generated_{key}'
        sprites.extend(parse(f'spriteType = {{ name = {sprite} texturefile = "{texture}" }}'))
        if kind=='focus':
            shine=copy.deepcopy(template); setv(shine,'name',sprite+'_shine'); setv(shine,'texturefile',texture)
            for anim in values(shine,'animation'): setv(anim,'animationmaskfile',texture)
            sprites.append(('spriteType',shine,'='))
        for consumer in j['consumers']:
            target_kind,consumer=consumer.split(':',1) if kind=='company' else (kind,consumer)
            maps[target_kind][consumer]=sprite.removeprefix('GFX_idea_') if target_kind in ('idea','company_idea') else sprite
        if not args.preview_only:
            target=ROOT/texture; target.parent.mkdir(parents=True,exist_ok=True); canvas.save(target,format='DDS')
        installed.append({**j,'generated_sprite':sprite,'texture':texture,'saved_source':source.relative_to(ROOT).as_posix(),
                          'canvas':[size,size],'alpha_bounds':canvas.getchannel('A').getbbox()})
        canvases[kind].append((j,canvas))
    font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',12)
    for kind,items in canvases.items():
        if not items: continue
        columns=7 if kind=='focus' else 6
        sheet=Image.new('RGBA',(columns*160,math.ceil(len(items)/columns)*160),(27,31,38,255)); draw=ImageDraw.Draw(sheet)
        for i,(j,canvas) in enumerate(items):
            x,y=i%columns*160,i//columns*160
            sheet.alpha_composite(canvas,(x+(160-canvas.width)//2,y+8))
            label=j['names'][0]
            draw.text((x+5,y+110),label[:24],font=font,fill='white')
            draw.text((x+5,y+126),label[24:48],font=font,fill='white')
        sheet.save(ART/f'{kind}_generated_preview.png')
    if not args.preview_only:
        for kind,path in FILES.items():
            p=ROOT/path; p.parent.mkdir(parents=True,exist_ok=True)
            text=paths[kind].read_text(encoding='utf-8-sig')
            if paths[kind]!=p: text='# NWW TUR artwork override: native gameplay preserved; see docs/TUR_generated_icons.md.\n'+text
            p.write_text(replace_fields(text,maps[kind],kind),encoding='utf-8',newline='\n')
            assert digest(p)==baseline[kind], path+': gameplay unexpectedly changed'
        (ROOT/'interface/TUR_generated_icons.gfx').write_text(dump([('spriteTypes',sprites,'=')])+'\n',encoding='utf-8',newline='\n')
        (ART/'installation.json').write_text(json.dumps({'jobs':installed},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f'{"Previewed" if args.preview_only else "Installed"} {len(installed)}/{len(jobs)} Ottoman icons.')

if __name__=='__main__': main()
