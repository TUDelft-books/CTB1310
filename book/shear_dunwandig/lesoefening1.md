````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is gebaseerd op [deze oefening uit het online boek van het vak CT1000S Structural Mechanics op de Technische Universiteit Delft](https://oit.tudelft.nl/CT1000/2024/week_30/session/intro.html#exam-assignment-3-continuum-mechanics) {cite:p}`CT1000_2024`.

```
````

# Begeleide oefening 1

Gegeven is de volgende constructie en doorsnede:

```{figure} ./lesoefening1_data/constructie.svg
:align: center
:class: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/continuum
:number:
```

Gevraagd is de normaal- en schuifspanning op een positieve snede in staaf $\rm{CD}$ net links van $\rm{D}$ in punt $\rm{E}$.

:::::{exercise}
:nonumber: true

Bepaal de snedekrachten in staaf $\rm{CD}$ net links van $\rm{D}$ volgens het assenstelsel.

```{h5p} https://tudelft.h5p.com/content/1292779192165205097/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Som van de momenten om punt A geeft:
$$
\begin{align*}
\sum T_{\rm{A}} &= 0 \\
+ B_{\rm{v}} \cdot 6 - 24 \cdot 6 \cdot 6 &= 0 \\
B_{\rm{v}} &= 144 \ \rm{kN} \left( \uparrow \right)
\end{align*}
$$

Verticaal en horizontaal evenwicht geeft:
$$
\begin{align*}
A_{\rm{v}} &= 0 \ \rm{kN}  \\
A_{\rm{h}} &= 0 \ \rm{kN}
\end{align*}
$$

Dit geeft dat de pendelstaven $AC$ en $AB$ nul staven zijn. De overige snede krachten kunnen bijvoorbeeld worden berekend met knoopevenwicht. Beginnend bij knoop $B$ en vervolgens knoop $C$ en $D$ geeft dit de volgende snede krachten:

```{figure} ./lesoefening1_data/constructie_FBD.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/continuum
:number:
```
Alleen staaf $CD$ is dus geen pendelstaaf, aangezien de staaf wordt belast door de q-last.

...

::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de doorsnedegrootheden

```{h5p} https://tudelft.h5p.com/content/1292779202594208307/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

$$
\begin{align*}
A &= 3 \cdot 300 \cdot 12\\&= 10800 \ \rm{mm^2}\\
\triangle z_{\rm{N.C.}} &= \frac{(12 \cdot 300)\cdot 300 + 2 \cdot (12 \cdot 300)\cdot 150}{3 \cdot 12 \cdot 300}\\ &= 200 \ \rm{mm}\\
I_{zz} &= \frac{12^3 \cdot 300}{12} + 300 \cdot 12 \cdot 100^2 + 2 \cdot \left( \frac{12 \cdot 300^3}{12} + 12 \cdot 300 \cdot 50^2 \right) \\
&= 108043200 \ \text{mm}^4 \\
&\approx 108 \cdot 10^6 \ \text{mm}^4
\end{align*}
$$

...

::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de normaalspanning en schuifspanning op een positieve snede in staaf $\rm{CD}$ net links van $\rm{D}$ in punt $\rm{E}$. Geef een positief antwoord voor een trekspanning en een positief antwoord voor een schuifspanning die omlaag wijst.

```{h5p} https://tudelft.h5p.com/content/1292779206036944887/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

$$
\begin{align*}
\sigma &= \frac{54000}{10800} \\
&= 5 \ \text{MPa} \\[6pt]

S_{z}^{\rm{a}} &= 2 \cdot (12 \cdot 300 \cdot 50) \\
&= 360000 \ \text{mm}^3 \\[6pt]

\tau &= \frac{-72000 \cdot 360000}{(2 \cdot 12)\cdot 108 \cdot 10^6} \\
&\approx -10 \ \text{MPa}
\end{align*}
$$


...

::::

% solution_end
