# LTB national-spirit artwork

Generated with the built-in imagegen tool on 2026-10-14. PNG originals are kept here; the game uses the separate 64×64 transparent DDS files in `gfx/interface/ideas/LTB/idea_nww_ltb_*.dds`. Rebuild the format conversion and sprite definitions with `python tools/build_ltb_idea_icons.py`.

The generation prompt for each image was the following template, with its subject inserted from the table:

> Create ONE new raster UI icon for a Hearts of Iron IV alternate-history mod NWW Reborn, national spirit for Lithuania-Belarus. Subject: {subject}. A carefully hand-painted vintage strategy-game emblem, muted gunmetal silver, aged bronze, restrained deep red, ivory highlights, crisp silhouette, warm directional light, dark low-saturation recesses. Visual cohesion with HOI4's national-spirit icons and the Union's white-red-white horizontal flag. Small unobtrusive red-white ribbon accent along the base. Compact centered arrangement, nearly square composition, opaque objects with clean transparent outer background. The design must remain readable at a final 65 by 67 pixel game UI size. No words, letters, numbers, watermark, people portrait, modern flags, Soviet symbols, elaborate outer wreath, or large blank padding. A single emblem, not a sprite sheet or a presentation board.

| File | Exact subject |
| --- | --- |
| `nww_ltb_national_question.png` | a silver medieval mounted knight coat of arms split by a jagged crack, two small separated red-and-white ribbon ends, symbolizing a fragile Lithuania-Belarus union |
| `nww_ltb_agrarian.png` | a wheat sheaf, a dark steel tractor wheel and a small old wooden plough, symbolizing an underdeveloped rural economy |
| `nww_ltb_depression.png` | an idle brick factory with a broken gear and a downward broken brass arrow, symbolizing economic depression |
| `nww_ltb_army.png` | two mismatched steel officer helmets above disordered crossed rifles and a broken command baton, symbolizing a disorganized joint army |
| `nww_ltb_union.png` | two hands sealing a parchment compact beneath a silver mounted knight shield, symbolizing a Lithuanian-Belarusian political compromise |
| `nww_ltb_arsenal.png` | a steel gear, artillery shell and brick arsenal building, symbolizing the Minsk arsenal and domestic military industry |

Generation used `transparent_background=true`. Export preserves the generated art and transparency, removes only empty outer padding, fits it to the UI canvas and writes DDS without changing the large originals. The national-spirit export uses a 64×64 canvas; the existing advisor portraits use their own 65×67 format.
