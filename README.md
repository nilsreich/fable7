# Mathe BGY 11

Unterrichtsbegleitende Website für den Mathematikunterricht der
Jahrgangsstufe 11 am Beruflichen Gymnasium (Rheinland-Pfalz).
Gebaut mit [Astro](https://astro.build) + [Starlight](https://starlight.astro.build),
Mathematik-Rendering mit KaTeX, Funktionsgraphen als statische SVGs.

## Befehle

| Befehl | Wirkung |
| --- | --- |
| `npm install` | Abhängigkeiten installieren |
| `npm run dev` | Dev-Server unter `localhost:4321` (zeigt auch Entwurfsseiten) |
| `npm run build` | Produktions-Build nach `./dist/` (Entwurfsseiten ausgeblendet) |
| `npm run preview` | Produktions-Build lokal ansehen |

## Beamer-Modus

Für die Projektion im Unterricht (halber Bildschirm neben dem Schreib-Canvas):
an eine beliebige Seiten-URL `?beamer` anhängen **oder** den Knopf „Beamer“
unten rechts antippen. Sidebar und Inhaltsverzeichnis verschwinden, Schrift
und Formeln werden größer. Der Modus bleibt beim Seitenwechsel erhalten;
`?beamer=off` oder erneutes Antippen beendet ihn.

## Interaktive Elemente

`public/interaktiv.js` (eingebunden über den `head` in `astro.config.mjs`)
schaltet die Kästchen der Checklisten zur Klassenarbeit frei — der Stand wird
pro Seite in `localStorage` gespeichert — und fügt den Beamer-Schalter ein.
Die Quiz-Antworten tragen Buchstaben A–D für das Abstimmen per Handzeichen
(`src/components/Quiz.astro`, ohne Client-JavaScript).

## Plots

Alle Funktionsgraphen sind statische SVGs in `src/assets/plots/` und werden
mit committet — der Website-Build benötigt **kein** Python.

Neu generieren (Python 3 + `pip install -r scripts/plots/requirements.txt`):

```sh
python scripts/plots/generate.py                 # alle Seiten
python scripts/plots/generate.py --only demo     # nur eine Seite
```

Ein Plot = eine Deklaration in `scripts/plots/pages/<seite>.py`
(Funktionsterm als Lambda, Definitionsbereich, Beschriftungen).
Der Stil (Achsenkreuz mit Pfeilen, Farben, Schriftgrößen) ist zentral in
`scripts/plots/plotstyle.py` festgelegt und für alle Plots identisch.
Die Ausgabe ist deterministisch: gleiche Eingabe → byte-identisches SVG.

## Inhaltsseiten

- Vorlage: `src/content/docs/_template.mdx` (wird nicht gebaut).
- Noch nicht fertige Seiten stehen als `draft: true` im Repo; sie erscheinen
  im Dev-Modus, aber nicht im Produktions-Build. Zum Freischalten die
  `draft`-Zeile entfernen.
- Sidebar-Gruppen sind in `astro.config.mjs` konfiguriert; die Reihenfolge
  innerhalb einer Gruppe steuert `sidebar.order` im Frontmatter.
