% Source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie

# Evenwichtsvergelijkingen voor wringende momenten

Net zoals bij krachten en momenten voor buiging, kunnen we ook voor wringende momenten met evenwichtsvergelijkingen oplegreacties en inwendige wringende momenten bepalen. Daarvoor is de aanpak vergelijkbaar met die van buigende momenten.

::::::{prf:algorithm} Evenwicht voor wringende momenten
:nonumber: true

1. Teken het vrijlichaamsschema van de constructie of maak een snede en teken het vrijlichaamschema van een deel van de constructie. Neem wringende momenten aan bij een inklemming of starre verbinding.
2. Stel de evenwichtsvergelijkingen op voor de wringende momenten rondom een as in de richting van een staaf: $\sum T_{\rm{staaf}} = 0$. Alle krachten, buigende en wringende momenten die een draaiing rondom deze as veroorzaken komen in deze evenwichtsvergelijking terecht.
3. Los de evenwichtsvergelijking op om de onbekende wringende momenten of oplegreacties te bepalen.
4. Herhaal dit op alle karakteristieke punten op de wringende momentenlijn te bepalen.

::::::

De toepassing van de evenwichtsvergelijkingen wordt getoond op onderstaande voorbeeld.

::::::{prf:example}
:nonumber: true

```{figure} ./instructie2_data/torsielijn.svg
---
align: center
---
Voorbeeldconstructie
```

Voor deze constructie wordt gevraagd naar de wringende momentenlijn.

Daarvoor maken we op alle karakteristieke punten een snede. Beginnend bij $\rm{G}$ aan de kant van $\rm{GH}$:

```{figure} ./instructie2_data/FBD_GH.svg
---
align: center
---
Vrijlichaamsschema van deel $\rm{GH}$ met het globale $y,z-$ assenstelsel. Het buigend moment $M_z$ is aangegeven met een kromme pijl en het wringend moment $M_{\rm{t}}$ met een pijl met dubbele pijlpunt. De snedekrachten in de andere vlakken en de normaalkracht zijn weggelaten.
```

Hiervoor kan een evenwichtsvergelijking worden opgesteld rondom de as:

$$
\begin{align*}
\sum T_{\rm{GH}} &= 0 \\
M_{\rm{t,G}}^{\rm{GH}} &= 0
\end{align*}
$$

Daarmee kan een beginnetje worden gemaakt met de wringende momentenlijn:

```{figure} ./instructie2_data/Mt-lijn-GH.svg
---
align: center
---
Wringende momentenlijn met enkel deel $\rm{GH}$ bekend
```

Vervolgens maken we een snede in $\rm{E}$:

```{figure} ./instructie2_data/FBD_EH.svg
---
align: center
---
Vrijlichaamsschema van deel $\rm{EH}$ met het globale $x,y,z-$ assenstelsel. De snedekrachten die gelijk zijn aan $0$ zijn weggelaten.
```

$$
\begin{align*}
\sum T_{\rm{EG}} &= 0 \\
-M_{\rm{t,E}}^{\rm{EH}} - 10 \cdot 1 &= 0 \\
M_{\rm{t,E}}^{\rm{EH}} &= -10 \, \rm{kNm} \includegraphics{instructie2_data/richting_EH.svg} 
\end{align*}
$$

text<img style="display:inline-block; height:2em; width:auto; transform:translate(0, 0.75em)" src="instructie2_data/richting_EH.svg" alt="Jupyter book v1"> text

::::::