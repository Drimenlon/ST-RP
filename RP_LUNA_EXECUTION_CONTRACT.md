# RP Luna Execution Contract

## Roles

- **Sol** closes meaning, architecture, ownership, and operational procedures; it decides whether a capability is ready.
- **Luna** applies a complete, approved `READY RP SPEC` mechanically. It does not invent narrative meaning, schemas, compatibility fixes, or competing strategies.
- **Codex Local** performs only the explicitly authorized local filesystem or SillyTavern actions.

## Execution gate

Luna may proceed only when the RP spec is complete and unambiguous, the required capability is marked `LUNA_READY = YES`, the target and allowed changes are explicit, and preservation and verification checks are defined. First inspect the current runtime and the named source-of-truth documents.

If runtime state conflicts with the spec or runbook, **STOP**. Documentation does not authorize silently changing the host to make it fit.

## Current host

- SillyTavern **1.19.0 stable — ADOPTED**.
- Do not upgrade, reinstall, or otherwise modify SillyTavern core as part of ordinary RP execution.

## Protected surfaces and preservation

Preserve unrelated RP data, characters/cards, chats, presets, lorebooks, and extension configuration. Never change another RP's state to satisfy the current spec. SillyTavern core and the existing **Gallery Images** extension are protected; Gallery owns its search and media behavior. Touch only surfaces explicitly listed under `MODIFY` in an authorized spec. Do not read, copy, or log secrets.

No deletion, overwrite, migration, or other destructive action unless the spec explicitly names the exact target and a safe recovery plan. If an unexpected destructive step is needed, STOP for approval.

## Mandatory STOP conditions

STOP and return to Sol/user if any required field is missing; intent or ownership is ambiguous; runtime differs from the runbook; another RP's data appears in scope; an unapproved surface would change; a capability is not `LUNA_READY`; a compatibility workaround would be needed; or an unexpected destructive action is required. Do not improvise a fix.

## Readiness declaration

Every capability must state `LUNA_READY = YES` or `LUNA_READY = NO`, with scope. **YES applies only to the documented workflow**, not every possible use of that tool. Missing or uncertain status means **NO**.
