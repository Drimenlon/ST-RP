# ESPECIFICACIÓN DE WORLD INFO — Lafiel & Almion — Story

Este archivo define el contenido exacto del lorebook de la variante single-card.

`WORLD.md`, `LAFIEL.md` y `ALMION.md` son las fuentes semánticas. Este archivo es la representación orientada a implementación.

## Identidad del lorebook

Nombre:

`Lafiel-Almion-Story — World`

Ámbito deseado:

`Chat Lorebook` vinculado únicamente al chat individual que use la Story Card `Lafiel & Almion — Story`.

No añadir este lorebook a `Active World(s) for all chats`.

No vincularlo a la arquitectura grupal `Lafiel & Almion` ni a chats/personajes no relacionados.

## Configuración global requerida

Los únicos valores globales de World Info requeridos por este paquete son:

- `Max Recursion Steps = 1`
- `Alert on overflow = ON`

Si ya tienen esos valores, preservarlos.

Si difieren, el paquete autoriza únicamente esos dos cambios. No modificar ningún otro ajuste global de World Info.

## Valores por defecto de entradas

Salvo que una entrada indique lo contrario:

- Enabled: `YES`
- Position: `Before Char Defs`
- Trigger %: `100`
- Non-recursable: `YES`
- Delay until recursion: `NO`
- Prevent further recursion: `NO`
- Ignore budget: `NO`
- Inclusion Group: `NONE`
- Character filter: `NONE`
- Additional Matching Sources: todos `OFF`

Las entradas SELECTIVE usan claves bilingües español + inglés cuando resulta útil.

---

## ENTRADA 001 — Sistema estamental

Título / Memo:

`Mundo — Sistema estamental hereditario`

Estrategia:

`CONSTANT`

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

`CONSTANT`

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

`SELECTIVE`

Primary Keys:

`city, cities, town, towns, village, villages, capital, settlement, settlements, estate, estates, palace, travel, road, inn, tavern, district, ciudad, ciudades, pueblo, pueblos, aldea, aldeas, asentamiento, asentamientos, residencia, residencias, palacio, palacios, viaje, viajar, camino, caminos, carretera, carreteras, posada, taberna, distrito, distritos`

Optional Filter:

`NONE`

Order:

`120`

Contenido:

```text
Los asentamientos conservan un carácter espacial y visual semejante al medieval mientras incorporan tecnología moderna. El escenario favorece aldeas, pueblos, propiedades nobiliarias, palacios y ciudades pequeñas o medianas en lugar de megaciudades modernas gigantes. Existen carreteras, posadas, estaciones, mercados, fincas y servicios modernos suficientes para viajar con comodidad relativa entre regiones. Los asentamientos pueden ser algo mayores que sus equivalentes medievales históricos, pero el paisaje social debe seguir sintiéndose descentralizado, centrado en propiedades y a escala humana.
```

---

## ENTRADA 004 — Nobleza moderna

Título / Memo:

`Mundo — Nobleza moderna`

Estrategia:

`CONSTANT`

Primary Keys:

`NONE`

Order:

`130`

Contenido:

```text
Los nobles antiguos eran más marciales, agresivos y guerreros. A lo largo de las generaciones, la maldición hereditaria coincidió con la transformación de los estamentos superiores en una casta dirigente más intelectual y administrativa. Los nobles modernos suelen ser muy educados, sofisticados, estratégicamente capaces, hábiles con las palabras y administradores competentes. Siguen siendo orgullosos, conscientes de su clase, jerárquicos y a menudo arrogantes. La maldición no los volvió igualitarios; su competencia y su clasismo coexisten. Tras generaciones conviviendo con la maldición, los nobles han desarrollado respuestas privadas muy distintas: algunos resisten activamente, otros se acomodan y otros hacen concesiones importantes mientras mantienen una vida pública competente. Son comunes las racionalizaciones sofisticadas —investigación, necesidad, excepción, costumbre privada, situación todavía bajo control— que pueden contener parte de verdad y al mismo tiempo ocultar el grado de indulgencia real. También es común criticar en otros conductas parecidas a las que uno mismo justifica en privado.
```

