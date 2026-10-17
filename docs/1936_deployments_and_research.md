# Scenario fixes, 17 October 2026

- TUR research focuses retain their IDs and positions. Each now takes 70 days. The fourth slot requires the industrial preparation `TUR_Factory_1`, the economic reform, at least 30 factories, and a date after 1 January 1937. The fifth also requires `TUR_civ_factory_2`, the fourth-slot focus, at least 50 factories, and a date after 1 January 1939. Both retain the five-slot reward cap. Explicit availability conditions avoid long connectors across the industry tree.
- Dodecanese (164) starts under Ottoman ownership; the Greek core remains. Italian Rhodes fleets move to Venice in both naval variants. Native Italian land and air OOBs contain no Rhodes garrison or wing. Italian divisions previously in Austrian Istria and Trieste move to Italian Veneto.
- British divisions in Ottoman Palestine, Jordan and Iraq move to Egypt and Cyprus; the former German Singapore garrison moves to Britain. All four LaR/NSB combinations are covered. British air wings in Palestine move to Alexandria; British subject bases remain valid.
- French divisions in German Alsace move to four French provinces directly touching the German border (521, 698, 5291, 11516), identified from the province bitmap. The Levant garrison and flotilla move to Marseille. Both tank variants and both naval variants are covered. The installed French land OOBs lack the final closing brace of `instant_effect`; the local overrides close that block.
- Austria starts with 18 fully equipped divisions instead of 12, including six additional infantry divisions. Existing templates, production and experience are retained. Its army is spread across its current territory. The base and neutrality flags use the installed imperial Austrian artwork at all three resolutions; later cosmetic tags remain separate.
- Poland, Russia, Ukraine, Litbel, the Makhnovists, Yugoslavia, Croatia, Romania, Latvia, Denmark, Hungary and Turkey deploy across owned cities and supply hubs. Primary state centres are visited before secondary centres; remaining divisions cycle across those points. Army sizes and templates are preserved except for Austria. Yugoslavia's inherited NSB OOB is corrected as well as its non-NSB OOB.
- Inherited guarantees involving Balkan countries are removed from effective country histories, including French and Czechoslovak guarantees of Yugoslavia/Romania and Romania's guarantees. Italy's guarantee of Albania remains. This changes starting obligations, not the ability to issue new guarantees during play.

## Installed references

Paths below are relative to `D:/Steam/steamapps/common/Hearts of Iron IV`:

- `common/national_focus/turkey.txt`: Battle for the Bosporus research focuses, including `TUR_reinstate_the_darulfununu_sahane`, use `cost = 10` and `add_research_slot`.
- `common/national_focus/sweden.txt`: Arms Against Tyranny research availability uses `num_of_factories` as an industrial gate.
- `history/units/ENG_1936*.txt`, `FRA_1936*.txt`, `ITA_1936*.txt`, `YUG_1936_nsb.txt`, `HUN_1936.txt`: native land deployment, fleet `naval_base`/task-force `location`, BBA air state scopes and DLC variants. Local overrides preserve native content except for the described corrections.
- `history/states/164-Dodecanese.txt`, `history/countries/CZE - Czechoslovakia.txt`, `history/countries/ROM - Romania.txt`: state ownership/core and inherited guarantee definitions.
- `gfx/flags/{,medium/,small/}AUS_austrian_empire_neutrality.tga`: Gotterdammerung imperial flag artwork, copied without creative changes.
- `map/supply_nodes.txt` and effective `history/states/*.txt`: deployment destinations, checked against current mod ownership.

## Validation

`python tools/validate_1936_deployments.py` checks the effective game/mod state map, army counts and ownership, DLC fleet/air positions, guarantees, the three flag resolutions and research requirements. `docs/1936_deployment_manifest.json` records army sizes and the number of occupied provinces.

Passed on 17 October: the deployment validator (25 army variants), `validate_country_content.py`, `validate_legacy_content.py`, `validate_soviet_content.py` (2566 checks), `validate_turkey_balkans.py` (1634 scenarios), `validate_austria_campaigns.py` (138 scenarios), `validate_austria_overhaul.py`, `validate_france_content.py`, engine syntax checks on all 36 changed history/focus scripts, and `git diff --check`. Game-aware validators used the installed game path above. The archive validator now expects Austria's 18 equipped divisions.

Scenario ownership, OOBs and starting diplomacy require a new campaign. A game reproduction and fresh `error.log` are still required to confirm runtime behaviour; static checks do not establish that result.
