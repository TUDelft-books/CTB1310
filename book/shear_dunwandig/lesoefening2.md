````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is gebaseerd op [deze oefening uit het online boek van het vak CTS1000 Structural Mechanics op de Technische Universiteit Delft](https://oit.tudelft.nl/CT1000/2025/week_12/session_1/intro.html) {cite:p}`CT1000_2025`.

```
````

# Begeleide oefening 2

Gegeven is de volgende constructie en doorsnede:

```{figure} ./lesoefening2_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_stresses
:number:
```

Gevraagd is de schuifspanningsverdeling op een positieve snede in de ligger.

:::::{exercise}
:nonumber: true

Gegeven zijn zes mogelijke schuifspanningsverdelingen.

```{figure} ./lesoefening2_data/varianten.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_stresses
:number:
```

```{h5p} https://tudelft.h5p.com/content/1292779162260344597/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

Variant 6 is correct. De dwarskracht werkt in z-richting, dus linear schuifsspanning verloop in y-richting en parabolisch in z-richting. $S_{z}^{\rm{a}}$ is nul voor een snede bij $y=0$ onderin en boven het profiel. De schuifspanning is maximaal ter hoogte van $N.C.$


...

::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de doorsnedegrootheden

```{h5p} https://tudelft.h5p.com/content/1292779169041444447/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

Voor de $I_{zz}$ berekening zijn de schuine delen berekend als trapezium. De lengte in y-richting voor de berekening van het eigen traagheidsmoment is dan $7 \cdot \sqrt{10}/3$, zoals wordt uitgelegd met de onderstaande afbeelding:

```{figure} ./lesoefening2_data/Dikte_uitleg.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_stresses
:number:
```
De doorsnedegrootheden zijn als volgt berekend:

$$
\begin{align*}
A &= 100 \cdot 7 + 300 \cdot 7 + 2 \cdot \left(100 \cdot \sqrt{10} \cdot 7 \right) \\
&\approx 7227 \ \text{mm}^2 \\[6pt]

\bar{z}_{\rm{N.C.}} &= \frac{100 \cdot 7 \cdot 300 + 2 \cdot \left(100 \cdot \sqrt{10} \cdot 7 \cdot 150 \right)}{7227} \\
&\approx 121 \ \text{mm}\\

I_{zz} &= \frac{300 \cdot 7^3}{12} + 300 \cdot 7 \cdot 121^2 \\
&\quad + 2 \cdot \left( \frac{7 \cdot \sqrt{10}/3 \cdot 300^3}{12} + 7 \cdot \sqrt{300^2 + 100^2} \cdot (150 - 121)^2 \right) \\
&\quad + \frac{100 \cdot 7^3}{12} + 100 \cdot 7 \cdot (300 - 121)^2 \\
&\approx 901 \cdot 10^5 \ \text{mm}^4
\end{align*}
$$
...

::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de maximale schuifspanning in de bovenflens, onderflens en het lijf.

```{h5p} https://tudelft.h5p.com/content/1292779172064134117/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

Voor de bovenflens geldt:
$$
\begin{align*}
\left| S_{z,\rm{bovenflens}}^{\rm{a}} \right| &= 7 \cdot 300 \cdot 121^2 \\
&= 254100 \ \text{mm}^3 \\
&\approx 251 \ \text{cm}^3 \\[6pt]

\left| \tau_{\rm{bovenflens}} \right| &= \frac{200000 \cdot 254100}{(7 \cdot 2)\cdot 901 \cdot 10^5} \\
&\approx 40 \ \text{MPa}
\end{align*}
$$

Voor de onderflens geldt:
$$
\begin{align*}
\left| S_{z,\rm{onderflens}}^{\rm{a}} \right| &= 7 \cdot 300 \cdot 121^2 \\
&= 125300 \ \text{mm}^3 \\
&\approx 125 \ \text{cm}^3 \\[6pt]

\left| \tau_{\rm{bovenflens}} \right| &= \frac{200000 \cdot 125300}{(7 \cdot 2)\cdot 901 \cdot 10^5} \\
&\approx 20 \ \text{MPa}
\end{align*}
$$

Voor het lijf geldt:
$$
\begin{align*}
\left| S_{z,\rm{lijf}}^{\rm{a}} \right| &= \left| S_{z,\rm{bovenflens}}^{\rm{a}} \right| + 2 \cdot (7 \cdot \sqrt{10}/3 \cdot 121 \cdot 121/2) \\
&\approx 362131 \ \text{mm}^3 \\
&\approx 362 \ \text{cm}^3 \\[6pt]

\left| \tau_{\rm{lijf}} \right| &= \frac{200000 \cdot 362131}{(7 \cdot 2)\cdot 901 \cdot 10^5} \\
&\approx 57 \ \text{MPa}
\end{align*}
$$

...

::::

% solution_end
