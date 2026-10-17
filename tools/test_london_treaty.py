"""Execute actual treaty lifecycle scripts, not the game scheduler or UI."""
from datetime import date
from pathlib import Path
from hoi4_script import read, one, values, variable_check
from test_britain_lifecycle import World, Country, EFFECTS
from build_london_treaty import ROOT, GAME, MEMBERS, IDEAS, P

EFFECTS.update({k:v for k,v,_ in read(ROOT/'common/scripted_effects/ENG_naval_treaty_effects.txt')})


class TreatyWorld(World):
    def __init__(self):
        super().__init__();self.gflags={};self.gvars={};self.wars=set();self.now=date(1936,1,1)
        for tag in MEMBERS:self.countries.setdefault(tag,Country())
    def test(self,node,ctx='ENG',root=None):
        results=[]
        for k,v,o in node:
            if k=='has_global_flag':
                if isinstance(v,str):ok=v in self.gflags
                else:
                    flag=one(v,'flag');entry=next(n for n in v if n[0]=='value')
                    ok=flag in self.gflags and self.num(self.gflags.get(flag,0),entry[2],float(entry[1]))
            elif k=='has_naval_treaty_trigger':ok=bool(self.country(ctx).ideas.intersection(IDEAS))==(v=='yes')
            elif k=='any_country':ok=any(c.exists and self.test(v,t,root or ctx) for t,c in self.countries.items())
            elif k=='any_enemy_country':ok=any(frozenset([ctx,t]) in self.wars and self.test(v,t,root or ctx) for t in self.countries if t!=ctx)
            elif k=='check_variable' and variable_check(v)[0].startswith('global.'):
                key,value,op=variable_check(v);ok=self.num(self.gvars.get(key,0),op,float(value))
            else:ok=super().test([(k,v,o)],ctx,root)
            results.append(ok)
        return all(results)
    def apply(self,node,ctx='ENG',root=None,params=None):
        branch=False
        for k,v,o in node:
            if k in ['if','else_if']:
                if k=='if':branch=False
                if not branch and self.test(one(v,'limit',[]),ctx,root):
                    self.apply([n for n in v if n[0]!='limit'],ctx,root);branch=True
            elif k=='else':
                if not branch:self.apply(v,ctx,root)
                branch=False
            elif k in ['every_country','every_other_country']:
                for t,c in self.countries.items():
                    if c.exists and (k=='every_country' or t!=ctx) and self.test(one(v,'limit',[]),t,root or ctx):self.apply([n for n in v if n[0]!='limit'],t,root or ctx)
            elif k=='set_global_flag':
                self.gflags[v if isinstance(v,str) else one(v,'flag')]=1 if isinstance(v,str) else float(one(v,'value',1))
            elif k=='clr_global_flag':self.gflags.pop(v,None)
            elif k=='modify_global_flag':
                flag=one(v,'flag');self.gflags[flag]=self.gflags.get(flag,0)+float(one(v,'value'))
            elif k=='swap_ideas':
                self.country(ctx).ideas.discard(one(v,'remove_idea'));self.country(ctx).ideas.add(one(v,'add_idea'))
            elif k=='remove_mission':self.country(ctx).missions.discard(v)
            elif k in ['set_variable','add_to_variable'] and v[0][0].startswith('global.'):
                key,value,_=v[0];self.gvars[key]=(self.gvars.get(key,0) if k=='add_to_variable' else 0)+float(value)
            else:super().apply([(k,v,o)],ctx,root,params)
    def run(self,key,ctx='ENG'):self.apply(EFFECTS[P+key],ctx)


