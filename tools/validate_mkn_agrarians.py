"""Source-script regressions for MKN agrarian barter, traps and isolation.

Static models do not reproduce engine combat, decision UI or game AI.
"""
from copy import deepcopy
from itertools import product
import hashlib
import json
import re
from PIL import Image

from hoi4_script import read, one, values, walk, tree_focuses, engine_script_errors
from validate_mkn_free_soviets import SovietWorld


FOCUSES = {
    'MKN_great_rural_exodus': (88,5,'MKN_grain_ultimatum'),
    'MKN_black_partition_of_soil': (88,6,'MKN_great_rural_exodus'),
    'MKN_village_assembly_sovereignty': (88,7,'MKN_black_partition_of_soil'),
    'MKN_abolition_of_paper_money': (92,5,'MKN_grain_ultimatum'),
    'MKN_village_smithies_over_plants': (92,6,'MKN_abolition_of_paper_money'),
    'MKN_steppe_grain_monopoly': (92,7,'MKN_village_smithies_over_plants'),
    'MKN_hunters_of_the_steppe': (88,8,'MKN_every_farm_a_fortress'),
    'MKN_fortified_homesteads': (88,9,'MKN_hunters_of_the_steppe'),
    'MKN_traps_and_ambush_lines': (88,10,'MKN_fortified_homesteads'),
    'MKN_empty_field_doctrine': (90,11,'MKN_impregnable_granary'),
    'MKN_death_to_grain_thieves': (90,12,'MKN_empty_field_doctrine'),
    'MKN_chernozem_autarky': (90,13,'MKN_death_to_grain_thieves'),
}


class AgrarianWorld(SovietWorld):
    def __init__(self, root):
        super().__init__()
        self.countries['MKN'].update(government='neutrality',focuses={'MKN_steppe_grain_monopoly'})
        self.idea_definitions = dict((k,v) for k,v,o in one(one(read(root/'common/ideas/MKN_agrarian_ideas.txt'),'ideas'),'country'))
        self.project = None
        self.cooldown = 0

    def test(self, nodes, current='MKN', previous=None):
        for key,val,op in nodes or []:
            c = self.data(current)
            if key == 'any_owned_state':
                ok = any(s['owner']==current and self.test(val,sid,current) for sid,s in self.states.items())
            elif key == 'has_tech': ok = val in c.get('techs',set())
            elif key == 'has_offensive_war': ok = c.get('offensive_war',False) == (val=='yes')
            else: ok = super().test([(key,val,op)],current,previous)
            if not ok: return False
        return True

    def apply(self, nodes, current='MKN', previous=None):
        matched = False
        for key,val,op in nodes:
            c = self.data(current)
            if key in {'if','else_if'}:
                if key == 'if': matched = False
                if not matched and self.test(one(val,'limit'),current,previous):
                    self.apply([n for n in val if n[0]!='limit'],current,previous)
                    matched = True
            elif key == 'else':
                if not matched: self.apply(val,current,previous)
                matched = True
            elif key == 'add_timed_idea':
                token=one(val,'idea');already=token in c['ideas']
                super().apply([(key,val,op)],current,previous)
                if not already and token in self.idea_definitions:
                    self.apply(one(self.idea_definitions[token],'on_add',[]),current,previous)
            elif key == 'remove_ideas' and isinstance(val,str) and val in self.idea_definitions:
                if val in c['ideas']:
                    self.apply(one(self.idea_definitions[val],'on_remove',[]),current,previous)
                super().apply([(key,val,op)],current,previous)
            elif key == 'add_offsite_building':
                kind=one(val,'type');offsite=c.setdefault('offsite',{})
                offsite[kind]=offsite.get(kind,0)+int(one(val,'level'))
            elif key == 'set_technology':
                c.setdefault('techs',set()).update(k for k,v,o in val if v=='1')
            else:
                super().apply([(key,val,op)],current,previous)

    def can_start(self, decision):
        c=self.countries['MKN']
        return self.project is None and self.day>=self.cooldown and c['pp']>=float(one(decision,'cost')) and all(self.test(one(decision,k,[])) for k in ('visible','available'))

    def start(self, decision):
        assert self.can_start(decision)
        self.countries['MKN']['pp']-=float(one(decision,'cost'))
        self.apply(one(decision,'complete_effect'))
        self.project=(self.day+int(one(decision,'days_remove')),decision)

    def advance(self, days):
        for _ in range(days):
            self.day+=1
            if self.project:
                deadline,d=self.project
                if self.test(one(d,'cancel_trigger')):
                    self.apply(one(d,'cancel_effect'));self.project=None
                elif self.day>=deadline:
                    self.apply(one(d,'remove_effect'));self.project=None
                    self.cooldown=self.day+int(one(d,'days_re_enable'))
            for pair,deadline in list(self.timed.items()):
                if self.day>=deadline:
                    self.apply([('remove_ideas',pair[1],'=')],pair[0]);del self.timed[pair]


