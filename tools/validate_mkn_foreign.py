"""Execute common foreign-policy rewards and recipient consent, not engine AI."""
from copy import deepcopy
from itertools import product
import re
from hoi4_script import read, one, values, walk, tree_focuses
from validate_mkn_ukraine import World


class ForeignWorld(World):
    def __init__(self):
        super().__init__()
        for tag in ('AUS','GER','TUR','HUN'):
            self.countries[tag] = deepcopy(self.countries['LTB'])

    def test(self, nodes, current='MKN', previous=None):
        for key,val,op in nodes or []:
            if key == 'has_dynamic_modifier':
                ok = one(val,'modifier') in self.countries[current].get('dynamic',set())
            elif key == 'has_war_with':
                ok = (self.scope(val,current,previous) or val) in self.countries[current]['wars']
            else:
                ok = super().test([(key,val,op)],current,previous)
            if not ok:return False
        return True

    def apply(self, nodes, current='MKN', previous=None):
        matched=False
        for key,val,op in nodes:
            if key in {'if','else_if'}:
                if key=='if':matched=False
                if not matched and self.test(one(val,'limit'),current,previous):
                    self.apply([n for n in val if n[0]!='limit'],current,previous);matched=True
            elif key=='else':
                if not matched:self.apply(val,current,previous)
                matched=True
            elif key=='hidden_effect':self.apply(val,current,previous)
            elif key == 'add_opinion_modifier':
                target = self.scope(one(val,'target'),current,previous) or one(val,'target')
                self.countries[current].setdefault('opinions',set()).add((target,one(val,'modifier')))
            else:super().apply([(key,val,op)],current,previous)


