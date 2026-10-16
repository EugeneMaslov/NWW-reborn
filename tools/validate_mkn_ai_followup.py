"""Regress MKN compact branches, player-facing rewards and paid AI frontier choices.

Decision selection is a deterministic priority model, not the engine AI scheduler.
"""
from itertools import product
from hoi4_script import read, one, values, walk, tree_focuses
from validate_mkn_ukraine import World


class AiWorld(World):
    def __init__(self):
        super().__init__()
        self.strength = 1.0

    def test(self, nodes, current='MKN', previous=None):
        for key, val, op in nodes or []:
            if key == 'strength_ratio':
                _, value, operator = next(n for n in val if n[0] == 'ratio')
                ok = self.compare(self.strength, float(value), operator)
            else:
                ok = super().test([(key,val,op)],current,previous)
            if not ok: return False
        return True


def score(world, decision):
    ai = one(decision,'ai_will_do',[])
    result = float(one(ai,'base',one(ai,'factor','0')))
    for modifier in values(ai,'modifier'):
        if world.test([n for n in modifier if n[0] not in {'factor','add'}]):
            result = (result+float(one(modifier,'add','0')))*float(one(modifier,'factor','1'))
    return result


def validate_ai_followup(root, game, check, localized):
    new = values(read(root/'common/national_focus/MKN_horizons_focuses.txt'),'shared_focus')
    def shown(nodes):
        for key,val,op in nodes:
            if key == 'hidden_effect': continue
            yield key,val,op
            if isinstance(val,list): yield from shown(val)
    for f in new:
        reward = list(shown(one(f,'completion_reward',[])))
        check(not any(k in {'nww_mkn_rebuild_services','remove_ideas','remove_dynamic_modifier','set_variable','add_to_variable','add_relation_rule_override'} for k,v,o in reward), one(f,'id')+': exposes migration or diplomatic internals in its reward')
        check(int(one(f,'x')) <= 104 and int(one(f,'y')) >= 4, one(f,'id')+': new branch is not underneath the existing tree')
    positions = {one(f,'id'):(int(one(f,'x')),int(one(f,'y'))) for f in new}
    check(positions['MKN_nabat_abroad'] == (102,4), 'MKN: diplomacy must join the common International branch')
    check(positions['MKN_death_or_freedom'] == (28,8), 'MKN: emergency defence must be underneath the army')
    check(positions['MKN_free_science_network'] == (10,15), 'MKN: science must continue beneath industry')
    all_foci = tree_focuses(one(read(root/'common/national_focus/MKN.txt'),'focus_tree'),root/'common/national_focus')
    for f in new:
        x,y = positions[one(f,'id')]
        for other in all_foci:
            if one(other,'id') == one(f,'id'): continue
            ox,oy = int(one(other,'x')),int(one(other,'y'))
            check(y != oy or abs(x-ox) >= 2, one(f,'id')+': overlaps '+one(other,'id'))
    permanent = {'MKN_nabat_foreign_cells','MKN_hidden_workshops','MKN_open_laboratories'}
    for fid in ('MKN_nabat_abroad','MKN_hide_the_machines','MKN_open_peer_review'):
        f = next(f for f in new if one(f,'id') == fid)
        check(not any(k == 'add_timed_idea' for k,v,o in walk(one(f,'completion_reward'))), fid+': permanent idea became temporary')
    for path in [root/'common/scripted_effects/nww_mkn_progression.txt', root/'common/scripted_effects/MKN_horizons_effects.txt']:
        for k,v,o in walk(read(path)):
            if k == 'remove_ideas':
                removed = {v} if isinstance(v,str) else {vv for kk,vv,oo in v}
                check(not removed & permanent, str(path)+': removes a persistent new spirit')
    campaigns = one(read(root/'common/decisions/nww_mkn_mandate.txt'),'MKN_public_mandate')
    countries = ('fascism','democratic','neutrality','communism')
    # No campaign before the route initializer, despite the communist starting government.
    w = AiWorld()
    check(all(score(w,one(campaigns,'MKN_campaign_'+route)) == 0 for route in countries), 'MKN: pre-selection government bias remains')
    for historical, pick in product((False,True),range(4)):
        w = AiWorld(); w.historical = historical; w.rule = 'DEFAULT'; w.pick = pick
        w.countries['MKN']['flags'].update(MKN_ai_plan_selected=-1,MKN_ai_route_communism=-1)
        w.run('MKN_initialize_ai_route')
        flags = w.countries['MKN']['flags']
        chosen = [r for r in countries if 'MKN_ai_route_'+r in flags]
        check(chosen == [countries[pick]], 'MKN: uncommitted DEFAULT old save retains the forced communist route')
        w.pick = (pick+1)%4;w.run('MKN_initialize_ai_route')
        check([r for r in countries if 'MKN_ai_route_'+r in flags] == chosen, 'MKN: route changes on the next day')
    branch = one(read(root/'common/scripted_effects/MKN_ai_effects.txt'),'MKN_initialize_ai_route')
    randoms = [v for k,v,o in walk(branch) if k == 'random_list']
    check(len(randoms) == 1 and one(randoms[0],'seed') == 'random', 'MKN: fresh campaigns reuse a deterministic country seed')
    check([k for k,v,o in randoms[0] if k and k.isdigit()] == ['25']*4, 'MKN: political random selection is not equal')
    decisions = one(read(root/'common/decisions/MKN_ukr_border_decisions.txt'),'MKN_ukr_border_category')
    withdraw = one(decisions,'mkn_deescalate_pull_back')
    drift = one(decisions,'MKN_passive_escalation_drift')
    attack_ids = ('mkn_escalate_steppe_alarm','mkn_raid_soviet_depots','mkn_launch_border_battle')
    root_focus = next(f for f in values(read(root/'common/national_focus/MKN_frontier_focuses.txt'),'shared_focus') if one(f,'id') == 'MKN_ukrainian_frontier_root')
    events = {one(e,'id'):e for e in values(read(root/'events/MKN_ukr_border_events.txt'),'country_event')}
    cases = 0
    for route,strong,prepared in product(countries,(False,True),(False,True)):
        w = AiWorld(); c = w.countries['MKN']; c['flags']['MKN_ai_route_'+route] = -1
        w.strength = 1.5 if strong else 1.0
        if prepared:c['focuses'].add('MKN_arrest_demagogues')
        w.run('mkn_ukr_initialize_frontier');c['variables']['mkn_ukr_escalation_level'] = 3
        pressure = route == 'fascism' and strong and prepared
        check((score(w,withdraw)>0) != pressure, 'MKN: peaceful/weak AI does not prioritize withdrawal')
        for fid in attack_ids:
            check((score(w,one(decisions,fid))>0) == pressure, fid+': AI escalates without a prepared strong military route')
        cases += 1
    # Exercise real paid 20-day decisions against all 30-day ticks for a full year.
    for route,initial_pp,income in product(countries,(0,100),(1,2)):
        w = AiWorld();c = w.countries['MKN']; c['flags']['MKN_ai_route_'+route] = -1;c['pp'] = initial_pp
        w.run('mkn_ukr_initialize_frontier')
        w.apply(one(events['mkn_ukr_border.10'],'immediate'))
        w.apply(one(root_focus,'completion_reward'))
        finish = None; spent = 0; maximum = 2
        for day in range(1,366):
            w.day = day;c['pp'] += income
            if day%30 == 0: w.apply(one(drift,'timeout_effect'))
            if finish == day:
                w.apply(one(withdraw,'remove_effect'));finish = None
            maximum = max(maximum,c['variables']['mkn_ukr_escalation_level'])
            if finish is None and w.test(one(withdraw,'available')) and score(w,withdraw)>0:
                cost = c['variables'][one(withdraw,'cost')]
                if c['pp']>=cost:
                    c['pp']-=cost;spent+=cost;w.apply(one(withdraw,'complete_effect'));finish=day+int(one(withdraw,'days_remove'))
            check(not w.flag('MKN','mkn_ukr_war_pending'), 'MKN: peace-seeking AI still reaches forced war despite paying for withdrawal')
        w.run('mkn_ukr_year_timeout')
        check(spent>0 and maximum<5 and w.flag('MKN','mkn_frontier_frozen'), 'MKN: paid withdrawal cannot sustain the frontier until the annual truce')
        check('UKR' in c['pacts'] and not w.declarations, 'MKN: peaceful year ends in war')
        cases+=1
    for actor in ('MKN','UKR'):
        w = AiWorld();w.run('mkn_ukr_initialize_frontier');w.countries['MKN']['variables']['mkn_ukr_escalation_level'] = 3
        w.countries[actor]['wars'].add('LTB')
        w.apply(one(drift,'timeout_effect'))
        check(w.countries['MKN']['variables']['mkn_ukr_escalation_level'] == 3, 'MKN: escalation grows while a full war blocks frontier decisions')
        cases+=1
    print(f'PASS: MKN follow-up: compact lower branches, hidden migration rewards, persistent ideas, random DEFAULT AI and {cases} frontier priority/paid-year scenarios (not engine scheduling)')
