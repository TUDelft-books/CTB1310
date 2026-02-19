# Instructie

De vorige keer hebben we gekeken naar [schuifspanningen in rechthoekige doorsnedes](../shear_rect/instructie.md). In deze instructie breiden we dat uit naar schuifspanningen in algemene dikwandige doorsnedes.

## Relatie met elasticiteitstheorie

Onze schuifspanningsmodel is gebaseerd op een aantal aannames om van snedekrachten naar spanningen te komen. Een meer geavanceerde manier om spanningen in constructies te bepalen is met (complexe) elasticiteitstheorie. Vaak wordt die theorie opgelost met computersimulaties, waarmee spanningen op elk punt in de doorsnede kunnen worden bepaald. Deze simulaties kunnen de beperkingen van ons model bevestigen.

:::::{prf:example}
:nonumber: true

Hieronder is een voorbeeld van simulatie getoond op basis van elasticiteitstheorie op doorsnedeniveau. De vectoren geven de richting aan van de schuifspanningen en de kleur en grootte de absolute waarde (donkerblauw lage waarde, donkerrood hoge waarde).

```{figure} ./instructie_data/RC-B_05_34.png
:align: center
:bib: IDEAStatiCa_shear_RCS
:show: author, license, copyright, source
:placement: caption
:name: simulation_shear_stresses
:number:
```
:::::

## Implicaties model schuifspanningen voor niet-rechthoekige dikwandige doorsneden

### Beperkingen van het model

Tijdens de afleiding van de schuifspanningsformule had ons model een aantal aannames. Voor niet-rechthoekige doorsnedes komen daar nog een aantal bij.

De eerdere aanname waarmee ons model alleen geldig is als de schuifspanningen evenredig verdeeld zijn over het afschuifvlak is voor niet-rechthoekige doorsnedes ook van belang vanwege de variatie in afschuivende delen. Voor elk afschuivend deel geldt dat het model alleen geldig is als de breedte van de het afschuivend deel veel kleiner is dan de hoogte van de afschuivend deel. Voor niet-rechthoekige doorsneden, die verschillende delen kunnen hebben met verschillende breedte-hoogte verhoudingen, kan deze aanname dus ook zorgen voor een ongeldig model voor een **deel** van de doorsnede. 

:::::{prf:example}
:nonumber: true

In onderstaande doorsnede is het schuifspanningsmodel alleen geldig in het lijf.

```{figure} ./instructie_data/samengesteld.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```

:::::

De overgangen van verschillende delen van een doorsnede zijn echter ook problematisch. Uit elasticiteitstheorie blijkt namelijk dat bij overgangen in breedte de schuifspanningen niet meer evenredig verdeeld.

:::::{prf:example}
:nonumber: true

De getoonde afschuifvlakken in onderstaande figuur zitten dicht bij een (plotselinge) overgang in de breedte van de doorsnede. De schuifspanningen zijn daar dus niet evenredig verdeeld.

```{figure} ./instructie_data/bsprong.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```

:::::

Daarnaast heeft de observatie dat de schuifspanningen dwars op de vrije randen van een doorsnede nul moeten zijn ook invloed op de geldigheid van ons model voor niet-rechthoekige doorsneden. Ons model geeft schuifspanning in de richting loodrecht op het afschuifvlak, maar als de randen van de doorsnede niet in diezelfde lopen loopt een component van de schuifspanning in de richting van de vrije rand. Die component moet daar nul zijn, wat niet gegarandeerd is met ons model.

:::::{prf:example}
:nonumber: true

In onderstaande figuur kunnen de verticale spanningen niet matchen met de eis van nulspanningen loodrecht op de twee schuine vrije randen, waarmee het model dus ongeldig is.

```{figure} ./instructie_data/randen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear

Links de schuifspanningen volgens ons model met horizontale afschuifvlakken, rechts nulspanningen getoond loodrecht op de vrije randen.
```

:::::

Daarmee kunnen we de schuifspanningsformule voor dikwandige doorsneden dus alleen toepassen op afschuivende vlakken:

- die door delen gaan waar de breedte veel kleiner is dan de hoogte
- die ver af liggen van overgangen in breedte van de doorsnede
- waarvan de vrije randen loodrecht op de afschuifvlakken lopen.

Als niet aan deze voorwaarden wordt voldaan zou wel een totale kracht kunnen worden gevonden die moet worden overgedragen in het afschuivend vlak, maar de verdeling van de schuifspanningen in dat vlak kan niet worden bepaald met de schuifspanningsformule.

### Schuifspanningen in andere richtingen

Niet-rechthoekige doorsnedes zouden kunnen voldoen aan alle aannames, maar niet in de $y$- of $z$-richting. Als er een afschuifvlak wordt genomen dat niet loodrecht op de $z$-as staat, bijvoorbeeld een verticaal afschuifvlak in het $y,z$-vlak, dan kan ons schuifspanningsmodel ook worden toegepast. Net zoals voorheen moet het afschuifvlak loodrecht op de randen worden genomen. De schuifspanning die dan wordt berekend is de schuifspanning loodrecht op het snedevlak en evenwijdig aan de rand, maar dus niet per sé in de $z$-richting.

