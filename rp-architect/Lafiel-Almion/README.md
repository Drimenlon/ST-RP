# Lafiel & Almion

```yaml
rp_architect_status: READY
technical_execution_status: READY_FOR_LUNA
rp_id: lafiel-almion
rp_name: Lafiel & Almion
group_name: Lafiel & Almion
user_role: narrator_director
preset_api_family: openai
preset_base: Default
preset_name: Lafiel & Almion
```

## Propósito

Primer RP de producción/prueba centrado en Lafiel y Almion antes de la entrada de Dalkon.

La dinámica principal es cuckolding psicológico, humillación aristocrática, celos, tensión de clase, orgullo y deseo contradictorio. No es una trama revolucionaria ni un triángulo amoroso genérico.

## Idioma del RP

El idioma principal y autoritativo del RP es el **español**.

La narración, diálogos, fichas, lore persistente y prompts específicos del RP deben redactarse en español, salvo que el narrador solicite explícitamente otro idioma para un elemento concreto.

Los identificadores técnicos de SillyTavern, nombres de archivos, nombres propios y valores estructurales pueden conservar su forma literal cuando cambiarla rompería el mapping o la identidad técnica.

Las claves SELECTIVE de World Info son bilingües español + inglés para permitir activación robusta; el contenido que recibe el modelo está redactado en español.

## Cierre semántico

Este paquete está **cerrado semánticamente por RP Architect** para esta versión del piloto.

`rp_architect_status: READY` significa que Luna/Infrastructure no deben reabrir ni reinterpretar:

- personajes;
- relaciones;
- worldbuilding;
- rol del usuario;
- NPC de prueba;
- límites de conocimiento;
- narrativa/pacing;
- apertura;
- World Info deseado;
- intención del RP;
- idioma principal del RP.

Si durante la implementación aparece una carencia puramente técnica —por ejemplo un binding, mapping o capability no Luna-ready— debe reportarse como bloqueo técnico concreto. Eso no convierte este RP otra vez en `DRAFT`.

## Paquete autoritativo

Luna debe leer los archivos de este paquete en este orden:

1. `README.md` — manifest, mapping y gates de ejecución.
2. `WORLD.md` — canon persistente/prosa de referencia del mundo.
3. `WORLD_INFO.md` — especificación exacta de lorebook/World Info: entradas, claves, estrategia, posición, orden, contenido y los dos cambios globales explícitamente autorizados.
4. `NARRATIVE_RULES.md` — fuente semántica de reglas globales de narración, pacing y comportamiento.
5. `PRESET_PROMPTS.md` — mapping de implementación exacto de las reglas narrativas a Main Prompt, Auxiliary Prompt y Post-History Instructions.
6. `LAFIEL.md` — definición operativa de la ficha de Lafiel.
7. `ALMION.md` — definición operativa de la ficha de Almion.
8. `GROUP.md` — participantes, rol del narrador, NPC de prueba, escenario compartido y límites de conocimiento.
9. `OPENING.md` — apertura grupal exacta y handoff al narrador.

No inferir contenido desde otros archivos del repositorio salvo los contratos globales de infraestructura.

## Regla crítica del rol del usuario

`{{user}}` es el narrador/director.

`{{user}}` NO es Rhevan, NO es un sirviente y NO es un participante dentro del mundo por defecto.

Los mensajes del usuario pueden establecer narración, dirección de escena, avance temporal, hechos ambientales y diálogo/acciones atribuidos explícitamente a NPC secundarios.

Lafiel y Almion no deben dirigirse a `{{user}}` como una persona diegética salvo que el narrador introduzca explícitamente un personaje separado dentro del mundo.

El primer punto de presión masculino de clase baja es el NPC secundario `Rhevan`, definido en `GROUP.md`. Rhevan no es Dalkon.

## Mapping hacia SillyTavern

- `LAFIEL.md` → Character Card `Lafiel`.
- `ALMION.md` → Character Card `Almion`.
- `WORLD.md` → referencia semántica del canon; no volcar este archivo entero en una ficha.
- `WORLD_INFO.md` → Chat Lorebook deseado `Lafiel-Almion — World`, con descomposición exacta de entradas, semántica de activación y los únicos cambios globales de World Info autorizados.
- `NARRATIVE_RULES.md` → fuente semántica del comportamiento narrativo global del RP.
- `PRESET_PROMPTS.md` → contenido exacto del prompt específico del RP y campos objetivo dentro del preset `Lafiel & Almion`.
- `GROUP.md` → definición del Group Chat `Lafiel & Almion`, escenario compartido, semántica del narrador, NPC secundario y límites de conocimiento.
- `OPENING.md` → apertura inicial del grupo.

