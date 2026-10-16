"""Move the steppe penalty into the persistent economy; replay each milestone."""
import json
from patch_mkn_overhaul import ROOT, save, put, block
from hoi4_script import read, one, values, walk

def main():
    if 'MKN_industry_projects_v3' in (ROOT/'common/scripted_effects/nww_mkn_progression.txt').read_text():
        raise SystemExit('Historical v2 patch cannot overwrite the consolidated v3 economy. Edit the current country files directly.')
    path='common/national_focus/MKN.txt';doc=read(ROOT/path);tree=one(doc,'focus_tree')
    fs={one(f,'id'):f for f in values(tree,'focus')}
    chains=[['MKN_dneprostroi','MKN_dnieper_audit','MKN_engineering_delegates','MKN_zaporizhstal','MKN_kommunar_tractor'],['MKN_free_cooperatives','MKN_artel_register','MKN_village_smithies','MKN_mobile_workshops','MKN_rifle_concern']]
    metadata=json.loads((ROOT/'docs/MKN_unified_progression.json').read_text(encoding='utf-8-sig'))
    metadata['initial']['industrial_capacity_factory']=-0.25
    # The extra -10% formerly on Steppes Freedom is repaired over five distinct
    # industrial milestones, never stacked as a second permanent economy spirit.
    for chain in chains:
        for fid in chain:
            old=metadata['industry_changes'].setdefault(fid,{})
            if not metadata.get('steppe_recovery_v2'):
                old['industrial_capacity_factory']=round(old.get('industrial_capacity_factory',0)+0.02,4)
    for fid in ('MKN_industrial_compact','MKN_communal_compact'):
        metadata['industry_changes'].setdefault(fid,{})['global_building_slots_factor']=0.30
    metadata['steppe_recovery_v2']=chains
    (ROOT/'docs/MKN_unified_progression.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    effects_path='common/scripted_effects/nww_mkn_progression.txt';effects=read(ROOT/effects_path);rebuild=one(effects,'nww_mkn_rebuild_industry')
    for n in values(rebuild,'set_variable'):
        if one(n,'MKN_unified_industrial_capacity_factory') is not None:put(n,'MKN_unified_industrial_capacity_factory','-0.2500')
    if not any(one(n,'MKN_unified_global_building_slots_factor') is not None for n in values(rebuild,'set_variable')):
        rebuild.insert(0,('set_variable',block('MKN_unified_global_building_slots_factor = 0'), '='))
    for fid in {f for chain in chains for f in chain}|{'MKN_industrial_compact','MKN_communal_compact'}:
        stats=metadata['industry_changes'][fid]
        reward=one(fs[fid],'completion_reward')
        for stat in ('industrial_capacity_factory','global_building_slots_factor'):
            if stat not in stats:continue
            var='MKN_unified_'+stat
            reward[:]=[n for n in reward if not(n[0]=='add_to_variable' and one(n[1],var) is not None)]
            reward.append(('add_to_variable',block(f'{var} = {stats[stat]:.4f} tooltip = {var}_tt'), '='))
            matching=next((n for n in values(rebuild,'if') if one(one(n,'limit'),'has_completed_focus')==fid),None)
            if matching is None:
                matching=block(f'limit = {{ has_completed_focus = {fid} }}');rebuild.append(('if',matching,'='))
            matching[:]=[n for n in matching if not(n[0]=='add_to_variable' and one(n[1],var) is not None)]
            matching.append(('add_to_variable',block(f'{var} = {stats[stat]:.4f}'), '='))
    if 'MKN_free_workshops_focus' not in fs:
        tree.extend(block('''focus = { id = MKN_free_workshops_focus icon = GFX_idea_MKN_free_workshops
            x = 24 y = 13 cost = 5
            available = { OR = { has_completed_focus = MKN_industrial_compact has_completed_focus = MKN_communal_compact } }
            completion_reward = { custom_effect_tooltip = MKN_free_workshops_unlock_tt }
            ai_will_do = { factor = 3 }
        }'''))
    save(path,doc);save(effects_path,effects)
    path='common/dynamic_modifiers/nww_dynamic_modifiers.txt';doc=read(ROOT/path)
    put(one(doc,'MKN_free_industry_modifier'),'global_building_slots_factor','MKN_unified_global_building_slots_factor');save(path,doc)
    path='common/ideas/MKN_ideas.txt';doc=read(ROOT/path)
    one(one(one(one(doc,'ideas'),'country'),'MKN_steppes_freedom'),'modifier')[:]=[n for n in one(one(one(one(doc,'ideas'),'country'),'MKN_steppes_freedom'),'modifier') if n[0]!='industrial_capacity_factory']
    ideas=one(doc,'ideas')
    if one(ideas,'industrial_concern') is None:put(ideas,'industrial_concern',[])
    put(one(ideas,'industrial_concern'),'MKN_free_workshops',block('''picture = MKN_free_workshops allowed = { original_tag = MKN }
        available = { has_completed_focus = MKN_free_workshops_focus } cost = 150
        research_bonus = { industry = 0.15 }
        modifier = { production_speed_buildings_factor = 0.10 production_factory_max_efficiency_factor = 0.05 }
    '''));save(path,doc)
    # AAT organization inherits its generic progression and offers a separate
    # equipment research/production role. The concern retains industry research.
    save('common/military_industrial_organization/organizations/MKN_organizations.txt',block('''MKN_free_workshops = {
        include = generic_infantry_equipment_organization icon = GFX_idea_MKN_free_workshops
        allowed = { original_tag = MKN }
        available = { FROM = { has_completed_focus = MKN_free_workshops_focus } }
        initial_trait = { name = MKN_free_workshops_initial_trait
            organization_modifier = { military_industrial_organization_research_bonus = 0.15 }
            production_bonus = { production_efficiency_cap_factor = 0.05 }
        }
    }'''))

if __name__=='__main__':main()
