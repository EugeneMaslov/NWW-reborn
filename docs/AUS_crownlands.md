# Austrian crown lands and Bohemian status UI

Owned and controlled states without a charter receive an imperial eagle decision on the map. A charter costs 75 political power and applies immediately, with a country-wide 30-day cooldown. It gives +10% local construction, an additional +10% infrastructure construction and +10% resource extraction. No cores, factories or territory are awarded. Austria's hereditary heartland (4, 152, 153, 848, 976) starts chartered; startup/daily initialization also handles existing saves once without repeating purchases. The state modifier is disabled under foreign ownership. Existing focus core rewards remain intact.

The Bohemian category uses its own illustrated chancery panel: an imperial eagle and a Bohemian lion frame Prague/Vienna architecture, with eleven brass sockets along the diplomatic rail. Red seals accumulate at the actual tension value (0–10); five text stages distinguish fragile agreement, Diet disputes, sovereignty demands, imminent rupture and secession. Tooltip details explain 60-day drift, penalties and paid remedies. No MKN textures are used. Existing crisis and settlement IDs and effects are preserved. Category descriptions no longer repeat the full tooltip; the unrelated political-mandate category now explains political campaigns.

Six generated emblems identify imperial government, constitutional government, Danube industry, army, aviation and navy. All 159 focuses now have an explicit semantic mapping, using 136 distinct sprites across political, diplomatic, Bohemian, economic and service branches. The original custom sprites had no `_shine` variants; all six now use `GFX_focus_AUS_nww_*` base/shine pairs, with the native `buttonstate.lua` animation pattern. All mapped native textures and their shine definitions are verified. Old modifier/category sprite IDs remain available.

Charter eligibility checks both the state flag and the actual dynamic modifier in target selection, visibility and availability. The completion effect rechecks eligibility and the country cooldown, refunding the cost of an invalid cached click. Startup and daily repair reconcile flag-only and modifier-only old saves without adding new purchases or rewards.

Rebuild presentation: `python tools/build_austria_presentation.py`. The former generator entry points delegate to it and cannot overwrite decision mechanics or restore the old MKN panel. DDS assets: `gfx/interface/goals/AUS/` and `gfx/interface/AUS/`. Generated originals and exact built-in imagegen prompts: `docs/art/AUS/imperial_atlas.png`, `prompt.txt`, `bohemian_panel_original.png`, `bohemian_panel_prompt.txt`. Exact focus mapping: `docs/art/AUS/focus_icon_map.json`. Technical layout and complete icon previews: `bohemian_panel_preview.png`, `focus_icons_preview.png`, produced by `python tools/preview_austria_presentation.py`. Preview fonts approximate the in-game fonts.

## Installed-game references inspected

The entire 440-pixel Bohemian panel is anchored to the horizontal center of the decision column, including every text box and tension seal. It follows `orientation = center_up` in `interface/AST_cabinet_trust_scripted_gui.gui`; `interface/countrydecisionview.gui` supplies the native 502-pixel decision-list slot width for the technical preview. Bohemian tension now increases once per 60 days; the crown-charter cooldown remains 30 days.

- `common/decisions/GER.txt`: `GER_seize_russian_citites_gold_reserves`, state targets, FROM scope and map highlights (Gotterdammerung).
- `common/decisions/AFG.txt`: map-and-decisions state actions (Graveyard of Empires).
- `common/decisions/African_Union_decisions.txt`: dynamically selected state targets without a fixed targets list (By Blood Alone).
- `interface/war_escalation_scripted_gui.gui`: embedded decision-category interface (By Blood Alone).
- `common/scripted_guis/war_escalation_scripted_gui.txt`: native category UI state binding.
- `common/decisions/ETH.txt`: `ETH_arm_resistance_decision`, state-scoped `has_dynamic_modifier` in targeted-decision visibility (By Blood Alone).
- `interface/goals.gfx` and `interface/goals_shine.gfx`: base/shine pairs, native textures, animation masks and button-state shader.
- `common/dynamic_modifiers/0_dynamic_modifiers.txt`: state construction and extraction modifiers.
- `common/dynamic_modifiers/aat_dynamic_modifiers.txt`: state infrastructure construction modifier.
- `documentation/modifiers_documentation.md`: target-version modifier validation.
- Project references: `common/scripted_guis/MKN_frontier_gui.txt`, `interface/MKN_frontier_gui.gui` and `.gfx`.

Validation: `validate_austrian_crownlands.py` checks exact focus/icon mapping, both sprite states, native textures/modifiers, transparent bounds and panel localization. `validate_austria_charter_lifecycle.py` executes 32 actual-script eligibility/cached-click combinations, the shared 30-day cooldown, repeated clicks, four idempotent old-save repair cases, hereditary setup and all eleven UI levels. Also run the Austria overhaul, country-content and archive validators, plus `git diff --check`.

Static checks and technical previews do not replace opening a new campaign, checking map markers and tooltips, advancing 60 days and reviewing a fresh game log. A fresh game process is needed to assess the updated sprite definitions. Existing saves are supported by charter reconciliation.
