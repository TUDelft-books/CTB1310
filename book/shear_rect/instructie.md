# Instructie

Tot nu toe hebben we enkel gerekend aan normaalspanningen, en enkel door buiging en verlenging/verkorting. Tijdens buiging treden er echter ook schuifspanningen op in de doorsnede: schuifspanningen die langs een een snede werken in plaats van loodrecht daarop.

::::::{prf:example}
:nonumber: true

Dit is voor te stellen door twee op elkaar liggende balken te beschouwen die doorbuigen. Als je deze twee balken aan elkaar zou willen lijmen zodat deze werken als één balk, zouden schuifspanningen nodig zijn die de vervormingen door buiging enigszins tegengaan:

::::{grid} 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/stacked_1.svg
:align: center
:width: 250px
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/stacked_2.svg
:align: center
:width: 250px
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

::::

::::::

## Model

### Evenwicht afschuivende deel
Voor het bepalen van schuifspanningen kijken we naar het evenwicht van een infinitesimaal (oneindig kleine afmetingen) stukje van een balk als lijn van lengte $\Delta x$ met daarop snedekrachten $V_z$ en $M_z$. Het moment op de rechter doorsnede is $\Delta M$ groter dan dat op de linker doorsnede.

```{figure} ./instructie_data/beam_section.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

We kunnen de spanningen bepalen op de doorsnedes. Daarvoor kijken we naar dezelfde lengte $\Delta x$, maar nu de volledige doorsnede in plaats van het lijnmodel. De schuifspanningen zijn nog onbekend, maar voor de normaalspanningen geldt de eerder afgeleide formule $\sigma = \cfrac{M_z z}{I_{zz}}$.

::::{grid} 3
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/spanningen_section-1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

:::{grid-item}
:columns: auto

\+

:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/spanningen_section-2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

::::

::::::{prf:assumption}
:nonumber: true

We negeren de afschuifvervorming ($\gamma$), enkel de vervormingen door extensie / buiging $\varepsilon$ nemen we mee in de daaruit volgende normaalspanningen. De schuifspanningen en afschuifvervorming zijn dus niet één-op-één gerelateerd in ons model, waar dat bij normaalspanningen wel het geval is. Hieronder is een infinitesimaal (oneindig kleine afmetingen) blokje getoond dat wordt belast door schuifspanningen en normaalspanningen. Het zal vervormen door zowel afschuiving $\gamma$ als extensie $\varepsilon$, maar in ons model nemen we enkel de extensie mee om de schuifspanningen te bepalen en negeren we de vervormingen door rek

::::{grid} 3
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/afschuiving-1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```
Spanningen
```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/afschuiving-2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```
Vervormingen door rek en afschuiving
```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/afschuiving-3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```
Vervormingen door enkel rek
```{figure-end}
```

:::

::::

De aannames die we hebben gebruikt voor normaalspanningen zijn dus nog steeds geldig:
- De doorsnedes blijven vlak en loodrecht op 'vezels' staan, waarmee het rekverloop lineair is
- Normaalspanningen en -rekken hebben een lineair verband, waarmee de vorm van het spanningsverloop gelijk is aan die van het rekverloop.

Tijdens de afleiding van de formules voor normaalspanningen werden daarnaast nog een aantal aannames gedaan. Aangezien we door gaan bouwen op hetzelfde model, zullen deze aannames ook gelden voor schuifspanningen:
- Het assenstelsel grijpt aan in het normaalkrachtencentrum van de doorsnede. Hierdoor vervallen de statische momenten $S_y$ en $S_z$ in de vergelijkingen.
- De doorsnede is symmetrisch in de $y$- en/of $z$-richting / krachten grijpen aan in de hoofdassen van de doorsnede. Hierdoor vervallen de termen met $I_{yz}$ en zijn spanniningen in de $y$- en $z$-richting onafhankelijk van elkaar.
- De doorsnede heeft een homogene verdeling van rekstijfheid $E$, waarmee de locatie van het normaalkrachtencentrum en traagheidsmomenten onafhankelijk van de rekstijfheid bepaald kunnen worden en de rekverdeling gelijk is van vorm aan de spanningsverdeling.

::::::