def validate_foreign(root, game, check, localized):
    fs={one(f,'id'):f for f in tree_focuses(one(read(root/'common/national_focus/MKN.txt'),'focus_tree'),root/'common/national_focus')}
    chain=['MKN_black_international','MKN_foreign_delegates','MKN_workers_corridors','MKN_consular_communes','MKN_solidarity_guarantees']
    for parent,fid in zip(['MKN_departure_of_batko']+chain,chain):
        f=fs[fid]
        check(values(one(f,'prerequisite'),'focus')==[parent],fid+': common foreign-policy branch disconnected')
        check(not one(f,'available') and not one(f,'allow_branch') and not values(f,'mutually_exclusive'),fid+': political restriction remains')
        localized(fid,fid);localized(fid+'_desc',fid)
        if fid!='MKN_black_international':localized(fid+'_tt',fid)
    check(values(one(fs['MKN_nabat_abroad'],'prerequisite'),'focus')==['MKN_black_international'],'MKN: Nabat not connected to common foreign policy')
    congress=set(values(one(fs['MKN_congress_of_free_peoples'],'prerequisite'),'focus'))
    check(congress=={'MKN_fund_the_underground','MKN_solidarity_guarantees'},'MKN: congress must allow either peaceful or clandestine preparation')
    for fid,y in [('MKN_memory_of_atamansha_marusya',1),('MKN_the_black_guard_battalions',2)]:
        check((one(fs[fid],'x'),one(fs[fid],'y'))==('28',str(y)),fid+': memorials have not been raised')
    positions={}
    for fid,f in fs.items():
        x,y=int(one(f,'x')),int(one(f,'y'))
        check(all(oy!=y or abs(ox-x)>=2 for ox,oy in positions.values()),fid+': overlapping focus card')
        positions[fid]=(x,y)
    # The foreign service grows persistently and survives daily/save repair
    # without replaying PP or replacing a spirit.
    cases=0
    for government in ('communism','democratic','neutrality','fascism'):
        w=ForeignWorld();c=w.countries['MKN'];c['government']=government;c['focuses'].add('MKN_departure_of_batko')
        for fid in chain[1:]:
            check(w.test(one(fs[fid],'available')),fid+': government cannot start common diplomacy')
            c['focuses'].add(fid);w.apply(one(fs[fid],'completion_reward'))
        before=deepcopy(c)
        w.run('MKN_rebuild_foreign_service');w.run('MKN_rebuild_foreign_service')
        check(c==before,'MKN: foreign service repair repeats rewards or changes the spirit')
        check(c['dynamic']=={'MKN_foreign_service'},'MKN: expected a single permanent diplomatic spirit')
        check({k:v for k,v in c['variables'].items() if k.startswith('MKN_foreign_')}=={
            'MKN_foreign_relations_upkeep':-0.1,'MKN_foreign_trade_opinion':0.1,
            'MKN_foreign_opinion_gain':0.1,'MKN_foreign_guarantee_cost':-0.1},'MKN: diplomatic progression has wrong stats')
        cases+=1
    modifier=one(read(root/'common/dynamic_modifiers/MKN_foreign_modifiers.txt'),'MKN_foreign_service')
    native=set(re.findall(r'^## (\w+)',(game/'documentation/modifiers_documentation.md').read_text(),re.M))
    check(all(k in native for k,v,o in modifier if isinstance(v,str) and v.startswith('MKN_foreign_')),'MKN: invalid native diplomatic modifier')
    decision=one(one(read(root/'common/decisions/MKN_foreign_decisions.txt'),'mkn_black_international_category'),'MKN_offer_workshop_exchange')
    event=one(read(root/'events/MKN_foreign_events.txt'),'country_event')
    accept,decline=values(event,'option')
    for key in ('MKN_offer_workshop_exchange','MKN_offer_workshop_exchange_desc','MKN_workshop_exchange_offer_tt','MKN_workshop_exchange_opinion','MKN_foreign_service','MKN_foreign_service_desc','mkn_foreign.1.t','mkn_foreign.1.d','mkn_foreign.1.a','mkn_foreign.1.b'):
        localized(key,'MKN common diplomacy')
    for target,government,choice in product(('LTB','AUS','GER','TUR','HUN'),('communism','democratic','neutrality','fascism'),('accept','decline','war','subject','capitulated','mkn_gone','expired','duplicate')):
        w=ForeignWorld();c=w.countries['MKN'];t=w.countries[target];c['government']=government
        c['focuses'].add('MKN_workers_corridors');w.froms=(target,target,target)
        check(w.test(one(decision,'available')),'MKN: valid workshop offer unavailable')
        w.apply(one(decision,'complete_effect'))
        check(w.flag(target,'MKN_workshop_exchange_pending') and len(w.events)==1,'MKN: offer did not queue recipient choice')
        check(not w.test(one(decision,'available')),'MKN: duplicate pending offer allowed')
        if choice=='war':t['wars'].add('MKN')
        elif choice=='subject':t['subject']=True
        elif choice=='capitulated':c['capitulated']=True
        elif choice=='mkn_gone':c['exists']=False
        elif choice=='expired':w.day=31
        elif choice=='duplicate':t['flags']['MKN_workshop_exchange_agreed']=-1
        w.root=target
        valid=choice in ('accept','decline')
        check(w.test(one(accept,'trigger'),target)==valid,'MKN: queued exchange accepts stale diplomacy')
        option=decline if choice=='decline' else accept
        w.apply([n for n in option if n[0] not in {'name','ai_chance','trigger'}],target)
        expected=1 if choice=='accept' else 0
        check(c.get('tech_bonus',0)==t.get('tech_bonus',0)==expected,'MKN: recipient refusal or invalid offer grants research')
        check(not w.flag(target,'MKN_workshop_exchange_pending'),'MKN: recipient choice leaves a pending request')
        if choice=='accept':
            w.apply([n for n in accept if n[0] not in {'name','ai_chance','trigger'}],target)
            check(c.get('tech_bonus',0)==t.get('tech_bonus',0)==1,'MKN: delayed duplicate acceptance repeats the exchange reward')
            w.root='MKN'
            check(not w.test(one(decision,'available')),'MKN: accepted exchange can be farmed repeatedly')
            check(c['opinions']=={(target,'MKN_workshop_exchange_opinion')} and t['opinions']=={('MKN','MKN_workshop_exchange_opinion')},'MKN: exchange opinion is not reciprocal')
        cases+=1
    # An invalidated decision returns its PP and never sends an offer.
    w=ForeignWorld();w.froms=('LTB',)*3;w.countries['LTB']['subject']=True
    before=w.countries['MKN']['pp'];w.apply(one(decision,'complete_effect'))
    check(w.countries['MKN']['pp']==before+50 and not w.events,'MKN: invalid queued exchange does not refund its price')
    print(f'PASS: MKN common foreign policy: all four governments, visible memorial connectors, one persistent service and {cases} consent/repair scenarios')
