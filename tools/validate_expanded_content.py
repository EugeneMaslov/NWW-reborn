"""Checks for MKN single-spirit progression and expanded country content."""
from hoi4_script import read, one, values, walk
import re
import json

def validate_expansion(root, game, check, localized):
    tree=one(read(root/'common/national_focus/MKN.txt'),'focus_tree')
    fs={one(f,'id'):f for f in values(tree,'focus')}
    effects=read(root/'common/scripted_effects/nww_mkn_progression.txt')
    initialize=one(effects,'nww_mkn_rebuild_industry')
    initial={k:float(v) for block in values(initialize,'set_variable') for k,v,o in block}
    dyn=read(root/'common/dynamic_modifiers/nww_dynamic_modifiers.txt')
    spirit=one(dyn,'MKN_free_industry_modifier')
    docs=(game/'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig')
    known=set(re.findall(r'^## (\w+)',docs,re.M))
    building_types={k for k,v,o in one(read(game/'common/buildings/00_buildings.txt'),'buildings')}
    known|={'production_speed_'+kind+'_factor' for kind in building_types}
    for stat,var,op in spirit:
        if stat in ('enable','icon','custom_modifier_tooltip'):continue
        check(stat in known,f'MKN unified industry: unknown modifier {stat}')
        check(var in initial,f'MKN unified industry: uninitialized variable {var}')
    history=read(root/'history/countries/MKN - Makhnovists.txt')
    starts={v for b in values(history,'add_ideas') for k,v,o in b}
    check(not starts & {'MKN_anarchic_economy_idea','MKN_fragmented_workshops','MKN_broken_supply','MKN_untrained_militias'},'MKN still starts with separate industrial crisis spirits')
    startup=one(one(read(root/'common/on_actions/nww_mkn_progression.txt'),'on_actions'),'on_startup')
    check(any(k=='nww_mkn_rebuild_industry' for k,v,o in walk(startup)),'MKN: unified industry is not initialized on startup')
    adverse={'consumer_goods_factor','supply_consumption_factor','training_time_army_factor','factory_energy_consumption','attrition'}
    for entry in ('MKN_dneprostroi','MKN_free_cooperatives'):
        branch={entry}
        while True:
            more={fid for fid,f in fs.items() if any(parent in branch for g in values(f,'prerequisite') for parent in values(g,'focus'))}-branch
            if not more:break
            branch|=more
        check(len(branch)>=20,f'{entry}: fewer than 20 dedicated focuses')
        deps={fid:{p for g in values(fs[fid],'prerequisite') for p in values(g,'focus')}|{v for k,v,o in walk(one(fs[fid],'available',[])) if k=='has_completed_focus'} for fid in branch}
        done=set();score=dict(initial)
        while done!=branch:
            ready={fid for fid in branch-done if deps[fid]<=done}
            if not ready:check(False,f'{entry}: availability cycle');break
            for fid in ready:
                reward=one(fs[fid],'completion_reward')
                check(not any(k=='add_ideas' and isinstance(v,str) for k,v,o in walk(reward)),f'{fid}: creates another permanent industrial spirit')
                for b in values(reward,'add_to_variable'):
                    for k,v,o in b:
                        if k.startswith('MKN_unified_'):score[k]=score.get(k,0)+float(v)
                    if one(b,'tooltip'):localized(one(b,'tooltip'),fid)
            done|=ready
        for stat,var,o in spirit:
            if stat in known:
                val=score[var]
                check(val<=1e-6 if stat in adverse else val>=-1e-6,f'{entry}: final unified spirit retains {stat} penalty ({val})')
        print(f'PASS: {entry}: {len(branch)} focuses, one permanent industry spirit, all initial penalties resolved')
    events={one(e,'id'):e for e in values(read(root/'events/nww_mkn.txt'),'country_event')}
    for eid in ('mkn.30','mkn.31'):
        e=events[eid];localized(one(e,'title'),eid);localized(one(e,'desc'),eid)
        for opt in values(e,'option'):
            localized(one(opt,'name'),eid)
            check(one(one(opt,'add_timed_idea',[]),'days')=='365',f'{eid}: temporary congress policy duration changed')
    # All new dynamic and advisor modifier names come from the installed version.
    all_dyn={}
    for path in (root/'common/dynamic_modifiers').glob('nww*txt'):
        for name,node,op in read(path):
            if name.startswith(('MKN_','UKR_')):all_dyn[name]=node
    initialization={k for key,node,op in walk(effects) if key=='set_variable' for k,v,o in node}
    initialization|={k for node in values(read(root/'history/countries/UKR - Ukraine.txt'),'set_variable') for k,v,o in node}
    for name,node in all_dyn.items():
        localized(name,name);localized(name+'_desc',name)
        for stat,var,op in node:
            if stat in ('enable','icon','custom_modifier_tooltip'):continue
            check(stat in known,f'{name}: unknown installed modifier {stat}')
            check(var in initialization,f'{name}: variable {var} is not initialized')
    for relative in ('common/country_leader/nww_mkn_advisor_traits.txt','common/country_leader/nww_mkn_industry_traits.txt'):
        for token,trait,op in one(read(root/relative),'leader_traits'):
            localized(token,token)
            for key,value,operator in trait:
                check(key in known or key in ('sprite','random','type'),f'{token}: unsupported advisor modifier {key}')
            check(one(trait,'random')=='no',f'{token}: local specialization can be assigned to foreign random characters')

    programs=[('army','MKN_steel_horses','MKN_batko_cavalry','MKN_mechanized_compact','MKN_free_army_compact'),
              ('air','MKN_black_swarm','MKN_close_support_program','MKN_free_sky_compact','MKN_air_support_compact'),
              ('navy','MKN_coastal_defense_steppe','MKN_black_sea_smugglers','MKN_escort_compact','MKN_raider_compact')]
    for service,left,right,left_end,right_end in programs:
        for entry,other,finale in ((left,right,left_end),(right,left,right_end)):
            branch={entry}
            while True:
                more={fid for fid,f in fs.items() if any(parent in branch for g in values(f,'prerequisite') for parent in values(g,'focus'))}-branch
                if not more:break
                branch|=more
            spec=next(p for p in json.loads((root/'docs/MKN_military_programs.json').read_text()) if p['entry']==entry)
            core=set(spec['core']);optional=set(spec['optional'])
            check(len(core)==10 and len(optional)==10 and not core & optional and core | optional==branch,f'{entry}: expected ten core and ten optional focuses')
            check(other in {p for g in values(fs[entry],'mutually_exclusive') for p in values(g,'focus')},f'{entry}: opposite military program is not excluded')
            required={v for k,v,o in walk(one(fs[finale],'available',[])) if k=='has_completed_focus'}
            check(required==core-{finale},f'{finale}: must require only the nine core institutions')
            check(len({one(fs[fid],'icon') for fid in branch})>=15,f'{entry}: insufficient illustration variety')
            check(len({str(one(fs[fid],'completion_reward')) for fid in branch})==len(branch),f'{entry}: duplicated military rewards')
            deps={fid:({p for g in values(fs[fid],'prerequisite') for p in values(g,'focus')}|{v for k,v,o in walk(one(fs[fid],'available',[])) if k=='has_completed_focus'}) & branch for fid in branch}
            done=set()
            while done!=branch:
                ready={fid for fid in branch-done if deps[fid]<=done}
                if not ready:check(False,f'{entry}: availability gates create a cycle');break
                done|=ready
            for fid in branch:
                reward=one(fs[fid],'completion_reward')
                check(not any(k=='add_ideas' and isinstance(v,str) for k,v,o in walk(reward)),f'{fid}: creates another permanent military spirit')
                check(any(k=='add_to_variable' and any(a and a.startswith('MKN_'+service+'_') for a,b,o in v) for k,v,o in reward),f'{fid}: does not develop its service spirit')
            check(all(not deps[fid] & optional for fid in core),f'{entry}: optional focus blocks the core programme')
            print(f'PASS: {entry}: ten core and ten optional focuses, varied icons/rewards, exclusive program, one service spirit')

    # Preserve the central templates while suppressing their generic instances only for MKN.
    generic='common/military_industrial_organization/organizations/00_generic_organization.txt'
    before=dict((k,v) for k,v,o in read(game/generic));after=dict((k,v) for k,v,o in read(root/generic))
    check(before.keys()==after.keys(),'Generic MIO template definitions were removed')
    for token,node in before.items():
        modified=after.get(token,[])
        check([(k,v,o) for k,v,o in node if k!='allowed']==[(k,v,o) for k,v,o in modified if k!='allowed'],f'{token}: generic template traits or statistics changed')
        check(any(one(n,'original_tag')=='MKN' for n in values(one(modified,'allowed',[]),'NOT')),f'{token}: generic instance is still available to MKN')
    base=read(game/generic)
    equipment={k for key,node,o in walk(base) if key=='equipment_bonus' for k,v,o in node}
    production={k for key,node,o in walk(base) if key=='production_bonus' for k,v,o in node}
    local=[(k,v) for k,v,o in read(root/'common/military_industrial_organization/organizations/nww_organizations.txt') if k.startswith('MKN_')]
    check(len(local)>=7,'MKN has fewer than seven specialized manufacturers')
    for token,node in local:
        localized(token,token);localized(one(one(node,'initial_trait'),'name'),token)
        traits={one(t,'token'):t for t in values(node,'add_trait')}
        pairs=set()
        for tid,trait in traits.items():
            localized(tid,tid)
            for other in [v for k,v,o in one(trait,'mutually_exclusive',[])]:
                pairs.add(frozenset((tid,other)))
                check(tid in {v for k,v,o in one(traits.get(other,[]),'mutually_exclusive',[])},f'{tid}: MIO exclusion is not reciprocal')
            parents={v for k,v,o in one(one(trait,'parent',[]),'traits',[])}
            check(parents<=traits.keys(),f'{tid}: missing local MIO parent')
        check(1<=len(pairs)<=2,f'{token}: requires one or two mutually exclusive specialization pairs')
        for key,bonus,op in walk(node):
            if key in ('equipment_bonus','production_bonus'):
                valid=equipment if key=='equipment_bonus' else production
                for stat,value,operator in bonus:check(stat in valid,f'{token}: undocumented MIO stat {stat}')
    print('PASS: seven specialized MIOs, exclusive traits, installed equipment stats, generic templates preserved')

    # Political changes have preparation, forty-percent support and timed campaigning.
    ukr=one(read(root/'common/national_focus/ukr_focus.txt'),'focus_tree')
    uf={one(f,'id'):f for f in values(ukr,'focus')}
    check(60<=len(uf)<=80,'Ukraine focus count must be between sixty and eighty')
    mandates={'MKN': [('MKN_everlasting_makhnovshchina','democratic'),('MKN_council_communism','democratic'),('MKN_constituent_assembly','democratic'),('MKN_red_banner_steppe','communism'),('MKN_black_hundreds','fascism'),('MKN_nestor_the_first','neutrality')],
              'UKR': [('UKR_council_mandate','communism'),('UKR_constituent_mandate','democratic'),('UKR_state_mandate','neutrality')]}
    for tag,routes in mandates.items():
        focuses=fs if tag=='MKN' else uf
        category=one(read(root/f'common/decisions/nww_{tag.lower()}_mandate.txt'),tag+'_public_mandate')
        for fid,ideology in routes:
            focus=focuses[fid];conditions=one(focus,'available',[])
            check(any((ideology,'0.40','<') in negation for negation in values(conditions,'NOT')),f'{fid}: missing forty-percent mandate')
            check(one(focus,'cancel_if_invalid')=='yes' and one(focus,'continue_if_invalid')=='no',f'{fid}: cannot cancel an invalid mandate')
            check(not values(one(focus,'completion_reward'),'add_popularity'),f'{fid}: transition supplies its own popularity')
            campaign=one(category,tag+'_campaign_'+ideology,[])
            check(one(campaign,'days_remove')=='60' and one(campaign,'cost')=='50',f'{tag}/{ideology}: campaign timing or cost differs')
            check(not values(one(campaign,'complete_effect',[]),'add_popularity'),f'{tag}/{ideology}: campaign grants immediate popularity')
            check(one(one(one(campaign,'remove_effect',[]),'add_popularity',[]),'popularity')=='0.10',f'{tag}/{ideology}: campaign does not build a viable mandate')
    foreign={one(e,'id'):e for e in values(read(root/'events/nww_ukr_diplomacy.txt'),'country_event')}
    for request,eid,flag in [('UKR_border_compact','ukr.50','UKR_MKN_border_settled'),('UKR_friends_in_moscow','ukr.51','UKR_moscow_trade'),('UKR_polish_trade','ukr.52','UKR_polish_trade')]:
        reward=one(uf[request],'completion_reward')
        check(not any(k in ('add_tech_bonus','set_country_flag','add_timed_idea') for k,v,o in walk(reward)),f'{request}: receives treaty rewards before acceptance')
        event=foreign[eid];localized(one(event,'title'),eid);localized(one(event,'desc'),eid)
        options=values(event,'option')
        for option in options:localized(one(option,'name'),eid)
        check(flag in {v for k,v,o in walk(options[0]) if k=='set_country_flag'},f'{eid}: acceptance does not settle the proposal')
        check(flag not in {v for k,v,o in walk(options[1]) if k=='set_country_flag'},f'{eid}: refusal grants acceptance')
    print(f'PASS: Ukraine {len(uf)} focuses, genuine political mandates and foreign acceptance/refusal')

    chars=one(read(root/'common/characters/nww_MKN.txt'),'characters')
    advisors=[k for k,v,o in chars if values(v,'advisor')]
    commanders=[k for k,v,o in chars if values(v,'corps_commander') or values(v,'field_marshal')]
    check(len(advisors)>=15,'MKN has fewer than fifteen different advisor characters')
    check(len(commanders)>=7,'MKN has fewer than seven military commanders')
    makhno=one(chars,'NWW_MKN_makhno')
    check(one(one(one(makhno,'field_marshal',[]),'visible',[]),'has_government')=='communism','Makhno field marshal is not restricted to communist governments')
    check(one(one(one(makhno,'advisor',[]),'available',[]),'has_government')=='communism','Makhno military advisor is not restricted to communist governments')
    leaders=values(read(root/'history/countries/MKN - Makhnovists.txt'),'create_country_leader')
    check(any(one(l,'name')=='Emperor Nestor I' and one(l,'picture')=='GFX_Portrait_makhno' for l in leaders),'Monarch Makhno was changed despite the user correction')
    from PIL import Image
    generated=list((root/'docs/art/mkn_commanders').glob('*.png'))
    check(len(generated)>=7,'Seven generated commander originals are required')
    for source in generated:
        check(source.with_suffix('.prompt.txt').is_file(),f'{source.name}: original generation prompt is missing')
        with Image.open(root/f'gfx/leaders/MKN/{source.stem}.dds') as image:
            check(image.size==(156,210),f'{source.name}: wrong large portrait dimensions')
        with Image.open(root/f'gfx/interface/ideas/nww_portraits/MKN_{source.stem}.dds') as image:
            check(image.size==(65,67),f'{source.name}: wrong advisor dimensions')
            bounds=image.getchannel('A').getbbox()
            check(bounds and bounds[0]>=3 and bounds[2]<=62 and bounds[3]<=61,f'{source.name}: artwork overlaps the advisor card frame')
    print(f'PASS: {len(advisors)} advisors, {len(commanders)} commanders, seven generated portraits; monarch Makhno preserved')
