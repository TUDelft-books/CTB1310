# Instructie

Tot nu toe hebben we enkel gerekend aan normaalspanningen, en enkel door buiging en verlenging/verkorting. Tijdens buiging treden er echter ook schuifspanningen op in de doorsnede: schuifspanningen die langs een een snede werken in plaats van loodrecht daarop.

Dit is voor te stellen door twee op elkaar liggende balken te beschouwen die doorbuigen. Als je deze twee balken aan elkaar zou willen lijmen zodat deze werken als één balk, zouden schuifspanningen nodig zijn die de onderliggende afschuiving van de twee afzonderlijke balken door buiging zouden tegengaan:

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

We gaan op zoek naar de relatie tussen snedekrachten en schuifspanningen.

## Model

Voordat we de schuifspanningen kunnen bepalen, moeten we eerst beseffen dat schuifspanningen ook vervormingen veroorzaken, net zoals dat normaalspanningen vervormingen veroorzaakten. Normaalspanningen zorgden voor rek, waarbij schuifspanningen zorgen voor afschuiving:

::::{grid} 2
:class-container: center-grid
:gutter: 1
:padding: 0

:::{grid-item-card} Rekvervormingen door normaalspanningen

```{figure} ./instructie_data/afschuiving-2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

:::{grid-item-card} Afschuifvervormingen door schuifspanningen

```{figure} ./instructie_data/afschuiving-3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

::::

Voor normaalspanningen is er een formule afgeleid op basis van het verband tussen de normaalspanningen en de vervormingen door rek van individuele vezels. Anders dan voor de normaalspanningen gaan we voor de schuifspanningen **niet kijken** naar het verband tussen schuifspanningen en de vervormingen door afschuiving. Daarmee volgt onze eerste aanname:

::::::{prf:assumption}
:nonumber: true

We gaan de afschuifvervorming  negeren, en baseren ons enkel op de vervormingen door extensie. De schuifspanningen en afschuifvervorming zijn dus niet één-op-één gerelateerd in ons model, waar dat bij normaalspanningen wel het geval was.

::::::

Om de schuifspanningen te kunnen bepalen gaan we: (1) alle spanningen in langsrichting op een afschuivend deel van een dwarsdoorsnede bepalen en daarmee (2) met krachtenevenwicht de schuifspanningsformule afleiden in langsrichting. Vervolgens (3) nemen we het momentenevenwicht van een infinitesimaal blokje om ook de spanningen in doorsnederichting te bepalen en (4) kijken we naar de implicaties van ons model.

We beginnen dus met:

::::::::::{steps}
:::::::::{step} Bepaal alle spanningen in langsrichting op een afschuivend deel van een dwarsdoorsnede

Voor het bepalen van schuifspanningen kijken we naar het evenwicht van een infinitesimaal (oneindig kleine afmetingen) stukje van een balk als lijn van lengte $\Delta x$ met daarop snedekrachten $V_z$ en $M_z$, volgens het gegeven assenstelsel. Het moment op de rechterkant is mogelijk $\Delta M_z$ groter dan dat op de linkerkant.

```{figure} ./instructie_data/beam_section.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

We kunnen de spanningen bepalen op de dwarsdoorsnedes: hoe de spanningen verdeeld over de dwarsdoorsnede zijn in plaats van enkel de resultaten snedekracht. Daarvoor kijken we naar dezelfde lengte $\Delta x$, maar nu een vrijlichaamsschema van de volledige dwarsdoorsnede in plaats van het lijnmodel. Deze snede heeft nu dus ook nog een breedte $b$ en hoogte $b$ (niet infinitesimaal!).

````{figure-start} ./instructie_data/snede_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
:name: snede_1
````

Het blauwe vlak is vlak waardoor we de balk hebben doorgesneden.

````{figure-end}
````

De verdeling van schuifspanningen op onze dwarsdoorsnedes zijn nog onbekend (dus onbekende functie van $y$ en $z$), maar voor de normaalspanningen geldt de eerder afgeleide formule $\sigma = \cfrac{M_z \cdot z}{I_{zz}}$, met aan de rechterzijde een moment van $M_z + \Delta M_z$.

::::{grid} 1 1 2 2
:class-container: center-grid
:gutter: 1
:padding: 0

:::{grid-item-card} Schuifspanningen op volledige dwarsdoorsnede

```{figure} ./instructie_data/spanningen_section-1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

De schuifspanningen zijn beschreven met index-notatie, waarbij de eerste index de normaalrichting van het vlakje aangeeft waar de spanning op werkt en de tweede index de richting van de werklijn van de spanning.

:::

