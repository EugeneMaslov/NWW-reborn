# Ottoman artwork regeneration

The active Ottoman tree and country-owned spirits, political decisions and council categories receive newly painted icons based on their existing artwork and gameplay subjects. This is an artwork change; focus IDs, costs, rewards, political paths and campaign safeguards are preserved.

## Coverage

- 63 distinct focus drawings serve all 85 active focuses, retaining deliberate reuse of a source motif along related branches.
- 31 spirit drawings serve all 56 spirit definitions, including successive army and industrialisation stages, the imperial crisis and compact, the public holding, trade fund and national aviation programme (TNPA).
- Two decision drawings and one category drawing replace the existing shared political and council motifs across seven Ottoman decisions and two categories.

Each of the 97 drawings is generated separately with `imagegen`, using a numbered catalog of the previous artwork and the regenerated LTB spirits as references. No universal icon is substituted for the entire set. Ottoman brass, steel, crimson and green connect the set; the main subjects distinguish the branches. Foreign symbols are adapted to Ottoman identity and the mod's history without World War I.

## Sources and installation

- Original references and catalog coordinates: `docs/art/TUR/manifest.json`, `references/` and `*_references.png`.
- Generated full-size transparent originals and exact prompts: `docs/art/TUR/generated/`.
- Individual generation records: `docs/art/TUR/jobs/`; initial examples: `generation_jobs.json`.
- Installed mapping and textures: `docs/art/TUR/installation.json` and `gfx/interface/{goals,ideas,decisions}/TUR/`.
- Actual game-size previews: `docs/art/TUR/*_generated_preview.png`.
- Country-local sprite registrations: `interface/TUR_generated_icons.gfx`. Shared legacy and vanilla sprites remain available to their other consumers.

Concrete implementation references: `tools/build_ltb_focus_icons.py`, `tools/build_ltb_idea_icons.py`, `docs/ltb_idea_icons_preview.png`; installed `D:/Steam/steamapps/common/Hearts of Iron IV/interface/goals_shine.gfx`, specifically `GFX_focus_generic_diplomatic_treaty_shine`, its two scrolling highlight animations and `gfx/FX/buttonstate.lua`. The native highlight template is copied with each new focus texture used as its animation mask. Both the base sprite and `_shine` variant are registered.

`tools/build_tur_generated_icons.py` crops occupied alpha bounds, resizes focus art to fit inside an 83-pixel area on a 95×95 transparent canvas, and spirit/decision art inside a 58-pixel area on a 64×64 canvas. It preserves source comments and edits only icon/picture tokens. A parsed gameplay hash, excluding icon/picture fields, guards against mechanical changes.

## Verification

Run `python tools/build_tur_generated_icons.py`, then `python tools/validate_tur_generated_icons.py`. The latter checks coverage of all active consumers, textures, alpha clearance, focus highlights, saved originals/prompts and unchanged gameplay. Also run the country, legacy and Ottoman validators and `git diff --check`.

Static texture and script checks do not establish rendering in a running campaign. A fresh game launch and visual inspection of the tree, spirits and decisions remain the runtime check.
