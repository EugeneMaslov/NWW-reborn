# NWW Reborn

Alt-history Hearts of Iron IV mod (1.19.*). Neither World War happened:
Kaiser Germany in 1914 borders, Austria with the Czech lands, Transleithanian
Hungary, free Croatia holding Bosnia, Ottomans keeping the Levant and Iraq,
a united China, Lithuania-Belarus, Makhnovist Ukraine, Soviet Ukraine in the
Comintern, communist Baltic satellites, Russia as the RSFSR.

## Structure

- `common/bookmarks/` — the NWW 1936 scenario (vanilla bookmarks blanked out)
- `common/countries/`, `country_tags/`, `cosmetic.txt`, `colors.txt` —
  tags `LTB` `MKN` `BYE` `UKR` `CRO` + cosmetic tags (`SOV_rsfsr`,
  `LTB_lithuania`, `LTB_belarus`)
- `common/decisions/` (+ `categories/`) — Makhnovist border raids vs Ukraine
- `common/ideas/nww_ideas.txt` — national spirits
- `common/national_focus/` — 12 trees: LTB, LIT, BYE, MKN, UKR, CRO, GER,
  SOV, LAT, EST (+ HUN/AUS stubs awaiting new trees)
- `common/units/names_divisions/` — division name packs for new tags
- `events/nww_ltb_mkn.txt` — LitBel crisis / peaceful Divorce, Makhno events
- `gfx/` + `interface/` — flags, leader portraits, sprite definitions
- `history/countries|states|units/` — the 1936 setup (owners, OOBs, leaders)
- `localisation/` — English + Russian (`mod_*_l_english.yml`,
  `mod_*_l_russian.yml`)

## Key mechanics

- LitBel national question: compromise, or a peaceful split into Lithuania
  (LIT) and Belarus (BYE) with a world-news "Great Divorce" event. Each side
  continues with its own branch; the other side is released with its own tree.
- Makhno: 6 ideological paths (Makhnovshchina, council communism, democracy,
  full communism, fascism, Emperor Nestor I) + repeatable border-raid
  decision chain against Soviet Ukraine (3 states transfer with cores;
  Kiev answers with a wargoal after the third raid).
- Harsh anarchist starting penalties, gradually reformed through focuses.

## Roadmap

1. Stability: solve the carrier-variant gate (carriers temporarily unspawned),
   verify sessions end-to-end (menu + all majors).
2. New Hungarian and Austrian focus trees (stubs in place, IDs preserved for
   foreign-tree prerequisites).
3. Content depth: more events/decisions, AI behavior, balance pass,
   English proofread.
4. GFX polish: portraits, idea icons, loading screens.
5. Steam Workshop release (descriptor `nwwreborn.mod` at repo root).
