# Begeleide oefening 1

In [](./instructie.md) is het schuifspanningsverloop op een positieve snede in doorsnede $\rm{D}$ gevonden voor de volgende constructie:

```{figure} ./instructie_data/voorbeeld.svg
:align: center
:class: sticky-margin
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

::::{admonition} Uitwerking
:class: solution, dropdown

Gevraagd is het schuifspanningsverloop op een negatieve snede in $\rm{D}$.

Allereerst bepalen we de dwarskracht in doorsnede $\rm{D}$. Daarvoor bepalen we eerst de oplegreacties:

```{figure} ./instructie_data/oplegreacties.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Vrijlichaamsschema van de gehele constructie.
```

$$
\left. \sum T \right| _{\rm{B}} = 0 \to A_{\rm{v}} = 30 \, \rm{kN} \left(↑\right)
$$

Daarmee kunnen we de dwarskracht in $\rm{D}$ bepalen op een negatieve snede:

$$
\sum F_{\rm{v}} = 0 \to V_{\rm{D}} = 30 \, \rm{kN} \left(⎽|⎺\right)
$$

Nu kunnen we de schuifspanningen bepalen op karakteristieke afschuivende delen in de doorsnede. Het punt van de doorsnede waarop we de schuifspanning moeten bepalen heeft de coordinaten: $\rm{y}= 15, \rm{z} = -45$. 

Het statisch moment van dit afschuivende deel is:

$$
\begin{align*}
S_{z}^{\rm{a}} &= A_{\rm{afschuivend} \, \rm{deel}} \, z_{\rm{N.C.} \longleftrightarrow \rm{zwaartepunt} \, \rm{afschuivend} \, \rm{deel} } \\
&= \left( 45 \cdot 62.25 \cdot 2\right) \cdot \left( -45 -\cfrac{45}{2}\right)\\
&= -379687.5 \, \rm{mm^3}
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
\tau_{\rm{max}} &= \cfrac{\left|V_{z} \, S_{z}^{\rm{a}}\right|}{b \, I_{zz}} \\
&= \cfrac{\left| 30000 \, \cdot -379687.5 \right|}{125 \cdot 60750000} \\
&= 1.5 \, \rm{MPa}
\end{align*}
$$

Aangezien de dwarskracht naar beneden wijst in de negatieve snede is de richting van de schuifspanning ook naar beneden.

----

Ook is het spanningsverloop net links van $\rm{C}$ gevraagd op een positieve snede.

Door het berekenen van de opleggingsreacties is de dwarskracht in de snede te bepalen:

$$
\sum F_{\rm{v}} = 0 \to V_{\rm{C_{l}}} = 30 \, \rm{kN} \left(⎺|⎽\right)
$$

Nu kunnen we de schuifspanningen bepalen op karakteristieke afschuivende delen in de doorsnede. Het punt van de doorsnede waarop we de schuifspanning moeten bepalen heeft de coordinaten: $\rm{y}= -40, \rm{z} = 81$. 

Het statisch moment van dit afschuivende deel is:

$$
\begin{align*}
S_{z}^{\rm{a}} &= A_{\rm{afschuivend} \, \rm{deel}} \, z_{\rm{N.C.} \longleftrightarrow \rm{zwaartepunt} \, \rm{afschuivend} \, \rm{deel} } \\
&= \left( 9 \cdot 62.25 \cdot 2\right) \cdot \left( 81 +\cfrac{9}{2}\right)\\
&= 96187.5 \, \rm{mm^3}
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
\tau_{\rm{max}} &= \cfrac{\left|V_{z} \, S_{z}^{\rm{a}}\right|}{b \, I_{zz}} \\
&= \cfrac{\left| 30000 \, \cdot 96187.5 \right|}{125 \cdot 60750000} \\
&= 0.38 \, \rm{MPa}
\end{align*}
$$

Aangezien de dwarskracht naar beneden wijst in de positieve doorsnede is de richting van de schuifspanning ook naar beneden.

::::

% solution_end