def validate_agrarians(root, game, check, localized):
    fs={one(f,'id'):f for f in tree_focuses(one(read(root/'common/national_focus/MKN.txt'),'focus_tree'),root/'common/national_focus')}
    for fid,(x,y,parent) in FOCUSES.items():
        f=fs[fid]
        check((one(f,'x'),one(f,'y'),one(f,'cost'))==(str(x),str(y),'5'),fid+': wrong location/duration')
        gate=one(f,'available')
        check(one(gate,'has_government')=='neutrality',fid+': missing neutrality gate')
        check(parent in values(one(f,'prerequisite',[]),'focus')+values(gate,'has_completed_focus'),fid+': missing predecessor')
        localized(fid,fid);localized(fid+'_desc',fid)
    ideas=one(one(read(root/'common/ideas/MKN_agrarian_ideas.txt'),'ideas'),'country')
    native=set(re.findall(r'^## (\w+)',(game/'documentation/modifiers_documentation.md').read_text(),re.M))
    categories={v for k,v,o in one(read(game/'common/technology_tags/00_technology.txt'),'technology_categories',[]) if k is None}
    for iid,idea,o in ideas:
        localized(iid,iid);localized(iid+'_desc',iid)
        check(all(k in native or k=='custom_modifier_tooltip' for k,v,o in one(idea,'modifier',[])),iid+': unknown modifier')
        for category,_,_ in one(idea,'research_bonus',[]):
            check(category in categories,iid+': undefined research category '+str(category))
    for path in root.glob('common/**/MKN_agrarian*.txt'):
        check(not list(engine_script_errors(read(path))),str(path)+': invalid engine syntax')
    tech=one(one(read(root/'common/technologies/MKN_agrarian_technologies.txt'),'technologies'),'MKN_steppe_hunter_training')
    units={k for path in (game/'common/units').glob('*.txt') for k,v,o in one(read(path),'sub_units',[])}
    for unit,node,o in tech:
        if unit in {'research_cost','allow'}:continue
        check(unit in units,'MKN hunters: undefined unit '+str(unit))
        check({k for k,v,o in node}=={'plains','forest'},'MKN hunters: unintended terrain bonus')
    decision=one(one(read(root/'common/decisions/MKN_decisions.txt'),'MKN_steppe_operations_category'),'MKN_barter_grain_surplus')
    localized('MKN_barter_grain_surplus','barter');localized('MKN_barter_grain_surplus_desc','barter')
    check((one(decision,'cost'),one(decision,'days_remove'),one(decision,'days_re_enable'))==('25','60','180'),'MKN barter: wrong price/timing')
    cases=0
    for pp,government,capitulated in product((24,25),('neutrality','democratic'),(False,True)):
        w=AgrarianWorld(root);c=w.countries['MKN'];c.update(pp=pp,government=government,capitulated=capitulated)
        check(w.can_start(decision)==(pp>=25 and government=='neutrality' and not capitulated),'MKN barter: incorrect affordability/regime boundary')
        cases+=1
    w=AgrarianWorld(root);c=w.countries['MKN'];pp=c['pp'];w.start(decision)
    w.advance(59);check(c['pp']==pp-25 and not c.get('offsite'),'MKN barter: premature reward')
    w.advance(1);check(c['pp']==pp+25 and c['offsite']['industrial_complex']==1,'MKN barter: missing PP/factory reward')
    before=(c['pp'],deepcopy(c['offsite']));w.apply(one(decision,'remove_effect'))
    check(before==(c['pp'],c['offsite']),'MKN barter: duplicate completion grants rewards')
    check(not w.can_start(decision),'MKN barter: active factory can be stacked')
    w.advance(179);check(c['offsite']['industrial_complex']==1,'MKN barter: factory expires prematurely')
    w.advance(1);check(c['offsite']['industrial_complex']==0 and 'MKN_grain_barter_factory_idea' not in c['ideas'],'MKN barter: temporary factory becomes permanent')
    w.apply(one(w.idea_definitions['MKN_grain_barter_factory_idea'],'on_remove'))
    check(c['offsite']['industrial_complex']==0,'MKN barter: duplicate removal subtracts a permanent factory')
    check(w.can_start(decision),'MKN barter: cannot restart after expiry/cooldown')
    w.start(decision);w.advance(60)
    check(c['offsite']['industrial_complex']==1 and c['pp']==pp+50,'MKN barter: second harvest stacks/loses factory')
    cases+=1
    for reason in ('government','capitulation','lost_land'):
        w=AgrarianWorld(root);c=w.countries['MKN'];pp=c['pp'];w.start(decision)
        if reason=='government':c['government']='democratic'
        elif reason=='capitulation':c['capitulated']=True
        else:
            for s in w.states.values():
                if s['owner']=='MKN':s['controller']='GER'
        w.advance(1);w.apply(one(decision,'cancel_effect'))
        check(c['pp']==pp and not c.get('offsite') and not w.flag('MKN','MKN_grain_barter_project_active'),'MKN barter: incorrect cancellation/refund at '+reason)
        cases+=1
    # Reload midway through a paid project and midway through a factory lease.
    for elapsed in (30,100):
        w=AgrarianWorld(root);w.start(decision);w.advance(elapsed)
        saved=deepcopy(w);saved.run('MKN_repair_agrarian_training');saved.run('MKN_sync_agrarian_defense')
        saved.advance(240-elapsed)
        c=saved.countries['MKN']
        check(c['offsite']['industrial_complex']==0 and c['pp']==525,'MKN barter: reload repeats PP or factory')
        cases+=1
    trapped=one(read(root/'common/dynamic_modifiers/MKN_agrarian_modifiers.txt'),'MKN_agrarian_trapped_roads')
    for owned,controlled,government in product((False,True),(False,True),('neutrality','democratic')):
        w=AgrarianWorld(root);c=w.countries['MKN'];c['ideas'].add('MKN_steppe_traps_idea');c['government']=government
        w.states['9000'].update(owner='MKN' if owned else 'GER',controller='MKN' if controlled else 'GER')
        check(w.test(one(trapped,'enable'),'9000')==(owned and controlled and government=='neutrality'),'MKN traps: effect enabled outside owned/controlled land')
        cases+=1
    for complete in (False,True):
        w=AgrarianWorld(root)
        if complete:w.countries['MKN']['focuses'].add('MKN_hunters_of_the_steppe')
        w.run('MKN_repair_agrarian_training');w.run('MKN_repair_agrarian_training')
        check(('MKN_steppe_hunter_training' in w.countries['MKN'].get('techs',set()))==complete,'MKN hunters: repair missing or grants unearned training')
        cases+=1
    final=one(fs['MKN_chernozem_autarky'],'available')
    for subject,faction,offensive in product((False,True),repeat=3):
        w=AgrarianWorld(root);c=w.countries['MKN'];c.update(subject=subject,faction='SOV' if faction else None,offensive_war=offensive)
        check(w.test(final)==(not(subject or faction or offensive)),'MKN autarky: available before resolving external obligations')
        cases+=1
    rules=one(one(ideas,'MKN_chernozem_autarky_idea'),'rule')
    check(one(rules,'can_not_declare_war')=='yes' and one(rules,'can_join_factions')==one(rules,'can_create_factions')=='no','MKN autarky: missing real diplomatic restrictions')
    art=json.loads((root/'docs/art/mkn_political_expansions/assets.json').read_text(encoding='utf-8'))
    sprites={one(s,'name'):s for s in values(one(read(root/'interface/MKN_political_expansions.gfx'),'spriteTypes'),'spriteType')}
    check(len(art['assets'])==36 and len(sprites)==72,'MKN artwork: incomplete political icon set')
    source_hashes=set()
    for asset in art['assets']:
        fid=asset['focus'];source=root/asset['source'];texture=root/asset['texture']
        source_hash=hashlib.sha256(source.read_bytes()).hexdigest();source_hashes.add(source_hash)
        check(source_hash==asset['source_sha256'] and (root/asset['prompt']).is_file(),fid+': missing original or exact imagegen prompt')
        check(hashlib.sha256(texture.read_bytes()).hexdigest()==asset['texture_sha256'],fid+': DDS differs from reviewed export')
        check(one(fs[fid],'icon')==asset['sprite'],fid+': unique artwork is not connected')
        for token in (asset['sprite'],asset['sprite']+'_shine'):
            check(one(sprites[token],'texturefile')==asset['texture'],fid+': wrong sprite texture')
        for animation in values(sprites[asset['sprite']+'_shine'],'animation'):
            check(one(animation,'animationmaskfile')==asset['texture'],fid+': wrong highlight mask')
        with Image.open(texture) as image:
            check(image.size==(96,96) and image.mode=='RGBA',fid+': invalid native canvas')
            bounds=image.getchannel('A').getbbox()
            check(list(bounds)==asset['occupied_alpha_bounds'] and bounds[0]>=6 and bounds[1]>=6 and bounds[2]<=90 and bounds[3]<=90,fid+': insufficient transparent clearance')
    check(len(source_hashes)==36,'MKN artwork: duplicate images assigned to distinct focuses')
    print('PASS: MKN political artwork: 36 distinct imagegen originals/prompts, 96x96 RGBA DDS, alpha margins and 72 normal/shine sprites')
    print(f'PASS: MKN agrarians: 12 focuses, native equipment/research/terrain, barter cancellation/expiry/reload and {cases} source-script cases; no runtime claim')
