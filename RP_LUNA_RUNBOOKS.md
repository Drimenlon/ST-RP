# RP Luna Runbooks

Host baseline: **SillyTavern 1.19.0 stable (adopted).** `LUNA_READY` is limited to the known operations below; it does not authorize undocumented repair or broaden a tool's guarantees.

## Prompt Inspector

- **Status:** validated / adopted.
- **Purpose:** inspect the constructed pre-final context.
- **Limit:** does not prove the exact final request received by the provider.
- **LUNA_READY:** YES for known install/configuration/smoke workflows. Verify the expected preset and context before any authorized generation; if unexpected RP instructions or data appear, stop. Do not claim provider-payload verification from this view alone.

## Inject Manager

- **Status:** validated / adopted.
- **Purpose:** observe/manage SillyTavern script injections.
- **Limit:** visibility does not establish which producer originated an injection.
- **LUNA_READY:** YES for known mechanical operations. Do not infer provenance or modify unrelated injections.

## WorldInfo Info

- **Status:** validated / adopted.
- **Purpose:** observe actual World Info activation state.
- **Limit:** the panel reflects the last constructed context and may be stale until context is reconstructed.
- **LUNA_READY:** YES for known install/configuration/smoke workflows. Reconstruct context before relying on a changed activation state.

## Memory Books

- **Version:** 9.3.4
- **Pinned commit:** `f779299a573aeb0701cf0e3410c40058d1ee0ddd`
- **Host compatibility:** PASS on SillyTavern 1.19.0; the prior `sha256` module-export load error from ST 1.17.0 was resolved on the adopted host.
- **Observed evidence:** fact, relationship, consequence, and open-thread preservation; source exclusion and memory presence in context; useful temporal recall; manual correction; and basic branch independence passed in the recorded partial acceptance.
- **Still open:** remaining isolation/Presence and rollback acceptance; Phase 1 was not completed.
- **LUNA_READY:** **NO**. Do not create or apply a production Memory Books procedure, and do not describe the extension as fully accepted/stable.

## Existing components and boundaries

- **Summaryception:** pre-existing summarization/memory component. No coexistence or replacement policy is established here.
- **Presence:** pre-existing; relevant to group behavior, but no group-isolation runbook is closed.
- **Recast:** pre-existing and may transform outputs; do not assume its effects or change it as a test workaround.
- **Gallery Images:** existing protected extension. Do not modify it or its data as part of RP execution.
- Character Locks, World Info Locks, lorebook ordering, Guided Generations, Story Mode, Custom Scenario, Timelines, and Chat Top Bar are not closed capabilities; no Luna procedure is defined here.

## Reusable Luna task

```text
TASK: <mechanical action>
TARGET: <RP / file / capability>
SOURCE OF TRUTH: <READY spec and applicable runbook>
MODIFY: <explicit surfaces>
PRESERVE: <explicit surfaces>
VERIFY: <objective checks and expected results>
STOP IF: runtime differs; a required field is missing; ambiguity appears;
          destructive work is unexpected; another RP's state appears; or a
          compatibility fix would be required.
RESULT: PASS / BLOCKED
```
