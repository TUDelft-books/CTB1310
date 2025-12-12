# Instructie

Tot nu toe hebben we enkel gerekend aan normaalspanningen, en enkel door buiging en verlenging/verkorting. Tijdens buiging treden er echter ook schuifspanningen op in de doorsnede: schuifspanningen die langs een een snede werken in plaats van loodrecht daarop. Dit is voor te stellen door twee op elkaar liggende balken te beschouwen die doorbuigen. Als je deze twee balken aan elkaar zou willen lijmen zodat deze werken als één balk zouden schuifspanningen nodig zijn die de vervormingen door buiging enigszins tegengaan:

```{figure} ./instructie_data/stacked.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Twee op elkaar liggende balken. Voor het samenvoegen zouden schuifspanningen nodig zijn zoals rechts getoond.
```

## Model

Voor het bepalen van schuifspanningen kijken we naar het evenwicht van een infinitesimaal (oneindig kleine afmetingen) stukje van een balk

```{figure} ./instructie_data/beam_section.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Infinitesimaal stukje balk van lengte $\Delta x$ met daarop snedekrachten $V_z$ en $M_z$. Het moment op de rechter doorsnede is $\Delta M$ groter dan dat op de linker doorsnede.
```

We kunnen de spanningen bepalen op de doorsnedes. De schuifspanningen zijn nog onbekend, maar voor de normaalspanningen geldt de eerder afgeleide formule $\sigma = \cfrac{M_z z}{I_{zz}}$.

```{figure} ./instructie_data/spanningen_section.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Boven de nog onbekende schuifspanningen. Onder de normaalspanningen.
```

::::::{prf:assumption}
:nonumber: true

We negeren de afschuifvervorming, enkel de vervormingen door extensie / buiging nemen we mee in de daaruit volgende normaalspanningen. De schuifspanningen en afschuifvervorming zijn dus niet één-op-één gerelateerd in ons model, waar dat bij normaalspanningen wel het geval is.

```{figure} ./instructie_data/afschuiving.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Een infinitesimaal (oneindig kleine afmetingen) blokje dat wordt belast door schuifspanningen en normaalspanningen kan vervormen door zowel afschuiving als extensie, maar in ons model nemen we enkel de extensie mee om de schuifspanningen te bepalen.
```

De aannames die we hebben gebruikt voor normaalspanningen zijn dus nog steeds geldig:
- De doorsnedes blijven vlak en loodrecht op 'vezels' staan, waarmee het rekverloop lineair is
- Normaalspanningen en -rekken hebben een lineair verband, waarmee de vorm van het spanningsverloop gelijk is aan die van het rekverloop.

Tijdens de afleiding van de formules voor normaalspanningen werden daarnaast nog een aantal aannames gedaan. Aangezien we door gaan bouwen op hetzelfde model, zullen deze aannames ook gelden voor schuifspanningen:
- Het assenstelsel grijpt aan in het normaalkrachtencentrum van de doorsnede. Hierdoor vervallen de statisch momenten $S_y$ en $S_z$ in de vergelijkingen.
- De doorsnede is symmetrisch in de $y$- en/of $z$-richting / krachten grijpen aan in de hoofdassen van de doorsnede. Hierdoor vervallen de termen met $I_{yz}$ en zijn spanniningen in de $y$- en $z$-richting onafhankelijk van elkaar.
- De doorsnede heeft een homogene verdeling van rekstijfheid $E$, waarmee de locatie van het normaalkrachtencentrum en traagheidsmomenten onafhankelijk van de rekstijfheid bepaald kunnen worden en de rekverdeling gelijk is van vorm aan de spanningsverdeling.

::::::

