# Research — RP / SillyTavern roadmap extension landscape

**Fecha:** 2026-10-08  
**Owner operativo:** Chat Local — RP / SillyTavern Infrastructure  
**Repo:** `Drimenlon/ST-RP`  
**Estado:** **RESEARCH / INPUT PARA RP ARCHITECT**  
**No es todavía una decisión canónica de roadmap salvo donde el roadmap ya lo hubiera decidido previamente.**

---

## 1. Objetivo

Esta investigación se realizó antes de seguir consumiendo prompts de Codex/Work para instalar, auditar y validar cada fase del roadmap RP.

La pregunta central fue:

> ¿Qué partes del roadmap ya están resueltas por extensiones existentes y suficientemente documentadas, qué partes necesitan una prueba local real, y qué partes no justifican ingeniería propia?

La estrategia recomendada que emerge de la investigación es:

1. **documentación oficial / README;**
2. **changelog;**
3. **código fuente actual;**
4. **issues / señales de uso real cuando aporten contexto;**
5. **smoke test local únicamente para incertidumbres críticas de nuestra combinación exacta.**

No se pretende “confiar ciegamente” en documentación ni “probar todo”.  
El objetivo es evitar tanto la fe ciega como la auditoría de NASA.

---

## 2. Criterio de evidencia

### Evidencia fuerte
- comportamiento documentado por el maintainer y coherente con el código;
- changelog actual que explicita cambios de comportamiento;
- código fuente que muestra la ruta efectiva de lectura/escritura;
- prueba local ya ejecutada en nuestro ST 1.19.

### Evidencia media
- README sin verificación de código;
- issues concretos reproducibles;
- documentación de versión anterior cuando no hay indicios de cambio.

### Evidencia débil / contextual
- Reddit, Discord, comentarios de usuarios;
- impresiones de compatibilidad sin reproducción;
- recomendaciones genéricas de comunidad.

Las señales comunitarias sirven para descubrir problemas y patrones, no para reemplazar documentación/código/pruebas.

---

# 3. Hallazgos por fase/extensión

## 3.1 Phase 1 — Memory Books

### Proyecto
- Repo: https://github.com/aikohanasaki/SillyTavern-MemoryBooks
- Canonical local project baseline ya adoptado en este proyecto:
  - versión: **9.3.4**
  - commit: `f779299a573aeb0701cf0e3410c40058d1ee0ddd`
- Host actual: SillyTavern **1.19.0 stable**.

### Fuentes revisadas
- Getting Started:
  https://github.com/aikohanasaki/SillyTavern-MemoryBooks/blob/main/Start_Here.md
- AI Reference Manual:
  https://github.com/aikohanasaki/SillyTavern-MemoryBooks/blob/main/userguides/1%20Memory_Books_AI_Reference_Manual.md

### Lo importante
Memory Books guarda recuerdos como entradas de lorebook y puede usar un libro separado de memoria. El propio Getting Started recomienda la separación porque facilita budget, reutilización, export y gestión mediante Lorebook Ordering.

La documentación también contempla explícitamente chats de grupo y configuración de Memory Books separadas por personaje cuando se desea.

### Corrección importante a nuestro antiguo acceptance plan
Nuestro plan antiguo trataba “edit”, “delete”, “rollback” y “swipe” como si todos debieran disparar una reconciliación automática equivalente.

Eso no es un criterio válido.

La documentación actual distingue el rollback automático de operaciones normales de edición/swipe. El comportamiento de rollback está orientado a eliminación/truncado del historial y además no debe asumirse habilitado por defecto.

Por tanto:

- **un edit que no reescriba automáticamente un recuerdo NO debe clasificarse como FAIL por sí solo**;
- los swipes tampoco deben evaluarse como si fueran rollback;
- si queremos usar rollback automático como feature operativa, entonces sí merece un smoke sintético específico de delete/truncate/rollback.

### Evidencia local ya positiva
Antes de esta investigación ya existía evidencia positiva para:
- preservation de hechos;
- relaciones;
- consecuencias;
- open threads;
- source exclusion;
- activación/presencia en contexto;
- temporal recall con respuesta útil;
- corrección manual persistente;
- independencia parent/child en branches;
- normalización de metadata visible.

