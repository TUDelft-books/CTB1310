# Instructie

Eerder hebben we het normaalkrachtencentrum gezien: het punt in de doorsnede waaromheen de momenten worden berekend en waarbij een normaalkracht geen kromming veroorzaakt. Op eenzelfde manier is er ook een dwarskrachtencentrum: het punt in de doorsnede waaromheen de wringende momenten worden berekend en waarbij een dwarskracht geen torsievervorming veroorzaakt. Echter is er een gesloten afleiding voor de locatie van het dwarskrachtencentrum niet mogelijk zoals bij het normaalkrachtencentrum. We zullen bekijken waarom dat zo is en hoe we de locatie van het dwarskrachtencentrum dan wel kunnen bepalen op basis van experimentele data en aannames.

:::::{grid} 1 2 2 2
:gutter: 1 1 1 2

::::{grid-item-card} Vervormingen door belasting in $x$-richting
:columns: 12 12 4 4

Over het algemeen zorgt een belasting in de $x$-richting naast rek $\varepsilon$ en normaalspanningen $\sigma$:

```{figure} ./instructie_data/rek.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

Vervormingen door rek $\varepsilon$, leidend tot normaalspanningen $\sigma$.
```

Ook voor kromming $\kappa$ en buigspanningen $\sigma$:

```{figure} ./instructie_data/kromming.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

Vervormingen door kromming $\kappa$, leidend tot buigspanningen $\sigma$.
```


::::

::::{grid-item-card} Vervormingen door belasting in $z$-richting
:columns: 12 12 8 8

Over het algemeen zorgt een belasting in de z- of y-richting naast afschuifrekken en schuifspanningen $\tau$ ten gevolge van afschuiving $\gamma_z$ (die we beide over het algemeen verwaarlozen):

```{figure} ./instructie_data/gamma_z.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

Vervorming door afschuiving $\gamma_z$, leidend tot schuifspanningen $\tau$. Beide worden over het algemeen verwaarloosd.
```

Ook voor torsievervorming (ook $\gamma_{\rm{t}}$ maar mogelijk in een andere richting) en schuifspanningen $\tau$ ten gevolge van torsie.

```{figure} ./instructie_data/gamma_t.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

Vervorming door torsievervorming $\gamma_{\rm{t}}$, leidend tot schuifspanningen $\tau$.
```

Daarnaast hebben we ook nog de schuifspanningen  $\tau$ ten gevolge van kromming $\kappa$ (buiging) zoals we die al kennen uit de vorige lessen:

```{figure} ./instructie_data/kromming_tau.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

Vervorming door kromming $\kappa$, leidend tot schuifspanningen $\tau$.
```

```{figure} ./instructie_data/C5-A2a-1-300x258.jpeg
:align: center
:bib: shear_force_center
:show: author, license, copyright, source, date
:placement: caption

Voorbeeld van een doorsnede die belast wordt in de $z$-richting waarbij zowel buiging $\kappa_z$ als torsievervorming $\gamma_{\rm{t}}$ optreedt.
```


::::
:::::

:::::{grid} 1 2 2 2
:gutter: 1 1 1 2

::::{grid-item-card} Normaalkrachtencentrum volgt uit constitutieve relaties
:columns: 12 12 4 4

Om de plek van het normaalkrachtencentrum te vinden kunnen we de relatie tussen normaalkracht, moment, rek en kromming uitdrukken voor een willekeurige referentiepunt. Hierbij houden we rekening met de aanname dat de doorsnedes vlak blijven en loodrecht op ‘vezels’ staan om het hele vervormingsgedrag te kunnen modelleren. Dat geeft onder andere $N = EA \epsilon + ES_z \kappa_z$:

```{figure} ./instructie_data/N_willekeurig.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

$N$ en $M_z$ als functie van $\epsilon$ en $\kappa_z$ voor een willekeurig referentiepunt.
```

Als we als referentiepunt voor deze relatie het normaalkrachtencentrum nemen is deze per definitie $S_z = 0$, dus zorgt een normaalkracht inderdaad enkel voor rek en niet voor kromming:

```{figure} ./instructie_data/N_NC.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

$N$ en $M_z$ als functie van $\epsilon$ en $\kappa_z$ voor het normaalkrachtencentrum.
```

::::

::::{grid-item-card} Dwarskrachtencentrum volgt **niet** uit constitutieve relaties
:columns: 12 12 8 8

Een zelfde aanpak zouden we kunnen proberen voor om een relatie te vinden tussen dwarskracht, wringend moment, afschuiving en kromming voor een willekeurig referentiepunt. Echter, er is geen algemene vergelijking om dit verband te vinden. Als de vergelijkingen er zou zijn zou die de vorm hebben: $V = \underbrace{... \cdot \gamma_z}_{\rm{verwaarloosd}} + ... \cdot \gamma_t + ... \cdot \kappa_z$.

```{figure} ./instructie_data/V_willekeurig.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

$V$ en $M_{\rm{t}}$ als functie van $\gamma_z$, $\gamma_t$ en $\kappa_z$ voor een willekeurig referentiepunt.
```

Als we dezelfde logica zouden toepassen zou het dwarskrachtencentrum het punt zijn waar alleen de term met de kromming overblijft, oftewel: $V = \underbrace{... \cdot \gamma_z + ... \cdot \gamma_t}_{\rm{=} \, 0} + ... \cdot \kappa_z$. Uit experimenten blijkt dat er een punt is waar dit geldt, maar er is geen algemene afleiding mogelijk zoals bij het normaalkrachtencentrum en dus ook geen formule voor het bepalen van de locatie van het dwarskrachtencentrum:

```{figure} ./instructie_data/V_DC.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

$V$ en $M_{\rm{t}}$ als functie van $\gamma_t$ en $\kappa_z$ voor het dwarskrachtencentrum.
```

```{figure} ./instructie_data/C5-A2b-300x262.jpeg
:align: center
:bib: shear_force_center
:show: author, license, copyright, source, date
:placement: caption

Voorbeeld van een doorsnede die belast wordt met enkel een dwarskracht en waarbij enkel kromming optreedt.
```


::::
:::::

:::::{grid} 1 2 2 2
:gutter: 1 1 1 2

::::{grid-item-card} Normaalkrachtencentrum als resultante normaalspanningen
:columns: 12 12 4 4

Bij een belasting in het normaalkrachtencentrum is er dus enkel rek en geen kromming. De ligging van het normaalkrachtencentrum nu gecontroleerd worden door deze gelijk te stellen aan het aangrijpingspunt van de resultante van de normaalspanningen.


```{figure} ./instructie_data/NC.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

Links een verdeling van normaalspanningen ten gevolge van rek, rechts de resultante van deze normaalspanningen die aangrijpt in het normaalkrachtencentrum.
```

::::

::::{grid-item-card} Dwarskrachtencentrum als resultante schuifspanningen
:columns: 12 12 8 8

Hoewel we enkel experimenteel weten dat er een punt is waar een dwarskracht enkel voor kromming zorgt, kunnen we de ligging van het dwarskrachtencentrum wel vinden door deze gelijk te stellen aan het aangrijpingspunt van de resultante van de schuifspanningen ten gevolge van enkel kromming. Hoewel geldt dat $... \cdot \gamma_z + ... \cdot \gamma_t =  0$ en daarmee ook dat $ \int_A{\left( \tau_{\rm{t.g.v.} \, \rm{afschuiving}} + \tau_{\rm{t.g.v.} \, \rm{wringing}} \right)}dA = 0$ is niet gegarandeerd dat er geen afschuiving- of schuifspanningen ten gevolge van afschuiving of wringing aanwezig zijn in de doorsnede: we kunnen enkel zeggen dat de resultante van deze schuifspanningen nul is.

```{figure} ./instructie_data/DC.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

Links een verdeling van schuifspanningen ten gevolge van kromming, rechts de resultante van deze schuifspanningen die aangrijpt in het dwarskrachtencentrum.
```

::::

:::::

## Implicaties model dwarskrachtencentrum

We hebben gevonden dat we het dwarskrachtencentrum kunnen vinden door de locatie te vinden van de resultante van de schuifspanningen. Voor volledig symmetrische doorsnedes betekent dit dat het dwarskrachtencentrum in het midden ligt, ook al is het niet mogelijk om de schuifspanning te bepalen

```{figure} ./instructie_data/DC_rond.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

Voor deze twee volledig symmetrische doorsnedes ligt het dwarskrachtencentrum in het midden.
```


Voor doorsnedes die slechts in één richting symmetrisch is ligt het dwarskrachtencentrum op de symmetrieas. Voor de andere richting moet de locatie bepaald worden door de resultante van de schuifspanningen in die richting te bepalen. Het snijpunt van de symmetrieas en de werklijn van de resultante is dan het dwarskrachtencentrum.

```{figure} ./instructie_data/DC_symmetrie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

Deze twee doorsnedes zijn symmtrisch in één richting, het dwarskrachtencentrum ligt dan op de symmetrieas.
```

Het berekenen van de resultante van de schuifspanningen ten gevolge van kromming kan enkel gedaan worden voor simpele symmetrische dikwandige of dunwandige doorsneden waarbij de schuifspanningen benaderd kunnen worden met het model afgeleid in de vorige lessen.

```{figure} ./instructie_data/DC_niet.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

In dezelfde twee doorsnedes is ons schuifspanningsmodel niet overal geldig, dus kunnen we de locatie van het dwarskrachtencentrum niet exact bepalen.
```

Voor simpele dunwandige doorsnedes bestaand uit slechts twee randen kan het dwarskrachtencentrum direct gevonden worden omdat de resultante van de schuifspanningen dan altijd aangrijpt in het verbindingspunt van de twee randen.

```{figure} ./instructie_data/dunwandig_DC.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_force_center_2

Voor deze dunwandige varianten is het dwarskrachtencentrum direct te vinden.
```

Daarmee kunnen we de volgende aanpak beschrijven voor het bepalen van het dwarskrachtencentrum:

::::::{prf:algorithm} Bepalen schuifspanningsverloop in een doorsnede
:nonumber: true
:label: alg:dc

1. Voor elke richting die geen symmetrieas heeft:
2. Bepaal voor een willekeurige snedekracht in die richting het schuifspanningsverloop in de doorsnede ten gevolge van enkel kromming.
3. Bepaal de werklijn van de resultante van deze schuifspanningen.
4. Het dwarskrachtencentrum is het snijpunt van deze werklijn met de symmetrieas (indien aanwezig) of de werklijn in de andere richting.

::::::

Het bepalen van het dwarskrachtencentrum wordt getoond in het volgende voorbeeld.

::::::{prf:example}
:nonumber: true

...

::::::