Nu stellen we een vrijlichaamsschema op met spanningen voor een deel van de doorsnede, het zogenaamde afschuivend deel. Hierop werken dezelfde spanningen, met op het doorgesneden vlak geen normaalspanning maar wel een mogelijk schuifspanning. Deze doorsnede heeft ook een dikte: $b$ is de dikte van de doorsnede in de dwarsrichting $y$. $A^{\rm{a}}$ is het oppervlakte van de linker en rechter doorsnede, $A^{\parallel}$ is het oppervlakte van de onderste doorsnede

```{figure} ./instructie_data/spanningen_afschuivend.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Spanningen op een afschuivend deel van de doorsnede.
```

Door het evenwicht in de langsrichting op te stellen, kunnen we de schuifspanning bepalen:

$$
\sum F_x = 0 \to \tau_{\rm{gem}} \left( z \right) = -\cfrac{V_{z} \, S_{z}^{\rm{a}} \left( z \right)}{b \left(z \right) \, I_{zz}}
$$

Met:
- $\tau_{\rm{gem}} \left( z \right)$: de gemiddelde schuifspanning op hoogte $z$ in de doorsnede
- $V_{z}$: de snedekracht in de $z$-richting
- $S_{z}^{\rm{a}} \left( z \right)$: het statisch moment van het afschuivende deel van de doorsnede ten opzichte van de $y$-as op hoogte $z$
- $b \left(z \right)$: de dikte van de doorsnede in de $y$-richting op hoogte $z$
- $I_{zz}$: het traagheidsmoment van de volledige doorsnede in de $z$-richting


::::::{prf:assumption}
:nonumber: true

Om het evenwicht op te stellen kunnen we alleen de resulterende schuifkracht bepalen, de verdeling is daarmee onbekend. We kunnen daarmee alleen maar de gemiddelde schuifspanning bepalen. Voor doorsnedes in het $xy$ vlak blijkt deze gemiddelde schuifspanning terecht als de breedte van de doorsnede veel kleiner is dan de hoogte van de doorsnede.

Daarnaast gaan we in deze berekeningen uit van dezelfde $I_{zz}$ in de linker en rechter doorsnede, wat betekent dat we aannemen dat de doorsnede niet verandert over de lengte van de balk; dus een prismatische balk.

::::::

::::::{admonition} Volledige afleiding
:class: notation, dropdown

$$
\begin{align*}
\sum F_x &= 0 \\
-\int_{A^{\rm{a}}} \sigma_{\rm{linker} \, \rm{doorsnede}} \, dA^{\rm{a}} + \int_{A^{\rm{a}}} \sigma_{\rm{rechter} \, \rm{doorsnede}}  \, dA^{\rm{a}} + \int_{A^{\parallel}} \tau \left( x\right) \, dA^{\parallel} &= 0 \\
\underbrace{-\int_{A^{\rm{a}}} \cfrac{M_z \, z}{I_{zz,\rm{linker} \, \rm{doorsnede}}} \, dA^{\rm{a}} + \int_{A^{\rm{a}}} \cfrac{M_z \, z}{I_{zz,\rm{rechter} \, \rm{ doorsnede}}} \, dA^{\rm{a}}}_{\rm{Als} \, I_{zz,\rm{linker} \, \rm{doorsnede}} = I_{zz,\rm{linker} \, \rm{doorsnede}}=I_{zz} \rm{vervallen} \, \rm{deze} \, \rm{termen}} + \int_{A^{\rm{a}}} \cfrac{\Delta M_z \,z}{I_{zz}} \, dA^{\rm{a}} + \int_{A^{\parallel}} \tau \left( x\right) \, dA^{\parallel} &= 0 \\
 \int_{A^{\rm{a}}} \cfrac{\Delta M_z \,z}{I_{zz}} \, dA^{\rm{a}} + \underbrace{\int_{A^{\parallel}} \tau \left( x\right) \, dA^{\parallel}}_{\rm{Als} \, \tau \left( x\right) = \tau_{\rm{gem}} \, \text{kan} \, \rm{deze} \, \rm{uit} \, \rm{de} \, \rm{integraal} \, \rm{worden} \, \rm{gehaald} } &= 0 \\