Si Luna carece de un runbook aprobado para alguna operación exacta de creación/binding descrita aquí, debe hacer STOP en esa capability técnica en lugar de inventar otra representación.

## Personajes requeridos

- Lafiel
- Almion

No crear una ficha de Dalkon para este piloto.

Rhevan es inicialmente un NPC secundario controlado por el narrador, no una ficha requerida ni miembro del grupo. No crear una ficha de Rhevan salvo que RP Architect cambie posteriormente esa decisión.

## Generación del grupo

Participantes deseados del grupo:

1. Lafiel
2. Almion

El narrador controla la progresión de la escena mediante los turnos del usuario.

No tratar todos los turnos del usuario como diálogo hablado. Leer literalmente la atribución:

- `Rhevan dice ...` → habló Rhevan.
- `Almion observa ...` → el narrador establece un hecho observable/de escena tal como está escrito.
- prosa descriptiva → narración, no acción de un personaje narrador.

## World Info

La fuente de implementación es `WORLD_INFO.md`, no categorías genéricas.

El lorebook deseado contiene entradas explícitas para:

- orden estamental hereditario;
- prosperidad/tecnología modernas;
- patrón de asentamientos;
- nobleza moderna;
- conocimiento público esencial de la maldición;
- efectos de la maldición sobre hombres nobles;
- efectos de la maldición sobre mujeres nobles;
- jerarquía pública frente a inversión privada;
- límites/consecuencias para sirvientes;
- Corona/sucesión/Lafiel;
- estado actual de la investigación de la maldición.

No fusionar estas entradas en una única entrada genérica de «mundo» salvo autorización explícita de RP Architect.

No inventar claves adicionales, activación aleatoria, vectores, timed effects, inclusion groups ni uso de Author's Note.

### Cambios globales de World Info explícitamente autorizados

El usuario/propietario del paquete autoriza explícitamente a Luna a cambiar exactamente estos dos ajustes **globales** de World Info de SillyTavern durante la materialización:

```yaml
max_recursion_steps: 1
alert_on_overflow: true
```

Valores legibles:

- `Max Recursion Steps = 1`
- `Alert on overflow = ON`

Son cambios deliberados de baseline global, no una emulación local del RP.

Si el runtime tiene actualmente `Max Recursion Steps = 0` y/o `Alert on overflow = OFF`, eso **NO es un bloqueo**. Luna está autorizada a cambiar esos ajustes exactos a `1` y `ON` respectivamente.

Después de aplicarlos:

- verificar ambos valores;
- dejarlos en `1` / `ON` después de la tarea;
- no revertirlos;
- no cambiar ningún otro ajuste global de World Info salvo que una instrucción separada del paquete lo autorice explícitamente.

Una discrepancia en cualquier *otro* ajuste global de World Info no debe «corregirse» por inferencia.

## Memoria

La prueba inicial del RP no depende de Memory Books.

Mientras Memory Books siga con `LUNA_READY = NO`, Luna no debe configurarlo para este paquete.

La coexistencia/sustitución con Summaryception está fuera del alcance de este paquete.

## Presence / aislamiento del grupo

Este paquete puede usar un chat grupal normal, pero no depende de comportamiento no validado entre Memory Books + Presence.

Los pensamientos privados de los personajes no deben convertirse en conocimiento compartido simplemente porque Lafiel y Almion estén en el mismo chat grupal.

## Preset / binding de configuración

Los datos de materialización del preset están explícitos y cerrados:

```yaml
preset_api_family: openai
preset_base: Default
preset_name: Lafiel & Almion
```

Interpretación:

- Familia API/preset: familia de preset OpenAI de SillyTavern.
- Preset base compartido exacto: `Default`.
- Luna debe crear un nuevo preset específico del RP llamado exactamente `Lafiel & Almion`, igual que el nombre del Group Chat.
- El nuevo preset debe crearse/copiarse desde el preset base `Default` según el runbook aprobado de materialización de presets.
- `Default` es únicamente fuente/base. NO modificar el preset compartido `Default` in-place.
- `NARRATIVE_RULES.md` es la fuente semántica del comportamiento narrativo global del RP.
- `PRESET_PROMPTS.md` es el mapping de implementación autoritativo y el texto exacto para el preset específico del RP.
- El texto de prompt específico del RP se escribe únicamente en:
  1. `Main Prompt`
  2. `Auxiliary Prompt`
  3. `Post-History Instructions`
- World Info, descripción/personalidad del personaje, escenario, ejemplos y chat history siguen siendo sus slots dinámicos normales y no deben recibir texto narrativo duplicado.
- `Persona Description` está controlado por el usuario y debe permanecer intacto.
- Vincular/usar el nuevo preset `Lafiel & Almion` para este RP/grupo según el runbook aprobado.
- No inferir provider o modelo a partir del nombre del preset. Connection profile/provider/model son aspectos separados del runtime.
- No sustituirlo por el preset actualmente seleccionado ni por ningún otro simplemente porque esté activo en runtime.

