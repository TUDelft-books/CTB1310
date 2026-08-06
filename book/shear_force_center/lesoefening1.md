````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is gebaseerd op [deze oefening uit het online boek van het vak CTS1000 Structural Mechanics op de Technische Universiteit Delft](https://oit.tudelft.nl/CT1000/2025/week_12/session_1/intro.html) {cite:p}`CT1000_2025`.

```
````

# Begeleide oefening

Gegeven is de volgende doorsnede:

```{figure} ./lesoefening_data/doorsnede.svg
:align: center
:class: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center
:number:
```

Gevraagd is de ligging van het dwarskrachtencentrum.

:::::{exercise}
:nonumber: true

Bepaal de doorsnedegrootheden.

```{h5p} https://tudelft.h5p.com/content/1292802725655071477/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

$$
\begin{align*}
A &= 2 \cdot 200 \cdot 15 + 400 \cdot 30 \\
&= 18000 \, \rm{mm^2} 
\end{align*}
$$


Om de locatie van het normaalkrachtencentrum te berekenen delen we de doorsnede op in drie delen:

```{figure} ./lesoefening_data/Berekening_zNC.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center
:number:
```

$$
\begin{align*}
z_{\rm{NC}} &= \cfrac{A_{1} \cdot z_{1} + A_{2} \cdot z_{2} + A_{3} \cdot z_{3} }{A} \\
&= \cfrac{200 \cdot 15 \cdot 0 + 30 \cdot 400 \cdot 200 + 200 \cdot 15 \cdot 400}{18000} \\
&= 200 \, \rm{mm}
\end{align*}
$$

$$
\begin{align*}
y_{\rm{NC}} &= \cfrac{A_{1} \cdot y_{1} + A_{2} \cdot y_{2} + A_{3} \cdot y_{3} }{A} \\
&= \cfrac{200 \cdot 15 \cdot 100 + 30 \cdot 400 \cdot 0 + 200 \cdot 15 \cdot 100}{18000} \\
&= 33 \, \rm{mm}
\end{align*}
$$

$$
\begin{align*}
I_{yy} &= \cfrac{1}{12} \cdot b_{1} \cdot h_{1}^3 + A_{1} \cdot d_{1}^2 + \cfrac{1}{12} \cdot b_{2} \cdot h_{2}^3 + A_{2} \cdot d_{2}^2 + \cfrac{1}{12} \cdot b_{3} \cdot h_{3}^3 + A_{3} \cdot d_{3}^2 \\
&= 2 \cdot \left( \cfrac{1}{12} \cdot 15 \cdot 200^3 + 200 \cdot 15 \cdot \left(100-33\right)^2 \right) + \cfrac{1}{12} \cdot 400 \cdot 30^3 + 30 \cdot 400 \cdot 33^2 \\
&= 61 \cdot 10^6 \, \rm{mm^4}
\end{align*}
$$

$$
\begin{align*}
I_{zz} &= \cfrac{1}{12} \cdot b_{1} \cdot h_{1}^3 + A_{1} \cdot d_{1}^2 + \cfrac{1}{12} \cdot b_{2} \cdot h_{2}^3 + A_{2} \cdot d_{2}^2 + \cfrac{1}{12} \cdot b_{3} \cdot h_{3}^3 + A_{3} \cdot d_{3}^2 \\
&= 2 \cdot \left( \cfrac{1}{12} \cdot 200 \cdot 15^3 + 200 \cdot 15 \cdot 200^2 \right) + \cfrac{1}{12} \cdot 30 \cdot 400^3 + 30 \cdot 400 \cdot 0^2 \\
&= 400 \cdot 10^6 \, \rm{mm^4}
\end{align*}
$$
::::

% solution_end

:::::{exercise}
:nonumber: true

Gegeven zijn 6 mogelijke werklijnen/assen waarop het dwarskrachtencentrum kan liggen.

::::{grid} 3 3 3 3
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ./lesoefening_data/optie_1.svg
:align: center
:scale: 75
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center
:number:
```
Optie 1
```{figure-end}
```
:::

:::{grid-item}
:columns: auto

```{figure-start} ./lesoefening_data/optie_2.svg
:align: center
:scale: 75
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center
:number:
```
Optie 2
```{figure-end}
```
:::

:::{grid-item}
:columns: auto

```{figure-start} ./lesoefening_data/optie_3.svg
:align: center
:scale: 75
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center
:number:
```
Optie 3
```{figure-end}
```
:::

:::{grid-item}
:columns: auto

```{figure-start} ./lesoefening_data/optie_4.svg
:align: center
:scale: 75
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center
:number:
```
Optie 4
```{figure-end}
```
:::

:::{grid-item}
:columns: auto

```{figure-start} ./lesoefening_data/optie_5.svg
:align: center
:scale: 75
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center
:number:
```
Optie 5
```{figure-end}
```
:::

:::{grid-item}
:columns: auto

```{figure-start} ./lesoefening_data/optie_6.svg
:align: center
:scale: 75
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center
:number:
```
Optie 6
```{figure-end}
```
:::


::::

```{h5p} https://tudelft.h5p.com/content/1292802734390960127/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

...

::::

% solution_end

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292802735884992227/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

...

::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de absolute waarde van de schuifspanningen op de aangegeven snedevlakken bij een dwarskracht van $100 \, \rm{kN}$.

```{figure} ./lesoefening_data/ABCDE.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center
:number:
```

```{h5p} https://tudelft.h5p.com/content/1292802740309219657/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Om de schuifspanning te berekenen op de aangegeven snedevlakken hebben we de volgende formule nodig:

$$
\begin{align*}
\tau_{\rm{max}} &= \cfrac{V_{z} \, S_{z}^{\rm{a}}}{b \, I_{zz}} \\
\end{align*}
$$

We nemen in dit geval het traagheidsmoment en het statisch moment in de $\rm{z}$-richting.

Voor elke snede zullen we moeten kijken wat het statisch moment $S_{z}^{\rm{a}}$ en de breedte ${b}$ in de snede is.

De standaardformule voor het berekenen van het statisch moment is:

$$
\begin{align*}
S_{z}^{\rm{a}} &= A_{\rm{afschuivend} \, \rm{deel}} \cdot z_{\rm{N.C.} \longleftrightarrow \rm{zwaartepunt} \, \rm{afschuivend} \, \rm{deel} } \\
\end{align*}
$$

De dwarskracht ${V}$ en het traagheidsmoment $I_{zz}$ zijn voor elke snede gelijk, deze zijn respectievelijk $100 \, {\rm{kN}}$ en $400 \cdot 10^6 \, \rm{mm^4}$.

Voor snede $\rm{A}$ geldt:

$$
\begin{align*}
S_{z}^{\rm{a}} &= 0 \cdot 200 \\
&= 0 \, \rm{mm^3}\\
\\
b &= 15 \rm {mm}\\
\\
\tau_{A} &= \cfrac{100 \cdot 10^3 \cdot 0 }{15 \cdot 400 \cdot 10^6} \\
&= 0 \, \rm{MPa}
\end{align*}
$$

Voor snede $\rm{B}$ geldt:

$$
\begin{align*}
S_{z}^{\rm{a}} &= 200 \cdot 15 \cdot 200 \\
&= 600000 \, \rm{mm^3}\\
\\
b &= 15 \rm {mm}\\
\\
\tau_{B} &= \cfrac{100 \cdot 10^3 \cdot 600000 }{15 \cdot 400 \cdot 10^6} \\
&= 10 \, \rm{MPa}
\end{align*}
$$

Voor snede $\rm{C}$ geldt:

$$
\begin{align*}
S_{z}^{\rm{a}} &= 200 \cdot 15 \cdot 200 + 200 \cdot 30 \cdot 100 \\
&= 1200000 \, \rm{mm^3}\\
\\
b &= 30 \rm {mm}\\
\\
\tau_{C} &= \cfrac{100 \cdot 10^3 \cdot 1200000 }{30 \cdot 400 \cdot 10^6} \\
&= 10 \, \rm{MPa}
\end{align*}
$$

Voor snede $\rm{D}$ geldt:

$$
\begin{align*}
S_{z}^{\rm{a}} &= 200 \cdot 15 \cdot 200 \\
&= 600000 \, \rm{mm^3}\\
\\
b &= 30 \rm {mm}\\
\\
\tau_{D} &= \cfrac{100 \cdot 10^3 \cdot 600000 }{30 \cdot 400 \cdot 10^6} \\
&= 5 \, \rm{MPa}
\end{align*}
$$

Voor snede $\rm{E}$ geldt:

$$
\begin{align*}
S_{z}^{\rm{a}} &= 166.67 \cdot 15 \cdot 200 \\
&= 500000 \, \rm{mm^3}\\
\\
b &= 15 \rm {mm}\\
\\
\tau_{E} &= \cfrac{100 \cdot 10^3 \cdot 500000 }{15 \cdot 400 \cdot 10^6} \\
&= 8 \, \rm{MPa}
\end{align*}
$$

```{figure} ./lesoefening_data/Schuifspanningsverdeling.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center
:number:
```

::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de absolute waarde van de resultante krachten van de schuifspanningen in de flenzen en het lijf.

```{h5p} https://tudelft.h5p.com/content/1292802743028408557/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Omd de absolute waarde van de resultante krachten van de schuifspanningen te berekenen moeten we de oppervlaktes onder de grafiek van de schuifspanning berekenen. 

```{figure} ./lesoefening_data/Schuifspanningsverdeling.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center
:number:
```

Voor de flenzen is de vorm van de grafiek een driehoek. Dit betekent dat we de resultante op de volgende manier berekenen:

$$
\begin{align*}
F_{flens} &= \cfrac{1}{2} \cdot 200 \cdot 10 \cdot 15 \\
&= 15 \, \rm{kN}\\
\end{align*}
$$

Voor het lijf is de vorm van de grafiek een parabool. Dit betekent dat we de resultante op de volgende manier berekenen:

$$
\begin{align*}
F_{lijf} &= 5 \cdot 400 \cdot 30 + \cfrac{2}{3} \cdot \left(10-5\right) \cdot 400 \cdot 30 \\
&= 100 \, \rm{kN}\\
\end{align*}
$$

```{figure} ./lesoefening_data/Resultantes_schuifspanningsverloop.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center
:number:
```

::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de locatie van het dwarskrachtencentrum.

```{h5p} https://tudelft.h5p.com/content/1292802744785292597/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De ${z}$-locatie van het dwarskrachtencentrum ligt in de symmetrie-as van de doorsnede. 

$$
\begin{align*}
z_{DC} &= 200 \, \rm{mm}\\
\end{align*}
$$

De ${y}$-locatie van het dwarskrachtencentrum moet worden berekend aan de hand van een evenwicht, waarbij de resultantes van de schuifspanning evenwicht moeten vormen met de dwarskracht die aangrijpt in het dwarskrachtencentrum.

```{figure} ./lesoefening_data/evenwicht_berekening_y_dc.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center
:number:
```

We nemen een moment linksom aan als positief. De momentensom om punt $\rm{X}$ wordt dan als volgt:

$$
\begin{align*}
\sum T_{\rm{X}} &= 0 \\
-15 \cdot 200 - 15 \cdot 200 + 100 \cdot 0 - 100 \cdot \rm{y_{DC}} &= 0 \\
\rm{y_{DC}} = -60 \, \rm{mm}
\end{align*} 
$$

::::

% solution_end
