"""Synchronize vanilla cosmetic colours and NWW country selection/history."""
from pathlib import Path
import copy
import json
from hoi4_script import read, one, values, parse, dump

ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')


def save(path,doc):
    path=ROOT/path;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(dump(doc)+'\n',encoding='utf-8',newline='\n')


def setv(doc,key,value):
    doc[:]=[n for n in doc if n[0]!=key];doc.append((key,value,'='))


def main():
    # cosmetic.txt is a filename override: a two-entry replacement discarded all
    # native Raj/Spanish/dominion palettes, even though colors.txt was intact.
    native=read(GAME/'common/countries/cosmetic.txt')
    own=read(ROOT/'common/countries/cosmetic.txt')
    native_keys={k for k,_,_ in native}
    custom=[n for n in own if n[0] not in native_keys]
    palette='\n'.join(line.rstrip() for line in (GAME/'common/countries/cosmetic.txt').read_text(encoding='utf-8-sig').splitlines())
    (ROOT/'common/countries/cosmetic.txt').write_text(palette.rstrip()+'\n\n# NWW-specific palettes.\n'+dump(custom)+'\n',encoding='utf-8',newline='\n')
    profiles={
        'GER':(['GER_imperial_overstretch','GER_master_of_mitteleuropa','GER_prussian_martial_spirit'],['GER_the_kaiser_endures','GER_prussian_traditions','GER_the_gilded_colossus'],'neutrality'),
        'ENG':(['ENG_nww_preview_'+s for s in ['state','economy','navy']],['ENG_nww_report','ENG_nww_federal','ENG_nww_labour'],'democratic'),
        'FRA':(['FRA_nww_preview_state','FRA_nww_preview_economy','FRA_nww_preview_army'],['FRA_nww_front','FRA_nww_right','FRA_nww_republic'],'democratic'),
        'SOV':(['NWW_SOV_state_0','NWW_SOV_economy_0','NWW_SOV_army_0'],[], 'communism'),
        'LTB':(['LTB_unresolved_national_question','LTB_semi_agrarian_economy','LTB_disorganized_army'],[], 'neutrality'),
        'MKN':(['MKN_free_territory','MKN_decaying_batko','MKN_cult_of_railways'],[], 'communism'),
        'UKR':(['UKR_breadbasket_of_the_union'],[], 'communism'),
        'TUR':(['NWW_TUR_imperial_crisis'],[], 'neutrality'),
        'AUS':(['AUS_nww_preview_bohemia'],[], 'neutrality'),
    }
    # Root focuses from each country's own playable tree, never old placeholders.
    for tag,(ideas,foci,ideology) in profiles.items():
        if foci:continue
        candidates=[]
        for path in (ROOT/'common/national_focus').glob('*.txt'):
            if not path.name.upper().startswith(tag):continue
            for tree in values(read(path),'focus_tree'):
                candidates.extend(one(f,'id') for f in values(tree,'focus') if not values(f,'prerequisite') and not values(f,'allow_branch'))
        profiles[tag]=(ideas,candidates[:3],ideology)
    bookmark=read(ROOT/'common/bookmarks/nww_1936.txt')
    node=one(one(bookmark,'bookmarks'),'bookmark')
    for tag,(ideas,foci,ideology) in profiles.items():
        country=one(node,tag)
        setv(country,'ideas',parse(' '.join(ideas)))
        setv(country,'focuses',parse(' '.join(foci)))
        setv(country,'ideology',ideology)
    save('common/bookmarks/nww_1936.txt',bookmark)
    # History effects are evaluated for the scenario before on_startup; retain
    # idempotent startup/daily repair, but display the actual institutions at once.
    for filename,effect in [('ENG - Britain.txt','ENG_nww_initialize'),('AUS - Austria.txt','AUS_nww_initialize')]:
        path=ROOT/'history/countries'/filename
        text=path.read_text(encoding='utf-8-sig')
        if not any(k==effect for k,_,_ in parse(text)):
            text=text.rstrip()+'\n\n# NWW scenario institutions; startup repair is idempotent.\n'+effect+' = yes\n'
        path.write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n',encoding='utf-8',newline='\n')
    # Snapshot ideas exist only for the selection menu and alias real spirit names.
    effects={k:v for k,v,_ in read(ROOT/'common/scripted_effects/ENG_effects.txt')}
    initial={one(v,'var',v[0][0]):float(one(v,'value',v[0][1])) for v in values(effects['ENG_nww_rebuild_spirits'],'set_variable')}
    previews=[]
    for key,mods,_ in read(ROOT/'common/dynamic_modifiers/ENG_modifiers.txt'):
        modifier=[(k,str(initial[v]),'=') for k,v,_ in mods if isinstance(v,str) and v in initial]
        previews.append(('ENG_nww_preview_'+key.removeprefix('ENG_nww_'),parse(f'name = {key} picture = {key} allowed = {{ always = no }} removal_cost = -1')+[('modifier',modifier,'=')],'='))
    save('common/ideas/ENG_preview_ideas.txt',[('ideas',[('country',previews,'=')],'=')])
    # Bohemia starts at tension 2: derive exactly the same formula as its live effect.
    aus=read(ROOT/'common/scripted_effects/AUS_overhaul_effects.txt')
    body=one(aus,'AUS_nww_update_bohemian_spirit')
    def coefficient(var):
        return float(next(one(v,'value',v[0][1]) for v in values(body,'multiply_variable') if one(v,'var',v[0][0])==var))
    bohemia=parse('name = AUS_nww_bohemian_question picture = generic_constitutional_guarantees allowed = { always = no } removal_cost = -1')
    bohemia.append(('modifier',parse(f'stability_factor = {2*coefficient("AUS_bohemian_stability")} industrial_capacity_factory = {2*coefficient("AUS_bohemian_output")}'),'='))
    save('common/ideas/AUS_preview_ideas.txt',[('ideas',[('country',[('AUS_nww_preview_bohemia',bohemia,'=')],'=')],'=')])
    from hoi4_script import quoted
    aliases={**{'ENG_nww_preview_'+s:'ENG_nww_'+s for s in ['state','economy','army','air','navy','science']},'AUS_nww_preview_bohemia':'AUS_nww_bohemian_question'}
    for tag in ['ENG','AUS']:
        for lang in ['russian','english']:
            entries=[]
            for key,real in aliases.items():
                if not key.startswith(tag):continue
                entries.extend([' '+key+':0 '+quoted('$'+real+'$'),' '+key+'_desc:0 '+quoted('$'+real+'_desc$')])
            (ROOT/f'localisation/{lang}/{tag}_preview_l_{lang}.yml').write_text('l_'+lang+':\n'+'\n'.join(entries)+'\n',encoding='utf-8-sig',newline='\n')
    out=ROOT/'docs/1936_start_profiles.json'
    out.write_text(json.dumps(profiles,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('Restored vanilla cosmetic palettes; synchronized nine NWW selection profiles and ENG/AUS scenario initialization.')


if __name__=='__main__':main()
