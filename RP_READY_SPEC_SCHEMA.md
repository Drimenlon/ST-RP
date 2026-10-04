# Schema de especificación READY de RP

RP Architect suministra este contrato mínimo antes de que Luna cambie SillyTavern. Usar `NOT APPLICABLE` únicamente cuando la especificación explique por qué; no dejar decisiones requeridas de forma implícita.

```yaml
status: READY
rp_id: <id único y estable>
rp_name: <nombre>

characters:
  - identity: <ficha/nombre exacto y cómo identificarlo>
    source: <ficha/fuente proporcionada>
    required_fields: <campos explícitos y valores/contenido previstos>
    greeting: <texto exacto, o NOT APPLICABLE>

preset:
  identity: <nombre/id exacto del preset previsto>
  binding: <cómo debe usarlo este RP/chat>
  required_configuration: <ajustes explícitos, o none>

lorebooks_world_info:
  books: <libros exactos propiedad del RP, o none>
  entries: <contenido suministrado y campos requeridos, o none>
  bindings_activation_order: <requisitos explícitos, o none>

memory:
  provider: <provider, o none>
  configuration: <valores explícitos, solo si el provider está LUNA_READY>

group:
  participants: <identidades exactas de personajes, o none>
  presence_rules: <reglas explícitas suministradas, o none>

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
- Configurar memoria solo cuando ese provider/workflow exacto tenga `LUNA_READY = YES`. No inferir reglas de coexistencia o sustitución entre sistemas de memoria.
- Los participantes del grupo y cualquier comportamiento de Presence deben ser explícitos. No inferir compatibilidad de Presence ni aislamiento de memoria grupal.
- Los cambios de extensiones solo están permitidos cuando la especificación nombre la extensión, el ajuste exacto bajo ownership del RP, el valor deseado y la validación. Nunca cambiar configuración global/no relacionada por suposición.
- Gallery Images y el core de SillyTavern permanecen protegidos incluso si el RP solicita comportamiento adyacente; escalar para una autorización separada.

## Pregunta de readiness

Antes de actuar, Luna debe poder responder: **«¿Puedo implementar esto literalmente sin decidir qué quiso decir el autor?»** Si no puede, o si queda sin resolver algún binding/valor requerido, la especificación no está READY: STOP y devolverla para aclaración.
