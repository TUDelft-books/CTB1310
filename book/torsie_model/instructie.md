# Instructie

In de vorige les hebben we bekeken hoe we het wringend moment in een doorsnede kunnen bepalen. In deze les gaan we bekijken hoe we de spanningen kunnen berekenen ten gevolge van het wringend moment.

Het spanningsverloop ten gevolge van een wringend moment is over het algemeen erg complex en afhankelijk van het soort doorsnede. We zullen een aantal doorsnedes met bijbehorende modellen behandelen: ronde massieve doorsnedes en ringen (zowel dikwandig als dunwandig), dunwandige niet-ronde gesloten doorsnedes, en open dunwandige doorsnedes.

## Model ronde massieve doorsnedes en ringen

:::::::{prf:assumption}
:nonumber: true
:label: assump_torsion_model_1

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

:::::::

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
I_{\rm{p}} = 2 \cdot \pi \cdot R^3 \cdot t
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

Voor niet-ronde doorsnedes hebben we een andere aanpak nodig. De aannames van vlakke doorsnedes en rechte radiale lijnen zijn namelijk niet meer geldig. 

:::::::{prf:assumption}
:nonumber: true
:label: assump_torsion_model_2

We nemen voor dit model aan dat dat de schuifspanningen constant zijn over de wanddikte vanwege de dunwandigheid.
:::::::

Daarnaast moet voor een gesloten doorsnede gelden dat de richtingen van de schuifspanningen overeenkomen met het wringend moment.

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

Tot slot bekijken we open dunwandige doorsnedes.

Ook hier is de aanname van vlakke doorsnedes en rechte radiale lijnen niet meer geldig. Daarnaast kunnen we ook niet meer aannemen dat de schuifspanningen constant zijn over de wanddikte, omdat de doorsnede anders geen wringing kan weerstaan.

De meest simpele open doorsnede, een strip, kan geen wringend moment weerstaan als de schuifspanningen constant zijn over de wanddikte omdat de schuifspanningen allemaal in dezelfde richting lopen.

```{figure} ./instructie_data/simpel.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

Complexere open dunwandige doorsnedes zijn er natuurlijk ook, welke kunnen worden gezien als een combinatie van wandsegmenten en dus ook geen resultant wringed moment kunnen opleveren. Bijvoorbeeld een I-ligger kan worden gezien als een combinatie van drie wandsegmenten: twee flenzen en het lijf:

```{figure} ./instructie_data/dunwandig_i.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

:::::::{prf:assumption}
:nonumber: true
:label: assump_torsion_model_3

Omdat een constant schuifspanningsprofiel geen wringend moment kan opnemen wordt er een lineair toenemende schuifspanning aangenomen vanuit het midden van de wand naar de buitenkant. Deze spanningen lopen als het ware rond in de doorsnede en kunnen dus wel een resulterend wringend moment veroorzaken.

Dit lineaire verband is een versimpeling en in werkelijkheid is het spanningsverloop complexer. Zeker in de buurt van overgangen en hoeken schiet dit model tekort. Voor dunwandige doorsnedes zijn deze invloeden beperkt. Dit model is daarom alleen geschikt voor dunwandige doorsnedes, ook al wordt deze hieronder getoond als dikwandige doorsnede om het spanningsverloop duidelijk te maken.

```{figure} ./instructie_data/I-balk.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

:::::::

De open doorsnede modelleren we vervolgens als een verzameling van dunwandige niet-ronde gesloten doorsnedes waarin voor elke gesloten doorsnede de schuifspanning constant is over de hele doorsnede. Dit is toegestaan volgens onze voorgaande aanname van een lineaire spanningsverdeling als de gesloten dunwandige doorsnedes overal dezelfde afstand $e_{\rm{m}}$ hebben. Hieronder zijn twee van dergelijke dunwandige niet-ronde gesloten doorsnede getoond met $e_1$ en $e_2$:

```{figure} ./instructie_data/dunwandig_open_gesloten.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

:::::::{prf:assumption}
:nonumber: true
:label: assump_torsion_model_4

