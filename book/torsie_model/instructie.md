# Instructie

In de vorige les hebben we bekeken hoe we het wringend moment in een doorsnede kunnen bepalen. In deze les gaan we bekijken hoe we de spanningen kunnen berekenen ten gevolge van het wringend moment.

Het spanningsverloop ten gevolge van een wringend moment is over het algemeen erg complex en afhankelijk van het soort doorsnede. We zullen een aantal doorsnedes met bijbehorende modellen behandelen: ronde massieve doorsnedes en ringen (zowel dikwandig als dunwandig), dunwandige niet-ronde gesloten doorsnedes, en open dunwandige doorsnedes.

## Model ronde massieve doorsnedes en ringen

Voor de afleiding van spanningen in ronde massieve doorsnedes en ringen maken we vergelijkbare aannames als bij de afleiding van buigspanningen:

::::::{grid} 1 2 2 2
:gutter: 1 1 1 2

:::::{grid-item-card} Buiging
%:columns: 12 12 4 4

De doorsnedes blijven vlak en loodrecht op ‘vezels’ staan, waarmee de vorm van de doorsnede behouden blijft en het rekverloop lineair is in $z$-richting.

::::{grid} 2 2 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/assump_bending_1.svg
:align: center
:scale: 100
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

:::
:::{grid-item}
:columns: auto

```{figure} ./instructie_data/assump_bending_2.svg
:align: center
:scale: 100
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```
:::
::::


+++

Normaalspanningen en -rekken hebben een lineair verband ($\sigma = E \varepsilon$), waarmee de vorm van het spanningsverloop gelijk is aan die van het rekverloop.

:::::

:::::{grid-item-card} Wringing
%:columns: 12 12 8 8

De doorsnedes blijven vlak en radiale lijnen blijven recht, waarmee de cirkelvormige vorm van de doorsnede behouden blijft en het rekverloop lineair is in radiale richting.

::::{grid} 2 2 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/assump_torsion_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:name: assump_torsion
:number:
```


:::
:::{grid-item}
:columns: auto

```{figure} ./instructie_data/assump_torsion_2.svg
:align: center
:scale: 100
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```
:::
::::

+++
Schuifspanningen en -rekken hebben een lineair verband ($\tau = G \gamma$), waarmee de vorm van het spanningsverloop gelijk is aan die van het rekverloop.

:::::

::::::

Zoals te zien is in {numref}`assump_torsion`, zorgt het wringend moment voor een rotatie van de doorsnede. De cirkelvormige 'vezels' schuiven dus in radiale richting steeds meer af in een lineair verband. Dit zorgt voor een lineair verloop van schuifrekken en schuifspanningen.

```{figure} ./instructie_data/spanningen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```


Als we een lineair spanningsverloop als functie van de straal $r$ aannemen, kunnen we dat schrijven als $\tau = k \cdot r$, waarbij $k$ een constante is die we nog moeten bepalen.

De bijdrage van een klein oppervlakte $dA$ aan het wringend moment ten opzichte van het dwarskrachtencentrum is dan: $dM_t = k \cdot r \cdot r \, dA$

Als we dit integreren over de hele doorsnede, vinden we het totale wringend moment. De term $\int\limits_A{r^2 \, dA}$ noemen we het polair traagheidsmoment $I_{\rm{p}}$ en is puur afhankelijk van de vorm van de doorsnede.

$$
\begin{align*}
M_t &= k \int\limits_A r^2 dA \\
M_t &=  k \cdot I_{\rm{p}} \\
k &= \cfrac{M_t}{I_{\rm{p}}} \\
\end{align*}
$$

Dit geeft:

$$
\tau \left(r\right)= \cfrac{M_t \cdot r}{I_{\rm{p}}}
$$


Het polair traagheidsmoment voor verschillende doorsnedes is hieronder getoond:

::::{grid} 1 2 3 3
:class-container: center-grid

:::{grid-item}
:columns: auto
```{figure-start} ./instructie_data/schijf.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```
$$
I_{\rm{p}} = \cfrac{\pi \cdot R^4}{2}
$$

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/dikwandig_ring.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

$$
I_{\rm{p}} = \cfrac{\pi \cdot \left(R_1^4 - R_2^4\right)}{2}
$$

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/dunwandig_ring.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

$$
I_{\rm{p}} = 2 \pi R^3 t
$$

```{figure-end}
```

:::

::::

::::::{admonition} Volledige afleiding
:class: notation, dropdown

Het polair traagheidsmoment voor een massieve cirkelvormige doorsnede met straal $R$ kunnen we afleiden door in polaire coördinaten te integreren:

$$
\begin{align*}
I_{\rm{p}} &= \int\limits_A r^2 dA \\
&=  \int\limits_0^{R}{\int\limits_0^{2 \pi}{ r^3 \, d\theta \, dr}} \\
&= \int\limits_0^{R}{ 2 \pi \cdot r^3 \, dr} \\
&= \cfrac{\pi}{2} R^4 \\
\end{align*}
$$

Op vergelijkbare wijze kan het polaire traagheidsmoment voor andere dikwandige en dunwandige doorsnedevormen worden afgeleid.

::::::

## Model dunwandige niet-ronde gesloten doorsnedes

Voor niet-ronde doorsnedes is bovenstaande aanpak niet geldig, omdat de aannames van vlakke doorsnedes en rechte radiale lijnen niet meer gelden. Echter kunnen we aannemen dat dat de schuifspanningen constant zijn over de wanddikte vanwege de dunwandigheid. Voor een gesloten doorsnede moet daarnaast de richtingen van de schuifspanningen overeenkomen met het wringend moment.

Om een functie te bepalen voor de schuifspanningen bekijken we een willekeurige dunwandige niet-ronde gesloten doorsnede:

```{figure} ./instructie_data/dunwandige_doorsnede.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

