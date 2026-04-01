````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is gebaseerd op [deze oefening uit het online boek van het vak CTS1000 Structural Mechanics op de Technische Universiteit Delft](https://oit.tudelft.nl/CT1000/2025/week_14/session_3/intro.html) {cite:p}`CT1000_2025`.

```
````

# Begeleide oefening 1


Gegeven is de volgende constructie en doorsnede in $\rm{D}$. Het is een versimpeld model van de [Prinses Amaliabrug, een fietsbrug in Dordrecht](https://www.ad.nl/dordrecht/zes-tips-om-het-hoofd-koel-te-houden~a2c4481b5/).

::::{grid} 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ../torsie_model/lesoefening2_data/constructie.svg
:align: center
:class: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/failure_criteria
:number:
```

De verdeelde belasting grijpt aan in het midden van de doorsnede.  
De $14.32\,\rm{kN}$ grijpt aan in $y=-2 \,\rm{m}$.  
De oplegreactie bij $A$ grijpt aan in $y=-2 \,\rm{m}$.  
De oplegreactie bij $B$ grijpt aan in zowel $y=-2 \,\rm{m}$ als $y=+2 \,\rm{m}$.

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure} lesoefening_data/doorsnede_2.svg
:align: center
:class: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/failure_criteria
:number:
```
:::

::::

Dit is dezelfde constructie en doorsnede als in [de vorige les](../torsie_model/lesoefening2.md). Ditmaal zijn echter niet alleen schuifspanningen gevraagd ten gevolge van de verwringing, maar nu de totale schuifspanning en normaalspanning in punt $\rm{E}$ in de doorsnede net rechts van $\rm{D}$.

Kijk terug naar je uitwerking van [de vorige les](../torsie_model/lesoefening2.md), een deel van de waardes zijn relevant voor de vragen van vandaag

:::::{exercise}
:nonumber: true

Gegeven is dat het oppervlakte en statisch moment ten opzichte van de $\bar y$-as van de boven- en zijkanten van de doorsnede  gelijk is aan $4 \cdot 0.01 + 2 \cdot 0.25 \cdot 0.01 = 0.045 \, \rm{m}^2 $ en $4 \cdot 0.01 \cdot 1.75 + 2 \cdot 0.25 \cdot 0.01 \cdot \left(1.75 + \cfrac{0.25}{2}\right) = 0.079375 \rm{m^3}$, respectievelijk.

Om het zwaartepunt van de gehele doorsnede te bepalen is ook het zwaartepunt van het gekromde gedeelte nodig ten opzichte van de $\bar y$-as. Maak daarvoor gebruik van $S_{\bar z} = \int\limits_A z \, dA$ en $A = \int\limits_A dA$. De volgende vragen zijn er om je op weg te helpen.

```{h5p} https://tudelft.h5p.com/content/1292808600979606797/embed
```

:::::

:::::{exercise}
:nonumber: true

Op eenzelfde manier is $I_{zz}$ te berekenen voor het gekromde gedeelte. Ten opzichte van het zwaartepunt van de gehele doorsnede zoals bepaald in de vorige opgave geeft dat: $I_{zz}^{\rm{gekromde} \, \rm{gedeelte}} = 98.63\,\mathrm{dm}^4$. Bepaal $I_{zz}$ van de gehele doorsnede.


```{h5p} https://tudelft.h5p.com/content/1292808647660137747/embed
```

:::::

:::::{exercise}
:nonumber: true

Bepaal de normaalspanning in punt $\rm{E}$ net rechts van $\rm{D}$.

```{h5p} https://tudelft.h5p.com/content/1292808652061755197/embed
```

:::::

:::::{exercise}
:nonumber: true

Bepaal de schuifspanning op een positieve doorsnede in punt $\rm{E}$ net rechts van $\rm{D}$ ten gevolge van de dwarskracht.

```{h5p} https://tudelft.h5p.com/content/1292808655867105037/embed
```

:::::

:::::{exercise}
:nonumber: true

Bepaal de totale schuifspanning op een positieve doorsnede in punt $\rm{E}$ net rechts van $\rm{D}$ ten gevolge van de kromming en verwringing.

```{h5p} https://tudelft.h5p.com/content/1292808657783449747/embed
```

:::::