Hier worden dus ook de spanningen in de overgangen en hoeken gemodelleerd hoewel ons model daar niet accuraat is. Het foutief meenemen van die spanningen heeft daarmee ook een kleine invloed op de spanningen waar ons lineaire verband wel geldig is. Er wordt aangenomen dat dat effect klein is omdat voor dunwandige doorsnedes dat invloed van overgangen en hoeken klein is.

:::::::

Nu kunnen we voor elke van deze dunwandige gesloten doorsnedes het voorgaande model toepassen en deze individuele bijdrages te integreren over de halve wanddikte. Dit geeft de volgende formule voor de schuifspanningen in open dunwandige doorsnedes:

$$
\tau \left(e_{\rm{m}}\right) = \cfrac{M_t \cdot e_{\rm{m}}}{\frac{1}{2} \cdot I_{\rm{t}}}
$$

Met:
- $e_{\rm{m}}$ de afstand van het midden van de wand tot het punt waar de schuifspanning wordt berekend
- $I_t$ het torsietraagheidsmoment: $\sum\limits_{i}{\frac{1}{3} \cdot h_i \cdot t_i^3}$
    - $h_i$ de hoogte/lengte van een wandsegment $i$
    - $t_i$ de wanddikte van een wandsegment $i$

:::::{prf:example}
:nonumber: true

Voor de drie wandsegmenten van een I-ligger zijn de hoogtes en diktes van de wandsegmenten hieronder getoond:

```{figure} ./instructie_data/hent.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

De theorie en formule voor het wringtraagheidsmoment werkt ook voor gekromde wandsegmenten:

```{figure} ./instructie_data/rond.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

:::::

De 'arm' in orde grootte $e_{\rm{m}}$ van de schuifspanningen in deze open dunwandige is vele malen kleiner dan de 'arm' in gesloten doorsnedes in ordegrootte $h$. Hierdoor zouden de spanningen veel groter moeten zijn om hetzelfde wringend moment te kunnen weerstaan. In de praktijk betekent dit dat open dunwandige doorsnedes veel minder goed in staat zijn om wringing te weerstaan dan gesloten dunwandige doorsnedes.

::::::{admonition} Volledige afleiding
:class: notation, dropdown

Voor de volledige afleiding wordt verwezen naar hoofdstuk 6.3.2 en 6.3.3 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013`

::::::

## Stappenplan

Daarmee kunnen we de volgende aanpak beschrijven voor het bepalen van het schuifspanningsverloop in een doorsnede ten gevolge van wringing:

::::::{prf:algorithm} Bepalen schuifspanningsverloop in een doorsnede ten gevolge van wringing
:nonumber: true

1. Bereken het inwendig wringend moment $M_t$ in de doorsnede.
2. Kies het juiste model voor de doorsnede:
    - Ronde massieve doorsnede of ring: gebruik $\tau \left(r\right)= \cfrac{M_t \cdot r}{I_{\rm{p}}}$
    - Dunwandige niet-ronde gesloten doorsnede: gebruik $\tau = \cfrac{M_t}{2 \cdot A_{\rm{m}} \cdot t}$
    - Open dunwandige doorsnede: gebruik $\tau \left(e_{\rm{m}}\right) = \cfrac{M_t \cdot e_{\rm{m}}}{\frac{1}{2} \cdot I_{\rm{t}}}$
3. Leid het teken af van de schuifspanningen af aan de hand van de richting van het wringend moment.
4. Teken het schuifspanningsprofiel op de doorsnede.

::::::

## Voorbeeld

Het bepalen van de schuifspanningen ten gevolge van wringing wordt getoond in het volgende voorbeeld.

::::::{prf:example}
:nonumber: true

Gegevens is de volgende constructie en twee dunwandige doorsnedes:

::::{grid} 2 2 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/Constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```


De uitwendige krachten en  
oplegreacties grijpen aan  
in het dwarskrachtencentrum.

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/doorsnede_1.svg
:align: center
:name: fig:doorsnede_1
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```
:::

:::{grid-item}
:columns: auto

```{figure-start} ./instructie_data/doorsnede_2.svg
:align: center
:name: fig:doorsnede_2
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

Infinitesimaal smalle  
snede in lengterichting

```{figure-end}
```

:::

::::