Nu stellen we een vrijlichaamsschema op met spanningen voor een deel van de doorsnede, het zogenaamde afschuivende deel. Hiervoor snijden we de doorsnede door in de lengterichting $x$. Dit afschuivende deel heeft breedte $b \left(z\right)$ en lengte $\Delta x$. $A^{\rm{a}}$ is de oppervlakte van de linker en rechter doorsnede, $A^{\parallel}$ is de oppervlakte van de onderste doorsnede. De spanningen op dit afschuivende deel kunnen ook worden aangegeven in het vrijlichaamsschema. Op de onderste doorsnede werkt mogelijk een schuifspanning, maar geen normaalspanningen:

::::{grid} 3
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/spanningen_afschuivend-1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

:::{grid-item}
:columns: auto

\+

:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/spanningen_afschuivend-2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

::::

Door het evenwicht in de langsrichting op te stellen (zonder de lichtblauwe spanningen $\tau \left(y,z\right)$), kunnen we de gemiddelde schuifspanning bepalen op het afschuivende oppervlakte:

$$
\sum F_x = 0 \to \tau_{\rm{gem}} = -\cfrac{V_{z} \, S_{z}^{\rm{a}} }{b \, I_{zz}}
$$

Met:
- $\tau_{\rm{gem}} $: de gemiddelde schuifspanning op het afschuivende oppervlakte van het afschuivende gedeelte op een hoogte $z$.
- $V_{z}$: de snedekracht in de $z$-richting
- $S_{z}^{\rm{a}}$: het statisch moment van het afschuivende deel van de doorsnede ten opzichte van de $y$-as
- $b$: de totale breedte van het afschuivende vlak.
- $I_{zz}$: het traagheidsmoment van de volledige doorsnede in de $z$-richting

::::::{admonition} Volledige afleiding
:class: notation, dropdown

$$
\begin{align*}
\sum F_x &= 0 \\
-\int_{A^{\rm{a}}_{\rm{links}}} \sigma_{\rm{links}} \, dA^{\rm{a}}_{\rm{links}} + \int_{A^{\rm{a}}_{\rm{rechts}}} \sigma_{\rm{rechts}} \, dA^{\rm{a}}_{\rm{rechts}} + \int_{A^{\parallel}} \tau \left( x,y\right) \, dA^{\parallel} &= 0 \\
\underbrace{-\int_{A^{\rm{a}}_{\rm{links}}} \cfrac{M_z \, z}{I_{zz,\rm{links}}} \, dA^{\rm{a}}_{\rm{links}} + \int_{A^{\rm{a}}_{\rm{rechts}}} \cfrac{M_z \, z}{I_{zz,\rm{rechts}}} \, dA^{\rm{a}}_{\rm{rechts}}}_{\rm{Als} \, \rm{linker-} \, \rm{en} \, \rm{rechter} \, \rm{afschuivend} \, \rm{vlak} \, \rm{gelijk} \, \rm{zijn} \, \rm{vervallen} \, \rm{deze} \, \rm{termen}} + \underbrace{\int_{A^{\rm{a}}} \cfrac{\Delta M_z \,z}{I_{zz}} \, dA^{\rm{a}}}_{\rm{uitgaande} \, \rm{van} \, \rm{gelijk} \, \rm{linker-} \, \rm{en} \, \rm{rechter} \, \rm{afschuivend} \, \rm{vlak}} + \int_{A^{\parallel}} \tau \left( x,y\right) \, dA^{\parallel} &= 0 \\
 \int_{A^{\rm{a}}} \cfrac{\Delta M_z \,z}{I_{zz}} \, dA^{\rm{a}} + \int_{A^{\parallel}} \underbrace{\tau \left( x,y\right)}_{\rm{Als} \, \tau \left( x,y\right) = \tau_{\rm{gem}} \, \text{kan} \, \rm{deze} \, \rm{uit} \, \rm{de} \, \rm{integraal} \, \rm{worden} \, \rm{gehaald} }  \, dA^{\parallel} &= 0 \\
\cfrac{\Delta M_z}{I_{zz}} \int_{A^{\rm{a}}} z \, dA^{\rm{a}} + \tau_{\rm{gem}} \int_{A^{\parallel}} \, dA^{\parallel} &= 0 \\
\cfrac{\Delta M_z}{I_{zz}} S_{z}^{\rm{a}} + \tau_{\rm{gem}} A^{\parallel} &= 0 \\
\cfrac{\Delta M_z}{I_{zz}} S_{z}^{\rm{a}} + \tau_{\rm{gem}} \, b  \, \Delta x &= 0 \\
\lim_{\Delta x \to 0} \tau_{\rm{gem}} &= \lim_{\Delta x \to 0} \cfrac{- \cfrac{\Delta M_z}{\Delta x} \, S_{z}^{\rm{a}}}{b \, I_{zz}} \\
\tau_{\rm{gem}} &= -\cfrac{V_z \, S_{z}^{\rm{a}}}{b \, I_{zz}}
\end{align*}
$$