---

## ENTRADA 005 — Maldición: hechos públicos y origen desconocido

Título / Memo:

`Maldición — Conocimiento público esencial`

Estrategia:

`CONSTANT`

Primary Keys:

`NONE`

Order:

`200`

Contenido:

```text
El fenómeno hereditario llamado la maldición y sus efectos sexuales/psicológicos generales son de conocimiento público. Su verdadero creador, mecanismo y propósito son desconocidos. Las teorías dentro del mundo pueden invocar a un dios, demonio, ángel, experimento, castigo, bendición, diversión o motivo incomprensible, pero ninguna está confirmada como canon. La maldición no borra el libre albedrío ni la personalidad. Crea fuertes predisposiciones hereditarias que interactúan con el orgullo, amor, celos, ambición, criterio y autocontrol ya existentes. La resistencia puede ser real sin ser necesariamente permanente: experiencias acumuladas, deseos, presión y decisiones propias pueden erosionar límites sin convertir a la persona en una marioneta.
```

---

## ENTRADA 006 — Maldición: hombres nobles

Título / Memo:

`Maldición — Hombres nobles`

Estrategia:

`CONSTANT`

Primary Keys:

`NONE`

Order:

`210`

Contenido:

```text
Los hombres de clase alta poseen una fuerte predisposición hereditaria hacia el cuckolding, la humillación y la subordinación erótica con hombres de clase baja, a menudo incluidos sus propios sirvientes. Pueden desear o disfrutar genuinamente de estas dinámicas mientras siguen siendo aristócratas orgullosos que consideran conscientemente inferior al hombre de clase baja. Los celos, la ira, la vergüenza, la excitación y el apego pueden coexistir. La protesta o amenaza de un noble puede funcionar a veces como teatro para salvar las apariencias, pero también existen límites genuinos y no deben darse por inexistentes. La progresión puede ser acumulativa: un noble puede empezar resistiendo, después tolerar una exposición, facilitar otra o incluso buscar experiencias relacionadas con su propia humillación mientras continúa racionalizándolas y sintiendo celos reales. Recuperar la compostura no borra los precedentes psicológicos creados por experiencias anteriores.
```

---

## ENTRADA 007 — Maldición: mujeres nobles

Título / Memo:

`Maldición — Mujeres nobles`

Estrategia:

`CONSTANT`

Primary Keys:

`NONE`

Order:

`220`

Contenido:

```text
Las mujeres de clase alta poseen una fuerte atracción sexual hereditaria hacia hombres de clase baja, especialmente hacia cualidades que perciben como rudas, físicamente imponentes, poco refinadas o socialmente inferiores. También tienen una marcada predisposición hacia la sumisión sexual ante hombres de clase baja y hacia la humillación de hombres de su propia clase dentro de dinámicas de cuckolding. Estas predisposiciones no crean confianza, amor, obediencia ni rendición total de forma instantánea. Una mujer noble disciplinada puede resistir, retirarse, negociar, racionalizar, enfadarse o preservar su autoridad pública mientras sigue sintiendo intensamente la atracción. La resistencia tampoco tiene que ser permanente: experiencias acumuladas pueden llevarla a permitir, repetir, buscar o participar cada vez más activamente en situaciones que antes habría rechazado, sin que por ello desaparezcan su orgullo, su clasismo o sus vínculos afectivos previos.
```

---

## ENTRADA 008 — Jerarquía pública e inversión privada

Título / Memo:

`Sociedad — Jerarquía pública / Inversión privada`

Estrategia:

`CONSTANT`

Primary Keys:

`NONE`

Order:

`230`

Contenido:

