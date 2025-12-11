# Instructie

Tot nu toe hebben we enkel gerekend aan normaalspanningen, en enkel door buiging en verlenging/verkorting. Tijdens buiging treden er echter ook schuifspanningen op in de doorsnede: schuifspanningen die langs een een snede werken in plaats van loodrecht daarop. Dit is voor te stellen door twee op elkaar liggende balken te beschouwen die doorbuigen. Als je deze twee balken aan elkaar zou willen lijmen zodat deze werken als één balk zouden schuifspanningen nodig zijn die de vervormingen door buiging enigszins tegengaan:

```{figure} ./instructie_data/stacked.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Twee op elkaar liggende balken. Voor het samenvoegen zouden schuifspanningen nodig zijn zoals rechts getoond.
```

## Model

::::::{prf:assumption}

We negeren de afschuifvervorming, enkel de vervormingen door extensie / buiging nemen we mee in de daaruit volgende normaalspanningen. De schuifspanningen en afschuifvervorming zijn dus niet één-op-één gerelateerd in ons model, waar dat bij normaalspanningen wel het geval is.

```{figure} ./instructie_data/afschuiving.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect

Een klein stukje materiaal dat wordt belast door schuifspanningen en normaalspanningen kan vervormen door zowel afschuiving als extensie, maar in ons model nemen we enkel de extensie mee om de schuifspanningen te bepalen.
```

::::::

Voor het bepalen van schuifspanningen kijken we naar het evenwicht van een stukje van een balk, het zogenaamde afschuivende deel.

...

We kunnen de spanningen bepalen op de doorsnedes. De schuifspanningen zijn nog onbekend, maar voor de normaalspanningen geldt de eerder afgeleide formule $\sigma = \cfrac{M_z z}{I_{zz}}$.

...

::::::{prf:assumption}

Voor het bepalen van de schuifspanningen door buiging maken we dezelfde aannames als bij het berekenen van de normaalspanningen:
- De doorsnedes blijven vlak en loodrecht op 'vezels' staan, waarmee het rekverloop lineair is
- Normaalspanningen en -rekken hebben een lineair verband, waarmee de vorm van het spanningsverloop gelijk is aan die van het rekverloop.

Tijdens de afleiding van de formules voor normaalspanningen werden daarnaast nog een aantal aannames gedaan. Aangezien we door gaan bouwen op hetzelfde model, zullen deze aannames ook gelden voor schuifspanningen:
- Het assenstelsel grijpt aan in het normaalkrachtencentrum van de doorsnede. Hierdoor vervallen de statisch momenten $S_y$ en $S_z$ in de vergelijkingen.
- De doorsnede is symmetrisch in de $y$- en/of $z$-richting / krachten grijpen aan in de hoofdassen van de doorsnede. Hierdoor vervallen de termen met $I_{yz}$ en zijn spanniningen in de $y$- en $z$-richting onafhankelijk van elkaar.
- De doorsnede heeft een homogene verdeling van rekstijfheid $E$, waarmee de locatie van het normaalkrachtencentrum en traagheidsmomenten onafhankelijk van de rekstijfheid bepaald kunnen worden en de rekverdeling gelijk is van vorm aan de spanningsverdeling.

::::::

Nu stellen we een vrijlichaamsschema op met spanningen voor een deel van de doorsnede. Hierop werken dezelfde spanningen, met op het doorgesneden vlak geen normaalspanning maar wel een mogelijk schuifspanning.

...

Door het evenwicht in de langsrichting op te stellen, kunnen we de schuifspanning bepalen:

$$
\begin{align*}
\sum F_x &= 0 \\
-\int_{A_{\perp}} \sigma \left( M \right) \, dA_{\perp} + \int_{A_{\perp}} \sigma \left( M + \Delta M \right) \, dA_{\perp} + \int_{A_{\parallel}} \tau \, dA_{\parallel} &= 0 \\
-\int_{A_{\perp}} \sigma \left( M \right) \, dA_{\perp} + \int_{A_{\perp}} \sigma \left( M\right) \, dA_{\perp} + \int_{A_{\perp}} \sigma \left( \Delta M\right) \, dA_{\perp} + \int_{A_{\parallel}} \tau \, dA_{\parallel} &= 0 \\
\int_{A_{\perp}} \sigma \left( \Delta M\right) \, dA_{\perp} + \int_{A_{\parallel}} \tau \, dA_{\parallel} &= 0 \\
\left(\int_{h_{\perp}} \sigma \left( \Delta M \right) \, dh_{\perp} + \int_{\Delta x} \tau \, d \Delta x \right) \cdot b &= 0 \\
\int_{h_{\perp}} \sigma \left( \Delta M \right) \, dh_{\perp} + \int_{\Delta x} \tau \, d \Delta x &= 0 \\
\int_{h_{\perp}} \sigma \left( \Delta M \right) \, dh_{\perp} + \tau_{\rm{gem}} \cdot \Delta x &= 0 \\
\int_{h_{\perp}} \cfrac{\Delta M z}{I_{zz}} \, dh_{\perp} + \tau_{\rm{gem}} \cdot \Delta x &= 0 \\
\cfrac{\Delta M}{I_{zz}} \int_{h_{\perp}} z \, dh_{\perp} + \tau_{\rm{gem}} \cdot \Delta x &= 0 \\
\cfrac{\Delta M}{I_{zz}} S_{z}^{h_{\perp}} + \tau_{\rm{gem}} \cdot \Delta x &= 0 \\
\tau_{\rm{gem}} &= - \cfrac{\Delta M}{\Delta x} \cdot \cfrac{S_{z}^{h_{\perp}}}{I_{zz}} \\
\tau_{\rm{gem}} &= -V \cdot \cfrac{S_{z}^{h_{\perp}}}{I_{zz}}
\end{align*}
$$

::::::{prf:assumption}

Om het evenwicht op te stellen kunnen we alleen de resulterende schuifkracht bepalen, de verdeling is daarmee onbekend. We kunnen daarmee alleen maar de gemiddelde schuifspanning bepalen.

Daarnaast gaan we in deze berekeningen uit van dezelfde $I_{zz}$ in de linker en rechter doorsnede, wat betekent dat we aannemen dat de doorsnede niet verandert over de lengte van de balk; dus een prismatische balk.

::::::

::::::{admonition} Volledige afleiding
class: notation, dropdown


::::::