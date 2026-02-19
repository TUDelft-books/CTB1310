# Instructie

Tot nu toe hebben we enkel gerekend aan buigende momenten. Echter, op en in sommige constructies komen ook wringende momenten voor. Waar buigende momenten om de lokale $y$- of $z$-as werken en zorgen voor verplaatsingen in de $z$ ($M_z$) en $y$ ($M_y$) richting, werken wringende momenten om de $x$-as van de doorsnede en zorgen voor rotaties om de $x$-as ($M_{\rm{t}}$, met de $\rm{t}$ van 'torsion'). Deze rotaties om de $x$-as noemen we verwringing.

:::::{prf:example}
:nonumber: true

In onderstaande figuur is een voorbeeld gegeven van een doorsnede die wordt belast met een wringend moment $M_{\rm{t}}$ en daardoor verwringt.

```{figure} ./instructie_data/torsion.png
:align: center
:bib: shear_force_center
:show: author, license, copyright, source, date
:placement: caption
:name: torsional_displacement
:number:
```

:::::

## Model locatie dwarskrachtencentrum

Bij buiging hebben we het normaalkrachtencentrum gezien: het punt in de doorsnede waaromheen de momenten worden berekend en waarbij een normaalkracht geen kromming veroorzaakt. Op eenzelfde manier is er ook een dwarskrachtencentrum: het punt in de doorsnede waaromheen de wringende momenten worden berekend en waarbij een dwarskracht niet voor verwringing zorgt. Echter is er een gesloten afleiding voor de locatie van het dwarskrachtencentrum niet mogelijk zoals bij het normaalkrachtencentrum. We zullen bekijken waarom dat zo is en hoe we de locatie van het dwarskrachtencentrum dan wel kunnen bepalen op basis van experimentele data en aannames.

::::::{grid} 1 2 2 2
:gutter: 1 1 1 2

:::::{grid-item-card} Vervormingen door belasting in $x$-richting
:columns: 12 12 4 4

Over het algemeen zorgt een belasting in de $x$-richting naast extensie, met rek $\varepsilon$ en normaalspanningen $\sigma$:

```{figure} ./instructie_data/rek.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

Ook voor buiging, met op infinitesimaal niveau kromming $\kappa$ en buigspanningen $\sigma$:

```{figure} ./instructie_data/kromming.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```


:::::

:::::{grid-item-card} Vervormingen door belasting in $z$-richting
:columns: 12 12 8 8

Over het algemeen zorgt een belasting in de z- of y-richting naast afschuiving, met afschuifrekken $\gamma$ en schuifspanningen $\tau$ (die we beide over het algemeen verwaarlozen):

```{figure} ./instructie_data/gamma_z.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

Ook voor verwringing, $\chi$, en schuifspanningen $\tau$. Deze rekken en spanningen zijn echter meestal niet verwaarloosbaar:

```{figure} ./instructie_data/gamma_t.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

Daarnaast hebben we ook nog de schuifspanningen $\tau$ ten gevolge van buiging en de kromming $\kappa$ van opeenvolgende doorsnedes zoals we die al kennen uit de vorige lessen:

```{figure} ./instructie_data/kromming_tau.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

Uit experimenten zijn de de draaiing van een doorsnede en buiging duidelijk zichtbaar.

::::{prf:example}
:nonumber: true

In onderstaande figuur is een voorbeeld getoond van een doorsnede die belast wordt in de $z$-richting waarbij zowel buiging als verwringing van de doorsnede optreedt.

```{figure} ./instructie_data/C5-A2a-1-300x258.jpeg
:align: center
:bib: shear_force_center
:show: author, license, copyright, source, date
:placement: caption
:name: shear_center_fig_1
:number:
```

::::

:::::
::::::

::::::{grid} 1 2 2 2
:gutter: 1 1 1 2

:::::{grid-item-card} Normaalkrachtencentrum volgt uit constitutieve relaties
:columns: 12 12 4 4

Om de plek van het normaalkrachtencentrum te vinden kunnen we de relatie tussen normaalkracht, moment, rek en kromming uitdrukken voor een willekeurige referentiepunt. Dat geeft onder andere $N = EA \epsilon + ES_z \kappa_z$:

