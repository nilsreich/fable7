"""Plots für funktionen/lineare-quadratische."""

from plotstyle import COLOR_F, COLOR_F1, COLOR_F2, COLOR_ORT, COLOR_TANGENTE, Curve, Plot, Point, punkt

PAGE = "funktionen/lineare-quadratische"


def _steigungsdreieck(ax):
    """Steigungsdreieck an g(x) = 0,5x + 1 zwischen x = 1 und x = 3."""
    ax.plot([1, 3], [1.5, 1.5], color="#555555", linewidth=1.6, zorder=3)
    ax.plot([3, 3], [1.5, 2.5], color="#555555", linewidth=1.6, zorder=3)
    ax.annotate("2", xy=(2, 1.5), xytext=(0, -18), textcoords="offset points",
                ha="center", fontsize=14)
    ax.annotate("1", xy=(3, 2.0), xytext=(8, -4), textcoords="offset points",
                fontsize=14)


PLOTS = [
    # Gerade mit Steigungsdreieck und y-Achsenabschnitt
    Plot(
        name="gerade-steigungsdreieck",
        curves=[Curve(lambda x: 0.5 * x + 1, label=r"$g(x)=0{,}5x+1$")],
        xlim=(-4, 5),
        ylim=(-2, 4),
        points=[Point(0, 1, punkt("B", 0, 1), dx=-46, dy=6)],
        extras=_steigungsdreieck,
    ),
    # Drei Geraden im Vergleich: Steigung positiv / negativ / null
    Plot(
        name="geraden-vergleich",
        curves=[
            Curve(lambda x: 2 * x - 1, label=r"$f(x)=2x-1$", color=COLOR_F),
            Curve(lambda x: -0.5 * x + 2, label=r"$g(x)=-0{,}5x+2$", color=COLOR_TANGENTE),
            Curve(lambda x: 0 * x + 2, label=r"$h(x)=2$", color=COLOR_ORT),
        ],
        xlim=(-4, 4),
        ylim=(-4, 4),
        legend_loc="lower right",
    ),
    # Scheitelform: verschobene Parabel neben der Normalparabel
    Plot(
        name="parabel-scheitelform",
        curves=[
            Curve(lambda x: x**2, label=r"$y=x^2$", color="#9e9e9e", linestyle="--", linewidth=1.8),
            Curve(lambda x: (x - 2) ** 2 - 1, label=r"$f(x)=(x-2)^2-1$", color=COLOR_F),
        ],
        xlim=(-3, 5),
        ylim=(-2, 6),
        points=[Point(2, -1, punkt("S", 2, -1), dx=6, dy=-18)],
    ),
    # Öffnung und Streckung: Formfaktor a
    Plot(
        name="parabel-oeffnung",
        curves=[
            Curve(lambda x: x**2, label=r"$y=x^2$", color=COLOR_F),
            Curve(lambda x: 2 * x**2, label=r"$y=2x^2$", color=COLOR_F1),
            Curve(lambda x: 0.5 * x**2, label=r"$y=0{,}5x^2$", color=COLOR_F2),
            Curve(lambda x: -(x**2), label=r"$y=-x^2$", color=COLOR_ORT),
        ],
        xlim=(-3, 3),
        ylim=(-4, 5),
        legend_loc="lower left",
    ),
    # Nullstellen einer quadratischen Funktion
    Plot(
        name="parabel-nullstellen",
        curves=[Curve(lambda x: x**2 - x - 6, label=r"$f(x)=x^2-x-6$")],
        xlim=(-4, 5),
        ylim=(-7, 6),
        points=[
            Point(-2, 0, r"$N_1$", dx=-26, dy=8),
            Point(3, 0, r"$N_2$", dx=10, dy=8),
            Point(0.5, -6.25, punkt("S", 0.5, -6.25), dx=8, dy=-4),
        ],
    ),
]
