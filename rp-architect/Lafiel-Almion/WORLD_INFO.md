# ESPECIFICACIÓN DE WORLD INFO — Lafiel & Almion

Este archivo define el contenido exacto deseado de World Info/Lorebook para el piloto.

`WORLD.md` sigue siendo la referencia en prosa del canon. Este archivo es la descomposición orientada a implementación que debe consumir Luna.

## Identidad del lorebook

Nombre:

`Lafiel-Almion — World`

Ámbito deseado:

`Chat Lorebook` para el chat grupal `Lafiel & Almion`.

No añadir este lorebook globalmente.

No vincularlo a personajes o chats no relacionados.

Si los runbooks actuales de Luna no autorizan la creación/vinculación de esta configuración exacta de World Info, STOP y devolver únicamente esa capability ausente a Infrastructure/Sol.

## Configuración de activación

### Cambios globales de World Info autorizados

Este paquete autoriza explícitamente a Luna a cambiar exactamente dos ajustes **globales** de World Info de SillyTavern como parte de la materialización de este RP:

- `Max Recursion Steps = 1`
- `Alert on overflow = ON`

Esta autorización es deliberada y global. Luna no debe tratar los valores actuales del runtime (`0` / `OFF`) como un bloqueo. Si difieren, Luna está autorizada a cambiarlos a los valores anteriores.

Estos dos valores pasan a ser la baseline global deseada de World Info tras la materialización; no revertirlos al terminar la tarea.

Este paquete no controla ni autoriza el cambio de ningún otro ajuste global de World Info. Preservar los valores existentes del runtime para todos los demás ajustes globales, incluidos:

- Include Names;
- Case-sensitive keys;
- Match whole words;
- Context/Budget global;
- Min Activations;
- cualquier otra opción global de World Info no enumerada explícitamente arriba.

Luna debe verificar los dos cambios autorizados después de aplicarlos y debe hacer STOP en lugar de alterar cualquier otro ajuste global de World Info para hacer funcionar este RP.

### Valores por defecto de las entradas

Salvo que una entrada indique lo contrario:

- Enabled: `YES`
- Position: `Before Char Defs`
- Trigger %: `100`
- Non-recursable: `YES`
- Delay until recursion: `NO`
- Prevent further recursion: `NO`
- Ignore budget: `NO`
- Inclusion Group: `NONE`
- Character filter: `NONE` (el ámbito ya está restringido por el binding del Chat Lorebook)
- Additional Matching Sources: todos `OFF`

Las entradas SELECTIVE usan claves bilingües español + inglés. El español es el idioma principal del RP; las claves inglesas se conservan como compatibilidad adicional. No traducir semánticamente las claves en runtime: SillyTavern debe hacer matching literal según su configuración global existente.

---

## ENTRADA 001 — Sistema estamental

Título / Memo:

`Mundo — Sistema estamental hereditario`

Estrategia:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`100`

Contenido:

```text
Esta sociedad está organizada en estamentos hereditarios rígidos: Corona/familia real, nobleza, clero y clases bajas, incluidos los sirvientes. La movilidad social es extraordinariamente rara. Una persona nacida sirviente normalmente permanece en la clase baja durante toda su vida; una persona nacida noble normalmente sigue siendo noble de por vida. La mayoría de los habitantes trata la jerarquía como la estructura normal de la civilización, no como una injusticia temporal a la espera de una revolución. La comodidad material de las clases bajas no implica igualdad social y las inversiones sexuales privadas no anulan el rango formal.
```

---

## ENTRADA 002 — Prosperidad y tecnología moderna

Título / Memo:

`Mundo — Prosperidad moderna`

Estrategia:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`110`

Contenido:

```text
El mundo es tecnológicamente moderno y extremadamente próspero a pesar de su jerarquía hereditaria. Existen electricidad, internet, smartphones, transporte moderno, electrodomésticos, automatización, medicina excelente, servicios públicos sólidos, seguridad de vivienda y una renta básica universal. Las enfermedades graves son raras e incluso los sirvientes disfrutan por lo general de un nivel de vida material alto. La desigualdad económica y de estatus sigue siendo grande: los hogares nobiliarios, propiedades y autoridad política pueden superar ampliamente a los de las personas de clase baja.
```

---

## ENTRADA 003 — Escala y estética de los asentamientos

Título / Memo:

`Mundo — Patrón de asentamientos`

Estrategia:

`SELECTIVE` / Green Circle

Primary Keys:

`city, cities, town, towns, village, villages, capital, settlement, settlements, estate, estates, palace, travel, road, district, ciudad, ciudades, pueblo, pueblos, aldea, aldeas, asentamiento, asentamientos, residencia, residencias, palacio, palacios, viaje, viajar, camino, caminos, carretera, carreteras, distrito, distritos`

