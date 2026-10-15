"""Build country-owned AI campaign safeguards using native relation-rule predicates."""
from pathlib import Path
from hoi4_script import read,one,values,parse,dump,walk

ROOT=Path(__file__).resolve().parents[1]
def write(path,text):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(text,encoding='utf-8',newline='\n')
def save(path,node):write(path,dump(node)+'\n')
def block(s):return parse(s)
def guard(node,trigger):
    if any(k==trigger for k,v,o in walk(node)):return
    node.append((trigger,'yes','='))

def generate(tag,tree,targets):
    prefix=f'nww_{tag}_ai'
    text=f'''# Owner {tag}. Ready/target triggers are also evaluated by a native relation rule.
{prefix}_campaign_ready = {{
 has_war = no
 has_capitulated = no
 has_civil_war = no
 is_subject = no
 surrender_progress < 0.05
 has_stability > 0.40
 has_war_support > 0.35
 NOT = {{ has_country_flag = NWW_{tag}_campaign_recovery }}
 NOT = {{ has_country_flag = NWW_{tag}_campaign_defeat_pending }}
 NOT = {{ has_country_flag = NWW_{tag}_campaign_was_at_war }}
}}
{prefix}_target_safe = {{
 exists = yes
 is_subject = no
 NOT = {{ is_ally_with = {tag} }}
'''
    if tag=='TUR':
        text+=''' is_major = no
 is_in_faction = no
 has_war = no
 strength_ratio = { tag = TUR ratio < 0.67 }
 NOT = { any_other_country = { has_guaranteed = PREV } }
'''
    else:
        text+=''' NOT = { has_war_with_major = yes }
 strength_ratio = { tag = GER ratio < 0.80 }
 NOT = { any_other_country = { has_guaranteed = PREV OR = { is_major = yes is_in_faction = yes is_subject = yes } } }
 OR = {
  is_in_faction = no
  AND = {
   OR = { is_faction_leader = yes is_major = no }
   NOT = { any_other_country = { is_major = yes is_in_faction_with = PREV NOT = { is_faction_leader = yes } } }
   NOT = { any_other_country = { is_faction_leader = yes is_in_faction_with = PREV NOT = { strength_ratio = { tag = GER ratio < 0.67 } } } }
  }
 }
'''
    text+=f'''}}
# FROM is the proposed target, following ETH has_lon_arms_embargo.
# Use the explicit owner for readiness, independently of the calling event ROOT.
{prefix}_unsafe_declaration = {{
 {tag} = {{ is_ai = yes has_focus_tree = {tree} }}
 OR = {{ {tag} = {{ NOT = {{ {prefix}_campaign_ready = yes }} }} FROM = {{ NOT = {{ {prefix}_target_safe = yes }} }} }}
}}
{prefix}_can_prepare_campaign = {{
 custom_trigger_tooltip = {{ tooltip = {prefix}_can_prepare_campaign OR = {{ is_ai = no {prefix}_campaign_ready = yes }} }}
}}
'''
    for target in targets:
        text+=f'''{prefix}_can_target_{target} = {{
 custom_trigger_tooltip = {{ tooltip = {prefix}_can_target_{target} OR = {{ is_ai = no AND = {{ {prefix}_campaign_ready = yes {target} = {{ {prefix}_target_safe = yes }} }} }} }}
}}
'''
    write(f'common/scripted_triggers/{tag}_campaign_safety_triggers.txt',text)
    effects=f'''# Owner {tag}. Negative relation rules combine without clearing other protections.
{prefix}_install_campaign_guard = {{
 remove_relation_rule_override = {{ trigger = {prefix}_unsafe_declaration can_not_declare_war = yes }}
 add_relation_rule_override = {{ trigger = {prefix}_unsafe_declaration usage_desc = NWW_{tag}_campaign_safety_tt can_not_declare_war = yes }}
 set_country_flag = NWW_{tag}_campaign_guard_installed
}}
{prefix}_observe_campaign = {{
 if = {{ limit = {{ NOT = {{ has_country_flag = NWW_{tag}_campaign_guard_installed }} }} {prefix}_install_campaign_guard = yes }}
 if = {{ limit = {{ has_capitulated = yes }} set_country_flag = NWW_{tag}_campaign_defeat_pending }}
 if = {{ limit = {{ has_war = yes }} set_country_flag = NWW_{tag}_campaign_was_at_war }}
 if = {{
  limit = {{ has_war = no OR = {{ has_country_flag = NWW_{tag}_campaign_was_at_war has_country_flag = NWW_{tag}_campaign_defeat_pending }} }}
  if = {{
   limit = {{ has_country_flag = NWW_{tag}_campaign_defeat_pending }}
   set_country_flag = {{ flag = NWW_{tag}_campaign_recovery days = 730 }}
  }}
  else = {{ set_country_flag = {{ flag = NWW_{tag}_campaign_recovery days = 180 }} }}
  clr_country_flag = NWW_{tag}_campaign_was_at_war
  clr_country_flag = NWW_{tag}_campaign_defeat_pending
 }}
}}
'''
    write(f'common/scripted_effects/{tag}_campaign_safety_effects.txt',effects)
    hooks=f'''on_actions = {{
 on_startup = {{ effect = {{ {tag} = {{ if = {{ limit = {{ exists = yes has_focus_tree = {tree} }}
  {prefix}_install_campaign_guard = yes
  if = {{ limit = {{ is_ai = yes has_war = no NOT = {{ has_country_flag = NWW_{tag}_campaign_safety_initialized }} }} set_country_flag = {{ flag = NWW_{tag}_campaign_recovery days = 180 }} }}
  set_country_flag = NWW_{tag}_campaign_safety_initialized
  {prefix}_observe_campaign = yes
 }} }} }} }}
 on_daily_{tag} = {{ effect = {{ if = {{ limit = {{ has_focus_tree = {tree} }} {prefix}_observe_campaign = yes }} }} }}
 on_war = {{ effect = {{ if = {{ limit = {{ tag = {tag} has_focus_tree = {tree} }} {prefix}_observe_campaign = yes }} }} }}
 on_war_relation_added = {{ effect = {{
  if = {{ limit = {{ tag = {tag} has_focus_tree = {tree} }} {prefix}_observe_campaign = yes }}
  FROM = {{ if = {{ limit = {{ tag = {tag} has_focus_tree = {tree} }} {prefix}_observe_campaign = yes }} }}
 }} }}
 on_capitulation = {{ effect = {{ if = {{ limit = {{ tag = {tag} has_focus_tree = {tree} }} set_country_flag = NWW_{tag}_campaign_defeat_pending }} }} }}
 on_peaceconference_ended = {{ effect = {{ if = {{ limit = {{ tag = {tag} has_focus_tree = {tree} }} set_country_flag = NWW_{tag}_campaign_was_at_war {prefix}_observe_campaign = yes }} }} }}
}}
'''
    write(f'common/on_actions/{tag}_campaign_safety_on_actions.txt',hooks)

