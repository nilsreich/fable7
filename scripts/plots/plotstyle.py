"""Einheitlicher Stil für alle Funktionsgraphen der Mathe-Website.

Alle Plots werden ausschließlich über die Datenklassen `Plot`, `Curve` und
`Point` deklariert und von `render()` gerendert. So sehen alle Graphen der
Website identisch aus (Achsenkreuz mit Pfeilen, Gitter, Farben, Schrift).

Farbkonventionen (site-weit verbindlich):
    f(x)   blau      COLOR_F
    f'(x)  rot       COLOR_F1
    f''(x) grün      COLOR_F2
    Ortskurven       violett, gestrichelt   COLOR_ORT
    Sekanten/Tangenten orange               COLOR_TANGENTE
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Sequence

import matplotlib

matplotlib.use("SVG")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

COLOR_F = "#1f77b4"  # blau
COLOR_F1 = "#d62728"  # rot
COLOR_F2 = "#2ca02c"  # grün
COLOR_ORT = "#9467bd"  # violett (Ortskurven, gestrichelt)
COLOR_TANGENTE = "#ff7f0e"  # orange (Sekanten/Tangenten)

_GRID_COLOR = "#c9c9c9"
_AXIS_COLOR = "#1a1a1a"
_BASE_FONTSIZE = 15  # bei 800 px SVG-Breite → ≈ 14 px bei 600 px Darstellung

# Deterministische SVG-Ausgabe: feste IDs, kein Zeitstempel.
matplotlib.rcParams.update(
    {
        "svg.hashsalt": "mathe-bgy11",
        "font.family": "DejaVu Sans",
        "font.size": _BASE_FONTSIZE,
        "mathtext.fontset": "dejavusans",
        "axes.unicode_minus": True,
    }
)


def fmt_de(value: float) -> str:
    """Zahl im deutschen Format (Dezimalkomma, echtes Minuszeichen)."""
    if value == int(value):
        text = str(int(value))
    else:
        text = f"{value:g}".replace(".", ",")
    return text.replace("-", "−")


def punkt(kuerzel: str, x: float, y: float) -> str:
    """Beschriftung im Stil H(1|2,5)."""
    return f"{kuerzel}({fmt_de(x)}|{fmt_de(y)})"


@dataclass
class Curve:
    """Eine Kurve: Funktionsterm als Lambda plus Darstellung."""

    fn: Callable[[np.ndarray], np.ndarray]
    label: str | None = None  # mathtext, z. B. r"$f(x)=x^2$"
    color: str = COLOR_F
    linestyle: str = "-"
    linewidth: float = 2.4
    domain: tuple[float, float] | None = None  # überschreibt xlim der Figur


@dataclass
class Point:
    """Ein markierter Punkt mit Beschriftung, z. B. Hochpunkt H(−1|2)."""

    x: float
    y: float
    label: str = ""
    # Versatz der Beschriftung in Punkten (damit sie die Kurve nicht überdeckt)
    dx: float = 8.0
    dy: float = 8.0
    color: str = _AXIS_COLOR


@dataclass
class Plot:
    """Deklaration eines vollständigen Plots. Ein Plot = eine Deklaration."""

    name: str  # Dateiname ohne .svg
    curves: Sequence[Curve]
    xlim: tuple[float, float]
    ylim: tuple[float, float]
    points: Sequence[Point] = field(default_factory=tuple)
    xlabel: str = "x"
    ylabel: str = "f(x)"
    xtick_step: float = 1.0
    ytick_step: float = 1.0
    legend_loc: str = "upper left"
    figsize: tuple[float, float] = (8.0, 6.0)  # 4:3
    samples: int = 600
    # Zahlengerade: nur x-Achse, keine y-Achse/-Beschriftung, flaches Format
    numberline: bool = False
    # Fluchtluke für Sonderelemente (Schraffuren, Hilfslinien …):
    extras: Callable | None = None


def _setup_numberline(ax, spec: Plot) -> None:
    """Zahlengerade: nur die x-Achse mit Pfeilspitze und ganzzahligen Ticks."""
    xmin, xmax = spec.xlim
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-1, 1)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_position("zero")
    ax.spines["bottom"].set_color(_AXIS_COLOR)
    ax.spines["bottom"].set_linewidth(1.2)
    ax.plot(1, 0, ">", color=_AXIS_COLOR, transform=ax.get_yaxis_transform(),
            clip_on=False, markersize=8)
    ax.annotate(spec.xlabel, xy=(1, 0), xycoords=ax.get_yaxis_transform(),
                xytext=(4, 10), textcoords="offset points",
                fontsize=_BASE_FONTSIZE, style="italic", ha="left", va="bottom")
    ax.xaxis.set_major_locator(MultipleLocator(spec.xtick_step))
    ax.tick_params(labelsize=_BASE_FONTSIZE - 1, length=6, color=_AXIS_COLOR)
    ax.xaxis.set_major_formatter(lambda v, _pos: fmt_de(v))
    ax.yaxis.set_visible(False)


def _setup_axes(ax, spec: Plot) -> None:
    """Achsenkreuz durch den Ursprung mit Pfeilspitzen, Gitter, ganzzahlige Ticks."""
    xmin, xmax = spec.xlim
    ymin, ymax = spec.ylim
    # Der Ursprung muss sichtbar sein, sonst gibt es kein Achsenkreuz.
    assert xmin < 0 < xmax or xmin == 0, f"{spec.name}: xlim muss 0 enthalten"
    assert ymin < 0 < ymax or ymin == 0, f"{spec.name}: ylim muss 0 enthalten"

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    ax.grid(True, linewidth=0.6, color=_GRID_COLOR, zorder=0)
    ax.set_axisbelow(True)

    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_position("zero")
        ax.spines[side].set_color(_AXIS_COLOR)
        ax.spines[side].set_linewidth(1.2)
        ax.spines[side].set_zorder(3)

    # Pfeilspitzen an den Achsenenden
    ax.plot(1, 0, ">", color=_AXIS_COLOR, transform=ax.get_yaxis_transform(),
            clip_on=False, markersize=8, zorder=3)
    ax.plot(0, 1, "^", color=_AXIS_COLOR, transform=ax.get_xaxis_transform(),
            clip_on=False, markersize=8, zorder=3)

    # Achsenbeschriftung an den Pfeilspitzen
    ax.annotate(spec.xlabel, xy=(1, 0), xycoords=ax.get_yaxis_transform(),
                xytext=(4, 10), textcoords="offset points",
                fontsize=_BASE_FONTSIZE, style="italic", ha="left", va="bottom")
    ax.annotate(spec.ylabel, xy=(0, 1), xycoords=ax.get_xaxis_transform(),
                xytext=(10, 2), textcoords="offset points",
                fontsize=_BASE_FONTSIZE, style="italic", ha="left", va="top")

    # Ticks an ganzen Zahlen (bzw. im angegebenen Raster), ohne die 0
    ax.xaxis.set_major_locator(MultipleLocator(spec.xtick_step))
    ax.yaxis.set_major_locator(MultipleLocator(spec.ytick_step))
    ax.tick_params(labelsize=_BASE_FONTSIZE - 1, length=4, color=_AXIS_COLOR)
    fmt = lambda v, _pos: "" if v == 0 else fmt_de(v)
    ax.xaxis.set_major_formatter(fmt)
    ax.yaxis.set_major_formatter(fmt)


def render(spec: Plot, out_path: str) -> None:
    """Rendert einen deklarierten Plot als deterministisches SVG."""
    figsize = (spec.figsize[0], 1.8) if spec.numberline else spec.figsize
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    if spec.numberline:
        _setup_numberline(ax, spec)
    else:
        _setup_axes(ax, spec)

    ymin, ymax = spec.ylim
    yspan = ymax - ymin
    for curve in spec.curves:
        dom = curve.domain or spec.xlim
        x = np.linspace(dom[0], dom[1], spec.samples)
        with np.errstate(all="ignore"):
            y = curve.fn(x)
        y = np.asarray(y, dtype=float)
        # Polstellen/Ausreißer nicht als senkrechte Striche zeichnen
        y[(y < ymin - 2 * yspan) | (y > ymax + 2 * yspan)] = np.nan
        ax.plot(x, y, color=curve.color, linestyle=curve.linestyle,
                linewidth=curve.linewidth, label=curve.label,
                zorder=2, clip_on=True, solid_capstyle="round")

    for p in spec.points:
        ax.plot(p.x, p.y, "o", color=p.color, markersize=7, zorder=4)
        if p.label:
            ax.annotate(p.label, xy=(p.x, p.y), xycoords="data",
                        xytext=(p.dx, p.dy), textcoords="offset points",
                        fontsize=_BASE_FONTSIZE, zorder=4)

    if spec.extras:
        spec.extras(ax)

    # Legende, sobald mindestens zwei Kurven beschriftet sind
    labeled = [c for c in spec.curves if c.label]
    if len(labeled) >= 2:
        leg = ax.legend(loc=spec.legend_loc, fontsize=_BASE_FONTSIZE - 1,
                        framealpha=0.95, edgecolor=_GRID_COLOR)
        leg.set_zorder(5)

    fig.savefig(
        out_path,
        format="svg",
        facecolor="white",
        transparent=False,
        bbox_inches="tight",
        pad_inches=0.15,
        metadata={"Date": None, "Creator": None},
    )
    plt.close(fig)
