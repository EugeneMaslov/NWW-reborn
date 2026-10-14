from patch_mkn_overhaul import ROOT, save, put, block
from hoi4_script import read, one, values
import re

def main():
    path='common/country_leader/MKN_overhaul_traits.txt';doc=read(ROOT/path);traits=one(doc,'leader_traits')
    teacher=one(traits,'mkn_literacy_organizer');teacher[:]=[n for n in teacher if n[0]!='industry_research'];put(teacher,'research_speed_factor','0.05')
    train=one(traits,'mkn_armored_train_commander');train[:]=[n for n in train if n[0]!='railway_gun_bombardment_factor'];save(path,doc)
    # local_building_slots_factor is state-only in 1.19.3. The leader's
    # country-wide equivalent gives the requested +20% slots in every state.
    elder=one(traits,'mkn_granary_overseer')
    elder[:]=[n for n in elder if n[0]!='local_building_slots_factor']
    put(elder,'global_building_slots_factor','0.20');save(path,doc)
    path='common/characters/nww_MKN.txt';doc=read(ROOT/path)
    trainchar=one(one(doc,'characters'),'NWW_MKN_roman_danylenko')
    trainstaff=next(r for r in values(trainchar,'advisor') if one(r,'slot')=='high_command')
    put(trainstaff,'on_add',block('add_ideas = MKN_armored_train_staff_bonus'))
    put(trainstaff,'on_remove',block('remove_ideas = MKN_armored_train_staff_bonus'));save(path,doc)
    path='common/ideas/MKN_ideas.txt';doc=read(ROOT/path)
    put(one(one(doc,'ideas'),'country'),'MKN_armored_train_staff_bonus',block('''picture = generic_railroads
        allowed = { original_tag = MKN } removal_cost = -1
        equipment_bonus = { train_equipment_3 = { instant = yes armor_value = 0.20 air_attack = 0.20 } }
    '''));save(path,doc)
    entries={
        'MKN_free_workshops':('Free Workshops','Вольные мастерские'),
        'MKN_free_workshops_focus':('Ekaterinoslav & Huliaipole Free Workshops','Вольные мастерские Екатеринослава и Гуляйполя'),
        'MKN_free_workshops_focus_desc':('Federate the urban and rural workshops into a common engineering network.','Объединим городские и сельские мастерские в общую инженерную сеть.'),
        'MKN_free_workshops_unlock_tt':('Unlocks the Free Workshops industrial concern and military industrial organization.','Открывает промышленный концерн и военно-промышленную организацию «Вольные мастерские».'),
        'MKN_free_workshops_initial_trait':('Federation of Free Workshops','Федерация вольных мастерских'),
        'MKN_revkom_terror_desc':('An emergency committee paralyses production through requisitions and arrests. The purge of irreconcilables will transfer authority to Osyp Tsebriy.','Чрезвычайный комитет парализует производство реквизициями и арестами. После устранения непримиримых власть перейдёт к Осипу Цебрию.'),
        'MKN_passive_escalation_drift_desc':('Tension rises by one level every 30 days until the frontier crisis ends.','Каждые 30 дней напряжённость повышается на один уровень до завершения пограничного кризиса.'),
        'MKN_unified_global_building_slots_factor_tt':('Maximum factories in core states: +30%.','Максимум предприятий в национальных регионах: +30%.'),
        'mkn_ukr_border.30.t':('The Fall of Kyiv','Падение Киева'),
        'mkn_ukr_border.30.d':('With all Ukrainian approaches to Kyiv cut off, the Soviet Ukrainian government surrenders. Its territory joins the free federation.','После отсечения всех украинских подступов к Киеву правительство Советской Украины капитулирует. Её территории входят в вольную федерацию.'),
        'mkn_ukr_border.30.a':('The communes stand victorious.','Победа вольных общин.'),
        'MKN_duel_category':('The Succession Civil War','Гражданская война за наследство Батьки'),
        'MKN_support_established_order':('Support the Established Order','Поддержать действующую власть'),
        'MKN_support_established_order_desc':('Remain with the incumbent government. This excludes joining the insurgents.','Остаться на стороне действующего правительства. Переход к повстанцам станет недоступен.'),
        'MKN_rally_to_challenger':('Rally to the Insurgent Challenger','Встать на сторону повстанцев'),
        'MKN_rally_to_challenger_desc':('Take command of the strongest opposition faction. This choice is irreversible.','Принять командование сильнейшей оппозиционной фракцией. Выбор необратим.'),
        'MKN_armored_train_staff_bonus':('Armored Train Command','Командование бронепоездами'),
        'MKN_armored_train_staff_bonus_desc':('While the train commander serves, armored trains receive +20% armor and anti-air effectiveness. Trains are logistical equipment rather than divisions.','Пока командующий состоит в штабе, бронепоезда получают +20% к броне и эффективности ПВО. Бронепоезда относятся к логистическому оснащению.'),
        'NWW_MKN_andrii_dorosh_high_command':('Andrii Dorosh','Андрей Дорош'),
    }
    russian_traits=['Железный воевода','Философ-идеалист','Хранитель житницы','Парализованный комитет','Организатор синдикатов','Батька в штабе','Специалист по пехоте','Эксперт по тачанкам','Командующий бронепоездами','Степной интендант','Специалист по укреплениям','Снабженец оружием','Организатор призыва','Военный оратор','Фронтовой делегат','Координатор арсеналов','Организатор ветеранов','Делегат просвещения','Секретарь общин','Теоретик безвластия','Казначей кооперативов','Организатор грамотности','Редактор вольной прессы','Распределитель зерна','Защитник села','Делегат ополчения','Агроном','Сельский посредник','Хранитель рынка','Организатор промышленности','Железнодорожный диспетчер','Секретарь профсоюзов','Инженер мастерских','Делегат труда','Теоретик синдикализма']
    for (key,node,op),name in zip(traits,russian_traits):
        entries[key]=(key.removeprefix('mkn_').replace('_',' ').title(),name)
    names=['Семён Каретник','Пётр Гавриленко','Михаил Калашников','Алексей Марченко','Григорий Васильковский','Иван Лютый','Всеволод Волин','Пётр Аршинов','Марк Мрачный','Аарон Барон','Ольга Таратута','Анатолий Горелик','Федот Козубенко','Анна Кравченко','Степан Ткаченко','Мария Гордиенко','Михаил Петренко','Иван Сытник','Осип Цебрий','Даниил Бондаренко','Екатерина Мельник','Николай Савченко','Елена Коваленко','Андрей Романенко']
    chars=one(read(ROOT/'common/characters/nww_MKN.txt'),'characters')
    tokens=[k for k,v,o in chars if k.startswith('MKN_advisor_')]
    for lang,index in [('english',0),('russian',1)]:
        path=ROOT/f'localisation/{lang}/MKN_overhaul_l_{lang}.yml'
        text=path.read_text(encoding='utf-8-sig')
        if lang=='russian':
            for token,name in zip(tokens,names):text=re.sub(rf'( {token}:0 )"[^"]*"',rf'\1"{name}"',text)
        for key,value in entries.items():
            text=re.sub(rf'^ {re.escape(key)}:.*\n','',text,flags=re.M)
            text+=f' {key}:0 "{value[index]}"\n'
        path.write_text(text,encoding='utf-8-sig',newline='\n')
    path=ROOT/'localisation/russian/MKN_l_russian.yml'
    text=path.read_text(encoding='utf-8-sig').replace('MKN_state_socialism:0 "Государственный социализм"','MKN_state_socialism:0 "Государственный синдикализм"')
    path.write_text(text,encoding='utf-8-sig',newline='\n')
    # Native UI containers must disappear immediately, not one daily pulse later.
    for path,container in [('common/decisions/categories/MKN_ukr_border_categories.txt','MKN_ukr_border_category'),('common/scripted_guis/MKN_frontier_gui.txt','MKN_frontier_decision_ui')]:
        doc=read(ROOT/path)
        node=one(doc,container) if 'categories/' in path else one(one(doc,'scripted_gui'),container)
        visible=one(node,'visible')
        if not any(one(n,'has_country_flag')=='mkn_ukr_frontier_concluded' for n in values(visible,'NOT')):
            visible.extend(block('NOT = { has_country_flag = mkn_ukr_frontier_concluded }'))
        save(path,doc)
    save('common/on_actions/MKN_overhaul_on_actions.txt',block('''on_actions = {
        on_startup = { effect = { every_country = { limit = { original_tag = MKN exists = yes } MKN_repair_overhaul = yes } } }
        on_daily = { effect = { every_country = { limit = { original_tag = MKN exists = yes } MKN_repair_overhaul = yes } } }
    }'''))
    save('common/scripted_effects/MKN_overhaul_effects.txt',block('''MKN_repair_overhaul = {
        if = { limit = { NOT = { has_country_flag = MKN_overhaul_v3 } }
            nww_mkn_rebuild_industry = yes nww_mkn_rebuild_services = yes
            set_country_flag = MKN_overhaul_v3
        }
        if = { limit = { has_completed_focus = MKN_purge_irreconcilables has_government = communism has_country_leader_with_trait = mkn_paralyzed_committee }
            MKN_install_tsebriy = yes
        }
        if = { limit = { has_country_flag = mkn_ukr_incident_fired NOT = { has_country_flag = mkn_ukr_frontier_concluded }
            NOT = { has_completed_focus = MKN_ukrainian_frontier_root } }
            complete_national_focus = MKN_ukrainian_frontier_root
        }
        if = { limit = { has_country_flag = mkn_frontier_conflict_active NOT = { has_country_flag = mkn_ukr_frontier_concluded }
            NOT = { has_active_mission = MKN_passive_escalation_drift } }
            activate_mission = MKN_passive_escalation_drift
        }
        if = { limit = { has_country_flag = mkn_ukr_frontier_concluded }
            remove_mission = MKN_passive_escalation_drift
            clr_country_flag = mkn_frontier_conflict_active clr_country_flag = mkn_ukr_frontier_unlocked
        }
    }'''))

if __name__=='__main__':main()