```{figure} ./instructie_data/N_willekeurig.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

Als we als referentiepunt voor deze relatie het normaalkrachtencentrum nemen is deze per definitie $S_z = 0$, dus zorgt een normaalkracht inderdaad enkel voor rek en niet voor kromming:

```{figure} ./instructie_data/N_NC.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

:::::

:::::{grid-item-card} Dwarskrachtencentrum volgt **niet** uit constitutieve relaties
:columns: 12 12 8 8

Een zelfde aanpak zouden we kunnen proberen voor om een relatie te vinden tussen dwarskracht, wringend moment, afschuifrekken, verwringing en kromming voor een willekeurig referentiepunt. Echter, er is geen algemene vergelijking om dit verband te vinden. Als de vergelijkingen er zou zijn zou die de vorm hebben: $V = \underbrace{... \cdot \gamma}_{\rm{verwaarloosd}} + ... \cdot \chi + ... \cdot \kappa_z$.

```{figure} ./instructie_data/V_willekeurig.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

Als we dezelfde logica zouden toepassen zou het dwarskrachtencentrum het punt zijn waar alleen de term met de kromming overblijft, oftewel: $V = \underbrace{... \cdot \gamma + ... \cdot \chi}_{\rm{=} \, 0} + ... \cdot \kappa_z$.

```{figure} ./instructie_data/V_DC.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

Uit experimenten blijkt dat er een punt is waar dit geldt, maar er is geen algemene afleiding mogelijk zoals bij het normaalkrachtencentrum en dus ook geen formule voor het bepalen van de locatie van het dwarskrachtencentrum.

::::{prf:example}
:nonumber: true

Hieronder is een voorbeeld getoond van een doorsnede die belast wordt met enkel een dwarskracht en waarbij enkel buiging optreedt en geen verwringing.

```{figure} ./instructie_data/C5-A2b-300x262.jpeg
:align: center
:bib: shear_force_center
:show: author, license, copyright, source, date
:placement: caption
:name: shear_center_fig_2
:number:
```
::::

:::::
::::::

:::::::{grid} 1 2 2 2
:gutter: 1 1 1 2

::::::{grid-item-card} Normaalkrachtencentrum als resultante normaalspanningen
:columns: 12 12 4 4

Bij een belasting in het normaalkrachtencentrum is er dus enkel rek en geen buiging. De ligging van het normaalkrachtencentrum nu gecontroleerd worden door deze gelijk te stellen aan het aangrijpingspunt van de resultante ({numref}`fig:normal_force_center_force`) van de normaalspanningen ({numref}`fig:normal_force_center_stresses`).

::::{grid} 2 2 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/NC_2.svg
:align: center
:name: fig:normal_force_center_force
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/NC_1.svg
:align: center
:name: fig:normal_force_center_stresses
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

:::

::::

In dit geval zijn er geen buigspanningen.

::::::

::::::{grid-item-card} Dwarskrachtencentrum als resultante schuifspanningen
:columns: 12 12 8 8

Hoewel we enkel experimenteel weten dat er een punt is waar een dwarskracht enkel voor buiging zorgt, kunnen we de ligging van het dwarskrachtencentrum wel vinden door deze gelijk te stellen aan het aangrijpingspunt van de resultante ({numref}`fig:shear_center_force`) van de schuifspanningen ({numref}`fig:shear_center_stresses`) ten gevolge van enkel buiging.

::::{grid} 2 2 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/DC_2.svg
:align: center
:name: fig:shear_center_force
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/DC_1.svg
:align: center
:name: fig:shear_center_stresses
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

:::

::::

We kunnen echter niet garanderen dat er geen afschuiving- of schuifspanningen ten gevolge van afschuiving of verwringing aanwezig zijn in de doorsnede.

::::::
:::::::

## Implicaties model dwarskrachtencentrum

### Volledige symmetrische doorsnedes
We hebben gevonden dat we het dwarskrachtencentrum kunnen vinden door de locatie te vinden van de resultante van de schuifspanningen. Voor volledig symmetrische doorsnedes betekent dit dat het dwarskrachtencentrum in het midden ligt, ook al is het niet mogelijk om de schuifspanning te bepalen.