\cfrac{\Delta M_z}{I_{zz}} \int_{A^{\rm{a}}} z \, dA^{\rm{a}} + \tau_{\rm{gem}} \int_{A^{\parallel}} \, dA^{\parallel} &= 0 \\
\cfrac{\Delta M_z}{I_{zz}} S_{z}^{\rm{a}}\left(z \right) + \tau_{\rm{gem}} A^{\parallel} &= 0 \\
\cfrac{\Delta M_z}{I_{zz}} S_{z}^{\rm{a}}\left(z \right) + \tau_{\rm{gem}} \, b \left(z \right) \, \Delta x &= 0 \\
\lim_{\Delta x \to 0} \tau_{\rm{gem}} &= \lim_{\Delta x \to 0} \cfrac{- \cfrac{\Delta M_z}{\Delta x} \, S_{z}^{\rm{a}}\left(z \right)}{b \left(z \right) \, I_{zz}} \\
\underbrace{\tau_{\rm{gem}} \left(z \right)}_{\rm{In} \, \rm{een} \, \rm{doorsnede} \, \rm{is} \, \rm{de} \, \rm{schuifspanning} \, \rm{dus} \, \rm{variabel} \, \rm{in} \, z} &= -\cfrac{V_z \, S_{z}^{\rm{a}}\left(z \right)}{b \left(z \right) \, I_{zz}}
\end{align*}
$$

::::::

We kunnen ook de schuifspanning op de linker en rechter doorsnede vinden. Dit kunnen we doen door het momentenevenwicht van de schuifspanningen te bekijken op een infinitesimaal (oneindig kleine afmetingen) blokje. De schuifspanningen zijn beschreven met index-notatie, waarbij de eerste index de normaalrichting van het vlakje aangeeft waar de spanning op werkt en de tweede index de richting van de werklijn van de spanning.

```{figure} ./instructie_data/blokje.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Infinitesimaal blokje met schuifspanningen.
```

$$
\begin{align*}
\left. \sum T \right|_{\rm{A}} &= 0 \\
\underbrace{\sigma_{zx} \, \Delta x}_{\rm{Resultante} \, \rm{kracht} \, \rm{op} \, \rm{vlakje} \, z} \, \underbrace{\Delta z}_{\rm{Arm} \, \rm{ten} \, \rm{opzichte} \, \rm{van} \, \rm{A}} - \underbrace{\sigma_{xz} \, \Delta x}_{\rm{Resultante} \, \rm{kracht} \, \rm{op} \, \rm{vlakje} \, x} \,  \underbrace{\Delta z}_{\rm{Arm} \, \rm{ten} \, \rm{opzichte} \, \rm{van} \, \rm{A}} = 0 \\
\sigma_{zx} &= \sigma_{xz} \\
\end{align*}
$$

Dus de schuifspanningen op een zijde $90^\circ$ ten opzichte van elkaar zijn gelijk van grootte en wijzen naar elkaar toe of van elkaar af. Deze worden daarom ook wel genoteerd met een algemene $\tau$ in plaats van $\sigma$ met subscripten.

Dat betekent dus dat de schuifspanningen op de linker en rechter doorsnede ter hoogte van de snede in de richting van $x$ gelijk zijn aan de schuifspanning in de $x$-richting:

```{figure} ./instructie_data/conclusie_afschuivend.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Spanningen op afschuivend deel van de doorsnede.
```

De schuifspanningsformule beschrijft dus de schuifspanningen zowel in langsrichting $x$ als in het doorsnedevlak $yz$


## Eigenschappen schuifspanningsmodel

Vanwege de aanname dat de schuifspanning gemiddeld verdeeld is over de langsrichting van het afschuivende deel van de doorsnede, geldt dat de formule alleen een geldig antwoord geeft als een afschuivend deel wordt genomen waarin de schuifspanning daadwerkelijk constant is. Het blijkt dat dit alleen geldig is als de breedte van de doorsnede veel kleiner is dan de hoogte. Als we zo'n doorsnede hebben moet het snedevlak dan symmetrisch en dwars op de randen van de doorsnede genomen:

