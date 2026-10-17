"""Audit native palettes, live starting spirits and selection-menu snapshots."""
import json
import re
from pathlib import Path
from hoi4_script import read, one, values, walk, engine_script_errors

ROOT=Path(__file__).resolve().parents[1]


def validate_presentation(root,game,check):
    native={k:v for k,v,_ in read(game/'common/countries/cosmetic.txt')}
    actual={k:v for k,v,_ in read(root/'common/countries/cosmetic.txt')}
    for key in native:check(actual.get(key)==native[key],'Native cosmetic colour missing/changed: '+key)
    check('SOV_rsfsr' in actual,'Custom Soviet palette discarded')
    profiles=json.loads((root/'docs/1936_start_profiles.json').read_text(encoding='utf-8'))
    bookmark=one(one(read(root/'common/bookmarks/nww_1936.txt'),'bookmarks'),'bookmark')
    ideas={};foci={};locs={}
    for base in [game,root]:
        for path in (base/'common/ideas').glob('*.txt'):
            try:doc=read(path)
            except ValueError:
                if base==game:continue
                raise
            for slot,entries,_ in one(doc,'ideas',[]):
                if isinstance(entries,list):ideas.update({k:v for k,v,_ in entries if isinstance(v,list)})
        for path in (base/'common/national_focus').glob('*.txt'):
            try:doc=read(path)
            except ValueError:
                if base==game:continue
                raise
            for k,v,_ in doc:
                if k=='focus_tree':foci.update({one(f,'id'):f for f in values(v,'focus')})
                elif k=='shared_focus':foci[one(v,'id')]=v
    for lang in ['russian','english']:
        keys=set()
        for base in [game,root]:
            for path in (base/'localisation').rglob('*l_'+lang+'.yml'):
                keys.update(re.findall(r'^\s+(\S+):\d* ',path.read_text(encoding='utf-8-sig',errors='replace'),re.M))
        locs[lang]=keys
    for tag,(spirit_ids,focus_ids,ideology) in profiles.items():
        entry=one(bookmark,tag)
        check(len(spirit_ids)<=3,tag+': bookmark exceeds three native idea slots')
        check([v for _,v,_ in one(entry,'ideas')]==spirit_ids,tag+': stale bookmark spirits')
        check([v for _,v,_ in one(entry,'focuses')]==focus_ids,tag+': stale bookmark focuses')
        check(one(entry,'ideology')==ideology,tag+': stale selection ideology')
        check(bool(focus_ids),tag+': no representative focuses')
        for fid in focus_ids:check(fid in foci and not values(foci[fid],'allow_branch'),tag+': hidden/unknown preview focus '+fid)
        for spirit in spirit_ids:
            check(spirit in ideas,tag+': undefined preview idea '+spirit)
            for lang,keys in locs.items():check(spirit in keys,lang+': missing preview name '+spirit)
    for tag,effect in [('ENG','ENG_nww_initialize'),('FRA','FRA_initialize'),('GER','nww_GER_initialize_politics'),('SOV','nww_SOV_update_reconstruction'),('AUS','AUS_nww_initialize')]:
        path=next((root/'history/countries').glob(tag+' - *.txt'))
        check(one(read(path),effect)=='yes',tag+': institutions initialized only after scenario startup')
    # Compare six immutable snapshots with actual zero-focus persistent modifiers.
    from test_britain_lifecycle import World,EFFECTS
    world=World();world.apply(EFFECTS['ENG_nww_rebuild_spirits']);country=world.country('ENG')
    for suffix in ['state','economy','army','air','navy','science']:
        snapshot=one(ideas['ENG_nww_preview_'+suffix],'modifier')
        check(all(float(v)==country.vars['ENG_nww_'+suffix+'_'+k] for k,v,_ in snapshot),suffix+': preview/live modifier mismatch')
    from build_london_treaty import MEMBERS,IDEAS
    for tag in MEMBERS:
        path=next((root/'history/countries').glob(tag+' - *.txt'))
        doc=read(path)
        top={v for v in values(doc,'add_ideas') if isinstance(v,str)}
        check((IDEAS[0] in top)==(tag in MEMBERS),tag+': incorrect scenario treaty membership')
        for key,value,_ in walk(doc):
            if key in ['set_global_flag','modify_global_flag']:
                flag=one(value,'flag') if isinstance(value,list) else value
                check(flag not in ['MTG_naval_treaty_signatories','MTG_second_london_conference'],tag+': stale native treaty counter')
    for path in [*root.glob('common/**/ENG_naval_treaty*.txt'),root/'events/ENG_naval_treaty_events.txt']:
        for error in engine_script_errors(read(path)):check(False,path.name+': '+error)
    print('PASS: 1936 presentation: full vanilla cosmetic palette, nine current country profiles, six live ENG snapshots, history initialization and seven treaty signatories')


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--game',type=Path,required=True);a=p.parse_args();errors=[]
    validate_presentation(ROOT,a.game,lambda ok,msg: errors.append(msg) if not ok else None)
    if errors:raise SystemExit('\n'.join(errors))
