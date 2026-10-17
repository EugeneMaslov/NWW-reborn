"""Split Dedeagach from Western Thrace, retaining Bulgaria's 1913 coastline.

No province bitmap, strategic region, supply node or railway is recreated.
Building placements are reassigned using the actual province bitmap.
"""
from collections import Counter
from copy import deepcopy
import csv,json
from pathlib import Path
from PIL import Image,ImageChops
from hoi4_script import read,one,values,parse,dump

ROOT=Path(__file__).resolve().parents[1]
GAME=Path('D:/Steam/steamapps/common/Hearts of Iron IV')


def save(path,doc):
    (ROOT/path).write_text(dump(doc)+'\n',encoding='utf-8',newline='\n')


def main():
    doc=read(ROOT/'history/states/184-Thrace.txt');state=one(doc,'state')
    state[:]=[(k,'260000' if k=='manpower' else '6.0' if k=='local_supplies' else v,o) for k,v,o in state]
    provinces=one(state,'provinces');provinces[:]=[e for e in provinces if e[1]!='11905']
    history=one(state,'history')
    history[:]=[e for e in history if e[0] not in ('owner','victory_points','add_claim_by')]
    history+=parse('owner = BUL')
    if 'BUL' not in values(history,'add_core_of'):history+=parse('add_core_of = BUL')
    resources=one(state,'resources');resources[:]=parse('chromium = 8')
    save('history/states/184-Thrace.txt',doc)
    save('history/states/1083-Dedeagach.txt',parse('''state = {
 id = 1083 name = STATE_1083 manpower = 122500 state_category = rural
 resources = { chromium = 3 }
 history = {
  owner = BUL add_core_of = BUL add_core_of = GRE
  victory_points = { 11905 1 }
  buildings = { infrastructure = 1 11905 = { naval_base = 1 } }
 }
 provinces = { 11905 }
 local_supplies = 3.0
}'''))
    definition=ROOT/'map/definition.csv'
    if not definition.exists():definition=GAME/'map/definition.csv'
    colors={}
    with definition.open(encoding='utf-8-sig') as f:
        for row in csv.reader(f,delimiter=';'):
            if row and row[0].isdigit():colors[tuple(map(int,row[1:4]))]=row[0]
    bitmap=ROOT/'map/provinces.bmp'
    if not bitmap.exists():bitmap=GAME/'map/provinces.bmp'
    im=Image.open(bitmap).convert('RGB')
    path=ROOT/'map/buildings.txt'
    source=path if path.exists() else GAME/'map/buildings.txt'
    lines=source.read_text(encoding='utf-8-sig').splitlines()
    templates={};seen={}
    for i,line in enumerate(lines):
        fields=line.split(';')
        if len(fields)!=7 or fields[0] not in ('184','1083'):continue
        if fields[0]=='184':
            templates.setdefault(fields[1],fields[:])
            pixel=(int(float(fields[2])),im.height-1-int(float(fields[4])))
            pid=colors.get(im.getpixel(pixel))
            if pid=='11905':fields[0]='1083';lines[i]=';'.join(fields)
        seen.setdefault(fields[0],set()).add(fields[1])
    # Pick an interior pixel for each state for missing mandatory spawn sites.
    for sid,pid in [('184','11774'),('1083','11905')]:
        color=next(c for c,p in colors.items() if p==pid)
        diff=ImageChops.difference(im,Image.new('RGB',im.size,color))
        r,g,b=diff.split();mask=ImageChops.lighter(ImageChops.lighter(r,g),b).point(lambda p:255 if p==0 else 0)
        box=mask.getbbox();cx=(box[0]+box[2])//2;cy=(box[1]+box[3])//2
        candidates=[(x,y) for y in range(box[1],box[3]) for x in range(box[0],box[2]) if mask.getpixel((x,y))]
        x,y=min(candidates,key=lambda p:(p[0]-cx)**2+(p[1]-cy)**2)
        for kind in ('air_base','rocket_site_spawn','nuclear_reactor_spawn','special_project_facility_spawn'):
            if kind in seen.get(sid,set()):continue
            fields=templates[kind][:];fields[0]=sid;fields[2]=f'{x:.2f}';fields[4]=f'{im.height-1-y:.2f}'
            lines.append(';'.join(fields))
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
    # Country-specific objectives must follow their new owners.
    path=ROOT/'docs/TUR_balkan_objectives.json';meta=json.loads(path.read_text(encoding='utf-8'))
    meta['BUL'][1]=sorted(set(meta['BUL'][1])|{184,1083})
    meta['GRE'][1]=[s for s in meta['GRE'][1] if s!=184]
    path.write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8',newline='\n')
    doc=read(ROOT/'common/national_focus/TUR_focuses.txt')
    fs={one(f,'id'):f for f in values(one(doc,'focus_tree'),'focus')}
    for fid in ('TUR_snova_copi','NWW_TUR_greek_settlement'):
        for key in ('available','bypass','completion_reward'):
            body=one(fs[fid],key,[]);body[:]=[e for e in body if e[0]!='184']
    for fid,key in [('TUR_war_with_bulgaria','bypass'),('afg_bolgi','available'),('afg_bolgi','completion_reward')]:
        body=one(fs[fid],key)
        for sid in ('184','1083'):
            if one(body,sid) is None:
                body+=parse(sid+' = { '+('add_compliance = 10' if key=='completion_reward' else 'is_owned_and_controlled_by = ROOT')+' }')
    for fid in ('NWW_TUR_balkan_mandate','NWW_TUR_rumelian_governorates'):
        body=one(fs[fid],'available')
        if one(body,'1083') is None:body+=parse('1083 = { is_owned_and_controlled_by = ROOT }')
    save('common/national_focus/TUR_focuses.txt',doc)
    doc=read(ROOT/'common/scripted_effects/TUR_effects.txt')
    for name,remove,add in [('nww_TUR_prepare_gre_campaign',{'184'},set()),('nww_TUR_prepare_bul_campaign',set(),{'184','1083'})]:
        body=one(one(doc,name),'if')
        body[:]=[e for e in body if not(e[0]=='add_state_claim' and e[1] in remove)]
        for sid in sorted(add):
            if sid not in values(body,'add_state_claim'):body.append(('add_state_claim',sid,'='))
    save('common/scripted_effects/TUR_effects.txt',doc)
    # Move the two native Greek divisions stranded by the border correction.
    owners={}
    effective={p.name:p for p in (GAME/'history/states').glob('*.txt')};effective.update({p.name:p for p in (ROOT/'history/states').glob('*.txt')})
    for p in effective.values():
        s=one(read(p),'state');owner=one(one(s,'history',[]),'owner')
        for k,pid,o in one(s,'provinces',[]):owners[pid]=owner
    unitpath=ROOT/'history/units/GRE_1936.txt'
    source=unitpath if unitpath.exists() else GAME/'history/units/GRE_1936.txt'
    doc=read(source);divs=values(one(doc,'units'),'division')
    counts=Counter(one(d,'location') for d in divs if owners.get(one(d,'location'))=='GRE')
    for d in divs:
        if owners.get(one(d,'location'))=='GRE':continue
        target=min(counts,key=lambda p:(counts[p],int(p)));counts[target]+=1
        d[:]=[(k,target if k=='location' else v,o) for k,v,o in d]
    save('history/units/GRE_1936.txt',doc)
    manifestpath=ROOT/'docs/1936_deployment_manifest.json';manifest=json.loads(manifestpath.read_text(encoding='utf-8'))
    manifest['GRE_1936.txt']={'divisions':len(divs),'positions':len({one(d,'location') for d in divs})}
    manifestpath.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
    for lang,name in [('russian','Дедеагач'),('english','Dedeagach')]:
        (ROOT/f'localisation/{lang}/NWW_thrace_l_{lang}.yml').write_text('l_'+lang+':\n STATE_1083:0 "'+name+'"\n',encoding='utf-8-sig',newline='\n')
    print('Split 184/1083: Bulgarian Western Thrace and Dedeagach; building positions and Turkish objectives updated.')


if __name__=='__main__':main()
