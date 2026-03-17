# Begeleide oefening 1

In [](./instructie.md) is het schuifspanningsverloop op een positieve snede in doorsnede $\rm{D}$ gevonden voor de volgende constructie:

```{figure} ./instructie_data/voorbeeld.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::::{exercise}
:nonumber: true

Wat zijn de schuifspanningen op een aantal andere punten?

```{h5p} https://tudelft.h5p.com/content/1292769916977998897/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

Deze opgave vraagt naar de schuifspanningen op verschillende punten in doorsnede $\rm{D}$ van de constructie uit de instructie.

De constructie heeft de volgende eigenschappen:
- Belasting: $F = 60 \, \rm{kN}$
- Dwarskracht in $\rm{D}$: $V_{\rm{D}} = 30 \, \rm{kN}$
- Breedte doorsnede: $b = 125 \, \rm{mm}$
- Hoogte doorsnede: $h = 180 \, \rm{mm}$
- Traagheidsmoment: $I_{zz} = \cfrac{b h^3}{12} = 60.75 \cdot 10^6 \, \rm{mm^4}$

**Maximale schuifspanning (in het normaalkrachtencentrum)**

Het statisch moment van het afschuivend deel door het normaalkrachtencentrum:

$$
\begin{align*}
S_{z}^{\rm{a}} &= A_{\rm{afschuivend}} \cdot z_{\rm{zwaartepunt}} \\
&= \left( 125 \cdot 90 \right) \cdot \cfrac{90}{2} \\
&= 506250 \, \rm{mm^3}
\end{align*}
$$

De maximale schuifspanning:

$$
\begin{align*}
\tau_{\rm{max}} &= \cfrac{V_z \, S_{z}^{\rm{a}}}{b \, I_{zz}} \\
&= \cfrac{30000 \cdot 506250}{125 \cdot 60.75 \cdot 10^6} \\
&= 2.0 \, \rm{MPa}
\end{align*}
$$

**Schuifspanning op $z = 45 \, \rm{mm}$ van het normaalkrachtencentrum**

Het statisch moment van het afschuivend deel op $z = 45 \, \rm{mm}$:

$$
\begin{align*}
S_{z}^{\rm{a}} &= b \cdot (h/2 - z) \cdot \cfrac{z + h/2}{2} \\
&= 125 \cdot (90 - 45) \cdot \cfrac{45 + 90}{2} \\
&= 379687.5 \, \rm{mm^3}
\end{align*}
$$

De schuifspanning op deze locatie:

$$
\begin{align*}
\tau &= \cfrac{V_z \, S_{z}^{\rm{a}}}{b \, I_{zz}} \\
&= \cfrac{30000 \cdot 379687.5}{125 \cdot 60.75 \cdot 10^6} \\
&= 1.5 \, \rm{MPa}
\end{align*}
$$

**Locatie waar schuifspanning $\tau = 0.38 \, \rm{MPa}$**

We zoeken de waarde van $z$ waarbij $\tau = 0.38 \, \rm{MPa}$:

$$
\begin{align*}
\tau &= \cfrac{V_z \, S_{z}^{\rm{a}}}{b \, I_{zz}} \\
0.38 \cdot 10^6 &= \cfrac{30000 \cdot 125 \cdot (90 - z) \cdot \cfrac{z + 90}{2}}{125 \cdot 60.75 \cdot 10^6}
\end{align*}
$$

Dit geeft een kwadratische vergelijking met oplossingen:

$$
z = \pm 81 \, \rm{mm}
$$

Dit betekent dat de schuifspanning van $0.38 \, \rm{MPa}$ optreedt op $81 \, \rm{mm}$ boven en onder het normaalkrachtencentrum.

::::

% solution_end
