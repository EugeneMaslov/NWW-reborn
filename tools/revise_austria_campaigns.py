"""Complete Austrian conquest objectives and add the post-conquest dual-monarchy focus."""
import copy,json,re
from pathlib import Path
from hoi4_script import read,one,values,walk,parse,dump
ROOT=Path(__file__).resolve().parents[1]
def save(path,doc):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(dump(doc)+'\n',encoding='utf-8')
def setv(node,key,value):
    node[:]=[(k,v,o) for k,v,o in node if k!=key];node.append((key,value,'='))
tree_path='common/national_focus/AUS_focuses.txt';doc=read(ROOT/tree_path);tree=one(doc,'focus_tree')
focuses={one(f,'id'):f for f in values(tree,'focus')}
effects=[];on_cap=[];refresh=[];peace_ai=[];peace_cost=[]
territories={tag:[] for tag in ('HUN','CRO')}
for p in (ROOT/'history/states').glob('*.txt'):
    state=one(read(p),'state');owner=one(one(state,'history'),'owner')
    if owner in territories:territories[owner].append(int(one(state,'id')))
for tag in territories:territories[tag].sort()
for tag,fid in [('HUN','AUS_war_with_hun'),('CRO','AUS_war_with_croatia')]:
    helper=f'nww_AUS_prepare_{tag.lower()}_campaign'
    effect=parse(f'''if = {{ limit = {{ tag = AUS NOT = {{ has_country_flag = NWW_AUS_dual_monarchy_restored }} {tag} = {{ exists = yes }} NOT = {{ is_ally_with = {tag} }} }}
 if = {{ limit = {{ NOT = {{ has_country_flag = NWW_AUS_{tag}_campaign_prepared }} }}
   set_country_flag = NWW_AUS_{tag}_campaign_prepared
   add_ai_strategy = {{ type = conquer id = {tag} value = 200 }}
 }}
 {tag} = {{ every_owned_state = {{ add_claim_by = AUS set_state_flag = NWW_AUS_{tag}_objective }} }}
 if = {{ limit = {{ NOT = {{ has_war_with = {tag} }} NOT = {{ has_wargoal_against = {tag} }} is_subject = no }}
   create_wargoal = {{ type = annex_everything target = {tag} }}
 }}
}}''')
    effects.append((helper,effect,'='))
    node=focuses[fid]
    reward=[(k,v,o) for k,v,o in one(node,'completion_reward') if k not in ('create_wargoal','add_ai_strategy',helper,'custom_effect_tooltip')]
    reward += parse(f'custom_effect_tooltip = NWW_AUS_{tag}_full_conquest_tt hidden_effect = {{ {helper} = yes }}')
    setv(node,'completion_reward',reward)
    refresh.extend(parse(f'if = {{ limit = {{ has_completed_focus = {fid} }} {helper} = yes }}'))
    # ROOT is the capitulated country; FROM is the actual victor, as in MTG's USA/CSA hook.
    on_cap.extend(parse(f'''if = {{ limit = {{ tag = {tag} exists = yes FROM = {{ tag = AUS has_completed_focus = {fid} NOT = {{ has_country_flag = NWW_AUS_dual_monarchy_restored }} }} }}
 FROM = {{ annex_country = {{ target = ROOT transfer_troops = no }} set_country_flag = NWW_AUS_{tag}_incorporated }} }}'''))
    enabled=f'ROOT = {{ tag = AUS has_completed_focus = {fid} NOT = {{ has_country_flag = NWW_AUS_dual_monarchy_restored }} }} FROM = {{ tag = AUS }} FROM.FROM = {{ original_tag = {tag} }}'
    peace_ai.extend(parse(f'NWW_AUS_{tag}_take_entire_country = {{ peace_action_type = take_states enable = {{ {enabled} }} ai_desire = 1000 }}'))
    enabled_alternatives=f'ROOT = {{ tag = AUS has_completed_focus = {fid} NOT = {{ has_country_flag = NWW_AUS_dual_monarchy_restored }} }} FROM.FROM = {{ original_tag = {tag} }}'
    peace_ai.extend(parse(f'NWW_AUS_{tag}_no_fragmentation = {{ peace_action_type = {{ puppet liberate force_government }} enable = {{ {enabled_alternatives} }} ai_desire = -1000 }}'))
    peace_cost.extend(parse(f'NWW_AUS_{tag}_imperial_claims = {{ category = treaties_or_conferences peace_action_type = take_states enable = {{ {enabled} }} cost_multiplier = 0.5 }}'))

effects_path='common/scripted_effects/AUS_effects.txt'
old=read(ROOT/effects_path) if (ROOT/effects_path).exists() else []
names={k for k,v,o in effects};save(effects_path,[(k,v,o) for k,v,o in old if k not in names]+effects)
save('common/on_actions/AUS_on_actions.txt',[('on_actions',[
 ('on_capitulation',[('effect',on_cap,'=')],'='),
 ('on_startup',[('effect',[('AUS',[('if',parse('limit = { has_focus_tree = AUS_focus }')+copy.deepcopy(refresh),'=')],'=')],'=')],'='),
 ('on_daily_AUS',[('effect',[('if',parse('limit = { has_focus_tree = AUS_focus }')+copy.deepcopy(refresh),'=')],'=')],'=')],'=')])
