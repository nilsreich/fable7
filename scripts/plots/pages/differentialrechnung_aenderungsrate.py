"""Plots für differentialrechnung/aenderungsrate."""

from plotstyle import COLOR_F, COLOR_TANGENTE, Curve, Plot, Point, punkt

PAGE = "differentialrechnung/aenderungsrate"


def _dreieck(ax):
    """Steigungsdreieck (Δt, Δs) an der Sekante."""
    ax.plot([1, 3], [1.5, 1.5], "--", color="#888888", linewidth=1.4, zorder=1)
    ax.plot([3, 3], [1.5, 5.5], "--", color="#888888", linewidth=1.4, zorder=1)
    ax.annotate(r"$\Delta x = 2$", xy=(2, 1.5), xytext=(0, -20),
                textcoords="offset points", ha="center", fontsize=14)
    ax.annotate(r"$\Delta y = 4$", xy=(3, 3.5), xytext=(8, -4),
                textcoords="offset points", fontsize=14)


PLOTS = [
    # Usain-Bolt-Modell: Weg-Zeit-Funktion mit Sekante
    Plot(
        name="bolt-weg-zeit",
        curves=[
            Curve(lambda t: 1.5 * t**2, domain=(0, 5), label=r"$s(t)=1{,}5t^2$"),
            Curve(lambda t: 6 * t - 4.5, domain=(0.4, 4.2),
                  label="Sekante", color=COLOR_TANGENTE),
        ],
        xlim=(-1, 6),
        ylim=(-5, 40),
        xlabel="t in s",
        ylabel="s(t) in m",
        ytick_step=5,
        points=[
            Point(1, 1.5, punkt("P", 1, 1.5), dx=-66, dy=4),
            Point(3, 13.5, punkt("Q", 3, 13.5), dx=-78, dy=4),
        ],
        legend_loc="upper left",
    ),
    # Sekante und Tangente am selben Graphen
    Plot(
        name="sekante-tangente",
        curves=[
            Curve(lambda x: 0.5 * x**2, label=r"$f(x)=0{,}5x^2$"),
            Curve(lambda x: 2 * x - 1.5, domain=(0.2, 3.8),
                  label="Sekante durch P und Q", color=COLOR_TANGENTE),
            Curve(lambda x: 2 * x - 2, domain=(0.2, 3.8),
                  label="Tangente in x = 2", color=COLOR_TANGENTE, linestyle="--"),
        ],
        xlim=(-2, 4),
        ylim=(-3, 8),
        points=[
            Point(1, 0.5, r"$P$", dx=-18, dy=6),
            Point(3, 4.5, r"$Q$", dx=-18, dy=8),
            Point(2, 2, r"$B$", dx=8, dy=-16),
        ],
        legend_loc="upper left",
    ),
    # Sekantenschar: h wird immer kleiner
    Plot(
        name="sekanten-werden-tangente",
        curves=[
            Curve(lambda x: x**2, label=r"$f(x)=x^2$"),
            Curve(lambda x: 4 * x - 3, domain=(-0.2, 3.2),
                  label=r"Sekante $h=2$", color="#ffc078"),
            Curve(lambda x: 3 * x - 2, domain=(-0.4, 3.2),
                  label=r"Sekante $h=1$", color="#ffa94d"),
            Curve(lambda x: 2.5 * x - 1.5, domain=(-0.6, 3.2),
                  label=r"Sekante $h=0{,}5$", color="#fd7e14"),
            Curve(lambda x: 2 * x - 1, domain=(-0.8, 3.2),
                  label="Tangente in P", color="#d9480f", linewidth=2.6),
        ],
        xlim=(-2, 4),
        ylim=(-3, 9),
        points=[Point(1, 1, punkt("P", 1, 1), dx=-60, dy=0)],
        legend_loc="upper left",
    ),
    # Differenzenquotient als Steigungsdreieck
    Plot(
        name="differenzenquotient-dreieck",
        curves=[
            Curve(lambda x: 0.5 * x**2 + 1, label=r"$f(x)=0{,}5x^2+1$"),
            Curve(lambda x: 2 * x - 0.5, domain=(0.2, 3.8),
                  label="Sekante", color=COLOR_TANGENTE),
        ],
        xlim=(-2, 4),
        ylim=(-2, 8),
        points=[
            Point(1, 1.5, punkt("P", 1, 1.5), dx=-76, dy=0),
            Point(3, 5.5, punkt("Q", 3, 5.5), dx=-78, dy=2),
        ],
        legend_loc="upper left",
        extras=_dreieck,
    ),
]
