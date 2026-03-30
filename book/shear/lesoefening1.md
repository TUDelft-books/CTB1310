# Begeleide oefening 1

Gegeven is de volgende constructie en doorsnede:

```{figure} ./lesoefening1_data/voorbeeld.svg
:align: center
:class: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_2
:number:
```

:::::{exercise}
:nonumber: true

Gegeven zijn een aantal mogelijke punten waarop de schuifspanning kan worden bepaald:

```{figure} ./lesoefening1_data/punten.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_2
:number:
```

```{h5p} https://tudelft.h5p.com/content/1292775862047125807/embed
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

Bepaal de doorsnedegrootheden

```{h5p} https://tudelft.h5p.com/content/1292775929941797377/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Om de oppervlakte van de doorsnede te bepalen knippen we doorsnede in verschillende stukjes op:

```{figure} ./lesoefening1_data/Schuifspanning dikwandig oefening 1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_2
:number:
```

De oppervlakte A is dan:

$$
\begin{align*} 
A &= A_{1} + A_{2} + 2 \cdot A{3} \\
&= 300 \cdot 100 + 150 \cdot 300 + 2 \cdot \cfrac{1}{2} \cdot 75 \cdot 50 \\
&= 78750 \, \rm{mm^2}
\end{align*}
$$

De z-coördinaat van het normaalkrachtencentrum (NC) is:

$$
\begin{align*}
z_{NC} &= \cfrac{A_{1} \cdot z_{1} + A_{2} \cdot z_{2} + 2 \cdot A_{3} \cdot z_{3} }{A} \\
&= \cfrac{300 \cdot 100 \cdot 50 + 150 \cdot 300 \cdot 250 + 2 \cdot \cfrac{1}{2} \cdot 75 \cdot 50 \cdot \left( 100 + \cfrac{1}{3} \cdot 50 \right)}{78750} \\
&= 167 \, \rm{mm}
\end{align*}
$$

Het traagheidsmoment van de doorsnede is:

$$
\begin{align*}
I_{zz} &= \cfrac{1}{12} b_{1} h_{1}^3 + A_{1} \cdot d_{1}^2 + \cfrac{1}{12} b_{2} h_{2}^3 + A_{2} \cdot d_{2}^2 + 2 \cdot \left(\cfrac{1}{36} b_{3} h_{3}^3 + A_{3} \cdot d_{3}^2 \right) \\
&= \cfrac{1}{12} \cdot 300 \cdot 100^3 + 300 \cdot 100 \cdot \left(167-50\right)^2 + \cfrac{1}{12} \cdot 150 \cdot 300^3 + 150 \cdot 300 \cdot \left(250-167\right)^2 + 2 \cdot \left( \cfrac{1}{36} \cdot 75 \cdot 50^3 + \cfrac{1}{2} \cdot 75 \cdot 50 \cdot \left(167 - \left(100 + \cfrac{1}{3} \cdot 50 \right)\right)^2 \right)\\
&= 10.93 \, \rm{dm^4}
\end{align*}
$$


::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de gemiddelde schuifspanning op het horizontale afschuifvlak op $\bar{z} = 250 \, \rm{mm}$ voor een negatieve snede in $\rm{C}$.

```{h5p} https://tudelft.h5p.com/content/1292775934968650997/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

...

::::

% solution_end
