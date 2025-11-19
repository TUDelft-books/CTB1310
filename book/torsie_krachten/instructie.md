% Source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie

````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina houdt de notatie aan zoals geïntroduceerd in {cite:t}`Hartsuijker2013`

% Source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie
```
````

# Instructie

Tot nu toe hebben we enkel gerekend aan uitwendige krachten, en momenten en inwendige dwarskrachten, normaalkrachten en buigende momenten. Echter, op en in sommige constructies komen ook wringende momenten voor. Waar buigende momenten om de lokale $y$- of $z$-as werken en zorgen voor verplaatsingen in de $z$ ($M_z$) en $y$ ($M_y$) richting, werken wringende momenten om de $x$-as van de doorsnede en zorgen voor rotaties om de $x$-as ($M_{\rm{t}}$, met de $\rm{t}$ van 'torsion').

## Uitwendige momenten

De verschillende uitwendige momenten kunnen we zowel in 3D als 2D bekijken. De afspraak is dat een positief moment loopt van $x$ naar $y$, van $y$ naar $z$ en van $z$ naar $x$.

```{figure} ./instructie_data/moment_curved.svg
---
align: center
---
Uitwendige momenten in 3D en 2D met gekromde pijlen in de positieve richtingen
```

Omdat het zeker in 3D lastig is om de verschillende momenten te onderscheiden, worden deze vaak of in 2D getekend, of met pijlen met een dubbele pijlpunt aangegeven. De pijl geeft de as aan waarom het moment draait, waarbij de richting van de pijl met de rechterhandregel de richting van de draaiing aangeeft.

```{figure} ./instructie_data/moment_pijl.svg
---
align: center
---
Uitwendige momenten in 3D met pijlen met dubbele pijlpunt in de positieve richtingen
```

Verdeelde wringende momenten zijn ook mogelijk.

## Inwendige momenten

Inwendige momenten kunnen we op dezelfde manier onderscheiden als uitwendige momenten met gekromde pijlen of pijlen met dubbele pijlpunt. Echter, voor de positieve richtingen gelden andere afspraken:
- De buigende momenten $M_y$ en $M_z$ zijn positief als ze zorgen voor trek aan de positieve kant van de $y$- of $z$-as.
- Het wringende moment $M_{\rm{t}}$ is positief als het op een positieve $x$-vlak van $y$ naar $z$ draait. Op een negative $x$-vlak draait het torderend moment dan van $z$ naar $y$.

```{figure} ./instructie_data/inwendige_moment.svg
---
align: center
---
Inwendige wringende momenten in de positieve richtingen met gekromde pijlen of pijlen met dubbele pijlpunt
```

Daarmee kunnen we ook een vervormingsteken introduceren voor wringende momenten, geïnspireerd op het vrijlichaamsschema met de pijlen met dubbele pijlpunt. Deze kunnen we in een wringende momentenlijn gebruiken om de richting van de wringende momenten aan te geven. Het maakt niet uit of dit teken boven of onder de as wordt gezet.

```{figure} ./instructie_data/vervormingstekens.svg
---
align: center
---
Vervormingstekens voor wringende momenten
```
