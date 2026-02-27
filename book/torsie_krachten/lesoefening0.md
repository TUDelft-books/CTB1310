````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina is gebaseerd op de [kennisclip 'torsielijn' als onderdeel van het vak 'Constructieve Analyse 3' op de Hogeschool van Amsterdam](https://youtu.be/fqbObUeKPYk) {cite:p}`HvA_torsielijn`

```
````

# Begeleide oefening 1

In [](./instructie2.md) is een deel van de wringende momentenlijn bepaald voor de volgende constructie:

```{figure} ./instructie2_data/torsielijn.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie
number:
---
```
Deze wringende momentenlijn was al gevonden:

```{figure} ./instructie2_data/Mt-lijn_deels.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie
number:
---
```

Waarvan je de rest van de wringende momentenlijn gaat bepalen.

:::::{exercise}
:nonumber: true

Bepaal de wringend momentenlijn.

```{h5p} https://tudelft.h5p.com/content/1292760395413508957/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Het wringend moment in deel $\rm{BC}$:

```{figure} ./instructie2_data/FBD_BC.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie
---
De snedekrachten die gelijk zijn aan $0$ zijn weggelaten.
```

$$
\begin{align*}
\sum T_{\rm{BC}} &= 0 \\
M_{\rm{t}}^{\rm{BC}} + 10 \cdot 3 + 3 \cdot 2 \cdot 1 + \frac{1}{2} \cdot 6 \cdot 2 \cdot \frac{2}{3}&= 0 \\
M_{\rm{t}}^{\rm{BC}} &= -40 \ \rm{kNm} \left( \twoheadrightarrow \mid \twoheadleftarrow \right)
\end{align*} 
$$

Tot slot het wringend moment in deel $\rm{AB}$:

```{figure} ./instructie2_data/FBD_AB.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie
---
De snedekrachten die gelijk zijn aan $0$ zijn weggelaten.
```

$$
\begin{align*}
\sum T_{\rm{AB}} &= 0 \\
M_{\rm{t}}^{\rm{AB}} + 10 \cdot 1 - 3 \cdot 2 \cdot 1 - \frac{1}{2} \cdot 6 \cdot 2 \cdot 1&= 0 \\
M_{\rm{t}}^{\rm{AB}} &= 2 \ \rm{kNm} \left( \twoheadleftarrow \mid \twoheadrightarrow \right)
\end{align*} 
$$

Dit geeft de volgende wringende momentenlijn:

```{figure} ./instructie2_data/Mt-lijn.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie
number:
---
```

::::
