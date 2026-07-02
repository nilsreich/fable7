"""Plots für funktionen/funktionsbegriff."""

import numpy as np

from plotstyle import COLOR_F, COLOR_TANGENTE, Curve, Plot, Point, punkt

PAGE = "funktionen/funktionsbegriff"


def _hilfslinien_ablesen(ax):
    """Gestrichelte Ablese-Hilfslinien zu f(3) = 2,5."""
    ax.plot([3, 3], [0, 2.5], "--", color="#888888", linewidth=1.4, zorder=1)
    ax.plot([0, 3], [2.5, 2.5], "--", color="#888888", linewidth=1.4, zorder=1)


def _kreis(ax):
    """Kreis x² + y² = 9 plus Senkrechten-Test bei x = 1,5."""
    ax.set_aspect("equal")
    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(3 * np.cos(t), 3 * np.sin(t), color=COLOR_F, linewidth=2.4,
            zorder=2, label=None)
    y = float(np.sqrt(9 - 1.5**2))
    ax.plot([1.5, 1.5], [-3.8, 3.8], "--", color=COLOR_TANGENTE,
            linewidth=1.8, zorder=2)
    ax.plot([1.5, 1.5], [y, -y], "o", color="#1a1a1a", markersize=7, zorder=4)


PLOTS = [
    # Tagesverlauf der Temperatur: Kontextgraph
    Plot(
        name="temperatur-tagesverlauf",
        curves=[
            Curve(lambda t: -0.05 * (t - 14) ** 2 + 9, domain=(0, 24)),
        ],
        xlim=(-2, 26),
        ylim=(-4, 11),
        xlabel="t in h",
        ylabel="T(t) in °C",
        xtick_step=4,
        ytick_step=2,
        points=[Point(14, 9, punkt("H", 14, 9), dx=-20, dy=10)],
    ),
    # Funktionswert am Graphen ablesen: f(3) = 2,5
    Plot(
        name="funktionswert-ablesen",
        curves=[
            Curve(lambda x: 0.5 * x**2 - 2, label=r"$f(x)=0{,}5x^2-2$"),
        ],
        xlim=(-4, 4),
        ylim=(-3, 7),
        points=[Point(3, 2.5, punkt("P", 3, 2.5), dx=-72, dy=6)],
        extras=_hilfslinien_ablesen,
    ),
    # Kreis: kein Funktionsgraph (Senkrechten-Test schlägt fehl)
    Plot(
        name="senkrechten-test",
        curves=[],
        xlim=(-4, 4),
        ylim=(-4, 4),
        ylabel="y",
        extras=_kreis,
    ),
    # Wurzelfunktion mit eingeschränktem Definitionsbereich
    Plot(
        name="wurzel-definitionsbereich",
        curves=[
            Curve(lambda x: np.sqrt(np.clip(x, 0, None)),
                  label=r"$f(x)=\sqrt{x}$", domain=(0, 9)),
        ],
        xlim=(-1, 10),
        ylim=(-1, 4),
        points=[
            Point(0, 0, "", dx=0, dy=0),
            Point(9, 3, punkt("Q", 9, 3), dx=-30, dy=10),
        ],
    ),
]
