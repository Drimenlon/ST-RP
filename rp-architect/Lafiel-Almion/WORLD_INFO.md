# WORLD INFO SPEC — Lafiel & Almion

This file defines the exact desired World Info/Lorebook content for the pilot.

`WORLD.md` remains the prose canon reference. This file is the implementation-oriented decomposition Luna must consume.

## Lorebook identity

Name:

`Lafiel-Almion — World`

Desired scope:

`Chat Lorebook` for the group chat `Lafiel & Almion`.

Do not add this lorebook globally.

Do not bind it to unrelated characters or chats.

If the current Luna runbooks do not authorize creation/binding of this exact World Info configuration, STOP and return only that missing capability to Infrastructure/Sol.

## Activation settings

RP-specific requirements:

- Include Names: `ON`
- Case-sensitive keys: `OFF`
- Match whole words: `ON`
- Max Recursion Steps: `1` (no recursive activation chain required for this pilot)
- Alert on overflow: `ON`
- Context/Budget: preserve the currently validated global value; this RP does not authorize changing the global World Info budget.
- Min Activations: `0`

Unless an entry says otherwise:

- Enabled: `YES`
- Position: `Before Char Defs`
- Trigger %: `100`
- Non-recursable: `YES`
- Delay until recursion: `NO`
- Prevent further recursion: `NO`
- Ignore budget: `NO`
- Inclusion Group: `NONE`
- Character filter: `NONE` (scope is already restricted by Chat Lorebook binding)
- Additional Matching Sources: all `OFF`

---

## ENTRY 001 — Estate system

Title / Memo:

`World — Hereditary Estate System`

Strategy:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`100`

Content:

```text
This society is organized into rigid hereditary estates: Crown/royal family, nobility, clergy, and lower classes including servants. Social mobility is extraordinarily rare. A person born a servant normally remains lower-class for life; a person born noble normally remains noble for life. The hierarchy is treated by most inhabitants as the normal structure of civilization, not as a temporary injustice awaiting revolution. Lower-class material comfort does not imply social equality, and private sexual inversions do not abolish formal rank.
```

---

## ENTRY 002 — Prosperity and modern technology

Title / Memo:

`World — Modern Prosperity`

Strategy:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`110`

Content:

```text
The world is technologically modern and extremely prosperous despite its hereditary hierarchy. Electricity, internet, smartphones, modern transport, domestic appliances, automation, excellent medicine, strong public services, housing security and a universal basic income exist. Serious disease is rare and even servants generally enjoy high material living standards. Economic and status inequality remain large: noble households, estates and political authority can still dwarf those of lower-class people.
```

---

## ENTRY 003 — Settlement scale and aesthetic

Title / Memo:

`World — Settlement Pattern`

Strategy:

`SELECTIVE` / Green Circle

Primary Keys:

`city, cities, town, towns, village, villages, capital, settlement, settlements, estate, estates, palace, travel, road, district`

Optional Filter:

`NONE`

Order:

`120`

Content:

```text
Settlements preserve a medieval-like spatial and visual character while incorporating modern technology. The setting favors villages, towns, noble estates, palaces and small-to-midsized cities rather than giant modern megacities. Settlements may be somewhat larger than their historical medieval equivalents, but the social landscape should still feel decentralized, estate-centered and human-scale.
```

---

## ENTRY 004 — Modern nobility

Title / Memo:

`World — Modern Nobility`

Strategy:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`130`

Content:

```text
Ancient nobles were more martial, aggressive and warlike. Across generations the hereditary curse coincided with the upper estates becoming a more intellectual and administrative ruling caste. Modern nobles are commonly highly educated, sophisticated, strategically capable, verbally skilled and competent administrators. They remain proud, class-conscious, hierarchical and often arrogant. The curse did not make them egalitarian; their competence and their classism coexist.
```

---

## ENTRY 005 — Curse: public facts and unknown origin

Title / Memo:

`Curse — Core Public Knowledge`

Strategy:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`200`

Content:

```text
The hereditary phenomenon called the curse and its broad sexual/psychological effects are common public knowledge. Its true creator, mechanism and purpose are unknown. In-world theories may invoke a god, demon, angel, experiment, punishment, blessing, amusement or incomprehensible motive, but none is confirmed canon. The curse does not erase free will or personality. It creates strong inherited predispositions that interact with existing pride, love, jealousy, ambition, judgment and self-control.
```

---

## ENTRY 006 — Curse: noble men

Title / Memo:

`Curse — Noble Men`

Strategy:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`210`

Content:

```text
High-class men possess a strong inherited predisposition toward cuckolding, humiliation and erotic subordination involving lower-class men, often including their own servants. They can genuinely desire or enjoy these dynamics while remaining proud aristocrats who consciously consider the lower-class man socially inferior. Jealousy, anger, shame, arousal and attachment can coexist. A noble man's protest or threat may sometimes function as face-saving theater, but genuine boundaries also exist and must not be assumed away.
```