def main():
    tur={'BUL':'TUR_war_with_bulgaria','GRE':'TUR_snova_copi','YUG':'NWW_TUR_serbian_campaign','ALB':'NWW_TUR_albanian_campaign','ROM':'NWW_TUR_romanian_campaign','CRO':'NWW_TUR_adriatic_campaign'}
    ger=['AUS','LTB','POL','MKN','UKR','FRA','ENG','SOV']
    generate('TUR','turkish_focus',tur)
    generate('GER','GER_focus',ger)
    for tag in ('TUR','GER'):
        path=f'common/scripted_effects/{tag}_effects.txt';doc=read(ROOT/path)
        for key,node,op in doc:
            # Every goal award, including daily repair and replies routed here,
            # checks AI readiness and the actual prospective coalition.
            def protect(branch):
                for index,(effect,value,operator) in enumerate(branch):
                    if effect=='create_wargoal':
                        target=one(value,'target')
                        if target in (tur if tag=='TUR' else ger):
                            branch[index]=('if',[('limit',block(f'nww_{tag}_ai_can_target_{target} = yes'),'='),(effect,value,operator)],'=')
                    elif isinstance(value,list):protect(value)
            # Detect existing generated guards for repeatable script execution.
            if not any(k and k.startswith(f'nww_{tag}_ai_can_target_') for k,v,o in walk(node)):protect(node)
        save(path,doc)
    path='common/national_focus/TUR_focuses.txt';doc=read(ROOT/path)
    for f in values(one(doc,'focus_tree'),'focus'):
        for target,fid in tur.items():
            if one(f,'id')==fid:
                available=one(f,'available');guard(available,f'nww_TUR_ai_can_target_{target}')
    save(path,doc)
    path='common/ai_strategy/TUR_balkans.txt';doc=read(ROOT/path)
    for name,node,op in doc:
        target=name.removeprefix('NWW_TUR_').removesuffix('_campaign')
        if target in tur:guard(one(node,'enable'),f'nww_TUR_ai_can_target_{target}')
    save(path,doc)
    path='common/national_focus/GER_political.txt';doc=read(ROOT/path)
    for focus in values(doc,'shared_focus'):
        fid=one(focus,'id')
        if fid in ('GER_the_austrian_question','GER_anschluss_by_force'):
            guard(one(focus,'available'),'nww_GER_ai_can_target_AUS')
        elif fid in ('GER_reign_in_mitteleuropa','GER_crush_eastern_syndicates','GER_lebensraum_in_the_east','GER_world_revolution'):
            guard(one(focus,'available'),'nww_GER_ai_can_prepare_campaign')
    save(path,doc)
    # Event replies can directly award goals as well as the scripted helpers.
    path='events/GER_events.txt';doc=read(ROOT/path)
    for kind,event,op in doc:
        if kind not in ('country_event','news_event'):continue
        def protect_reply(branch):
            for i,(k,v,o) in enumerate(branch):
                if k=='create_wargoal' and one(v,'target')=='AUS':
                    branch[i]=('if',[('limit',block('nww_GER_ai_can_target_AUS = yes'),'='),(k,v,o)],'=')
                elif isinstance(v,list):protect_reply(v)
        if not any(k=='nww_GER_ai_can_target_AUS' for k,v,o in walk(event)):protect_reply(event)
    save(path,doc)
    # Avoid even sending coercive diplomatic demands from a busy/recovering AI.
    path='common/scripted_effects/GER_effects.txt';doc=read(ROOT/path)
    for name,node,op in doc:
        if name=='GER_nww_dispatch_austrian_demand':guard(one(one(node,'if'),'limit'),'nww_GER_ai_can_target_AUS')
        if name=='nww_GER_mitteleuropa_demand':guard(one(one(node,'if'),'limit'),'nww_GER_ai_can_prepare_campaign')
    save(path,doc)
    print('Built GER/TUR native declaration guards, peace/defeat recovery and focus/goal/strategy checks')

if __name__=='__main__':main()
