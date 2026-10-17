"""Describe real flag/variable consequences that the native tooltip omits."""
import re

# Native PP/XP/buildings/research and explicit branch modifiers keep their native
# descriptions. These texts only expose genuine hidden operations/unlocks.
NOTES={
 'labour':('Открывает 35-дневные кампании за лейбористскую программу в категории «Вестминстер». Для парламентской победы требуется мандат 40/100.',
           'Unlocks 35-day Labour programme campaigns under Westminster. A parliamentary victory requires a 40/100 mandate.'),
 'premiers':('Открывает решение «Открыть сессию Имперской конференции».','Unlocks the decision to open an Imperial Conference session.'),
 'conference':('Открывает решение «Открыть сессию Имперской конференции».','Unlocks the decision to open an Imperial Conference session.'),
 'treaty_diplomacy':('Открывает оплачиваемые переговоры с Германией, США и Османской империей. Каждая сторона может принять или отклонить предложение.',
                    'Unlocks paid talks with Germany, the United States and the Ottoman Empire. Each recipient may accept or decline.'),
 'ratification':('Открывает решения о ратификации федерации. Для предложения требуются торговый договор, доверие 65 и наступление 1938 года; для Индии также ответственное правительство.',
                 'Unlocks federal ratification decisions. Offers require a trade compact, 65 trust and the year 1938; India also requires responsible government.'),
 'national_press':('Открывает кампании националистических собраний и союза сторонников порядка в категории «Вестминстер». Каждая завершённая кампания добавляет 10 процентных пунктов поддержки соответствующей партии.',
                    'Unlocks nationalist and order campaigns under Westminster. Each completed campaign adds 10 percentage points of support for its party.'),
 'imperial_discipline':('Прекращает ежемесячную потерю доверия и появление новых ультиматумов зависимых правительств. Уже начатые кризисы остаются отдельными обязательствами.',
                        'Stops monthly trust loss and new dependency ultimatums. Existing crises remain separate commitments.'),
 'crown_directory':('Прекращает ежемесячную потерю доверия и появление новых ультиматумов зависимых правительств. Уже начатые кризисы остаются отдельными обязательствами.',
                     'Stops monthly trust loss and new dependency ultimatums. Existing crises remain separate commitments.'),
 'colonial_review':('Открывает оплачиваемые предложения независимости пяти имперским партнёрам и социалистические кампании. Передача суверенитета требует согласия получателя.',
                     'Unlocks paid independence offers to the five imperial partners and socialist campaigns. Sovereignty transfers require recipient consent.'),
 'parliamentary_socialism':('Постоянный государственный дух: стабильность +5%. Снимает дух «Заморские рынки»; торговые договоры сохраняются.',
                            'Persistent state spirit: stability +5%. Removes Overseas Markets; trade compacts are retained.'),
 'island_treaties':('Открывает оплачиваемые предложения независимости имперским партнёрам. Передача суверенитета требует согласия получателя.',
                    'Unlocks paid independence offers to imperial partners. Sovereignty transfers require recipient consent.'),
 'island_fortress':('Завершение островного курса снимает духи «Заморские рынки» и «Мировой клиринговый центр».',
                     'Completing the island settlement removes Overseas Markets and World Clearing Centre.'),
 'irish_report':('Открывает посредничество между общинами в категории «Вестминстер». При напряжённости 70 начинается миссия урегулирования на 180 дней.',
                  'Unlocks intercommunal mediation under Westminster. At 70 tension, a 180-day settlement mission begins.'),
 'irish_talks':('Открывает оплачиваемое возвращение к переговорам с Дублином. Условия соглашения требуют отдельного согласия Ирландии.',
                 'Unlocks paid renewed talks with Dublin. Settlement terms require Ireland’s separate consent.'),
 'ulster_review':('Открывает оплачиваемое возвращение к переговорам с Дублином и прекращает дополнительный ежемесячный рост напряжённости от принуждения.',
                   'Unlocks paid renewed talks with Dublin and ends the additional monthly tension from coercion.'),
 'irish_future':('Открывает решение о согласованной передаче Северной Ирландии. Требуются владение регионом, мир и согласие Дублина.',
                  'Unlocks a negotiated Northern Ireland transfer decision. Ownership, peace and Dublin’s consent are required.'),
 'imperial_investment':('Открывает оплачиваемые инфраструктурные кредиты Австралии, Южной Африке и Новой Зеландии. Канадская и индийская программы открываются отдельными фокусами.',
                         'Unlocks paid infrastructure credits to Australia, South Africa and New Zealand. Canadian and Indian programmes require their own focuses.'),
 'canadian_corridors':('Открывает канадский инфраструктурный кредит. После оплаченных переговоров и согласия Канады в её регионе строится одна гражданская фабрика.',
                       'Unlocks the Canadian infrastructure credit. Paid negotiations and Canadian consent build one civilian factory in a Canadian state.'),
 'indian_electricity':('Открывает индийский инфраструктурный кредит. После оплаченных переговоров и согласия Индии в её регионе строится одна гражданская фабрика.',
                       'Unlocks the Indian infrastructure credit. Paid negotiations and Indian consent build one civilian factory in an Indian state.'),
 'naval_planning':('Открывает решение о заказе резервных транспортов: 50 политической власти, две гражданские фабрики и 70 дней на 40 конвоев.',
                    'Unlocks reserve transport orders: 50 political power, two civilian factories and 70 days for 40 convoys.'),
 'cape_route':('Подготавливает обходной маршрут вокруг Африки. Его доступность также требует доступа к ключевой базе и резерва не менее 100 конвоев.',
                'Prepares the Cape diversion. Availability also requires key base access and at least 100 convoys in reserve.'),
}


def focus_reward_tooltips(focus,loc):
    result=[];key=focus['key']
    if key in NOTES:
        tip='ENG_nww_reward_'+key+'_tt';loc(tip,*NOTES[key]);result.append(tip)
    for amount in re.findall(r'add_to_variable\s*=\s*\{\s*ENG_nww_irish_pressure\s*=\s*(-?\d+)\s*\}',focus['effect']):
        tip='ENG_nww_irish_pressure_change_'+amount.replace('-','minus')+'_tt'
        loc(tip,f'Напряжённость в Ольстере: {int(amount):+d} пунктов (в пределах 0–100).',
            f'Ulster tension: {int(amount):+d} points (bounded to 0–100).')
        result.append(tip)
    return result
