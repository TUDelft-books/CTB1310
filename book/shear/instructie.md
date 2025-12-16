# Instructie

De vorige keer hebben we gekeken naar [schuifspanningen in rechthoekige doorsnedes](../shear_rect/instructie.md). In deze instructie breiden we dat uit naar schuifspanningen in algemene dikwandige doorsnedes.

## Model

Tijdens de afleiding van de schuifspanningsformule had ons model een aantal aannames. Een aanname was voor rechthoekige doorsnedes als een grote aanname: [ons model is alleen geldig als de schuifspanningen evenredig verdeeld zijn over het afschuifvlak](gemiddelde_schuifspanning). Dit is alleen het geval als de breedte van de doorsnede veel kleiner is dan de hoogte van de doorsnede. Voor niet-rechthoekige doorsneden, die verschillende delen kunnen hebben met verschillende breedte-hoogte verhoudingen, kan deze aanname dus zorgen voor een ongeldig model voor een deel van de doorsnede.

```{figure} ./instructie_data/samengesteld.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear

Voor samengestelde doorsneden is het schuifspanningsmodel alleen geldig in de delen waar $h \gg b$ geldt. In deze doorsnede is dat alleen in het lijf.
```

De overgangen van verschillende delen van een doorsnede zijn echter ook problematisch. Uit elasticiteitstheorie blijkt namelijk dat bij overgangen in breedte de schuifspanningen niet meer evenredig verdeeld.

```{figure} ./instructie_data/bsprong.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear

In de twee getoonde afschuifvlakken zitten dich bij een overgang in de breedte van de doorsnede. De schuifspanningen zijn daar dus niet evenredig verdeeld.
```

Daarnaast heeft de observatie dat de schuifspanningen dwars op de vrije randen van een doorsnede nul moeten zijn ook invloed op de geldigheid van ons model voor niet-rechthoekige doorsneden. Ons model geeft schuifspanning in de $x$- en $z$-richting, maar als de randen van de doorsnede niet niet in de $z$-richting lopen loopt een component van de schuifspanning in de richting van de vrije rand. Die component moet daar nul zijn, wat niet gegarandeerd is met ons model.

```{figure} ./instructie_data/randen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear

Links de schuifspanningen volgens ons model, rechts nulspanningen getoond loodrecht op de vrije randen. Op diagonale randen kunnen deze spanningen niet matchen, waarmee het model dus ongeldig is.
```

Daarmee kunnen we de schuifspanningsformule voor dikwandige doorsneden dus alleen toepassen op afschuivende vlakken die:

- Als 
- Ver af liggen van overgangen in breedte van de doorsnede
- Waarvan de vrije randen in de $y$- of $z$-richting lopen.

## Voorbeeld

Het bepalen van de wringende momentenlijn wordt getoond op onderstaande voorbeeld.

::::::{prf:example}
:nonumber: true

...

:::::

## Alternatieve afleiding
In hoofdstuk ... van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` wordt een alternatief model afgeleid gegeven voor het bepalen van schuifspanningen.

## Meer voorbeelden
In hoofdstuk ... van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` worden meer voorbeelden gegeven van het bepalen van schuifspanningen in verschillende situaties.

% ## Instructies in collegevorm
%
% Dit onderwerp is [les ...](...) gepresenteerd in collegevorm tot ....

## Oefeningen
Opgaves ... in hoofdstuk 5 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013`. Antwoorden zijn [hier](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol2/Chapter6/) beschikbaar.