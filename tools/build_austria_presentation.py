"""Rebuild Austrian presentation from project originals; verified semantic icon map."""
from pathlib import Path
import re, json, math, shutil
from PIL import Image, ImageDraw, ImageFont
from hoi4_script import read, one, values

ROOT = Path(__file__).resolve().parents[1]
GAME = Path('D:/Steam/steamapps/common/Hearts of Iron IV')
def write(name, text):
    p = ROOT/name
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(text,encoding='utf-8-sig' if name.endswith('.yml') else 'utf-8',newline='\n')

def build_icons():
    mapping = {}
    def assign(ids, icons):
        ids,icons = ids.split(),icons.split()
        assert len(ids)==len(icons),(ids,icons)
        for fid,icon in zip(ids,icons):
            mapping[fid] = icon if icon.startswith('GFX_') else 'GFX_focus_generic_'+icon
    assign('AUS_nww_rebuild AUS_political_power AUS_reinstate_the_imperial_council AUS_hold_elections AUS_the_danubian_federation AUS_via_danube_to_europe AUS_not_germany AUS_join_to_axis AUS_help_from_eng AUS_war_with_hun AUS_war_with_croatia AUS_reclaiming_yugoslavian_territories AUS_nww_army AUS_army_expierience AUS_bring_generals_out_of_retirement AUS_establish_bohme_plan AUS_nww_industry aus_prom aus_prom_2 aus_prom_3 aus_prom_4 aus_prom_5 AUS_new_economic AUS_reform_the_economic AUS_create_a_new_econimic NWW_AUS_restore_dual_monarchy',
      'GFX_focus_AUS_nww_eagle improve_the_administration GFX_focus_AUS_nww_eagle GFX_focus_AUS_nww_constitution the_council_of_europe balkan_diplomacy monarchist_sentiment german_trade british_trade attack_hungary GFX_goal_generic_territory_or_war balkans_focus GFX_focus_AUS_nww_army advanced_military_studies advisors GFX_goal_generic_army_artillery GFX_focus_AUS_nww_danube public_works industry_investment steel_mill improve_roads industry_3 economic_recovery currency_reforms central_planning GFX_focus_proclaim_the_restauration_of_Austria_Hungary')
    groups = {
      'absolute':('debate cabinet crown_service provincial_diets loyal_officers imperial_chancery crown_law','GFX_focus_AUS_nww_eagle monarchy_1 improve_the_administration_2 subjugation soldier_salute commission monarchy_2'),
      'constitutional':('debate responsible_ministry parliament rights coalition federal_court constitutional_crown','GFX_focus_AUS_nww_constitution advisors vote universal_suffrage public_meetings court GFX_focus_BRA_constitutional_monarchy'),
      'fascist':('debate settlement directorate corporations veterans propaganda security national_state','fascist_propaganda military_dictatorship national_security industrialists fascist_troops printing_press secret_service_agency spread_fascism'),
      'communist':('debate settlement workers_councils land unions planning nationalities social_republic','red_flags communist worker_administration land_redistribution workers central_planning diverse_army social_democracy'),
      'alternative':('debate settlement dynastic_pact landed_elites royal_guard court_reform crown_diplomats succession_act','monarchist_sentiment monarchy_2 royal_wedding farmland GFX_focus_AFG_royal_guard improve_the_administration diplomatic_treaty GFX_focus_AUS_nww_eagle'),
    }
    for branch,(suffixes,icons) in groups.items():
        assign(' '.join('AUS_nww2_'+branch+'_'+s for s in suffixes.split()),icons)
    assign(' '.join('AUS_nww2_'+s for s in 'galician_ultimatum bukovina_ultimatum german_competition danubian_congress customs finance intelligence strategic_reserve sovereign_danube equal_empires invite_rom invite_bul invite_yug danubian_security danubian_research crownland_administration language_charter prague_conference local_budget land_compromise technical_compact provincial_court representation crownland_settlement'.split()),
      'GFX_goal_generic_demand_territory GFX_goal_generic_forceful_treaty GFX_goal_generic_political_pressure conference GFX_goal_generic_trade monetary_union secret_agent_operative stockpile_fuel GFX_goal_generic_neutrality_focus GFX_goal_generic_major_alliance befriend_romania befriend_bulgaria GFX_goal_generic_improve_relations GFX_goal_generic_military_sphere GFX_goal_tfv_generic_tech_sharing GFX_focus_AUS_nww_eagle GFX_focus_AUS_nww_constitution befriend_bohemia stockpile_currency agricultural_subsidies GFX_goal_generic_scientific_exchange sympathetic_judges freedom_council GFX_focus_AUS_nww_eagle')
    numbered = {
      'civilian':'GFX_goal_generic_construct_civ_factory steel_mill industrial_experts railroad public_works electrification low_cost_housing mass_production full_employment',
      'military':'military_industry GFX_goal_generic_small_arms military_mission GFX_goal_generic_army_artillery2 arms_trade reorient_production mass_production tank_production stockpile_currency',
      'technology':'university_1 education GFX_goal_generic_secret_weapon GFX_goal_generic_radar GFX_goal_tfv_generic_tech_sharing industrial_experts GFX_focus_research university_3 resource_extraction',
      'air':'pilot_training aircraft_production flight_instructors GFX_goal_generic_air_fighter cas_aircraft GFX_goal_generic_air_doctrine air_bases air_partners multi_role_aircraft jet_planes radio_communication air_defense',
      'navy':'GFX_goal_generic_construct_naval_dockyard merchant_fleet GFX_goal_generic_navy_cruiser naval_discipline mine_warfare GFX_goal_generic_navy_anti_submarine GFX_goal_generic_navy_submarine GFX_goal_generic_navy_battleship refit_civilian_ships GFX_goal_generic_navy_doctrines_tactics escort_efficiency adriatic_sea_focus',
    }
    for branch,icons in numbered.items():
        assign(' '.join(f'AUS_nww2_{branch}_{i+1}' for i in range(len(icons.split()))),icons)
    armies = [
      'military_academy GFX_goal_generic_army_doctrines radio_communication reinforce_placeholder mountain_training soldier_salute',
      'mountain_troops mountain_fortification GFX_goal_generic_army_artillery2 home_defense field_hostpital GFX_goal_generic_special_forces',
      'truck GFX_goal_generic_army_tanks motor_cycle supply_line combined_arms tank_assault',
    ]
    armies[0] = armies[0].replace('reinforce_placeholder','reinforcing_the_supply_network')
    for row,icons in enumerate(armies):
        assign(' '.join(f'AUS_nww2_army_{row}_{i}' for i in range(6)),icons)
    assign('AUS_nww2_air_command AUS_nww2_navy_command','GFX_focus_AUS_nww_air GFX_focus_AUS_nww_navy')
    # Parse direct sprite definitions only; validate exact textures and state variants.
    sprites = {}
    for path in (GAME/'interface').glob('*.gfx'):
        try:
            parsed = read(path)
        except ValueError:
            # A few unrelated native files contain shader text outside this parser.
            continue
        for node in values(parsed,'spriteTypes'):
            for typ,body,op in node:
                if typ.lower() == 'spritetype' and isinstance(body,list):
                    name,texture = one(body,'name'),one(body,'texturefile')
                    if name and texture: sprites[name.strip('"')] = texture.strip('"')
    custom = {f'GFX_focus_AUS_nww_{n}':f'gfx/interface/goals/AUS/{n}.dds' for n in ['eagle','constitution','danube','army','air','navy']}
    mapping['AUS_nww2_invite_rom'] = 'GFX_goal_generic_alliance'
    # Avoid the modern European flag and the native Nazi trade badge in NWW lore.
    mapping['AUS_the_danubian_federation'] = 'GFX_focus_AUS_nww_constitution'
    mapping['AUS_join_to_axis'] = 'GFX_goal_generic_military_deal'
    mapping['AUS_nww2_constitutional_constitutional_crown'] = 'GFX_focus_AUS_nww_constitution'
    tree = one(read(ROOT/'common/national_focus/AUS_focuses.txt'),'focus_tree')
    ids = {one(f,'id') for f in values(tree,'focus')}
    assert ids == set(mapping),(ids-set(mapping),set(mapping)-ids)
    for fid,icon in mapping.items():
        assert icon in sprites or icon in custom,(fid,icon)
        texture = custom.get(icon,sprites.get(icon))
        assert (ROOT/texture).exists() or (GAME/texture).exists(),(icon,texture)
    gfx = 'spriteTypes = {\n'
    for icon,texture in custom.items():
        gfx += f' spriteType = {{ name = {icon} texturefile = "{texture}" }}\n'
    # Preserve modifier/category sprite IDs from existing saves.
    for n in ['eagle','constitution','danube','army','air','navy']:
        gfx += f' spriteType = {{ name = GFX_AUS_nww_{n} texturefile = "gfx/interface/goals/AUS/{n}.dds" }}\n'
    gfx += ' spriteType = { name = GFX_decision_AUS_nww_eagle texturefile = "gfx/interface/goals/AUS/eagle.dds" }\n}\n'
    write('interface/AUS_crownlands.gfx',gfx)
    shine = 'spriteTypes = {\n'
    for icon in sorted(set(mapping.values())):
        if icon+'_shine' in sprites: continue
        texture = custom.get(icon,sprites.get(icon))
        shine += f' spriteType = {{\n  name = {icon}_shine\n  texturefile = "{texture}"\n  effectFile = "gfx/FX/buttonstate.lua"\n  legacy_lazy_load = no\n'
        for rotation in ['-90.0','90.0']:
            shine += f'''  animation = {{
   animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
   animationmaskfile = "{texture}"
   animationrotation = {rotation}
   animationlooping = no
   animationtime = 0.75
   animationdelay = 0
   animationblendmode = add
   animationtype = scrolling
   animationrotationoffset = {{ x = 0.0 y = 0.0 }}
   animationtexturescale = {{ x = 1.0 y = 1.0 }}
  }}
'''
        shine += ' }\n'
    write('interface/AUS_focus_shine.gfx',shine+'}\n')
    path = ROOT/'common/national_focus/AUS_focuses.txt'
    text = re.sub(r'^\t\tid = (\w+)\s+(?:(?!icon =).)*?icon = (\w+)',lambda m:m[0][:-len(m[2])]+mapping[m[1]],path.read_text(encoding='utf-8-sig'),flags=re.S|re.M)
    write(str(path.relative_to(ROOT)),text)
    write('docs/art/AUS/focus_icon_map.json',json.dumps(mapping,indent=2)+'\n')
    print(f'Assigned {len(mapping)} focuses to {len(set(mapping.values()))} verified icons with shine variants')

