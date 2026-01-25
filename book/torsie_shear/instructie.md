# Instructie

Tot nu toe hebben we afzonderlijk schuifspanngen ten gevolge van kromming en verwringing behandeld. In praktijk treden deze twee verschijnselen vaak gelijktijdig op. Afhankelijk van de richtingen van de krachten kunnen de schuifspanningen ten gevolge van buiging en wringing elkaar versterken of afzwakken.

:::::{prf:example}
:nonumber: true

Hieronder is een voorbeeld getoond van een I-profiel met de schuifspanningen ten gevolge van kromming en verwringing apart.

::::{grid} 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ../shear_dunwandig/instructie_data/richting_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ../torsie_model/instructie_data/I-balk.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

```{figure-end}
```

:::

::::

:::::

De plek waar de schuifspanning maximaal zijn is meestal het meest van belang. Voor de schuifspanning ten gevolge van kromming is dat ter hoogte van het normaalkrachtencentrum. Voor de schuifspanning ten gevolge van verwringing is dat afhankelijk van het model.

:::::{prf:example}
:nonumber: true

Voor het I-profiel is de maximale schuifspanning ten gevolge van wringing ter hoogte van het normaalkrachtencentrum aan de rechterkant van de wand omdat daar de schuifspanningen allebei maximaal zijn en in dezelfde richting wijzen.

```{figure} ./instructie_data/maximum.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

:::::

:::{caution}
Merk op dat we de schuifspanningen ten gevolge van afschuiving verwaarlozen en dat we de schuifspanningen ten gevolge van verwringing enkel bepalen ten opzichte van het dwarskrachtencentrum. Echter is met onze huidige modelling niet vast te stellen of we deze schuifspanningen inderdaad mogen negeren
:::

## Voorbeeld

Het bepalen van de schuifspanningen ten gevolge van wringing wordt getoond in het volgende voorbeeld.

::::::{prf:example}
:nonumber: true

Gegevens is de volgende constructie en twee dunwandige doorsnede:

::::{grid} 2 2 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/Constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```


De uitwendige krachten en  
oplegreacties grijpen aan  
in het dwarskrachtencentrum.

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/doorsnede_1.svg
:align: center
:name: fig:doorsnede_1
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```
:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/doorsnede_2.svg
:align: center
:name: fig:doorsnede_2
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```
:::

::::

https://oit.tudelft.nl/CT1000/2025/week_15/session/intro.html