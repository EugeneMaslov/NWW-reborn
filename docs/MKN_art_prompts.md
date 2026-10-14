# MKN: commissioned artwork prompts

The five special political focus icons and both funeral-event pictures now use project-bound artwork through `interface/MKN_custom.gfx`, including `_shine` variants for the focuses. The user supplied `docs/black-horde.jpg`, `docs/iron-fist-train.jpg` and `docs/mahno-death.jpg`; their original generation prompts were not supplied. Built-in **imagegen** prepared those references and generated the missing artwork. [Saved PNGs, exact execution prompts and provenance](art/mkn_crisis/README.md), [in-game-size preview](mkn_crisis_art_preview.png), [export manifest](art/mkn_crisis/assets.json).

The structured commissions below remain the initial art direction. The exact prompts actually used are saved beside each resulting PNG. The train icon preserves the supplied locomotive; it does not add the weapons described in the earlier commissioning concept. The council portraits remain a technical resize of the existing MKN flag, not invented people.

## Common art direction

- World: NWW Reborn, 1936; the First World War never happened. Southern Ukrainian Free Territory, village assemblies, insurgent cavalry and railway workshops. Makhno is a recognizable historical revolutionary, never a crowned fantasy ruler.
- Visual language: 1930s woodcut and lithographic propaganda, rough ink, engraved edges, restrained black, warm ivory and muted ochre. Event pictures use documentary realism with the same palette. Avoid modern uniforms, Soviet state emblems on anarchist scenes, lettering, watermarks and glossy fantasy styling.
- Icons: one readable central silhouette, generous clearance for the focus frame, no edge-to-edge background. Deliver an archival PNG and a transparent PNG, then convert locally to DDS. Inspect alpha bounds before export.
- Event targets: the installed funeral country-event texture is 210 × 176 and its news counterpart is 397 × 153. The saved panoramic master supports separate crops at those actual native dimensions. Masters and exact prompts are under `docs/art/mkn_crisis/`.
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

## 5. Icon: the Departure of the Batko

**Sprite:** `GFX_focus_MKN_departure_of_batko`.

**Executed prompt:** [departure_of_batko.prompt.txt](art/mkn_crisis/departure_of_batko.prompt.txt).

**Direction:** A respectful 1930s engraved memorial medallion, preserving the face, cap, moustache and coat collar from the supplied Makhno portrait. Narrow aged brass oval rim, folded black mourning ribbon, warm ivory and charcoal shading. Transparent exterior, no crown or lettering, readable as a 96×96 icon. The PNG and icon are separate from Makhno's existing leader portrait.

## 6. Icon: the Beacon of Statelessness

**Sprite:** `GFX_focus_MKN_beacon_of_statelessness`.

**Executed prompt:** [beacon_of_statelessness.prompt.txt](art/mkn_crisis/beacon_of_statelessness.prompt.txt).

**Direction:** A black anarchist flag above a glowing railway lantern sheltered by two open hands, with wheat at the base representing mutual aid between villages. 1930s woodcut and lithographic texture, warm ivory, aged brass and ochre; compact connected silhouette on a genuinely transparent background. No government seal, crown, lettering or Soviet state emblem.