Una aparente contaminación cross-RP se investigó y se atribuyó a preset/config heredado, no a Memory Books.

Invariante ya establecido:

> crear un personaje/chat nuevo NO implica un prompt neutral; preset/config debe ser explícito por RP.

### Qué sí merece prueba local
La documentación no puede garantizar nuestra combinación exacta:

`Memory Books + Presence 3.5.0 + ST 1.19 + nuestra configuración`.

Por eso el cierre de Phase 1 debería reducirse a:

1. **smoke real Group + Presence**;
2. **opcional**: un smoke delete/rollback si decidimos que auto-rollback forma parte del uso requerido;
3. clasificación formal y cierre.

### Conclusión
**No repetir toda la batería histórica.**  
Memory Books parece requerir como máximo un prompt de Codex pequeño para cerrar gaps reales.

---

## 3.2 Chat Top Bar — mover antes en el roadmap

### Proyecto
- Repo: https://github.com/SillyTavern/Extension-TopInfoBar
- README:
  https://github.com/SillyTavern/Extension-TopInfoBar/blob/main/README.md

### Qué hace
Añade una barra superior con accesos a:
- lista de chats;
- file manager;
- nombre/selector de chat;
- búsqueda;
- new chat;
- rename;
- delete;
- close.

### Relación con Memory Books
Memory Books documenta integración opcional con Chat Top Bar / Chat Top Info Bar para mostrar una **Job Queue**:
- progreso;
- jobs fallidos;
- retry;
- cancel;
- review-needed.

Memory Books funciona sin Top Bar, pero la cola aporta observabilidad operativa.

### Implicación
No tiene sentido reservar Top Bar para el final como Phase 8 si ya es útil durante Phase 1.

Propuesta:

> moverlo a **1.5 — utility opcional**, incluso instalar manualmente sin consumir Codex.

### Codex
**0 prompts** salvo incompatibilidad real.

---

## 3.3 Phase 2.1 — Character Locks vs Generation Locks

### Generation Locks
- Repo:
  https://github.com/aikohanasaki/SillyTavern-GenerationLocks
- README:
  https://github.com/aikohanasaki/SillyTavern-GenerationLocks/blob/main/README.md
- Comparativa oficial:
  https://github.com/aikohanasaki/SillyTavern-GenerationLocks/blob/main/compare.md
- Changelog:
  https://github.com/aikohanasaki/SillyTavern-GenerationLocks/blob/main/CHANGELOG.md
- Manifest revisado: versión **1.2.4**

### Hallazgo principal
Generation Locks (STGL) es la evolución consolidada de:
- Character Locks (STCL);
- CC Prompt Manager (CCPM).

Bloquea tres familias:
- connection profile;
- generation preset;
- completion template.

Dimensiones documentadas:
- Character;
- Model;
- Chat;
- Group;
- Individual-in-Group.

Incluye:
- prioridad configurable;
- auto-apply Never / Ask / Always;
- overlay individual sobre Group cuando se habilita;
- status indicator;
- migración desde STCL / CCPM;
- protección/context validation alrededor de cambios asíncronos.

El changelog indica que desde 1.1.0 se considera estable/recomendada por el maintainer, y versiones posteriores incluyen fixes de apply loops y Assistant/default-character handling.

### Restricción crítica
**STGL es para Chat Completion.**

La propia comparativa aclara que Character Locks sigue siendo útil cuando se necesita Text Completion.

### Implicación para nuestro stack
Nuestro RP actual está operando en Chat Completion.

Por ello, la propuesta técnica es:

> reemplazar provisionalmente **2.1 Character Locks** por **2.1 Generation Locks**.

Esto no debe convertirse en canon hasta que RP Architect lo acepte, porque es un cambio de solución dentro de una fase existente.

### Codex
Probablemente **0–1 prompt**:
- instalación/config manual puede bastar;
- una única validación A→B→A o character/chat/group puede cerrar integración.

---

## 3.4 Phase 2.2 — World Info Locks

### Proyecto
- Repo:
  https://github.com/aikohanasaki/SillyTavern-WorldInfoLocks
- README:
  https://github.com/aikohanasaki/SillyTavern-WorldInfoLocks/blob/master/README.md
- Changelog:
  https://github.com/aikohanasaki/SillyTavern-WorldInfoLocks/blob/master/CHANGELOG.md
