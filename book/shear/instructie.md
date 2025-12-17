# Instructie

De vorige keer hebben we gekeken naar [schuifspanningen in rechthoekige doorsnedes](../shear_rect/instructie.md). In deze instructie breiden we dat uit naar schuifspanningen in algemene dikwandige doorsnedes.

## Implicaties model schuifspanningen voor niet-rechthoekige dikwandige doorsneden

### Beperkingen van het model

Tijdens de afleiding van de schuifspanningsformule had ons model een aantal aannames. Voor niet-rechthoekige doorsnedes komen daar nog een aantal bij.

De eerdere aanname [ons model is alleen geldig als de schuifspanningen evenredig verdeeld zijn over het afschuifvlak](gemiddelde_schuifspanning) is voor niet-rechthoekige doorsnedes ook van belang vanwege de variatie in afschuivende delen. Voor elk afschuivend deel geldt dat het model alleen geldig is als de breedte van de het afschuivend deel veel kleiner is dan de hoogte van de afschuivend deel. Voor niet-rechthoekige doorsneden, die verschillende delen kunnen hebben met verschillende breedte-hoogte verhoudingen, kan deze aanname dus ook zorgen voor een ongeldig model voor een **deel** van de doorsnede.

```{figure} ./instructie_data/samengesteld.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear

Voor samengestelde doorsneden is het schuifspanningsmodel alleen geldig in de afschuivende delen waar $h \gg b$ geldt. In deze doorsnede is dat alleen in het lijf.
```

De overgangen van verschillende delen van een doorsnede zijn echter ook problematisch. Uit elasticiteitstheorie blijkt namelijk dat bij overgangen in breedte de schuifspanningen niet meer evenredig verdeeld.

```{figure} ./instructie_data/bsprong.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear

In de getoonde afschuifvlakken zitten dicht bij een (plotselinge) overgang in de breedte van de doorsnede. De schuifspanningen zijn daar dus niet evenredig verdeeld.
```

Daarnaast heeft de observatie dat de schuifspanningen dwars op de vrije randen van een doorsnede nul moeten zijn ook invloed op de geldigheid van ons model voor niet-rechthoekige doorsneden. Ons model geeft schuifspanning in de richting loodrecht op het afschuifvlak, maar als de randen van de doorsnede niet in diezelfde lopen loopt een component van de schuifspanning in de richting van de vrije rand. Die component moet daar nul zijn, wat niet gegarandeerd is met ons model.

```{figure} ./instructie_data/randen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear

Links de schuifspanningen volgens ons model, rechts nulspanningen getoond loodrecht op de vrije randen. Op diagonale randen kunnen deze spanningen niet matchen, waarmee het model dus ongeldig is.
```

Daarmee kunnen we de schuifspanningsformule voor dikwandige doorsneden dus alleen toepassen op afschuivende vlakken die:

- Door delen waar de breedte veel kleiner is dan de hoogte
- Ver af liggen van overgangen in breedte van de doorsnede
- Waarvan de vrije randen niet loodrecht op de afschuifvlakken lopen.

Als niet aan deze voorwaarden wordt voldaan zou wel een totale kracht kunnen worden gevonden die moet worden overgedragen in het afschuivend vlak, maar de verdeling van de schuifspanningen in dat vlak kan niet worden bepaald met de schuifspanningsformule.

### Schuifspanningen in andere richtingen

Niet-rechthoekige doorsnedes zouden kunnen voldoen aan alle aannames, maar niet in de $y$- of $z$-richting. Als er een afschuifvlak wordt genomen dat niet loodrecht op de $z$-as staat, bijvoorbeeld een verticaal afschuifvlak in het $y,z$-vlak, dan kan ons schuifspanningsmodel ook worden toegepast. Net zoals voorheen moet het afschuifvlak loodrecht op de randen worden genomen. De schuifspanning die dan wordt berekend is de schuifspanning loodrecht op het snedevlak en evenwijdig aan de rand, maar dus niet per sé in de $z$-richting.

```{figure} ./instructie_data/nonz.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear

Afschuifvlakken in verschillende richtingen, maar altijd loodrecht op de rand
```

## Voorbeeld

Het bepalen van de schuifspanningen voor een niet-rechthoekige doorsnede wordt getoond op onderstaande voorbeeld.

::::::{prf:example}
:nonumber: true

```{figure} ./instructie_data/voorbeeld.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear

Doorsnede en constructie
```

Gevraagd is om zoveel mogelijk informatie te geven over de absolute waarde van de schuifspanningen in een doorsnede bij $\rm{A}$

Allereerst kunnen we de afschuifvlakken bepalen waar we de schuifspanningen kunnen berekenen. Deze afschuifvlakken moeten loodrecht op de randen worden genomen. Daarnaast mag het afschuifvlak niet genomen worden in de buurt van een overgang in breedte. Dat heeft tot gevolg dat de afschuifvlakken alleen in de getoonde delen kan worden genomen.


Voor deze delen geldt dat $h \gg b$, dus we kunnen de schuifspanningsformule toepassen. We berekenen de schuifspanningen in de verschillende delen:

::::::

## Alternatieve uitleg en voorbeeld
In voorbeeld 2 van hoofdstuk 5.4 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` komt een deel van de conclusies van dit hoofdstuk ook aan bod.

% ## Instructies in collegevorm
%
% Dit onderwerp is [les ...](...) gepresenteerd in collegevorm tot ....

## Oefeningen
Opgaves 5.7, 5.8, 5.29, 5.30, 5.32a-b in hoofdstuk 5 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013`. Antwoorden zijn [hier](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol2/Chapter5/) beschikbaar.
