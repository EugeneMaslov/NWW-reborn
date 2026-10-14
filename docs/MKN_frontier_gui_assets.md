# Ukrainian Frontier GUI and textures

The category `MKN_ukr_border_category` attaches `MKN_frontier_decision_ui`. Its
246-pixel status panel reads `mkn_ukr_escalation_level` in player-country scope,
shows the five-color meter, and displays exactly one stage marker and caption.
The original decision buttons appear directly beneath the panel through the
native category list. Their native controls enforce costs, availability,
cooldowns and tooltips; the GUI contains no duplicate click rewards.

The panel remains visible once `mkn_frontier_conflict_active` or
`mkn_ukr_frontier_unlocked` is set, including full war with UKR or SOV. The numeric
level is always shown. Full war displays `MKN_frontier_war_locked_tt`; a frozen
frontier displays `MKN_frontier_frozen_tt` while neither war is in progress.
The native decision rows provide disabled controls and their own availability
tooltips during locked states. No extra marker-position variable, polling event
or GUI AI is required.

Run `python tools/generate_frontier_gui_assets.py` to regenerate the textures.
Pillow draws deterministic antialiased primitives at four times the final size.
The PNG masters and uncompressed RGBA DDS files are both project-owned under
`gfx/interface/frontier_conflicts/`; the DDS round trip must preserve every pixel.
Each output has transparent outer clearance and nonempty alpha content:

| Texture | Canvas | Purpose |
| --- | --- | --- |
| `frontier_escalation_meter` | 400 × 36 | Green, lime, yellow, orange, crimson stages |
| `icon_frontier_ukr` | 64 × 64 | Crossed curved sabres over railway tracks |
| `frontier_stage_marker` | 32 × 48 | Amber glow and downward current-stage pointer |
| Eight `focus_MKN_*` variants | 96 × 96 | Frontier, reconnaissance, miners, first shot, train, fort, war, treaty |

The eight frontier focus sprites and their `_shine` variants are generated in
`interface/MKN_frontier_focus_icons.gfx`. All eight have at least five pixels of
transparent alpha clearance; the native animation uses each icon as its mask.
The generator also saves `docs/art/MKN_frontier_assets_preview.png` for review.

Concrete installed-game references inspected before implementation:

- `common/scripted_guis/_documentation.md`: `decision_category` context,
  `window_name` and element `_visible` triggers.
- `common/scripted_guis/war_escalation_scripted_gui.txt` and
  `interface/war_escalation_scripted_gui.gui`: By Blood Alone escalation panel
  embedded in a decision category.
- `common/decisions/categories/ETH_decision_categories.txt`, category
  `ETH_second_italo_ethiopian_war_category`: `scripted_gui` attachment alongside
  the original decision list and complete category sprite token.
- `common/scripted_guis/RAJ_tax_fraud_scripted_gui.txt`: mutually exclusive
  variable-driven visibility for current-state text elements.
- `interface/RAJ_famine.gui`: Cyrillic-compatible `hoi_18mbs` text boxes and
  constrained widths inside a decision category.
- `interface/goals_shine.gfx`: native opposing scrolling animations, shared
  shine overlay, per-icon alpha mask and `gfx/FX/buttonstate.lua` effect.
- `documentation/effects_documentation.md`, `activate_decision`: documented
  activation is not a substitute for the native decision purchase control.

Static GUI/texture checks do not establish in-game rendering. Inspect the
category in a fresh campaign at the game's current UI scale and check a fresh
game log for missing textures, elements or localization.