- Manifest revisado: versión **1.10.5**

### Capacidades relevantes
World Info Locks gestiona presets de World Info y puede capturar:
- selección de lorebooks;
- settings de activación opcionales;
- profundidad;
- budget/cap;
- recursion;
- text matching;
- scoring/strategy;
- otras opciones de WI.

Permite locks por:
- character;
- chat.

En group chats, la documentación actual trata el contexto de grupo de forma específica: los character locks no se aplican como si fuera un solo personaje; el lock efectivo se gestiona mediante el contexto/chat de grupo.

También aporta:
- prioridad configurable chat vs character;
- global default;
- import/export;
- rename detection;
- selección granular de settings que un preset controla.

### Por qué encaja con nuestra arquitectura
Ya sufrimos un caso real donde un RP heredó configuración/preset no neutral.

World Info Locks ataca exactamente la clase de error:

> “estoy en este RP pero están activos libros/settings de otro contexto”.

### Recomendación
Mantener la fase. No hacer investigación Codex grande.

### Smoke suficiente
- contexto A;
- cambiar a B;
- verificar preset/books/settings esperados;
- volver a A;
- confirmar restore.

Prompt Inspector + WorldInfo Info pueden observar el resultado.

### Codex
**0–1 prompt**, preferentemente combinado con Generation Locks + Lorebook Ordering.

---

## 3.5 Phase 3 — Lorebook Ordering

### Proyecto
- Repo:
  https://github.com/aikohanasaki/SillyTavern-LorebookOrdering
- Changelog:
  https://github.com/aikohanasaki/SillyTavern-LorebookOrdering/blob/main/CHANGELOG.md

### Hallazgo importante: documentación histórica contradictoria
Versiones antiguas/documentación histórica asociaban STLO a una insertion strategy concreta.

El changelog actual declara un breaking change en **v2.0.0**:

> se elimina el check de insertion strategy; si STLO está habilitado, funciona; “strategy no longer matters”.

Por tanto, no debemos convertir documentación vieja sobre strategy en requirement actual.

### Cambios posteriores relevantes
- v2.1.0: aprovecha `WORLDINFO_SCAN_DONE` para acelerar el procesamiento en ST moderno;
- v2.2.0: random trim opcional;
- v2.2.4, 2026-09-24: fix de un caso donde entradas descartadas por budget durante recursion podían volver a entrar al rescan y provocar loops.

El changelog también documenta soporte/overrides de group chat y per-character behavior.

### Relación con Memory Books
Memory Books recomienda separar el memory lorebook y gestionarlo de manera independiente; Lorebook Ordering es una solución natural para dar prioridad diferente a:
- memoria;
- canon;
- flavor;
- character-specific lore.

### Recomendación
Mantener la fase y usar la versión actual, no una versión indexada vieja.

### Codex
**0–1 prompt**, idealmente compartido con 2.1 y 2.2 en un solo integration smoke.

---

# 4. Structured Scene State

## 4.1 Hallazgo: zTracker ya cubre gran parte del problema

### Proyecto
- Repo:
  https://github.com/Zaakh/SillyTavern-zTracker
- README:
  https://github.com/Zaakh/SillyTavern-zTracker/blob/main/readme.md
- Changelog:
  https://github.com/Zaakh/SillyTavern-zTracker/blob/main/CHANGELOG.md
- Changelog observado hasta **v2.8.0 — 2026-10-01**

### Arquitectura actual
Desde 2.0 zTracker permite múltiples **Modules** independientes, con:
- schema propio;
- prompt propio;
- connection propia;
- generation propia;
- injection propia;
- auto-mode independiente;
- history/snapshot behavior independiente.

Los módulos se pueden:
- añadir;
- clonar;
- reordenar;
- borrar;
- exportar;
- importar.

También existe orden de generación y capacidad de que un módulo consuma historial de módulos anteriores.

### Starter modules
La versión moderna incluye/seedea:
- **Scene Tracker**;
- **Plot Log**;
- **Plot Steer**.

La recomendación para nuestro stack es:

> usar **Scene Tracker** / un módulo derivado para Structured Scene State;
> mantener **Plot Log** y **Plot Steer** inicialmente desactivados para no solapar Memory Books y Narrative Steering.

