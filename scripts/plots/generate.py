#!/usr/bin/env python3
"""Erzeugt alle statischen SVG-Plots der Website.

Aufruf (aus dem Repo-Root oder von beliebig woanders):

    python scripts/plots/generate.py                 # alle Seiten
    python scripts/plots/generate.py --only demo     # nur eine Seite

Jede Seite hat ein Modul in scripts/plots/pages/ mit zwei Attributen:
    PAGE  – Slug der Seite, z. B. "funktionen/funktionsbegriff"
    PLOTS – Liste von plotstyle.Plot-Deklarationen

Die SVGs landen in src/assets/plots/<PAGE>/<name>.svg und werden committet.
Der Website-Build (npm run build) benötigt Python NICHT.
"""

from __future__ import annotations

import argparse
import importlib
import pkgutil
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
OUT_ROOT = REPO_ROOT / "src" / "assets" / "plots"

sys.path.insert(0, str(SCRIPT_DIR))

import plotstyle  # noqa: E402


def load_page_modules() -> list:
    """Lädt alle Seitenmodule aus scripts/plots/pages/."""
    pages_dir = SCRIPT_DIR / "pages"
    modules = []
    for info in sorted(pkgutil.iter_modules([str(pages_dir)]), key=lambda m: m.name):
        module = importlib.import_module(f"pages.{info.name}")
        if not hasattr(module, "PAGE") or not hasattr(module, "PLOTS"):
            sys.exit(f"FEHLER: pages/{info.name}.py braucht PAGE und PLOTS.")
        modules.append(module)
    return modules


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        metavar="PAGE_SLUG",
        help='nur die Plots einer Seite erzeugen, z. B. "demo" oder "funktionen/funktionsbegriff"',
    )
    args = parser.parse_args()

    modules = load_page_modules()
    if args.only:
        modules = [m for m in modules if m.PAGE == args.only]
        if not modules:
            known = ", ".join(m.PAGE for m in load_page_modules())
            sys.exit(f'FEHLER: Seite "{args.only}" unbekannt. Bekannt: {known}')

    total = 0
    for module in modules:
        out_dir = OUT_ROOT / module.PAGE
        out_dir.mkdir(parents=True, exist_ok=True)
        for spec in module.PLOTS:
            out_path = out_dir / f"{spec.name}.svg"
            plotstyle.render(spec, str(out_path))
            print(f"  {out_path.relative_to(REPO_ROOT)}")
            total += 1

    print(f"{total} Plot(s) erzeugt.")


if __name__ == "__main__":
    main()