::::::

::::::::{prf:assumption-start} Gemiddelde schuifspanning
:nonumber: true
::::::::

Om het evenwicht op te stellen kunnen we alleen de resulterende schuifkracht bepalen, de verdeling is daarmee onbekend. We kunnen daarmee alleen maar de gemiddelde schuifspanning bepalen. Voor afschuivende vlakken blijkt deze gemiddelde schuifspanning terecht als de breedte van het deel van de doorsnede waar de schuifspanningen worden bepaald veel kleiner is dan de hoogte deze doorsnede.

:::::::{grid} 1 2 2 2
:gutter: 1 1 1 2

::::::{grid-item-card} $h \gg b$
:columns: 12 12 6 6

Voor de volgende doorsnede is de hoogte veel groter dan de breedte:

```{figure} ./instructie_data/hgroterdanb.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

In dit geval is de schuifspanning op het afschuivende vlak constant en dus gelijk aan de gemiddelde schuifspanning:

```{figure} ./instructie_data/hgroterdanb_spanningen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

::::::

::::::{grid-item-card} $h\cancel{\gg} b$
:columns: 12 12 6 6

Voor de volgende doorsnede is de hoogte niet veel groter dan de breedte:

```{figure} ./instructie_data/hnietgroterdanb.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

In dit geval zijn de schuifspanningen op het afschuivende vlak niet constant en dus niet gelijk aan de gemiddelde schuifspanning.

```{figure} ./instructie_data/hnietgroterdanb_spanningen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

::::::

:::::::

::::::::{prf:assumption-end}
::::::::

::::::{prf:assumption} Prismatische balk
:nonumber: true


We gaan in deze berekeningen uit van dezelfde doorsnede (en dus ook dezelfde doorsnedegrootheden $I_{zz}$ en $A^{\rm{a}}$) in de linker en rechter doorsnede, wat betekent dat we aannemen dat de doorsnede niet verandert over de lengte van de balk; dus een prismatische balk.

:::::{prf:example}
:nonumber: true

Hieronder is een voorbeeld getoond van een niet-prismatische balk (hier met afwijkende $I_{zz}$ en $A^{\rm{a}}$ in de linker en rechter doorsnede). Hiervoor is de formule voor schuifspanningen niet geldig.

```{figure} ./instructie_data/prismatisch.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::::

::::::

### Evenwicht infinitesimaal blokje

De formule die we net hebben afgeleid gaf de gemiddelde schuifspanningen op het afschuivende oppervlakte. We kunnen ook de schuifspanning op de linker en rechter doorsnede vinden ter hoogte van het afschuivende oppervlakte. Dit kunnen we doen door het momentenevenwicht van de schuifspanningen te bekijken op een infinitesimaal (oneindig kleine afmetingen) blokje rondom hoekpunt $\rm{A}$. De schuifspanningen zijn beschreven met index-notatie, waarbij de eerste index de normaalrichting van het vlakje aangeeft waar de spanning op werkt en de tweede index de richting van de werklijn van de spanning. Het blokje heeft een dikte $\Delta y$

```{figure} ./instructie_data/blokje.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

$$
\begin{align*}
\left. \sum T \right|_{\rm{A}} &= 0 \\
\underbrace{\sigma_{zx} \, \Delta x \, \Delta y}_{\rm{Resultante} \, \rm{kracht} \, \rm{op} \, \rm{vlakje} \, z} \, \underbrace{\Delta z}_{\rm{Arm} \, \rm{ten} \, \rm{opzichte} \, \rm{van} \, \rm{A}} - \underbrace{\sigma_{xz} \, \Delta x \, \Delta y}_{\rm{Resultante} \, \rm{kracht} \, \rm{op} \, \rm{vlakje} \, x} \,  \underbrace{\Delta z}_{\rm{Arm} \, \rm{ten} \, \rm{opzichte} \, \rm{van} \, \rm{A}} &= 0 \\
\sigma_{zx} &= \sigma_{xz} \\
\end{align*}
$$