### Persistencia
Los snapshots del tracker quedan asociados a mensajes/chat, no convertidos automáticamente en World Info persistente.

Eso encaja con nuestra separación conceptual:

- Memory Books = qué ocurrió;
- Scene State = cómo están las cosas ahora;
- World Info = canon persistente aprobado.

### Regeneración granular
zTracker permite regenerar:
- tracker completo;
- top-level field;
- array item;
- campo concreto de un array item.

También tiene cleanup/pending targets.

Esto es especialmente útil para un state estructurado donde un único campo puede quedar mal sin necesidad de regenerar todo.

### JSON Schema
zTracker soporta un subconjunto concreto de JSON Schema y documenta errores/warnings sobre:
- arrays sin items;
- objects sin properties;
- keywords ignoradas;
- identidad de items;
- dependency annotations.

También puede derivar HTML desde schema.

### World Info durante generación del tracker
zTracker puede:
- incluir todo WI;
- excluirlo;
- allowlist por libro/UID.

Esto permite evitar que el tracker lea capas que no queremos que contaminen la extracción.

### Propuesta de schema conceptual
RP Architect ya definió como posibles campos:

- location;
- approximate time/date;
- present characters;
- active cover identities;
- current objectives;
- known facts by character;
- active deceptions;
- unresolved threads;
- explicit boundaries;
- established precedents;
- recent consequences.

Restricción canónica actual:

> NO usar barras numéricas tipo affection / desire / corruption / trust salvo autorización futura.

### Implicación
Antes de desarrollar una extensión propia, probar:

> **zTracker + schema RP propio**

Si satisface las invariantes, elimina un proyecto entero de ingeniería.

### Codex
**1 prompt** razonable para:
- materializar schema;
- configurar un módulo;
- probar un chat sintético;
- observar inyección/actualización.

---

# 5. NPC Lore Promotion / Lore Promotion Queue

## 5.1 Candidato: World Info Recommender (WREC)

### Proyecto
- Repo:
  https://github.com/bmen25124/SillyTavern-WorldInfo-Recommender
- README:
  https://github.com/bmen25124/SillyTavern-WorldInfo-Recommender/blob/main/readme.md
- Código inspeccionado:
  - `src/components/SuggestedEntry.tsx`
  - `src/components/MainPopup.tsx`
  - `src/generate.ts`
  - `src/commands.ts`
- Manifest/source observado: versión extension **0.2.0**

### Requirement del Architect
El flujo deseado es:

1. NPC incidental;
2. recurrencia/importancia;
3. extracción de hechos establecidos;
4. propuesta World Info;
5. review humana;
6. discard/edit/approve;
7. sólo después materialización persistente.

Principio:

> **NO AUTO-CANON SILENCIOSO.**

### Qué hace WREC realmente según el código
Las generaciones producen **suggested entries**.

La UI de una sugerencia ofrece:
- Add / Update;
- Revise;
- Continue;
- Edit;
- Compare;
- Blacklist;
- Remove.

El código de `SuggestedEntry.tsx` no materializa una entrada simplemente por haber sido generada.

La escritura a World Info ocurre cuando se ejecuta el flujo de **Add/Update**.

En `MainPopup.tsx`, el flujo aplica la sugerencia sobre una copia del World Info y posteriormente usa `saveWorldInfo` cuando el usuario aplica la acción.

También existe una acción “Add All” que solicita confirmación antes de guardar las sugerencias.

### Encaje con proposal-only
Esto es muy cercano a:

> detect/propose → review/edit → explicit apply → World Info

Por tanto, antes de construir una Lore Promotion Queue propia, WREC debe considerarse candidato serio.

### Limitaciones / riesgos
WREC depende de salida estructurada XML y su propio README advierte que:
- modelos RP pequeños pueden fallar;
- presets “fancy” de RP no son ideales;
- es mejor un perfil/preset simple dedicado para output estructurado;
- puede ser necesario aumentar max response tokens.

Además, se observó durante la investigación un issue abierto de 2026 sobre compatibilidad de schema/settings con modelos GPT. Ese punto debe tratarse como incertidumbre real hasta probar nuestra combinación actual.

### Acceptance mínimo propuesto
Un único escenario sintético:

1. historial contiene NPC recurrente;
2. pedir recomendación;
3. comprobar que aparece como sugerencia;
4. verificar que **World Info NO cambia todavía**;
5. editar propuesta;
6. aprobar explícitamente;
7. verificar que entonces sí aparece en World Info;
8. comprobar ownership/target correcto.

Si esto pasa, gran parte de Phase 3.6 puede resolverse sin desarrollo propio.

### Codex
**1 prompt**.

---

# 6. Narrative Reasoning / Steering

## 6.1 Guided Generations

### Proyecto
- Repo:
  https://github.com/Samueras/GuidedGenerations-Extension
- README:
  https://github.com/Samueras/GuidedGenerations-Extension/blob/main/README.md

### Capacidades
- Guided Response;
- Guided Swipe;
- Impersonation 1st/2nd/3rd;
- Persistent Guides;
- Situational / Thinking / Clothes / State / Rules / Custom guides;
- Corrections;
- Separated Thinking;
- Simple Send;
- Edit Intros;
- Input Recovery.

Permite seleccionar profiles/presets distintos por tool sin cambiar globalmente la conexión activa.

### Riesgo de solapamiento
Guided Generations también puede mantener State/Thinking/Clothes guides y lanzar triggers automáticos.

Si zTracker adquiere ownership de **Structured Scene State**, no deberíamos activar automáticamente otro “State tracker” que produzca una segunda fuente de verdad.

### Recomendación
Para nuestro estilo de RP dirigido por usuario:

> probar **Guided Generations primero** como capa explícita de dirección/corrección.

Inicialmente:
- State guide auto: OFF;
- tracker-like features que dupliquen zTracker: OFF;
- usar Guided Response / Swipe / Corrections / Separated Thinking según necesidad.

---

## 6.2 Stepped Thinking

### Proyecto
- Repo:
  https://github.com/cierru/st-stepped-thinking
- README:
  https://github.com/cierru/st-stepped-thinking/blob/master/README.md

### Qué hace
Stepped Thinking implementa **prompt chaining previo a la respuesta normal**.

Puede ejecutar un número arbitrario de prompts para generar pensamientos/emociones/planes antes de la generación regular.

La propia documentación reconoce el tradeoff:

> más tiempo de espera a cambio de intentar mejorar la respuesta.

Incluye:
- múltiples prompts de pensamiento;
- historial de pensamientos;
- regeneración;
- regex cleanup;
- ocultación/spoiler;
- settings por personaje;
- exclusión de personajes;
- aislamiento de pensamientos por personaje en grupos;
- opcionalmente permitir que personajes “lean” pensamientos de otros.

README actual indica compatibilidad probada con ST 1.15+.

### Diferencia conceptual
- **Guided Generations**: control/director humano + corrección/refinamiento.
- **Stepped Thinking**: deliberación/prompt-chain automática antes de la respuesta.

No son lo mismo, pero sí pueden acumular capas y latencia.

### Recomendación
**No instalar ambos automáticamente de entrada.**

Orden propuesto:
1. Guided Generations;
2. usar RP real;
3. sólo si seguimos echando en falta planificación interna previa, probar Stepped Thinking.

### Codex
No se justifica un prompt sólo para instalarlo.

---

# 7. Story Mode

### Proyecto
- Repo:
  https://github.com/Prompt-And-Circumstance/StoryMode
- README:
  https://github.com/Prompt-And-Circumstance/StoryMode/blob/main/README.md
- Changelog:
  https://github.com/Prompt-And-Circumstance/StoryMode/blob/main/CHANGELOG.md
- Manifest revisado: **1.1.5**
- README/changelog documentan feature-set de 1.1.x.

### Capacidades actuales
- tipos de historia;
- author style;
- arco Setup → Escalation → Resolution;
- arc length;
- scenario blueprints;
- scene/beat progression;
- opening message generation;
- scenario library;
- PNG metadata import/export;
- epilogue;
- summarization;
- “what’s next”;
- configurable prompt injection;
- perfiles API por fase en versiones recientes.

### Solapamiento
Story Mode puede convertirse fácilmente en una capa grande que toque:
- pacing;
- planning;
- summaries;
- scene progression;
- character injection.

