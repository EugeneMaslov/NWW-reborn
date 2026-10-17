"""Polish focus art, explicit reward notes and political opening gates.

Native references: interface/goals.gfx and common/national_focus/poland.txt (NSB).
"""
ICONS = {
 'cop_plan':'the_four_year_plan','industrial_census':'common_organization_of_society',
 'accept_german_capital':'beck_ribbentrop','economic_independence':'polish_revanchism',
 'vistula_rail_corridor':'warsaw_main_station','precision_machine_tools':'the_four_year_plan',
 'aftermath_of_the_marshal':'the_castle','castle_and_colonels_dialogue':'sanation_right',
 'national_democratic_leagues':'nationalist_education','berlin_trade_delegation':'beck_ribbentrop',
 'workers_defence_committees':'riot_of_37','state_budget_commission':'complete_april_constitution',
 'the_colonels_regime':'consolidate_sanation_government','castle_compact':'the_castle',
 'professional_civil_service':'complete_april_constitution','fortify_the_borders':'prussia_line',
 'intermarium_concept':'romania_bridgehead_strategy','vilnius_settlement':'belarus_army',
 'baltic_danubian_congress':'common_organization_of_society','agrarian_conciliation':'sanation_left',
 'national_defence_fund_nww':'prepare_for_the_inevitable','republic_survives':'resistance',
 'endecja_ascendant':'OZON','national_bloc':'nationalist_education','radical_polonization':'OZON',
 'western_claims_dossier':'reassert_silesian_claims','march_to_the_sea':'plan_west',
 'secure_the_corridor':'clamp_down_on_danzig','silesian_reconstruction':'reassert_silesian_claims',
 'continental_army':'prepare_for_the_inevitable','sovereign_national_state':'polish_revanchism',
 'pragmatic_deal':'beck_ribbentrop','customs_commission':'common_organization_of_society',
 'guaranteed_transit':'warsaw_main_station','join_mitteleuropa_officially':'beck_ribbentrop',
 'staff_exchange':'plan_east','recognize_the_western_frontier':'ban_nazi_party',
 'galician_assurances':'romania_bridgehead_strategy','polish_institutions_in_mitteleuropa':'the_castle',
 'the_lodz_uprising':'riot_of_37','council_republic':'common_organization_of_society',
 'land_and_food_committees':'sanation_left','nationalize_german_assets':'polish_revanchism',
 'workers_militias_nww':'reach_out_to_underground_state','alliance_with_the_east':'plan_east',
 'socialist_constitution':'complete_april_constitution','red_logistics_service':'warsaw_main_station',
 'red_wisla':'resistance','baltic_fleet_program':'develop_polish_shipbuilding',
 'first_coastal_dockyard':'develop_polish_shipbuilding','defend_the_wisla':'prussia_line',
 'fortress_engineers':'prepare_for_the_inevitable','vistula_reserve_battalions':'resistance',
 'unified_general_staff':'plan_east','quartermaster_service':'warsaw_main_station',
 'reserve_officer_network':'reach_out_to_underground_state','national_manoeuvres':'plan_west',
}
NOTES = {
 'aftermath_of_the_marshal':('Открывает хозяйственную и военную подготовку, кампании поддержки партий и событие о наследии Маршала.','Unlocks economic and military preparation, party support campaigns and the Marshal’s legacy event.'),
 'state_budget_commission':('Кризис Санации ослабляется: штраф стабильности меняется с −15% на −10%, политическая власть в день — с −0.20 на −0.10. Завершение кризиса требует институтов выбранного пути.','Eases the Sanation Crisis: stability penalty changes from −15% to −10%, daily political power from −0.20 to −0.10. Institutions of the selected path must finish the settlement.'),
 'pragmatic_deal':('Фиксирует прогерманский политический путь и открывает подготовку соглашения с Берлином. Союз и марионеточный статус этим фокусом не устанавливаются.','Commits to the German political path and unlocks preparations for a Berlin compact. This focus establishes neither an alliance nor puppet status.'),
 'baltic_fleet_program':('Подготовительный проект: открывает фокус первой верфи. Сам проект не создаёт кораблей, дивизий или зданий.','Preparatory project: unlocks the first dockyard focus. The project itself creates no ships, divisions or buildings.'),
 'castle_and_colonels_dialogue':('Открывает платную кампанию поддержки Санации; необходимы бюджетная комиссия и мандат 40%.','Unlocks the paid Sanation support campaign; the budget commission and a 40% mandate are required.'),
 'national_democratic_leagues':('Открывает платную агитацию Эндеции для достижения поддержки 40%.','Unlocks paid Endecja campaigning towards 40% support.'),
 'workers_defence_committees':('Открывает платную рабочую агитацию для достижения поддержки коммунистов 40%.','Unlocks paid worker campaigning towards 40% communist support.'),
 'berlin_trade_delegation':('Открывает кампанию прагматиков и подготовку переговоров с Германией.','Unlocks pragmatic campaigning and preparation for talks with Germany.'),
 'intermarium_concept':('Создаёт польскую оборонительную фракцию. Вступление Румынии и ЛитБела требует отдельных переговоров.','Creates a Polish defensive faction. Romanian and Lithuanian-Belarusian membership requires separate negotiations.'),
 'vilnius_settlement':('Направляет ЛитБелу предложение отказаться от взаимных претензий, если Союз сохранился после своего Виленского компромисса. Открывает платные повторные переговоры.','Sends Lithuania-Belarus an offer to renounce mutual claims if the Union survived its own Vilnius compromise. Unlocks paid renewed talks.'),
 'baltic_danubian_congress':('Направляет приглашения подходящим Румынии и ЛитБелу; каждое правительство вправе отказать.','Invites eligible Romania and Lithuania-Belarus; each government may refuse.'),
 'join_mitteleuropa_officially':('При мандате 40% принимает идеологию действующего германского правительства и направляет предложение союза и гарантии. Берлин вправе отказать; доступны платные повторные переговоры.','With a 40% mandate, adopts the current German government’s ideology and offers an alliance and guarantee. Berlin may refuse; paid renewed talks remain available.'),
 'alliance_with_the_east':('После реальной победы восставших направляет предложение союза коммунистической России либо подходящему ЛитБелу. Принятие не гарантировано.','After actual rebel victory, offers an alliance to communist Russia or eligible Lithuania-Belarus. Acceptance is not guaranteed.'),
 'western_claims_dossier':('Добавляет претензии на Познань, Померанию, Данциг и Верхнюю Силезию. Владение и национальный статус не меняются.','Adds claims on Poznan, Pomerelia, Danzig and Upper Silesia. Ownership and core status do not change.'),
 'recognize_the_western_frontier':('Снимает польские претензии на германские западные области без передачи территории.','Removes Polish claims on German western states without transferring territory.'),
}

def enhance_focuses(focuses):
    for f in focuses:
        short=f['id'][4:]
        if short in ICONS:f['icon']='GFX_focus_POL_'+ICONS[short]
        if not f['parents'] and short not in ('aftermath_of_the_marshal','baltic_fleet_program'):
            f['available']+=' has_completed_focus = POL_aftermath_of_the_marshal'
        if short in NOTES:f['reward_note']=NOTES[short]
        if short=='aftermath_of_the_marshal':f['reward']+='\ncountry_event = { id = nww_pol.2 days = 1 }'
        if short=='state_budget_commission':f['reward']+='\ncountry_event = { id = nww_pol.3 days = 1 }'
        for focus,event in [('professional_civil_service',50),('national_bloc',51),('customs_commission',52),('council_republic',53)]:
            if short==focus:f['reward']+=f'\ncountry_event = {{ id = nww_pol.{event} days = 1 }}'
