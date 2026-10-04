# Lafiel & Almion — Story

```yaml
rp_architect_status: READY
technical_execution_status: READY_FOR_LUNA
rp_id: lafiel-almion-story
rp_name: Lafiel & Almion — Story
runtime_model: single_character_story_engine
story_card_name: Lafiel & Almion — Story
user_role: almion
narrator_identity: Narrador
preset_api_family: openai
preset_base: Default
preset_name: Lafiel & Almion — Story
lorebook_name: Lafiel-Almion-Story — World
```

## Propósito

Variante de runtime de Lafiel y Almion orientada a una historia larga de viaje, encuentros cambiantes y NPC episódicos.

El paquete grupal existente `../Lafiel-Almion/` se conserva como una arquitectura independiente y no debe modificarse, migrarse ni reemplazarse al materializar este paquete.

Esta variante usa una sola Character Card como motor narrativo. Lafiel y Almion no son miembros de un Group Chat: sus definiciones persistentes viven en World Info y el motor narrativo interpreta la escena completa.

## Modelo de runtime

- `{{user}}` representa a **Almion** en los mensajes normales del usuario.
- La IA puede narrar el mundo e interpretar a **Lafiel**, **Almion** y cualquier NPC presente.
- La IA puede continuar palabras, acciones, reacciones y pensamientos de Almion cuando resulte natural.
- Cualquier palabra, acción, pensamiento, intención o decisión de Almion establecida explícitamente por `{{user}}` prevalece sobre lo generado por la IA.
- Los mensajes del historial atribuidos explícitamente a **`Narrador`** —introducidos por el usuario mediante `/sendas`— son dirección narrativa autoritativa.
- El Narrador puede establecer hechos del mundo, tiempo, entorno, acontecimientos, NPC, diálogo, consecuencias y correcciones de continuidad.
- La IA no debe tratar a `Narrador` como una persona físicamente presente dentro de la ficción salvo que el propio Narrador lo establezca.

Orden de precedencia:

1. hechos/correcciones explícitos de `Narrador`;
2. contenido explícito de `{{user}}` como Almion respecto a Almion;
3. continuidad establecida del historial;
4. definiciones persistentes de World Info;
5. improvisación de la IA para completar lo no fijado.

## Diseño de personajes

- `LAFIEL.md` y `ALMION.md` son fuentes semánticas de personaje.
- No se materializan como Character Cards en esta variante.
- `WORLD_INFO.md` contiene sus representaciones ejecutables como entradas `CONSTANT`.
- La única Character Card requerida por este paquete es `Lafiel & Almion — Story`, definida en `STORY_CARD.md`.

## NPC episódicos

La historia debe soportar personajes que aparecen durante un arco corto o una sola escena: posaderos, trabajadores, viajeros, guardias, sirvientes, comerciantes, autoridades locales, habitantes de pueblos, nobles menores y otros adultos plausibles.

Un NPC incidental no necesita Character Card ni entrada propia de World Info. La IA puede crearlo e interpretarlo directamente dentro de la escena.

Un NPC puede recibir posteriormente una entrada SELECTIVE de World Info si se vuelve recurrente o necesita identidad persistente. No debe obtener importancia excepcional, conocimiento imposible, poder especial ni conexión predestinada con los protagonistas por el mero hecho de aparecer.

Rhevan no es un punto de presión obligatorio en esta variante. Si aparece en el futuro, será un NPC como cualquier otro salvo que una especificación posterior le otorgue persistencia.

Dalkon no debe aparecer hasta que RP Architect lo introduzca explícitamente en una versión posterior.

## Estructura del viaje

Lafiel y Almion viajan por propiedades, carreteras, aldeas, pueblos, ciudades pequeñas, posadas, residencias y otros entornos coherentes con el mundo mientras investigan la maldición y se exponen a situaciones que ponen a prueba su relación y su autocontrol.

Las tentaciones y dinámicas de inversión de clase no dependen de un único hombre fijo. Pueden surgir de personas adultas distintas en lugares distintos, con personalidades, profesiones, capacidades y actitudes propias.

No convertir cada encuentro en una tentación automática. El mundo debe sentirse habitado y causal; algunas personas serán irrelevantes, otras útiles, molestas, atractivas, peligrosas, memorables o recurrentes según lo que ocurra.

## Paquete autoritativo

