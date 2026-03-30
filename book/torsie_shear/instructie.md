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
Merk op dat we de schuifspanningen ten gevolge van afschuiving verwaarlozen en dat we de schuifspanningen ten gevolge van verwringing enkel bepalen ten opzichte van het dwarskrachtencentrum. Echter is met onze huidige modellering niet vast te stellen of we deze schuifspanningen inderdaad mogen negeren
:::

## Voorbeeld

Het bepalen van de schuifspanningen ten gevolge van wringing wordt getoond in het volgende voorbeeld.

````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Dit voorbeeld is gebaseerd op [deze oefening uit het online boek van het vak CTS1000 Structural Mechanics op de Technische Universiteit Delft](https://oit.tudelft.nl/CT1000/2025/week_15/session/intro.html#exam-assignment-1-continuum-mechanics) {cite:p}`CT1000_2025`.

```
````


::::::{prf:example}
:nonumber: true

Gegevens is de volgende constructie en dunwandige doorsnede:

::::{grid} 2 2 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/constructie.svg
:align: center
:class: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum
:number:
```

De uitwendige krachten en oplegreacties grijpen  
aan in het normaal- en dwarskrachtencentrum.

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/doorsnede.svg
:align: center
:class: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum
:number:
```

De doorsnede mag als dunwandig beschouwd worden.

```{figure-end}
```
:::

::::

Waarvoor de maximale schuifspanningen ten gevolge van buiging en wringing gevraagd zijn op een positieve doorsnede, inclusief de plek van die spanningen.

De maximale schuifspanning is daar waar zowel de dwarskracht als het wringend moment maximaal zijn. Dat is in het gehele gedeelte $\rm{AB}$. Het buiging moment neemt in dat gedeelte wel toe, maar dat is niet van invloed op de schuifspanningen.

Laten we beginnen met de schuifspanningen ten gevolge van buiging. Daarvoor moeten we eerst de dwarskracht in de doorsnede bepalen. Deze kan gevonden worden met het evenwicht in de $z$-richting:

```{figure} instructie_data/FBD_continuum.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum
:number:
```

$$
\sum F_{\rm{z}} = 0 \to V_{z,\rm{A}} = 120 \, \rm{kN}
$$

Om de schuifspanningen te bepalen moeten we de doorsnedegrootheden berekenen:

$$
A = 500 \cdot 12 + 2 \cdot \sqrt{600^2 + 250^2} \cdot 12= 21600
$$

$$
\bar z_{\rm{N.C.}} = \cfrac{2\cdot \sqrt{600^2 + 250^2} \cdot 12 \cdot 300}{A} = \cfrac{650}{3} \approx 217 \, \rm{mm}
$$

Voor het bereken van het oppervlaktetraagheidsmoment moeten we de hoogte en breedte in de $y$ en $z$ richting bepalen om onze formules voor rechthoekige doorsnedes te kunnen gebruiken:

```{figure} instructie_data/wand.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum
:number:
```

$$
\begin{align*}
I_{zz} &= \cfrac{1}{12} \cdot 500 \cdot 12^3 + 500 \cdot 12 \cdot \left( -\cfrac{650}{3} \right)^2 \\
& \quad + 2 \cdot \left( \cfrac{1}{12} \cdot \cfrac{13}{12} \cdot 12 \cdot 600^3 + \sqrt{600^2 + 250^2} \cdot 12 \cdot \left( 300 - \cfrac{650}{3} \right)^2 \right) \\
& = 858.072 \cdot 10^6 \, \rm{mm^4}
\end{align*}
$$

De maximale schuifspanning bevindt zich ter hoogte van het normaalkrachtencentrum. Het statisch moment van het afschuivende gedeelte daarboven kunnen we nu berekenen:

```{figure} instructie_data/afschuivend.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum
:number:
```

$$
S_z^{\rm{a}} = 12 \cdot 500 \cdot \cfrac{-650}{3} + 2 \cdot \cfrac{13}{12} \cdot 12 \cdot \cfrac{650}{3} \cdot \cfrac{\cfrac{-650}{3}}{2} = \cfrac{17192500}{9} \approx 1.91 \cdot 10^6 \, \rm{mm^3}
$$

De absolute waarde van de schuifspanning kan nu gevonden worden:

$$
\tau \approx \cfrac{120 \cdot 10^3 \cdot 1.91 \cdot 10^6}{2 \cdot 12 \cdot 85.8072 \cdot 10^6} \approx 11 \, \rm{MPa}
$$

We weten het volgende over het verloop:

- Vanwege symmetrie moet de schuifspanning middenin de flens en in het onderste punt gelijk zijn aan $0$.
- De horizontale flens zal een lineair verloop van de schuifspanning hebben in de horizontale richting.
- Het diagonale gedeelte zal een gekromd verloop van de schuifspanning hebben in de verticale richting.
- Het maximum van de schuifspanning zit ter hoogte van het normaalkrachtencentrum omdat daar het statisch moment van het afschuivend gedeelte het grootst is.
- De dwarskracht zorgt voor een dwarskracht omlaag op een positieve snede. Dat betekent dat de schuifspanning in de diagonale delen schuin omlaag wijst.
- Vanwege de stroming van de schuifstroom zal de schuifspanning vanuit het midden in de flenzen naar buiten stromen.

Dit geeft:

```{figure} instructie_data/maximaal.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum
:number:
```

Daarbij komt nog de schuifspanning ten gevolge van wringing.

Het dwarskrachtencentrum bevindt zich in de verticale symmetrieas op een onbekende hoogte. Echter is deze hoogte niet van belang voor het berekenen van het wringend moment.

Het wringend moment kan gevonden worden met het evenwicht rond de $x$-as:

```{figure} instructie_data/FBD_continuum.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum
:number:
```

$$
\begin{align*}
\sum T_{\rm{x}} &= 0 \\
M_{\rm{t,A}} - 120 \cdot 0.6 &= 0 \\
M_{\rm{t,A}} &= 72 \, \rm{kNm} \left(  \twoheadleftarrow \mid \twoheadrightarrow \right)
\end{align*}
$$

We hebben een dunwandige, gesloten, niet-cirkelvormige doorsnede, dus hebben we het omhullend oppervlakte nodig voor het berekenen van de schuifspanning ten gevolge van wringing.

$$
A_{\rm{m}} = 500 \cdot 600 \cdot \frac{1}{2} = 150000 \, \rm{mm^2}
$$

De schuifspanning ten gevolge van wringing kan nu berekend worden:

$$
\tau = \cfrac{M_{\rm{t}}}{2 t A_{\rm{m}}} = \cfrac{72 \cdot 10^6}{2 \cdot 12 \cdot 150000} = 20 \, \rm{MPa}
$$

De richting van het wringend moment is van $y$ naar $z$ op onze positieve snede. Dus de schuifspanningen werken ook in die richting (tegen de klok in):

```{figure} instructie_data/wringing.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum
:number:
```

De maximale schuifspanning is dus te vinden ter hoogte van het normaalkrachtencentrum aan de positieve $y$-kant van de doorsnede. Over de gehele dikte van de wand (loogrecht op de rand) is de schuifspanning daar maximaal. Daar werken de schuifspanningen ten gevolge van buiging en wringing in dezelfde richting en zijn ze dus op te tellen: $\tau \approx 11 + 20 \approx 31 \, \rm{MPa}$. Deze werkt naar schuinbeneden:

```{figure} instructie_data/som.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum
:number:
```

::::::

```{hide-sticky-margin}
```

## Meer voorbeelden
In hoofdstuk 6.4 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` worden meer voorbeelden gegeven van het bepalen van schuifspanningen in verschillende situaties: Voorbeeld 5, 6 en 8.

## Instructies in collegevorm
Dit onderwerp is [in les 11](https://collegerama.tudelft.nl/Mediasite/Channel/public-ctb1310/watch/0e6b6d69aebc4c61887b5b2aaca496b11d) gepresenteerd in collegevorm van 8:50 tot 44:15

## Oefeningen
[Opgaves 6.22 - 6.28, 6.31 - 6.34 in hoofdstuk 6 van het boek Mechanica, spanningen, vervormingen en verplaatsingen](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/files/TM2vraagstukkenbundel.pdf) {cite:p}`Hartsuijker2013`. Antwoorden zijn [hier](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol2/Chapter5/) beschikbaar.