Por eso no debe adquirir accidentalmente ownership sobre:
- Memory Books;
- Structured Scene State;
- World Info canon;
- Lore Promotion.

### Importante
Su propio README coloca como features futuras:
- mejor World Lore Integration;
- World State Tracking;
- Lorebook Generation.

No debemos asumir que Story Mode ya resuelve esas capas.

### Recomendación
Mantenerlo como **capa opcional de narrative planning/orchestration**.

Probar después de que memory/state/lore ownership esté cerrado.

---

# 8. Custom Scenario

### Proyecto
- Repo:
  https://github.com/bmen25124/SillyTavern-Custom-Scenario
- README:
  https://github.com/bmen25124/SillyTavern-Custom-Scenario/blob/main/readme.md
- Manifest revisado: **0.4.5**

### Qué hace realmente
Es principalmente un **constructor parametrizable de character cards/scenarios**.

Permite:
- preguntas de texto/dropdown/checkbox;
- variables;
- sustitución en description, first message, personality, scenario notes, character notes;
- scripting JS simple;
- import/export JSON/PNG;
- lectura de lorebook entries desde scripting.

### Implicación
No es infraestructura indispensable para nuestro RP long-run actual.

Sólo aporta valor directo si queremos un workflow tipo:

> “abre plantilla → responde preguntas → genera variante de character/scenario”.

### Recomendación
Mover de **core roadmap** a **optional capability**.

No consumir Codex salvo que el usuario decida usarla.

---

# 9. Timelines

### Proyecto
- Repo:
  https://github.com/SillyTavern/SillyTavern-Timelines
- README:
  https://github.com/SillyTavern/SillyTavern-Timelines/blob/master/README.md

### Hallazgo conceptual
La extensión **NO es una timeline semántica del mundo ficticio**.

Representa gráficamente:
- chats;
- branches;
- swipes;
- checkpoints;
- mensajes compartidos entre chats.

Permite:
- fulltext search;
- navegar a nodos;
- expandir swipes;
- crear branch desde un mensaje;
- seguir checkpoint paths.

### Consecuencia
No debe describirse como:

> “Timelines = cuándo ocurrió”.

La separación correcta sería:

- **Memory Books** = qué ocurrió;
- **Scene State** = cómo están las cosas ahora;
- **event chronology futura** = cuándo ocurrió;
- **SillyTavern Timelines** = navegación del grafo de historial/branches.

### Recomendación
Renombrar la fase conceptual a:

> **Branch / History Navigator — Timelines**

Si en el futuro necesitamos una cronología ficticia consultable, es otra capability.

---

# 10. Roadmap técnico recomendado para revisión del Architect

> Esta tabla es propuesta de research, NO decisión canónica hasta aceptación del RP Architect.

| Orden propuesto | Capability | Solución candidata | Cambio |
|---|---|---|---|
| 1 | Memory Books | actual | cerrar sólo gaps reales |
| 1.5 | Chat Top Bar | Extension-TopInfoBar | adelantar como utility |
| 2.1 | Generation Locks | STGL | sustituir Character Locks si seguimos Chat Completion |
| 2.2 | World Info Locks | STWIL | mantener |
| 3 | Lorebook Ordering | STLO | mantener; seguir changelog actual |
| 3.5 | Structured Scene State | zTracker | preferir schema propio sobre extensión nueva |
| 3.6 | NPC Lore Promotion | WREC candidato | validar proposal-only antes de construir |
| 4 | Narrative Steering | Guided Generations primero | Stepped Thinking condicional |
| 5 | Story Mode | Story Mode | opcional/orchestration, sin ownership de memory/state/lore |
| 6 | Custom Scenario | optional | sacar del core |
| 7 | Branch/History Navigator | Timelines | renombrar semántica |
| 8 | — | — | Top Bar ya adelantado |

---

# 11. Nuevo enfoque de ejecución

## No hacer
- una auditoría completa por extensión;
- repetir pruebas que el código/documentación ya cierran;
- instalar dos capas que compitan por la misma fuente de verdad;
- usar Codex como “botón Install Extension”.

## Sí hacer
- instalar manualmente las extensiones simples cuando el orden/config ya esté claro;
- usar Prompt Inspector / WorldInfo Info para observar invariantes críticas;
- usar Codex sólo para:
  - configuración no trivial;
  - integración entre extensiones;
  - smoke de persistencia/canon;
  - schema/materialización;
  - resolver contradicciones reales.