Dus de schuifspanningen op een zijde $90^\circ$ ten opzichte van elkaar zijn gelijk van grootte en wijzen naar elkaar toe of van elkaar af. Deze worden daarom ook wel genoteerd met een algemene $\tau$ in plaats van $\sigma$ met subscripten.

Dat betekent dus dat de schuifspanningen op de linker en rechter doorsnede ter hoogte van de snede in de richting van $x$ gelijk zijn aan de schuifspanning in de $x$-richting en naar elkaar toe of van elkaar af wijzen.

```{figure} ./instructie_data/conclusie_afschuivend.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

### Implicaties model schuifspanningen

De schuifspanningsformule beschrijft dus de schuifspanningen zowel in langsrichting $x$ als in het doorsnedevlak $yz$ volgens $\tau_{\rm{gem}}  = -\cfrac{V_{z} \, S_{z}^{\rm{a}} }{b \, I_{zz}}$

Aangezien de spanningen constant zijn over de breedte kunnen we de spanningen in het $x,z$-vlak tekenen in plaats van in 3D:

```{figure} ./instructie_data/2d_spanningen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

Voor de vorm van het schuifspanningsverloop in de doorsnede is af te leiden dat bij een doorsnede met constante breedte de schuifspanning maximaal is ter hoogte van het normaalkrachtencentrum. Daarnaast verloopt deze, specifiek voor rechthoekige doorsnedes, parabolisch.

```{figure} ./instructie_data/parabolisch.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

::::::{admonition} Volledige afleiding
:class: notation, dropdown

Om het schuifspanningsverloop te bepalen, kunnen we de formule voor de gemiddelde schuifspanning herschrijven door het statisch moment uit te werken voor een constante breedte:

$$
\begin{align*}
\tau_{\rm{gem}} &= -\cfrac{V_z \, S_{z}^{\rm{a}}}{b \, I_{zz}} \\
\tau_{\rm{gem}} &= -\cfrac{V_z \, \int_{A^{\rm{a}}} z \, dA^{\rm{a}} }{b \, I_{zz}} \\
\tau_{\rm{gem}} &= -\cfrac{V_z \, b \int z \, dz }{b \, I_{zz}} \\
\tau_{\rm{gem}} &= -\cfrac{V_z \, \left(z^2 + \underbrace{C}_{\rm{integration} \, \rm{constant}} \right)}{\, I_{zz}}
\end{align*}
$$

Het statisch moment is maximaal ter hoogte van het normaalkrachtencentrum, waar $z=0$. Dus daar is ook de schuifspanning maximaal.

::::::

Daarnaast leidt de relatie $\sigma_{zx} = \sigma_{xz}$ ook tot de conclusie dat de schuifspanningen dwars op de vrije oppervlakten van een doorsnede nul moeten zijn; de spanning $\sigma_{zx}$ op een vrij oppervlakte met de normaal in de $z$-richting moet nul zijn, waardoor ook $\sigma_{xz}$ nul moet zijn.

:::::{prf:example}
:nonumber: true

In het onderstaande voorbeeld is voor een rechthoekige doorsnede de nulspanning $\sigma_{zx}$ expliciet aangegeven, waarmee ook de spanning in het doorsnedevlak $\sigma_{xz}$ nul is.

```{figure} ./instructie_data/randen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::::

Daarnaast geldt dat, vanwege de aanname dat de schuifspanning gemiddeld verdeeld is over de langsrichting van het afschuivende deel van de doorsnede, de formule alleen een geldig antwoord geeft als een afschuivend deel wordt genomen waarin de schuifspanning daadwerkelijk constant is. We moeten het snedevlak daarom altijd loodrecht op de randen van de doorsnede nemen.

:::::{prf:example}
:nonumber: true

In onderstaande twee doorsnedes is in het eerste figuur het afschuivende deel loodrecht op de randen van de doorsnede genomen, waardoor de schuifspanning constant is over het afschuivende oppervlaktevlak. In het tweede geval is het afschuivende deel niet loodrecht op de randen van de doorsnede genomen, waardoor de schuifspanning niet constant is over het afschuivende oppervlaktevlak.

::::{grid} 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/constant_wel.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/constant_niet.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

::::

:::::

