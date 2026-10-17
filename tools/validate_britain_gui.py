"""Validate read-only British panels and compose a labelled layout preview."""
from pathlib import Path
import json
import math
import re
from PIL import Image, ImageDraw, ImageFont
from hoi4_script import read, one, values
from test_britain_lifecycle import World

ROOT=Path(__file__).resolve().parents[1]
P='ENG_nww_'


def load():
    windows={one(v,'name'):v for v in values(one(read(ROOT/'interface/ENG_mechanics.gui'),'guiTypes'),'containerWindowType')}
    scripts=dict((k,v) for k,v,_ in one(read(ROOT/'common/scripted_guis/ENG_mechanics.txt'),'scripted_gui'))
    sprites={one(v,'name'):v for file in ['ENG_icons.gfx','ENG_mechanics.gfx'] for v in values(one(read(ROOT/'interface'/file),'spriteTypes'),'spriteType')}
    return windows,scripts,sprites


def validate_gui(check):
    windows,scripts,sprites=load()
    layout=json.loads((ROOT/'docs/art/ENG/mechanics/layout.json').read_text(encoding='utf-8'))
    cats=read(ROOT/'common/decisions/categories/ENG_categories.txt')
    world=World();eng=world.country('ENG')
    localized={lang:{m[1] for m in re.finditer(r'^\s+(\S+):\d+ ',(ROOT/f'localisation/{lang}/ENG_nww_l_{lang}.yml').read_text(encoding='utf-8-sig'),re.M)} for lang in ['russian','english']}
    for panel in layout['panels']:
        name=panel['name'];script=scripts[P+name+'_ui'];window=windows[one(script,'window_name')]
        check(one(one(cats,P+name+'_category'),'scripted_gui')==P+name+'_ui',name+': unbound category')
        check(one(script,'context_type')=='decision_category',name+': incorrect scope')
        check(world.test(one(script,'visible')),name+': hidden from Britain')
        check(not world.test(one(script,'visible'),'CAN'),name+': visible to Canada')
        eng.tree='other_tree';check(not world.test(one(script,'visible')),name+': visible with native tree');eng.tree='ENG_nww_focus'
        check(not any(one(script,k) is not None for k in ['effects','clicks']),name+': panel must remain read-only')
        names=[]
        for kind,element,_ in window:
            if kind not in ['iconType','instantTextBoxType']:continue
            names.append(one(element,'name'))
            for key in ['text','pdx_tooltip']:
                if one(element,key):
                    for lang,keys in localized.items():check(one(element,key) in keys,lang+': missing '+one(element,key))
            pos=one(element,'position');x=float(one(pos,'x'))+220;y=float(one(pos,'y'))
            if kind=='iconType':
                sprite=one(element,'spriteType');check(sprite in sprites,'Unknown GUI sprite '+sprite)
                if sprite not in sprites:continue
                texture=ROOT/one(sprites[sprite],'texturefile')
                check(texture.exists(),'Missing '+str(texture))
                if not texture.exists():continue
                with Image.open(texture) as im:w,h=im.size
            else:w=float(one(element,'maxWidth'));h=float(one(element,'maxHeight'))
            check(x>=0 and y>=0 and x+w<=440 and y+h<=panel['height'],one(element,'name')+': outside panel bounds')
        check(len(names)==len(set(names)),name+': duplicate elements')
        for key,_,_ in one(script,'triggers',[]):
            check(key.endswith('_visible') and key[:-8] in names,'Unbound visibility trigger '+key)
    checks=0
    for meter in layout['meters']:
        script=scripts[P+meter['panel']+'_ui'];triggers=one(script,'triggers')
        for value in ([0,1,2,3,4] if meter['maximum']==4 else [0,4,5,24,25,39,40,49,50,64,65,69,70,99,100]):
            eng.vars[meter['var']]=value
            lit=sum(world.test(one(triggers,P+'ui_'+meter['name']+f'_fill_{i}_visible')) for i in range(20))
            check(lit==math.floor(value*20/meter['maximum']+1e-8),meter['name']+f': wrong fill at {value}')
            checks+=1
        if meter['name'].startswith('trust_'):
            tag=meter['name'][-3:];partner=world.country(tag);eng.vars[meter['var']]=100
            for state in ['absent','foreign_subject','capitulated','enemy']:
                partner.exists=state!='absent';partner.subject='GER' if state=='foreign_subject' else 'ENG'
                partner.capitulated=state=='capitulated';partner.war=eng.war=state=='enemy'
                check(not any(world.test(one(triggers,P+'ui_'+meter['name']+f'_fill_{i}_visible')) for i in range(20)),tag+': stale trust fill '+state)
                checks+=1
            partner.exists=True;partner.subject='ENG';partner.capitulated=False;partner.war=eng.war=False
    # Pending treaties must not masquerade as ratified ones; absent partners show no treaty badge.
    triggers=one(scripts[P+'imperial_ui'],'triggers')
    for mode in ['federal','compact','independence']:
        eng.flags={P+'request_'+mode+'_CAN'}
        check(not world.test(one(triggers,P+'ui_'+mode+'_CAN_visible')),'Pending offer displayed as treaty')
        eng.flags={P+mode+'_CAN'}
        check(world.test(one(triggers,P+'ui_'+mode+'_CAN_visible')),'Ratified treaty hidden')
        world.country('CAN').exists=False
        check(not world.test(one(triggers,P+'ui_'+mode+'_CAN_visible')),'Absent country treaty shown')
        world.country('CAN').exists=True
    eng.flags=set();triggers=one(scripts[P+'routes_ui'],'triggers');eng.vars[P+'route_cape']=0
    check(world.test(one(triggers,P+'ui_cape_unprepared_visible')),'Unprepared Cape misreported')
    check(not world.test(one(triggers,P+'ui_cape_blocked_visible')),'Unprepared Cape marked disrupted')
    eng.flags.add(P+'cape_ready')
    check(world.test(one(triggers,P+'ui_cape_blocked_visible')),'Prepared inaccessible Cape not disrupted')
    for count in range(5):
        eng.vars[P+'open_routes']=count
        check(world.test(one(triggers,P+'ui_route_warning_visible'))==(count<3),'Route project warning boundary')
        check(world.test(one(triggers,P+'ui_route_normal_visible'))==(count>=3),'Route project readiness boundary')
    cabinet=one(scripts[P+'cabinet_ui'],'triggers')
    for flags,expected in [(set(),'monitor'),({P+'irish_final'},'settled'),({P+'irish_deadline_active'},'deadline'),({P+'irish_final',P+'irish_deadline_active'},'deadline')]:
        eng.flags=flags
        shown=[name for name in ['monitor','settled','deadline'] if world.test(one(cabinet,P+'ui_'+name+'_visible'))]
        check(shown==[expected],'Inconsistent Irish status '+str(flags))
    print(f'PASS: ENG decision GUI: 3 bound panels, element bounds, live gauges ({checks} boundary/state cases), treaty badges and Cape preparation')


