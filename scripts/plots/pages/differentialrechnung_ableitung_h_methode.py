"""Plots für differentialrechnung/ableitung-h-methode."""

from plotstyle import COLOR_F, COLOR_F1, COLOR_TANGENTE, Curve, Plot, Point, punkt

PAGE = "differentialrechnung/ableitung-h-methode"


def _tangentenstuecke(ax):
    """Kurze Tangentenabschnitte an f(x) = x² bei x = −2, −1, 0, 1, 2."""
    for x0 in (-2, -1, 0, 1, 2):
        m = 2 * x0
        y0 = x0**2
        dx = 0.45
        ax.plot([x0 - dx, x0 + dx], [y0 - m * dx, y0 + m * dx],
                color="#ff7f0e", linewidth=2.4, zorder=3, solid_capstyle="round")
        ax.plot(x0, y0, "o", color="#1a1a1a", markersize=5, zorder=4)
        ax.annotate(f"m = {m}".replace("-", "−"), xy=(x0, y0),
                    xytext=(6, -16 if x0 < 0 else 10), textcoords="offset points",
                    fontsize=13)


PLOTS = [
    # Tangente an der Normalparabel im Punkt P(1|1)
    Plot(
        name="tangente-parabel",
        curves=[
            Curve(lambda x: x**2, label=r"$f(x)=x^2$"),
            Curve(lambda x: 2 * x - 1, domain=(-0.6, 2.8),
                  label=r"Tangente: $y=2x-1$", color=COLOR_TANGENTE),
        ],
        xlim=(-3, 3),
        ylim=(-3, 8),
        points=[Point(1, 1, punkt("P", 1, 1), dx=-58, dy=2)],
        legend_loc="upper left",
    ),
    # Tangentensteigungen an mehreren Stellen → Muster erkennen
    Plot(
        name="tangentensteigungen",
        curves=[
            Curve(lambda x: x**2, label=r"$f(x)=x^2$"),
        ],
        xlim=(-3.2, 3.2),
        ylim=(-2, 8),
        legend_loc="upper center",
        extras=_tangentenstuecke,
    ),
    # Funktion und Ableitungsfunktion
    Plot(
        name="ableitungsfunktion",
        curves=[
            Curve(lambda x: x**2, label=r"$f(x)=x^2$", color=COLOR_F),
            Curve(lambda x: 2 * x, label=r"$f'(x)=2x$", color=COLOR_F1),
        ],
        xlim=(-3, 3),
        ylim=(-6, 8),
        legend_loc="upper left",
    ),
]
