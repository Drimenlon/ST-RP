# Schema de especificación READY de RP

RP Architect suministra este contrato mínimo antes de que Luna cambie SillyTavern. Usar `NOT APPLICABLE` únicamente cuando la especificación explique por qué; no dejar decisiones requeridas de forma implícita.

```yaml
status: READY
rp_id: <id único y estable>
rp_name: <nombre>

# La identidad técnica no se infiere del nombre visible. Cada artefacto fuente
# debe tener una identidad estable explícita o usar la convención determinista
# <rp_id>:<kind>:<ruta-canónica-relativa-del-paquete> cuando el runbook lo permita.
resources:
  character_ids: <source-file -> stable resource id, o convención determinista>
  group_id: <stable resource id, o convención determinista>
  lorebook_id: <stable resource id, o convención determinista>
  lorebook_entry_ids: <source entry id -> stable resource id, o convención determinista>

characters:
  - identity: <ficha/nombre exacto y cómo identificarlo>
    source: <ficha/fuente proporcionada>
    required_fields: <campos explícitos y valores/contenido previstos>
    greeting: <texto exacto, o NOT APPLICABLE>

preset:
  api_family: <familia exacta del preset manager/API de SillyTavern>
  identity: <nombre exacto del preset destino>
  binding: <personaje/grupo exacto cuyo nombre/selector debe usarlo>
  base_preset: <preset base existente exacto; nunca “currently selected”>
  narrative_sources: <sources ordenados -> identificadores/roles exactos de prompt>
  managed_prompt_fields: <contenido/orden exacto de los campos propiedad del RP>
  preserve_from_base: <provider/model/generation fields que deben preservarse>

lorebooks_world_info:
  books: <libros exactos propiedad del RP, o none>
  entries: <contenido suministrado y campos requeridos, o none>
  bindings_activation_order: <requisitos explícitos, o none>
  global_requirements: <valores globales que deben existir/preservarse, o none>
  authorized_global_changes: <cambios globales exactos autorizados + alcance, o none>

memory:
  provider: <provider, o none>
  configuration: <valores explícitos, solo si el provider está LUNA_READY>

group:
  participants: <identidades exactas de personajes, o none>
  presence_rules: <reglas explícitas suministradas, o none>
  opening_source: <source exacto del opening, o NOT APPLICABLE>
  managed_settings: <solo settings de grupo explícitamente suministrados; el resto se preserva>

extensions:
  settings: <solo ajustes explícitamente propiedad del RP; indicar capability y valores>

preserve:
  - datos de RP, personajes, chats, presets, lorebooks y ajustes de extensiones no relacionados
  - core de SillyTavern
  - implementación de Gallery Images y sus datos/comportamiento

verify:
  - <comprobaciones objetivas posteriores al cambio y resultados esperados>

stop_if:
  - <ambigüedad o discrepancia específica de la especificación>
```

## Comprobaciones de interpretación requeridas

- Un personaje o chat nuevo **no** implica un prompt limpio. Verificar que está vinculado el preset exacto previsto; no asumir que el preset seleccionado actualmente pertenece a este RP. Comprobar si existen instrucciones de otros RP antes de cualquier generación o smoke test. Si la identidad/binding del preset o el ownership del prompt no están claros, STOP.
- El contenido y los bindings de lorebook deben suministrarse o referenciarse explícitamente mediante identidad estable. No inventar entradas, reglas de activación ni orden.
- Las fichas, grupos, presets, lorebooks y entradas existentes solo se actualizan cuando su identidad estable/ownership coincide con el RP. Si existe un target con el mismo nombre visible sin esa prueba de ownership, STOP; no sobrescribirlo ni crear un duplicado bajo una identidad adivinada.
- Para recursos cuyo formato permita marcadores de ownership, usar el namespace definido por el runbook. Un display name coincidente no sustituye ese marcador.
- Los presets Chat Completion de SillyTavern pueden auto-seleccionarse mediante el nombre visible exacto del personaje/grupo. El paquete debe indicar familia API, preset base exacto, identidad destino y mapping de prompts gestionados; Luna no debe elegir la base por preferencia ni copiar lo que esté activo en ese momento.
- World Info contiene settings por entrada y settings globales. La especificación debe distinguirlos. Preservar los globales por defecto. Solo puede cambiarse un global cuando la READY spec autorice explícitamente el valor y el impacto cross-chat, y exista un procedimiento técnico validado para efectuar la escritura; en otro caso, STOP.
- Si un global requerido ya tiene el valor correcto, verificarlo y no reescribirlo innecesariamente.
- Configurar memoria solo cuando ese provider/workflow exacto tenga `LUNA_READY = YES`. No inferir reglas de coexistencia o sustitución entre sistemas de memoria.
- Los participantes del grupo y cualquier comportamiento de Presence deben ser explícitos. No inferir compatibilidad de Presence ni aislamiento de memoria grupal.
- El opening grupal debe proceder de una fuente exacta cuando el paquete lo gestione. No sustituirlo por `first_mes`, generación del provider ni una paráfrasis. Actualizar un opening existente solo cuando el chat/mensaje gestionado esté positivamente identificado como owned por el RP.
- Los cambios de extensiones solo están permitidos cuando la especificación nombre la extensión, el ajuste exacto bajo ownership del RP, el valor deseado y la validación. Nunca cambiar configuración global/no relacionada por suposición.
- Gallery Images y el core de SillyTavern permanecen protegidos incluso si el RP solicita comportamiento adyacente; escalar para una autorización separada.

## Pregunta de readiness

Antes de actuar, Luna debe poder responder: **«¿Puedo implementar esto literalmente sin decidir qué quiso decir el autor?»** Si no puede, o si queda sin resolver algún binding/valor requerido, la especificación no está READY: STOP y devolverla para aclaración.