Tot slot kunnen we de formule simplificeren door het teken direct te relateren aan de richting van de snedekracht. De resultante van de schuifspanning werkt namelijk altijd in de richting van de snedekracht. We kunnen daarmee de formule herschrijven naar: $ \left| \tau_{\rm{gem}} \right|  = \cfrac{\left|  V_{z} \, S_{z}^{\rm{a}}  \right|}{b \, I_{zz}} $.

:::::{prf:example}
:nonumber: true

Hieronder is een voorbeeld getoond van een stuk balk met dwarskrachten en een verdeelde belasting. De richting van de (resultante van de) schuifspanningen in de doorsnede moet overeenkomen met de richting van de dwarskracht.
```{figure} ./instructie_data/richtingen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::::

Daarmee kunnen we de volgende aanpak beschrijven voor het bepalen van het schuifspanningsverloop in een doorsnede:

::::::{prf:algorithm} Bepalen schuifspanningsverloop in een doorsnede ten gevolge van buiging
:nonumber: true

1. Bereken de snedekracht $V_z$ in de doorsnede.
2. Neem een aantal karakteristieke afschuivende delen waarin de schuifspanningen constant zijn en bepaal de schuifspanningen op deze delen. Het afschuivende deel door het normaalkrachtencentrum geeft de maximale schuifspanning. Leid het teken van de schuifspanningen af aan de hand van de richting van de snedekracht. De schuifspanningen kunnen berekend worden met $ \left| \tau_{\rm{gem}} \right|  = \cfrac{ \left| V_{z} \, S_{z}^{\rm{a}} \right|}{b  \, I_{zz}}$. Hierin is:
    - $\tau_{\rm{gem}} $: de gemiddelde schuifspanning op het afschuivende oppervlakte van het afschuivende gedeelte op een hoogte $z$ én in de doorsnede op dezelfde hoogte $z$.
    - $V_{z}$: de snedekracht in de $z$-richting.
    - $S_{z}^{\rm{a}}$: het statisch moment van het afschuivende deel van de doorsnede ten opzichte van de $y$-as.
    - $b$: de totale breedte van het afschuivende vlak.
    - $I_{zz}$: het traagheidsmoment van de volledige doorsnede in de $z$-richting.
3. Teken het schuifspanningsprofiel op de doorsnede. Voor een rechthoekige doorsnede verloopt dit parabolisch.

::::::

## Voorbeeld

Het bepalen van schuifspanningen voor een rechthoekige doorsnede wordt gedemonstreerd op het onderstaande voorbeeld.

::::::{prf:example}
:nonumber: true

```{figure} ./instructie_data/voorbeeld.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

Gevraagd is het schuifspanningsverloop op een positieve snede in $\rm{D}$.

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
\sum F_{\rm{v}} = 0 \to V_{\rm{D}} = 30 \, \rm{kN} \left(⎽|⎺\right)
$$

Nu kunnen we de schuifspanningen bepalen op karakteristieke afschuivende delen in de doorsnede. Op de boven en onderzijde is de schuifspanning $0$ en aangezien we een rechthoekige doorsnede hebben weten we dat het schuifspanningsverloop parabolisch is met een maximum ter hoogte van het normaalkrachtencentrum. Daarom wordt op dat punt de maximale schuifspanning bepaald waarmee het hele schuifspanningsverloop gedefinieerd is. Het normaalkrachtencentrum bevindt zich in het zwaartepunt van de doorsnede, wat voor een rechthoek precies in het midden is.

```{figure} ./instructie_data/afschuivend_deel.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

Het statisch moment van dit afschuivende deel is:

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

Dat geeft het volgende schuifspanningsverloop in de doorsnede:

```{figure} ./instructie_data/antwoord.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Schuifspanningsverloop op positieve snede in $\rm{D}$.
```

## Alternatieve afleiding
In hoofdstuk 5.1 en 5.3 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` wordt hetzelfde model op een alternatieve manier afgeleid.

## Meer voorbeelden
In hoofdstuk 5.2 en 5.4.1 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` worden meer voorbeelden gegeven van het bepalen van schuifspanningen in verschillende situaties. Negeer voorbeeld 5.2.2 - 5.2.4 en voorbeeld 2 in 5.4.1.

% ## Instructies in collegevorm
%
% Dit onderwerp is [les ...](...) gepresenteerd in collegevorm tot ....

## Oefeningen
Opgaves 5.2b, 5.3, 5.13 - 5.28, 5.69 en 5.71 in hoofdstuk 5 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013`. Antwoorden zijn [hier](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol2/Chapter5/) beschikbaar.
