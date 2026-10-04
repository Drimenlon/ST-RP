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

## Mappings de materialización — SillyTavern 1.19.0

Los siguientes mappings fueron validados contra el source local de SillyTavern 1.19.0 en los módulos de personajes, grupos, chat, World Info y preset manager. La inspección fue de solo lectura; no se modificaron el core ni las extensiones.

### Character Cards

- **LUNA_READY = YES** para el workflow de campos gestionados descrito aquí.
- Mapear Card V2 así: `Name` → `data.name` (SillyTavern también mantiene `name` a nivel superior); `Description` → `data.description`; `Personality` → `data.personality`; `Scenario` → `data.scenario`; `Example Dialogue` → `data.mes_example`; `Greeting / First Message` suministrado → `data.first_mes`. `NOT APPLICABLE` significa no autorizar un greeting.
- No mapear otra prosa hacia `system_prompt` ni campos no relacionados.
- La identidad estable es un `resource_id` explícito o, si no se suministra, la convención determinista `<rp_id>:character:<ruta-canónica-relativa-del-paquete>`.
- Guardar identidad/ownership bajo `data.extensions.rp_infrastructure`, incluyendo al menos `rp_id` y source path cuando el formato lo soporte.
- Usar un filename/avatar interno determinista derivado de esa identidad; el nombre visible de la ficha permanece exactamente como lo define el paquete.
- Antes de crear, comprobar identidad objetivo y colisiones de nombre visible.
- Resolver futuras membresías de grupo por el avatar/filename devuelto, nunca mediante búsqueda ambigua por nombre.
- Actualizar solo cuando el marcador de ownership coincida. Leer el objeto Card V2 completo, fusionar únicamente los campos gestionados y preservar imagen, chats, tags, creator fields, extensiones y demás datos no gestionados.
- Una ficha del mismo nombre sin marcador esperado, un filename objetivo sin ownership esperado, marcadores duplicados o una colisión ambigua son STOP.
- Verificar campos gestionados y preservación después de guardar.

### Grupo + opening

- **LUNA_READY = YES** para estructura de grupo e inicialización/actualización segura del opening.
- El contenido conductual adicional pertenece al mapping separado del preset; el metadata del grupo no debe recibir un `scenario` inventado si SillyTavern no lo soporta en esa superficie.
- Resolver cada miembro explícitamente nombrado a exactamente una ficha owned y almacenar su avatar filename en `members`.
- No inferir miembros desde menciones. Narrador, NPC secundarios o personajes futuros no son miembros salvo declaración explícita del paquete.
- SillyTavern genera el `id` del grupo. Guardar `<rp_id>:group:<ruta-canónica-del-source-de-grupo>` en un campo namespaced `rp_infrastructure` cuando el formato lo soporte.
- Actualizar solo el grupo cuyo marcador coincida y preservar todos los demás ajustes. Configurar únicamente settings gestionados/suministrados por el paquete; para el resto mantener los valores existentes/por defecto de SillyTavern.
- Grupo del mismo nombre sin marcador esperado o miembro no resoluble → STOP.
- Al crear un chat nuevo, sembrar el texto exacto de `OPENING.md` como primer mensaje narrador/usuario (`is_user: true`). El narrador sigue siendo el usuario, no un miembro del grupo.
- No usar `first_mes` de una ficha como sustituto del opening grupal, no reescribirlo y no llamar a Generate para crearlo.
- Guardar la identidad del recurso grupal en metadata del chat cuando el formato lo permita.
- Sustituir un opening existente solo si ownership del chat y mensaje gestionado están positivamente identificados. En otro caso, STOP.
- Verificar nombre exacto del grupo, lista de miembros por avatar, opening exacto, semántica del narrador y ausencia de settings añadidos sin autorización.

### World Info / Chat Lorebook

