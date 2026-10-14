# MKN political succession overhaul

## Scope and ownership

Implemented the 1936 congress, Makhno’s death, an event-only 180-day mission, four exclusive eight-focus paths, native BoP, border battles, volunteers, foreign strikes, scorched railways and consent-based Soviet diplomacy. All new/changed display text is owned by `localisation/english/MKN_l_english.yml` and its Russian counterpart. Standard ideology groups remain unchanged; existing country-scoped scripted display names rename only MKN.

Existing focus/event IDs, industrial and service branches, MIOs, portraits and archived monarch Makhno are retained. New campaigns start after the congress, last 30 days, give 10 percentage points of support for 50 PP, and can repeat after seven days. Each new political entry requires 40% support and either supply or discipline preparation. Historical AI favors the red compromise and its settlement. The 22 archived political path focuses are hidden and unavailable in new campaigns; their old-save behavior remains defined. New campaigns begin with the revolutionary Makhno, equal 25% program support and all three requested starting spirits. Death installs named Belash and Volin leaders and institutional peasant/revkom councils, with no random monarchs. Makhno’s old monarch definition/portrait remain available to archived saves; the new funeral naturally retires his living roles in new campaigns.

The existing industry and army dynamic spirits accumulate new policy parameters. Their reconstruction replays only parameters, never factories, units, diplomacy, government changes or mission activation. A new reconstruction marker updates older saves once. BoP is enabled by the congress, not history. Its constitutional removal and soviet lock cannot be undone by daily initialization or legacy focus shifts. Daily settlement repair recognizes all four lifesavers and never resets the timer.

## Necessary native-script adaptations

Target inspected: installed HOI4 `Operation Postern v1.19.3.0.c01a (5632)`.

- `division_attack_factor` / `division_defense_factor` become `army_attack_factor` / `army_defence_factor`.
- Cavalry speed uses `modifier_army_sub_unit_cavalry_speed_factor`; motorized speed uses an instant `motorized_equipment` equipment bonus to `maximum_speed`, since the proposed motorized speed modifier is not registered. Motorized attack uses the documented `motorized_attack_factor`.
- `enemy_partisan_effect` becomes `resistance_damage_to_garrison_on_our_occupied_states`; `enemy_attrition_factor` becomes `enemy_attrition`.
- Train/equipment cost reductions use `equipment_bonus` and `build_cost_ic`, not nonexistent `production_cost_armored_train_factor` or `production_cost_railway_gun_factor`. Armored trains are `train_equipment_3`. Railway and supply-node construction use generated building modifiers.
- Side control is `(1 ± native_value)/2`. The requested 55% and 80% side-control thresholds therefore map to ±0.1 and ±0.6. The balanced range is 45–55% control per side. Literal −0.45…+0.45 combined with 55% side-control leans would overlap; contiguous native ranges avoid both overlap and dead zones. Requested bonuses are retained, including the explicit 7.5% lean attack and 0.5% relative recruitable-population factor.
- Concealment is represented by reconnaissance and reduced enemy air-superiority advantage. Tachanka ambushes buff cavalry and motorized battalions, since the installed unit set has no distinct tachanka battalion.
- Commune guards use an infantry militia template without requiring the BBA militia unit unlock. Three fully equipped three-battalion guards plus reserve rifles/manpower are awarded once.

## Real four-way collapse and map rounding

The starting MKN map had only three states. A new connected Huliaipole state, ID 1082, splits provinces 429 and 9571 from state 200. Total starting territory, manpower, resources and existing factories are conserved; the new state receives a provincial VP and its own rural infrastructure. State 200 retains its ID, capital, dam and old focus references. The new province boundary was checked against the installed map bitmap. This map change is intended for a fresh campaign; existing save-state geometry is not migrated.

Collapse snapshots all four party popularities before any split. The shares are normalized without a minimum military allocation; a party with zero support receives zero inherited armed forces. Zero remaining support is guarded against division by zero. Sequential civil wars use `share / remaining_share` for stockpiles, army, navy and air, preventing the second and third revolt from receiving a fraction of an already reduced pool. The player retains the original tag and current ideology. Each rival has an explicit named/institutional successor and cosmetic country name; all six pairs become enemies.