:::{grid-item-card} Normaalspanningen op volledige dwarsdoorsnede

```{figure} ./instructie_data/spanningen_section-2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

::::

```{attention}
De schuif- en normaalspanningen zijn los van elkaar getekend, maar treden gelijktijdig op. Dit geldt ook voor de andere figuren op deze pagina.
```

De normaalspanningen zijn al eerder afgeleid. In dat model hebben we een aantal aannames gedaan over de rekverdeling en de constitutieve vergelijking die hier nog steeds geldig zijn. Ga terug naar die lessen om deze te herhalen als je ze niet meer weet.

Nu stellen we een vrijlichaamsschema op met spanningen voor een deel van de dwarsdoorsnede, het zogenaamde afschuivende deel. Hiervoor maken we een langssnede (in de lengterichting $x$) en bekijken we het bovenste afgeschoven gedeelte. $A^{\rm{a}}$ is het dwarsoppervlakte van de linker- en rechterkant van het afgeschoven deel, $A^{\parallel}$ is het langsoppervlakte van onderkant van het afgeschoven deel.

```{figure} ./instructie_data/snede_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

De spanningen op dit afschuivende deel kunnen ook worden aangegeven in het vrijlichaamsschema. Op de onderkant van dit afgeschoven deel werkt mogelijk een schuifspanning met onbekend verloop (dus als functie van $x$ en $y$), maar geen normaalspanningen:

::::{grid} 1 1 2 2
:class-container: center-grid
:gutter: 1
:padding: 0
    
:::{grid-item-card} Schuifspanningen op afschuivend deel

```{figure} ./instructie_data/spanningen_afschuivend-1.svg
:align: center
:name: afschuivend-1
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

:::{grid-item-card} Normaalspanningen op afschuivend deel

```{figure} ./instructie_data/spanningen_afschuivend-2.svg
:align: center
:name: afschuivend-2
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

:::

::::

:::::::::

:::::::::{step} Gebruik krachtenevenwicht om de schuifspanningsformule af te leiden in langsrichting.

Door het evenwicht in de langsrichting op te stellen, kunnen we de gemiddelde schuifspanning bepalen op het afschuivende oppervlakte:

::::::{admonition} Schuifspanningsformule
:class: definition

$$
\sigma_{zx,\rm{gem}} = -\cfrac{V_{z} \, S_{z}^{\rm{a}} }{b \, I_{zz}}
$$

Met:
- $\sigma_{zx,\rm{gem}} $: de gemiddelde schuifspanning op het afschuivende langsoppervlakte ($A^{\parallel}$ in {numref}`afschuivend-1`) van het afschuivende gedeelte.
- $V_{z}$: de snedekracht in de $z$-richting
- $S_{z}^{\rm{a}}$: het statisch moment van het dwarsoppervlakte ($A^{\rm{a}}$ in {numref}`afschuivend-2`) van het afschuivende gedeelte ten opzichte van de $y$-as.
- $b$: de totale breedte van het afschuivende vlak in het dwarsoppervlakte.
- $I_{zz}$: het traagheidsmoment van de volledige dwarsdoorsnede in de $z$-richting
- Het teken volgens het assenstelsel: een positieve $\tau$ werkt in de richting van de $x$-as.

::::::

::::::{admonition} Volledige afleiding
:class: proposition, dropdown

$$
\begin{align*}
\sum F_x &= 0 \\
-\int_{A^{\rm{a}}_{\rm{links}}} \sigma_{\rm{links}} \, dA^{\rm{a}}_{\rm{links}} + \int_{A^{\rm{a}}_{\rm{rechts}}} \sigma_{\rm{rechts}} \, dA^{\rm{a}}_{\rm{rechts}} + \int_{A^{\parallel}} \sigma_{zx} \left( x,y\right) \, dA^{\parallel} &= 0 \\
\underbrace{\cancel{-\int_{A^{\rm{a}}_{\rm{links}}} \cfrac{M_z \, z}{I_{zz,\rm{links}}} \, dA^{\rm{a}}_{\rm{links}} + \int_{A^{\rm{a}}_{\rm{rechts}}} \cfrac{M_z \, z}{I_{zz,\rm{rechts}}} \, dA^{\rm{a}}_{\rm{rechts}}}}_{\rm{Als} \, \rm{linker-} \, \rm{en} \, \rm{rechter} \, \rm{afschuivend} \, \rm{vlak} \, \rm{gelijk} \, \rm{zijn} \, \rm{vervallen} \, \rm{deze} \, \rm{termen}} &\\
+ \underbrace{\int_{A^{\rm{a}}} \cfrac{\Delta M_z \,z}{I_{zz}} \, dA^{\rm{a}}}_{\rm{uitgaande} \, \rm{van} \, \rm{gelijk} \, \rm{linker-} \, \rm{en} \, \rm{rechter} \, \rm{afschuivend} \, \rm{vlak}} + \int_{A^{\parallel}} \sigma_{zx} \left( x,y\right) \, dA^{\parallel} &= 0 \\
 \int_{A^{\rm{a}}} \cfrac{\Delta M_z \,z}{I_{zz}} \, dA^{\rm{a}} + \int_{A^{\parallel}} \underbrace{\sigma_{zx} \left( x,y\right)}_{\rm{Als} \, \sigma_{zx} \left( x,y\right) = \sigma_{zx,\rm{gem}} \, \text{kan} \, \rm{deze} \, \rm{uit} \, \rm{de} \, \rm{integraal} \, \rm{worden} \, \rm{gehaald} }  \, dA^{\parallel} &= 0 \\
