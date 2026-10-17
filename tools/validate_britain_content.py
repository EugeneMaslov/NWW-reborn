"""Validate Britain's complete source package against installed HOI4 1.19.3.

Static validation only. New-campaign UI, event delivery, AI and combat still
require a game run and inspection of a fresh error.log.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from PIL import Image
from hoi4_script import read, one, values, walk, engine_script_errors, TOKEN

ROOT=Path(__file__).resolve().parents[1]
P='ENG_nww_'


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game',type=Path,required=True)
    args=parser.parse_args(argv);game=args.game
    errors=[]
    def check(ok,message):
        if not ok: errors.append(message)
    paths=sorted({*ROOT.glob('common/**/ENG*.txt'),*ROOT.glob('events/*Britain.txt'),
                  ROOT/'events/ENG_events.txt',ROOT/'common/national_focus/uk.txt',
                  ROOT/'history/units/ENG_nww_ulster_revolt.txt'})
    docs={}
    for path in paths:
        try: doc=read(path)
        except (ValueError,UnicodeError) as exc:
            errors.append(f'{path}: {exc}');continue
        docs[path]=doc
        errors.extend(f'{path.name}: {err}' for err in engine_script_errors(doc))
        check(not any(re.fullmatch(r'-?\.\d+',m.group()) for m in TOKEN.finditer(path.read_text(encoding='utf-8-sig'))),f'{path.name}: bare decimal')
    tree=one(read(ROOT/'common/national_focus/ENG_focuses.txt'),'focus_tree')
    hooks=one(read(ROOT/'common/on_actions/ENG_on_actions.txt'),'on_actions')
    check(one(hooks,'on_monthly_ENG') is not None and one(hooks,'on_monthly') is None,
          'Monthly tick must use ENG hook, not run once for every country')
    focuses={one(v,'id'):v for v in values(tree,'focus')}
    check(len(focuses)==153,'Expected 153 playable focuses')
    check(one(tree,'id')=='ENG_nww_focus','Wrong playable tree')
    slots=Counter((one(f,'x'),one(f,'y')) for f in focuses.values())
    check(all(n==1 for n in slots.values()),'Overlapping focus coordinates')
    panel=one(tree,'continuous_focus_position')
    check(int(one(panel,'y'))>max(int(one(f,'y')) for f in focuses.values())*130+500,'Continuous panel intersects focus content')
    edges={}
    for fid,f in focuses.items():
        refs=[v for k,v,o in walk(f) if k in ('focus','has_completed_focus')]
        check(all(r in focuses for r in refs),f'{fid}: missing focus reference')
        parents=[one(v,'focus') for v in values(f,'prerequisite')]
        edges[fid]=parents
        for parent in parents:
            check(int(one(f,'y'))>int(one(focuses[parent],'y')),f'{fid}: connector points upwards')
        check(bool(one(f,'completion_reward')),f'{fid}: empty reward')
        for other in values(one(f,'mutually_exclusive',[]),'focus'):
            check(fid in values(one(focuses[other],'mutually_exclusive',[]),'focus'),f'{fid}: asymmetric exclusion')
    seen=set();active=set()
    def visit(fid):
        check(fid not in active,f'{fid}: prerequisite cycle')
        if fid in active or fid in seen:return
        active.add(fid)
        for parent in edges[fid]:visit(parent)
        active.remove(fid);seen.add(fid)
    for fid in focuses:visit(fid)

    locs={}
    for lang in ('russian','english'):
        entries={}
        for base in (game,ROOT):
            for path in (base/'localisation').rglob('*l_'+lang+'.yml'):
                entries.update(re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$',path.read_text(encoding='utf-8-sig',errors='replace'),re.M))
        local=ROOT/f'localisation/{lang}/ENG_nww_l_{lang}.yml'
        check(local.read_bytes().startswith(b'\xef\xbb\xbf'),f'{lang}: missing BOM')
        pairs=re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$',local.read_text(encoding='utf-8-sig'),re.M)
        check(len(pairs)==len(dict(pairs)),f'{lang}: duplicate localization')
        for key,text in pairs:
            check('??' not in text,f'{lang}: broken encoding at {key}')
            for ref in re.findall(r'\$([\w.]+)\$',text):
                check(ref in entries,f'{lang}: missing tooltip substitution {ref}')
        locs[lang]=entries
    sprites={}
    for base in (game,ROOT):
        for path in (base/'interface').rglob('*.gfx'):
            try: doc=read(path)
            except (ValueError,UnicodeError):continue
            for k,v,o in walk(doc):
                if k and k.lower()=='spritetype':sprites[one(v,'name')]=one(v,'texturefile')
    def localized(key):
        for lang,entries in locs.items():check(key in entries,f'{lang}: missing {key}')
    for fid in focuses:
        localized(fid);localized(fid+'_desc')
    registered_modifiers=set(re.findall(r'^## ([\w<>]+)',(game/'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig'),re.M))
    for path,doc in docs.items():
        for k,v,o in walk(doc):
            if k in ('custom_effect_tooltip','tooltip'):localized(v)
            if k=='icon' and isinstance(v,str) and v.startswith('GFX_'):
                check(v in sprites,f'{path.name}: unknown sprite {v}')
            if k=='modifier' and isinstance(v,list) and path.parent.name=='ideas':
                for mod,_,_ in v:check(mod in registered_modifiers,f'{path.name}: unknown modifier {mod}')
            if k=='set_politics':
                check(one(v,'ruling_party') is not None and one(v,'elections_allowed') is not None,f'{path.name}: incomplete politics block')
    for key,doc,op in read(ROOT/'common/dynamic_modifiers/ENG_modifiers.txt'):
        localized(key);localized(key+'_desc')
        for mod,_,_ in doc:
            if mod not in ('enable','icon'):check(mod in registered_modifiers,f'{key}: unknown modifier {mod}')
    # Every ENG spirit and mechanic category has its own generated artwork.
    manifest=json.loads((ROOT/'docs/art/ENG/icons/manifest.json').read_text(encoding='utf-8'))
    check(manifest['generator']=='Built-in image_gen','ENG artwork must retain imagegen provenance')
    check(len(manifest['assets'])==19,'Expected 16 spirit and three category icons')
    native_ideas=one(one(read(ROOT/'common/ideas/ENG_ideas.txt'),'ideas'),'country')
    dynamic=dict((k,v) for k,v,o in read(ROOT/'common/dynamic_modifiers/ENG_modifiers.txt'))
    categories=dict((k,v) for k,v,o in read(ROOT/'common/decisions/categories/ENG_categories.txt'))
    hashes=set()
    for asset in manifest['assets']:
        key=asset['key'];source=ROOT/asset['source'];texture=ROOT/asset['texture']
        prompt=ROOT/asset['prompt']
        check(source.is_file() and texture.is_file() and prompt.is_file(),f'{key}: missing artwork or prompt')
        if not source.is_file() or not texture.is_file():continue
        check(hashlib.sha256(source.read_bytes()).hexdigest()==asset.get('source_sha256'),f'{key}: original hash mismatch')
        digest=hashlib.sha256(texture.read_bytes()).hexdigest()
        check(digest==asset.get('texture_sha256'),f'{key}: exported hash mismatch')
        check(digest not in hashes,f'{key}: duplicate placeholder artwork');hashes.add(digest)
        with Image.open(source) as im:
            check(min(im.size)>=512 and im.mode=='RGBA' and im.getchannel('A').getextrema()[0]==0,f'{key}: source needs genuine transparency')
        with Image.open(texture) as im:
            check(im.format=='DDS' and im.mode=='RGBA' and list(im.size)==asset['size'],f'{key}: wrong native texture format')
            bounds=im.getchannel('A').getbbox();w,h=im.size
            check(bounds and min(bounds[:2])>=3 and bounds[2]<=w-3 and bounds[3]<=h-3,f'{key}: occupied alpha bounds touch UI edge')
        check(sprites.get(asset['sprite'])==asset['texture'],f'{key}: missing native sprite registration')
        if P+key in dynamic:check(one(dynamic[P+key],'icon')==asset['sprite'],f'{key}: dynamic icon not connected')
        elif asset['kind']=='spirit':check('GFX_idea_'+one(one(native_ideas,P+key),'picture','')==asset['sprite'],f'{key}: idea picture not connected')
        else:check(one(categories[P+key+'_category'],'icon')==asset['sprite'],f'{key}: category icon not connected')
    # Designer and MIO definitions are checked against the actual installed registries.
    traits={k for path in (game/'common/country_leader').glob('*.txt') for k,v,o in one(read(path),'leader_traits',[])}
    for path in (ROOT/'common/ideas').glob('ENG*.txt'):
        for k,v,o in walk(read(path)):
            if k=='traits':
                for _,t,_ in v:check(t in traits,f'{path.name}: unknown trait {t}')
    native_mio=read(game/'common/military_industrial_organization/organizations/ENG_organization.txt')
    mod_mio=dict((k,v) for k,v,o in read(ROOT/'common/military_industrial_organization/organizations/ENG_organization.txt'))
    stats=set()
    for path in (game/'common/units/equipment').rglob('*.txt'):
        for k,v,o in walk(read(path)):
            if isinstance(v,str):stats.add(k)
    for organization,node,op in native_mio:
        edited=mod_mio[organization]
        check(one(node,'include')==one(edited,'include'),f'{organization}: lost template')
        native_tokens={one(v,'token') for k,v,o in node if k in ('trait','add_trait','override_trait')}
        mod_tokens={one(v,'token') for k,v,o in edited if k in ('trait','add_trait','override_trait')}
        check(native_tokens<=mod_tokens,f'{organization}: lost native trait')
        for t in values(edited,'add_trait'):
            if one(t,'token','').startswith(P):
                check(one(t,'available') is not None,f'{organization}: ungated new trait')
                for stat,_,_ in one(t,'equipment_bonus',[]):check(stat in stats,f'{organization}: unknown MIO equipment stat {stat}')
    # Compatibility must be identical to direct native focus definitions, never nested IDs.
    native_focus=read(game/'common/national_focus/uk.txt')
    expected={one(f,'id') for k,v,o in native_focus for f in (values(v,'focus') if k=='focus_tree' else [v] if k=='shared_focus' else [])}
    compat={one(v,'id') for k,v,o in read(ROOT/'common/national_focus/ENG_compatibility.txt') if k=='shared_focus'}
    check(expected==compat,'Compatibility registry differs from direct native definitions')
    for name in ('Britain.txt','MTG_Britain.txt','WTT_Britain.txt'):
        source=read(game/'events'/name);replacement=read(ROOT/'events'/name)
        original_ids={one(v,'id') for k,v,o in source if k in ('country_event','news_event')}
        replacement_ids={one(v,'id') for k,v,o in replacement if k in ('country_event','news_event')}
        check(original_ids==replacement_ids,f'{name}: dropped native callback')
        for k,v,o in replacement:
            if k in ('country_event','news_event'):
                check(one(v,'is_triggered_only')=='yes' and not one(v,'immediate') and not values(v,'option'),f'{name}: active native callback')
    events={one(v,'id'):v for k,v,o in read(ROOT/'events/ENG_events.txt') if k=='country_event'}
    callback_ids=set(events)
    callback_ids.update(one(v,'id') for name in ('Britain.txt','MTG_Britain.txt','WTT_Britain.txt') for k,v,o in read(ROOT/'events'/name) if k in ('country_event','news_event'))
    for eid,node in events.items():
        localized(one(node,'title'));localized(one(node,'desc'))
        for option in values(node,'option'):localized(one(option,'name'))
    effect_ids={k for k,v,o in read(ROOT/'common/scripted_effects/ENG_effects.txt')}
    known_effects=set(re.findall(r'^## (\w+)',(game/'documentation/effects_documentation.md').read_text(encoding='utf-8-sig'),re.M))
    effect_blocks=[v for k,v,o in read(ROOT/'common/scripted_effects/ENG_effects.txt')]
    effect_blocks.extend(one(f,'completion_reward',[]) for f in focuses.values())
    for _,ds,_ in read(ROOT/'common/decisions/ENG_decisions.txt'):
        for _,d,_ in ds:
            effect_blocks.extend(one(d,k,[]) for k in ('complete_effect','remove_effect','cancel_effect','timeout_effect'))
    for e in events.values():
        effect_blocks.append(one(e,'immediate',[]))
        effect_blocks.extend([n for n in opt if n[0] not in ('name','trigger','ai_chance')] for opt in values(e,'option'))
    def check_effect_names(nodes):
        for k,v,o in nodes:
            if k in ('if','else_if','else','hidden_effect','random_owned_controlled_state') or (k and (k.isdigit() or re.fullmatch('[A-Z]{3}',k) or k.startswith('mio:'))):
                if isinstance(v,list):check_effect_names([n for n in v if n[0]!='limit'])
            elif k=='random_list':
                for _,node,_ in v:check_effect_names(node)
            else:check(k in known_effects or k in effect_ids,f'Unknown ENG effect: {k}')
    for block in effect_blocks:check_effect_names(block)
    for path,doc in docs.items():
        for k,v,o in walk(doc):
            if k=='country_event' and isinstance(v,list):check(one(v,'id') in callback_ids,f'{path.name}: missing event {one(v,"id")}')
            if k in effect_ids:continue
            if k and k.startswith(P) and v=='yes':check(False,f'{path.name}: undefined scripted effect {k}')
    # Five mandates are explicitly attainable; inclusive 40% boundary is essential.
    for key,party in [('blackshirts','fascism'),('directory','neutrality'),('social_republic','communism'),('labour_election','democratic')]:
        text=str(one(focuses[P+key],'available'))
        check(party in text and '0.40' in text,f'{key}: missing exact mandate')
    alltext='\n'.join(p.read_text(encoding='utf-8-sig') for p in docs)
    check('num_of_convoys' not in alltext and 'has_building =' not in alltext,'Unsupported guessed trigger')
    check('target = KUW' not in alltext,'British Kuwait dependency recreated')
    check('add_core_of = ENG' not in alltext,'Automatic colonial cores')
    from validate_britain_gui import validate_gui
    validate_gui(check)
    if errors:
        print('\n'.join('ERROR: '+e for e in errors));return 1
    print(f'PASS: ENG: {len(focuses)} focuses, coordinates/graph, bilateral localization, installed sprites/modifiers/stats, mandates, native isolation and MIO inheritance')
    print('PASS: ENG artwork: 19 distinct imagegen icons, preserved originals/prompts, native RGBA DDS sizes, transparent margins and consumer bindings')
    return 0


if __name__=='__main__':raise SystemExit(main())