```{figure} ./instructie_data/constant.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Het afschuivend deel van de doorsnede moet symmetrisch en dwars op de randen van de doorsnede genomen worden om een constante schuifspanning te garanderen.
```

Daarnaast is voor de vorm van het schuifspanningsverloop in de doorsnede af te leiden dat bij een doorsnede met constante dikte $b$ de schuifspanning maximaal is ter hoogte van het normaalkrachtencentrum. Daarnaast verloop deze voor rechthoekige doorsnedes parabolisch.

```{figure} ./instructie_data/parabolisch.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Parabolisch verloop van schuifspanningen met maximum ter hoogte van het normaalkrachtencentrum.
```

::::::{admonition} Volledige afleiding
:class: notation, dropdown

Om het schuifspanningsverloop te bepalen, kunnen we de formule voor de gemiddelde schuifspanning herschrijven door het statisch moment uit te werken voor een constante dikte $b$:

$$
\begin{align*}
\tau_{\rm{gem}} \left(z \right) &= -\cfrac{V_z \, S_{z}^{\rm{a}}\left(z \right)}{b \, I_{zz}} \\
\tau_{\rm{gem}} \left(z \right) &= -\cfrac{V_z \, \int_{A^{\rm{a}}} z \, dA^{\rm{a}} }{b \, I_{zz}} \\
\tau_{\rm{gem}} \left(z \right) &= -\cfrac{V_z \, b \int z \, dz }{b \, I_{zz}} \\
\tau_{\rm{gem}} \left(z \right) &= -\cfrac{V_z \, \left(z^2 + \underbrace{C}_{\rm{integration} \, \rm{constant}} \right)}{\, I_{zz}}
\end{align*}
$$

Het statisch moment is maximaal ter hoogte van het normaalkrachtencentrum, waar $z=0$. Dus daar is ook de schuifspanning maximaal.

::::::

Daarnaast leidt de relatie $\sigma_{zx} = \sigma_{xz}$ ook tot de conclusie dat de schuifspanningen dwars op de vrije randen van een doorsnede nul moeten zijn, omdat er daar geen evenwicht kan zijn met een andere spanning.

```{figure} ./instructie_data/randen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Spanningen op randen zijn nul loodrecht op de rand.
```

Tot slot kunnen we de formule simplificeren door het teken direct te relateren aan de richting van de snedekracht. De resultante van de schuifspanning werkt namelijk altijd in de richting van de snedekracht. We kunnen daarmee de formule herschrijven naar: $\tau_{\rm{gem}} \left( z \right) = \left| \cfrac{V_{z} \, S_{z}^{\rm{a}} \left( z \right)}{b \left(z \right) \, I_{zz}} \right|$.

```{figure} ./instructie_data/richtingen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Resultante van schuifspanningen komt overeen met richting van snedekracht. Normaalspanningen zijn niet getoond.
```

Daarmee kunnen we de volgende aanpak beschrijven voor het bepalen van het schuifspanningsverloop in een doorsnede:

::::::{prf:algorithm} Bepalen schuifspanningsverloop in een doorsnede
:nonumber: true

1. Bereken de snedekracht $V_z$ in de doorsnede.
2. Neem een aantal karakteristieke afschuivend delen waarin de schuifspanningen constant zijn en bepaal de schuifspanningen op deze delen met $\tau_{\rm{gem}} \left( z \right) = \left| \cfrac{V_{z} \, S_{z}^{\rm{a}} \left( z \right)}{b \left(z \right) \, I_{zz}} \right|$. Het afschuivende deel door het normaalkrachtencentrum geeft de maximale schuifspanning. Leidt het teken af van de schuifspanningen af aan de hand van de richting van de snedekracht.
3. Teken het schuifspanningsprofiel in bijvoorbeeld het $x,z$-assenstelsel. Voor een rechthoekige doorsnede verloopt dit parabolisch.

