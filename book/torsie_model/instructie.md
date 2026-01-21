# Instructie

In de vorige les hebben we bekeken hoe we het wringend moment in een doorsnede kunnen bepalen. In deze les gaan we bekijken hoe we de spanningen kunnen berekenen ten gevolge van het wringend moment.

Het spanningsverloop ten gevolge van een wringend moment is over het algemeen erg complex en afhankelijk van het soort doorsnede. We zullen een aantal doorsnedes met bijbehorende modellen behandelen: ronde massieve doorsnedes en ringen (zowel dikwandig als dunwandig), dunwandige niet-ronde gesloten doorsnedes, en open dunwandige doorsnedes.

## Ronde massieve doorsnedes en ringen

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

&nbsp;
```

:::
:::{grid-item}
:columns: auto

```{figure} ./instructie_data/assump_bending_2.svg
:align: center
:scale: 100
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models

&nbsp;
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

&nbsp;
```


:::
:::{grid-item}
:columns: auto

```{figure} ./instructie_data/assump_torsion_2.svg
:align: center
:scale: 100
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_models

&nbsp;
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

&nbsp;
```


Als we een lineair spanningsverloop als functie van de straal $r$ aannemen, kunnen we dat schrijven als $\tau = k \cdot r$, waarbij $k$ een constante is die we nog moeten bepalen.

De bijdrage van een klein oppervlakte $dA$ aan het wringend moment ten opzichte van het dwarskrachtencentrum is dan: $dM_t = k \cdot r \cdot r \, dA$

Als we dit integreren over de hele doorsnede, vinden we het totale wringend moment. De term $\int_A{r^2 \, dA}$ noemen we het polair traagheidsmoment $I_{\rm{p}}$ en is puur afhankelijk van de vorm van de doorsnede.

$$
\begin{align*}
M_t &= k \int_A r^2 dA \\
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

&nbsp;
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

&nbsp;
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

&nbsp;
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
I_{\rm{p}} &= \int_A r^2 dA \\
&=  \int_0^{R}{\int_0^{2 \pi}{ r^3 \, d\theta \, dr}} \\
&= \int_0^{R}{ 2 \pi \cdot r^3 \, dr} \\
&= \cfrac{\pi}{2} R^4 \\
\end{align*}
$$

Op vergelijkbare wijze kan het polaire traagheidsmoment voor andere dikwandige en dunwandige doorsnedevormen worden afgeleid.

::::::