States cannot be divided dynamically. One controlled state is reserved per camp, then remaining states are apportioned by largest remainder according to the normalized shares. The player’s capital is reserved. At the four-state start, this necessarily means one state per camp while military shares follow support. If prior conquest supplies additional states, their quotas reflect support; physical state selection is random among eligible owned/controlled states. If an external war leaves fewer than four controlled owned states, only camps with a physical foothold spawn; the script cannot manufacture land or confiscate foreign territory. Unit counts and equipment also remain subject to engine rounding.

## Diplomacy and assets

The embassy asks SOV for reciprocal transit. Consent enables a level-two connection across an actually controlled common border, with routing confined to MKN/SOV land, ten locomotives and a two-year supply agreement. This does not require the later faction focus. Repeated negotiation decisions recover from refusal. SOV separately decides on the defensive alliance. The fatal plenum is available only to allied independent communist countries: equal autonomy grants a settlement; betrayal breaks the shared faction, adds one year of `MKN_betrayed_twice` and starts a real war.

`interface/MKN_custom.gfx` supplies all requested sprite IDs with existing valid game artwork. Institutional council portraits resize the existing MKN flag. New raster artwork was not generated; the four detailed commissions are in [MKN_art_prompts.md](MKN_art_prompts.md). The shipped event pictures are generic funeral art until those commissions are produced.

## Concrete installed-game references read

Game root: `/home/dima00138/.local/share/Steam/steamapps/common/Hearts of Iron IV`.

- `common/ideologies/00_ideologies.txt`: democratic volunteers are normally disabled; the Black International explicitly enables them with `set_rule`.
- `common/ai_strategy_plans/FIN_historical_strategy_plan.txt` (AAT): historical focus sequencing; the plan is paired with actual repeatable mandate decisions.
- `common/bop/FIN.txt` (AAT): native sides, contiguous ranges, decision category and range modifiers.
- `common/national_focus/italy.txt` (BBA), around line 13039: complete `set_politics` block including ruling party and election state.
- `common/decisions/SPR.txt` (La Résistance), around lines 14005–14058: event-only mission activation, harmful timeout, cancellation when hidden.
- `common/national_focus/spain.txt` (La Résistance), around lines 9257–9258: remove/activate mission effects.
- `common/scripted_effects/NOR_scripted_effects.txt` (AAT), around line 920: popularity-based native civil-war size and explicit state filters.
- `common/scripted_effects/SIA_scripted_effects.txt`, around line 1488: variable civil-war size; `JAP_scripted_effects.txt`, around line 1114: variable army ratio.
- `common/ideas/italy.txt` (BBA), around lines 374–399: train/railway-gun `equipment_bonus`, `instant` and `build_cost_ic`.
- `common/national_focus/switzerland.txt` (BBA), around lines 263–273: level-two fort construction on all provinces bordering a named country.
- `common/ideas/australia.txt`, around lines 2995–3015: equipment speed bonuses using `maximum_speed`.
- `common/units/equipment/trains.txt`: actual armored train equipment ID and archetype; `common/units/infantry.txt`: cavalry, motorized and militia definitions.
- `interface/eventpictures.gfx`, `goals.gfx`, `ideas.gfx`: existing texture/sprite definitions.
- `documentation/effects_documentation.md`: civil wars, state iteration/filtering, variable arithmetic, `while_loop_effect`, mission effects, rail routing, building damage, military transit, factions and wars.
- `documentation/triggers_documentation.md`, `modifiers_documentation.md`, `dynamic_variables_documentation.md`: valid comparisons, border-war/neighbor triggers, party popularity, native modifiers and generated subunit/building names.

## Validation and game acceptance

The prescribed Windows-path command was attempted; that path does not exist on this Linux machine. Validation uses the installed Linux game root above. Regression checks execute 123 collapse scenarios and 32 additional intermediate succession-program reconstruction scenarios. They cover legacy BoP repair, the new mission lifecycle, all four paths, native script names, localization, map ownership/province conservation, sequential military fractions, largest-remainder territory allocation and diplomatic response gates. `git diff --check` is required as well.

[Политическая ветка](mkn_crisis_focus_preview.png) и [полное дерево](mkn_focus_tree.svg) построены из реальных координат.

Static validation is not a game reproduction. Before release, start a fresh 1936 campaign and inspect a fresh game log; exercise the funeral, all lifesavers, timeout with different support shares, border-war callbacks, both plenum outcomes, no-DLC commune guards, BoP locking and destruction/repair tooltips. Runtime stability and final balance are not claimed verified here.