def main(game=None):
    global GAME
    if game is not None:
        GAME=Path(game)
    elif not GAME.is_dir():
        GAME=Path.home()/'.local/share/Steam/steamapps/common/Hearts of Iron IV'
    EFFECTS['remove_naval_treaty_effect']=one(read(GAME/'common/scripted_effects/00_scripted_effects.txt'),'remove_naval_treaty_effect')
    checks=0
    def check(ok,message):
        nonlocal checks;checks+=1
        if not ok:raise AssertionError(message)
    w=TreatyWorld();w.country('TUR').ideas.add(IDEAS[0])
    legacy=one(read(GAME/'common/decisions/MTG_naval_treaty.txt'),'MTG_naval_treaties')
    old_missions={k for k,v,_ in legacy if one(v,'days_mission_timeout') is not None}
    w.country('JAP').missions.update(old_missions);w.run('setup')
    check(old_missions and not w.country('JAP').missions,'Native treaty missions survived migration')
    check(w.gvars['global.ENG_london_members']==7,'Not exactly seven signatories')
    check(not w.country('TUR').ideas.intersection(IDEAS),'Outsider remains a signatory')
    for t in MEMBERS:check(w.country(t).ideas=={IDEAS[0]},t+' has unequal starting limits')
    w.run('setup');check(w.gvars['global.ENG_london_members']==7,'Repeated startup corrupts count')
    w.run('withdraw','ITA');check(w.gvars['global.ENG_london_members']==6,'First withdrawal miscount')
    check(all(w.country(t).ideas.intersection(IDEAS) for t in MEMBERS if t!='ITA'),'Unrelated member expelled')
    w.run('setup');check(not w.country('ITA').ideas.intersection(IDEAS),'Withdrawn member forcibly restored')
    w.run('escalate')
    for t in MEMBERS:
        if t!='ITA':check(IDEAS[2] in w.country(t).ideas,t+' did not receive protective clause')
    for t,count in [('GER',5),('JAP',4),('CHI',3),('USA',0)]:
        w.run('withdraw',t);check(w.gvars['global.ENG_london_members']==count,'Incorrect dissolution boundary '+t)
    check(P+'ended' in w.gflags,'Agreement survived fewer than three parties')
    w.run('setup');check(w.gvars['global.ENG_london_members']==0,'Dissolved agreement resurrected')
    w.country('JAP').ideas.add(IDEAS[0]);w.run('tick')
    check(w.gvars['global.ENG_london_members']==0,'Native focus resurrected expired restrictions')
    w=TreatyWorld();w.run('setup');w.apply(EFFECTS['remove_naval_treaty_effect'],'JAP');w.run('tick')
    check(w.gvars['global.ENG_london_members']==6,'Native focus withdrawal not counted')
    check(P+'withdrawal' in w.gflags,'Native focus withdrawal did not unlock protective clause')
    w=TreatyWorld();w.run('setup');w.wars.add(frozenset(['GER','TUR']));w.run('tick')
    check(P+'ended' not in w.gflags,'External war incorrectly dissolved agreement')
    w.wars.add(frozenset(['JAP','CHI']));w.run('tick')
    check(P+'ended' in w.gflags,'China excluded from war dissolution rule')
    check(w.gvars['global.ENG_london_members']==0,'War failed to clear all limits')
    # Late old saves retain actual existing members and never seed new ones.
    w=TreatyWorld();w.now=date(1940,1,1)
    for t in ['ENG','FRA','GER']:w.country(t).ideas.add(IDEAS[0])
    w.run('setup');check(w.gvars['global.ENG_london_members']==3,'Late save received new signatories')
    w=TreatyWorld();w.gflags[P+'initialized']=1
    for t in MEMBERS:
        if t!='USA':w.country(t).ideas.add(IDEAS[0])
    w.run('setup');check(w.gvars['global.ENG_london_members']==7,'Prior six-party save did not recover USA')
    w.run('withdraw','USA');w.run('setup')
    check(not w.country('USA').ideas.intersection(IDEAS),'US withdrawal overwritten by revision repair')
    decisions=one(read(ROOT/'common/decisions/ENG_naval_treaty_decisions.txt'),P+'category')
    for name in ['withdraw','clause']:
        d=one(decisions,P+name);w=TreatyWorld();w.run('setup');before=w.country('ENG').pp
        w.country('ENG').pp-=int(one(d,'cost'));w.apply(one(d,'complete_effect',[]));w.apply(one(d,'cancel_effect'))
        check(w.country('ENG').pp==before,name+': cancellation not refunded')
        check(P+'conference_busy' not in w.gflags,name+': cancelled conference stuck busy')
        check(w.gvars['global.ENG_london_members']==7,name+': cancellation removed a member')
    print(f'PASS: London agreement: {checks} source-script cases; seven parties including USA, withdrawal, equal escalation, China war, dissolution, cancellation and old saves')


if __name__=='__main__':main()
