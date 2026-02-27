````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is gebaseerd op [deze oefening uit het online boek van het vak CT1000S Structural Mechanics op de Technische Universiteit Delft](https://oit.tudelft.nl/CT1000/2024/week_13/session_3/intro.html#exercise-internal-forces-and-displacement-due-to-torsion) {cite:p}`CT1000_2024`.

```
````

# Begeleide oefening 2

Gegeven is de volgende constructie:

```{figure} ./lesoefening_data/constructie.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```

Waarvan je de wringende momentenlijn moet bepalen.

:::::{exercise}
:nonumber: true

Gegeven zijn vier 3D-weergaves van de constructie

```{figure} ./lesoefening_data/3D.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```

```{h5p} https://tudelft.h5p.com/content/1292760346691162017/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Optie 1 is correct:

Ons assenstelsel is altijd rechtsdraaiend, dus een rotatie van bijvoorbeeld z naar x geeft met de rechterhandregel je duim in de richting van de y-as.

Het assenstelsel had daarnaast de verdeelde belastingen en oplegging op de x-as, niet de puntlasten.

Optie 3 is ook correct:

Je hebt nu het assenstelsel verplaatst, maar dat is niet erg zolang je de wringende momenten nog maar wel laat aangrijpen in het dwarskrachtencentrum, niet op de locatie van het nieuwe assenstelsel.

::::

:::::{exercise}
:nonumber: true

Gegeven zijn vier 2D-weergaves van de constructie

```{figure} ./lesoefening_data/2D.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```

```{h5p} https://tudelft.h5p.com/content/1292760349282191447/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Optie 1 is correct:

De puntenlasten zorgen voor draaiing van $z$ naar $y$ dus dat is een negatief wringend moment. De verdeelde belasting zorgt niet voor een wringend moment.

::::

:::::{exercise}
:nonumber: true

Wat weet je over de vorm van de wringende momentenlijn.

```{h5p}  https://tudelft.h5p.com/content/1292751704243715217/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De wringende momentenlijn verloopt tussen de punten $\rm{A}$ en $\rm{B}$, $\rm{B}$ en $\rm{C}$, etc *constant*: de verdeelde belasting treedt op in het dwarskrachtencentrum, dus er is geen verdeelde belasting die zorgt voor wringende momenten.

In $\rm{E}$ is het wringend moment gelijk aan *0*: op het vrije uiteinde werken geen uitwendige wringende momenten, dus de wringende momentenlijn begint op 0.

Rondom de punten $\rm{B}$, $\rm{C}$, $\rm{D}$ en $\rm{E}$, maakt het wringende moment *een sprong*: de puntlasten zorgen voor een uitwendig wringend moment, wat een sprong veroorzaakt in de wringende momentenlijn.

::::

:::::{exercise}
:nonumber: true

Bepaal de wringend momentenlijn.

```{h5p}  https://tudelft.h5p.com/content/1292751710544863507/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Het wringend moment tussen $\rm{D}$ en $\rm{DE}$ is nul. $\rm{E}$ is een vrij uiteinde en op deel $\rm{DE}$ werkt geen wringend moment. Het wringend moment voor het deel $\rm{CD}$ is te bepalen met de volgende snede:

```{figure} ./lesoefening_data/Snede_CD.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```
$$
\begin{align*}
\sum T_{\rm{CD}} &= 0 \\
- M_{\rm{t}}^{\rm{CD}} - 120 &= 0 \\
M_{\rm{t}}^{\rm{CD}} &= -120 \ \rm{kNm} \left( \twoheadrightarrow \mid \twoheadleftarrow \right)
\end{align*} 
$$

Een vergelijkbare snede kan worden gemaakt om het wringend moment te vinden in deel $\rm{BC}$:
```{figure} ./lesoefening_data/Snede_BC.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```
$$
\begin{align*}
\sum T_{\rm{BC}} &= 0 \\
- M_{\rm{t}}^{\rm{BC}} - 120 - 120 &= 0 \\
M_{\rm{t}}^{\rm{BC}} &= -240 \ \rm{kNm} \left( \twoheadrightarrow \mid \twoheadleftarrow \right)
\end{align*} 
$$

Het wringend moment in $\rm{AB}$ kan worden gevonden met de volgende snede:

```{figure} ./lesoefening_data/Snede_AB.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```

$$
\begin{align*}
\sum T_{\rm{AB}} &= 0 \\
- M_{\rm{t}}^{\rm{AB}} - 120 - 120 - 120 &= 0 \\
M_{\rm{t}}^{\rm{AB}} &= -360 \ \rm{kNm} \left( \twoheadrightarrow \mid \twoheadleftarrow \right)
\end{align*} 
$$

```{figure} ./lesoefening_data/Mt-line.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```

::::
