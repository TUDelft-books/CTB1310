# Voorbeeld

::::{grid} 1 1 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/voorbeeld_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
:figclass: sticky-margin
```

:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/voorbeeld_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
:figclass: sticky-margin
```

:::

::::

:::{container} sticky-margin

Bepaal het schuifspanningsverloop op een positieve snede in $\rm{D}$.

:::

::::::::::{steps}
:::::::::{step} Bereken de dwarskracht.

Allereerst bepalen we de dwarskracht in doorsnede $\rm{D}$. Daarvoor bepalen we eerst de oplegreacties:

```{figure} ./instructie_data/oplegreacties.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

$$
\left. \sum T \right| _{\rm{B}} = 0 \to A_{\rm{v}} = 3 \, \rm{kN} \left(↑\right)
$$

Daarmee kunnen we de dwarskracht in $\rm{D}$ bepalen op een positieve snede:

```{figure} ./instructie_data/FBD_D.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

$$
\sum F_{\rm{v}} = 0 \to V_{\rm{D}} = 30 \, \rm{kN} \negativeshear
$$

:::::::::
:::::::::{step} Bepaal de schuifspanning op een aantal karakteristieke afschuivende delen

Nu kunnen we de schuifspanningen bepalen op karakteristieke afschuivende delen in de doorsnede.

Op de boven en onderzijde is de schuifspanning $0$.

Aangezien we een rechthoekige doorsnede hebben weten we dat het schuifspanningsverloop parabolisch is met een maximum ter hoogte van het normaalkrachtencentrum. Daarom wordt op dat punt de maximale schuifspanning bepaald waarmee het hele schuifspanningsverloop gedefinieerd is.

De afschuivende deel van de doorsnede is dus het volgende (getekend op het dwarsvlak $y,z$, met nog onbekende spanningen):

```{figure} ./instructie_data/afschuivend_deel.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

Het statisch moment van het dwarsoppervlakte van dit afschuivende deel is ten opzichte van het normaalkrachtencentrum (precies in het midden):

$$
\begin{align*}
S_{z}^{\rm{a}} &= A_{\rm{afschuivend} \, \rm{deel}} \, z_{\rm{N.C.} \longleftrightarrow \rm{zwaartepunt} \, \rm{afschuivend} \, \rm{deel} } \\
&= \left( 90 \cdot 62.25 \cdot 2\right) \cdot -\cfrac{90}{2}\\
&= -506250 \, \rm{mm^3}
\end{align*}
$$

Het traagheidsmoment van de volledige doorsnede is:

$$
\begin{align*}
I_{zz} &= \cfrac{b \, h^3}{12} \\
&= \cfrac{125 \cdot 180^3}{12} \\
&= 60750000 \, \rm{mm^4}
\end{align*}
$$

Daarmee kunnen we de maximale schuifspanning bepalen:

$$
\begin{align*}
\left| \tau_{\rm{max}} \right| &= \cfrac{\left|V_{z} \, S_{z}^{\rm{a}}\right|}{b \, I_{zz}} \\
&= \cfrac{\left| 30000 \, \cdot -506250 \right|}{125 \cdot 60750000} \\
&= 2 \, \rm{MPa}
\end{align*}
$$

:::::::::
:::::::::{step} Leid het teken van de schuifspanningen af aan de hand van de richting van de snedekracht.

Deze schuifspanning moet omhoog lopen, overeenkomend met de richting van de snedekracht.

:::::::::
:::::::::{step} Teken het schuifspanningsprofiel in het 2D.

Dat geeft het volgende schuifspanningsverloop in de doorsnede:

```{figure} ./instructie_data/antwoord.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Schuifspanningsverloop op positieve snede in $\rm{D}$.
```

:::::::::
::::::::::