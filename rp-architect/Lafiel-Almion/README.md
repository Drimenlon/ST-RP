# Lafiel & Almion

```yaml
status: DRAFT_NOT_READY
rp_id: lafiel-almion
rp_name: Lafiel & Almion
group_name: Lafiel & Almion
user_role: narrator_director
```

## Purpose

Primer RP de producción/prueba centrado en Lafiel y Almion antes de la entrada de Dalkon.

La dinámica principal es cuckolding psicológico, humillación aristocrática, celos, tensión de clase, orgullo y deseo contradictorio. No es una trama revolucionaria ni un triángulo amoroso genérico.

## Authoritative package

Luna debe leer los archivos de este paquete en este orden:

1. `README.md` — manifest, mapping y gates de ejecución.
2. `WORLD.md` — canon persistente/prosa de referencia del mundo.
3. `WORLD_INFO.md` — especificación exacta de lorebook/World Info: entries, keys, strategy, position, order y contenido.
4. `NARRATIVE_RULES.md` — reglas globales de narración, pacing y comportamiento.
5. `LAFIEL.md` — definición operativa de la card de Lafiel.
6. `ALMION.md` — definición operativa de la card de Almion.
7. `GROUP.md` — participantes, narrator role, NPC de prueba, escenario compartido y knowledge boundaries.
8. `OPENING.md` — opening grupal exacto y handoff al narrador.

No inferir contenido desde otros archivos del repositorio salvo los contratos globales de infraestructura.

## Critical user-role rule

`{{user}}` is the narrator/director.

`{{user}}` is NOT Rhevan, NOT a servant, and NOT an in-world participant by default.

User messages can establish narration, scene direction, time progression, environmental facts, and dialogue/actions explicitly attributed to supporting NPCs.

Lafiel and Almion must not address `{{user}}` as a diegetic person unless the narrator explicitly introduces a separate in-world character.

The initial lower-class male pressure point is the supporting NPC `Rhevan`, defined in `GROUP.md`. Rhevan is not Dalkon.

## Mapping hacia SillyTavern

- `LAFIEL.md` → Character Card `Lafiel`.
- `ALMION.md` → Character Card `Almion`.
- `WORLD.md` → semantic canon reference; do not dump this file wholesale into a card.
- `WORLD_INFO.md` → desired Chat Lorebook `Lafiel-Almion — World`, with exact entry decomposition and activation semantics.
- `NARRATIVE_RULES.md` → requisitos del prompt global/preset del RP; no duplicar innecesariamente dentro de las cards.
- `GROUP.md` → definición del Group Chat `Lafiel & Almion`, scenario compartido, narrator semantics, supporting NPC and knowledge boundaries.
- `OPENING.md` → greeting/opening inicial del grupo.

If Luna lacks an approved runbook for any exact creation/binding operation described here, it must STOP on that capability rather than invent another representation.

## Required characters

- Lafiel
- Almion

Do not create a Dalkon card for this pilot.

Rhevan is initially a narrator-controlled supporting NPC, not a required group-member card. Do not create a Rhevan character card unless RP Architect later changes that decision.

## Group generation

Desired group participants:

1. Lafiel
2. Almion

The narrator controls scene progression through user turns.

Do not treat every user turn as spoken dialogue. Read attribution literally:

- `Rhevan says ...` → Rhevan spoke.
- `Almion notices ...` → narrator establishes an observable/scene fact as written.
- descriptive prose → narration, not a narrator-character action.

## World Info

The implementation source is `WORLD_INFO.md`, not generic category names.

The desired lorebook contains explicit entries for:

- hereditary estate order;
- modern prosperity/technology;
- settlement pattern;
- modern nobility;
- curse core/public knowledge;
- curse effects on noble men;
- curse effects on noble women;
- public hierarchy vs private inversion;
- servant boundaries/consequences;
- Crown/succession/Lafiel;
- current curse research state.

Do not merge these into one generic "world" entry unless RP Architect explicitly authorizes that simplification.

Do not invent extra keys, random activation, vectors, timed effects, inclusion groups or Author's Note usage.

## Memory

The RP initial test does not depend on Memory Books.

While Memory Books remains `LUNA_READY = NO`, Luna must not configure it for this package.

Summaryception coexistence/replacement is outside this package.

## Presence / group isolation

This package can use normal group chat but does not depend on unvalidated Memory Books + Presence behavior.

Private character thoughts must not become shared knowledge merely because Lafiel and Almion are in the same group chat.

## Preset gate

The RP requires an explicitly identified RP-specific preset/configuration bound to this group.

The exact preset identity and binding are still unresolved.

Therefore the package remains:

`DRAFT_NOT_READY`

Do not implement in SillyTavern until the preset binding is closed and the package is explicitly promoted to `status: READY`.

## Preserve

Luna must preserve:

- other RPs, cards, groups and chats;
- presets/configs not owned by this RP;
- unrelated lorebooks;
- Summaryception, Presence and Recast unless explicitly authorized;
- Gallery Images implementation/settings/data;
- SillyTavern core;
- Author's Note, which is user-controlled and out of scope.

## Verify when READY

After implementation verify at least:

- exactly the intended Lafiel and Almion cards exist with supplied fields;
- the group `Lafiel & Almion` has only the intended required character participants;
- `{{user}}` is represented semantically as narrator/director, not servant;
- the opening matches `OPENING.md`;
- the intended preset is bound and no foreign RP prompt is inherited;
- lorebook identity is exactly `Lafiel-Almion — World`;
- World Info entries/keys/strategies/orders/content match `WORLD_INFO.md`;
- WorldInfo Info activation behavior matches the verification cases in `WORLD_INFO.md`;
- Prompt Inspector shows the expected world/character/narrative context and no foreign RP instructions;
- Dalkon is not a participant and is not implicitly substituted for Rhevan;
- no unrelated RP is modified.

## STOP IF

Luna must STOP if:

- preset/binding remains unresolved;
- any required capability is not `LUNA_READY` for the requested operation;
- it needs to decide how to reinterpret semantic content between surfaces;
- it cannot create/bind the exact World Info configuration without an undocumented procedure;
- it finds another Lafiel/Almion and is not explicitly authorized to update it;
- it detects instructions from another RP in context;
- it would need to modify SillyTavern core or a protected extension;
- any manifest file is missing or materially contradictory.