Deze volledige symmetrische doorsnedes zijn de enige doorsnedes waarbij het dwarskrachtencentrum op dezelfde plek ligt als het normaalkrachtencentrum.

::::::{prf:example}
:nonumber: true

Voor de volgende twee doorsnedes is dat het geval:

::::{grid} 2 2 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/DC_rond_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/DC_rond_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

:::
::::

::::::

### Gedeeltelijk symmetrische doorsnedes

Voor doorsnedes die slechts in één richting symmetrisch is ligt het dwarskrachtencentrum op de symmetrieas. Voor de andere richting moet de locatie bepaald worden door de resultante van de schuifspanningen in die richting te bepalen. Het snijpunt van de symmetrieas en de werklijn van de resultante is dan het dwarskrachtencentrum.

::::::{prf:example}
:nonumber: true

De volgende twee doorsnedes zijn symmtrisch in de $z$-richting, het dwarskrachtencentrum ligt dan op de symmetrieas.

::::{grid} 2 2 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/DC_symmetrie_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/DC_symmetrie_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

:::
::::

::::::

### Schuifspanningsmodel niet geldig

Het berekenen van de resultante van de schuifspanningen ten gevolge van buiging kan enkel gedaan worden voor simpele symmetrische dikwandige of dunwandige doorsneden waarbij de schuifspanningen benaderd kunnen worden met het model afgeleid in de vorige lessen.

::::::{prf:example}
:nonumber: true

Voor de volgende doorsnedes is ons schuifspanningsmodel maar beperkt geldig, dus kunnen we de locatie van het dwarskrachtencentrum niet exact bepalen. Echter geldt vanwege symmetrie nog wel dat het dwarskrachtencentrum ergens op de symmetrieas ligt.

::::{grid} 2 2 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/DC_niet_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/DC_niet_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

:::
::::

::::::

### Dunwandige doorsnedes met twee rechte randen
Voor simpele dunwandige doorsnedes bestaand uit slechts twee rechte randen kan het dwarskrachtencentrum direct gevonden worden omdat de resultante van de schuifspanningen dan altijd aangrijpt in het verbindingspunt van de twee randen.

::::::{prf:example}
:nonumber: true

Voor de twee doorsnedes hieronder geldt dat het dwarskrachtencentrum direct gevonden kan worden.

::::{grid} 2 2 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/dunwandig_DC_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/dunwandig_DC_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

:::
::::

::::::

Daarmee kunnen we de volgende aanpak beschrijven voor het bepalen van het dwarskrachtencentrum:

::::::{prf:algorithm} Bepalen schuifspanningsverloop in een doorsnede
:nonumber: true
:label: alg:dc

1. Voor elke richting die geen symmetrieas heeft:
2. Bepaal voor een willekeurige snedekracht in die richting het schuifspanningsverloop in de doorsnede ten gevolge van enkel buiging.
3. Bepaal de werklijn van de resultante van deze schuifspanningen.
4. Het dwarskrachtencentrum is het snijpunt van deze werklijn met de symmetrieas (indien aanwezig) of de werklijn in de andere richting.

::::::

## Voorbeeld

Het bepalen van het dwarskrachtencentrum wordt getoond in het volgende voorbeeld.

::::::{prf:example}
:nonumber: true

Gegevens is de volgende constructie en doorsnede:

::::{grid} 2 2 2 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```
:::

:::{grid-item}
:columns: auto

```{figure} ./instructie_data/doorsnede.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```
:::

::::

De doorsnede is symmetrisch in de $y$-richting, maar niet in de $z$-richting. We weten daarmee dat het dwarskrachtencentrum op de verticale symmetrieas ligt:

```{figure} ./instructie_data/voorbeeld_symmetrie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

Om de ligging op de symmetrieas te bepalen moeten we de schuifspanningen ten gevolge van kromming in de $y$-richting bepalen. De grootte van de kromming is niet relevant omdat we enkel de werklijn van de resultante zoeken. In ons schuifspanningsmodel kunnen we dus een willekeurige waarde kiezen voor de dwarskracht in de $y$-richting. We kiezen hiervoor een waarde van $128 \, \rm{kN}$, enkel omdat deze waarde op mooie gehele waardes uitkomt. Over het algemeen weet je dat niet bij een berekening.

