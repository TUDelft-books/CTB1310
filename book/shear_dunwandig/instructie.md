# Instructie

De vorige keer hebben we gekeken naar [schuifspanningen in dikwandige doorsnedes](../shear/instructie.md). In deze instructie breiden we dat uit naar schuifspanningen in dunwandige doorsnedes.

## Implicaties model schuifspanningen voor dunwandige doorsneden

Voor dunwandige doorsneden geldt dat de wanddikte klein is ten opzichte van de andere afmetingen van de doorsnede. Dit heeft tot gevolg dat overal wordt voldaan aan de voorwaarde $h \gg b$ en $R \gg b$ en lopen de schuifspanningen altijd evenwijdig aan de wand. Daarmee kunnen we ook in een knooppunt waar meerdere constructiedelen bij elkaar komen de schuifspanningen berekenen, in tegenstelling tot dikwandige doorsnedes. Dus kan de schuifspanning in de gehele doorsnede worden bepaald.

::::{grid} 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/overal_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

Ook in de uiteindes van de flenzen  
en in de knooppunten tussen flens  
en lijf kunnen schuifspanningen  
worden bepaald terwijl bij een  
dikwandige doorsnede hier complexe  
spanningsverdelingen optreden.

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/overal_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

Ook in de de hoekpunten kunnen de  
schuifspanningen worden bepaald  
terwijl bij een dikwandige  
doorsnede hier complexe  
spanningsverdelingen optreden.

```{figure-end}
```

:::

::::

Omdat we nu de schuifspanning in de volledige continue doorsnede kunnen bepalen met ons schuifspanningsmodel kunnen we de schuifspanning zien als een 'stroom' van de dwarskracht door de doorsnede. Aangezien de dwarskracht de resultante is van de schuifspanningen kan de richting van de schuifspanning in elk van de doorsnededelen worden afgeleid zonder een berekening te maken.

::::{grid} 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/richting_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

In het lijf moet de schuifspanning  
naar beneden lopen als er een  
dwarskracht omlaag werkt. Om een  
symmetrisch stroom te krijgen moet  
de schuifspanningen in de bovenste  
flenzen naar binnen en in de  
onderste flenzen naar buiten lopen.

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/richting_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

In het linker lijf kan de grootste  
verticale kracht optreden (ter hoogte  
van het normaalkrachtencentrum), dus  
bij een dwarskracht omlaag moet de  
schuifspanning in dat lijf naar  
beneden lopen. De richting van de  
schuifspanningen in de flenzen en in  
het rechter lijf volgt dan uit de  
stroming van de schuifspanning.

```{figure-end}
```

:::

::::

## Voorbeeld

Het bepalen van de schuifspanningen voor een dunwandige doorsnede wordt getoond op onderstaande voorbeeld.

::::::{prf:example}
:nonumber: true

Gegeven is de volgende constructie en doorsnede:

::::{grid} 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/doorsnede.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

De doorsnede mag als dunwandig worden beschouwd.

```{figure-end}
```

:::

::::

Gevraagd is het schuifspanningsverloop op een negatieve snede.

Zonder een berekening te maken kunnen we al wat zeggen over de schuifspanningen in de verschillende delen van de doorsnede:
- Vanwege symmetrie moet de schuifspanning middenin de flens gelijk zijn aan $0$.
- Dat geldt ook voor de vrije uiteindes van zowel de flens als het lijf.
- De horizontale flens zal een lineair verloop van de schuifspanning hebben in de horizontale richting.
- Het verticale lijf zal een parabolisch verloop van de schuifspanning hebben in de verticale richting.
- Het maximum van de schuifspanning zit ter hoogte van het normaalkrachtencentrum omdat daar het statisch moment van het afschuivend gedeelte het grootst is.
- De dwarskracht met vervormingsteken ⎽|⎺ zorgt voor een dwarskracht omhoog op een negatieve snede.
- Vanwege de stroming van de schuifstroom zal de schuifspanning vanuit in het lijf vanuit de flenzen naar buiten en binnen stromen en afnemen.

