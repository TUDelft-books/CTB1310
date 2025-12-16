# Instructie

De vorige keer hebben we gekeken naar [schuifspanningen in rechthoekige doorsnedes](../shear_rect/instructie.md). In deze instructie breiden we dat uit naar schuifspanningen in algemene dikwandige doorsnedes.

## Model

### Beperkingen van het model voor niet-rechthoekige dikwandige doorsneden

Tijdens de afleiding van de schuifspanningsformule had ons model een aantal aannames. Een aanname was voor rechthoekige doorsnedes als een grote aanname: [ons model is alleen geldig als de schuifspanningen evenredig verdeeld zijn over het afschuifvlak](gemiddelde_schuifspanning). Dit is alleen het geval als de breedte van de het afschuivend deel veel kleiner is dan de hoogte van de afschuivend deel. Voor niet-rechthoekige doorsneden, die verschillende delen kunnen hebben met verschillende breedte-hoogte verhoudingen, kan deze aanname dus zorgen voor een ongeldig model voor een deel van de doorsnede.

```{figure} ./instructie_data/samengesteld.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear

Voor samengestelde doorsneden is het schuifspanningsmodel alleen geldig in de afschuivende delen waar $h \gg b$ geldt. In deze doorsnede is dat alleen in het lijf.
```

De overgangen van verschillende delen van een doorsnede zijn echter ook problematisch. Uit elasticiteitstheorie blijkt namelijk dat bij overgangen in breedte de schuifspanningen niet meer evenredig verdeeld.

```{figure} ./instructie_data/bsprong.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear

In de twee getoonde afschuifvlakken zitten dicht bij een overgang in de breedte van de doorsnede. De schuifspanningen zijn daar dus niet evenredig verdeeld.
```

Daarnaast heeft de observatie dat de schuifspanningen dwars op de vrije randen van een doorsnede nul moeten zijn ook invloed op de geldigheid van ons model voor niet-rechthoekige doorsneden. Ons model geeft schuifspanning in de $x$- en $z$-richting, maar als de randen van de doorsnede niet niet in de $z$-richting lopen loopt een component van de schuifspanning in de richting van de vrije rand. Die component moet daar nul zijn, wat niet gegarandeerd is met ons model.

```{figure} ./instructie_data/randen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear

Links de schuifspanningen volgens ons model, rechts nulspanningen getoond loodrecht op de vrije randen. Op diagonale randen kunnen deze spanningen niet matchen, waarmee het model dus ongeldig is.
```

Daarmee kunnen we de schuifspanningsformule voor dikwandige doorsneden dus alleen toepassen op afschuivende vlakken die:

- Door delen waar de breedte veel kleiner is dan de hoogte
- Ver af liggen van overgangen in breedte van de doorsnede
- Waarvan de vrije randen in de $y$- of $z$-richting lopen.

Als niet aan deze voorwaarden wordt voldaan zou wel een totale kracht kunnen worden gevonden die moet worden overgedragen in het afschuivend vlak, maar de verdeling van de schuifspanningen in dat vlak kan niet worden bepaald met de schuifspanningsformule.

### Schuifspanningen in andere richtingen

Als er een afschuifvlak wordt genomen dat niet loodrecht op de $z$-as staat, bijvoorbeeld een afschuifvlak in de $x$-richting, dan kan ons schuifspanningsmodel ook worden toegepast. Net zoals voorheen moet het afschuifvlak loodrecht op de randen worden genomen. De schuifspanning die dan wordt berekend is de schuifspanning loodrecht op het snedevlak en evenwijdig aan de rand, maar dus niet per sé in de $z$-richting.

```{figure} ./instructie_data/nonz.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear

Afschuifvlakken in verschillende richtingen, maar altijd loodrecht op de rand
```

## Voorbeeld

Het bepalen van de wringende momentenlijn wordt getoond op onderstaande voorbeeld.

::::::{prf:example}
:nonumber: true

...

::::::

## Alternatieve uitleg en voorbeeld
In voorbeeld 2 van hoofdstuk 5.4 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` komt een deel van de conclusies van dit hoofdstuk ook aan bod.

% ## Instructies in collegevorm
%
% Dit onderwerp is [les ...](...) gepresenteerd in collegevorm tot ....

## Oefeningen
Opgaves 5.7, 5.8, 5.29, 5.30, 5.32a-b in hoofdstuk 5 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013`. Antwoorden zijn [hier](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol2/Chapter5/) beschikbaar.