Als we een dwarskracht in de $y$-richting op deze doorsnede aannemen kunnen we zonder een berekening te maken al het volgende zeggen over de schuifspanningen in de verschillende delen van de doorsnede:

- Op de vrije uiteindes van de flens is de schuifspanning gelijk aan 0
- De verticale flens zal een lineair verloop van de schuifspanning hebben in de verticale richting.
- Het horizontale lijf zal een parabolisch verloop van de schuifspanning hebben in de horizontale richting.
- Het maximum van de schuifspanning zit ter breedte van het normaalkrachtencentrum die op de symmetrieas ligt omdat daar het statisch moment van het afschuivend gedeelte het grootst is.
- Vanwege de stroming van de schuifstroom zal de schuifspanning vanuit de vrije uiteindes naar het lijf stromen, daar samenvoegen en in de andere flenzen weer splitsen en naar de vrije uiteindes stromen.

```{figure} ./instructie_data/voorbeeld_verloop.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:
```

Om de daadwerkelijke waardes te berekenen hebben we in ieder geval het traagheidsmoment $I_{yy}$ nodig. De hoogte van het zwaartepunt in de $z$-richting hebben we daarvoor niet nodig.

$$
\begin{align*}
I_{yy} = & 2 \cdot \left(\underbrace{\cfrac{1}{12}\cdot \left(160+40\right)\cdot 8^3}_{\rm{wordt}   \, \rm{verwaarloosd}} +\left(40+160\right) \cdot 8 \cdot  200^2 \right)\ \\
& + \cfrac{1}{12}\cdot 8 \cdot 400^3\\
\approx & 170.\bar{6} \cdot 10^6 \, \rm{mm^4}
\end{align*}
$$

Uit het eerder bepaalde verloop blijkt dat een aantal punten interessant zijn om de schuifspanning te bepalen:

- Ter breedte van het normaalkrachtencentrum
- Rondom de aansluiting van het lijf met de flens

Beginnend met de schuifspanning op het afschuifvlak net boven de aansluiting van het lijf met de flens:

```{figure} ./instructie_data/S1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:  
```

$$
\begin{align*}
S_{y}^{\rm{a}} &= 8 \cdot 40 \cdot \left(-200\right) = -64000 \, \rm{mm^3} \\
\tau &\approx \cfrac{\left| 128000 \cdot \left(-64000\right)\right|}{8 \cdot  170.\bar{6} \cdot 10^6 } \approx 6 \, \rm{MPa}
\end{align*}
$$

Vervolgens de schuifspanning op het afschuifvlak net onder de aansluiting van het lijf met de flens:

```{figure} ./instructie_data/S2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:  
```

$$
\begin{align*}
S_{y}^{\rm{a}} &= 8 \cdot 160 \cdot \left(-200\right) = -256000 \, \rm{mm^3} \\
\tau &\approx \cfrac{\left| 128000 \cdot \left(-256000\right)\right|}{8 \cdot  170.\bar{6} \cdot 10^6 } \approx 24 \, \rm{MPa}
\end{align*}
$$

Vervolgens de schuifspanning op het afschuifvlak net links van de aansluiting van het lijf met de flens:

```{figure} ./instructie_data/S3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:  
```

$$
\begin{align*}
S_{y}^{\rm{a}} &= -64000 + \left(-256000\right) = -320000 \, \rm{mm^3} \\
\tau &\approx \cfrac{\left| 128000 \cdot \left(-320000\right)\right|}{8 \cdot  170.\bar{6} \cdot 10^6 } \approx 30 \, \rm{MPa}
\end{align*}
$$

En tot slot de schuifspanning op het afschuifvlak ter breedte van het normaalkrachtencentrum:

```{figure} ./instructie_data/S4.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2
:number:  
```

