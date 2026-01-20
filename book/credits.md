(credits)=
# Credits en Licentie 📚

Je kunt naar dit boek verwijzen als:

> Tom van Woudenberg van de Technische Universiteit Delft (2025) _CTB1310 - Constructiemechanica 2_. https://oit.tudelft.nl/CTB1310. Bronbestanden op https://github.com/TUDelft-books/CTB1310. CC BY 4.0.

Je kunt naar individuele hoofdstukken of pagina's binnen dit boek verwijzen als:

> `<Titel van Hoofdstuk of Pagina>`. in Tom van Woudenberg van de Technische Universiteit Delft (2025) _CTB1310 - Constructiemechanica 2_. `<url naar specifieke pagina op de boekwebsite>`. Bronbestanden op `<link naar specifieke commit / bestand in github repo>`. CC BY 4.0.

We verwachten dat de inhoud van dit boek aanzienlijk zal veranderen. Daarom raden we aan om direct de broncode te gebruiken met de bovenstaande referentie naar de GitHub-repository, inclusief datum en bestandsnaam. Hoewel er in de loop van de tijd inhoud wordt toegevoegd, blijven hoofdstuktitels en URL's naar verwachting redelijk stabiel. We geven echter geen garantie; als het belangrijk is om naar een specifieke locatie/commit binnen het boek te verwijzen, doe dit dan expliciet.

## Hoe het boek is gemaakt 🛠️💻
Deze website is geschreven in markdown- en jupyternotebook-bestanden, die worden omgezet naar html met behulp van tools van [TeachBooks](https://teachbooks.io/). De bestanden zijn opgeslagen in een [publieke GitHub-repository](https://github.com/TUDelft-books/CTB1310). De website is te bekijken op https://oit.tudelft.nl/CTB1310.

Om de website opnieuw te maken heb je twee opties (meer informatie in de [TeachBooks handleiding](https://teachbooks.io/manual/)):
- In de GitHub-interface: fork deze repository, schakel Github Pages in via de bron GitHub actions (Settings - Code and automation - Pages - Build and deployment - Source - GitHub Actions), schakel workflows in (Actions - I understand my workflows, go ahead and enable them) en voer de call-deploy-book workflow uit (Actions - call-deploy-book - Run workflow - Run workflow). De website wordt gepubliceerd op de URL zoals weergegeven in het workflowoverzicht wanneer de workflow is voltooid (Actions - call-deploy-book - call-deploy-book - Summary).
- Op je eigen computer: clone deze repository, installeer de vereiste pakketten (`pip install -r requirements.txt`) en bouw het boek (`teachbooks build book`). De website wordt lokaal opgeslagen in `book/_build/index.html`.

## Licentie 📝
Dit boek is [CC BY 4.0 gelicenseerd](https://creativecommons.org/licenses/by/4.0/) waardoor je het materiaal mag delen en aanpassen, zolang de bron wordt vermeld.

Een deel van de inhoud van dit boek is afkomstig van bronnen. Deze inhoud heeft geen CC BY licentie maar er is toestemming verleend door de originele auteurs voor gebruik in dit boek. Het gaat om:
- [](simulation_shear_stresses) van {cite:ts}`IDEAStatiCa_shear_RCS`
- [](torsional_displacement) van {cite:ts}`shear_force_center`
- [](shear_center_fig_1) van {cite:ts}`shear_force_center`
- [](shear_center_fig_2) van {cite:ts}`shear_force_center`

(editor)=
## Over de auteur 👨‍🏫

### Tom van Woudenberg

```{figure} figures/Tom.jpg
:width: 300px
:align: center
:class: dark-light
:source: Private collection

&nbsp;
```

Tom is docent aan de Technische Universiteit Delft. Tom heeft een passie voor het mechanicaonderwijs en streeft ernaar een blended leerweg te faciliteren voor studenten, waarin actief leren aantrekkelijk en lonend is.

Tom is in 2020 afgestudeerd bij de Technische Universiteit Delft met onderzoek naar wiskundige optimalisatie van een constructief ontwerp. Van augustus 2020 tot augustus 2022 was Tom werkzaam bij de Hogeschool van Amsterdam als docent constructie, gespecialiseerd in constructiemechanica. Sinds september 2022 is Tom werkzaam bij de TU Delft.

Naast constructiemechanicavakken, geeft Tom vakken over optimalisatie, numerieke methodes, data-analyse en statistiek. Ook begeleidt Tom BSc- en MSc-studenten, deels onderdeel van zijn onderzoekproject over [Macaulay's methode](https://oit.tudelft.nl/Macaulays-method). Daarnaast, ben ik actief betrokken in interfacultaire samenwerkingen zoals [PRIMECH](https://www.tudelft.nl/teachingacademy/communities/primech), [TeachBooks](https://teachbooks.io/) en diverse digitale tooling voor het onderwijs zoals [ANS](https://ans.app/) en Git

- {fa}`envelope` T.R.vanWoudenberg@tudelft.nl
- {fa}`envelope` tomvanw@hotmail.com
- {fa}`phone` +31152789739
- {fa}`location-dot` TU Delft – Civiele Techniek & Geowetenschappen - Afdeling 3MD – Kamer 6.45
- <i class="fa-brands fa-github"></i> [GitHub profiel](https://github.com/Tom-van-Woudenberg)
- <i class="fa-brands fa-linkedin"></i> [LinkedIn profiel](https://www.linkedin.com/in/tom-van-woudenberg/)
- {fa}`building-columns` [TU Delft profiel](https://www.tudelft.nl/en/staff/t.r.vanwoudenberg/)

### Dankwoord 🙏

Daarnaast veel dank aan de diverse collega's en studentassistenten van [TeachBooks](https://teachbooks.io/) voor het samen ontwikkelen van tools en het bieden van ondersteuning om dit boek te verbeteren.