:::::{prf:example}
:nonumber: true

In onderstaande figuur zijn een aantal mogelijke afschuifvlakken getoond, altijd loodrecht op de vrije randen van de doorsnede.

```{figure} ./instructie_data/nonz.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```

:::::

Voor verticale afschuifvlakken (in horizontale doorsnededelen) geldt dat de schuifspanningen linear verlopen over de 'hoogte' (in horizontale richting) van het constructiedeel, mits de breedte van het afschuifvlak constant blijft. Dit kan op vergelijkbare wijze worden afgeleid als het parabolisch verband wat werd gevonden voor horizontale afschuifvlakken in verticale delen.

::::::{admonition} Volledige afleiding
:class: notation, dropdown

Om het schuifspanningsverloop te bepalen, kunnen we de formule voor de gemiddelde schuifspanning herschrijven door het statisch moment uit te werken voor een constante breedte:

$$
\begin{align*}
\tau_{\rm{gem}} &= -\cfrac{V_z \, S_{z}^{\rm{a}}}{b \, I_{zz}} \\
\tau_{\rm{gem}} &= -\cfrac{V_z \, \int_{A^{\rm{a}}} z \, dA^{\rm{a}} }{b \, I_{zz}} \\
\tau_{\rm{gem}} &= -\cfrac{V_z \, z \int_{A^{\rm{a}}} \, dA^{\rm{a}} }{b \, I_{zz}} \\
\tau_{\rm{gem}} &= -\cfrac{V_z \, z \, A^{\rm{a}}}{b \, I_{zz}}
\end{align*}
$$

Het statisch moment is dus niet afhankelijk van $z$, waarmee de spanning alleen maar toeneemt door de lineair toenemende waarde van $A^{\rm{a}}$.

::::::

In plaats van $h \gg b$ geldt voor gekromde delen van de constructie dat $R \gg b$ moet gelden, met $R$ de straal van kromming van het gekromde deel.

:::::{prf:example}
:nonumber: true

In onderstaande figuur is links de kromming te sterk om een evenredige schuifspanningsverdeling te garanderen, terwijl dat rechts wel het geval is.

```{figure} ./instructie_data/rondingen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```

:::::

In theorie zouden ook niet-vlakke afschuifvlakken kunnen worden genomen, maar dat vereist kennis uit de elasticiteitstheorie om evenredige verdelingen te kunnen garanderen. Daarom beperken we ons tot vlakke afschuifvlakken.

:::::{prf:example}
:nonumber: true

In onderstaande figuur zijn mogelijke gekromde afschuifvlakken getoond.

```{figure} ./instructie_data/curved.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```

:::::

Geknikt afschuifvlakken zijn wel toegestaan, zolang elk vlakdeel maar loodrecht op de randen staat en voldoen aan de andere voorwaarden. Als een symmetrische doorsnede symmetrisch wordt doorgesneden, kunnen we uitgaan van een evenredig verdeelde schuifspanning op elk vlakdeel.

:::::{prf:example}
:nonumber: true

In onderstaande figuur is een mogelijke geknikte afschuifvlak getoond.

```{figure} ./instructie_data/geknikt.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```

:::::

Ongeacht dat de richting van de schuifspanningen en daarmee de richting van het afschuifvlak niet altijd te bepalen zijn, kunnen we vanwege symmetrie op sommige delen van de doorsnede wel de richting bepalen (zonder waarde). In het middel van de getoonde doorsnedes moet de schuifspanning wel verticaal lopen, anders is er geen symmetrisch schuifspanningsverloop mogelijk.

:::::{prf:example}
:nonumber: true

In onderstaande doorsnedes is de richting van de schuifspanningen dus bekend in het midden van de doorsnede vanwege symmetrie.

```{figure} ./instructie_data/werklijn_bekend.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```

:::::

## Voorbeeld

Het bepalen van de schuifspanningen voor een niet-rechthoekige doorsnede wordt getoond op onderstaande voorbeeld.

::::::{prf:example}
:nonumber: true

```{figure} ./instructie_data/voorbeeld.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```

Gevraagd is de absolute waarde van schuifspanningen ergens op een positieve doorsnede bij $\rm{A}$.

Allereerst kunnen we de afschuifvlakken bepalen waar we de schuifspanningen kunnen berekenen. Deze afschuifvlakken moeten loodrecht op de randen worden genomen. Daarnaast mag het afschuifvlak niet genomen worden in de buurt van een overgang in breedte. Dat heeft tot gevolg dat de afschuifvlakken alleen in de getoonde delen kunnen worden genomen. Links zijn afschuifvlakken getoond die niet mogelijk zijn, rechts mogelijke afschuifvlakken.

