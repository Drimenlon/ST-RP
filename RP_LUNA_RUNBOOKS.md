# Runbooks de RP para Luna

Baseline del host: **SillyTavern 1.19.0 stable (adopted).** `LUNA_READY` se limita a las operaciones conocidas que aparecen a continuación; no autoriza reparaciones no documentadas ni amplía las garantías de una herramienta.

## Prompt Inspector

- **Estado:** validado / adoptado.
- **Propósito:** inspeccionar el contexto construido antes de la llamada final.
- **Límite:** no demuestra la request final exacta recibida por el provider.
- **LUNA_READY:** YES para workflows conocidos de instalación/configuración/smoke test. Verificar el preset y contexto esperados antes de cualquier generación autorizada; si aparecen instrucciones o datos inesperados de otro RP, hacer STOP. No afirmar verificación del payload del provider basándose únicamente en esta vista.

## Inject Manager

- **Estado:** validado / adoptado.
- **Propósito:** observar/gestionar inyecciones de scripts de SillyTavern.
- **Límite:** la visibilidad no establece qué productor originó una inyección.
- **LUNA_READY:** YES para operaciones mecánicas conocidas. No inferir procedencia ni modificar inyecciones no relacionadas.

## WorldInfo Info

- **Estado:** validado / adoptado.
- **Propósito:** observar el estado real de activación de World Info.
- **Límite:** el panel refleja el último contexto construido y puede quedar desactualizado hasta que se reconstruya el contexto.
- **LUNA_READY:** YES para workflows conocidos de instalación/configuración/smoke test. Reconstruir el contexto antes de confiar en un cambio de estado de activación.

## Memory Books

- **Versión:** 9.3.4
- **Commit fijado:** `f779299a573aeb0701cf0e3410c40058d1ee0ddd`
- **Compatibilidad con el host:** PASS en SillyTavern 1.19.0; el error previo de carga por exportación del módulo `sha256` de ST 1.17.0 quedó resuelto en el host adoptado.
- **Evidencia observada:** preservación de hechos, relaciones, consecuencias e hilos abiertos; exclusión de fuentes y presencia de memoria en contexto; recuperación temporal útil; corrección manual; e independencia básica de ramas superaron la aceptación parcial registrada.
- **Todavía pendiente:** aceptación restante de aislamiento/Presence y rollback; la Fase 1 no se completó.
- **LUNA_READY:** **NO**. No crear ni aplicar un procedimiento de producción para Memory Books y no describir la extensión como plenamente aceptada/estable.

## Componentes existentes y límites

- **Summaryception:** componente de resumen/memoria preexistente. Aquí no se establece ninguna política de coexistencia o sustitución.
- **Presence:** preexistente; relevante para comportamiento de grupo, pero no hay cerrado un runbook de aislamiento grupal.
- **Recast:** preexistente y puede transformar outputs; no asumir sus efectos ni cambiarlo como workaround de pruebas.
- **Gallery Images:** extensión existente protegida. No modificarla ni modificar sus datos como parte de la ejecución del RP.
- Character Locks, World Info Locks, orden de lorebooks, Guided Generations, Story Mode, Custom Scenario, Timelines y Chat Top Bar no son capabilities cerradas; aquí no se define ningún procedimiento para Luna.

## Tarea reutilizable para Luna

```text
TAREA: <acción mecánica>
OBJETIVO: <RP / archivo / capability>
FUENTE DE VERDAD: <especificación READY y runbook aplicable>
MODIFICAR: <superficies explícitas>
PRESERVAR: <superficies explícitas>
VERIFICAR: <comprobaciones objetivas y resultados esperados>
STOP SI: el runtime difiere; falta un campo requerido; aparece ambigüedad;
         el trabajo destructivo es inesperado; aparece estado de otro RP; o
         sería necesario un arreglo de compatibilidad.
RESULTADO: PASS / BLOCKED
```
