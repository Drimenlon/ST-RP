# RP Architect workspace

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
    ├── GROUP.md
    ├── NARRATIVE_RULES.md
    └── OPENING.md
```

Los archivos de personaje contienen únicamente la definición operativa de ese personaje. El mundo, reglas narrativas, estado del grupo/escenario y opening se mantienen separados para evitar duplicación y contradicciones.

## Contrato de consumo

El `README.md` de cada grupo es el **manifest autoritativo** para ese RP. Debe indicar:

- identidad y status del RP;
- archivos que forman parte del paquete;
- orden de lectura;
- mapping semántico de cada archivo hacia SillyTavern;
- qué capacidades técnicas requiere;
- qué decisiones siguen abiertas;
- qué debe preservar Luna;
- verificaciones posteriores;
- condiciones de STOP.

Luna no debe descubrir archivos por intuición ni inferir cómo combinarlos. Debe seguir el README del grupo y los contratos globales de la raíz del repositorio.

## Ownership

RP Architect es autoridad sobre:

- historia;
- personajes;
- worldbuilding;
- relaciones;
- arcos;
- knowledge boundaries;
- intención narrativa;
- requisitos semánticos del RP.

Esta carpeta no autoriza por sí sola cambios técnicos en SillyTavern ni convierte una capability en `LUNA_READY`.

Para ejecución siguen siendo autoritativos:

- `RP_LUNA_EXECUTION_CONTRACT.md`
- `RP_READY_SPEC_SCHEMA.md`
- `RP_LUNA_RUNBOOKS.md`

Si un README de grupo marca el paquete como no READY, Luna debe detenerse y devolverlo para cierre semántico/técnico en lugar de improvisar.
