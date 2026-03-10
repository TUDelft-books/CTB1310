# 10 maart: TOZ schuifspanningen

Gegeven is de volgende constructie en doorsnede

::::{grid} 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ./toz_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

De verdeelde belasting en oplegreacties  
grijpen aan in het normaalkrachtencentrum.

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./toz_data/doorsnede.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

Deze doorsnede moet als dunwandige  
doorsnede worden beschouwd.

```{figure-end}
```

:::

::::

Gevraagd zijn de schuifspanningen ten gevolge van buiging en wringing op een positieve doorsnede in $\rm{B}$

:::::{exercise}
:label: TOZ_2
:nonumber: true

Wat is de locatie van het normaalkrachtencentrum in $y$-richting?
% Geef de coördinaten in het $y,z$-assenstelsel in $\rm{mm}$

:::::

::::{admonition} Oplossing
:class: solution, dropdown

In de $y$-richting kan de locatie gevonden worden ten opzichte van de rechter wand:

```{figure} ./toz_data/statisch_moment.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

$$\bar y_{\rm{N.C.}} = \cfrac{S_{\bar y}}{A} = \cfrac{300 \cdot 12 \cdot \cfrac{300}{2}}{300 \cdot 12 + 300 \cdot 12} = 75 \, \rm{mm}$$

::::

## Buiging

:::::{exercise}
:label: TOZ_3_5
:nonumber: true

De volgende vraag gaat over de absolute waarde van de maximale spanning in doorsnede $\rm{B}$ ten gevolge van buiging. Wat is de absolute waarde van het statisch moment van het afschuivende gedeelte voor deze maximale schuifspanning?

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De schuifspanning kan bepaald worden met het afschuivende gedeelte van de helft van de verticale wand:

```{figure} ./toz_data/afsnijden.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

$$ S_z^{\rm{a}} = 150 \cdot 12 \cdot 75 = 135000 \, \rm{mm^3} $$

::::

:::::{exercise}
:label: TOZ_3
:nonumber: true

Wat is de absolute waarde van de maximale spanning in doorsnede $\rm{B}$ ten gevolge van buiging?
% Geef je antwoord in $\rm{MPa}$.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De maximale schuifspanning bevindt zich ter hoogte van het normaalkrachtencentrum in de verticale wanden:

```{figure} ./toz_data/verdeling.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

Er geldt:

$$I_{zz} = \frac{1}{12} \cdot 300 \cdot 12^3 + \frac{1}{12} \cdot 12 \cdot 300^3 = 27043200 \, \rm{mm}^4$$

en

```{figure} ./toz_data/VLS_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

$$
\begin{align*}
\sum F_{\rm{v}} &= 0 \\
V_{\rm{B}} - 15024 \cdot 3 &=0 \\
V_{\rm{B}} &= 45072 \, \rm{N}
\end{align*}
$$

Dit geeft:

$$\left| \tau \right| = \cfrac{\left| 45072 \cdot 135000 \right|}{12 \cdot 27043200} = 18.75 \, \rm{MPa}$$
::::

:::::{exercise}
:label: TOZ_4
:nonumber: true

Wat is/zijn de richting(en) van de maximale schuifspanning ten gevolge van alleen buiging op een positieve doorsnede in $\rm{B}$?

% kies één of meerdere antwoorden aan

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De dwarskracht werkt op een negatieve doorsnede omhoog, dus op een positieve doorsnede omlaag. Voor de eerder afgeleide spanningsverdeling moet de maximale schuifspanning dan ook naar beneden lopen

::::

## Wringing

:::::{exercise}
:label: TOZ_1
:nonumber: true

Gegeven zijn drie 2D-weergaves van de constructie. Welk model is de juiste om de snedekrachten en oplegreacties te bepalen?

::::{grid} 3
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ./toz_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

Optie 1

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./toz_data/optie2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

Optie 2

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./toz_data/optie3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

Optie 3

```{figure-end}
```

:::

::::

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Het dwarskrachtencentrum ligt op het kruispunt van de wanden ($y = - \bar y_{\rm{N.C.}}$). De verdeelde belasting grijpt aan in het normaalkrachtencentrum wat daarom voor wringing van $y$ naar $z$ zorgt, dus de dubbele vectorpijl naar rechts.

```{figure-start} ./toz_data/optie2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

Optie 2

```{figure-end}
```

::::

:::::{exercise}
:label: TOZ_5
:nonumber: true

Wat is het wringend moment in $\rm{B}$?
% Geef je antwoord in $\rm{Nm}$. Ga uit van de standaard tekenafspraken.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Het verdeelde wringend moment is $15024 \cdot \bar y_{\rm{N.C.}} = 15024 \cdot 0.075 = 1126.8 \, \rm{Nm/m}$

Dit geeft:

```{figure} ./toz_data/VLS.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

$$
\begin{align*}
\left. \sum T \right|_{\rm{BC}} &= 0 \\
-M_{\rm{t,B}} + 1126.8 \cdot 3 - 604.8 &= 0 \\
M_{\rm{t,B}} &= 2775.6 \, \rm{Nm}
\end{align*}
$$

::::

:::::{exercise}
:label: TOZ_42
:nonumber: true


Welk model heb je nodig om de schuifspanningen ten gevolge van wringing te berekenen?

- $\tau  = \cfrac{{{M_t} \cdot r}}{{{I_p}}} $
- $\tau  = \cfrac{{{M_t}}}{{2 \cdot {A_m} \cdot t}}$
- $\tau  = \cfrac{{{M_t} \cdot {e_m}}}{{\tfrac{1}{2} \cdot \sum\limits_i {\tfrac{1}{3} \cdot {h_i} \cdot t_i^3} }} $

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Het gaat om een open, dunwandige doorsnede, dus de derde formule is van toepassing: $\tau  = \cfrac{{{M_t} \cdot {e_m}}}{{\tfrac{1}{2} \cdot \sum\limits_i {\tfrac{1}{3} \cdot {h_i} \cdot t_i^3} }} $

::::

:::::{exercise}
:label: TOZ_6
:nonumber: true

Wat is de absolute waarde van de maximale spanning in doorsnede $\rm{B}$ ten gevolge van wringing?
% Geef je antwoord in $\rm{MPa}$.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De doorsnede is een open, dunwandige doorsnede. De maximale spanning bevindt zich dus aan de buitenrand van de wanden: $e_m = \frac{1}{2} \cdot 12 = 6 \, \rm{mm}$

Dit geeft:

$$ \tau = \cfrac{2775.6 \cdot 10^3 \cdot 6}{\frac{1}{2} \cdot \left( \frac{1}{3} \cdot 300 \cdot 12^3 + \frac{1}{3} \cdot 300 \cdot 12^3 \right)} = 96.375 \, \rm{MPa}$$

::::


:::::{exercise}
:label: TOZ_7
:nonumber: true

Wat is/zijn de richting(en) van de schuifspanning ten gevolge van alleen wringing op een positieve doorsnede in $\rm{B}$?

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Op een negatieve doorsnede werkt een negatief wringend moment, dus van $y$ naar $z$. Op een positieve doorsnede werkt dan ook een negatief wringend moment, van $z$ naar $y$. Deze werkt op alle uiterste randen van de wanden dus zowel omhoog, omlaag, naar links als naar rechts.

::::
