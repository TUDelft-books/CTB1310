# Begeleide oefening 2

Gegeven is de volgende constructie:

::::{grid} 1 1 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./lesoefening2/constructie_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect_oef
:number:
:figclass: sticky-margin
```

:::

:::{grid-item}
:columns: auto

```{figure} ./lesoefening2/constructie_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect_oef
:number:
:figclass: sticky-margin
```

:::

::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:

---
M[4]
> Heb je het goede teken? Het assenstelsel bepaalt het teken van de dwarskracht.
^^^
?
De dwarskracht net rechts van $\rm{B}$ is {gap} $\rm{kN}$
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Er kan een snede net rechts van $\rm{B}$ worden gemaakt:

```{figure} ./lesoefening2/Dwarskracht_B.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect_oef
:number:
```

Verticaal evenwicht geeft:

$$
\begin{align*}
\sum F_ {\rm{v}} &= 0 \\
- V_{\rm{B}} + 2 \cdot 2 &= 0 \\
V_{\rm{B}} &= 4 \, \rm{kN} \positiveshear 
\end{align*}
$$

::::

% solution_end

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:

---
M[-0.24]
^^^
?
De maximale schuifspanning op een negatieve doorsnede net rechts van $\rm{B}$ is {gap} $\rm{MPa} \, \left(\downarrow\right)$
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De maximale schuifspanning vindt plaats ter hoogte van het normaalkrachtencentrum. Dat geeft dit afschuivende deel:

```{figure} ./lesoefening2/afschuivend_deel_B.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect_oef
:number:
```

Het statisch moment van dit afschuivende deel is:

$$
\begin{align*}
S_{z}^{\rm{a}} &= A_{\rm{afschuivend} \, \rm{deel}} \, z_{\rm{N.C.} \longleftrightarrow \rm{zwaartepunt} \, \rm{afschuivend} \, \rm{deel} } \\
&= \left( 125 \cdot 100 \right) \cdot -\cfrac{125}{2}\\
&= -781250 \, \rm{mm^3}
\end{align*}
$$

Het traagheidsmoment van de volledige doorsnede is:

$$
\begin{align*}
I_{zz} &= \cfrac{b \, h^3}{12} \\
&= \cfrac{100 \cdot 250^3}{12} \\
&= 130208333.\bar{3} \, \rm{mm^4}
\end{align*}
$$

Daarmee kunnen we de maximale schuifspanning bepalen:

$$
\begin{align*}
\left| \tau_{\rm{max}} \right| &= \cfrac{\left|V_{z} \, S_{z}^{\rm{a}}\right|}{b \, I_{zz}} \\
&= \cfrac{\left| 4000 \, \cdot -781250 \right|}{100 \cdot 130208333.\bar{3}} \\
&= 0.24 \, \rm{MPa}
\end{align*}
$$

De dwarskracht op deze negatieve snede is omhoog, dus zal de schuifspanning ook omhoog zijn. 

::::

% solution_end

::::{question} Opgave
:variant: multiple-select
:admonition:
:class: exercise
:nocaption:
:columns: 1 1 1 1

Waar is de absolute schuifspanning maximaal?
---
[ ] Op een negatieve snede tussen $ \rm{A} $ en $ \rm{S} $
> Heb je ook de dwarskracht berekend op de andere punten? Is de schuifspanning maximaal waar de dwarskracht maximaal is?
[ ] Op een positieve snede tussen $ \rm{A} $ en $ \rm{S} $
> Heb je ook de dwarskracht berekend op de andere punten? Is de schuifspanning maximaal waar de dwarskracht maximaal is?
[x] Op een positieve snede net links van $ \rm{B} $
[x] Op een negatieve snede net rechts van $ \rm{B} $
[ ] Op een positieve snede net rechts van $ \rm{B} $
> Heb je ook de dwarskracht berekend op de andere punten? Is de schuifspanning maximaal waar de dwarskracht maximaal is?
[ ] Op een negatieve snede net links van $ \rm{B} $
> Heb je ook de dwarskracht berekend op de andere punten? Is de schuifspanning maximaal waar de dwarskracht maximaal is?
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De dwarskracht is de enige parameter voor de schuifspanning die verandert over de lengte van de constructie, dus waar deze het grootst is zal de absolute schuifspanning maximaal zijn. 

Evenwicht geeft de volgende dwarskrachtenlijn:

```{figure} ./lesoefening2/dwarskrachtenlijn.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect_oef
:number:
```

Dus de absolute schuifspanning is maximaal op een positieve en negatieve snede net links van $\rm{B}$.

::::

% solution_end

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:

---
M[0.348]
^^^
?
De maximale absolute schuifspanning is {gap} $\rm{MPa}$
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De eerder berekende $S_{z}^{\rm{a}}$ en $I_{zz}$ kunnen worden gebruikt om de absolute maximale schuifspanning te vinden in de constructie.

$$
\begin{align*}
\left| \tau_{\rm{max}} \right| &= \cfrac{\left|V_{z} \, S_{z}^{\rm{a}}\right|}{b \, I_{zz}} \\
&= \cfrac{\left| 5800 \, \cdot -781250 \right|}{100 \cdot 130208333.\bar{3}} \\
&= 0.348 \, \rm{MPa}
\end{align*}
$$

::::

% solution_end