\cfrac{\Delta M_z}{I_{zz}} \int_{A^{\rm{a}}} z \, dA^{\rm{a}} + \sigma_{zx,\rm{gem}} \int_{A^{\parallel}} \, dA^{\parallel} &= 0 \\
\cfrac{\Delta M_z}{I_{zz}} S_{z}^{\rm{a}} + \sigma_{zx,\rm{gem}} A^{\parallel} &= 0 \\
\cfrac{\Delta M_z}{I_{zz}} S_{z}^{\rm{a}} + \sigma_{zx,\rm{gem}} \, b  \, \Delta x &= 0 \\
\lim_{\Delta x \to 0} \sigma_{zx,\rm{gem}} &= \lim_{\Delta x \to 0} \cfrac{- \cfrac{\Delta M_z}{\Delta x} \, S_{z}^{\rm{a}}}{b \, I_{zz}} \\
\sigma_{zx,\rm{gem}} &= -\cfrac{V_z \, S_{z}^{\rm{a}}}{b \, I_{zz}}
\end{align*}
$$

::::::

**Beperkingen en aannames**

- In de afleiding zijn alleen krachten bekeken die werken in de $z$-richting of zorgen vooor buiging in de $z$-richting.

    ::::::::{prf:assumption-start}
    :nonumber: true
    ::::::::
    De krachten in de $y$-richting worden buiten beschouwing gelaten. Als er ook nog krachten in de y-richting zouden werken zouden er ook schuifspanningen in de $y$-richting optreden, waarvoor een gelijkwaardige afleiding kan worden gedaan.
    :::::::{prf:assumption-end}
    ::::::::

- De formule wordt ook wel eens gepresenteerd zonder $b$: $s = -\cfrac{V_{z} \, S_{z}^{\rm{a}} }{I_{zz}}$. $s$ is dan de schuifstroom per eenheid van lengte.

- In de afleiding is $\sigma_{zx} \left( x,y\right)$ vervangen door $\sigma_{zx,\rm{gem}}$, dit is een aanname die niet altijd geldig is:

    ::::::::{prf:assumption-start}
    :nonumber: true
    ::::::::

    Voor afschuivende vlakken blijkt deze gemiddelde schuifspanning terecht als de breedte van het deel van de doorsnede waar de schuifspanningen worden bepaald veel kleiner is dan de hoogte deze doorsnede.

    :::::::{grid} 1 1 2 2
    :class-container: center-grid
    :gutter: 1
    :padding: 0

    ::::::{grid-item-card} $h \gg b$

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
    :name: hgroterdanb_spanningen
    ```

    ::::::

    ::::::{grid-item-card} $h\cancel{\gg} b$

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

- Daarnaast zijn in de afleiding een aantal termen weggevallen en vereenvoudigd waarbij er aangenomen is dat de doorsnede aan de linker- en rechterzijde gelijk zijn (en dus ook dezelfde doorsnedegrootheden $I_{zz}$ en $A^{\rm{a}}$): er is een aanname gedaan van een prismatische balk.

    ::::::{prf:assumption}
    :nonumber: true

    De doorsnede moet zijn prismatisch zijn. Hieronder is een voorbeeld getoond van een wel- en niet-prismatische balk (hier met afwijkende $I_{zz}$ en $A^{\rm{a}}$ in de linker en rechter doorsnede). Voor de tweede doorsnede is de schuifspanningsformule niet geldig.

    :::::{grid} 2
    :class-container: center-grid
    :gutter: 1
    :padding: 0

    ::::{grid-item-card} Prismatische doorsnede

    ````{figure} ./instructie_data/snede_1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
    :number:
    ````

    ::::

    ::::{grid-item-card} Niet-prismatische doorsnede

    ```{figure} ./instructie_data/niet_prismatisch.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
    :number:
    ```

    ::::

    :::::

    ::::::

- Tot slot moet het afschuivend vlak zo worden gekozen dat deze loodrecht is op de randen van de doorsnede.

    ::::::{prf:assumption}
    :nonumber: true

    Alleen als het afschuivend vlak loodrecht staat op de randen van de doorsnede is de schuifspanning uniform over het afschuivend vlak en dus gelijk aan de gemiddelde schuifspanning. Zonder deze aanname is de schuifspanning niet uniform over het afschuivend vlak en is de schuifspanningsformule dus niet geldig.

    :::::{grid} 2
    :class-container: center-grid
    :gutter: 1
    :padding: 0

    ::::{grid-item-card} Afschuivend deel loodrecht op randen van de doorsnede met een uniforme schuifspanning

    :::{fetch} {ref}`hgroterdanb_spanningen`
    :::

    ::::

    ::::{grid-item-card} Afschuivend deel niet loodrecht op randen van de doorsnede met een uniform schuifspanning

    ```{figure} ./instructie_data/constant_niet.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
    :number:
    ```

    ::::

    :::::

    ::::::

:::::::::

:::::::::{step} Neem het momentenevenwicht van een infinitesimaal blokje om ook de spanningen in doorsnederichting te bepalen.

De formule die we net hebben afgeleid gaf de gemiddelde schuifspanningen op het afschuivende langsoppervlakte $A^{\parallel}$. We zagen echter dat er ook schuifspanningen optreden op het dwarsoppervlakte $A^{\rm{a}}$, waarvan we nog niet weten hoe deze verdeeld zijn:

```{figure} ./instructie_data/dwars_langs.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

