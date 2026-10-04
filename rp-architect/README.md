# Workspace de RP Architect

Esta carpeta es la raíz autoritativa de los RPs creados por **RP Architect**.

## Convención

Cada RP/grupo vive en su propia carpeta, cuyo nombre identifica al grupo narrativo.

Ejemplo:

```text
rp-architect/
└── Lafiel-Almion/
    ├── README.md
    ├── LAFIEL.md
    ├── ALMION.md
    ├── WORLD.md
    ├── WORLD_INFO.md
    ├── GROUP.md
    ├── NARRATIVE_RULES.md
    ├── PRESET_PROMPTS.md
    └── OPENING.md
```

Los archivos de personaje contienen la definición operativa de cada personaje. El mundo, World Info, reglas narrativas, prompts ejecutables, estado del grupo/escenario y apertura se mantienen separados para evitar duplicación y contradicciones.

## Idioma por defecto

Los RPs de este workspace se redactan y juegan en **español por defecto**, salvo que el manifest de un RP concreto indique explícitamente otro idioma.

Esto incluye:

- narración;
- diálogos;
- fichas de personaje;
- worldbuilding y contenido de World Info;
- reglas narrativas;
- prompts específicos del RP;
- aperturas y material de escenario.

Los identificadores técnicos de SillyTavern, nombres de archivos, nombres propios y valores estructurales pueden conservarse literalmente cuando sean necesarios para el mapping o la identidad técnica.

Las claves de activación de World Info pueden ser bilingües cuando mejore la robustez del matching sin alterar el idioma narrativo del RP.

## Contrato de consumo

El `README.md` de cada grupo es el **manifest autoritativo** para ese RP. Debe indicar:

- identidad del RP;
- `rp_architect_status`;
- estado técnico de ejecución por separado;
- idioma principal;
- archivos que forman parte del paquete;
- orden de lectura;
- mapping semántico de cada archivo hacia SillyTavern;
- capacidades técnicas requeridas;
- qué debe preservar Luna;
- verificaciones posteriores;
- condiciones de STOP.

Luna no debe descubrir archivos por intuición ni inferir cómo combinarlos. Debe seguir el README del grupo y los contratos globales de la raíz del repositorio.

## Separación obligatoria de estados

No confundir cierre semántico con readiness técnico.

### `rp_architect_status`

Lo decide RP Architect.

- `READY`: historia, personajes, relaciones, mundo, reglas narrativas, límites de conocimiento, escenario y demás intención semántica requerida por el paquete están cerrados para esta versión del RP.
- `DRAFT`: todavía falta una decisión creativa/semántica real de RP Architect.

Una capability técnica todavía no estabilizada, un preset que necesite mapping técnico o un runbook ausente **NO convierte por sí mismo un RP semánticamente cerrado en DRAFT**.

### `technical_execution_status`

Describe si el paquete puede aplicarse mecánicamente con los contratos/runbooks actuales.

Valores habituales:

- `READY_FOR_LUNA`: todas las operaciones necesarias están cerradas y Luna-ready.
- `PENDING_INFRASTRUCTURE_VALIDATION`: el RP está semánticamente cerrado, pero Infrastructure/Luna debe comprobar bindings, mappings o capabilities técnicas.
- `BLOCKED_<CAPABILITY>`: una capability técnica concreta impide completar la implementación.

Un bloqueo técnico debe devolverse a Infrastructure/Sol en la capability afectada; no reabre automáticamente la semántica del RP.

## Ownership

RP Architect es autoridad sobre:

- historia;
- personajes;
- worldbuilding;
- relaciones;
- arcos;
- límites de conocimiento;
- intención narrativa;
- idioma narrativo del RP;
- requisitos semánticos del RP.

Esta carpeta no autoriza por sí sola cambios técnicos en SillyTavern ni convierte una capability en `LUNA_READY`.

Para ejecución siguen siendo autoritativos:

- `RP_LUNA_EXECUTION_CONTRACT.md`
- `RP_READY_SPEC_SCHEMA.md`
- `RP_LUNA_RUNBOOKS.md`

Si `rp_architect_status: DRAFT`, Luna debe hacer STOP porque falta cierre semántico.

Si `rp_architect_status: READY` pero existe un bloqueo técnico, Luna debe preservar el paquete como semánticamente cerrado, reportar la capability/binding técnico concreto que falta y seguir los contratos globales sin improvisar.
