"""Adapt the archived non-LTB trees. Bootstrap only: --write replaces generated content."""
from pathlib import Path
import argparse, copy, json, re, shutil, sys
from PIL import Image
from hoi4_script import read, one, values, parse, dump, walk

ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT/'old-mod/noworldwarzhive'
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')
sys.stdout.reconfigure(encoding='utf-8')
argparse.ArgumentParser(description=__doc__).add_argument('--write',action='store_true')
if '--write' not in sys.argv:
    raise SystemExit('Pass --write to generate the adapted files. Review changes before rerunning.')
loc={}
for p in OLD.glob('localisation/*.yml'):
    loc.update(re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$',p.read_text(encoding='utf-8-sig'),re.M))
texts={'russian':{},'english':{}}
manifest={'source':'old-mod/noworldwarzhive','game_version':'1.19.3','countries':{},'notes':['No Hungarian tree is present in the archive; Hungary extends the existing NWW stub.','The archived Bulgarian focus file is empty.','Existing LTB/MKN content is preserved.']}

def text(key,ru,en):
    texts['russian'][key]=ru; texts['english'][key]=en
def setv(node,key,value):
    node[:]=[(k,v,o) for k,v,o in node if k!=key];node.append((key,value,'='))
def save(relative,doc):
    path=ROOT/relative;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(dump(doc)+'\n',encoding='utf-8')
def tech(category,uses=1,bonus=.5):
    return f'add_tech_bonus = {{ category = {category} uses = {uses} bonus = {bonus} }}'
def doctrine(category):
    key='NWW_legacy_'+category+'_bonus';text(key,'Программа изучения доктрины','Doctrine study programme')
    return f'add_doctrine_cost_reduction = {{ name = {key} category = {category} uses = 1 cost_reduction = 0.5 }}'
def slot():
    return 'if = { limit = { amount_research_slots < 5 } add_research_slot = 1 }'
def build(kind='industrial_complex',level=1,state=None):
    body=f'add_extra_state_shared_building_slots = {level} add_building_construction = {{ type = {kind} level = {level} instant_build = yes }}'
    if state:return f'{state} = {{ if = {{ limit = {{ is_owned_and_controlled_by = ROOT }} {body} }} }}'
    return f'random_owned_controlled_state = {{ limit = {{ is_core_of = PREV }} {body} }}'
def resource(state,kind,amount):
    return f'{state} = {{ if = {{ limit = {{ is_owned_and_controlled_by = ROOT }} add_resource = {{ type = {kind} amount = {amount} }} }} }}'
def mandate(ideology):return f'NOT = {{ {ideology} < 0.40 }}'
def politics(ideology):return f'set_politics = {{ ruling_party = {ideology} elections_allowed = {"yes" if ideology=="democratic" else "no"} }}'
def foreign(tag,event=1):
    return f'{tag} = {{ country_event = {{ id = nww_legacy.{event} days = 1 }} }}'
def peaceful(tag):return f'{tag} = {{ exists = yes is_subject = no }} NOT = {{ has_war_with = {tag} }} is_subject = no'
def war(tag):return f'{tag} = {{ exists = yes }} NOT = {{ has_war_with = {tag} }} NOT = {{ is_in_faction_with = {tag} }} is_subject = no has_war_support > 0.30 date > 1937.1.1'
def goal(tag):return f'create_wargoal = {{ type = annex_everything target = {tag} expire = 730 }}'

class Tree:
    def __init__(self,tag,file,archive=None):
        self.tag=tag;self.file=file;self.archive=archive
        self.tree=parse(f'id = {tag}_focus country = {{ factor = 0 modifier = {{ add = 100 tag = {tag} }} }} default = no')
        self.nodes={};self.source=one(read(OLD/f'common/national_focus/{archive}'),'focus_tree') if archive else None
    def add(self,fid,x,y,parents=(),reward='',ru=None,en=None,description=None,available='',exclusive=(),icon='GFX_focus_generic_diplomatic_treaty',cost=5):
        if fid in self.nodes:raise ValueError('Duplicate focus '+fid)
        f=parse(f'id = {fid} x = {x} y = {y} icon = {icon} cost = {cost} completion_reward = {{ {reward} }}')
        for parent in parents:
            group=parent if isinstance(parent,list) else [parent]
            f.append(('prerequisite',[('focus',v,'=') for v in group],'='))
        if available:
            f.append(('available',parse(available),'='));f.extend(parse('cancel_if_invalid = yes continue_if_invalid = no'))
        if exclusive:f.append(('mutually_exclusive',[('focus',v,'=') for v in exclusive],'='))
        ru=ru or loc.get(fid,fid);en=en or fid.replace('_',' ')
        text(fid,ru,en)
        if description:
            d_ru,d_en=description
        else:
            d_ru=loc.get(fid+'_desc','Согласуем программу с правительством и направим ресурсы на её выполнение.')
            d_en='Coordinate this programme with the government and commit resources to its implementation.'
        text(fid+'_desc',d_ru,d_en)
        self.nodes[fid]=f
    def finish(self):
        oldids=[one(f,'id') for f in values(self.source,'focus')] if self.source else []
        missing=set(oldids)-self.nodes.keys()
        if missing:raise ValueError(f'{self.tag}: unmapped archive focuses {missing}')
        self.tree.extend(('focus',f,'=') for f in self.nodes.values())
        self.tree.append(('continuous_focus_position',parse(f'x = 100 y = {max(int(one(f,"y")) for f in self.nodes.values())*130+1100}'),'='))
        self.tree.append(('initial_show_position',[('focus',next(iter(self.nodes)),'=')],'='))
        save(self.file,[('focus_tree',self.tree,'=')])
        manifest['countries'][self.tag]={'source':self.archive,'destination':self.file,'archive_ids':oldids,'focus_ids':list(self.nodes),'total':len(self.nodes)}

ideas=[];sprites=[]
old_sprites={one(v,'name'):one(v,'texturefile') for p in OLD.glob('interface/*.gfx') for k,v,o in walk(read(p)) if k and k.lower()=='spritetype'}
def idea(token,ru,en,mods,picture='generic_industrial_concern_1',desc=None):
    texture=old_sprites.get('GFX_idea_'+picture)
    if texture and (OLD/texture).is_file():
        relative=f'gfx/interface/ideas/nww_legacy/{picture}.dds'
        target=ROOT/relative;target.parent.mkdir(parents=True,exist_ok=True)
        with Image.open(OLD/texture) as src:
            artwork=src.convert('RGBA');artwork.thumbnail((64,64),Image.Resampling.LANCZOS)
            canvas=Image.new('RGBA',(64,64));canvas.alpha_composite(artwork,((64-artwork.width)//2,(64-artwork.height)//2));canvas.save(target,format='DDS')
        new_picture='nww_legacy_'+picture
        if not any(one(s,'name')=='GFX_idea_'+new_picture for s in sprites):sprites.append(parse(f'name = GFX_idea_{new_picture} texturefile = "{relative}"'))
        picture=new_picture
    ideas.extend(parse(f'{token} = {{ picture = {picture} removal_cost = -1 allowed = {{ always = yes }} modifier = {{ {mods} }} }}'))
    text(token,ru,en)
    text(token+'_desc',*(desc or ('Правительство финансирует эту программу и поддерживает её действие через государственные учреждения.','The government funds this programme and sustains it through public institutions.')))

# Progressive reforms use a single else-if chain, so one focus advances one tier.
effects=[]
def stages(name,sequence):
    branches=[]
    for index in range(len(sequence)-2,-1,-1):
        branches.append(('if' if not branches else 'else_if',parse(f'limit = {{ has_idea = {sequence[index]} }} swap_ideas = {{ remove_idea = {sequence[index]} add_idea = {sequence[index+1]} }}'),'='))
    effects.append((name,branches,'='))
army=['tur_silly_army_nowar',*[f'tur_silly_army_nowar_{i}' for i in range(1,4)],*[f'tur_good_army_{i}' for i in range(1,5)],*[f'tur_perfect_army_{i}' for i in range(1,5)]]
for i,token in enumerate(army):
    strength=[-.20,-.15,-.10,-.05,0,.05,.10,.15,.20,.25,.30,.35][i]
    attack=[-.10,-.10,-.05,-.05,0,.05,.05,.10,.10,.15,.15,.20][i]
    idea(token,loc.get(token,'Реформа османской армии'),f'Ottoman army reform {i+1}',f'army_org_factor = {strength} planning_speed = {strength} army_attack_factor = {attack}', 'silly_army' if i<4 else 'good_army' if i<8 else 'perfect_army',('Согласование командования, снабжения и подготовки поэтапно устраняет слабости османской армии.','Unified command, supply and training gradually overcome weaknesses in the Ottoman army.'))
stages('nww_legacy_TUR_army_step',army)
industry=[*[f'tur_agricultural_economic_{i}' for i in range(1,5)],*[f'tur_small_industry_economic_{i}' for i in range(1,5)],'tur_industry_economic_1']
for i,token in enumerate(industry):
    strength=round(-.20+i*.05,2)
    idea(token,loc.get(token,'Османская индустриализация'),f'Ottoman industrialisation {i+1}',f'industrial_capacity_factory = {strength} production_speed_buildings_factor = {strength}', 'tur_agricult' if i<4 else 'tur_small_industy' if i<8 else 'tur_industy',('Обновление предприятий и инфраструктуры поэтапно сокращает отставание аграрной экономики.','Factory and infrastructure investment gradually closes the gap of an agrarian economy.'))
stages('nww_legacy_TUR_industry_step',industry)
misc={
 'tur_new_democ':('Конституционное движение','Constitutional movement','democratic_drift = 0.02','generic_democratic_drift_bonus'),
 'tur_comun_d':('Рабочее движение','Workers movement','communism_drift = 0.02','generic_communism_drift_bonus'),
 'tur_fascism_d':('Национальное движение','National movement','fascism_drift = 0.02','generic_fascism_drift_bonus'),
 'tur_not_fascism_d':('Конституционный султанат','Constitutional sultanate','stability_factor = 0.05 political_power_gain = 0.05','generic_democratic_drift_bonus'),
 'TUR_factory_idea_1':('Улучшение условий труда','Improved working conditions','stability_factor = 0.04 consumer_goods_factor = 0.02','generic_industrial_concern_1'),
 'TUR_factory_idea_2':('Согласованный трудовой порядок','Industrial labour settlement','stability_factor = 0.04 production_factory_efficiency_gain_factor = 0.04','generic_industrial_concern_1'),
 'TUR_capitalism_economic_1':('Частная промышленность','Private industry','research_speed_factor = 0.02 consumer_goods_factor = 0.02','capitalism_economic'),
 'TUR_capitalism_economic_2':('Экспортная промышленность','Export industry','research_speed_factor = 0.02 production_factory_efficiency_gain_factor = 0.03','capitalism_economic'),
 'TUR_capitalism_economic_3':('Зрелый частный сектор','Mature private sector','research_speed_factor = 0.03 production_factory_efficiency_gain_factor = 0.05','capitalism_economic'),
 'TUR_NFT_1':('Национальный фонд торговли','National trade fund','trade_opinion_factor = 0.10 production_speed_industrial_complex_factor = 0.03','generic_industrial_concern_1'),
 'TUR_NFT_2':('Расширенный торговый фонд','Expanded trade fund','trade_opinion_factor = 0.15 production_speed_industrial_complex_factor = 0.05','generic_industrial_concern_1'),
 'TUR_IPT_1':('Институт промышленных технологий','Institute of industrial technology','research_speed_factor = 0.02 production_factory_max_efficiency_factor = 0.03','generic_industrial_concern_3'),
 'TUR_gold_1':('Золотое обеспечение кредита','Gold-backed credit','consumer_goods_factor = -0.02 production_speed_industrial_complex_factor = 0.05','tur_gold'),
 'TUR_TAS_1':('Турецкая акционерная система','Turkish public holding','consumer_goods_factor = -0.02','tur_TAS'),
 'TUR_TAS_2':('Расширенная акционерная система','Expanded public holding','consumer_goods_factor = -0.03 production_factory_efficiency_gain_factor = 0.03','tur_TAS'),
 'TUR_NNSP_1':('Национальный промышленный совет','National industrial council','production_speed_buildings_factor = 0.05','generic_industrial_concern_3'),
 'TUR_religion_1':('Культурное единство империи','Imperial cultural cohesion','stability_factor = 0.04 war_support_factor = 0.04','generic_industrial_concern_3'),
 'TUR_supply_reform':('Реформа снабжения','Supply reform','supply_consumption_factor = -0.05 army_org_factor = 0.02','supply_reform'),
 'TUR_disagree_reform':('Самостоятельные армейские закупки','Independent army procurement','production_factory_efficiency_gain_factor = 0.05 consumer_goods_factor = 0.02','disagree_reform'),
 'TUR_universal_army_1':('Общевойсковая армия','Combined-arms army','army_org_factor = 0.03 planning_speed = 0.05','universal_army'),
 'tur_closed_cities_1':('Военные городки','Military towns','training_time_factor = -0.05 max_command_power = 10','closed_cities'),
 'TUR_TNPA_1':('Национальная авиационная программа','National aviation programme','air_accidents_factor = -0.10 air_training_xp_gain_factor = 0.10','tur_TNPA'),
 'tur_dominatuim_turco_1':('Османская научная программа','Ottoman scientific programme','research_speed_factor = 0.03 production_factory_max_efficiency_factor = 0.03','dominatium_turcorum'),
 'NWW_TUR_federal_constitution':('Конституция имперской федерации','Imperial federal constitution','stability_factor = 0.05 political_power_gain = 0.05','generic_democratic_drift_bonus'),
 'NWW_TUR_workers_federation':('Федерация рабочих советов','Federation of workers councils','industrial_capacity_factory = 0.03 recruitable_population_factor = 0.03','generic_communism_drift_bonus'),
 'NWW_AUS_currency':('Обновлённый шиллинг','Reformed schilling','consumer_goods_factor = -0.02 production_factory_efficiency_gain_factor = 0.03','generic_industrial_concern_1'),
 'NWW_GER_quality':('Промышленная стандартизация','Industrial standardisation','production_factory_efficiency_gain_factor = 0.04','generic_industrial_concern_1'),
 'NWW_HUN_workshops':('Венгерские производственные мастерские','Hungarian production workshops','production_factory_efficiency_gain_factor = 0.04','generic_industrial_concern_1'),
}
for token,(ru,en,mods,picture) in misc.items():
    # Percentage modifiers advance in useful five-point steps. Daily drift and PP are absolute values.
    mods=re.sub(r'(\w+) = (-?0\.0[234])\b',lambda m: m.group(0) if m.group(1).endswith('_drift') else m.group(1)+' = '+('-0.05' if m.group(2).startswith('-') else '0.05'),mods)
    if token=='TUR_capitalism_economic_3':mods='research_speed_factor = 0.10 production_factory_efficiency_gain_factor = 0.10'
    if token=='TUR_NFT_2':mods='trade_opinion_factor = 0.15 production_speed_industrial_complex_factor = 0.10'
    if token=='TUR_TAS_2':mods='consumer_goods_factor = -0.10 production_factory_efficiency_gain_factor = 0.10'
    idea(token,ru,en,mods,picture)
for i in range(1,5):idea(f'TUR_national_economic_{i}',f'Государственный хозяйственный план — этап {i}',f'State economic plan — stage {i}',f'industrial_capacity_factory = {round(0.05*i,2)} consumer_goods_factor = {round(0.05*i,2)}','national_economic')

# Turkey: all 68 archived IDs, plus complete democratic and socialist endings.
t=Tree('TUR','common/national_focus/turkey.txt','TUR_focus.txt')
labels={
 'TUR_political_rw':'Develop imperial institutions','TUR_prom':'Industrial development','TUR_reform_the_army':'Army reform','TUR_air_1':'Aviation development',
 'TUR_new_fascism':'Turkish nationalism','TUR_not_fascism':'Constitutional sultanate','TUR_new_dem':'The constitutional path','TUR_new_communism':'Workers representation',
 'TUR_set_capital':'Return to Constantinople','TUR_dux_national':'National consolidation','tur_bred':'Rights and liberties','tur_polos':'Representative elections','TUR_proper_stoper':'An independent imperial course','TUR_store_eng':'European diplomatic missions','TUR_kosa_smerti':'The Balkan military programme',
 'TUR_new_economic':'The economic plan','TUR_resourse_icons':'Resource extraction','TUR_Factory_2':'Industrial employment','TUR_Infrastructure_up':'The road network','TUR_Factory_1':'Working conditions','TUR_Factory_5':'Machine-tool purchases','TUR_Army_Factory_1':'Army factories','TUR_civ_factory_1':'Civilian factories','TUR_civ_factory_2':'Civilian factory expansion','TUR_new_order':'Industrial administration',
 'TUR_Factory_3':'Privatisation','TUR_Factory_6':'The world market','TUR_capitalism_1':'Private industrial policy','TUR_capitalism_4':'Attract investors','TUR_capitalism_2':'The national trade fund','TUR_capitalism_3':'Fund trade expansion','TUR_capitalism_5':'The industrial technology institute','TUR_capitalism_6':'Gold-backed credit',
 'TUR_Factory_4':'Nationalisation','TUR_Factory_7':'The public holding system','TUR_nationalist_1':'Economic security','TUR_nationalist_3':'The national industrial council','TUR_nationalist_2':'Expand the public holding','TUR_nationalist_4':'Imperial cultural cohesion','TUR_nationalist_5':'Develop strategic resources','TUR_nationalist_6':'The state distribution network',
 'TUR_Army_1':'Accept the supply reform','TUR_Army_2':'Independent army procurement','TUR_Army_3':'The Ottoman army','TUR_Infantry_1':'Modern infantry equipment','TUR_Doctrine_1':'Doctrine development','TUR_Artillery_1':'Artillery development','TUR_Army_4':'Combined-arms training','TUR_Army_6':'Advanced doctrine study','TUR_Army_5':'Motor transport','TUR_Army_8':'Tank development','TUR_Army_7':'Military towns',
 'TUR_air_2':'Fighters','TUR_air_3':'Ground-attack aviation','TUR_air_4':'Bombers','TUR_air_5':'Air-base expansion','TUR_air_6':'The aviation school','TUR_air_7':'The national aviation programme',
 'TUR_war_with_bulgaria':'Pressure on Bulgaria','afg_bolgi':'Administer the Bulgarian territories','TUR_snova_copi':'Pressure on Greece',
 'TUR_Army_Factory_2':'Army factory expansion','TUR_infrastructure_up_2':'Industrial network expansion','TUR_research_1':'Ankara University','TUR_research_2':'The university network','TUR_rocketly_1':'Rocket testing','TUR_nuclear_1':'The Ankara atomic project','TUR_supereq_1':'The Ottoman scientific programme'}
positions={
 'TUR_political_rw':(8,0),'TUR_new_fascism':(2,1),'TUR_not_fascism':(6,1),'TUR_new_dem':(10,1),'TUR_new_communism':(14,1),'TUR_set_capital':(2,2),'TUR_dux_national':(2,3),'tur_bred':(6,2),'tur_polos':(6,3),'TUR_proper_stoper':(2,4),'TUR_store_eng':(6,4),'TUR_kosa_smerti':(2,5),'TUR_war_with_bulgaria':(2,6),'afg_bolgi':(2,7),'TUR_snova_copi':(2,8),
 'TUR_prom':(26,0),'TUR_new_economic':(26,1),'TUR_resourse_icons':(24,2),'TUR_Infrastructure_up':(28,2),'TUR_Factory_2':(24,3),'TUR_Factory_1':(28,3),'TUR_Factory_5':(26,4),'TUR_civ_factory_1':(24,5),'TUR_Army_Factory_1':(28,5),'TUR_civ_factory_2':(24,6),'TUR_Army_Factory_2':(28,6),'TUR_infrastructure_up_2':(26,7),
 'TUR_new_order':(20,2),'TUR_Factory_3':(18,3),'TUR_Factory_4':(22,3),'TUR_Factory_6':(18,4),'TUR_Factory_7':(22,4),'TUR_capitalism_1':(16,5),'TUR_capitalism_2':(18,5),'TUR_nationalist_1':(22,5),'TUR_nationalist_2':(24,5),'TUR_capitalism_4':(16,6),'TUR_capitalism_3':(18,6),'TUR_nationalist_3':(22,6),'TUR_nationalist_4':(24,6),'TUR_capitalism_5':(17,7),'TUR_nationalist_5':(23,7),'TUR_capitalism_6':(17,8),'TUR_nationalist_6':(23,8),
 'TUR_research_1':(34,0),'TUR_research_2':(34,1),'TUR_rocketly_1':(33,2),'TUR_nuclear_1':(35,2),'TUR_supereq_1':(34,3),
 'TUR_reform_the_army':(42,0),'TUR_Army_1':(40,1),'TUR_Army_2':(44,1),'TUR_Army_3':(42,2),'TUR_Infantry_1':(40,3),'TUR_Doctrine_1':(42,3),'TUR_Artillery_1':(44,3),'TUR_Army_4':(42,4),'TUR_Army_5':(40,5),'TUR_Army_6':(42,5),'TUR_Army_8':(44,5),'TUR_Army_7':(42,6),
 'TUR_air_1':(50,0),'TUR_air_2':(48,1),'TUR_air_3':(50,1),'TUR_air_4':(52,1),'TUR_air_5':(50,2),'TUR_air_6':(50,3),'TUR_air_7':(50,4)}
# Give each economic model its own lane without colliding with the factory chain.
for fid in ['TUR_nationalist_2','TUR_nationalist_4']:positions[fid]=(21,positions[fid][1])
for fid in ['TUR_nationalist_1','TUR_nationalist_3']:positions[fid]=(23,positions[fid][1])
for fid in ['TUR_civ_factory_1','TUR_civ_factory_2']:positions[fid]=(27,positions[fid][1])
for fid in ['TUR_Army_Factory_1','TUR_Army_Factory_2']:positions[fid]=(29,positions[fid][1])
rewards={
 'TUR_political_rw':'add_political_power = 100','TUR_prom':build()+tech('industry')+' nww_legacy_TUR_industry_step = yes',
 'TUR_new_economic':build()+tech('industry')+' nww_legacy_TUR_industry_step = yes',
 'TUR_resourse_icons':resource(49,'steel',8)+resource(49,'coal',6),
 'TUR_Factory_2':build()+' nww_legacy_TUR_industry_step = yes',
 'TUR_Infrastructure_up':'49 = { if = { limit = { is_owned_and_controlled_by = ROOT infrastructure < 5 } add_building_construction = { type = infrastructure level = 1 instant_build = yes } } }',
 'TUR_Factory_1':'add_timed_idea = { idea = TUR_factory_idea_1 days = 365 } nww_legacy_TUR_industry_step = yes',
 'TUR_Factory_5':build('arms_factory')+' add_ideas = TUR_factory_idea_2 nww_legacy_TUR_industry_step = yes',
 'TUR_civ_factory_1':build()+' nww_legacy_TUR_industry_step = yes','TUR_civ_factory_2':build()+' nww_legacy_TUR_industry_step = yes',
 'TUR_Army_Factory_1':build('arms_factory')+' nww_legacy_TUR_industry_step = yes','TUR_Army_Factory_2':build('arms_factory')+' nww_legacy_TUR_industry_step = yes',
 'TUR_infrastructure_up_2':build()+' nww_legacy_TUR_industry_step = yes',
 'TUR_new_order':'add_political_power = 50 '+tech('industry'),
 'TUR_Factory_3':'add_ideas = TUR_capitalism_economic_1 '+build(),
 'TUR_Factory_6':'swap_ideas = { remove_idea = TUR_capitalism_economic_1 add_idea = TUR_capitalism_economic_2 } '+tech('industry'),
 'TUR_capitalism_1':'swap_ideas = { remove_idea = TUR_capitalism_economic_2 add_idea = TUR_capitalism_economic_3 } '+build(),
 'TUR_capitalism_2':'add_ideas = TUR_NFT_1','TUR_capitalism_3':'swap_ideas = { remove_idea = TUR_NFT_1 add_idea = TUR_NFT_2 }',
 'TUR_capitalism_4':build(),'TUR_capitalism_5':'add_ideas = TUR_IPT_1 '+tech('electronics'),
 'TUR_capitalism_6':'add_timed_idea = { idea = TUR_gold_1 days = 730 }',
 'TUR_Factory_4':'add_ideas = TUR_national_economic_1 '+build('arms_factory'),
 'TUR_Factory_7':'add_ideas = TUR_TAS_1','TUR_nationalist_1':tech('industry'),
 'TUR_nationalist_2':'swap_ideas = { remove_idea = TUR_TAS_1 add_idea = TUR_TAS_2 }',
 'TUR_nationalist_3':'add_ideas = TUR_NNSP_1 swap_ideas = { remove_idea = TUR_national_economic_1 add_idea = TUR_national_economic_2 }',
 'TUR_nationalist_4':'add_ideas = TUR_religion_1',
 'TUR_nationalist_5':resource(49,'tungsten',4)+' swap_ideas = { remove_idea = TUR_national_economic_2 add_idea = TUR_national_economic_3 }',
 'TUR_nationalist_6':'swap_ideas = { remove_idea = TUR_national_economic_3 add_idea = TUR_national_economic_4 }',
 'TUR_new_fascism':politics('fascism')+' add_ideas = tur_fascism_d add_war_support = 0.05',
 'TUR_not_fascism':politics('neutrality')+' add_ideas = tur_not_fascism_d',
 'TUR_new_dem':politics('democratic')+' add_ideas = tur_new_democ',
 'TUR_new_communism':politics('communism')+' add_ideas = tur_comun_d',
 'TUR_set_capital':'set_capital = { state = 797 }','TUR_dux_national':'add_stability = 0.05 add_war_support = 0.05',
 'tur_bred':'add_stability = 0.05 add_political_power = 50','tur_polos':'set_politics = { ruling_party = neutrality elections_allowed = yes } add_stability = 0.05',
 'TUR_proper_stoper':'army_experience = 20 add_command_power = 15','TUR_store_eng':foreign('ENG'),
 'TUR_kosa_smerti':'add_war_support = 0.05 add_state_claim = 48 add_state_claim = 184',
 'TUR_war_with_bulgaria':goal('BUL'),'TUR_snova_copi':goal('GRE'),
 'afg_bolgi':build(state=48)+' if = { limit = { 48 = { is_owned_and_controlled_by = ROOT } } add_state_core = 48 }',
 'TUR_reform_the_army':doctrine('land_doctrine')+' army_experience = 15 nww_legacy_TUR_army_step = yes',
 'TUR_Army_1':'add_ideas = TUR_supply_reform','TUR_Army_2':'add_ideas = TUR_disagree_reform',
 'TUR_Army_3':tech('infantry_weapons')+' army_experience = 15','TUR_Infantry_1':tech('infantry_weapons'),
 'TUR_Doctrine_1':doctrine('land_doctrine'),'TUR_Artillery_1':tech('artillery'),
 'TUR_Army_4':'add_ideas = TUR_universal_army_1 army_experience = 20',
 'TUR_Army_5':tech('motorized_equipment'),'TUR_Army_6':doctrine('land_doctrine'),'TUR_Army_8':tech('armor'),
 'TUR_Army_7':'add_ideas = tur_closed_cities_1 army_experience = 20',
 'TUR_air_1':tech('light_air'),'TUR_air_2':tech('light_air',2),'TUR_air_3':tech('cas_bomber'),
 'TUR_air_4':tech('medium_air'),'TUR_air_5':'capital_scope = { if = { limit = { air_base < 8 } add_building_construction = { type = air_base level = 2 instant_build = yes } } } air_experience = 15',
 'TUR_air_6':doctrine('air_doctrine'),'TUR_air_7':'add_ideas = TUR_TNPA_1 air_experience = 15',
 'TUR_research_1':slot(),'TUR_research_2':slot(),'TUR_rocketly_1':tech('rocketry'),
 'TUR_nuclear_1':tech('nuclear'),'TUR_supereq_1':'add_ideas = tur_dominatuim_turco_1 '+tech('electronics')}
for source in values(t.source,'focus'):
    fid=one(source,'id');parents=[values(g,'focus') for g in values(source,'prerequisite')]
    parents=[p[0] if len(p)==1 else p for p in parents]
    if fid=='TUR_research_1':parents=[]
    if fid=='TUR_Factory_6':parents=['TUR_Factory_3']
    if fid=='TUR_proper_stoper':parents=[['TUR_dux_national','tur_polos']]
    reward=rewards[fid]
    if fid.startswith('TUR_Army_') and not 'Factory' in fid:reward+=' nww_legacy_TUR_army_step = yes'
    if fid in ['TUR_Infantry_1','TUR_Doctrine_1','TUR_Artillery_1']:reward+=' nww_legacy_TUR_army_step = yes'
    exclusive=[v for g in values(source,'mutually_exclusive') for v in values(g,'focus')]
    available=''
    if fid in ['TUR_new_fascism','TUR_not_fascism','TUR_new_dem','TUR_new_communism']:available=mandate(dict(zip(['TUR_new_fascism','TUR_not_fascism','TUR_new_dem','TUR_new_communism'],['fascism','neutrality','democratic','communism']))[fid])
    if fid=='TUR_set_capital':available='797 = { is_owned_and_controlled_by = ROOT }'
    if fid=='TUR_store_eng':available=peaceful('ENG')
    if fid=='TUR_war_with_bulgaria':available=war('BUL')
    if fid=='TUR_snova_copi':available=war('GRE')
    if fid=='afg_bolgi':available='48 = { is_owned_and_controlled_by = ROOT }'
    if fid=='TUR_nuclear_1':available='date > 1938.1.1'
    if fid=='TUR_research_1':available='has_completed_focus = TUR_new_economic'
    desc=loc.get(fid+'_desc','')
    if not desc or any(s in desc.lower() for s in ['честно','фашист','золот','первой мировой','вернём','салат','смерт']):desc='Согласуем эту программу с учреждениями империи и обеспечим её ресурсами.'
    icon=one(source,'icon')
    if icon=='GFX_focus_SAF_colonialist_crusade':icon='GFX_focus_generic_army_attack'
    t.add(fid,*positions[fid],parents,reward,en=labels[fid],description=(desc,'Develop '+labels[fid].lower()+' as part of the empire\'s long-term programme.'),available=available,exclusive=exclusive,icon=icon,cost=10 if fid in ['TUR_supereq_1','TUR_Army_7','TUR_new_fascism','TUR_new_dem','TUR_new_communism'] else 5)
for fid,ru,en in [('TUR_not_fascism','Конституционный султанат','Constitutional sultanate'),('TUR_kosa_smerti','Балканская военная программа','Balkan military programme'),('TUR_snova_copi','Давление на Грецию','Pressure on Greece'),('TUR_store_eng','Европейские дипломатические миссии','European diplomatic missions'),('TUR_set_capital','Возвращение в Константинополь','Return to Constantinople')]:text(fid,ru,en)
for fid,x,parent,ru,en,rew in [
 ('NWW_TUR_civil_assembly',10,'TUR_new_dem','Гражданское собрание','Civil assembly','add_political_power = 50 add_stability = 0.05'),
 ('NWW_TUR_federal_charter',10,'NWW_TUR_civil_assembly','Федеральная хартия','Federal charter','add_ideas = NWW_TUR_federal_constitution'),
 ('NWW_TUR_workers_congress',14,'TUR_new_communism','Съезд рабочих советов','Workers congress','add_political_power = 50 add_stability = 0.05'),
 ('NWW_TUR_workers_union',14,'NWW_TUR_workers_congress','Союз республик труда','Union of labour republics','add_ideas = NWW_TUR_workers_federation')]:
    t.add(fid,x,2 if 'assembly' in fid or 'congress' in fid else 3,[parent],rew,ru,en)
t.finish()

# Austria: retain all ten NWW IDs and all fifteen archive IDs.
a=Tree('AUS','common/national_focus/austria.txt','AUS_gnida.txt')
rows=[
 ('AUS_nww_rebuild',8,0,[], 'add_political_power = 75','Обновить государство','Renew the state'),
 ('AUS_political_power',4,1,['AUS_nww_rebuild'],'add_political_power = 100 add_stability = 0.05','Австрийские реформы','Austrian reforms'),
 ('AUS_reinstate_the_imperial_council',2,2,['AUS_political_power'],politics('neutrality'),'Имперский совет','The imperial council'),
 ('AUS_hold_elections',6,2,['AUS_political_power'],politics('democratic'),'Парламентский мандат','A parliamentary mandate'),
 ('AUS_the_danubian_federation',2,3,[['AUS_reinstate_the_imperial_council','AUS_hold_elections']],foreign('HUN',3),'Дунайское соглашение','The Danubian agreement'),
 ('AUS_via_danube_to_europe',2,4,['AUS_the_danubian_federation'],tech('industry')+build(),'Через Дунай в Европу','Via the Danube to Europe'),
 ('AUS_not_germany',6,3,[['AUS_reinstate_the_imperial_council','AUS_hold_elections']],'add_stability = 0.05 add_political_power = 50','Самостоятельный австрийский курс','An independent Austrian course'),
 ('AUS_join_to_axis',6,4,['AUS_not_germany'],foreign('GER'),'Германская техническая миссия','German technical mission'),
 ('AUS_help_from_eng',8,5,['AUS_not_germany'],foreign('FRA'),'Французские промышленные связи','French industrial ties'),
 ('AUS_war_with_hun',4,4,['AUS_not_germany'],goal('HUN'),'Венгерский ультиматум','The Hungarian ultimatum'),
 ('AUS_war_with_croatia',4,5,['AUS_war_with_hun'],goal('CRO'),'Хорватский вопрос','The Croatian question'),
 ('AUS_reclaiming_yugoslavian_territories',4,6,['AUS_war_with_croatia'],'add_war_support = 0.05 add_state_claim = 109','Адриатические претензии','Adriatic claims'),
 ('AUS_nww_army',12,1,['AUS_nww_rebuild'],'army_experience = 15','Обновить командование','Renew the command'),
 ('AUS_army_expierience',12,2,['AUS_nww_army'],doctrine('land_doctrine'),'Австрийский военный дух','Austrian military spirit'),
 ('AUS_bring_generals_out_of_retirement',12,3,['AUS_army_expierience'],'army_experience = 20 add_command_power = 15','Вернуть опытных офицеров','Recall experienced officers'),
 ('AUS_establish_bohme_plan',12,4,['AUS_bring_generals_out_of_retirement'],tech('infantry_weapons')+tech('artillery'),'План модернизации Бёме','Bohme modernisation plan'),
 ('AUS_nww_industry',18,1,['AUS_nww_rebuild'],tech('industry'),'Производственная программа','Production programme'),
 ('aus_prom',16,2,['AUS_nww_industry'],build()+' remove_ideas = AUS_recovering_from_the_depression','Промышленность','Industrial investment'),
 ('aus_prom_2',16,3,['aus_prom'],build('arms_factory')+' remove_ideas = AUS_widespread_unemployment','Рабочие места','Industrial employment'),
 ('aus_prom_3',16,4,['aus_prom_2'],build(),'Индустриализация','Industrialisation'),
 ('aus_prom_4',15,5,['aus_prom_3'],build('arms_factory'),'Военная мощь','Military production'),
 ('aus_prom_5',17,5,['aus_prom_3'],build(),'Фабрики для народа','Factories for the people'),
 ('AUS_new_economic',20,2,['AUS_nww_industry'],build('arms_factory'),'Новая экономика','A new economy'),
 ('AUS_reform_the_economic',20,3,['AUS_new_economic'],resource(4,'steel',8)+' remove_ideas = AUS_phonix_insurance','Новая валюта','Currency reform'),
 ('AUS_create_a_new_econimic',20,4,['AUS_reform_the_economic'],'add_ideas = NWW_AUS_currency '+slot(),'Обеспечить шиллинг','Back the schilling'),
]
for fid,x,y,parents,reward,ru,en in rows:
    avail='';exclusive=[]
    if fid=='AUS_reinstate_the_imperial_council':avail=mandate('neutrality');exclusive=['AUS_hold_elections']
    if fid=='AUS_hold_elections':avail=mandate('democratic');exclusive=['AUS_reinstate_the_imperial_council']
    if fid=='AUS_the_danubian_federation':avail=peaceful('HUN');exclusive=['AUS_war_with_hun']
    if fid=='AUS_war_with_hun':avail=war('HUN');exclusive=['AUS_the_danubian_federation']
    if fid=='AUS_war_with_croatia':avail=war('CRO')
    if fid=='AUS_join_to_axis':avail=peaceful('GER')
    if fid=='AUS_help_from_eng':avail=peaceful('FRA')
    if fid=='AUS_via_danube_to_europe':avail='has_country_flag = NWW_danubian_agreement'
    desc=('Согласуем реформу с представителями земель и направим ресурсы на укрепление австрийского государства.','Coordinate the reform with the provinces and invest in the Austrian state.')
    if fid in ['aus_prom','aus_prom_2','aus_prom_3','aus_prom_4','aus_prom_5','AUS_new_economic']:desc=('Расширим действующие предприятия и создадим рабочие места на контролируемой территории Австрии.','Expand operating enterprises and create jobs on Austrian-controlled territory.')
    if fid in ['AUS_the_danubian_federation','AUS_join_to_axis','AUS_help_from_eng']:desc=('Предложим партнёру договор. Сотрудничество начнётся только после его согласия; независимость участников сохраняется.','Offer a treaty to our partner. Cooperation requires their consent and preserves the participants\' independence.')
    icon='GFX_focus_generic_diplomatic_treaty'
    if fid in ('AUS_nww_rebuild','AUS_reinstate_the_imperial_council'):icon='GFX_focus_generic_support_the_left_right'
    if fid=='AUS_hold_elections':icon='GFX_focus_research'
    if fid in ('AUS_war_with_hun','AUS_war_with_croatia','AUS_reclaiming_yugoslavian_territories'):icon='GFX_focus_generic_army_attack'
    if fid in ('AUS_nww_army','AUS_army_expierience','AUS_bring_generals_out_of_retirement'):icon='GFX_focus_generic_military_academy'
    if fid=='AUS_establish_bohme_plan':icon='GFX_goal_generic_army_artillery'
    if fid in ('AUS_nww_industry','aus_prom','aus_prom_3','aus_prom_5'):icon='GFX_focus_generic_industry_1'
    if fid in ('aus_prom_2','aus_prom_4','AUS_new_economic'):icon='GFX_focus_generic_industry_2'
    if fid in ('AUS_reform_the_economic','AUS_create_a_new_econimic'):icon='GFX_focus_research2'
    a.add(fid,x,y,parents,reward,ru,en,desc,avail,exclusive,icon=icon)
a.finish()

# Afghanistan: preserve the fourteen archive IDs, repair the diplomatic route.
f=Tree('AFG','common/national_focus/afghanistan.txt','AFG_style.txt')
rows=[
 ('AFG_nww_council',6,0,[],'add_political_power = 75','Совет при дворе','The royal council'),
 ('AFG_new_political',4,1,['AFG_nww_council'],'add_stability = 0.05 add_political_power = 50','Реформа правительства','Government reform'),
 ('AFG_not_new_political_power',8,1,['AFG_nww_council'],'add_war_support = 0.05 add_political_power = 50','Сохранить власть двора','Retain royal authority'),
 ('AFG_remove_borders',8,2,[['AFG_new_political','AFG_not_new_political_power']],build('arms_factory')+' add_war_support = 0.05','Закрыть границы','Close the borders'),
 ('AFG_give_free',4,2,['AFG_new_political'],politics('democratic')+' add_stability = 0.05','Гражданские свободы','Civil liberties'),
 ('AFG_industrial_1',6,3,[['AFG_give_free','AFG_remove_borders']],build()+tech('industry')+slot()+' set_country_flag = NWW_AFG_industry_complete nww_legacy_AFG_economic_step = yes','Индустриализация','Industrialisation'),
 ('AFG_ready_the_army',6,4,['AFG_industrial_1'],doctrine('land_doctrine')+slot()+' army_experience = 20','Реформа армии','Army reform'),
 ('AFG_crush_soviet',4,5,['AFG_ready_the_army','AFG_remove_borders'],goal('SOV'),'Давление на советскую границу','Pressure on the Soviet frontier'),
 ('AFG_good_friend',8,5,['AFG_ready_the_army'],foreign('SOV'),'Переговоры с Москвой','Talks with Moscow'),
 ('afg_tashkent',6,6,[['AFG_crush_soviet','AFG_good_friend']],tech('industry')+' add_political_power = 50','Ташкентский договор','The Tashkent agreement'),
 ('afg_usa',4,7,['afg_tashkent'],foreign('USA'),'Американское сотрудничество','American cooperation'),
 ('afg_ussr',8,7,['afg_tashkent'],politics('communism')+foreign('SOV'),'Советский курс','The Soviet course'),
 ('afg_site',14,0,[],build(),'Промышленный концерн','Industrial concern'),
 ('afg_anon_ussr',14,1,['afg_site'],build('arms_factory')+tech('industry'),'Расширить мастерские','Expand the workshops'),
 ('afg_invest_usa',14,2,['afg_anon_ussr'],build()+slot()+' set_country_flag = NWW_AFG_institute_complete nww_legacy_AFG_economic_step = yes','Технический институт','Technical institute'),
]
for fid,x,y,parents,reward,ru,en in rows:
    exclusive=[];avail=''
    pairs=[('AFG_new_political','AFG_not_new_political_power'),('AFG_remove_borders','AFG_give_free'),('AFG_crush_soviet','AFG_good_friend'),('afg_usa','afg_ussr')]
    for left,right in pairs:
        if fid==left:exclusive=[right]
        if fid==right:exclusive=[left]
    if fid=='AFG_give_free':avail=mandate('democratic')
    if fid=='afg_ussr':avail=mandate('communism')+' '+peaceful('SOV')
    if fid=='AFG_crush_soviet':avail=war('SOV')
    if fid=='AFG_good_friend':avail=peaceful('SOV')
    if fid=='afg_usa':avail=peaceful('USA')
    if fid=='afg_tashkent':avail='OR = { has_country_flag = NWW_foreign_contract 405 = { is_owned_and_controlled_by = ROOT } } NOT = { has_war_with = SOV }'
    desc=('Двор, провинциальные советы и новые учреждения согласуют программу развития независимого Афганистана.','The court, provincial councils and new institutions coordinate development for an independent Afghanistan.')
    if fid=='afg_tashkent':desc=('Мирный договор откроет торговлю и технический обмен. Ташкент не передаётся нам автоматически: территориальное решение зависит от результата войны.','A peaceful agreement opens trade and technical exchange. Territorial settlements depend on the outcome of war.')
    f.add(fid,x,y,parents,reward,ru,en,desc,avail,exclusive)
f.finish()
effects.extend(parse('''nww_legacy_AFG_economic_step = {
 if = { limit = { has_dynamic_modifier = { modifier = AFG_subsistence_economy_modifier } }
   if = { limit = { has_country_flag = NWW_AFG_industry_complete has_country_flag = NWW_AFG_institute_complete }
     remove_dynamic_modifier = { modifier = AFG_subsistence_economy_modifier }
   } else = {
     set_variable = { AFG_economy_production_efficiency_gain_factor = -0.25 }
     set_variable = { AFG_economy_production_max_efficiency_factor = -0.20 }
     set_variable = { AFG_economy_industrial_capacity_factor = -0.25 }
   }
 }
}'''))

# Germany: preserve its seven existing NWW focuses and add all ten old industry IDs.
g=Tree('GER','common/national_focus/ger_focus.txt','german_focus.txt')
existing=values(one(read(ROOT/('common/national_focus/GER_focuses.txt' if (ROOT/'common/national_focus/GER_focuses.txt').exists() else 'common/national_focus/ger_focus.txt')),'focus_tree'),'focus')
current_loc={}
for p in ROOT.glob('localisation/*l_russian.yml'):current_loc.update(re.findall(r'^\s+([\w.]+):\d*\s+"(.*)"\s*$',p.read_text(encoding='utf-8-sig'),re.M))
positions_g={'GER_the_kaiser_endures':(5,0),'GER_prussian_traditions':(3,1),'GER_guardians_of_the_reich':(7,1),'GER_the_eastern_question':(3,2),'GER_krupp_and_thyssen':(13,0),'GER_mitteleuropa_trade':(18,1),'GER_the_fleet_question':(23,0)}
for node in existing:
    fid=one(node,'id')
    if fid in {one(f,'id') for f in values(g.source,'focus')}:continue
    new=copy.deepcopy(node);x,y=positions_g[fid];setv(new,'x',str(x));setv(new,'y',str(y))
    if fid=='GER_krupp_and_thyssen':new[:]=[(k,v,o) for k,v,o in new if k!='prerequisite']
    if fid=='GER_the_fleet_question':setv(new,'completion_reward',parse(doctrine('naval_doctrine')+' navy_experience = 15'));new[:]=[(k,v,o) for k,v,o in new if k!='prerequisite']
    if fid=='GER_mitteleuropa_trade':setv(new,'completion_reward',parse(build()+' add_political_power = 50'))
    g.nodes[fid]=new;text(fid,current_loc.get(fid,fid),fid.replace('GER_','').replace('_',' ').title());text(fid+'_desc',current_loc.get(fid+'_desc','Укрепим государственные и производственные учреждения империи.'),'Strengthen the imperial institutions and production system.')
english_g=['Ruhr coal','Colonial resources','Eastern industrial development','Military technology','Economic development','Industrial subsidies','Production consolidation','Integrated industrial plan','New enterprises','Automatic weapons']
reward_g=[resource(42,'coal',8),resource(546,'rubber',8)+resource(541,'chromium',6),build('arms_factory'),build('arms_factory')+tech('infantry_weapons'),build(),build(),build()+' add_ideas = NWW_GER_quality',build()+slot(),build('arms_factory'),tech('infantry_weapons',2)]
for source in values(g.source,'focus'):
    fid=one(source,'id');i=int(fid.split('_')[1])-1
    parents=[values(p,'focus') for p in values(source,'prerequisite')];parents=[p[0] if len(p)==1 else p for p in parents]
    if fid=='GER_1':parents=['GER_krupp_and_thyssen']
    g.add(fid,int(one(source,'x'))*2+9,int(one(source,'y'))+1,parents,reward_g[i],en=english_g[i],description=('Расширим сырьевую базу и действующие предприятия империи. Разработка ресурсов за её пределами возможна только на собственных контролируемых землях.','Expand the empire\'s resources and operating enterprises. Overseas deposits can be developed only on owned and controlled territory.'),icon=one(source,'icon'))
g.finish()

# Hungary has no archive tree: expand the existing NWW IDs around the Danube.
h=Tree('HUN','common/national_focus/hungary.txt')
rows=[
 ('HUN_nww_rebuild',6,0,[],'add_political_power = 75','Обновить государственные учреждения','Renew state institutions'),
 ('HUN_elect_a_king',6,1,['HUN_nww_rebuild'],'add_political_power = 50','Обсудить будущее короны','Debate the crown\'s future'),
 ('HUN_elect_a_democratic_king',2,2,['HUN_elect_a_king'],politics('democratic'),'Парламентская монархия','Parliamentary monarchy'),
 ('HUN_invite_the_habsburg_prince',6,2,['HUN_elect_a_king'],politics('neutrality')+' promote_character = HUN_otto_von_habsburg','Пригласить Габсбурга','Invite a Habsburg'),
 ('HUN_elect_a_fascist_king',10,2,['HUN_elect_a_king'],politics('fascism'),'Национальная власть','National government'),
 ('HUN_proclaim_the_restoration_of_austria_hungary',6,3,['HUN_invite_the_habsburg_prince'],foreign('AUS',3),'Предложить Дунайский союз','Propose the Danubian union'),
 ('HUN_protect_czechoslovakia',6,4,['HUN_proclaim_the_restoration_of_austria_hungary'],tech('industry')+' add_stability = 0.05','Дунайские торговые гарантии','Danubian trade guarantees'),
 ('NWW_HUN_sovereign_parliament',2,3,['HUN_elect_a_democratic_king'],'add_stability = 0.05 add_political_power = 50','Суверенный парламент','Sovereign parliament'),
 ('NWW_HUN_national_defence',10,3,['HUN_elect_a_fascist_king'],'add_war_support = 0.05 army_experience = 20','Национальная оборона','National defence'),
 ('HUN_nww_army',16,0,[],'army_experience = 15','Военная программа','Military programme'),
 ('NWW_HUN_officer_school',16,1,['HUN_nww_army'],doctrine('land_doctrine'),'Офицерское училище','Officer school'),
 ('NWW_HUN_artillery',15,2,['NWW_HUN_officer_school'],tech('artillery'),'Венгерская артиллерия','Hungarian artillery'),
 ('NWW_HUN_motorisation',17,2,['NWW_HUN_officer_school'],tech('motorized_equipment'),'Моторизация резерва','Reserve motorisation'),
 ('NWW_HUN_manoeuvres',16,3,['NWW_HUN_artillery','NWW_HUN_motorisation'],'army_experience = 25','Совместные учения','Combined exercises'),
 ('HUN_nww_industry',24,0,[],tech('industry'),'Промышленный план','Industrial plan'),
 ('NWW_HUN_ganz',22,1,['HUN_nww_industry'],build(),'Предприятия Ганц','Ganz enterprises'),
 ('NWW_HUN_weiss',26,1,['HUN_nww_industry'],build('arms_factory'),'Заводы Вейсса','Weiss works'),
 ('NWW_HUN_railways',22,2,['NWW_HUN_ganz'],build(),'Железнодорожные мастерские','Railway workshops'),
 ('NWW_HUN_machine_tools',26,2,['NWW_HUN_weiss'],'add_ideas = NWW_HUN_workshops '+tech('industry'),'Стандартизация станков','Machine-tool standards'),
 ('NWW_HUN_technical_university',24,3,['NWW_HUN_railways','NWW_HUN_machine_tools'],slot(),'Будапештский технический институт','Budapest technical institute'),
 ('NWW_HUN_research_network',24,4,['NWW_HUN_technical_university'],slot(),'Университетская сеть','University network'),
]
political=['HUN_elect_a_democratic_king','HUN_invite_the_habsburg_prince','HUN_elect_a_fascist_king']
for fid,x,y,parents,reward,ru,en in rows:
    avail='';exclusive=[]
    if fid in political:avail=mandate(dict(zip(political,['democratic','neutrality','fascism']))[fid]);exclusive=[p for p in political if p!=fid]
    if fid=='HUN_proclaim_the_restoration_of_austria_hungary':avail=peaceful('AUS')
    if fid=='HUN_protect_czechoslovakia':avail='has_country_flag = NWW_danubian_agreement'
    h.add(fid,x,y,parents,reward,ru,en,('Согласуем программу с венгерскими учреждениями. Дунайское сотрудничество сохраняет независимость участников и требует их согласия.','Coordinate the programme with Hungarian institutions. Danubian cooperation preserves independence and requires the participants\' consent.'),avail,exclusive)
h.finish()

# Consent-based foreign contracts and a bilateral Danubian research network.
text('NWW_foreign_contract','Промышленный договор принят партнёром','The partner accepted an industrial contract')
text('NWW_danubian_agreement','Дунайское соглашение принято обеими странами','Both countries accepted the Danubian agreement')
text('NWW_legacy_trade','Промышленное сотрудничество','Industrial cooperation')
save('common/opinion_modifiers/nww_legacy_opinions.txt',parse('opinion_modifiers = { NWW_legacy_trade = { value = 30 days = 1095 } }'))
save('common/technology_sharing/nww_legacy_research.txt',parse('technology_sharing_group = { id = NWW_Danubian_research name = NWW_Danubian_research_name desc = NWW_Danubian_research_desc picture = GFX_technology_sharing_default research_sharing_per_country_bonus = 0.05 available = { OR = { tag = AUS tag = HUN } AUS = { exists = yes has_country_flag = NWW_danubian_agreement } HUN = { exists = yes has_country_flag = NWW_danubian_agreement } NOT = { AUS = { has_war_with = HUN } } } }'))
text('NWW_Danubian_research_name','Дунайская исследовательская сеть','Danubian research network')
text('NWW_Danubian_research_desc','Австрия и Венгрия обмениваются исследованиями на основе добровольного договора. Во время войны между участниками обмен не действует.','Austria and Hungary share research under a voluntary treaty. Cooperation stops during a war between the participants.')
events=parse('add_namespace = nww_legacy')
events.extend(parse(f'''country_event = {{ id = nww_legacy.1 title = nww_legacy.1.t desc = nww_legacy.1.d picture = GFX_report_event_election_vote is_triggered_only = yes
 option = {{ name = nww_legacy.1.a trigger = {{ FROM = {{ exists = yes is_subject = no has_political_power > 49 NOT = {{ has_war_with = ROOT }} }} }}
   FROM = {{ add_political_power = -50 set_country_flag = NWW_foreign_contract {tech('industry')} {build('arms_factory')} country_event = {{ id = nww_legacy.2 days = 1 }} }}
   if = {{ limit = {{ tag = GER FROM = {{ tag = AUS }} }} FROM = {{ {slot()} }} }}
   add_opinion_modifier = {{ target = FROM modifier = NWW_legacy_trade }} ai_chance = {{ factor = 60 }} }}
 option = {{ name = nww_legacy.1.b FROM = {{ if = {{ limit = {{ exists = yes }} country_event = {{ id = nww_legacy.4 days = 1 }} }} }} ai_chance = {{ factor = 40 }} }}
}}'''))
events.extend(parse('country_event = { id = nww_legacy.2 title = nww_legacy.2.t desc = nww_legacy.2.d picture = GFX_report_event_election_vote is_triggered_only = yes option = { name = nww_legacy.2.a } }'))
events.extend(parse('''country_event = { id = nww_legacy.3 title = nww_legacy.3.t desc = nww_legacy.3.d picture = GFX_report_event_election_vote is_triggered_only = yes
 option = { name = nww_legacy.3.a trigger = { is_subject = no NOT = { has_war_with = FROM } FROM = { exists = yes is_subject = no } }
 set_country_flag = NWW_danubian_agreement FROM = { set_country_flag = NWW_danubian_agreement add_to_tech_sharing_group = NWW_Danubian_research }
 add_to_tech_sharing_group = NWW_Danubian_research add_opinion_modifier = { target = FROM modifier = NWW_legacy_trade }
 FROM = { country_event = { id = nww_legacy.5 days = 1 } } ai_chance = { factor = 70 } }
 option = { name = nww_legacy.3.b FROM = { if = { limit = { exists = yes } country_event = { id = nww_legacy.4 days = 1 } } } ai_chance = { factor = 30 } }
}'''))
for number in [4,5]:events.extend(parse(f'country_event = {{ id = nww_legacy.{number} title = nww_legacy.{number}.t desc = nww_legacy.{number}.d picture = GFX_report_event_election_vote is_triggered_only = yes option = {{ name = nww_legacy.{number}.a }} }}'))
save('events/nww_legacy_diplomacy.txt',events)
event_text={
 '1.t':('Предложение промышленного сотрудничества','Industrial cooperation proposal'),
 '1.d':('Государство [FROM.GetName] предлагает оплатить техническую миссию и поставку оборудования. Согласие позволит партнёру открыть военное предприятие и освоить новые производственные методы.','[FROM.GetName] offers to pay for a technical mission and equipment deliveries. Acceptance helps the partner establish a military enterprise and learn new production methods.'),
 '1.a':('Согласиться на контракт','Accept the contract'),'1.b':('Отклонить предложение','Decline the proposal'),
 '2.t':('Промышленный договор принят','Industrial contract accepted'),'2.d':('Партнёр одобрил техническую миссию. Оплаченное оборудование направляется на строительство предприятия, а специалисты приступают к передаче производственных знаний.','Our partner approved the technical mission. Paid equipment will support factory construction and specialists will share production knowledge.'),'2.a':('Начать совместную программу','Begin the joint programme'),
 '3.t':('Дунайский научный договор','A Danubian research treaty'),'3.d':('Государство [FROM.GetName] предлагает совместную исследовательскую сеть. Участники сохранят собственные правительства, армии и территории.','[FROM.GetName] proposes a joint research network. Both participants retain their own governments, armies and territories.'),'3.a':('Подписать добровольное соглашение','Sign the voluntary agreement'),'3.b':('Сохранить отдельные программы','Keep separate programmes'),
 '4.t':('Предложение отклонено','Proposal declined'),'4.d':('Партнёр отказался от предлагаемого договора. Согласованные награды и совместные программы не вступят в силу.','Our partner declined the proposed treaty. Its rewards and joint programmes will not take effect.'),'4.a':('Продолжить самостоятельное развитие','Continue independent development'),
 '5.t':('Дунайский договор подписан','Danubian treaty signed'),'5.d':('Обе страны согласились на совместную исследовательскую сеть. Договор ускорит изучение технологий, уже известных другому участнику.','Both countries agreed to the research network. The treaty accelerates research into technologies already known to the other participant.'),'5.a':('Открыть научный обмен','Open the research exchange')}
for suffix,(ru,en) in event_text.items():text('nww_legacy.'+suffix,ru,en)

# Reusable timed political campaigns, retaining the 40% mandate rule.
campaigns=[];categories=[]
for tag,opening in [('TUR','TUR_political_rw'),('AFG','AFG_nww_council'),('AUS','AUS_nww_rebuild'),('HUN','HUN_nww_rebuild')]:
    category=f'NWW_{tag}_political_campaigns';text(category,'Политические кампании','Political campaigns');text(category+'_desc','Для смены государственного курса требуется поддержка соответствующей партии не менее 40%.','A change of course requires at least 40% popularity for the corresponding party.')
    categories.extend(parse(f'{category} = {{ icon = generic_political_actions visible = {{ tag = {tag} has_completed_focus = {opening} }} }}'))
    decisions=[]
    for ideology,ru,en in [('democratic','Республиканские собрания','Republican meetings'),('neutrality','Собрания сторонников короны','Royalist meetings'),('fascism','Национальные собрания','Nationalist meetings'),('communism','Рабочие собрания','Workers meetings')]:
        token=f'NWW_{tag}_campaign_{ideology}';text(token,ru,en);text(token+'_desc','Кампания стоит 50 политической власти, длится 60 дней и добавляет 10 процентных пунктов поддержки по завершении. Одновременно проводится одна кампания.','The campaign costs 50 political power, lasts 60 days and grants 10 percentage points of popularity on completion. Only one campaign may run at a time.')
        decisions.extend(parse(f'''{token} = {{ icon = generic_political_discourse allowed = {{ original_tag = {tag} }} visible = {{ tag = {tag} has_completed_focus = {opening} }}
         available = {{ {ideology} < 0.40 NOT = {{ has_country_flag = NWW_legacy_campaign_active }} }} cost = 50 days_remove = 60 days_re_enable = 15 fire_only_once = no
         complete_effect = {{ set_country_flag = NWW_legacy_campaign_active }}
         remove_effect = {{ add_popularity = {{ ideology = {ideology} popularity = 0.10 }} clr_country_flag = NWW_legacy_campaign_active }}
         cancel_trigger = {{ NOT = {{ tag = {tag} }} }} cancel_effect = {{ clr_country_flag = NWW_legacy_campaign_active }} ai_will_do = {{ factor = 0 }} }}'''))
    campaigns.append((category,decisions,'='))
text('NWW_legacy_campaign_active','Проводится другая политическая кампания','Another political campaign is in progress')
save('common/decisions/nww_legacy_campaigns.txt',campaigns);save('common/decisions/categories/nww_legacy_categories.txt',categories)

# Ottoman leaders and starting spirits from the archive, with modern physical setup.
characters=[]
for token,legacy,ru,en,ideology in [
 ('NWW_TUR_omar','omar_faruh_osmanoglu','Омер Фарук Османоглу','Omer Faruk Osmanoglu','despotism'),
 ('NWW_TUR_fatma','Fatma_Alie_Topuz','Фатма Алие Топуз','Fatma Aliye Topuz','conservatism'),
 ('NWW_TUR_hosnu','Shephik_Hosnu','Шефик Хюсню','Sefik Husnu','marxism'),
 ('NWW_TUR_fethi','Okayar_Ali_Fethi','Али Фетхи','Ali Fethi','fascism_ideology')]:
    source=OLD/f'gfx/leaders/TUR/Portrait_TUR_{legacy}.dds';relative=f'gfx/leaders/nww_legacy/Portrait_TUR_{legacy}.dds'
    (ROOT/relative).parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,ROOT/relative)
    sprite='GFX_Portrait_'+token; sprites.append(parse(f'name = {sprite} texturefile = "{relative}"'))
    characters.extend(parse(f'{token} = {{ name = {token} portraits = {{ civilian = {{ large = {sprite} }} }} country_leader = {{ ideology = {ideology} expire = "1965.1.1" }} }}'))
    text(token,ru,en)
save('common/characters/nww_legacy_TUR.txt',[('characters',characters,'=')])
physical={'capital','set_oob','oob','set_naval_oob','set_air_oob','set_technology','set_research_slots','set_stability','set_war_support','set_convoys','create_equipment_variant','set_equipment_fraction','add_equipment_to_stockpile','set_fuel_ratio','set_doctrine','add_doctrine','set_convoy_ratio'}
def physical_only(doc):
    result=[]
    for k,v,o in doc:
        if k in physical:result.append((k,v,o))
        elif k and k.lower() in ('if','else_if','else') and isinstance(v,list):
            nested=physical_only(v)
            if nested:
                if one(v,'limit') is not None:nested.insert(0,('limit',one(v,'limit'),'='))
                result.append((k,nested,o))
    return result
history=physical_only(read(GAME/'history/countries/TUR - Turkey.txt'))
history.extend(parse('set_politics = { ruling_party = neutrality elections_allowed = no } set_popularities = { democratic = 25 fascism = 14 communism = 16 neutrality = 45 } add_ideas = { tur_silly_army_nowar tur_agricultural_economic_1 }'))
for token in ['NWW_TUR_omar','NWW_TUR_fatma','NWW_TUR_hosnu','NWW_TUR_fethi']:history.append(('recruit_character',token,'='))
def adapt_native_characters(doc):
    result=[]
    for k,v,o in doc:
        if k=='country_leader':continue
        if isinstance(v,list):v=adapt_native_characters(v)
        if k=='has_completed_focus' and v in ('TUR_invite_german_officers_to_izmir','TUR_the_italo_turkish_naval_academy'):v='TUR_Army_3'
        if k=='advisor':
            gate={'army_chief':'TUR_Army_3','high_command':'TUR_Army_3','theorist':'TUR_Army_3','air_chief':'TUR_air_5'}.get(one(v,'slot'))
            setv(v,'available',parse('has_completed_focus = '+gate if gate else 'always = yes'))
            setv(v,'visible',parse('always = yes'))
        result.append((k,v,o))
    return result
native_chars=adapt_native_characters(one(read(GAME/'common/characters/TUR.txt'),'characters'))
save('common/characters/TUR.txt',[('characters',native_chars,'=')])
native_recruits=[]
for token,char,o in native_chars:
    if any(k in ('advisor','corps_commander','field_marshal','naval_commander','scientist') for k,v,o in walk(char)):
        history.append(('recruit_character',token,'='));native_recruits.append(token)
manifest['countries']['TUR']['native_recruits']=native_recruits
text('TUR_neutrality','Османская империя','Ottoman Empire')
text('TUR_neutrality_DEF','Османская империя','the Ottoman Empire')
text('TUR_neutrality_ADJ','Османск.','Ottoman')
save('history/countries/TUR - Turkey.txt',history)

# Keep disabled vanilla focus IDs registered for cross-country event/character checks.
# These shared definitions are never attached to a playable tree.
replaced=['austria.txt','hungary.txt','hungary_wuw.txt','turkey.txt','afghanistan.txt']
game_focus_docs={name:read(GAME/'common/national_focus'/name) for name in replaced}
loaded_ids=set()
for p in ROOT.glob('common/national_focus/*.txt'):
    if 'compatibility' in p.name or p.name in {tag+'_focuses.txt' for tag in manifest['countries']}:continue
    doc=read(p)
    loaded_ids.update(one(f,'id') for f in values(doc,'shared_focus'))
    loaded_ids.update(one(f,'id') for tree in values(doc,'focus_tree') for f in values(tree,'focus'))
for p in GAME.glob('common/national_focus/*.txt'):
    if not (ROOT/'common/national_focus'/p.name).exists():loaded_ids.update(re.findall(r'\bid\s*=\s*(\w+)',p.read_text(encoding='utf-8-sig')))
compat=[]
for filename in ['austria.txt','hungary.txt','hungary_wuw.txt','turkey.txt','afghanistan.txt']:
    candidates=values(game_focus_docs.get(filename,[]),'shared_focus')
    for tree in values(game_focus_docs.get(filename,[]),'focus_tree'):candidates+=values(tree,'focus')
    for node in candidates:
        v=one(node,'id')
        if v and v not in loaded_ids:
            compat.extend(parse(f'shared_focus = {{ id = {v} icon = GFX_focus_generic_diplomatic_treaty x = 0 y = 0 cost = 10 allow_branch = {{ always = no }} available = {{ always = no }} completion_reward = {{ }} }}'))
            loaded_ids.add(v)
save('common/national_focus/nww_legacy_compatibility.txt',compat)
manifest['compatibility_ids']=[one(v,'id') for k,v,o in compat]

save('common/ideas/nww_legacy_ideas.txt',[('ideas',[('country',ideas,'=')],'=')])
save('common/scripted_effects/nww_legacy_effects.txt',effects)
save('interface/nww_legacy.gfx',[('spriteTypes',[('spriteType',s,'=') for s in sprites],'=')])
for lang,entries in texts.items():
    # Existing stub descriptions must not compete with the imported definitions.
    for p in ROOT.glob(f'localisation/*l_{lang}.yml'):
        if p.name==f'nww_legacy_l_{lang}.yml':continue
        original=p.read_text(encoding='utf-8-sig');updated='\n'.join(line for line in original.splitlines() if not any(re.match(r'^\s+'+re.escape(key)+r':',line) for key in entries))+'\n'
        if updated!=original:p.write_text(updated,encoding='utf-8-sig')
    lines=['l_'+lang+':']
    for key,value in entries.items():lines.append(' '+key+':0 "'+value.replace('"','\\"').replace('\n','\\n')+'"')
    (ROOT/f'localisation/nww_legacy_l_{lang}.yml').write_text('\n'.join(lines)+'\n',encoding='utf-8-sig')
text_path=ROOT/'docs/legacy_import.json';text_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(', '.join(f'{tag}: {country["total"]} focuses' for tag,country in manifest['countries'].items()))
import runpy
runpy.run_path(str(ROOT/'tools/finalize_legacy_content.py'),run_name='__main__')
