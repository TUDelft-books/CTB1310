````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is gebaseerd op [deze oefening uit het online boek van het vak CT1000S Structural Mechanics op de Technische Universiteit Delft](https://oit.tudelft.nl/CT1000/2024/week_13/session_3/intro.html#exercise-internal-forces-and-displacement-due-to-torsion) {cite:p}`CT1000_2024`.

```
````

# Begeleide oefening 3

Gegeven is de volgende constructie en een willekeurige doorsnede met bekend dwarskrachtencentrum.:

```{figure} ./lesoefening2_data/constructie.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
```

Waarvan je de wringende momentenlijn moet bepalen.

:::::{exercise}
:nonumber: true

Gegeven zijn drie 2D-weergaves van de constructie

```{figure} ./lesoefening2_data/opties.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```

```{h5p} https://tudelft.h5p.com/content/1292760477571217987/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

Optie 3 is correct:

De verdeelde belasting werkt naast het dwarskrachtencentrum, dus dit veroorzaakt een wringend moment van $z$ naar $y$. De rechterhandregel geeft dan een vectorpijl in de negatieve $x$-richting.

::::

% solution_end

:::::{exercise}
:nonumber: true

Wat weet je over de vorm van de wringende momentenlijn.

```{h5p} https://tudelft.h5p.com/content/1292757750575012567/embed
```

:::::


% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

De wringende momentenlijn verloopt tussen de punten $\rm{A}$ en $\rm{B}$, $\rm{B}$ en $\rm{C}$ *linear*: de constante verdeelde belasting treedt op naast het dwarskrachtencentrum, dus dat zorgt voor een lineair verlopende wringende momentenlijn.

In $\rm{C}$ het wringend moment is gelijk aan *een nog onbekende waarde*: dit uiteinde is geen vrij uiteinde.

Rondom de punten $\rm{A}$ en $\rm{B}$, het wringende moment maakt *een sprong*: de uitwendige geconcentreerde wringende momenten zorgen voor een uitwendig wringend moment, wat een sprong veroorzaakt inde wringende momentenlijn.

::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de wringend momentenlijn.

```{h5p}  https://tudelft.h5p.com/content/1292760481373833897/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

Het wringend moment halverwege $\rm{C}$ en $\rm{B}$:

```{figure} ./lesoefening2_data/Snede_CB_halverwege.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```
$$
\begin{align*}
\sum T_{\rm{BC}} &= 0 \\
M_{\rm{t}}^{\rm{BC} \, \rm{halverwege}} - 100 \cdot 2 &= 0 \\
M_{\rm{t}}^{\rm{BC} \, \rm{halverwege}} &= 200 \, \rm{Nm} \left( \twoheadleftarrow \mid \twoheadrightarrow \right)
\end{align*} 
$$

Het wringend moment net links van $\rm{B}$:

```{figure} ./lesoefening2_data/Snede_B_links.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```
$$
\begin{align*}
\sum T_{\rm{BC}} &= 0 \\
M_{\text{t}}^{\rm{B} \, \rm{links}} - 100 \cdot 4 &= 0 \\
M_{\text{t}}^{\rm{B} \, \rm{links}} &= 400 \, \rm{Nm} \left( \twoheadleftarrow \mid \twoheadrightarrow \right)
\end{align*}
$$


Het wringend moment net rechts van $\rm{B}$:
```{figure} ./lesoefening2_data/Snede_B_rechts.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```
$$
\begin{align*}
\sum T_{\text{BC}} &= 0 \\
M_{\rm{t}}^{\rm{B} \, \rm{rechts}} - 100 \cdot 4 + 400 &= 0 \\
M_{\rm{t}}^{\rm{B} \, \rm{rechts}} &= 0 
\end{align*} 
$$

Het wringend moment halverwege $\rm{B}$ en $\rm{A}$:

```{figure} ./lesoefening2_data/Snede_AB_halverwege.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```
$$
\begin{align*}
\sum T_{\text{AC}} &= 0 \\
M_{\rm{t}}^{\rm{AB} \, \rm{halverwege}} - 100 \cdot 6 + 400 &= 0 \\
M_{\rm{t}}^{\rm{AB} \, \rm{halverwege}} &= 200 \, \rm{Nm} \left( \twoheadleftarrow \mid \twoheadrightarrow \right)
\end{align*} 
$$

Het wringend moment in $\rm{A}$:

```{figure} ./lesoefening2_data/Moment_A.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```
$$
\begin{align*}
\sum T_{\text{AC}} &= 0 \\
M_{\rm{t}}^{\rm{A}} - 100 \cdot 8 + 400 &= 0 \\
M_{\rm{t}}^{\rm{A}} &= 400 \, \rm{Nm} \left( \twoheadleftarrow \mid \twoheadrightarrow \right)
\end{align*} 
$$

De wringende momentenlijn ziet er dan als volgt uit:
```{figure} ./lesoefening2_data/Mt-line.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2
number:
---
```

::::

% solution_end
