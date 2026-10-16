"""Check MKN common industry/science, retired archive and equal service programmes."""
from itertools import permutations, product
import json
from hoi4_script import read,one,values,walk,tree_focuses,focus_registry
from validate_mkn_ukraine import World


def validate_tree_consolidation(root, game, check, localized):
    contract=json.loads((root/'docs/MKN_tree_consolidation.json').read_text())
    tree=one(read(root/'common/national_focus/MKN.txt'),'focus_tree')
    fs={one(f,'id'):f for f in tree_focuses(tree,root/'common/national_focus')}
    registry=focus_registry(root/'common/national_focus')
    retired=set(contract['retired'])
    check(len(retired)==35 and not retired & fs.keys(),'MKN: preparation/archive branch is still playable')
    for fid in retired | set(contract['retired_science']):
        node=registry[fid]
        check(one(one(node,'allow_branch'),'always')=='no' and not one(node,'completion_reward'),fid+': compatibility token has playable rewards')
    for fid,f in fs.items():
        for p in values(f,'prerequisite'):
            check(not set(values(p,'focus')) & retired,fid+': active prerequisite still needs a retired focus')
    check(one(one(tree,'initial_show_position'),'focus')=='MKN_congress_1936','MKN: initial camera points at retired archive')
    chain=contract['science_chain']
    for a,b in zip(chain,chain[1:]):
        if b=='MKN_dnieper_jet_falcons':continue
        # Parallel rocket/jet applications converge using an OR prerequisite.
        parents={p for g in values(fs[b],'prerequisite') for p in values(g,'focus')}
        wanted='MKN_open_peer_review' if b=='MKN_jet_tachankas' else a
        check(wanted in parents,b+': broken shared science continuation')
    bridge=fs['MKN_free_workshops_focus']
    check(set(values(one(bridge,'prerequisite'),'focus'))=={'MKN_steel_volnitsa','MKN_communal_compact'},'MKN: workshops must follow either industrial finale')
    for path in ('MKN_steel_volnitsa','MKN_communal_compact'):
        done={path,'MKN_steppe_hawks_and_schools'}
        for fid in chain:
            groups=values(fs[fid],'prerequisite')
            check(all(any(p in done for p in values(g,'focus')) for g in groups),path+': common science is not reachable at '+fid)
            done.add(fid)
    check(not any(k=='date' for fid in chain for k,v,o in walk(one(fs[fid],'available',[]))),'MKN: shared science retains a calendar gate')
    check(max(int(one(f,'x')) for f in fs.values())==128,'MKN: removed archive columns left a wide gap')
    check(min(int(one(fs[f],'x')) for f in ('MKN_motorized_vanguard','MKN_steppe_horde'))==24,'MKN: army has not shifted beside industry')
    slots=contract['research_slot_focuses']
    all_slots=[fid for fid,f in fs.items() if any(k=='add_research_slot' for k,v,o in walk(one(f,'completion_reward',[])))]
    check(set(all_slots)==set(slots)|{'MKN_kyiv_scientific_exchange', 'MKN_ferrer_modern_schools'},'MKN: unexpected research slot source')
    check(one(read(root/'history/countries/MKN - Makhnovists.txt'),'set_research_slots')=='3','MKN: expected three starting research slots')
    cases=0
    # The two common institutions stop at five. Kyiv is available only once
    # both institutions are completed; it is the sixth slot in a fresh game.
    for initial,order in product(range(3,7),permutations(slots)):
        world=World();c=world.countries['MKN'];c['slots']=initial
        for fid in order:
            c['focuses'].add(fid)
            world.apply(one(fs[fid],'completion_reward'))
        check(c['slots']==max(initial,5),'MKN: core science must stop at five without Ukraine')
        c['focuses'].add('MKN_kyiv_scientific_exchange')
        world.apply(one(fs['MKN_kyiv_scientific_exchange'],'completion_reward'))
        check(c['slots']==6,'MKN: Kyiv must provide the sixth slot')
        cases+=1
    kyiv=one(fs['MKN_kyiv_scientific_exchange'],'available')
    check(set(values(kyiv,'has_completed_focus'))==set(slots),'MKN: Kyiv science lacks common institutional preparation')
    homeland=json.loads((root/'docs/MKN_ukraine_integration.json').read_text())['states']
    for first,second,capacity in product((False,True),(False,True),(4,5,6)):
        world=World();c=world.countries['MKN'];c['slots']=capacity
        world.countries['UKR']['exists']=False
        for sid in homeland:
            world.states[str(sid)]['owner']=world.states[str(sid)]['controller']='MKN'
        c['focuses']={fid for fid,done in zip(slots,(first,second)) if done}
        check(world.test(kyiv)==(first and second and capacity>=5),'MKN: Kyiv science opens before its fifth slot/institutions')
        cases+=1
    for initial,complete,ukraine in product(range(3,8),(False,True),(False,True)):
        world=World();c=world.countries['MKN'];c['slots']=initial
        c['focuses']=set(slots if complete else slots[:-1])
        if ukraine:c['focuses'].add('MKN_kyiv_scientific_exchange')
        before=(c['pp'],dict(c.get('buildings',{})),c.get('tech_bonus',0))
        world.run('MKN_repair_research_capacity');world.run('MKN_repair_research_capacity')
        floor=6 if ukraine else 5
        check(c['slots']==(max(initial,floor) if complete else initial),'MKN: research repair gives a sixth slot before integration or removes an earned slot')
        check(before==(c['pp'],dict(c.get('buildings',{})),c.get('tech_bonus',0)),'MKN: research repair replays non-capacity rewards')
        cases+=1
    groups=json.loads((root/'docs/MKN_military_refactor.json').read_text())['groups']
    programmes=json.loads((root/'docs/MKN_military_programs.json').read_text())
    for p in programmes:
        route=p['focuses']
        check(len(route)==5 and len(set(route))==5,p['entry']+': expected exactly five reforms')
        for before,after in zip(route,route[1:]):
            check(values(one(fs[after],'prerequisite'),'focus')==[before],after+': broken service programme chain')
        check(route[-1]==p['finale'],p['entry']+': finale moved before an added reform')
    native=set(__import__('re').findall(r'^## (\w+)',(game/'documentation/modifiers_documentation.md').read_text(),__import__('re').M))
    dynamic=read(root/'common/dynamic_modifiers/nww_dynamic_modifiers.txt')
    for fid,stats in contract['new_military'].items():
        localized(fid,fid);localized(fid+'_desc',fid);localized(fid+'_tt',fid)
        f=fs[fid];service=next(g['service'] for g in groups if g['id']==fid)
        check(one(f,'cost')=='10',fid+': new major reform must take 70 days')
        spirit=one(dynamic,'MKN_'+service+'_development')
        for var in stats:
            names=[k for k,v,o in spirit if v==var]
            check(len(names)==1 and names[0] in native,fid+': new bonus does not use a registered native service modifier')
    print(f'PASS: MKN tree consolidation: 35 retired archive focuses and one retired school, shared industry/science, 6 research slots in {cases} reward-order/save scenarios, six equal five-focus programmes')
