"""Plots für funktionen/transformationen (Vorher-Nachher-Paare)."""

import numpy as np

from plotstyle import COLOR_F, COLOR_F1, COLOR_F2, Curve, Plot, Point, punkt

PAGE = "funktionen/transformationen"

_GRAU = "#9e9e9e"


def _asymptote(y):
    def extras(ax):
        ax.axhline(y, color="#777777", linestyle=":", linewidth=1.4, zorder=1)
    return extras


PLOTS = [
    # 1. Verschiebung in y-Richtung
    Plot(
        name="verschiebung-y",
        curves=[
            Curve(lambda x: x**2, label=r"$f(x)=x^2$", color=_GRAU, linestyle="--", linewidth=1.8),
            Curve(lambda x: x**2 + 2, label=r"$g(x)=x^2+2$", color=COLOR_F),
            Curve(lambda x: x**2 - 3, label=r"$h(x)=x^2-3$", color=COLOR_F2),
        ],
        xlim=(-3, 3),
        ylim=(-4, 7),
        legend_loc="lower right",
    ),
    # 2. Verschiebung in x-Richtung
    Plot(
        name="verschiebung-x",
        curves=[
            Curve(lambda x: x**2, label=r"$f(x)=x^2$", color=_GRAU, linestyle="--", linewidth=1.8),
            Curve(lambda x: (x - 3) ** 2, label=r"$g(x)=(x-3)^2$", color=COLOR_F),
        ],
        xlim=(-3, 6),
        ylim=(-2, 7),
        points=[Point(3, 0, punkt("S", 3, 0), dx=8, dy=8)],
        legend_loc="upper left",
    ),
    # 3. Streckung in y-Richtung
    Plot(
        name="streckung-y",
        curves=[
            Curve(lambda x: x**3 - 3 * x, label=r"$f(x)=x^3-3x$", color=_GRAU, linestyle="--", linewidth=1.8),
            Curve(lambda x: 2 * (x**3 - 3 * x), label=r"$g(x)=2\cdot f(x)$", color=COLOR_F),
            Curve(lambda x: 0.5 * (x**3 - 3 * x), label=r"$h(x)=0{,}5\cdot f(x)$", color=COLOR_F2),
        ],
        xlim=(-3, 3),
        ylim=(-5, 5),
        legend_loc="lower right",
    ),
    # 4. Spiegelung an der x-Achse
    Plot(
        name="spiegelung-x-achse",
        curves=[
            Curve(lambda x: (x - 1) ** 2, label=r"$f(x)=(x-1)^2$", color=COLOR_F),
            Curve(lambda x: -((x - 1) ** 2), label=r"$g(x)=-f(x)$", color=COLOR_F1),
        ],
        xlim=(-3, 5),
        ylim=(-5, 5),
        legend_loc="lower left",
    ),
    # 5. Spiegelung an der y-Achse
    Plot(
        name="spiegelung-y-achse",
        curves=[
            Curve(lambda x: np.sqrt(np.clip(x, 0, None)), label=r"$f(x)=\sqrt{x}$",
                  color=COLOR_F, domain=(0, 5)),
            Curve(lambda x: np.sqrt(np.clip(-x, 0, None)), label=r"$g(x)=f(-x)=\sqrt{-x}$",
                  color=COLOR_F1, domain=(-5, 0)),
        ],
        xlim=(-5, 5),
        ylim=(-1, 4),
        legend_loc="upper left",
    ),
    # 6. Streckung in x-Richtung
    Plot(
        name="streckung-x",
        curves=[
            Curve(lambda x: x**3 - 3 * x, label=r"$f(x)=x^3-3x$", color=_GRAU, linestyle="--", linewidth=1.8),
            Curve(lambda x: (2 * x) ** 3 - 3 * (2 * x), label=r"$g(x)=f(2x)$", color=COLOR_F),
        ],
        xlim=(-3, 3),
        ylim=(-4, 4),
        legend_loc="lower right",
    ),
    # 7. Kombination mehrerer Transformationen
    Plot(
        name="kombination",
        curves=[
            Curve(lambda x: x**2, label=r"$f(x)=x^2$", color=_GRAU, linestyle="--", linewidth=1.8),
            Curve(lambda x: 2 * (x - 1) ** 2 - 3, label=r"$g(x)=2(x-1)^2-3$", color=COLOR_F),
        ],
        xlim=(-3, 4),
        ylim=(-4, 7),
        points=[Point(1, -3, punkt("S", 1, -3), dx=8, dy=-16)],
        legend_loc="upper left",
    ),
    # 8. Verschobene Exponentialfunktion mit Asymptote
    Plot(
        name="exponential-verschoben",
        curves=[
            Curve(lambda x: 2.0**x, label=r"$f(x)=2^x$", color=_GRAU, linestyle="--", linewidth=1.8),
            Curve(lambda x: 2.0**x - 4, label=r"$g(x)=2^x-4$", color=COLOR_F),
        ],
        xlim=(-4, 4),
        ylim=(-6, 8),
        points=[Point(2, 0, punkt("N", 2, 0), dx=10, dy=6)],
        legend_loc="upper left",
        extras=_asymptote(-4),
    ),
]
