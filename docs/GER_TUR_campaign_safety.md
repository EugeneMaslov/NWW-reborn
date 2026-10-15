# German and Ottoman AI campaign safeguards

The previous date gates did not prevent Germany from declaring several wars after a deadline. Ottoman campaign strategies added +300 declaration desire regardless of a target's major-power guarantees/faction. Completed-focus repair could keep regenerating war goals during a disastrous war or after defeat.

The correction has three independent layers, with country-owned GER/TUR definitions:

1. A named native `can_not_declare_war` relation-rule predicate checks readiness and target risk at the actual declaration, including when a goal was awarded before guarantees/factions changed. It is registered at startup and removed/replaced only by its exact trigger identity. It does not remove the existing German pre-1939 relation rules.
2. War focuses and Ottoman positive declaration strategies check readiness. Every one of the sixteen goal awards in GER/TUR campaign effects and German event replies checks the corresponding AI target predicate. Daily repair therefore cannot bypass the new restrictions.
3. War/peace/capitulation hooks maintain recovery state. Readiness is false immediately when any war exists, or while the observed-war flag is waiting for peace processing, so the next declaration cannot slip between a capitulation/annexation and the daily tick.

## Readiness and recovery

AI must be at peace, independent, not capitulated or in civil war, with surrender progress below 5%, stability above 40% and war support above 35%. The checks supplement existing focus prerequisites and historical date gates; they do not replace them.

After complete peace: 180 days without a new offensive campaign. After capitulation: 730 days measured from the eventual complete peace. Capitulation records a persistent pending-defeat flag; peace processing converts it into the longer recovery flag. Other continuing wars prevent recovery from starting. Startup reinstalls the rule without resetting existing timers. A one-time 180-day peace-time initialization also catches old saves lacking any war-history flags; it does not repeat on subsequent loads.

The named predicate is AI-only. Players keep the original focus/war rules. Defensive war, existing wars, completed conquest objectives, ownership-gated integration and actual-victor annexation remain intact. External declarations and later diplomatic escalation by other countries are not rewritten. Switching player/AI control changes the predicate evaluation without leaving an AI-only permanent country rule behind.

## Target selection

Ottoman AI only initiates campaigns against an independent non-major target at peace, outside a faction and without any guarantor. Estimated target army strength must be below 67% of Turkey's strength. The canonical Bulgarian → settlement → Greek → wider Balkan route and explicit AI-path rules remain unchanged; protected targets can cause that route to wait rather than start a world war.

Germany requires the target's estimated army strength to be below 80% of its own. It avoids subjects, targets already fighting a major power, and targets guaranteed by a major, faction member or subject. A faction target is permitted only if it is not a non-leader major, there are no other non-leader major powers in the faction, and a separate faction leader is below 67% of Germany's estimated strength. Thus an isolated weaker major or a sufficiently weak coalition with one leading major remains possible; an Anglo-French coalition does not become a routine opportunistic target. One ongoing war blocks all additional German declarations.

The relation rules cover existing stockpiled focus goals and manual AI justifications. They cannot themselves force peace or stop another country from entering an already active war. No subject, country territory or peace deal is altered by the safeguards.

## Files and regeneration

`tools/restrain_campaign_ai.py` generates `GER_campaign_safety_*` and `TUR_campaign_safety_*` trigger/effect/on-action files, then idempotently guards existing focuses, goal effects and replies. Russian/English usage descriptions explain the blocks. Country files and focus/event IDs are retained. Rerun this tool after regenerating the underlying GER/TUR campaign scripts.

## Concrete installed references inspected

Paths are relative to `D:/Steam/steamapps/common/Hearts of Iron IV`:

- `documentation/effects_documentation.md`, `add_relation_rule_override` and `remove_relation_rule_override`: named-trigger overrides and negative-rule OR composition. The documentation explicitly lists `can_not_declare_war` in its examples.
- `common/scripted_effects/ETH_scripted_effects.txt`, `ETH_set_up_lon_arms_resolution_effect`, and `common/scripted_triggers/ETH_scripted_triggers.txt`, `has_lon_arms_embargo` (By Blood Alone): a named dynamic relation predicate and its FROM target scope.
- `common/national_focus/usa.txt`, Neutrality Act AAT block, and `common/scripted_triggers/00_scripted_triggers.txt`, `trade_partner_not_at_war` (Arms Against Tyranny): re-evaluate the other country's war state in a named relation restriction.
- `common/on_actions/00_on_actions.txt`: exact ROOT/FROM semantics of `on_war`, `on_war_relation_added`, `on_capitulation` and `on_peaceconference_ended`.
- `common/ai_strategy/AUS.txt`: avoid risky alignment/pressure involving guarantees.
- `documentation/triggers_documentation.md`: actual `strength_ratio`, `is_guaranteed_by`/`has_guaranteed`, `has_war_with_major`, `surrender_progress`, faction and country-iterator triggers.
- Existing project `GER_effects.txt`, `nww_GER_eastern_war_guard`: retain the older target-specific protections alongside the new named rule.

## Verification

`validate_campaign_safety.py` executes 84 readiness/recovery/coalition cases, checking queued goals, a second-front attempt immediately after the first declaration, 180/730-day timers, defeat/save-load persistence, player control, changes in guarantee/faction after goal issuance, and all sixteen guarded goal awards. It also verifies callback coverage, rule ownership and native documentation support.

Run the country-content, archive, Turkey/Balkans, Germany/politics, German rework and runtime-setup validators plus `git diff --check`. These source-script tests do not reproduce engine AI behavior. Actual campaign declarations, native relation-rule UI and a fresh game log still require an in-game check.
