# Lafiel & Almion

```yaml
status: DRAFT_NOT_READY
rp_id: lafiel-almion
rp_name: Lafiel & Almion
group_name: Lafiel & Almion
```

## Purpose

Primer RP de producción/prueba centrado en Lafiel y Almion antes de la entrada de Dalkon.

La dinámica principal es cuckolding psicológico, humillación aristocrática, celos, tensión de clase, orgullo y deseo contradictorio. No es una trama revolucionaria ni un triángulo amoroso genérico.

## Authoritative package

Luna debe leer los archivos de este paquete en este orden:

1. `README.md` — manifest, mapping y gates de ejecución.
2. `WORLD.md` — canon persistente del mundo relevante para este RP.
3. `NARRATIVE_RULES.md` — reglas globales de narración y comportamiento.
4. `LAFIEL.md` — definición operativa de la card de Lafiel.
5. `ALMION.md` — definición operativa de la card de Almion.
6. `GROUP.md` — participantes, rol de {{user}}, escenario compartido y knowledge boundaries.
7. `OPENING.md` — saludo/opening grupal exacto.

No inferir contenido desde otros archivos del repositorio salvo los contratos globales de infraestructura.

## Mapping hacia SillyTavern

- `LAFIEL.md` → Character Card `Lafiel`.
- `ALMION.md` → Character Card `Almion`.
- `WORLD.md` → fuente semántica para World Info/Lorebook de este RP. La representación técnica exacta debe seguir únicamente un mapping/runbook validado.
- `NARRATIVE_RULES.md` → requisitos del prompt global/preset del RP; no duplicar innecesariamente dentro de las cards.
- `GROUP.md` → definición del Group Chat `Lafiel & Almion`, escenario compartido y rol de {{user}}.
- `OPENING.md` → greeting inicial del grupo.

## Required characters

- Lafiel
- Almion

No crear una card para Dalkon en este RP.

El personaje de clase baja interpretado por `{{user}}` NO es Dalkon y no debe recibir automáticamente historia, reputación o capacidades de Dalkon.

## Memory

El RP inicial no depende de Memory Books.

Mientras Memory Books siga `LUNA_READY = NO`, Luna no debe configurarlo para este paquete.

## Presence / group isolation

Este paquete puede usar group chat normal, pero no debe depender de comportamiento Memory Books + Presence todavía no validado.

No inferir conocimiento privado entre personajes fuera de lo explícitamente definido en `GROUP.md`.

## Preset gate

El RP requiere un preset/config explícitamente ligado a este grupo.

La identidad técnica exacta del preset y su binding todavía están pendientes.

Por tanto el paquete permanece:

`DRAFT_NOT_READY`

No ejecutar todavía en SillyTavern hasta que ese binding quede cerrado y el README pase a `status: READY`.

## Preserve

Luna debe preservar:

- otros RPs, cards, groups y chats;
- presets/configs no pertenecientes a este RP;
- lorebooks ajenos;
- Summaryception, Presence y Recast salvo autorización explícita;
- Gallery Images y su configuración/datos;
- SillyTavern core.

## Verify when READY

Tras implementación deberá comprobarse al menos:

- existen exactamente las cards Lafiel y Almion con los campos suministrados;
- existe el grupo `Lafiel & Almion` con ambos participantes;
- el greeting coincide con `OPENING.md`;
- el preset correcto está ligado al RP y no hereda instrucciones de otro RP;
- el contexto construido contiene únicamente el canon/reglas esperados para este RP;
- no aparece Dalkon como participante ni como conocimiento implícito;
- no se modifica ningún RP ajeno.

## STOP IF

Luna debe STOP si:

- el preset/binding sigue sin resolver;
- alguna capability requerida no es `LUNA_READY`;
- necesita decidir cómo repartir semánticamente información entre superficies;
- encuentra otra versión de Lafiel/Almion y no está explícitamente autorizada a actualizarla;
- detecta instrucciones de otro RP en el contexto;
- necesita modificar SillyTavern core o una extensión protegida;
- cualquier archivo del manifest falta o se contradice materialmente con otro.
