# Germany: industry, historical pacing and Bohemian operations

The German tree has 64 playable focuses: 28 political focuses, 31 industrial/intelligence focuses and five retained military/state focuses. Nineteen focuses are new; all seventeen existing direct German focus IDs and all ten archived `GER_1`–`GER_10` IDs remain intact. The industry graph and exact persistent rewards are recorded in `GER_industry_rework.json`; the archive manifest lists direct definitions only.

## Industry

The former short factory ladder is rebuilt into three connected programs:

- Ruhr coal, electrical grids, Silesian steel, arsenals and weapon standards.
- Investment banks, industrial bonds, precision manufacturing, machine tools, technical standards and colleges.
- Trade chambers, overseas extraction, freight, shipping contracts, export finance and supply resilience.

The completed programs lead to research coordination and balanced civilian/military procurement. Side projects cover worker housing, synthetic fuel, electromechanics and the target-version `energy_infrastructure` building. Thirty focuses take 70 days; the intelligence contact focus takes 35 days. Existing non-industrial opening focuses retain their timing.

One persistent dynamic spirit develops construction (+15% maximum), military output (+10%), efficiency growth (+10%), efficiency cap (+10%), research (+10%) and energy gain (+10%). Daily/startup reconstruction replays completed-focus parameters only, removes the superseded `NWW_GER_quality` idea where appropriate, and never repeats factories, resources, equipment or research slots. The research-slot focus remains capped at five slots. Construction targets owned, controlled core territory; overseas resources require actual ownership/control and grant no colonial cores. MEFO, conquest debt and repayment missions remain disabled by the existing guarded cleanup.

Rebuild: `python tools/rework_german_industry.py`. Focus/idea text is localized in Russian and English; explicit variable tooltips describe the actual percentage rewards.

## Historical progression

The Austrian ultimatum has an unconditional 1 January 1939 lower bound in focus availability, dispatch and event/reply execution. Its one-time dispatch helper also handles old saves with an already completed focus, without repeatedly sending demands or subjugating Austria automatically. Existing wars are not rewritten.

Historical AI first develops energy, investment, technical standards and arsenals. It can start coercive Mitteleuropa pressure in 1940 and the subsequent eastern-war focus in 1941. Historical-only AI strategies restrain war declarations against Austria/CZE before 1939, Poland/LTB before 1940 and MKN/UKR/SOV before 1941. The existing universal pre-1939 eastern safeguards remain intact. Human and nonhistorical eastern routes retain their existing 1939 minimum; the Austrian minimum applies to all users of the imperial ultimatum.

With uninterrupted historical focus selection and no situational delays, the scripted order completes the Austrian focus around 14 June 1939, Mitteleuropa pressure around 20 March 1940 and the eastern-war focus around 14 May 1941. These are arithmetic focus-budget estimates, not an observed AI campaign.

## Agency operation and contribution

`GER_nww_prague_network` unlocks **Support Bohemian Autonomists** against Austria in the La Résistance agency. The native operation requires one operative and network strength 35, lasts 45 days, and costs two civilian factories, 100 infantry equipment and 25 support equipment. It uses native infiltration/bribery/exfiltration phases and native operation risk/cost mechanics. The focus still provides political power without La Résistance; it does not create a substitute decision operation.

Each completion adds two Bohemian tension points. Only the increase actually fitting below the 10-point cap is credited to Germany. Both ordinary and alternate outcome definitions award the same amount. Requirements and the outcome effect recheck that Austria owns/controls Bohemia, the crisis is unresolved, CZE does not already exist, Germany is independent and the two countries are neither at war nor allied. Invalidated operations cannot restart a settled crisis or grant late pressure.

German contribution is the German-attributable portion of **current** tension. Natural 60-day growth increases total tension without adding German credit. Negotiations/reforms reduce German pressure proportionally: at tension 8 with German pressure 6, a two-point reduction leaves tension 6 and German pressure 4.5, keeping the share at 75%. Missing old-save contribution initializes to zero. The Austrian panel and operation description show the current share.

At the actual secession callback, **strictly more than 60%** produces a German puppet; exactly 60% does not. The comparison uses `5 * German pressure > 3 * total tension`, avoiding a rounded display percentage. Puppeting is limited to the newly created CZE, never an existing independent country or someone else's subject. It requires independent Germany, the new Bohemian capital, no conflicting faction or war, and a one-use fresh-secession flag. No land beyond the existing Austrian secession effect is annexed. Repair does not retroactively puppet an existing country. GER owns the shared cross-country influence definitions; Austrian variables are kept in Austrian scope.

## Installed-game references inspected

All paths are relative to `D:/Steam/steamapps/common/Hearts of Iron IV`:

- `common/national_focus/norway.txt`, `NOR_expand_military_industry` (Arms Against Tyranny): owned/controlled state construction and explicit state slots.
- `common/dynamic_modifiers/aat_dynamic_modifiers.txt`, Danish industrial capability: a persistent spirit backed by country variables.
- `common/national_focus/indonesia.txt`, energy infrastructure construction around lines 7349–7366: actual target-version energy building, free-slot checks and state prioritization.
- `common/buildings/00_buildings.txt`: energy infrastructure, slot grouping and energy effects.
- `common/operations/_documentation.md`: ROOT/FROM scopes, requirements, equipment costs and completion outcomes.
- `common/operations/00_operations.txt`, `operation_boost_resistance`, `operation_rescue_operative`: native operation requirements, phases, alternate outcomes and cancellation conditions.
- `common/operations/NSB_historical_operations.txt`, `raid_trotskys_villa` (No Step Back): a country-owned focus-unlocked operation with a dedicated country target and guarded outcomes.
- `common/operations/POL_historical_operations.txt`: focus-gated operations and resistance-support presentation.
- `common/operation_phases/*.txt`: exact phase IDs resolved by the validator.
- `documentation/modifiers_documentation.md`: exact country industrial and energy modifiers.
- `common/ai_strategy/GER_politics.txt` and `common/ai_strategy_plans/GER_historical.txt` in the project: existing restraint and historical-plan structure retained and extended.

## Validation

`validate_german_rework.py` executes 189 operation/reform/secession cases, including pressure cap, exact 60%, stale outcomes, existing CZE, war, faction, subject and missing-variable cases. It also runs 60 idempotent industrial-stage reconstructions, checks native modifiers/buildings/operation phases, historical/human date boundaries and one-time old-save Austrian dispatch. Existing German political and Austrian lifecycle validators remain in use. Run:

```
python tools/validate_german_rework.py --game "D:/Steam/steamapps/common/Hearts of Iron IV"
python tools/validate_country_content.py --game "D:/Steam/steamapps/common/Hearts of Iron IV"
python tools/validate_legacy_content.py --game "D:/Steam/steamapps/common/Hearts of Iron IV"
python tools/validate_runtime_setup.py
git diff --check
```

Static execution and UI previews do not establish in-game operation behavior or AI dates. A fresh campaign, actual agency operation, secession and fresh game log still need game verification.