---

# 12. Presupuesto revisado de Codex

El usuario fijó un máximo de **5 prompts** para este roadmap; si no basta, prefiere instalar manualmente y recibir el orden/config.

Tras esta investigación, el objetivo técnico razonable es **4 prompts + 1 reserva**:

### Prompt 1
**Memory Books**
- Group + Presence;
- rollback/delete sólo si forma parte del uso requerido;
- cierre formal.

### Prompt 2
**Generation Locks + World Info Locks + Lorebook Ordering**
- después de instalación/config;
- un único integration smoke;
- comprobar cambio de contexto y restore correcto.

### Prompt 3
**zTracker / Structured Scene State**
- schema definido por RP Architect;
- materialización;
- synthetic update;
- observación de snapshot/inyección;
- sin Plot Log/Steer inicialmente.

### Prompt 4
**WREC / NPC Lore Promotion**
- propuesta sin escritura;
- review/edit;
- explicit apply;
- verificación World Info.

### Prompt 5
**Reserva**
Usar sólo si:
- aparece incompatibilidad material;
- WREC falla y hay que decidir una alternativa;
- Narrative/Story Mode presenta integración realmente ambigua;
- otra capability nueva requiere Sol.

No gastar el prompt 5 por ceremonia.

---

# 13. Ownership recomendado entre capas

## Memory Books
Fuente de memoria histórica derivada:
> qué ocurrió.

## Structured Scene State / zTracker
Estado presente estructurado:
> cómo están las cosas ahora.

## NPC Lore Promotion
Proceso de decisión:
> qué entidad/hecho recurrente merece convertirse en canon persistente.

## World Info
Canon persistente aprobado.

## Lorebook Ordering
Prioridad/activación entre libros.

## Generation Locks
Fijación de profile/preset/template por contexto.

## Guided Generations
Dirección/corrección narrativa del siguiente output.

## Story Mode
Planning/orchestration opcional.

## Timelines
Navegación de ramas/historial, no cronología semántica.

---

# 14. Riesgos de doble ownership detectados

### zTracker vs Guided Generations State Guide
No activar dos state trackers como autoridades simultáneas.

### Memory Books vs zTracker Plot Log
Plot Log puede parecer memoria histórica; mantenerlo OFF inicialmente.

### zTracker Plot Steer vs Guided Generations / Story Mode
Puede introducir varias capas de steering en paralelo.

### WREC vs auto-canon
WREC sólo es aceptable si el flujo efectivo sigue siendo review-before-write en nuestro setup.

### Story Mode vs Memory/State/Lore
Story Mode no debe adueñarse automáticamente de capas que ya tienen owner.

### Generation Locks vs otras extensiones que cambian profiles/presets
Hay que validar que la prioridad/autopapply no cause loops con herramientas auxiliares que usan perfiles dedicados.

---

# 15. Qué debe decidir RP Architect

Antes de cambiar el roadmap canónico, Architect debe pronunciarse sobre:

1. **Character Locks → Generation Locks** para Chat Completion.
2. **Top Bar** adelantado a utility temprana.
3. **Structured Scene State → zTracker** como implementación preferente.
4. **WREC** como candidato de NPC Lore Promotion.
5. **Guided Generations primero / Stepped Thinking condicional**.
6. **Custom Scenario** fuera del core.
7. **Timelines renombrado** a Branch/History Navigator.
8. límites de schema de Scene State y qué campos son realmente canónicos.

Infrastructure no debe convertir estas propuestas en decisiones semánticas por su cuenta.

---

# 16. Estado de confianza

| Área | Confianza | Motivo |
|---|---|---|
| Memory Books semantics | Alta | docs extensas + experiencia local previa |
| Generation Locks reemplaza STCL para Chat Completion | Alta técnica / pendiente Architect | comparativa oficial + changelog |
| World Info Locks | Alta | README + manifest + lifecycle claro |
| Lorebook Ordering strategy actual | Alta | changelog explícito |
| zTracker para Scene State | Alta como candidato | arquitectura/modules/schema muy alineados |
| WREC proposal-only | Alta en source actual; media en compatibilidad GPT | escritura inspeccionada; issue/structured-output risk |
| Guided vs Stepped | Alta conceptual | READMEs describen workflows distintos |
| Story Mode ownership limitado | Alta | feature-set actual vs planned features |
| Custom Scenario optional | Alta | scope estrecho y claro |
| Timelines no es semantic chronology | Muy alta | README define navegación de branches/chats |
| Top Bar temprano | Alta | utility simple + integración MB |

