"""Plots für extremwertprobleme/extremwertprobleme."""

import numpy as np

from plotstyle import COLOR_F, COLOR_TANGENTE, Curve, Plot, Point, punkt

PAGE = "extremwertprobleme/extremwertprobleme"


def _rechteck(ax):
    """Einbeschriebenes Rechteck unter der Parabel y = 3 − x² (x = 1)."""
    ax.plot([-1, 1, 1, -1, -1], [0, 0, 2, 2, 0], color=COLOR_TANGENTE,
            linewidth=2.2, zorder=3)
    ax.annotate("2x", xy=(0, 0), xytext=(0, -20), textcoords="offset points",
                ha="center", fontsize=14)
    ax.annotate("f(x)", xy=(1, 1), xytext=(8, -4), textcoords="offset points",
                fontsize=14)


PLOTS = [
    # Zielfunktion des Zahlenpaar-Problems
    Plot(
        name="produkt-maximal",
        curves=[Curve(lambda x: x * (20 - x), domain=(0, 20),
                      label=r"$P(x)=x(20-x)$")],
        xlim=(-2, 22),
        ylim=(-15, 115),
        xtick_step=2,
        ytick_step=20,
        points=[Point(10, 100, punkt("H", 10, 100), dx=-24, dy=10)],
        legend_loc="lower right",
    ),
    # Schachtelproblem
    Plot(
        name="schachtel-volumen",
        curves=[Curve(lambda x: x * (12 - 2 * x) ** 2, domain=(0, 6),
                      label=r"$V(x)=x(12-2x)^2$")],
        xlim=(-1, 7),
        ylim=(-15, 145),
        ytick_step=20,
        xlabel="x in cm",
        ylabel="V(x) in cm³",
        points=[Point(2, 128, punkt("H", 2, 128), dx=8, dy=6)],
        legend_loc="upper right",
    ),
    # Dosenproblem: Oberfläche in Abhängigkeit vom Radius
    Plot(
        name="dose-oberflaeche",
        curves=[Curve(lambda r: 2 * np.pi * r**2 + 2000 / r, domain=(1.2, 12),
                      label=r"$O(r)=2\pi r^2+\frac{2000}{r}$")],
        xlim=(-1, 13),
        ylim=(-100, 1300),
        ytick_step=200,
        xlabel="r in cm",
        ylabel="O(r) in cm²",
        points=[Point(5.42, 553.7, punkt("T", 5.42, 553.7), dx=-20, dy=-24)],
        legend_loc="upper right",
    ),
    # Einbeschriebenes Rechteck unter einer Parabel
    Plot(
        name="rechteck-unter-parabel",
        curves=[Curve(lambda x: 3 - x**2, label=r"$f(x)=3-x^2$")],
        xlim=(-2.5, 2.5),
        ylim=(-1, 4),
        legend_loc="lower left",
        extras=_rechteck,
    ),
    # Zaunproblem am Fluss
    Plot(
        name="zaun-flaeche",
        curves=[Curve(lambda x: x * (100 - 2 * x), domain=(0, 50),
                      label=r"$A(x)=x(100-2x)$")],
        xlim=(-5, 55),
        ylim=(-150, 1400),
        xtick_step=5,
        ytick_step=200,
        xlabel="x in m",
        ylabel="A(x) in m²",
        points=[Point(25, 1250, punkt("H", 25, 1250), dx=-24, dy=10)],
        legend_loc="lower right",
    ),
    # Dosis-Wirkungs-Kurve
    Plot(
        name="dosis-wirkung",
        curves=[Curve(lambda d: 6 * d**2 - d**3, domain=(0, 6),
                      label=r"$W(d)=6d^2-d^3$")],
        xlim=(-1, 7),
        ylim=(-5, 38),
        ytick_step=5,
        xlabel="d (Dosiseinheiten)",
        ylabel="W(d)",
        points=[Point(4, 32, punkt("H", 4, 32), dx=-20, dy=10)],
        legend_loc="lower right",
    ),
]