- **LUNA_READY = YES** para creación/actualización exacta de entradas y binding al chat mediante el workflow documentado.
- Usar el nombre exacto del lorebook del paquete y almacenar su identidad estable bajo `extensions.rp_infrastructure` a nivel raíz cuando el formato lo soporte.
- Vincular únicamente el chat objetivo mediante `chat_metadata.world_info`; no añadir el libro a la selección global de World Info salvo autorización explícita separada.
- Cada entrada fuente necesita identidad estable. Usar `source_entry_id` explícito o una identidad determinista derivada del `rp_id`, lorebook y ordinal/source estable. Guardarla bajo `entry.extensions.rp_infrastructure` cuando el formato lo soporte.
- El `uid` de SillyTavern es numérico: al crear, asignar un UID libre; en actualizaciones posteriores localizar por el marcador de ownership, no por título/comentario.
- Libro del mismo nombre sin ownership esperado, marcadores ausentes/duplicados en una actualización o colisión ambigua de entradas → STOP.
- Mapping de `WORLD_INFO.md` a campos de SillyTavern: título/memo → `comment`; contenido → `content`; `CONSTANT` → `constant=true`, `selective=false`, `key` vacío; `SELECTIVE` → `constant=false`, `selective=true`, primary keys → `key`; secondary keys suministradas → `keysecondary`; lógica suministrada → `selectiveLogic`; orden → `order`; `Before Char Defs` → `position=0`; enabled → `disable=false`; probabilidad → `probability` + `useProbability`; recursión → `excludeRecursion`, `preventRecursion`, `delayUntilRecursion`, `ignoreBudget`; matching sources → booleans explícitos `matchPersonaDescription`, `matchCharacterDescription`, `matchCharacterPersonality`, `matchCharacterDepthPrompt`, `matchScenario`, `matchCreatorNotes`.
- Mapear `caseSensitive` y `matchWholeWords` como overrides de entrada únicamente cuando el paquete los especifique a nivel de entrada.
- Dejar filtros opcionales ausentes/vacíos si el paquete no los suministra. No inventar keys, inclusion groups, vectors, recursion chains, timed effects ni automation.
- Una actualización segura debe leer el lorebook completo, modificar únicamente entradas owned con marcador coincidente, preservar todas las demás propiedades/entradas/campos no gestionados y guardar el objeto completo fusionado. `/api/worldinfo/edit` reemplaza el libro completo: nunca enviar un objeto parcial.
- Los ajustes `world_info_include_names`, `world_info_max_recursion_steps`, `world_info_overflow_alert`, `world_info_min_activations` y otros equivalentes de ese nivel son globales, no campos del Chat Lorebook.
- Por defecto, preservar todos los globales. Si una especificación READY autoriza explícitamente un cambio global concreto y existe un procedimiento técnico validado para esa escritura, puede aplicarse únicamente ese cambio y debe verificarse su impacto global. Si falta cualquiera de esas dos condiciones, STOP en lugar de cambiar el global.
- Para `Lafiel & Almion`, el paquete actual exige/preserva `Max Recursion Steps = 1` y `Alert on overflow = ON`; no introduce requisitos nuevos sobre otros globales. Si esos dos valores ya coinciden, no volver a escribirlos.
- Verificar entries/campos exactos y binding solo al chat. Usar WorldInfo Info tras reconstruir contexto para casos de activación; Prompt Inspector comprueba contexto pre-final, no el payload final del provider.

### Preset RP / prompts narrativos

- **LUNA_READY = YES** cuando el paquete READY proporciona explícitamente: familia API del preset, preset base exacto, nombre destino exacto, mapping ordenado de sources → campos de prompt y contenido exacto de los campos gestionados.
- SillyTavern puede auto-seleccionar un preset por el nombre visible exacto del personaje/grupo. El nombre destino puede por tanto coincidir con el nombre del grupo, pero ese selector no constituye por sí solo prueba de ownership.
- Derivar únicamente del preset base indicado por el paquete. Nunca usar como autoridad el preset actualmente seleccionado.
- Preservar provider, model, connection y generation fields que el paquete marque como no gestionados.
- Reemplazar únicamente el contenido de prompt explícitamente gestionado por el RP, usando el source text de forma literal.
- Si existe ya un preset con el nombre objetivo, actualizarlo solo cuando ownership/contenido previo pueda demostrarse de forma segura. De lo contrario, STOP; no crear un duplicado para esquivar la colisión.
- Verificar selección esperada en el grupo, read-back de los campos gestionados y Prompt Inspector para detectar contaminación de otro RP antes de cualquier generación autorizada.
- Para `Lafiel & Almion`, el paquete actual ya proporciona `preset_api_family: openai`, `preset_base: Default`, `preset_name: Lafiel & Almion` y el mapping exacto en `PRESET_PROMPTS.md`; esta precondición está cerrada.

## Sesión API local segura de SillyTavern

- **LUNA_READY = YES** para POST locales soportados contra SillyTavern 1.19.0 en `http://127.0.0.1:8000`, usando `C:\Users\Jonat\Documents\Codex\RP-Infrastructure\SillyTavernLocalApi.psm1`.
- Importar el helper y llamar a `Initialize-STLocalApiSession`; crea una `WebRequestSession` nueva, obtiene `/csrf-token` y mantiene cookie jar y token de forma privada en memoria del módulo.
- Para POST protegidos usar `Invoke-STLocalApi -Path '/api/<endpoint>' -Body <object>`.
- El helper restringe requests a paths locales `/api/` y no imprime ni persiste tokens/cookies.
- Llamar a `Reset-STLocalApiSession` al terminar.
- No extraer cookies del navegador, exponer/persistir el token CSRF, desactivar CSRF, enviar requests a otro host ni escribir directamente archivos runtime de SillyTavern.
- Los errores deben informar endpoint y status HTTP sin secretos de respuesta.
- **Validación registrada:** sesión nueva + adquisición CSRF PASS; cookie de sesión preservada; `POST /api/worldinfo/list` protegido devolvió HTTP 200; se creó un recurso World Info sintético temporal con nombre único, se observó en la lista, se eliminó y se confirmó ausente. No se usó ningún recurso RP de producción ni provider.

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