def preview():
    windows,scripts,sprites=load();world=World();eng=world.country('ENG')
    for tag,value in [('CAN',75),('AST',65),('SAF',24),('NZL',55),('RAJ',40)]:eng.vars[P+'trust_'+tag]=value
    eng.flags={P+'conference_active',P+'compact_CAN',P+'federal_AST',P+'irish_deadline_active'}
    eng.vars.update({P+'compact_count':2,P+'federal_count':1,P+'labour_mandate':40,P+'irish_pressure':73,P+'open_routes':3,
                     P+'route_atlantic':1,P+'route_suez':1,P+'route_cape':0,P+'route_indian':1})
    loc={}
    for line in (ROOT/'localisation/russian/ENG_nww_l_russian.yml').read_text(encoding='utf-8-sig').splitlines():
        m=re.match(r'\s+(\S+):\d+ "(.*)"$',line)
        if m:loc[m[1]]=m[2]
    font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',15)
    small=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',14)
    canvas=Image.new('RGB',(940,790),(13,19,27));draw=ImageDraw.Draw(canvas)
    draw.text((20,12),'NWW REBORN · ВЕЛИКОБРИТАНИЯ',font=font,fill=(222,204,154))
    draw.text((20,37),'Предпросмотр компоновки · демонстрационные значения · не снимок из игры',font=small,fill=(160,173,190))
    for panel,(ox,oy) in {'imperial':(20,79),'cabinet':(480,79),'routes':(480,389)}.items():
        script=scripts[P+panel+'_ui'];triggers=one(script,'triggers')
        for kind,element,_ in windows[one(script,'window_name')]:
            if kind not in ['iconType','instantTextBoxType']:continue
            name=one(element,'name');condition=one(triggers,name+'_visible')
            if condition is not None and not world.test(condition):continue
            pos=one(element,'position');x=ox+220+int(one(pos,'x'));y=oy+int(one(pos,'y'))
            if kind=='iconType':
                im=Image.open(ROOT/one(sprites[one(element,'spriteType')],'texturefile')).convert('RGBA')
                canvas.paste(im,(x,y),im)
            else:
                label=loc[one(element,'text')]
                label=re.sub(r'\[\?(\w+)\|0\]',lambda m:str(eng.vars.get(m[1],0)),label)
                if draw.textlength(label,font=font)>int(one(element,'maxWidth')):
                    raise AssertionError('Preview text overflows: '+label)
                draw.text((x,y),label,font=font,fill=(225,221,203))
    draw.text((20,565),'Шкалы: шаг 5 пунктов + точное число.',font=small,fill=(160,173,190))
    draw.text((20,589),'Риски доверия: 25 · торговля: 40 · федерация: 65.',font=small,fill=(160,173,190))
    draw.text((20,613),'Порог лейбористского мандата: 40.',font=small,fill=(160,173,190))
    draw.text((20,637),'Ольстер: ниже 50 / кризис с 70.',font=small,fill=(160,173,190))
    draw.text((20,661),'Морские статусы учитывают базы и конвои.',font=small,fill=(160,173,190))
    canvas.save(ROOT/'docs/art/ENG/mechanics/preview.png')


if __name__=='__main__':
    errors=[]
    validate_gui(lambda ok,message: errors.append(message) if not ok else None)
    if errors:raise SystemExit('\n'.join(errors))
    preview()