Leer en este orden:

1. `README.md`
2. `WORLD.md`
3. `PLAYER.md`
4. `NARRATIVE_RULES.md`
5. `LAFIEL.md`
6. `ALMION.md`
7. `STORY_CARD.md`
8. `WORLD_INFO.md`
9. `PRESET_PROMPTS.md`
10. `OPENING.md`

## Mapping hacia SillyTavern

- `STORY_CARD.md` → única Character Card `Lafiel & Almion — Story`.
- `LAFIEL.md` → fuente semántica para la entrada CONSTANT `Personaje — Lafiel` de World Info.
- `ALMION.md` → fuente semántica para la entrada CONSTANT `Personaje — Almion` de World Info.
- `WORLD.md` → referencia semántica del canon del mundo.
- `WORLD_INFO.md` → Chat Lorebook `Lafiel-Almion-Story — World`, vinculado únicamente al chat de esta variante.
- `NARRATIVE_RULES.md` + `PLAYER.md` → fuentes semánticas del comportamiento del motor narrativo.
- `PRESET_PROMPTS.md` → texto exacto de `Main Prompt`, `Auxiliary Prompt` y `Post-History Instructions` del preset `Lafiel & Almion — Story`.
- `OPENING.md` → First Message exacto de la Story Card.

No crear Group Chat para este paquete.

## World Info

Las entradas de mundo mantienen el canon del paquete original y añaden dos entradas CONSTANT de protagonistas:

- `Personaje — Lafiel`
- `Personaje — Almion`

El lorebook no debe añadirse a `Active World(s) for all chats`.

Los valores globales requeridos siguen siendo:

```yaml
max_recursion_steps: 1
alert_on_overflow: true
```

No modificar ningún otro ajuste global de World Info.

## Preset

```yaml
preset_api_family: openai
preset_base: Default
preset_name: Lafiel & Almion — Story
```

`Default` es solo la base y debe permanecer sin cambios.

El preset específico de esta variante contiene reglas para:

- `{{user}} = Almion`;
- Narrador mediante mensajes atribuidos a `Narrador`;
- una sola IA que interpreta escena completa;
- separación de conocimientos y voces;
- NPC episódicos improvisados;
- progresión psicológica lenta;
- viaje con múltiples fuentes posibles de tentación;
- continuidad del amor y la alianza entre Lafiel y Almion.

## Persona del usuario

Este paquete no modifica `Persona Description`, porque sigue siendo una superficie controlada por el usuario.

Para una interfaz coherente se recomienda usar una Persona cuyo nombre visible sea `Almion`, pero la semántica del runtime no depende de ello: el preset establece explícitamente que `{{user}}` representa a Almion.

## Preservar

Durante la materialización:

- no modificar `../Lafiel-Almion/` ni sus recursos ya materializados;
- no modificar el Group Chat `Lafiel & Almion` existente;
- no modificar sus cards `Lafiel` y `Almion` existentes;
- no modificar su preset `Lafiel & Almion`;
- no modificar su lorebook `Lafiel-Almion — World`;
- no modificar chats existentes;
- no modificar `Default`;
- no modificar otros RP, lorebooks, presets, extensiones ni el core de SillyTavern.

## Verificación mínima

Tras la materialización verificar:

- existe exactamente una nueva Story Card `Lafiel & Almion — Story` bajo ownership de este paquete;
- la variante usa un chat individual, no un Group Chat;
- el First Message coincide con `OPENING.md`;
- existe el preset `Lafiel & Almion — Story`, derivado de `Default` sin modificar `Default`;
- los tres campos gestionados coinciden exactamente con `PRESET_PROMPTS.md`;
- existe `Lafiel-Almion-Story — World` y no está activo globalmente;
- el lorebook está vinculado únicamente al chat de esta variante;
- las entradas CONSTANT de Lafiel y Almion están siempre disponibles;
- los NPC incidentales pueden aparecer y hablar sin card propia;
- los mensajes normales del usuario se interpretan como Almion;
- los mensajes atribuidos a `Narrador` se interpretan como dirección narrativa;
- la IA puede continuar a Almion sin contradecir lo establecido explícitamente por el usuario;
- el paquete grupal anterior permanece byte-for-byte fuera del alcance de esta materialización;
- no se realizan llamadas al provider durante la materialización/verificación técnica.