```{figure} ./instructie_data/mogelijke_afschuifvlakken.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```

We kunnen de schuifspanningen dus alleen bepalen in het diagonale gedeelte en dan niet te dicht bij de hoeken. We kiezen daarom voor een afschuifvlak op een vrij willekeurige hoogte van $\bar{z} = -48 \, \rm{mm}$.

```{figure} ./instructie_data/snede.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```

Nu moeten we eerst de doorsnedegrootheden worden bepaald, beginnend met het oppervlakte $A$.

```{figure} ./instructie_data/A.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```

$$
A = 280 \cdot 140 \cdot \cfrac{1}{2} - 200 \cdot 100 \cfrac{1}{2} = 9600 \, \rm{mm^2}
$$

Vervolgens kunnen we het zwaartepunt/normaalkrachtencentrum bepalen. Daarvoor verdelen we de constructie in parallellogrammen en driehoeken, elk met een eigen zwaartepunt ($\rm{C}$)

```{figure} ./instructie_data/statisch_moment.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```

$$
\bar{z}_{\rm{N.C.}} = \cfrac{40 \cdot 100 \cdot 50 \cdot 2 + 80 \cdot 40 \cdot \cfrac{1}{2} \cdot \left(100 + \cfrac{1}{3} \cdot 40 \right)}{9600} = 60.\bar{5} \, \rm{mm}
$$

Daarmee kan het traagheidsmoment $I_{zz}$ worden bepaald, gebruik makend van dezelfde onderverdeling als voor het zwaartepunt.

$$
\begin{align*}
I_{zz} = &  \,2 \cdot \left( \cfrac{1}{12} \cdot 40 \cdot 100^3 + 100 \cdot 40\ \cdot \left(60.\bar{5} - 50 \right)^2 \right) \\
& + \cfrac{1}{36} \cdot 80 \cdot 40^3 + 80 \cdot 40 \cdot \cfrac{1}{2} \cdot \left(60.\bar{5} - \left(100 + \cfrac{1}{3} \cdot 40 \right) \right)^2 \\
\approx & \, 12.2 \cdot 10^6 \, \rm{mm^4}
\end{align*}
$$

Nu kan het statisch moment van het afschuivend deel worden bepaald. We kiezen voor een afschuifvlak met de hartlijn op $\bar{z} = -48 \, \rm{mm}$. Het afschuivend deel nemen we het deel onder deze snede, hoewel we ook het andere deel hadden kunnen nemen, maar dat is complexer. Dit afschuivend deel is verdeeld in een gekantelde rechthoek en driehoek, waarvan de afmetingen volgen uit de goniometrie van de doorsnede. In onderstaande figuur is het afschuivend deel met afmetingen getoond, met de $\rm{N.C.}$ van de hele doorsnede op $60.\bar{5} \, \rm{mm}$ vanaf de onderkant en het snijpunt van afschuifvlak en hartlijn op $-48 \, \rm{mm}$


```{figure} ./instructie_data/Sa.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```

$$
\begin{align*}
S_{z}^{\rm{a}} = & \, 40 \cdot 20 \cdot \cfrac{1}{2} \cdot \left(60.\bar{5} - \cfrac{20}{3} \right)\\
& + 20 \sqrt{2} \cdot 38 \sqrt{2} \cdot \left(60.\bar{5} - \cfrac{38}{2} \right) \\
= & \, 84720 \, \rm{mm}^3 \\
\end{align*}
$$

Dit geeft:

$$
\tau = \cfrac{\left| V_z \, S_{z}^{\rm{a}} \right| }{I_{zz} \, t} \approx \cfrac{\left| 120000 \cdot 84720\right|}{12.2 \cdot 10^6 \cdot 20 \sqrt{2}} \approx 29.6 \, \rm{MPa}
$$

Het resultaat is dus een evenredig verdeelde schuifspanning op ons schuifvlak. De werklijn is dwars op het afschuifvlak en evenwijdig aan de rand en de richting is nog niet bepaald. Het bepalen van de richting passen we pas een volgende keer toe bij dunwandige doorsneden. In onderstaande figuur is deze schuifspaning getoond.


```{figure} ./instructie_data/resultaat.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear
:number:
```


::::::

## Alternatieve uitleg en voorbeeld
In voorbeeld 2 van hoofdstuk 5.4 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` komt een deel van de conclusies van dit hoofdstuk ook aan bod.

% ## Instructies in collegevorm
%
% Dit onderwerp is [les ...](...) gepresenteerd in collegevorm tot ....

## Oefeningen
[Opgaves 5.7, 5.8, 5.29, 5.30, 5.32a-b in hoofdstuk 5 van het boek Mechanica, spanningen, vervormingen en verplaatsingen](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/files/TM2vraagstukkenbundel.pdf) {cite:p}`Hartsuijker2013`. Antwoorden zijn [hier](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol2/Chapter5/) beschikbaar.