def build_panel():
    folder = ROOT/'gfx/interface/AUS'
    folder.mkdir(parents=True,exist_ok=True)
    panel = Image.open(ROOT/'docs/art/AUS/bohemian_panel_original.png').convert('RGBA').resize((440,220),Image.Resampling.LANCZOS)
    panel.save(folder/'bohemian_panel.dds')
    # Simple code-native UI indicator primitives; artwork is generated separately.
    for name,color in [('socket',(43,35,30,255)),('seal',(171,44,34,255))]:
        im=Image.new('RGBA',(16,16)); d=ImageDraw.Draw(im)
        d.ellipse((1,1,14,14),fill=(91,67,37,255),outline=(212,181,113,255),width=1)
        d.ellipse((4,4,11,11),fill=color)
        if name=='seal': d.ellipse((5,5,9,8),fill=(219,112,71,255))
        im.save(folder/f'bohemian_{name}.dds')
    gfx='spriteTypes = {\n'
    for name in ['panel','socket','seal']:
        gfx+=f' spriteType = {{ name = GFX_AUS_bohemian_{name} texturefile = "gfx/interface/AUS/bohemian_{name}.dds" }}\n'
    write('interface/AUS_bohemian_gui.gfx',gfx+'}\n')
    gui='''guiTypes = {
 containerWindowType = {
  name = "AUS_bohemian_window"
  position = { x = 0 y = 0 }
  size = { width = 100% height = 228 }
  iconType = { name = "AUS_background" spriteType = "GFX_AUS_bohemian_panel" orientation = center_up position = { x = -220 y = 0 } pdx_tooltip = AUS_nww_meter_help }
'''
    def text(name,key,x,y,width,height,font='hoi_16mbs'):
        return f'  instantTextBoxType = {{ name = "{name}" orientation = center_up position = {{ x = {x-228} y = {y} }} font = "{font}" text = "{key}" format = center maxWidth = {width} maxHeight = {height} pdx_tooltip = AUS_nww_meter_help }}\n'
    gui+=text('AUS_panel_title','AUS_nww_panel_title',108,83,240,24,'hoi_18mbs')
    gui+=text('AUS_panel_value','AUS_nww_panel_value',108,109,240,24,'hoi_18mbs')
    gui+=text('AUS_panel_influence','AUS_nww_panel_influence',124,130,208,20).replace('pdx_tooltip = AUS_nww_meter_help','pdx_tooltip = AUS_nww_german_influence_tt')
    gui+=text('AUS_panel_vienna','AUS_nww_panel_vienna',24,130,100,20)
    gui+=text('AUS_panel_prague','AUS_nww_panel_prague',332,130,100,20)
    gui+=text('AUS_zero','AUS_nww_panel_zero',19,154,20,20)
    gui+=text('AUS_ten','AUS_nww_panel_ten',417,154,24,20)
    script='''scripted_gui = {
 AUS_bohemian_ui = {
  context_type = decision_category
  window_name = AUS_bohemian_window
  visible = { original_tag = AUS }
  triggers = {
'''
    for i in range(11):
        x,y=42+i*34,146+round(8*math.sin(math.pi*i/10))
        gui+=f'  iconType = {{ name = "AUS_socket_{i}" spriteType = "GFX_AUS_bohemian_socket" orientation = center_up position = {{ x = {x-228} y = {y} }} }}\n'
        gui+=f'  iconType = {{ name = "AUS_seal_{i}" spriteType = "GFX_AUS_bohemian_seal" orientation = center_up position = {{ x = {x-228} y = {y} }} pdx_tooltip = AUS_nww_meter_help }}\n'
        script+=f'   AUS_seal_{i}_visible = {{ check_variable = {{ var = AUS_bohemian_tension value = {i} compare = greater_than_or_equals }} }}\n'
    for i,(lo,hi) in enumerate([(0,2),(3,4),(5,6),(7,9),(10,10)]):
        gui+=text(f'AUS_stage_{i}',f'AUS_nww_panel_stage_{i}',25,191,404,24)
        script+=f'   AUS_stage_{i}_visible = {{ check_variable = {{ var = AUS_bohemian_tension value = {lo} compare = greater_than_or_equals }} check_variable = {{ var = AUS_bohemian_tension value = {hi} compare = less_than_or_equals }} }}\n'
    write('interface/AUS_bohemian_gui.gui',gui+' }\n}\n')
    write('common/scripted_guis/AUS_bohemian_gui.txt',script+'  }\n }\n}\n')

if __name__=='__main__':
    build_icons()
    build_panel()
