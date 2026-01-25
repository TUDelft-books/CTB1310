% Source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie

````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina houdt de notatie aan zoals geïntroduceerd in {cite:t}`Hartsuijker2013`

```
````

# Instructie inleiding wringende momenten, wringende momentenlijn, evenwichtsvergelijking en differentiaalvergelijking

In de vorige les zijn wringende momenten al kort geïntroduceerd om het dwarskrachtencentrum te vinden. Vandaag gaan we dieper in op deze wringende momenten en wat er gebeurd als een kracht niet aangrijpt in het dwarskrachtencentrum.

## Uitwendige momenten

De verschillende uitwendige momenten kunnen we zowel in 3D als 2D bekijken. De afspraak is dat een positief moment loopt van $x$ naar $y$, van $y$ naar $z$ en van $z$ naar $x$. In 2D gaven we momenten vaak aan met een gekromde pijl, echter is dat in 3D niet altijd helemaal duidelijk.

:::::{prf:example}
:nonumber: true

In het volgende figuur zijn de positieve richtingen van de uitwendige momenten in 3D en 2D weergegeven met gekromde pijlen.

```{figure} ./instructie_data/moment_curved.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie
number:
---
```

:::::

Omdat het zeker in 3D lastig is om de verschillende momenten te onderscheiden, worden deze vaak of in 2D getekend, of met pijlen met een dubbele pijlpunt aangegeven. De pijl geeft de as aan waarom het moment draait, waarbij de richting van de pijl met de rechterhandregel de richting van de draaiing aangeeft.

:::::{prf:example}
:nonumber: true

In het volgende figuur zijn de positieve richtingen van de uitwendige momenten in 3D en 2D weergegeven met pijlen met dubbele pijlpunt.

```{figure} ./instructie_data/moment_pijl.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie
number:
---
```

:::::

Verdeelde wringende momenten zijn ook mogelijk.

## Inwendige momenten

Inwendige momenten kunnen we op dezelfde manier onderscheiden als uitwendige momenten met gekromde pijlen of pijlen met dubbele pijlpunt. Echter, voor de positieve richtingen gelden andere afspraken:
- De buigende momenten $M_y$ en $M_z$ zijn positief als ze zorgen voor trek aan de positieve kant van de $y$- of $z$-as.
- Het wringende moment $M_{\rm{t}}$ is positief als het op een positieve $x$-vlak van $y$ naar $z$ draait. Op een negative $x$-vlak draait het torderend moment dan van $z$ naar $y$.

:::::{prf:example}
:nonumber: true

In het volgende figuur zijn de positieve richtingen van de inwendige wringende momenten in 3D en 2D weergegeven met gekromde pijlen.

```{figure} ./instructie_data/inwendige_moment.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie
number:
---
```

:::::

### Wringende momentenlijn

Net als bij de andere snedekrachtenlijnen (momentenlijn, dwarskrachtenlijn, normaalkrachtenlijn) kunnen we ook een wringende momentenlijn tekenen. Daarvoor introduceren we een vervormingsteken, geïnspireerd op het vrijlichaamsschema met de pijlen met dubbele pijlpunt. Deze kunnen we in een wringende momentenlijn gebruiken om de richting van de wringende momenten aan te geven. Het maakt niet uit of dit teken boven of onder de as wordt gezet.

```{figure} ./instructie_data/vervormingstekens.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie
number:
---
```

Net als bij de buigende momentenlijn kunnen we een aantal eigenschappen van de wringende momentenlijn vinden:

- De wringende momentenlijn is constant als er geen verdeelde wringende momenten op de constructie werken. Dit verband volgt uit de differentiaalvergelijking zoals hieronder wordt afgeleid.
- De wringende momentenlijn springt bij een uitwendig wringend moment. Dit volgt uit het evenwicht rondom een uitwendige wringend moment.

## Evenwichtsvergelijkingen voor wringende momenten

Net zoals bij krachten en momenten voor buiging, kunnen we ook voor wringende momenten met evenwichtsvergelijkingen oplegreacties en inwendige wringende momenten bepalen. Daarvoor is de aanpak vergelijkbaar met die van buigende momenten: op basis van het het vrijlichaamsschema van de constructie of maak een een deel van de constructie wordt een evenwichtsvergelijking opgesteld. Deze evenwichtsvergelijkingen wordt opgesteld rondom een as: $\sum T_{\rm{as}} = 0$. Alle krachten, buigende en wringende momenten die een draaiing rondom deze as veroorzaken komen in deze evenwichtsvergelijking terecht.

## Differentiaalvergelijking voor wringing

Net als bij de differentiaalvergelijkingen voor buiging kan de differentiaalvergelijking voor wringing worden afgeleid door te kijken naar het vrijlichaamsschema van een klein element van infinitesimale lengte $\Delta x$ belast met wringende momenten:

```{figure} ./instructie_data/deltax.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie
number:
---
```

Evenwicht rondom de as van het element geeft:

$$
\begin{align*}
\sum T_{\rm{element}} &= 0 \\
- M_{\rm{t}} + q_{\rm{M}_{\rm{t}}} \cdot \Delta x +  M_{\rm{t}} + \Delta M_{\rm{t}} &= 0 \\
q_{\rm{M}_{\rm{t}}} \cdot \Delta x + \Delta M_{\rm{t}} &= 0 \\
\mathop {\lim }\limits_{\Delta x \to 0 } \left( \cfrac{\Delta M_{\rm{t}}}{\Delta x} \right) &= \mathop {\lim }\limits_{\Delta x \to 0 } \left( - q_{\rm{M}_{\rm{t}}} \right) \\
\cfrac{dM_{\rm{t}}}{dx} &= - q_{\rm{M}_{\rm{t}}}
\end{align*} 
$$