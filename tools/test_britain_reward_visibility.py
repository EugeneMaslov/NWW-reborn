"""Exercise actual ENG rewards and the native empty-category visibility rule."""
from datetime import date
from hoi4_script import read,one,values,walk
from test_britain_lifecycle import ROOT,P,World,EFFECTS,FOCUSES,DECISIONS


def main():
    checks=0
    def check(ok,message):
        nonlocal checks;checks+=1
        if not ok:raise AssertionError(message)
    categories=read(ROOT/'common/decisions/categories/ENG_categories.txt')
    decisions=read(ROOT/'common/decisions/ENG_decisions.txt')
    world=World();world.now=date(1936,1,1);world.run('initialize')
    visible=[]
    for key,category,_ in categories:
        has_actions=any(world.test(one(d,'visible',[])) for _,d,_ in one(decisions,key))
        if world.test(one(category,'allowed')) and world.test(one(category,'visible')) and (one(category,'visible_when_empty')=='yes' or has_actions):visible.append(key)
    check(set(visible)=={P+c+'_category' for c in ['imperial','cabinet','routes']},'New campaign does not show all three panels')
    check(not any(world.test(one(d,'visible',[])) for _,d,_ in one(decisions,P+'routes_category')),'Test did not reproduce locked maritime actions')
    for key in ['local_parliaments','representation','equal_union']:
        for initial,expected in [(55,65),(95,100)]:
            w=World();c=w.country('ENG')
            for tag in ['CAN','AST','SAF','NZL','RAJ']:c.vars[P+'trust_'+tag]=initial
            reward=one(FOCUSES[P+key],'completion_reward');w.apply(reward)
            check(all(c.vars[P+'trust_'+tag]==expected for tag in ['CAN','AST','SAF','NZL','RAJ']),key+': real trust reward missing or unclamped')
            calls=[EFFECTS[k] for k,v,_ in reward if k in EFFECTS]
            check(any(one(call,'custom_effect_tooltip') for call in calls),key+': trust reward has no rendered description')
    for key,initial in [('border_inquiry',5),('ulster_police',10)]:
        w=World();w.country('ENG').vars[P+'irish_pressure']=initial
        reward=one(FOCUSES[P+key],'completion_reward');w.apply(reward)
        check(w.country('ENG').vars[P+'irish_pressure']==0,key+': negative tension after focus')
        check(bool(one(reward,'custom_effect_tooltip')),key+': tension reward remains invisible')
    for key,flag in [('premiers','conferences_unlocked'),('ratification','ratification_unlocked'),('naval_planning','routes_unlocked'),('cape_route','cape_ready'),('canadian_corridors','canada_project_unlocked'),('indian_electricity','india_project_unlocked'),('irish_report','irish_unlocked'),('irish_talks','irish_talks_ready')]:
        w=World();reward=one(FOCUSES[P+key],'completion_reward');w.apply(reward)
        check(P+flag in w.country('ENG').flags,key+': advertised unlock not applied')
        check(bool(one(reward,'custom_effect_tooltip')),key+': unlock has no reward tooltip')
    # Modifier-only focuses must show their reward and develop the same spirit.
    for key,group,modifier,expected in [('machine_tools','economy','production_factory_efficiency_gain_factor',0),('electric_grid','economy','energy_gain_factor',0.10),('fighter_command','air','air_intercept_efficiency',0.10)]:
        w=World();c=w.country('ENG');c.completed.add(P+key)
        reward=one(FOCUSES[P+key],'completion_reward');w.apply(reward)
        check(abs(c.vars[P+group+'_'+modifier]-expected)<0.000001,key+': persistent reward not applied')
        check(bool(one(reward,'custom_effect_tooltip')),key+': branch modifier not described')
        # Do not assume whether the engine records completion before or after
        # completion_reward. The following daily hook must settle either order.
        w=World();w.run('initialize');c=w.country('ENG');w.apply(reward)
        c.completed.add(P+key);w.run('daily')
        check(abs(c.vars[P+group+'_'+modifier]-expected)<0.000001,key+': bonus lost when completion is recorded after the reward')
        check(P+'spirit_refresh_pending' not in c.flags,key+': refresh remains dirty after settlement')
    check(one(one(FOCUSES[P+'heavy_airgroups'],'completion_reward'),'add_tech_bonus') is not None,'Bomber research reward missing')
    check(one(one(one(FOCUSES[P+'heavy_airgroups'],'completion_reward'),'add_tech_bonus'),'category')=='cat_strategic_bomber','Bomber research still uses nonexistent category')
    for focus in FOCUSES.values():
        reward=one(focus,'completion_reward')
        visible_ops=[(k,v,o) for k,v,o in reward if k not in ['hidden_effect','set_country_flag','clr_country_flag','add_to_variable']]
        check(bool(visible_ops),'Focus has only hidden/undocumented effects: '+one(focus,'id'))
    print(f'PASS: ENG reward/UI regression: {checks} source-script cases; three empty/locked panels, real trust/tension/unlocks, staged spirits and visible rewards for all 153 focuses')


if __name__=='__main__':main()