save('common/peace_conference/ai_peace/AUS_peace.txt',[('peace_ai_desires',peace_ai,'=')])
save('common/peace_conference/cost_modifiers/AUS_peace.txt',[('peace_action_modifiers',peace_cost,'=')])

# Formation follows conquest and ownership. Flags alone cannot unlock the new crown.
fid='NWW_AUS_restore_dual_monarchy';all_states=sorted(set(sum(territories.values(),[])))
conditions='is_subject = no NOT = { HUN = { exists = yes } } NOT = { CRO = { exists = yes } } 4 = { is_owned_and_controlled_by = ROOT } '
conditions+=' '.join(f'{sid} = {{ is_owned_and_controlled_by = ROOT }}' for sid in all_states)
reward='set_cosmetic_tag = HUN_EMPIRE set_country_flag = NWW_AUS_dual_monarchy_restored add_stability = 0.05 add_political_power = 100 '
reward+=' '.join(f'{sid} = {{ add_core_of = ROOT }}' for sid in all_states)
node=parse(f'''id = {fid} x = 6 y = 7 cost = 10 icon = GFX_focus_proclaim_the_restauration_of_Austria_Hungary
prerequisite = {{ focus = AUS_reclaiming_yugoslavian_territories }} available = {{ {conditions} }}
cancel_if_invalid = yes continue_if_invalid = no completion_reward = {{ {reward} }} ai_will_do = {{ factor = 100 }}''')
tree[:]=[(k,v,o) for k,v,o in tree if not (k=='focus' and one(v,'id')==fid)];tree.append(('focus',node,'='))
setv(tree,'continuous_focus_position',parse('x = 100 y = 2400'));save(tree_path,doc)
plan_path='common/ai_strategy_plans/AUS_historical.txt';plan=read(ROOT/plan_path)[0][1]
order=one(plan,'ai_national_focuses')
for token in ('AUS_reclaiming_yugoslavian_territories',fid):
    if not any(v==token for k,v,o in order):order.append((None,token,None))
save(plan_path,[('NWW_AUS_historical',plan,'=')])

text={
 'AUS_war_with_hun_desc':('Венгерский ультиматум требует полного присоединения королевства. Претензии охватывают все его земли. Если Венгрия капитулирует перед Австрией в этой войне, она полностью входит в состав нашей страны.','The Hungarian ultimatum demands the entire kingdom. Claims cover all its territory. Hungary is fully annexed if it capitulates to Austria in this campaign.'),
 'AUS_war_with_croatia_desc':('Хорватские земли должны войти в восстановленную монархию целиком. Капитуляция Хорватии перед Австрией в войне по этому фокусу приводит к полному присоединению страны.','The Croatian lands must enter the restored monarchy as a whole. Croatia is fully annexed if it capitulates to Austria in this campaign.'),
 'NWW_AUS_HUN_full_conquest_tt':('Предъявить претензии на все венгерские земли и получить постоянную цель войны на полное присоединение. Капитуляция Венгрии перед Австрией в этой кампании означает полную аннексию.','Claim all Hungarian territory and gain a permanent full-annexation war goal. Hungary is fully annexed if it capitulates to Austria in this campaign.'),
 'NWW_AUS_CRO_full_conquest_tt':('Предъявить претензии на все хорватские земли и получить постоянную цель войны на полное присоединение. Капитуляция Хорватии перед Австрией в этой кампании означает полную аннексию.','Claim all Croatian territory and gain a permanent full-annexation war goal. Croatia is fully annexed if it capitulates to Austria in this campaign.'),
 fid:('Восстановить Австро-Венгрию','Restore Austria-Hungary'),
 fid+'_desc':('После полного присоединения Венгрии и Хорватии заключим новый договор коронных земель. На карте появится Австро-Венгрия, а включённые венгерские и хорватские земли станут национальными территориями общего государства.','After fully annexing Hungary and Croatia, conclude a new crown-land settlement. The country becomes Austria-Hungary and the incorporated Hungarian and Croatian lands become its cores.')}
for lang,index in [('russian',0),('english',1)]:
    p=ROOT/f'localisation/replace/AUS_l_{lang}.yml';original=p.read_text(encoding='utf-8-sig')
    lines=[line for line in original.splitlines() if not any(re.match(r'^\s+'+re.escape(key)+r':',line) for key in text)]
    lines += [' '+key+':0 "'+value[index]+'"' for key,value in text.items()];p.write_text('\n'.join(lines)+'\n',encoding='utf-8-sig')
manifest_path=ROOT/'docs/legacy_import.json';manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
c=manifest['countries']['AUS'];c['focus_ids']=[one(f,'id') for f in values(tree,'focus')];c['total']=len(c['focus_ids'])
manifest['content_files']=sorted(set(manifest['content_files'])|{effects_path,'common/on_actions/AUS_on_actions.txt','common/peace_conference/ai_peace/AUS_peace.txt','common/peace_conference/cost_modifiers/AUS_peace.txt'})
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'docs/AUS_conquest_objectives.json').write_text(json.dumps({'target_states':territories,'formation_focus':fid,'capitulation_reference':'04_mtg_on_actions.txt: USA/CSA','peace_references':['ai_peace/RAJ.txt','cost_modifiers/AFG_peace.txt']},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Austrian campaigns claim entire target countries, annex after actual capitulation, renew unfinished objectives and lead to Austria-Hungary.')
