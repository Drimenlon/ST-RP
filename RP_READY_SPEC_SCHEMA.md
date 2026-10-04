# READY RP Spec Schema

RP Architect supplies this minimum contract before Luna changes SillyTavern. Use `NOT APPLICABLE` only where the spec explains why; do not leave required decisions implicit.

```yaml
status: READY
rp_id: <stable unique id>
rp_name: <name>

characters:
  - identity: <exact card/name and how to identify it>
    source: <provided card/source>
    required_fields: <explicit fields and intended values/content>
    greeting: <exact text, or NOT APPLICABLE>

preset:
  identity: <exact intended preset name/id>
  binding: <how this RP/chat must use it>
  required_configuration: <explicit settings, or none>

lorebooks_world_info:
  books: <exact RP-owned books, or none>
  entries: <provided content and required fields, or none>
  bindings_activation_order: <explicit requirements, or none>

memory:
  provider: <provider, or none>
  configuration: <explicit values, only if provider is LUNA_READY>

group:
  participants: <exact character identities, or none>
  presence_rules: <explicit supplied rules, or none>

extensions:
  settings: <only explicitly RP-owned settings; name capability and values>

preserve:
  - unrelated RP data, characters, chats, presets, lorebooks, and extension settings
  - SillyTavern core
  - Gallery Images implementation and its data/behavior

verify:
  - <objective post-change checks and expected results>

stop_if:
  - <spec-specific ambiguity or mismatch>
```

## Required interpretation checks

- A new character or chat does **not** imply a clean prompt. Verify that the exact intended preset is bound; do not assume the currently selected preset belongs to this RP. Check for foreign RP instructions before generation or smoke testing. If the preset identity/binding or prompt ownership is unclear, STOP.
- Lorebook content and bindings must be supplied or explicitly referenced by stable identity. Do not invent entries, activation rules, or ordering.
- Configure memory only when that exact provider/workflow is `LUNA_READY = YES`. Do not infer coexistence or replacement rules between memory systems.
- Group participants and any Presence behavior must be explicit. Do not infer Presence compatibility or group-memory isolation.
- Extension changes are allowed only when the spec names the extension, exact owned setting, desired value, and validation. Never change unrelated/global configuration by assumption.
- Gallery Images and SillyTavern core remain protected even if the RP asks for adjacent behavior; escalate for separate authorization.

## Readiness question

Before acting, Luna must be able to answer: **“Can I implement this literally without deciding what the author meant?”** If not, or if any required binding/value is unresolved, the spec is not READY: STOP and return it for clarification.