$$
\begin{align*}
S_{y}^{\rm{a}} &= -320000 + 8 \cdot 200 \cdot \left(-100\right) = -480000 \, \rm{mm^3} \\
\tau &\approx \cfrac{\left| 128000 \cdot \left(-480000\right)\right|}{8 \cdot  170.\bar{6} \cdot 10^6 } \approx 45 \, \rm{MPa}
\end{align*}
$$

Dit geeft het volgende schuifspanningsverloop:

```{figure} ./instructie_data/conclusie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

Om de locatie van het dwarskrachtencentrum te bepalen moeten we nu de werklijn van de resultante van deze schuifspanningen bepalen. Daarvoor kunnen we eerst de resultante kracht op elk deel van de doorsnede bepalen:

```{figure} ./instructie_data/resultantes.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

Beginnend met $F_1$, de kracht op het bovenste deel van de flens is:

$$
F_1 \approx \frac{1}{2} \cdot 8 \cdot 40 \cdot 6 \approx 960 \, \rm{N}
$$

Vervolgens $F_2$, de kracht op het onderste deel van de flens is:

$$
F_2 \approx \frac{1}{2} \cdot 8 \cdot 160 \cdot 24 \approx 15360 \, \rm{N}
$$

Vervolgens $F_3$, de kracht op het linker deel van het lijf is. Deze kan bepaald worden door de schuifspanningsverdeling op te delen in een rechthoek en parabolisch deel:

```{figure} ./instructie_data/parabool.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

$$
F_3 \approx 8 \cdot 400 \cdot 30 + \frac{2}{3} \cdot 8 \cdot 400 \cdot \left(45-30\right) \approx 128000 \, \rm{N}
$$

:::::{note}
Deze waarde had je ook kunnen vinden door gelijk te stellen aan de totale dwarskracht van $128 \, \rm{kN}$: het lijf draagt immers de volledige dwarskracht in $y$-richting.
:::::

Vervolgens kan de werklijn van de resultante gevonden worden. De totale kracht is $128 \, \rm{kN}$ in horizontale richting en $0 \, \rm{N}$ in verticale richting. De werklijn kan daarmee gevonden worden:

```{figure} ./instructie_data/werklijn_onb.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

$$
\begin{align*}
\left. \sum T \right| _{\rm{lijf}}^{\rm{spanningen}} &= \left. \sum T \right| _{\rm{lijf}}^{128 \, \rm{kN}}\\
-128 \cdot z_{\rm{D.C.}} &= 0.96 \cdot 200 + 0.96 \cdot 200 - 15.36 \cdot 200 - 15.36 \cdot 200 \\
z_{\rm{D.C.}} &= 45 \, \rm{mm}
\end{align*}
$$

Dus de horizontale werklijn van de resultante van de schuifspanningen grijpt $45 \, \rm{mm}$ boven het lijf aan:

```{figure} ./instructie_data/werklijn_bek.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

Daarmee kan de locatie van het dwarskrachtencentrum worden bepaald door het snijpunt van deze werklijn met de symmetrieas te bepalen:

```{figure} ./instructie_data/DC_oplossing.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_dunwandig
:number:
```

::::::

## Alternatieve afleiding
In hoofdstuk 5.5 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` wordt er gesproken over 'geen torsie'. Dit moet geïnterpreteerd worden als geen draaiing van de doorsnede. Het betekent niet dat er geen torsieafschuifrek is. Later wordt ook gesteld dat er enkel spanningen ten gevolge van buiging optreden als de dwarskracht in het dwarskrachtencentrum aangrijpt, dat kan niet zomaar gesteld worden zoals hierboven beschreven.

## Meer voorbeelden
In hoofdstuk 5.5 van het boek Mechanica, spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` worden meer voorbeelden gegeven van het bepalen van het dwarskrachtencentrum.

% ## Instructies in collegevorm
%
% Dit onderwerp is [les ...](...) gepresenteerd in collegevorm tot ....

## Oefeningen
[Opgaves 5.49 - 5.54 in hoofdstuk 5 van het boek Mechanica, spanningen, vervormingen en verplaatsingen](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/files/TM2vraagstukkenbundel.pdf) {cite:p}`Hartsuijker2013`. Antwoorden zijn [hier](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol2/Chapter5/) beschikbaar.