---

## ENTRY 007 — Curse: noble women

Title / Memo:

`Curse — Noble Women`

Strategy:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`220`

Content:

```text
High-class women possess a strong inherited sexual attraction toward lower-class men, especially qualities they perceive as rough, physically imposing, unrefined or socially beneath them. They also have a marked predisposition toward sexual submission to lower-class men and toward humiliating men of their own class within cuckolding dynamics. These predispositions do not create instant trust, love, obedience or total surrender. A disciplined noble woman can resist, retreat, negotiate, rationalize, become angry or preserve public authority while still feeling the attraction strongly.
```

---

## ENTRY 008 — Public hierarchy and private inversion

Title / Memo:

`Society — Public Hierarchy / Private Inversion`

Strategy:

`CONSTANT` / Blue Circle

Primary Keys:

`NONE`

Order:

`230`

Content:

```text
Formal hierarchy remains fully real even when the curse produces private inversions of dignity or erotic power. A servant may be ordered, disciplined, dismissed or punished by a noble and later participate in a private situation where that same noble seeks humiliation or subordination. Society does not interpret this contradiction as abolition of the estate system. Etiquette, appearances and face-saving behavior matter. Cuckolding is humiliating, not a noble status symbol.
```

---

## ENTRY 009 — Boundaries, punishment and servant skill

Title / Memo:

`Society — Servant Boundaries and Consequences`

Strategy:

`SELECTIVE` / Green Circle

Primary Keys:

`punish, punishment, discipline, disciplined, dismiss, dismissed, expel, expelled, execution, kill, killed, boundary, boundaries, threat, threaten, servant, servants`

Optional Filter:

`NONE`

Order:

`240`

Content:

```text
Lower-class men are not automatically protected by the curse. Skill matters. A servant who correctly distinguishes desired loss of dignity from genuine hatred or broken trust may gain unusual private influence, but a servant who pushes crudely, violates real boundaries, betrays trust or mistakes arousal for immunity can be dismissed, punished or even killed. Formal coercive institutions still exist, though they are used comparatively rarely in this long-peaceful society.
```

---

## ENTRY 010 — Crown and succession

Title / Memo:

`Crown — Succession and Lafiel`

Strategy:

`SELECTIVE` / Green Circle

Primary Keys:

`Lafiel, Crown, crown, throne, succession, heir, princess, queen, king, royal, royalty`

Optional Filter:

`NONE`

Order:

`250`

Content:

```text
The Crown remains the apex of the hereditary order. Lafiel is an adult royal princess and one of several siblings/candidates competing for succession. She is among the strongest candidates despite being one of the youngest. Her ambition is to become queen and govern exceptionally well; she does not seek democratization or dilution of royal authority. Almion is extremely high nobility but remains formally beneath the Crown and accepts that precedence as normal.
```

Note:

The exact number/distribution of Lafiel's siblings is intentionally NOT defined here because RP Architect has not closed that canon detail.

---

## ENTRY 011 — Research into the curse

Title / Memo:

`Curse — Research State`

Strategy:

`SELECTIVE` / Green Circle

Primary Keys:

`curse, cure, cured, origin, creator, entity, demon, angel, god, research, investigate, investigation, experiment, theory, theories`

Optional Filter:

`NONE`

Order:

`260`

Content:

```text
Lafiel and Almion are still in the observation and investigation stage. They possess no definitive explanation for the curse's origin, creator, mechanism or purpose and no proven cure. They may form hypotheses, compare cases and conduct controlled observations, but the narration must not promote an unconfirmed theory into objective truth. Their shared long-term goal is to restore aristocratic autonomy from the curse while retaining aristocratic rule.
```

---

## Determinism requirements

For this pilot:

- Do not use Vectorized/embedding activation.
- Do not use probability below 100%.
- Do not use inclusion groups.
- Do not use timed effects.
- Do not use automation IDs.
- Do not use Author's Note positions.
- Do not introduce recursive lore chains.

The goal is predictable, inspectable activation during the first RP test.

## Verification

When implementation becomes authorized, verify with WorldInfo Info + Prompt Inspector:

1. Entries 001, 002, 004, 005, 006, 007 and 008 are active every generation in the bound group chat.
2. Entry 003 is inactive without settlement/location keys and activates when one of its keys appears.
3. Entry 009 is inactive without boundary/discipline/servant-related keys and activates on a matching key.
4. Entry 010 activates when Lafiel/Crown/succession terminology enters scanned context.
5. Entry 011 activates when curse/research terminology enters scanned context.
6. No entry from this lorebook activates in unrelated chats.
7. No unrelated lorebook content appears because of this package.
