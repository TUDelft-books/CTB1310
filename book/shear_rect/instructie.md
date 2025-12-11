# Instructie

Tot nu toe hebben we enkel gerekend aan normaalspanningen, en enkel door buiging en verlenging/verkorting. Tijdens buiging treden er echter ook schuifspanningen op in de doorsnede: schuifspanningen die langs een een snede werken in plaats van loodrecht daarop. Dit is voor te stellen door twee op elkaar liggende balken te beschouwen die doorbuigen. Als je deze twee balken aan elkaar zou willen lijmen zodat deze werken als één balk zouden schuifspanningen nodig zijn die de vervormingen door buiging enigszins tegengaan:

```{figure} ./instructie_data/stacked.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Twee op elkaar liggende balken. Voor het samenvoegen zouden schuifspanningen nodig zijn zoals rechts getoond.
```

## Model

Voor het bepalen van schuifspanningen kijken we naar het evenwicht van een stukje van een balk

```{figure} ./instructie_data/beam_section.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Stukje balk van lengte $\Delta x$ met daarop snedekrachten $V_z$ en $M_z$. Het moment op de rechter doorsnede is $\Delta M$ groter dan dat op de linker doorsnede.
```

We kunnen de spanningen bepalen op de doorsnedes. De schuifspanningen zijn nog onbekend, maar voor de normaalspanningen geldt de eerder afgeleide formule $\sigma = \cfrac{M_z z}{I_{zz}}$.

```{figure} ./instructie_data/spanningen_section.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Boven de nog onbekende schuifspanningen. Onder de normaalspanningen.
```

::::::{prf:assumption}
:nonumber: true


We negeren de afschuifvervorming, enkel de vervormingen door extensie / buiging nemen we mee in de daaruit volgende normaalspanningen. De schuifspanningen en afschuifvervorming zijn dus niet één-op-één gerelateerd in ons model, waar dat bij normaalspanningen wel het geval is.

```{figure} ./instructie_data/afschuiving.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Een klein stukje materiaal dat wordt belast door schuifspanningen en normaalspanningen kan vervormen door zowel afschuiving als extensie, maar in ons model nemen we enkel de extensie mee om de schuifspanningen te bepalen.
```

De aannames die we hebben gebruikt voor normaalspanningen zijn dus nog steeds geldig:
- De doorsnedes blijven vlak en loodrecht op 'vezels' staan, waarmee het rekverloop lineair is
- Normaalspanningen en -rekken hebben een lineair verband, waarmee de vorm van het spanningsverloop gelijk is aan die van het rekverloop.

Tijdens de afleiding van de formules voor normaalspanningen werden daarnaast nog een aantal aannames gedaan. Aangezien we door gaan bouwen op hetzelfde model, zullen deze aannames ook gelden voor schuifspanningen:
- Het assenstelsel grijpt aan in het normaalkrachtencentrum van de doorsnede. Hierdoor vervallen de statisch momenten $S_y$ en $S_z$ in de vergelijkingen.
- De doorsnede is symmetrisch in de $y$- en/of $z$-richting / krachten grijpen aan in de hoofdassen van de doorsnede. Hierdoor vervallen de termen met $I_{yz}$ en zijn spanniningen in de $y$- en $z$-richting onafhankelijk van elkaar.
- De doorsnede heeft een homogene verdeling van rekstijfheid $E$, waarmee de locatie van het normaalkrachtencentrum en traagheidsmomenten onafhankelijk van de rekstijfheid bepaald kunnen worden en de rekverdeling gelijk is van vorm aan de spanningsverdeling.

::::::

Nu stellen we een vrijlichaamsschema op met spanningen voor een deel van de doorsnede, het zogenaamde afschuivend deel. Hierop werken dezelfde spanningen, met op het doorgesneden vlak geen normaalspanning maar wel een mogelijk schuifspanning.

```{figure} ./instructie_data/spanningen_afschuivend.svg
:align: center
%:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Spanningen op een afschuivend deel van de doorsnede. $t$ is de dikte van de doorsnede in de dwarsrichting $y$. $A^{\rm{a}}$ is het oppervlakte van de linker en rechter doorsnede, $A^{\parallel}$ is het oppervlakte van de onderste doorsnede
```


Door het evenwicht in de langsrichting op te stellen, kunnen we de schuifspanning bepalen:

$$
\sum F_x = 0 \to \tau_{\rm{gem}} = -\cfrac{V_{z} \, S_{z}^{\rm{a}}}{t \, I_{zz}}
$$


::::::{prf:assumption}
:nonumber: true

Om het evenwicht op te stellen kunnen we alleen de resulterende schuifkracht bepalen, de verdeling is daarmee onbekend. We kunnen daarmee alleen maar de gemiddelde schuifspanning bepalen.

Daarnaast gaan we in deze berekeningen uit van dezelfde $I_{zz}$ in de linker en rechter doorsnede, wat betekent dat we aannemen dat de doorsnede niet verandert over de lengte van de balk; dus een prismatische balk.

::::::

::::::{admonition} Volledige afleiding
:class: notation, dropdown

$$
\begin{align*}
\sum F_x &= 0 \\
-\int_{A^{\rm{a}}} \sigma_{\text{linker doorsnede}} \, dA^{\rm{a}} + \int_{A^{\rm{a}}} \sigma_{\text{rechter doorsnede}}  \, dA^{\rm{a}} + \int_{A^{\parallel}} \tau \left( x\right) \, dA^{\parallel} &= 0 \\
\underbrace{-\int_{A^{\rm{a}}} \cfrac{M_z \, z}{I_{zz,\text{linker doorsnede}}} \, dA^{\rm{a}} + \int_{A^{\rm{a}}} \cfrac{M_z \, z}{I_{zz,\text{rechter doorsnede}}} \, dA^{\rm{a}}}_{\text{Als }I_{zz,\text{linker doorsnede}} = I_{zz,\text{linker doorsnede}}=I_{zz} \text{vervallen deze termen}} + \int_{A^{\rm{a}}} \cfrac{\Delta M_z \,z}{I_{zz}} \, dA^{\rm{a}} + \int_{A^{\parallel}} \tau \left( x\right) \, dA^{\parallel} &= 0 \\
 \int_{A^{\rm{a}}} \cfrac{\Delta M_z \,z}{I_{zz}} \, dA^{\rm{a}} + \underbrace{\int_{A^{\parallel}} \tau \left( x\right) \, dA^{\parallel}}_{\text{Als }\tau \left( x\right) = \tau_{\rm{gem}} \text{kan deze uit de integraal worden gehaald} } &= 0 \\
\cfrac{\Delta M_z}{I_{zz}} \int_{A^{\rm{a}}} z \, dA^{\rm{a}} + \tau_{\rm{gem}} \int_{A^{\parallel}} \, dA^{\parallel} &= 0 \\
\cfrac{\Delta M_z}{I_{zz}} S_{z}^{\rm{a}} + \tau_{\rm{gem}} A^{\parallel} &= 0 \\
\cfrac{\Delta M_z}{I_{zz}} S_{z}^{\rm{a}} + \tau_{\rm{gem}} \, t \, \Delta x &= 0 \\
\lim_{\Delta x \to 0} \tau_{\rm{gem}} &= \lim_{\Delta x \to 0} \cfrac{- \cfrac{\Delta M_z}{\Delta x} \, S_{z}^{\rm{a}}}{t \, I_{zz}} \\
\tau_{\rm{gem}} &= -\cfrac{V_z \, S_{z}^{\rm{a}}}{t \, I_{zz}}
\end{align*}
$$

::::::

## Implicaties model voor schuifspanningen