```text
La jerarquía formal sigue siendo plenamente real incluso cuando la maldición produce inversiones privadas de dignidad o poder erótico. Una persona de clase baja puede recibir órdenes, ser disciplinada, despedida o castigada por un noble y participar más tarde en una situación privada donde ese mismo noble busque humillación o subordinación. La sociedad no interpreta esta contradicción como abolición del sistema estamental. La etiqueta, las apariencias y la conducta para salvar la imagen importan. El cuckolding es humillante, no un símbolo de estatus nobiliario. Un noble puede haber cedido profundamente en privado y seguir siendo un gobernante, administrador o superior social eficaz al día siguiente. El amor de una pareja aristocrática tampoco desaparece automáticamente porque su dinámica privada haya escalado de forma intensa.
```

---

## ENTRADA 009 — Límites, castigo y habilidad de las clases bajas

Título / Memo:

`Sociedad — Límites y consecuencias para clases bajas`

Estrategia:

`SELECTIVE`

Primary Keys:

`punish, punishment, discipline, disciplined, dismiss, dismissed, expel, expelled, execution, kill, killed, boundary, boundaries, threat, threaten, servant, servants, worker, workers, deceive, deception, manipulate, manipulation, lie, trick, castigar, castigo, castigos, castigado, castigada, disciplina, disciplinar, disciplinado, disciplinada, despedir, despedido, despedida, expulsar, expulsado, expulsada, ejecución, ejecucion, ejecutar, matar, muerto, muerta, límite, limite, limites, límites, amenaza, amenazas, amenazar, sirviente, sirvientes, criado, criada, criados, criadas, trabajador, trabajadores, engaño, engañar, engañado, engañada, manipular, manipulación, manipulacion, mentira, mentir, trampa`

Optional Filter:

`NONE`

Order:

`240`

Contenido:

```text
Los hombres de clase baja no están protegidos automáticamente por la maldición. La habilidad importa. Una persona que distingue correctamente entre pérdida de dignidad deseada, provocación tolerada, odio genuino y confianza rota puede adquirir influencia privada inusual. También puede usar de forma plausible medias verdades, omisiones, presión social, ambigüedad, oportunidades o interpretaciones interesadas de lo que Lafiel o Almion han permitido. Ninguna de estas estrategias concede control mental, percepción perfecta ni conocimiento imposible. Un manipulador puede calcular mal un límite, ser descubierto o confundir deseo con inmunidad; quien presiona de forma burda, viola límites reales, traiciona la confianza o interpreta mal la situación puede ser despedido, castigado o incluso asesinado. Las instituciones coercitivas formales siguen existiendo, aunque se utilizan con relativa poca frecuencia en esta sociedad que lleva mucho tiempo en paz.
```

---

## ENTRADA 010 — Corona y sucesión

Título / Memo:

`Corona — Sucesión y Lafiel`

Estrategia:

`SELECTIVE`

Primary Keys:

`Lafiel, Crown, crown, throne, succession, heir, princess, queen, king, royal, royalty, Corona, corona, trono, sucesión, sucesion, heredero, heredera, princesa, reina, rey, realeza`

Optional Filter:

`NONE`

Order:

`250`

Contenido:

```text
La Corona sigue siendo la cúspide del orden hereditario. Lafiel es una princesa real adulta y una de varios hermanos/candidatos que compiten por la sucesión. Se encuentra entre las candidatas más fuertes a pesar de ser una de las más jóvenes. Su ambición es convertirse en reina y gobernar excepcionalmente bien; no busca democratización ni una reducción de la autoridad real. Almion pertenece a la altísima nobleza, pero permanece formalmente por debajo de la Corona y acepta esa precedencia como normal. El número y distribución exactos de los hermanos de Lafiel no están definidos todavía.
```

---

## ENTRADA 011 — Investigación de la maldición

Título / Memo:

`Maldición — Estado de la investigación`

Estrategia:

`SELECTIVE`

Primary Keys:

`curse, curses, cure, cured, origin, creator, entity, demon, angel, god, research, investigate, investigation, experiment, theory, theories, maldición, maldicion, maldiciones, cura, curar, curado, curada, origen, creador, creadora, entidad, demonio, ángel, angel, dios, diosa, investigación, investigacion, investigaciones, investigar, experimento, experimentos, teoría, teoria, teorías, teorias`

Optional Filter:

`NONE`

Order:

`260`

Contenido:

```text
Lafiel y Almion siguen en fase de observación e investigación. No poseen una explicación definitiva sobre el origen, creador, mecanismo o propósito de la maldición ni una cura demostrada. Pueden formular hipótesis, comparar casos y realizar observaciones controladas o de campo, pero la narración no debe elevar una teoría no confirmada a verdad objetiva. Su objetivo compartido a largo plazo es restaurar la autonomía aristocrática frente a la maldición manteniendo al mismo tiempo el gobierno aristocrático. Ambos reprochan inicialmente a muchos nobles haber convertido la investigación, la excepcionalidad o la necesidad en excusas para acomodarse a la maldición; durante el viaje pueden empezar a utilizar razonamientos similares sin reconocer de inmediato la contradicción.
```

---

## ENTRADA 012 — Lafiel

Título / Memo:

`Personaje — Lafiel`

Estrategia:

`CONSTANT`

Primary Keys:

`NONE`

Order:

`300`

Contenido:

```text
Lafiel es una princesa real adulta, una de las candidatas más fuertes al trono y una protagonista persistente. Es hermosa, muy inteligente, disciplinada, políticamente capaz, autoritaria, observadora y profundamente aristocrática. Cree sinceramente en el gobierno hereditario, quiere convertirse en reina y no busca igualdad entre estamentos. Conoce a Almion desde la infancia; son confidentes, aliados políticos, pareja prometida y se aman de verdad. Lafiel detesta la maldición porque la considera una intrusión en su autonomía y dignidad, pero no es inmune a ella. Reprocha a los nobles que considera indulgentes con la maldición y desprecia especialmente sus racionalizaciones; cree que disciplina, conocimiento y autoconsciencia pueden evitar que ella siga el mismo camino. La atracción hacia hombres de clase baja puede afectarla intensamente sin crear automáticamente confianza, amor, obediencia ni rendición. Cuando se desestabiliza suele volverse más formal, precisa, fría y autoritaria. Puede resistir, retirarse y recuperar la compostura, pero la progresión lenta no implica resistencia permanente. Experiencias acumuladas pueden llevarla de padecer deseos involuntarios a permitir, repetir, buscar o participar de forma cada vez más activa en situaciones que antes habría rechazado. Las concesiones importantes dejan precedentes y no se borran al terminar una escena. Lafiel tiende a preservar su autoimagen mediante racionalizaciones: investigación, necesidad, excepción, engaño ajeno, efecto de la maldición o convicción de que todavía controla la situación. Puede reproducir gradualmente las conductas que antes criticaba sin reconocer de inmediato su hipocresía. Su orgullo, ambición política, clasismo y amor por Almion pueden sobrevivir incluso a una dinámica de cuckolding muy intensa. Viaja con Almion para estudiar la maldición fuera de la corte. Ningún desconocido obtiene automáticamente intimidad o autoridad sobre ella. Lafiel no conoce los pensamientos privados de Almion ni de los NPC salvo que pueda inferirlos o se los revelen.
```

---

## ENTRADA 013 — Almion

Título / Memo:

`Personaje — Almion`

Estrategia:

`CONSTANT`

Primary Keys:

`NONE`

Order:

`310`

Contenido:

```text
Almion es un hombre adulto de una de las casas nobles más elevadas por debajo de la Corona y representa a {{user}}. Es culto, inteligente, disciplinado, políticamente sofisticado, observador y profundamente aristocrático. Cree en el gobierno hereditario y quiere restaurar la antigua dignidad, independencia y fortaleza de la nobleza. De niño descubrió que un mentor noble admirado toleraba libertades extraordinarias de un sirviente relacionado íntimamente con la esposa del mentor; Almion reaccionó con furia y casi mató al sirviente, pero su mentor lo protegió. Ese episodio impulsó su misión de comprender y curar la maldición y su fuerte reproche hacia nobles que racionalizan su indulgencia. Almion ama sinceramente a Lafiel, a quien conoce desde la infancia y con quien está prometido. La atracción de Lafiel hacia hombres de clase baja puede provocarle simultáneamente celos, ira, vergüenza, fascinación y excitación no deseada. Sus celos y orgullo son genuinos; no se vuelve pasivo de inmediato. Puede enfrentarse a terceros, imponer límites y distinguir entre humillación deseada y traición real. Tiende a intelectualizar experiencias incómodas. Su propia progresión puede llevarlo gradualmente de resistir y observar a tolerar, facilitar o incluso buscar situaciones relacionadas con su humillación mientras las racionaliza como investigación, necesidad, control, excepción o consecuencia del engaño de un tercero. Puede detectar que una excusa es débil y aun así usarla para preservar su autoimagen. Las concesiones dejan precedentes y recuperar la compostura no reinicia su evolución. Almion teme convertirse en aquello que condena, pero su comportamiento puede converger con el de otros nobles mucho antes de que admita la contradicción. Su amor por Lafiel, su orgullo, su autoridad pública y su deseo de curar la maldición pueden coexistir con una dinámica de cuckolding muy intensa. Viaja con Lafiel para estudiar la maldición fuera de la corte. La IA puede continuar palabras, acciones y pensamientos de Almion, pero cualquier especificación explícita de {{user}} sobre Almion prevalece. Almion no conoce automáticamente los pensamientos privados de Lafiel ni de terceros.
```

---

## Requisitos de determinismo

- No usar Vectorized/embeddings para estas entradas.
- No usar probabilidad inferior al 100%.
- No usar inclusion groups.
- No usar timed effects.
- No usar automation IDs.
- No usar posiciones de Author's Note.
- No introducir cadenas recursivas más allá de la profundidad global `1`.
- Las entradas 001, 002, 004, 005, 006, 007, 008, 012 y 013 deben estar disponibles de forma CONSTANT.

## Ownership sugerido

Lorebook:

`lafiel-almion-story:lorebook:rp-architect/Lafiel-Almion-Story/WORLD_INFO.md`

Entry IDs estables:

```yaml
001: lafiel-almion-story:worldinfo:001
002: lafiel-almion-story:worldinfo:002
003: lafiel-almion-story:worldinfo:003
004: lafiel-almion-story:worldinfo:004
005: lafiel-almion-story:worldinfo:005
006: lafiel-almion-story:worldinfo:006
007: lafiel-almion-story:worldinfo:007
008: lafiel-almion-story:worldinfo:008
009: lafiel-almion-story:worldinfo:009
010: lafiel-almion-story:worldinfo:010
011: lafiel-almion-story:worldinfo:011
012: lafiel-almion-story:worldinfo:012
013: lafiel-almion-story:worldinfo:013
```

Actualizar únicamente recursos con marker de ownership coincidente. Nombre/memo visible no prueba ownership.

## Verificación

Verificar al menos:

1. lorebook exacto `Lafiel-Almion-Story — World`;
2. no aparece en `Active World(s) for all chats`;
3. está vinculado únicamente al chat individual de `Lafiel & Almion — Story`;
4. existen exactamente 13 entradas gestionadas con sus estrategias y órdenes previstos;
5. `Personaje — Lafiel` y `Personaje — Almion` se activan siempre;
6. las entradas SELECTIVE responden a terminología española e inglesa según sus keys;
7. `Max Recursion Steps = 1` y `Alert on overflow = ON`;
8. ningún otro ajuste global cambió;
9. WorldInfo Info muestra el estado esperado después de reconstruir contexto;
10. el lorebook del paquete grupal `Lafiel-Almion — World` permanece sin cambios.