````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is gebaseerd op [deze oefening uit het online boek van het vak CTS1000 Structural Mechanics op de Technische Universiteit Delft](https://oit.tudelft.nl/CT1000/2025/week_14/session_3/intro.html) {cite:p}`CT1000_2025`.

```
````

# Begeleide oefening 1


Gegeven is de volgende constructie en doorsnede in $\rm{D}$. Het is een versimpeld model van de [Prinses Amaliabrug, een fietsbrug in Dordrecht](https://www.ad.nl/dordrecht/zes-tips-om-het-hoofd-koel-te-houden~a2c4481b5/).

::::{grid} 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ../torsie_model/lesoefening2_data/constructie.svg
:align: center
:class: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/failure_criteria
:number:
```

- De verdeelde belasting grijpt aan in het midden van de doorsnede.
- De $14.32\,\rm{kN}$ grijpt aan in $y=-2 \,\rm{m}$.
- De oplegreactie bij $A$ grijpt aan in $y=-2 \,\rm{m}$.
- De oplegreactie bij $B$ grijpt aan in zowel $y=-2 \,\rm{m}$ als $y=+2 \,\rm{m}$.

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure} lesoefening_data/doorsnede_2.svg
:align: center
:class: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/failure_criteria
:number:
```
:::

::::

Dit is dezelfde constructie en doorsnede als in [de vorige les](../torsie_model/lesoefening2.md). Ditmaal zijn echter niet alleen schuifspanningen gevraagd ten gevolge van de verwringing, maar nu de totale schuifspanning en normaalspanning in punt $\rm{E}$ in de doorsnede net rechts van $\rm{D}$.

Kijk terug naar je uitwerking van [de vorige les](../torsie_model/lesoefening2.md), een deel van de waardes zijn relevant voor de vragen van vandaag

:::::{exercise}
:nonumber: true

Gegeven is dat het oppervlakte en statisch moment ten opzichte van de $\bar y$-as van de boven- en zijkanten van de doorsnede gelijk is aan $4 \cdot 0.01 + 2 \cdot 0.25 \cdot 0.01 = 0.045 \, \rm{m}^2 $ en $4 \cdot 0.01 \cdot 1.75 + 2 \cdot 0.25 \cdot 0.01 \cdot \left(1.75 + \cfrac{0.25}{2}\right) = 0.079375 \rm{m^3}$, respectievelijk.

Om het zwaartepunt van de gehele doorsnede te bepalen is ook het zwaartepunt van het gekromde gedeelte nodig ten opzichte van de $\bar y$-as. Maak daarvoor gebruik van $S_{\bar z} = \int\limits_A z \, dA$ en $A = \int\limits_A dA$. De volgende vragen zijn er om je op weg te helpen.

::::{question}
:type: multiple-choice
:variant: single-select
:showanswer:
:nocaption:

Welke van de volgende formules is/zijn correct voor het bepalen van $A$ van het gekromde gedeelte?
---
[x] $ A = \int\limits_A dA = \int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} r t d\varphi $
[ ] $ A = \int\limits_A dA = \int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} \int\limits_{r - \frac{1}{2}t}^{r+\frac{1}{2}} r dr d\varphi $
> Hoewel dit antwoord correct is, is het een dikwandige berekening. Je mag hier een dunwandige berekening maken, die simpeler is.
---

::::

::::{question}
:type: multiple-choice
:variant: single-select
:columns: 1 1 1 1
:showanswer:
:nocaption:

Welke van de volgende formules is/zijn correct voor het bepalen van $S_{\bar z}$ van het gekromde gedeelte?
---
[ ] $ S_{\bar z} = \int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} z r t d\varphi  = \int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} \sin \left( \varphi \right) d\varphi $
> $ z = r \sin\left(\varphi\right) $. Dit geeft in de integraal $ r^2 t \sin\left(\varphi\right) = \left( 2 \sqrt{2} \right)^2 \cdot 0.01 \cdot \sin\left(\varphi\right) $
[ ] $ S_{\bar z} = \int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} z r t d\varphi  = \int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} 0.02 \sqrt{2} \sin \left( \varphi \right) d\varphi $
> $ z = r \sin\left(\varphi\right) $. Dit geeft in de integraal $ r^2 t \sin\left(\varphi\right) = \left( 2 \sqrt{2} \right)^2 \cdot 0.01 \cdot \sin\left(\varphi\right) $
[x] $ S_{\bar z} = \int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} z r t d\varphi  = \int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} 0.08 \sin \left( \varphi \right) d\varphi $
---

::::

::::{question}
:type: multiple-choice
:variant: single-select
:columns: 1 1 1 1
:showanswer:
:nocaption:

Welke van de volgende formules is/zijn correct voor het bepalen van $S_{\bar z}$ van het gekromde gedeelte?
---
[ ] $ S_{\bar z} = \int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} 0.08 \sin \left( \varphi \right) d\varphi = 0.04 $
>
$$\begin{align*}
\int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} \sin \left( \varphi \right) d\varphi &= -\cos \left( \cfrac{3 \pi}{4} \right) - \left( -\cos \left( \cfrac{ \pi}{4} \right) \right) \\
 &= - \left( - \frac{1}{2} \sqrt{2} \right) - \left( - \frac{1}{2} \sqrt{2} \right) \\
 &= \sqrt{2}
\end{align*}$$
[ ] $ S_{\bar z} = \int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} 0.08 \sin \left( \varphi \right) d\varphi = 0.04 \sqrt{2} $
>
$$\begin{align*}
\int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} \sin \left( \varphi \right) d\varphi &= -\cos \left( \cfrac{3 \pi}{4} \right) - \left( -\cos \left( \cfrac{ \pi}{4} \right) \right) \\
 &= - \left( - \frac{1}{2} \sqrt{2} \right) - \left( - \frac{1}{2} \sqrt{2} \right) \\
 &= \sqrt{2}
\end{align*}$$
[ ] $ S_{\bar z} = \int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} 0.08 \sin \left( \varphi \right) d\varphi = 0.08 $
>
$$\begin{align*}
\int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} \sin \left( \varphi \right) d\varphi &= -\cos \left( \cfrac{3 \pi}{4} \right) - \left( -\cos \left( \cfrac{ \pi}{4} \right) \right) \\
 &= - \left( - \frac{1}{2} \sqrt{2} \right) - \left( - \frac{1}{2} \sqrt{2} \right) \\
 &= \sqrt{2}
\end{align*}$$
[x] $ S_{\bar z} = \int\limits_{\cfrac{\pi}{4}}^{\cfrac{3 \pi}{4}} 0.08 \sin \left( \varphi \right) d\varphi = 0.08 \sqrt{2} $
---

::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:showanswer:
:nocaption:

Wat is de locatie van het zwaartepunt van het gekromde gedeelte en van het geheel?
---
MRP[8 / \pi;0.025]
MRP[2.1464;0.025]
^^^
?
$ \bar z_{\rm{N.C.}} \, \rm{gekromde} \, \rm{gedeelte} = $ {gap} $ \, \rm{m} $

$ \bar z_{\rm{N.C.}} \, \rm{gehele} \, \rm{doorsnede} \approx $ {gap} $ \, \rm{m} $

---

::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:showanswer:
:admonition:
:class: exercise
:nocaption:

Wat is de locatie van het zwaartepunt van het gekromde gedeelte en van het geheel?
---
MRP[8/ \pi;0.025]
MRP[2.1464;0.025]
^^^
?
$ \bar z_{\rm{N.C.}} \, \rm{gekromde} \, \rm{gedeelte} = $ {gap} $ \, \rm{m} $

$ \bar z_{\rm{N.C.}} \, \rm{gehele} \, \rm{doorsnede} \approx $ {gap} $ \, \rm{m} $

---

::::

:::::

:::::{exercise}
:nonumber: true

Op eenzelfde manier is $I_{zz}$ te berekenen voor het gekromde gedeelte. Ten opzichte van het zwaartepunt van de gehele doorsnede zoals bepaald in de vorige opgave geeft dat: $I_{zz}^{\rm{gekromde} \, \rm{gedeelte}} = 98.63\,\mathrm{dm}^4$. Bepaal $I_{zz}$ van de gehele doorsnede.


```{h5p} https://tudelft.h5p.com/content/1292808647660137747/embed
```

:::::

:::::{exercise}
:nonumber: true

Bepaal de normaalspanning in punt $\rm{E}$ net rechts van $\rm{D}$.

```{h5p} https://tudelft.h5p.com/content/1292808652061755197/embed
```

:::::

:::::{exercise}
:nonumber: true

Bepaal de schuifspanning op een positieve doorsnede in punt $\rm{E}$ net rechts van $\rm{D}$ ten gevolge van de dwarskracht.

```{h5p} https://tudelft.h5p.com/content/1292808655867105037/embed
```

:::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:showanswer:
:admonition:
:class: exercise
:nocaption:

Bepaal de totale schuifspanning op een positieve doorsnede in punt $\rm{E}$ net rechts van $\rm{D}$ ten gevolge van de kromming en verwringing.
---
MAP[17;0.5]
DS[{omhoog};omlaag]
^^^
? De totale spanning is {gap} $\rm{MPa}$ {gap}.
---

::::