Optional Filter:

`NONE`

Order:

`120`

Contenido:

```text
Los asentamientos conservan un carácter espacial y visual semejante al medieval mientras incorporan tecnología moderna. El escenario favorece aldeas, pueblos, propiedades nobiliarias, palacios y ciudades pequeñas o medianas en lugar de megaciudades modernas gigantes. Los asentamientos pueden ser algo mayores que sus equivalentes medievales históricos, pero el paisaje social debe seguir sintiéndose descentralizado, centrado en propiedades y a escala humana.
```

---

## ENTRADA 004 — Nobleza moderna

Título / Memo:

`Mundo — Nobleza moderna`

Estrategia:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`130`

Contenido:

```text
Los nobles antiguos eran más marciales, agresivos y guerreros. A lo largo de las generaciones, la maldición hereditaria coincidió con la transformación de los estamentos superiores en una casta dirigente más intelectual y administrativa. Los nobles modernos suelen ser muy educados, sofisticados, estratégicamente capaces, hábiles con las palabras y administradores competentes. Siguen siendo orgullosos, conscientes de su clase, jerárquicos y a menudo arrogantes. La maldición no los volvió igualitarios; su competencia y su clasismo coexisten.
```

---

## ENTRADA 005 — Maldición: hechos públicos y origen desconocido

Título / Memo:

`Maldición — Conocimiento público esencial`

Estrategia:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`200`

Contenido:

```text
El fenómeno hereditario llamado la maldición y sus efectos sexuales/psicológicos generales son de conocimiento público. Su verdadero creador, mecanismo y propósito son desconocidos. Las teorías dentro del mundo pueden invocar a un dios, demonio, ángel, experimento, castigo, bendición, diversión o motivo incomprensible, pero ninguna está confirmada como canon. La maldición no borra el libre albedrío ni la personalidad. Crea fuertes predisposiciones hereditarias que interactúan con el orgullo, amor, celos, ambición, criterio y autocontrol ya existentes.
```

---

## ENTRADA 006 — Maldición: hombres nobles

Título / Memo:

`Maldición — Hombres nobles`

Estrategia:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`210`

Contenido:

```text
Los hombres de clase alta poseen una fuerte predisposición hereditaria hacia el cuckolding, la humillación y la subordinación erótica con hombres de clase baja, a menudo incluidos sus propios sirvientes. Pueden desear o disfrutar genuinamente de estas dinámicas mientras siguen siendo aristócratas orgullosos que consideran conscientemente inferior al hombre de clase baja. Los celos, la ira, la vergüenza, la excitación y el apego pueden coexistir. La protesta o amenaza de un noble puede funcionar a veces como teatro para salvar las apariencias, pero también existen límites genuinos y no deben darse por inexistentes.
```

---

## ENTRADA 007 — Maldición: mujeres nobles

Título / Memo:

`Maldición — Mujeres nobles`

Estrategia:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`220`

Contenido:

```text
Las mujeres de clase alta poseen una fuerte atracción sexual hereditaria hacia hombres de clase baja, especialmente hacia cualidades que perciben como rudas, físicamente imponentes, poco refinadas o socialmente inferiores. También tienen una marcada predisposición hacia la sumisión sexual ante hombres de clase baja y hacia la humillación de hombres de su propia clase dentro de dinámicas de cuckolding. Estas predisposiciones no crean confianza, amor, obediencia ni rendición total de forma instantánea. Una mujer noble disciplinada puede resistir, retirarse, negociar, racionalizar, enfadarse o preservar su autoridad pública mientras sigue sintiendo intensamente la atracción.
```

---

## ENTRADA 008 — Jerarquía pública e inversión privada

Título / Memo:

`Sociedad — Jerarquía pública / Inversión privada`

Estrategia:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`230`

Contenido:

```text
La jerarquía formal sigue siendo plenamente real incluso cuando la maldición produce inversiones privadas de dignidad o poder erótico. Un sirviente puede recibir órdenes, ser disciplinado, despedido o castigado por un noble y participar más tarde en una situación privada donde ese mismo noble busque humillación o subordinación. La sociedad no interpreta esta contradicción como abolición del sistema estamental. La etiqueta, las apariencias y la conducta para salvar la imagen importan. El cuckolding es humillante, no un símbolo de estatus nobiliario.
```

---

## ENTRADA 009 — Límites, castigo y habilidad de los sirvientes

Título / Memo:

`Sociedad — Límites y consecuencias para sirvientes`

Estrategia:

`SELECTIVE` / Green Circle

Primary Keys:

`punish, punishment, discipline, disciplined, dismiss, dismissed, expel, expelled, execution, kill, killed, boundary, boundaries, threat, threaten, servant, servants, castigar, castigo, castigos, castigado, castigada, disciplina, disciplinar, disciplinado, disciplinada, despedir, despedido, despedida, expulsar, expulsado, expulsada, ejecución, ejecucion, ejecutar, matar, muerto, muerta, límite, limites, límites, amenaza, amenazas, amenazar, sirviente, sirvientes, criado, criada, criados, criadas`

Optional Filter:

`NONE`

Order:

`240`

Contenido:

```text
Los hombres de clase baja no están protegidos automáticamente por la maldición. La habilidad importa. Un sirviente que distingue correctamente entre una pérdida de dignidad deseada y odio genuino o confianza rota puede adquirir una influencia privada inusual, pero un sirviente que presiona de forma burda, viola límites reales, traiciona la confianza o confunde excitación con inmunidad puede ser despedido, castigado o incluso asesinado. Las instituciones coercitivas formales siguen existiendo, aunque se utilizan con relativa poca frecuencia en esta sociedad que lleva mucho tiempo en paz.
```

---

## ENTRADA 010 — Corona y sucesión

Título / Memo:

`Corona — Sucesión y Lafiel`

Estrategia:

`SELECTIVE` / Green Circle

Primary Keys:

`Lafiel, Crown, crown, throne, succession, heir, princess, queen, king, royal, royalty, Corona, corona, trono, sucesión, sucesion, heredero, heredera, princesa, reina, rey, realeza`

Optional Filter:

`NONE`

Order:

`250`

Contenido:

```text
La Corona sigue siendo la cúspide del orden hereditario. Lafiel es una princesa real adulta y una de varios hermanos/candidatos que compiten por la sucesión. Se encuentra entre las candidatas más fuertes a pesar de ser una de las más jóvenes. Su ambición es convertirse en reina y gobernar excepcionalmente bien; no busca democratización ni una reducción de la autoridad real. Almion pertenece a la altísima nobleza, pero permanece formalmente por debajo de la Corona y acepta esa precedencia como normal.
```

Nota:

El número y distribución exactos de los hermanos de Lafiel NO se definen intencionadamente aquí porque RP Architect todavía no ha cerrado ese detalle del canon.

---

## ENTRADA 011 — Investigación de la maldición

Título / Memo:

`Maldición — Estado de la investigación`

Estrategia:

`SELECTIVE` / Green Circle

Primary Keys:

`curse, curses, cure, cured, origin, creator, entity, demon, angel, god, research, investigate, investigation, experiment, theory, theories, maldición, maldicion, maldiciones, cura, curar, curado, curada, origen, creador, creadora, entidad, demonio, ángel, angel, dios, diosa, investigación, investigacion, investigaciones, investigar, experimento, experimentos, teoría, teoria, teorías, teorias`

Optional Filter:

`NONE`

Order:

`260`

Contenido:

```text
Lafiel y Almion siguen en la fase de observación e investigación. No poseen una explicación definitiva sobre el origen, creador, mecanismo o propósito de la maldición ni una cura demostrada. Pueden formular hipótesis, comparar casos y realizar observaciones controladas, pero la narración no debe elevar una teoría no confirmada a verdad objetiva. Su objetivo compartido a largo plazo es restaurar la autonomía aristocrática frente a la maldición manteniendo al mismo tiempo el gobierno aristocrático.
```

---

## Requisitos de determinismo

Para este piloto:

- No usar activación Vectorized/embeddings.
- No usar probabilidad inferior al 100%.
- No usar inclusion groups.
- No usar timed effects.
- No usar automation IDs.
- No usar posiciones de Author's Note.
- No introducir cadenas recursivas de lore más allá de la profundidad global de recursión `1` explícitamente autorizada.

El objetivo es una activación predecible e inspeccionable durante la primera prueba del RP.

## Verificación

Cuando la implementación esté autorizada, verificar con WorldInfo Info + Prompt Inspector:

1. `Max Recursion Steps` global es exactamente `1`.
2. `Alert on overflow` global está `ON`.
3. Este paquete no cambió ningún otro ajuste global de World Info.
4. Las entradas 001, 002, 004, 005, 006, 007 y 008 están activas en cada generación del chat grupal vinculado.
5. La entrada 003 está inactiva sin claves de asentamiento/localización y se activa cuando aparece una de sus claves españolas o inglesas.
6. La entrada 009 está inactiva sin claves relacionadas con límites/disciplina/sirvientes y se activa con una clave coincidente española o inglesa.
7. La entrada 010 se activa cuando entra en el contexto escaneado terminología de Lafiel/Corona/sucesión en español o inglés.
8. La entrada 011 se activa cuando entra en el contexto escaneado terminología de maldición/investigación en español o inglés.
9. Ninguna entrada de este lorebook se activa en chats no relacionados.
10. No aparece contenido de lorebooks no relacionados a causa de este paquete.