Gevraagd is de spanningsverdeling in kolom $\rm{AB}$ in de gesloten doorsnede ({numref}`fig:doorsnede_1`) en in de open doorsnede ({numref}`fig:doorsnede_2`).

Allereerst bepalen we het wringend moment in de doorsnede:

```{figure} ./instructie_data/FBD_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

Evenwicht rondom as $\rm{AB}$ geeft:

$$
\begin{align*}
\sum T_{\rm{AB}} &= 0 \\
M_{\rm{t}}^{\rm{AB}} - 0.648 \cdot \pi \cdot 4 \cdot 2 &= 0 \\
M_{\rm{t}}^{\rm{AB}} &= 5.184 \cdot \pi \ \rm{kNm} \left( \twoheadleftarrow \mid \twoheadrightarrow \right)
\end{align*} 
$$

Dit is een positief wringend moment, dus op onze positieve doorsnede zal deze van $y$ naar $z$ draaien.

We hebben een ronde ring in de gesloten doorsnede ({numref}`fig:doorsnede_1`), dus we kunnen het overeenkomende model gebruiken. Als we de doorsnede dunwandig behandlen, is het polair traagheidsmoment:

$$
I_{\rm{p}} = 2 \cdot \pi \cdot R^3 \cdot t = 2 \pi \cdot 90^3 \cdot 8 = 11.664 \cdot \pi \cdot 10^6 \ \rm{mm^4}
$$

De schuifspanningen zijn dan:

$$
\tau = \cfrac{M_t \cdot r}{I_{\rm{p}}} = \cfrac{5.184 \cdot \pi \cdot 10^6 \cdot 90}{11.664 \cdot \pi \cdot 10^6} = 40 \, \rm{MPa}
$$

Dat geeft de volgende spanningen:

```{figure} ./instructie_data/spanningen_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

De andere doorsnede is een open dunwandige doorsnede ({numref}`fig:doorsnede_2`), dus daarvoor gebruiken we een ander model. We hebben geen model om deze doorsnede dikwandig te behandelen. Het torsietraagheidsmoment is:

$$
I_{\rm{t}} = \frac{1}{3} \cdot h \cdot t ^3 = \frac{1}{3} \cdot \pi \cdot 180 \cdot 8^3 = 30720 \cdot \pi \, \rm{mm}^4
$$

De schuifspanningen zijn $0$ middenin de wand van de doorsnede en nemen lineair toe naar buiten, de maximale schuifspanningen wordt dan:

$$
\tau = \cfrac{M_{\rm{t}} \cdot e_{\rm{m}}}{\frac{1}{2}\cdot I_{\rm{t}}} = \cfrac{5.184 \cdot \pi \cdot 10^6 \cdot 4}{\frac{1}{2} \cdot 30720 \cdot \pi} = 1350 \, \rm{MPa}
$$

Dit geeft het volgende schuifspanningsprofiel (met de dikte van de wand uitvergroot weergegeven):

```{figure} ./instructie_data/torsiespanning_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models
:number:
```

Deze spanning is vele malen hoger en waarschijnlijk kan deze doorsnede deze spanning niet weerstaan. De vervormingen zullen waarschijnlijk ook vele malen groter zijn, hoewel we dat hier niet hebben berekend.

::::::

## Meer voorbeelden
In hoofdstuk 6.4 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` worden meer voorbeelden gegeven van het bepalen van schuifspanningen in verschillende situaties. Negeer vraag d van voorbeeld 2 en b en c van voorbeeld 4. Voorbeeld 5, 6 en 8 worden in de volgende les behandeld.

## Instructies in collegevorm
Dit onderwerp is [in les 10](https://collegerama.tudelft.nl/Mediasite/Channel/public-ctb1310/watch/5e023361d22448879680afcaf5b210831d) gepresenteerd in collegevorm van 7:00 tot 1:01:10

## Oefeningen
[Opgaves 6.3 - 6.9a, 6.10a, 6.11a - 6.11b, 6.12, 6.13a, 6.14 - 6.21 in hoofdstuk 6 van het boek Mechanica, spanningen, vervormingen en verplaatsingen](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/files/TM2vraagstukkenbundel.pdf) {cite:p}`Hartsuijker2013`. Antwoorden zijn [hier](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol2/Chapter5/) beschikbaar.
