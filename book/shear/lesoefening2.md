# Begeleide oefening 2

Gegeven is de volgende doorsnede:

```{figure} ./lesoefening2_data/voorbeeld.svg
:align: center
:class: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_3
:number:
```

Verder is gegeven dat voor een segment van een ring geldt:

```{figure-start} ./lesoefening2_data/Centroid_of_an_annular_sector.svg.png
:name: cirkelsegment
:align: center
:source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Centroid_of_an_annular_sector.svg)
:author: DuckRabbitDuckRabbit
:license: CC-BY-SA
:copyright: © DuckRabbitDuckRabbit 2020
:date: 2020-12-13
:placement: caption
:width: 30%

Zwaartepunt $\bar{x}$ van een ringsegment met binnenste straal $r_1$, buitenste straal $r_2$ en totale hoek $2\alpha$.
```

$$
\begin{align*}
A &= \alpha \left( r_2^2 - r_1^2 \right) \\
\bar{x} &= \cfrac{2 \sin \left( \alpha \right)}{ 3 \alpha} \cfrac{r_2^3 - r_1^3}{r_2^2 - r_1^2}
\end{align*}
$$

```{figure-end}
```

:::::{exercise}
:nonumber: true

Gegeven zijn een aantal mogelijke punten waarop de schuifspanning kan worden bepaald:

```{figure} ./lesoefening2_data/punten.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_3
:number:
```

Je mag er vanuit gaan dat $R \gg b$ voor alle relevante afschuifvlakken.

```{h5p} https://tudelft.h5p.com/content/1292778320901018827/embed
```

:::::

:::::{exercise}
:nonumber: true

Gegeven zijn vier mogelijke schuifspanningsverdelingen.

```{figure} ./lesoefening2_data/verloop.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_3
:number:
```

```{h5p} https://tudelft.h5p.com/content/1292778326294019037/embed
```

:::::

:::::{exercise}
:nonumber: true

Bepaal de doorsnedegrootheden

```{h5p} https://tudelft.h5p.com/content/1292778334042905987/embed
```

:::::

::::{admonition} Uitwerking
:class: solution, dropdown

Voor de oppervlakte van de dikwandige ring geldt de volgende formule:

$$
\begin{align*}
A &= \alpha \left( r_2^2 - r_1^2 \right) \\
&= \pi \cdot \left(300^2 - 150^2\right) \\
&= 67500 \pi \, \rm{mm^2}
\end{align*}
$$

Voor het berekenen van het traagheidsmoment van de dikwandige ring geldt het volgende:

$$
\begin{align*}
I &= \cfrac{\pi}{4} \left(r_2^4 - r_1^4 \right) \\
&= \cfrac{\pi}{4} \left(300^4 - 150^4 \right) \\
&= 60 \, \rm{dm^4}
\end{align*}
$$

::::

:::::{exercise}
:nonumber: true

Stel je wilt de formule getoond in {numref}`cirkelsegment` zelf afleiden in het $y,z$-assenstelsel van de doorsnede.

::::{hint}

Voorbeeld van een hoek van $-\cfrac{\pi}{4}$.

```{figure} ./lesoefening2_data/voorbeeld_hoek.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_3
:number:
```

::::

```{h5p} https://tudelft.h5p.com/content/1292808037756808497/embed
```

:::::

::::{admonition} Uitwerking
:class: solution, dropdown

...

::::

:::::{exercise}
:nonumber: true

Bepaal de maximale schuifspanning

```{h5p} https://tudelft.h5p.com/content/1292778356403071697/embed
```

:::::

::::{admonition} Uitwerking
:class: solution, dropdown

De maximale schuifspanning bevindt zich ter hoogte van het normaalkrachtcentrum in $\rm{z} = 0$.

Het statisch moment ter hoogte van het normaalkrachtcentrum is:

$$
\begin{align*}
S_{z}^{\rm{a}} &= A_{\rm{afschuivend} \, \rm{deel}} \, z_{\rm{N.C.} \longleftrightarrow \rm{zwaartepunt} \, \rm{afschuivend} \, \rm{deel} } \\
&= \frac{1}{2} \cdot A \cdot \cfrac{2 \cdot \sin \left( \alpha \right)}{ 3 \cdot \alpha} \cfrac{r_2^3 - r_1^3}{r_2^2 - r_1^2} \\
&= \frac{1}{2} \cdot \pi \cdot \left( r_2^2 - r_1^2 \right) \cdot \cfrac{2 \cdot \sin \left( \frac{1}{2} \cdot \pi \right)}{ \cfrac{3}{2} \pi} \cfrac{r_2^3 - r_1^3}{r_2^2 - r_1^2} \\
&= \frac{3}{2} \cdot \left(r_2^3 - r_1^3 \right) \\
&= \frac{3}{2} \cdot \left(300^3 - 150^3 \right) \\
&= 15.75 \, \rm{dm^3}
\end{align*}
$$

De dwarskracht is gegeven, deze is $2025 \pi \, \rm{kN}$.

Uiteindelijk kunnen we dan de maximale schuifspanning bepalen:

$$
\begin{align*}
\tau_{\rm{max}} &= \cfrac{V_{z} \cdot S_{z}^{\rm{a}}}{b \cdot I_{zz}} \\
&= \cfrac{2025 \pi \cdot 10^3 \, \cdot 15.75 \cdot 10^6}{\left(2 \cdot 150\right) \cdot 60 \cdot 10^8} \\
&= 56 \, \rm{MPa}
\end{align*}
$$

Omdat de dwarskracht naar beneden wijst is de schuifspanning omhoog en is deze dus negatief.

::::

:::::{exercise}
:nonumber: true

Waar is de schuifspanning de helft van de maximale waarde uitgedrukt als hoek van het afschuifvlak $\varphi$ tov het assenstelsel tussen $-\cfrac{\pi}{2}$ en $0$ ten opzichte van de $y$-as?

```{h5p} https://tudelft.h5p.com/content/1292778358149562237/embed
```

:::::

::::{admonition} Uitwerking
:class: solution, dropdown

We willen de hoek $\alpha$ vinden uit de formule van het statisch moment waarbij de schuifspanning precies gehalveerd is ten opzichte van de maximale schuifspanning. 

$$
\begin{align*}
\frac{1}{2} \tau_{\rm{max}} &= \cfrac{V_{z} \cdot S_{z}^{\rm{a}}}{b \cdot I_{zz}} \\
\frac{1}{2} \tau_{\rm{max}} &= \frac{V_{z}}{b \cdot I_{zz}} \cdot \alpha \cdot \left( r_2^2 - r_1^2 \right) \cdot \cfrac{2 \cdot \sin \left( \alpha \right)}{ 3 \cdot \alpha} \cfrac{r_2^3 - r_1^3}{r_2^2 - r_1^2} \\
\\
\frac{56}{2} &= \cfrac{2025 \cdot  \pi \cdot 10^3}{\left(2 \cdot 150\right) \cdot 60 \cdot 10^8}  \cdot \cfrac{2 \cdot \sin \left( \alpha \right)}{3} \left(300^3 - 150^3 \right) \\
\\
\sin \left( \alpha \right) &= 0.503 \\
\alpha &= \frac{1}{6} \pi
\end{align*}
$$

Omdat er wordt gevraagd naar de hoek $\varphi$ tussen $-\cfrac{\pi}{2}$ en $0$ ten opzichte van de $y$-as moeten we de hoek alpha nog even omschrijven.

```{figure} ./lesoefening2_data/phi_bepaling.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_3
:number:
```

De hoek $\varphi$ is dus:

$$
\begin{align*}
\varphi &= - \left(\frac{1}{2} \cdot \pi - \alpha \right)
&= -\frac{1}{3} \cdot \pi
&= -1.05 \, \rm{rad}
\end{align*}
$$

::::