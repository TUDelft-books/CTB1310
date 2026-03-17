# Begeleide oefening 2

Gegeven is de volgende constructie

```{figure} ./lesoefening2/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_rect_oef
:number:
```

:::::{exercise}
:nonumber: true

Wat is de dwarskracht net rechts van $\rm{B}$?

```{h5p} https://tudelft.h5p.com/content/1292769955038569107/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

De constructie heeft een verdeelde belasting $q = 20 \, \rm{kN/m}$ over een lengte van $L_3 = 3 \, \rm{m}$ rechts van punt $\rm{B}$.

Eerst bepalen we de dwarskracht net rechts van $\rm{B}$ (voor de oplegging):

$$
V_{\rm{B,rechts}} = q \cdot L_3 = 20 \cdot 3 = 60 \, \rm{kN}
$$

Nu bepalen we de oplegreactie in $\rm{B}$. Met momentenevenwicht om de linker steunpunt:

$$
B_{\rm{v}} = \cfrac{q \cdot (L_2 + L_3)}{L_2} = \cfrac{20 \cdot (3 + 3)}{3} = 40 \, \rm{kN}
$$

De dwarskracht net links van $\rm{B}$ is:

$$
V_{\rm{B,links}} = V_{\rm{B,rechts}} - B_{\rm{v}} = 60 - 40 = 20 \, \rm{kN}
$$

::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de maximale schuifspanning op een negatieve doorsnede net rechts van $\rm{B}$.

```{h5p} https://tudelft.h5p.com/content/1292769957827644647/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

De doorsnede heeft:
- Breedte: $b = 10 \, \rm{mm}$
- Hoogte: $h = 250 \, \rm{mm}$

Het traagheidsmoment:

$$
I_{zz} = \cfrac{b \, h^3}{12} = \cfrac{10 \cdot 250^3}{12} = 13.02 \cdot 10^6 \, \rm{mm^4}
$$

Het statisch moment van het afschuivend deel door het normaalkrachtencentrum:

$$
S_{z}^{\rm{a}} = \cfrac{b \, h}{4} \cdot \cfrac{h}{2} = \cfrac{10 \cdot 250}{4} \cdot \cfrac{250}{2} = 78125 \, \rm{mm^3}
$$

De maximale schuifspanning (in het normaalkrachtencentrum) met $V_{\rm{B,links}} = 20 \, \rm{kN}$:

$$
\tau_{\rm{max}} = \cfrac{V_z \, S_{z}^{\rm{a}}}{b \, I_{zz}} = \cfrac{20000 \cdot 78125}{10 \cdot 13.02 \cdot 10^6} = 12.0 \, \rm{MPa}
$$

::::

% solution_end

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292769959370185427/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

De vraag betreft waarschijnlijk de dwarskracht bij het linker steunpunt $\rm{S}$.

De dwarskracht bij het linker steunpunt kan bepaald worden door het krachtenevenwicht vanaf links:

$$
V_{\rm{S}} = V_{\rm{B,links}} + q \cdot L_2 = 20 + 20 \cdot 3 = 80 \, \rm{kN}
$$

Of via de oplegreactie:

$$
A_{\rm{v}} = q \cdot L_3 + q \cdot L_2 - B_{\rm{v}} = 20 \cdot 3 + 20 \cdot 3 - 40 = 80 \, \rm{kN}
$$

::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de maximale absolute schuifspanning

```{h5p} https://tudelft.h5p.com/content/1292769961422841717/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

We moeten de maximale schuifspanning bepalen op verschillende locaties in de constructie en de grootste waarde vinden.

**Bij punt B rechts:**

$$
\tau_{\rm{B,rechts}} = \cfrac{V_{\rm{B,rechts}} \, S_{z}^{\rm{a}}}{b \, I_{zz}} = \cfrac{60000 \cdot 78125}{10 \cdot 13.02 \cdot 10^6} = 36.0 \, \rm{MPa}
$$

**Bij punt B links:**

$$
\tau_{\rm{B,links}} = \cfrac{V_{\rm{B,links}} \, S_{z}^{\rm{a}}}{b \, I_{zz}} = \cfrac{20000 \cdot 78125}{10 \cdot 13.02 \cdot 10^6} = 12.0 \, \rm{MPa}
$$

**Bij linker steunpunt S:**

$$
\tau_{\rm{S}} = \cfrac{V_{\rm{S}} \, S_{z}^{\rm{a}}}{b \, I_{zz}} = \cfrac{80000 \cdot 78125}{10 \cdot 13.02 \cdot 10^6} = 48.0 \, \rm{MPa}
$$

De maximale absolute schuifspanning is dus:

$$
\tau_{\rm{max,abs}} = \max\left( 36.0, 12.0, 48.0 \right) = 48.0 \, \rm{MPa}
$$

Deze treedt op bij het linker steunpunt.

::::

% solution_end