---

# 17. Fuentes principales

## Memory Books
- https://github.com/aikohanasaki/SillyTavern-MemoryBooks
- https://github.com/aikohanasaki/SillyTavern-MemoryBooks/blob/main/Start_Here.md
- https://github.com/aikohanasaki/SillyTavern-MemoryBooks/blob/main/userguides/1%20Memory_Books_AI_Reference_Manual.md

## Generation Locks
- https://github.com/aikohanasaki/SillyTavern-GenerationLocks
- https://github.com/aikohanasaki/SillyTavern-GenerationLocks/blob/main/compare.md
- https://github.com/aikohanasaki/SillyTavern-GenerationLocks/blob/main/CHANGELOG.md

## World Info Locks
- https://github.com/aikohanasaki/SillyTavern-WorldInfoLocks
- https://github.com/aikohanasaki/SillyTavern-WorldInfoLocks/blob/master/README.md
- https://github.com/aikohanasaki/SillyTavern-WorldInfoLocks/blob/master/CHANGELOG.md

## Lorebook Ordering
- https://github.com/aikohanasaki/SillyTavern-LorebookOrdering
- https://github.com/aikohanasaki/SillyTavern-LorebookOrdering/blob/main/CHANGELOG.md

## zTracker
- https://github.com/Zaakh/SillyTavern-zTracker
- https://github.com/Zaakh/SillyTavern-zTracker/blob/main/readme.md
- https://github.com/Zaakh/SillyTavern-zTracker/blob/main/CHANGELOG.md

## World Info Recommender
- https://github.com/bmen25124/SillyTavern-WorldInfo-Recommender
- https://github.com/bmen25124/SillyTavern-WorldInfo-Recommender/blob/main/readme.md
- https://github.com/bmen25124/SillyTavern-WorldInfo-Recommender/blob/main/src/components/SuggestedEntry.tsx
- https://github.com/bmen25124/SillyTavern-WorldInfo-Recommender/blob/main/src/components/MainPopup.tsx
- https://github.com/bmen25124/SillyTavern-WorldInfo-Recommender/blob/main/src/generate.ts

## Guided Generations
- https://github.com/Samueras/GuidedGenerations-Extension
- https://github.com/Samueras/GuidedGenerations-Extension/blob/main/README.md

## Stepped Thinking
- https://github.com/cierru/st-stepped-thinking
- https://github.com/cierru/st-stepped-thinking/blob/master/README.md

## Story Mode
- https://github.com/Prompt-And-Circumstance/StoryMode
- https://github.com/Prompt-And-Circumstance/StoryMode/blob/main/README.md
- https://github.com/Prompt-And-Circumstance/StoryMode/blob/main/CHANGELOG.md

## Custom Scenario
- https://github.com/bmen25124/SillyTavern-Custom-Scenario
- https://github.com/bmen25124/SillyTavern-Custom-Scenario/blob/main/readme.md

## Timelines
- https://github.com/SillyTavern/SillyTavern-Timelines
- https://github.com/SillyTavern/SillyTavern-Timelines/blob/master/README.md

## Chat Top Info Bar
- https://github.com/SillyTavern/Extension-TopInfoBar
- https://github.com/SillyTavern/Extension-TopInfoBar/blob/main/README.md

---

# 18. Próximo paso recomendado

1. **No ejecutar todavía cambios de roadmap.**
2. RP Architect revisa este documento.
3. Architect acepta/rechaza cada cambio propuesto.
4. Se actualiza el roadmap canónico.
5. Sólo entonces se emite el **Prompt 1/5** definitivo.

La investigación debe permanecer separada de la decisión canónica para que:
- podamos revisar fuentes más adelante;
- un cambio upstream no reescriba silenciosamente la historia de por qué se tomó una decisión;
- Architect conserve ownership semántico del roadmap.
