"""Read-only ENG decision panels. Geometric UI primitives, not painted artwork."""
from pathlib import Path
from PIL import Image, ImageDraw
import json

ROOT = Path(__file__).resolve().parents[1]
P = 'ENG_nww_'
PARTNERS = [('CAN','Канада','Canada'),('AST','Австралия','Australia'),
            ('SAF','Южная Африка','South Africa'),('NZL','Новая Зеландия','New Zealand'),
            ('RAJ','Индия','India')]
HEIGHTS = {'imperial':458, 'cabinet':290, 'routes':366}


def ck(var, value, compare='greater_than_or_equals'):
    return f'check_variable = {{ var = {P+var} value = {value} compare = {compare} }}'


def eligible(tag):
    return f'{tag} = {{ exists = yes has_capitulated = no NOT = {{ has_war_with = ENG }} OR = {{ is_subject = no is_subject_of = ENG }} }}'


def emit_gui(write, loc):
    gui=[]; scripts=[]; manifest={'panels':[], 'meters':[]}
    for cat,ru,en in [
        ('imperial','Доверие облегчает переговоры; каждый участник сохраняет право отказа.','Trust helps negotiations; every participant retains the right to refuse.'),
        ('cabinet','Мандат реформ и ирландский вопрос определяют свободу действий кабинета.','The reform mandate and the Irish question determine the cabinet’s room for action.'),
        ('routes','Базы и транспортный резерв связывают метрополию с заморскими проектами.','Bases and transport reserves connect Britain to its overseas projects.')]:
        loc(P+cat+'_category_desc',ru,en)
    def L(key,ru,en):
        key=P+'ui_'+key;loc(key,ru,en);return key
    trust_help=L('trust_help','Доверие: 0–100. Ниже 25 — риск кризиса; 40 — порог торгового предложения; 65 — порог федеративного предложения. Получатель сохраняет право отказа. Неучаствующие страны не заполняют шкалу.',
                 'Trust: 0–100. Below 25: crisis risk; 40: trade offer threshold; 65: federal offer threshold. Recipients may refuse. Ineligible countries do not fill the gauge.')
    mandate_help=L('mandate_help','Мандат лейбористской программы: 0–100. Для победы на выборах требуется 40. Кампания занимает 35 дней и добавляет 10 пунктов. Остальные условия фокуса сохраняются.',
                   'Labour programme mandate: 0–100. An election victory requires 40. A 35-day campaign adds 10 points. Other focus requirements still apply.')
    irish_help=L('irish_help','Напряжённость: 0–100. При 70 начинается кризис с миссией на 180 дней. Для снятия ультиматума снизьте напряжённость ниже 50 или заключите соглашение. Шкала показывает давление, статус — итог урегулирования.',
                 'Tension: 0–100. At 70, a crisis starts with a 180-day mission. Reduce tension below 50 or reach an agreement to end the ultimatum. The gauge shows pressure; the status shows the settlement.')
    route_help=L('route_help','Доступ проверяется ежедневно: контроль ключевой базы Британией, союзником или страной, предоставляющей военный доступ, и резерв не менее 100 конвоев. Для мыса нужен подготовительный фокус. Это доступность баз, а не превосходство на море. При двух недоступных направлениях новые заморские проекты приостановлены.',
                 'Checked daily: key base control by Britain, a faction partner or a country granting military access, plus at least 100 convoys. The Cape requires its preparation focus. This measures base access, not naval supremacy. Two unavailable routes suspend new overseas projects.')
    for panel,height in HEIGHTS.items():
        elements=[];triggers=[]
        def icon(name,sprite,x,y,tip=None,condition=None):
            name=P+'ui_'+name
            elements.append(f'iconType = {{ name = "{name}" spriteType = "{sprite}" orientation = center_up position = {{ x = {x-220} y = {y} }}'+(f' pdx_tooltip = {tip}' if tip else '')+' }')
            if condition:triggers.append(name+'_visible = { '+condition+' }')
        def text(name,key,x,y,width=380,condition=None,tip=None):
            name=P+'ui_'+name
            elements.append(f'instantTextBoxType = {{ name = "{name}" orientation = center_up position = {{ x = {x-220} y = {y} }} font = "hoi_16mbs" text = "{key}" format = left maxWidth = {width} maxHeight = 20'+(f' pdx_tooltip = {tip}' if tip else '')+' }')
            if condition:triggers.append(name+'_visible = { '+condition+' }')
        def meter(name,var,y,tip,marks,gate='',reverse=False,maximum=100):
            manifest['meters'].append({'name':name,'var':P+var,'panel':panel,'y':y,'gate':gate,'maximum':maximum})
            for i in range(20):
                icon(name+f'_socket_{i}','GFX_ENG_ui_socket',30+i*19,y,tip)
                threshold=(i+1)*maximum/20
                # One segment is five points; exact values remain visible above.
                condition=gate+' '+ck(var,threshold)
                color='red' if reverse else 'gold'
                icon(name+f'_fill_{i}','GFX_ENG_ui_'+color,30+i*19,y,tip,condition)
            for mark in marks:
                icon(name+f'_mark_{mark}','GFX_ENG_ui_tick',30+round(380*mark/maximum)-1,y-3,tip)
        icon(panel+'_background','GFX_ENG_ui_'+panel,0,0)
        icon(panel+'_emblem','GFX_decision_category_'+P+panel,14,9)
        title={'imperial':('ИМПЕРСКИЙ ДОГОВОР','THE IMPERIAL TREATY'),
               'cabinet':('ВЕСТМИНСТЕР','WESTMINSTER'), 'routes':('МОРСКИЕ АРТЕРИИ','IMPERIAL SEA ARTERIES')}[panel]
        text(panel+'_title',L(panel+'_title',*title),78,18,340)
        if panel=='imperial':
            for i,(tag,ru,en) in enumerate(PARTNERS):
                y=65+i*64;gate=eligible(tag)
                text('trust_'+tag,L('trust_'+tag,ru+f' — [?{P}trust_{tag}|0]/100',en+f' — [?{P}trust_{tag}|0]/100'),30,y,condition=gate,tip=trust_help)
                text('absent_'+tag,L('absent_'+tag,ru+' — вне переговоров',en+' — unavailable'),30,y,condition='NOT = { '+gate+' }',tip=trust_help)
                meter('trust_'+tag,'trust_'+tag,y+24,trust_help,[25,40,65],gate)
                preceding=[]
                for mode,r,e in [('federal','Федеративный договор','Federal treaty'),('compact','Торговый договор','Trade compact'),('independence','Договор независимости','Independence treaty')]:
                    flag='has_country_flag = '+P+mode+'_'+tag
                    cond=gate+' '+flag+(' NOT = { OR = { '+' '.join(preceding)+' } }' if preceding else '')
                    text(mode+'_'+tag,L(mode,r,e),30,y+39,condition=cond)
                    preceding.append(flag)
                text('no_treaty_'+tag,L('no_treaty','Нет ратифицированного договора','No ratified treaty'),30,y+39,condition=gate+' NOT = { OR = { '+' '.join(preceding)+' } }')
            text('imperial_totals',L('imperial_totals','Торговые: [?ENG_nww_compact_count|0]   Федеративные: [?ENG_nww_federal_count|0]',
                 'Trade: [?ENG_nww_compact_count|0]   Federal: [?ENG_nww_federal_count|0]'),30,395)
            for flag,r,e in [('yes','Конференция открыта','Conference in session'),('no','Конференция закрыта','Conference in recess')]:
                cond='has_country_flag = '+P+'conference_active'
                if flag=='no':cond='NOT = { '+cond+' }'
                text('conference_'+flag,L('conference_'+flag,r,e),30,421,condition=cond)
        elif panel=='cabinet':
            text('mandate_value',L('mandate_value','Мандат лейбористов: [?ENG_nww_labour_mandate|0]/100','Labour mandate: [?ENG_nww_labour_mandate|0]/100'),30,66,tip=mandate_help)
            meter('mandate','labour_mandate',94,mandate_help,[40])
            text('mandate_threshold',L('mandate_threshold','40 — мандат на смену кабинета','40 — mandate for a new cabinet'),30,111,tip=mandate_help)
            text('irish_value',L('irish_value','Ольстер: [?ENG_nww_irish_pressure|0]/100','Ulster tension: [?ENG_nww_irish_pressure|0]/100'),30,155,tip=irish_help)
            meter('irish','irish_pressure',183,irish_help,[50,70],reverse=True)
            text('irish_thresholds',L('irish_thresholds','<50 — деэскалация; 70 — кризис','<50 — de-escalation; 70 — crisis'),30,201,tip=irish_help)
            active='has_country_flag = '+P+'irish_deadline_active'
            final='has_country_flag = '+P+'irish_final'
            for name,r,e,cond in [
                ('deadline','Ультиматум: действует миссия','Ultimatum: timed mission active',active),
                ('settled','Урегулирование завершено','Settlement concluded',final+' NOT = { '+active+' }'),
                ('monitor','Ирландский вопрос остаётся открытым','The Irish question remains open','NOT = { OR = { '+active+' '+final+' } }')]:
                text(name,L(name,r,e),30,246,condition=cond,tip=irish_help)
        else:
            text('routes_total',L('routes_total','Доступно направлений: [?ENG_nww_open_routes|0]/4','Routes available: [?ENG_nww_open_routes|0]/4'),30,64,tip=route_help)
            meter('routes','open_routes',92,route_help,[],maximum=4)
            for i,(route,r,e) in enumerate([('atlantic','Северная Атлантика','North Atlantic'),('suez','Суэц и Средиземноморье','Suez and Mediterranean'),('cape','Мыс Доброй Надежды','Cape of Good Hope'),('indian','Индийский океан','Indian Ocean')]):
                y=122+i*47
                text('route_'+route,L('route_'+route,r,e),30,y,tip=route_help)
                ready='has_country_flag = '+P+'cape_ready' if route=='cape' else ''
                on=ck('route_'+route,1);off=ck('route_'+route,1,'less_than')
                icon('route_'+route+'_on','GFX_ENG_ui_gold',30,y+25,route_help,on)
                icon('route_'+route+'_off','GFX_ENG_ui_red',30,y+25,route_help,off+(' '+ready if ready else ''))
                for state,ru,en,cond in [('open','База доступна','Base accessible',on),('blocked','Доступ нарушен','Access disrupted',off+(' '+ready if ready else ''))]:
                    text(route+'_'+state,L('route_'+state,ru,en),57,y+20,350,condition=cond,tip=route_help)
                if ready:
                    text('cape_unprepared',L('cape_unprepared','Обходной маршрут не подготовлен','Diversion not prepared'),57,y+20,350,condition='NOT = { '+ready+' } '+off,tip=route_help)
            text('route_warning',L('route_warning','Заморские проекты приостановлены','Overseas projects suspended'),30,326,condition=ck('open_routes',3,'less_than'),tip=route_help)
            text('route_normal',L('route_normal','Морские условия проектов выполнены','Project route conditions met'),30,326,condition=ck('open_routes',3),tip=route_help)
        gui.append(f'containerWindowType = {{ name = "{P+panel}_window" position = {{ x = 0 y = 0 }} size = {{ width = 100% height = {height} }}\n'+'\n'.join(elements)+'\n}')
        scripts.append(f'{P+panel}_ui = {{ context_type = decision_category window_name = {P+panel}_window visible = {{ tag = ENG has_focus_tree = ENG_nww_focus }} ai_enabled = {{ always = no }} triggers = {{\n'+'\n'.join(triggers)+'\n} }')
        manifest['panels'].append({'name':panel,'width':440,'height':height})
    write('interface/ENG_mechanics.gui','guiTypes = {\n'+'\n'.join(gui)+'\n}')
    write('common/scripted_guis/ENG_mechanics.txt','scripted_gui = {\n'+'\n'.join(scripts)+'\n}')
    write('docs/art/ENG/mechanics/layout.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    build_primitives(write)


def build_primitives(write):
    """Native-style rectangular UI geometry; existing imagegen emblems stay intact."""
    out=ROOT/'gfx/interface/decisions/ENG/mechanics';out.mkdir(parents=True,exist_ok=True)
    sprites=[]
    for name,size,color in [('socket',(18,10),(31,36,43,255)),('gold',(18,10),(185,153,80,255)),
                            ('red',(18,10),(174,70,61,255)),('tick',(2,16),(224,220,188,255))]+[(p,(440,h),(24,32,43,255)) for p,h in HEIGHTS.items()]:
        img=Image.new('RGBA',size,color);d=ImageDraw.Draw(img)
        if name in HEIGHTS:
            d.rectangle((0,0,439,size[1]-1),outline=(113,103,75),width=2)
            d.rectangle((3,3,436,53),fill=(34,44,57),outline=(71,78,83))
            d.line((22,55,417,55),fill=(153,128,76),width=1)
        elif name!='tick':
            d.rectangle((0,0,size[0]-1,size[1]-1),outline=(105,99,78))
        img.save(out/(name+'.dds'))
        sprites.append(f'spriteType = {{ name = GFX_ENG_ui_{name} texturefile = "gfx/interface/decisions/ENG/mechanics/{name}.dds" }}')
    write('interface/ENG_mechanics.gfx','spriteTypes = {\n'+'\n'.join(sprites)+'\n}')