Als we een snede maken in deze doorsnede, worden ook de schuifspanningen in de $x$-richting zichtbaar, die gelijk zijn aan de schuifspanningen in de wandrichting ter plekke van het afschuifvlak:

```{figure} ./instructie_data/afschuifvlak.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

Krachtenevenwicht in de $x$-richting geeft:

$$
\begin{align*}
\sum{F_x} &= 0 \\
\tau_1 \cdot t_1 \cdot dx - \tau_2 \cdot t_2 \cdot dx &= 0 \\
\tau_1 \cdot t_1 &= \tau_2 \cdot t_2 \\
\end{align*}
$$

Het product van schuifspanningen met wanddikte noemen we ook wel schuifstroom en is dus constant over de hele doorsnede.

Als vervolgens het aandeel van de schuifspanning op telkens een klein stukje van de wand op het totale wringend moment wordt bekeken, kan een functie worden gevonden voor de schuifspanning als functie van de dikte van de wand. Deze functie kan alleen worden gevonden vanwege de constante schuifstroom:

$$
\tau = \cfrac{M_t}{2 \cdot A_{\rm{m}} \cdot t}
$$

Met voor $A_{\rm{m}}$ het oppervlakte dat wordt ingesloten door door hartlijn van de wanden.

::::::{admonition} Volledige afleiding
:class: notation, dropdown

Voor de volledige afleiding wordt verwezen naar hoofdstuk 6.3.1 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013`

::::::

## Model open dunwandige doorsnedes

Tot slot bekijken we open dunwandige doorsnedes. Ook hier is de aanname van vlakke doorsnedes en rechte radiale lijnen niet meer geldig. Daarnaast kunnen we ook niet meer aannemen dat de schuifspanningen constant zijn over de wanddikte, omdat de doorsnede anders geen wringing kan weerstaan.

De meest simpele open doorsnede, een strip, kan geen wringend weerstaan als de schuifspanningen constant zijn over de wanddikte omdat de schuifspanningen allemaal in dezelfde richting lopen.

```{figure} ./instructie_data/simpel.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

Er wordt daarom een lineair toenemende schuifspanning aangenomen vanuit het midden van de wand naar de buitenkant. Dit lineaire verband is een versimpeling en in werkelijkheid is het spanningsverloop complexer. Zeker in de buurt van overgangen en hoeken schiet dit model tekort.

```{figure} ./instructie_data/I-balk.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

De open doorsnede modelleren vervolgens als een verzameling van dunwandige niet-ronde gesloten doorsnedes. Hier worden dus ook de spanningen in de overgangen en hoeken gemodelleerd hoewel ons model daar niet accuraat is. Het foutief meenemen van die spanningen heeft daarmee ook een kleine invloed op de spanningen waar ons lineaire verband wel geldig is.

```{figure} ./instructie_data/dunwandig_open_gesloten.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

Door deze individuele bijdrages te integreren over de halve wanddikte komen we tot de volgende formule voor de schuifspanningen in open dunwandige doorsnedes:

$$
\tau \left(e_{\rm{m}}\right) = \cfrac{M_t \cdot e_{\rm{m}}}{\frac{1}{2}\sum\limits_{i}{\frac{1}{3} \cdot h_i \cdot t_i^3}}
$$

Met:
- $e_{\rm{m}}$ de afstand van het midden van de wand tot het punt waar de schuifspanning wordt berekend
- $h_i$ de hoogte/lengte van een wandsegment $i$
- $t_i$ de wanddikte van een recht wandsegment $i$

De 'arm' in orde grootte $e_{\rm{m}}$ van de schuifspanningen in deze open dunwandige is vele malen kleiner dan de 'arm' in gesloten doorsnedes in ordegrootte $h$. Hierdoor zouden de spanningen veel groter moeten zijn om hetzelfde wringend moment te kunnen weerstaan. In de praktijk betekent dit dat open dunwandige doorsnedes veel minder goed in staat zijn om wringing te weerstaan dan gesloten dunwandige doorsnedes.

::::::{admonition} Volledige afleiding
:class: notation, dropdown

Voor de volledige afleiding wordt verwezen naar hoofdstuk 6.3.2 en 6.3.3 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013`

::::::

## Voorbeeld

voorbeeld https://collegeramavideoportal.tudelft.nl/catalogue/ctb1310/presentation/27d1cdefc7cd4e94ad010c251f61a0041d?academicYear=2021-2022-ctb1310 met gesloten en open cirkel

## Meer voorbeelden
In hoofdstuk 6 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` worden meer voorbeelden gegeven van het bepalen van schuifspanningen in verschillende situaties. Negeer voorbeeld ...

% ## Instructies in collegevorm
%
% Dit onderwerp is [les ...](...) gepresenteerd in collegevorm tot ....

## Oefeningen
Opgaves ... in hoofdstuk 6 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013`. Antwoorden zijn [hier](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol2/Chapter5/) beschikbaar.