We kunnen deze spanningen aan elkaar relateren door het evenwicht van een infinitesimaal blokje te bekijken ergens uit de constructie. Ditmaal infinitesimaal in alle richtingen:

```{figure} ./instructie_data/blokje_snede.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

Op het vrijlichaamsschema van dit infinitesimale blokje kunnen we het momentenevenwicht loslaten rondom de $y$-as door het midden van het blokje.

```{figure} ./instructie_data/blokje.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
:number:
```

```{attention}
De normaalspanningen zijn niet getekend, maar treden gelijktijdig op. Deze zouden wegvallen in het momentenevenwicht omdat deze door het middden van het blokje gaan.
```

$$
\begin{align*}
\left. \sum T \right|_{\rm{y}} &= 0 \\
\underbrace{\sigma_{zx} \cdot \Delta x \cdot \Delta y}_{\rm{Resultante} \, \rm{kracht} \, \rm{op} \, y,z-\rm{vlakje}} \cdot \underbrace{\Delta z}_{\rm{Arm} \, \rm{van} \, \rm{koppel}} &\\
- \underbrace{\sigma_{xz} \cdot \Delta x \cdot \Delta y}_{\rm{Resultante} \, \rm{kracht} \, \rm{op} \, x,y-\rm{vlakje}} \cdot  \underbrace{\Delta z}_{\rm{Arm} \, \rm{van} \, \rm{koppel}} &= 0 \\
\sigma_{zx} \cdot \cancel{ \Delta x \cdot \Delta y \cdot \Delta z} &= \sigma_{xz} \cdot \cancel{ \Delta x \cdot \Delta y \cdot \Delta z } \\
\sigma_{zx} &= \sigma_{xz}
\end{align*}
$$

Dus de schuifspanningen op een zijde $90^\circ$ ten opzichte van elkaar zijn gelijk van grootte en wijzen naar elkaar toe of van elkaar af. De spanningen in de doorsnederichting kunnen we nu dus ook bepalen, Ze zijn immers gelijk aan de schuifspanningen in de langsrichting.

:::::::::

:::::::::{step} Bepaal de implicaties van het model.

-   Omdat de schuifspanningen in de doorsnederichting gelijk zijn aan de schuifspanningen in de langsrichting, kunnen we deze ook wel aangeduid met een algemene $\tau$ in plaats van $\sigma_{zx}$ en $\sigma_{xz}$:

    ```{figure} ./instructie_data/conclusie_afschuivend.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
    :number:
    ```

-   Aangezien de spanningen constant zijn over de breedte kunnen we de spanningen daarom in het $x,z$-vlak of $y,z$-vlak tekenen in plaats van in 3D:

    ::::{grid} 2
    :class-container: center-grid
    :gutter: 1
    :padding: 0

    :::{grid-item-card} Schuifspanningen in het $x,z$-vlak

    ```{figure} ./instructie_data/2d_spanningen.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
    :number:
    ```

    :::

    :::{grid-item-card} Schuifspanningen in het $y,z$-vlak

    ```{figure} ./instructie_data/2d_spanningen_yz.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
    :number:
    ```

    Merk op dat de schuifspanningen op de langsoppervlakte van het afgeschoven deel in dit vlak niet zichtbaar zijn omdat ze het scherm in gaan.

    :::

    ::::

-   Daarnaast moeten de schuifspanningen dwars op de vrije oppervlakten van een doorsnede nul moeten zijn: vanwege zowel de relatie $\sigma_{zx} = \sigma_{xz}$ als dat het statisch moment van het afschuivende gedeelte $0$ nadert.

    In het onderstaande voorbeeld is voor een rechthoekige doorsnede de nulspanning $\sigma_{zx}$ expliciet aangegeven, waarmee ook de spanning in het doorsnedevlak $\sigma_{xz}$ nul is.

    ```{figure} ./instructie_data/randen.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
    :number:
    ```

-   Voor de vorm van het schuifspanningsverloop in de doorsnede is af te leiden dat bij een doorsnede met constante breedte de schuifspanning maximaal is ter hoogte van het normaalkrachtencentrum.

    Daarnaast verloopt deze, specifiek voor rechthoekige delen van doorsnedes, parabolisch.

    ```{figure} ./instructie_data/parabolisch.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
    :number:
    ```

    ::::::{admonition} Volledige afleiding
    :class: proposition, dropdown

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

-   Tot slot kunnen we de formule simplificeren door het teken direct te relateren aan de richting van de snedekracht. De resultante van de schuifspanning werkt namelijk altijd in de richting van de snedekracht.

    Hieronder is een voorbeeld getoond van een stuk balk met dwarskrachten en een verdeelde belasting. De richting van de (resultante van de) schuifspanningen in de doorsnede moet overeenkomen met de richting van de dwarskracht.

    ::::{grid} 1 1 2 2
    :class-container: center-grid

    :::{grid-item}

    ```{figure} ./instructie_data/richtingen_1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
    :number:
    ```

    :::

    :::{grid-item}

    ```{figure} ./instructie_data/richtingen_2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
    :number:
    ```

    :::

    ::::

    We kunnen daarmee de formule herschrijven naar: $ \left| \tau_{\rm{gem}} \right|  = \cfrac{\left|  V_{z} \, S_{z}^{\rm{a}}  \right|}{b \, I_{zz}} $.

:::::::::
::::::::::

## Stappenplan

Nu we het model vastgesteld hebben, kunnen we de volgende aanpak beschrijven voor het bepalen van het schuifspanningsverloop in een doorsnede:

::::::{admonition} Stappenplan
:class: algorithm

1. Bereken de dwarskracht: Bereken de snedekracht $V_z$ in de doorsnede.
2. Bepaal de schuifspanning op een aantal karakteristieke afschuivende delen: Neem een aantal karakteristieke afschuivende delen waarin de schuifspanningen constant zijn en bepaal de schuifspanningen op deze delen. Het afschuivende deel door het normaalkrachtencentrum geeft de maximale schuifspanning en er zijn geen schuifspanningen op vrije oppervlaktes. De schuifspanningen kunnen berekend worden met $ \left| \tau_{\rm{gem}} \right|  = \cfrac{ \left| V_{z} \, S_{z}^{\rm{a}} \right|}{b  \, I_{zz}}$. Hierin is:
    :::::{grid}
    ::::{grid-item}
    :columns: 12 12 8 8
    - $\tau_{\rm{gem}} $: de gemiddelde schuifspanning op het afschuivende langsoppervlakte $A^{\parallel}$ én in de dwarsdoorsnede op dezelfde hoogte.
    - $V_{z}$: de snedekracht in de $z$-richting.
    - $S_{z}^{\rm{a}}$: het statisch moment van het dwarsoppervlakte van het afschuivende deel van de doorsnede $A^{\rm{a}}$ in de $z$-richting.
    - $b$: de totale breedte van het afschuivende vlak.
    - $I_{zz}$: het traagheidsmoment van de volledige doorsnede in de $z$-richting.
    ::::
    ::::{grid-item}
    :columns: 12 12 4 4
    ```{figure} ./instructie_data/stappenplan.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect
    :number:
    ```
    :::::
4. Leid het teken van de schuifspanningen af aan de hand van de richting van de snedekracht.
3. Teken het schuifspanningsprofiel in het 2D: Voor een rechthoekige doorsnede verloopt dit parabolisch.

::::::
