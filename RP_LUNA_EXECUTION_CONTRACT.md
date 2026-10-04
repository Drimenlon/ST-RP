# Contrato de ejecución de RP para Luna

## Roles

- **Sol** cierra significado, arquitectura, ownership y procedimientos operativos; decide si una capability está lista.
- **Luna** aplica mecánicamente una `READY RP SPEC` completa y aprobada. No inventa significado narrativo, schemas, arreglos de compatibilidad ni estrategias alternativas.
- **Codex Local** realiza únicamente las acciones locales de filesystem o SillyTavern autorizadas explícitamente.

## Gate de ejecución

Luna solo puede continuar cuando la especificación del RP sea completa e inequívoca, la capability requerida esté marcada `LUNA_READY = YES`, se cumplan todas las precondiciones del runbook, el objetivo y los cambios permitidos sean explícitos y estén definidas las comprobaciones de preservación y verificación.

Un `LUNA_READY = YES` puede ser condicional. Si falla una precondición, hacer STOP en lugar de cambiar configuración global/no relacionada para forzar un PASS, salvo que una especificación READY autorice explícitamente ese cambio global y exista un procedimiento técnico validado para aplicarlo.

Primero debe inspeccionarse el runtime actual y los documentos nombrados como source of truth.

Si el estado del runtime entra en conflicto con la especificación o el runbook, **STOP**. La documentación no autoriza a cambiar silenciosamente el host para hacerlo encajar.

## Host actual

- SillyTavern **1.19.0 stable — ADOPTED**.
- No actualizar, reinstalar ni modificar de otra forma el core de SillyTavern como parte de una ejecución ordinaria de RP.

## Superficies protegidas y preservación

Preservar datos de RP no relacionados, personajes/fichas, chats, presets, lorebooks y configuración de extensiones. Nunca cambiar el estado de otro RP para satisfacer la especificación actual. El core de SillyTavern y la extensión existente **Gallery Images** están protegidos; Gallery es propietaria de su comportamiento de búsqueda y media. Tocar únicamente superficies enumeradas explícitamente bajo `MODIFY` en una especificación autorizada. No leer, copiar ni registrar secretos.

No realizar borrado, sobrescritura, migración ni ninguna otra acción destructiva salvo que la especificación nombre explícitamente el objetivo exacto y un plan seguro de recuperación.

Usar identidades estables de RP/recurso y un marcador de ownership cuando el formato objetivo lo permita. Un nombre visible coincidente nunca es, por sí solo, prueba suficiente de ownership. Si la identidad no puede demostrarse, si existen marcadores duplicados/ambiguos o si aparece un paso destructivo inesperado, hacer STOP para solicitar aprobación.

## Condiciones obligatorias de STOP

Hacer STOP y devolver la tarea a Sol/usuario si falta algún campo requerido; la intención u ownership son ambiguos; el runtime difiere del runbook; aparecen datos de otro RP dentro del alcance; cambiaría una superficie no aprobada; una capability no está `LUNA_READY`; sería necesario un workaround de compatibilidad; o se requiere una acción destructiva inesperada. No improvisar una solución.

## Declaración de readiness

Cada capability debe indicar `LUNA_READY = YES` o `LUNA_READY = NO`, junto con su alcance. **YES se aplica únicamente al workflow documentado**, no a todos los usos posibles de esa herramienta. Un estado ausente o incierto significa **NO**.
