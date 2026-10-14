"""Restore the German colonial start and disable the MEFO debt system for NWW."""
import json,re
from pathlib import Path
from hoi4_script import read,one,values,walk,parse,dump
ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')
territories={
 'German South-West Africa':[541,893,894,895],
 'German East Africa':[546,768,769],
 'Cameroon':[773],'Togoland':[777],
 'German New Guinea and Bismarck Archipelago':[979,737,1070],
 'Pacific islands':[633,646,647,684,725],
 'German Samoa':[726], 'Kiautschou lease':[743]}
states={int(one(one(read(p),'state'),'id')):p for p in (ROOT/'history/states').glob('*.txt')}
changes=[]
for region,ids in territories.items():
    for sid in ids:
        p=states[sid];original=p.read_text(encoding='utf-8-sig');history=one(one(read(p),'state'),'history')
        previous=one(history,'owner')
        # Preserve the map's native province/core setup and comments; replace all bookmark owners/controllers.
        updated=re.sub(r'\b(owner|controller)(\s*=\s*)[A-Z]{3}\b',lambda m:m[1]+m[2]+'GER',original)
        updated=re.sub(r'^\s*add_core_of\s*=\s*(?:SAF|JAP)\s*(?:#[^\n]*)?$', '',updated,flags=re.M)
        updated=re.sub(r'^(\s*(?:owner|controller)\s*=\s*GER)[ \t]+$',r'\1',updated,flags=re.M)
        if sid in (768,769):
            # WUW's original state initializer transfers these Belgian colonies to Congo
            # after reading owner, so updating the owner alone cannot fix the start.
            doc=parse(updated);state=one(doc,'state');setup=one(state,'history')
            setup[:]=[(k,v,o) for k,v,o in setup if not (isinstance(v,list) and any(key=='transfer_state_to' and target=='COG' for key,target,op in walk(v)))]
            updated=dump(doc)+'\n'
        p.write_text(updated,encoding='utf-8')
        changes.append({'state':sid,'region':region,'file':str(p.relative_to(ROOT)).replace('\\','/'),'previous_owner':previous})

native_ideas=one(one(read(GAME/'common/ideas/GER.txt'),'ideas'),'country')
mefo=[k for k,v,o in native_ideas if k.startswith('GER_mefo_bills')]
effect=[]
for modifier in ('GER_mefo_bills_modifier','GER_economy_of_conquest_modifier'):
    effect.extend(parse(f'if = {{ limit = {{ has_dynamic_modifier = {{ modifier = {modifier} }} }} remove_dynamic_modifier = {modifier} }}'))
for token in mefo:
    effect.extend(parse(f'if = {{ limit = {{ has_idea = {token} }} remove_ideas = {token} }}'))
effect.extend(parse('''if = { limit = { has_active_mission = GER_mefo_bills_mission } remove_mission = GER_mefo_bills_mission }
clr_country_flag = ger_has_cancelled_mefo
clr_country_flag = paid_for_mefo
clr_country_flag = GER_mefo_bills_penalty_flag
set_variable = { GER_mefo_bill_counter = 0 }
set_variable = { GER_monthly_consumer_goods_increase = 0 }
set_variable = { GER_industrial_consumer_goods_factor = 0 }
set_country_flag = NWW_GER_no_mefo'''))
effects_path=ROOT/'common/scripted_effects/GER_effects.txt'
effects=read(effects_path) if effects_path.exists() else []
effects[:]=[(k,v,o) for k,v,o in effects if k!='nww_GER_disable_mefo'];effects.append(('nww_GER_disable_mefo',effect,'='))
effects_path.write_text(dump(effects)+'\n',encoding='utf-8')
history_path=ROOT/'history/countries/GER - Germany.txt';history=read(history_path)
def strip_mefo(doc):
    result=[]
    for k,v,o in doc:
        if k=='add_dynamic_modifier' and one(v,'modifier') in ('GER_mefo_bills_modifier','GER_economy_of_conquest_modifier'):continue
        if k=='add_ideas' and isinstance(v,str) and v in mefo:continue
        if isinstance(v,list):
            if k=='add_ideas':v=[item for item in v if item[1] not in mefo]
            else:v=strip_mefo(v)
        if k=='activate_mission' and v=='GER_mefo_bills_mission':continue
        if k=='nww_GER_disable_mefo':continue
        result.append((k,v,o))
    return result
history=strip_mefo(history);history.append(('nww_GER_disable_mefo','yes','='));history_path.write_text(dump(history)+'\n',encoding='utf-8')
on_actions=parse('''on_actions = {
on_startup = { effect = { GER = { if = { limit = { has_focus_tree = GER_focus } nww_GER_disable_mefo = yes } } } }
on_daily_GER = { effect = { if = { limit = { has_focus_tree = GER_focus OR = { NOT = { has_country_flag = NWW_GER_no_mefo } has_dynamic_modifier = { modifier = GER_mefo_bills_modifier } has_dynamic_modifier = { modifier = GER_economy_of_conquest_modifier } has_active_mission = GER_mefo_bills_mission } } nww_GER_disable_mefo = yes } } }
}''')
(ROOT/'common/on_actions/GER_on_actions.txt').write_text(dump(on_actions)+'\n',encoding='utf-8')
report={'territories':changes,'total_states':len(changes),'no_ger_colonial_cores':True,'mefo_ideas':mefo,'historical_sources':['https://www.dhm.de/lemo/kapitel/kaiserreich/aussenpolitik/statistische-angaben-zu-den-deutschen-kolonien','https://www.dhm.de/lemo/kapitel/kaiserreich/aussenpolitik/kolonialpolitik','https://www.bundesarchiv.de/themen-entdecken/online-entdecken/geschichtsgalerien/die-entstehung-der-musterkolonie-kiautschou/']}
(ROOT/'docs/GER_overseas_setup.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Restored {len(changes)} German overseas states; MEFO disabled at setup and repaired for existing saves.')