::::::

## Voorbeeld

Het bepalen van de wringende momentenlijn wordt getoond op onderstaande voorbeeld.

::::::{prf:example}
:nonumber: true

```{figure} ./instructie_data/voorbeeld.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Voorbeeldconstructie
```

Gevraagd is het schuifspanningsverloop op een positieve snede in $\rm{D}$.

Allereerst bepalen we de dwarskracht in doorsnede $\rm{D}$. Daarvoor bepalen we eerst de oplegreacties:

```{figure} ./instructie_data/oplegreacties.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Vrijlichaamsschema van de gehele constructie.
```

$$
\left. \sum T \right| _{\rm{B}} = 0 \to A_{\rm{v}} = 3 \, \rm{kN} \left(↑\right)
$$

Daarmee kunnen we de dwarskracht in $\rm{D}$ bepalen op een positieve snede:

```{figure} ./instructie_data/FBD_D.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Vrijlichaamsschema van linker deel van constructie doorgesneden in $\rm{D}$.
```

$$
\sum F_{\rm{v}} = 0 \to V_{\rm{D}} = 3 \, \rm{kN} \left(⎽|⎺\right)
$$

Nu kunnen we de schuifspanningen bepalen op karakteristieke afschuivende delen in de doorsnede. Op de boven en onderzijde is de schuifspanning $0$ en aangezien we een rechthoekige doorsnede hebben weten we dat het schuifspanningsverloop parabolisch is met een maximum ter hoogte van het normaalkrachtencentrum. Daarom wordt op dat punt de maximale schuifspanning bepaald waarmee het hele schuifspanningsverloop gedefinieerd is. Het normaalkrachtencentrum bevindt zich in het zwaartepunt van de doorsnede, wat voor een rechthoek precies in het midden is.

```{figure} ./instructie_data/afschuivend_deel.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Afschuivend deel door het normaalkrachtencentrum.
```

Het statisch moment van dit afschuivende deel is:

$$
\begin{align*}
S_{z}^{\rm{a}} \left( 0 \right) &= A_{\rm{afschuivend} \, \rm{deel}} \, z_{\rm{N.C.} \longleftrightarrow \rm{zwaartepunt} \, \rm{afschuivend} \, \rm{deel} } \\
&= \left( 90 \cdot 62.25 \cdot 2\right) \cdot \cfrac{90}{2}\\
&= 506250 \, \rm{mm^3}
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
\tau_{\rm{max}} &= \left| \cfrac{V_{z} \, S_{z}^{\rm{a}} \left( 0 \right)}{b \, I_{zz}} \right| \\
&= \left| \cfrac{3000 \, \cdot 506250}{125 \cdot 60750000} \right| \\
&= 20 \, \rm{MPa}
\end{align*}
$$

Dat geeft het volgende schuifspanningsverloop in de doorsnede:

```{figure} ./instructie_data/antwoord.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Schuifspanningsverloop op positieve snede in $\rm{D}$.
```

## Alternatieve afleiding
In hoofdstuk 5.1 en 5.3 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` wordt een alternatief model afgeleid gegeven voor het bepalen van schuifspanningen.

## Meer voorbeelden
In hoofdstuk 5.2 en 5.4.1 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` worden meer voorbeelden gegeven van het bepalen van schuifspanningen in verschillende situaties. Negeer voorbeeld 5.2.2 - 5.2.4 en voorbeeld 2 in 5.4.1.

% ## Instructies in collegevorm
%
% Dit onderwerp is [les ...](...) gepresenteerd in collegevorm tot ....

## Oefeningen
Opgaves 5.2b, 5.3, 5.13 - 5.28, 5.69 en 5.71 in hoofdstuk 5 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013`. Antwoorden zijn [hier](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol2/Chapter6/) beschikbaar.