Con estos valores suministrados, el paquete está completo para la capa básica de materialización y puede volver a Luna.

`technical_execution_status: READY_FOR_LUNA`

Las precondiciones de runtime y gates `LUNA_READY` siguen aplicando. Una discrepancia de runtime es una condición técnica de STOP, no una reapertura semántica del RP.

## Preservar

Luna debe preservar:

- otros RP, fichas, grupos y chats;
- presets/configuraciones no pertenecientes a este RP;
- preset base compartido `Default`;
- lorebooks no relacionados;
- todos los ajustes globales de World Info excepto los dos explícitamente autorizados arriba;
- Summaryception, Presence y Recast salvo autorización explícita;
- implementación/configuración/datos de Gallery Images;
- core de SillyTavern;
- Author's Note, controlado por el usuario y fuera de alcance;
- Persona Description, controlado por el usuario y fuera de alcance de este paquete.

## Verificar durante/después de la implementación

Verificar al menos:

- existen exactamente las fichas previstas de Lafiel y Almion con los campos suministrados;
- el grupo `Lafiel & Almion` contiene únicamente los participantes requeridos;
- `{{user}}` está representado semánticamente como narrador/director, no como sirviente;
- la apertura coincide con `OPENING.md`;
- el idioma efectivo del RP es español;
- la familia del preset es `openai`;
- el preset base exacto usado para crear el preset del RP es `Default` y permanece sin cambios;
- existe el preset específico `Lafiel & Almion`;
- `Main Prompt`, `Auxiliary Prompt` y `Post-History Instructions` coinciden exactamente con `PRESET_PROMPTS.md`;
- los slots dinámicos de World Info/fichas/escenario/ejemplos/historial siguen dinámicos y no contienen prosa duplicada del RP;
- `Max Recursion Steps` global es exactamente `1`;
- `Alert on overflow` global está `ON`;
- ningún otro ajuste global de World Info cambió a causa de este paquete;
- la configuración/preset efectivo del RP no contiene prompts extraños ni instrucciones heredadas de otros RP;
- la identidad del lorebook es exactamente `Lafiel-Almion — World`;
- entradas/claves/estrategias/órdenes/contenido de World Info coinciden con `WORLD_INFO.md`;
- las claves SELECTIVE permiten activación con terminología española y conservan compatibilidad inglesa según `WORLD_INFO.md`;
- el comportamiento de activación de WorldInfo Info coincide con los casos de verificación de `WORLD_INFO.md`;
- Prompt Inspector muestra el contexto esperado de mundo/personajes/narrativa y ninguna instrucción de otro RP;
- Dalkon no es participante ni sustituye implícitamente a Rhevan;
- no se modifica ningún RP no relacionado.

## Reglas de STOP / escalado

Luna debe distinguir bloqueos semánticos y técnicos.

### Bloqueo semántico

Solo reportar bloqueo semántico si los archivos del paquete realmente omiten o contradicen significado narrativo que RP Architect deba decidir.

En ese caso:

`RP_ARCHITECT_BLOCKED`

e identificar la decisión semántica exacta ausente/contradictoria.

### Bloqueo técnico

Si el RP está semánticamente cerrado pero la implementación requiere una capability, binding o runbook que no esté autorizado actualmente:

`TECHNICAL_EXECUTION_BLOCKED`

e identificar la capability/binding exacta que Infrastructure/Sol debe cerrar.

No degradar `rp_architect_status: READY` por ese bloqueo técnico.

### Casos obligatorios de STOP

STOP si:

- alguna capability requerida no está `LUNA_READY` para la operación solicitada;
- cambiar `Max Recursion Steps` a `1` o `Alert on overflow` a `ON` exigiría una operación no documentada/insegura;
- sería necesario cambiar cualquier ajuste global adicional de World Info;
- necesita decidir cómo reinterpretar contenido semántico entre superficies;
- no puede crear/vincular la configuración exacta de World Info mediante un procedimiento autorizado;
- no puede crear el preset específico del RP desde `Default` sin modificar la base compartida;
- encuentra otro Lafiel/Almion y no está explícitamente autorizado a actualizarlo;
- detecta instrucciones de otro RP en contexto;
- necesitaría modificar el core de SillyTavern o una extensión protegida;
- falta algún archivo del manifest o existe una contradicción material.

En todos los casos, preservar toda la semántica de RP ya cerrada y reportar únicamente la capa no resuelta.