```{figure} ./instructie_data/verloop.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

Om de daadwerkelijke waardes te berekenen beginnen we met het bepalen van de doorsnedegrootheden, startend met het oppervlakte $A$.

$$
A = 200 \cdot 4 + 2 \cdot 4 \cdot 150 = 2000 \, \rm{mm^2}
$$

Vervolgens kunnen we het zwaartepunt/normaalkrachtencentrum bepalen.

$$
\bar{z}_{\rm{N.C.}} = \cfrac{2 \cdot 150 \cdot 4 \cdot \cfrac{150}{2}}{2000} = 45 \, \rm{mm}
$$

Daarmee kan het traagheidsmoment $I_{zz}$ worden bepaald.

$$
\begin{align*}
I_{zz} = &  \,\cfrac{1}{12} \cdot 200 \cdot 4^3 + 200 \cdot 4\ \cdot \left(-45\right)^2 \\
& + 2 \cdot \left( \cfrac{1}{12} \cdot 4 \cdot 150^3 + 4 \cdot 150 \cdot 
\left( \cfrac{150}{2} -45 \right)^2 \right)\\
\approx & \, 4.95 \cdot 10^6 \, \rm{mm^4}
\end{align*}
$$

Uit het eerder bepaalde verloop blijkt dat een aantal punten interessant zijn om de schuifspanning te bepalen:
- Ter hoogte van het normaalkrachtencentrum
- Rondom de aansluiting van het lijf met de flens

Beginnend met de schuifspanning ter hoogte van het normaalkrachtencentrum, waarbij één van de twee lijven wordt doorgesneden:

```{figure} ./instructie_data/snede1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig

Afschuifvlak ter hoogte van het normaalkrachtencentrum.
```


$$
S_{z}^{\rm{a}} = 4 \cdot \left(150 - 45 \right) \cdot \cfrac{\left(150 - 45 \right)}{2} = 22050 \, \rm{mm^3} \\
\tau = \cfrac{\left| V \, S_{z}^{\rm{a}} \right| }{I_{zz} \, t} \approx \cfrac{\left| 9900 \cdot 22050\right|}{4 \cdot  4.95 \cdot 10^6 } \approx 11 \, \rm{MPa}
$$

Vervolgens net onder de aansluiting van het lijf met de flens, waarbij wederom één van de twee lijven wordt doorgesneden:

```{figure} ./instructie_data/snede2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig

Afschuifvlak net onder de aansluiting van het lijf met de flens.
```

$$
S_{z}^{\rm{a}} = 4 \cdot 150 \cdot \left(\cfrac{150}{2}-45\right) = 18000 \, \rm{mm^3} \\
\tau = \cfrac{\left| V \, S_{z}^{\rm{a}} \right| }{I_{zz} \, t} \approx \cfrac{\left| 9900 \cdot 18000\right|}{4 \cdot  4.95 \cdot 10^6 } \approx 9.0 \, \rm{MPa}
$$

Vervolgens nemen we een afschuifvlak net links van de linker aansluiting van het lijf met de flens, waarbij nu de flens wordt doorgesneden:

```{figure} ./instructie_data/snede3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig

Afschuifvlak net links van de linker aansluiting van het lijf met de flens.
```

$$
S_{z}^{\rm{a}} = 4 \cdot 50 \cdot \left(-45\right) = -9000 \, \rm{mm^3} \\
\tau = \cfrac{\left| V \, S_{z}^{\rm{a}} \right| }{I_{zz} \, t} \approx \cfrac{\left| 9900 \cdot -9000\right|}{4 \cdot  4.95 \cdot 10^6 } \approx 4.5 \, \rm{MPa}
$$

En tot slot het afschuifvlak net rechts van de linker aansluiting van het lijf met de flens, wederom met de flens doorgesneden:

```{figure} ./instructie_data/snede4.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig

Afschuifvlak net rechts van de linker aansluiting van het lijf met de flens.
```

$$
S_{z}^{\rm{a}} = 18000-9000 = 9000 \, \rm{mm^3} \\
\tau = \cfrac{\left| V \, S_{z}^{\rm{a}} \right| }{I_{zz} \, t} \approx \cfrac{\left| 9900 \cdot 9000\right|}{4 \cdot  4.95 \cdot 10^6 } \approx 4.5 \, \rm{MPa}
$$

Dit geeft dus het volgende schuifspanningsverloop:

```{figure} ./instructie_data/conclusie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig

Schuifspanningsverloop
```

::::::

## Meer voorbeelden
In hoofdstuk 5.4.2 en 5.4.3 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` worden meer voorbeelden gegeven van het bepalen van schuifspanningen in verschillende situaties.

% ## Instructies in collegevorm
%
% Dit onderwerp is [les ...](...) gepresenteerd in collegevorm tot ....

## Oefeningen
Opgaves 5.33 - 5.46 in hoofdstuk 5 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013`. Antwoorden zijn [hier](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol2/Chapter5/) beschikbaar.