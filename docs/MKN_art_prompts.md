# MKN: commissioned artwork prompts

These prompts describe new artwork; no generated images are claimed. The live sprites currently use shipped HOI4 art, with real existing texture paths in `interface/MKN_custom.gfx`. Replace the corresponding texture paths when the commissioned assets are ready. The council portraits are a technical resize of the existing MKN flag, not invented people.

## Common art direction

- World: NWW Reborn, 1936; the First World War never happened. Southern Ukrainian Free Territory, village assemblies, insurgent cavalry and railway workshops. Makhno is a recognizable historical revolutionary, never a crowned fantasy ruler.
- Visual language: 1930s woodcut and lithographic propaganda, rough ink, engraved edges, restrained black, warm ivory and muted ochre. Event pictures use documentary realism with the same palette. Avoid modern uniforms, Soviet state emblems on anarchist scenes, lettering, watermarks and glossy fantasy styling.
- Icons: one readable central silhouette, generous clearance for the focus frame, no edge-to-edge background. Deliver an archival PNG and a transparent PNG, then convert locally to DDS. Inspect alpha bounds before export.
- Event targets: inspect the installed event picture’s dimensions before conversion; typical country-event art is 450 × 150, news art 465 × 150. Compose a wider master with crop clearance. Keep masters and exact prompts under `docs/art/mkn_crisis/` if generation is commissioned.
- Midjourney v6: append `--v 6 --style raw --s 100`, `--ar 3:1` for events or `--ar 1:1` for icons. Request a flat plain background and remove it during the export process; do not assume Midjourney supplies alpha.
- Flux: use the full subject, lighting and composition prompt as positive text. Use the exclusions as a negative prompt when the workflow supports one.
- DALL·E 3: use the complete prompt as natural language, including explicit negative constraints and composition; request transparent delivery only in a workflow that supports it.

## 1. News: Makhno lying in state

**Sprite:** `GFX_news_event_makhno_death`; a tighter companion crop can serve `GFX_report_event_makhno_funeral`.

**Prompt:**

> Wide documentary composition of Nestor Makhno lying in state in Huliaipole, Ukrainian Free Territory, 1936 in an alternate history where the First World War never happened. Preserve Makhno’s recognizable lean face, swept dark hair and moustache; peaceful closed eyes, fully clothed, respectful non-graphic funeral. A plain wooden casket is draped in a heavy black anarchist flag without lettering. His worn cap and one loaf of bread rest beside the casket. Weathered peasant delegates, railway workers in wool coats and exhausted insurgent soldiers stand in silent rows. Simple assembly hall, rough plank walls and narrow windows, no palace and no religious pomp. The casket occupies the central lower third; faces form a subdued arc behind it. Soft cold morning light enters from the upper left, touches the face and bread, and falls into deep charcoal shadows at the right. Restrained 1930s documentary photography translated into finely engraved lithographic shading, warm ivory highlights, smoky blacks, delicate grain. Solemn dignity, collective grief, an uncertain revolution. Wide panoramic crop with clear margins, no captions, no modern objects, no crown, no gore, no hammer-and-sickle, no watermark.

**Composition:** Keep the face, cap and bread inside the middle 60% of the frame. Reserve darker empty space at the outer edges for cropping. The black flag must be distinguishable from the shadowed clothing.

## 2. Icon: the armored train and tachankas

**Sprite:** `GFX_focus_MKN_iron_fist_trains`.

**Prompt:**

> A compact 1930s revolutionary propaganda emblem of a heavy improvised armored steam train sweeping across the Ukrainian steppe. Three-quarter front view from slightly below, blunt riveted armor plates, a small black flag above the locomotive, visible Maxim machine guns on open armored flatcars. Tachanka horse-drawn machine-gun carts race beside the railway embankment; distinguish horse-drawn carts from rail-mounted gun positions. Strong diagonal motion from lower left to upper right, two bold wheel silhouettes, one curling plume of smoke contained within the icon. Rough black woodcut engraving with muted steel gray and ochre accents, warm ivory edge highlights from upper left. A single dominant train silhouette, crisp readable shapes at small scale, isolated on a plain background, broad clear margins. No typography, no red star, no modern diesel train, no oversized science-fiction cannon, no frame, no watermark.

**Composition:** Locomotive is the primary shape; the carts are secondary. Deliver a 1024 × 1024 master and a transparent 96 × 96 game export after inspecting the existing focus frame.

## 3. Icon: the Black Horde banner

**Sprite:** `GFX_focus_MKN_the_black_horde`.

**Prompt:**

> A severe 1930s Ukrainian revolutionary woodcut emblem: a tattered black banner bearing a stark ivory skull and crossed bones, held above a tight fan of period rifle bayonets. The skull is a simplified printed symbol, not a realistic severed head. Three rifles form the lower support; the flag bends into one readable triangular silhouette. Black ink, aged ivory, restrained dark ochre metal highlights, directional light from upper left, deep engraved shadows and hand-printed texture. Symmetrical base with an asymmetrical windblown upper edge, compact central composition readable as a Hearts of Iron IV focus icon. Isolated on a plain background with generous transparent export clearance. No lettering, no crowns, no Nazi symbols, no red stars, no modern assault rifles, no gore, no fantasy armor, no frame, no watermark.

**Composition:** Leave space around the bayonet tips and flag corners. The skull should remain readable after reduction without filling the whole banner.

## 4. Icon: the armed grain harvest

**Sprite:** `GFX_focus_MKN_impregnable_granary`; a lighter variant can accompany communal-defense material.

**Prompt:**

> A hopeful but resolute 1930s agrarian revolutionary lithograph emblem of the Free Commune’s grain harvest in the Ukrainian steppe. Golden wheat sheaves form a compact protective circle around three period bolt-action rifles stacked like harvested sheaves. A sickle and a small black cloth pennant are secondary details; no hammer-and-sickle emblem. Two small figures, a woman harvester and a peasant defender, stand behind the central stack without crowding it. Low warm harvest sunlight from upper left, deep charcoal engraved contours, warm ivory paper highlights, muted golden ochre grain, matte black metal. Front-facing monumental propaganda composition, one strong central silhouette, small-scale readable wheat ears and rifle barrels, isolated plain background with generous border clearance. No lettering, no crowns, no modern machinery, no Soviet state insignia, no fantasy weapons, no frame, no watermark.

**Composition:** Keep the rifle stack central, wheat forming the lower two thirds. Avoid fine filigree that disappears at game-icon resolution.
