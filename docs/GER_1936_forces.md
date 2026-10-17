# Imperial German forces, 1936

This is a counterfactual peacetime establishment for an intact imperial Germany. It is not a claimed historical 1936 order of battle. The assumptions are continuity of the professional army and shipbuilding industry, retained overseas stations, no Versailles disarmament and a gradual interwar transition to motor vehicles and naval aviation. Peace also means less combat experience: starting divisions and ships use 20% experience rather than universal veteran status.

| Service | Starting establishment |
| --- | --- |
| Army | 84 fully equipped divisions: 60 line infantry, 6 motorized, 4 mixed light-armour formations, 4 mountain brigades, 2 cavalry brigades, 8 colonial Schutztruppen |
| Fleet | 163 ships: 14 battleships, 4 battlecruisers, 3 carriers, 10 heavy cruisers, 24 light cruisers, 72 destroyers, 36 submarines |
| Aviation | 2160 aircraft: 900 land fighters, 240 CAS, 480 tactical bombers, 180 naval bombers, 120 strategic bombers, 60 transports; 90 carrier fighters and 90 carrier torpedo bombers |
| Research, all relevant DLC | 69 initial technologies, compared with Britain's 54; four research slots |

The British comparison counts only technologies actually enabled in the 1936 country history for the selected DLC, including the new German initialization effect. Later 1939 history entries and unused alternate DLC branches are excluded. Special projects are not counted as ordinary technologies. Germany has 53–69 technologies against Britain's 32–54 across the 32 tested DLC combinations. Additions cover electronics/radio, 1936 industry, support services, naval fire control/armour and carriers. This is not a blanket grant of future technology.

The line fleet combines retained Kaiser/Koenig ships, completed Bayern successors, two modern replacements and four fast battlecruisers. Older pre-dreadnoughts and treaty-driven pocket battleships do not form its battle line. The fleet is about 68% of the installed British fleet's 239 hulls; the British overseas screening network remains larger. Carrier construction is an explicit scenario assumption, not evidence that Germany historically operated carriers in 1936.

`SMS Graf Zeppelin` and `SMS Deutschland` serve in separate North Sea carrier task forces; the converted `SMS Europa` serves with the East Asia squadron at German Qingdao. Each carries 30 fighters and 30 torpedo bombers, with two heavy-cruiser escorts and ten screens. Baltic, African, Pacific and submarine groups remain separate. All bases are German-owned, and all 19 overseas ownership/core rules remain intact. Land forces are distributed across mainland centres, with eight colonial garrisons at actual owned ports.

The roster is identical with/without No Step Back and Man the Guns. BBA and legacy aircraft totals also match. MTG carriers use three deck modules (60 planes); the legacy purpose-built carriers use the 1936 `carrier_2`, and Europa uses `carrier_1` with two deck-space upgrades, also 60 planes. Custom variants are created after native starting research and designs. Existing named division templates are retained for focus/event compatibility. The fleet doctrine changes from convoy raiding to fleet in being.

## Concrete installed references

Relative to `D:/Steam/steamapps/common/Hearts of Iron IV` unless explicitly marked as mod files:

- `history/units/GER_1936.txt`, `history/units/GER_1936_nsb.txt` and the mod's previous `GER_1936_nsb.txt`: native and existing imperial land templates, full-equipment deployment and production syntax.
- `history/countries/ENG - Britain.txt`, `history/units/ENG_1936_Naval.txt`, `history/units/ENG_1936_Naval_Legacy.txt`, `history/units/ENG_1936_air_bba.txt`, `history/units/ENG_1936_air_legacy.txt`: MTG/legacy fleets, screened carrier groups, aircraft keyed by exact ship names, initial technology comparison. The mod's ENG country history supplies the same retained equipment definitions.
- The mod's `history/countries/GER - Germany.txt`: German destroyer, submarine, cruiser and Bismarck design patterns; native DLC conditions and the 1939 history boundary.
- `common/units/equipment/ship_hull_carrier.txt`, `common/units/equipment/upgrades/naval_upgrades.txt`, `common/units/equipment/modules/00_ship_modules.txt`: carrier capacity, `ship_deckspace_upgrade`, deck modules and hull slots.
- `common/units/equipment/plane_airframes.txt`, `common/units/equipment/x_plane_airframes.txt`, `common/units/equipment/modules/00_plane_modules.txt`: carrier airframes, generated mission-role equipment names and weapon/engine modules.
- `common/technologies/MTG_naval.txt`, `naval.txt`, `air_techs.txt`, `industry.txt`, `support.txt`, `electronic_mechanical_engineering.txt`: actual technology identifiers and unlocks.

Historical context: [Churchill's 17 March 1914 naval estimates statement, UK Parliament](https://hansard.parliament.uk/Commons/1914-03-17/debates/2e3044b3-a82a-4a23-b00a-cbf11f6c77a8/MrChurchillSStatement) documents the prewar British/German naval rivalry and Germany's strong continental army. The [Bundesarchiv overview of naval airships](https://www.bundesarchiv.de/themen-entdecken/online-entdecken/themenbeitraege/luftschiffe-im-ersten-weltkrieg/) records the institutional separation of German naval aviation in 1913. These establish starting conditions; the 1936 numbers and carrier programme above are NWW design choices.

## Validation and reproduction

`tools/build_german_1936_forces.py` generates the country-owned setup effect and both DLC variants of each service; `docs/GER_1936_forces.json` records the roster. `tools/validate_german_1936_forces.py` verifies equipped armies, templates and ownership, identical fleet rosters, carrier screens and capacity, exact carrier-name air groups, air-base capacity, engine script tokens and research parity in all 32 DLC combinations.

Passed: the German force validator, general country validator, archive validator, runtime setup validator and the earlier 1936 deployment regression check. Static validation does not reproduce a campaign. A fresh 1936 campaign and fresh game log remain necessary to verify deployment, deck aircraft and tooltips in the engine. Existing saves do not receive a new army or navy.

## Atlas and README

The atlas was regenerated from current ownership on 17 October 2026, including Ottoman Dodecanese, and published through Sites at [the existing atlas address](https://nww-reborn-atlas.mellowgecko1024.chatgpt.site). Published version: 1; source commit: `7eb2dd9e9764965e79efd9ac9a61e458d4a86d81`. The existing owner-only audience was preserved.

README embeds `docs/art/readme/nww-content-map.png`, captured from the rebuilt site's actual UI with its legend and source date, framed on Europe and western Asia. Clicking the picture opens the atlas; an offline ZIP is also linked. Refresh with `python tools/build_content_atlas.py --snapshot-date YYYY-MM-DD`, then `python tools/capture_content_atlas.py`. Browser QA passed desktop controls, SVG export, mobile width, console-error checks and 2000 ownership samples against the game map. No image generation was used for this map.
