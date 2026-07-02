"""Plots für differentialrechnung/tangente-normale."""

from plotstyle import COLOR_F, COLOR_TANGENTE, Curve, Plot, Point, punkt

PAGE = "differentialrechnung/tangente-normale"

PLOTS = [
    # Tangente an einer Parabel
    Plot(
        name="tangente",
        curves=[
            Curve(lambda x: 0.5 * x**2 + 1, label=r"$f(x)=0{,}5x^2+1$", color=COLOR_F),
            Curve(lambda x: 2 * x - 1, domain=(-0.4, 4.2),
                  label=r"Tangente $y=2x-1$", color=COLOR_TANGENTE),
        ],
        xlim=(-3, 5),
        ylim=(-2, 9),
        points=[Point(2, 3, punkt("B", 2, 3), dx=-58, dy=4)],
        legend_loc="upper left",
    ),
    # Tangente und Normale im selben Punkt
    Plot(
        name="tangente-und-normale",
        curves=[
            Curve(lambda x: 0.5 * x**2 + 1, label=r"$f(x)=0{,}5x^2+1$", color=COLOR_F),
            Curve(lambda x: 2 * x - 1, domain=(-0.4, 4.2),
                  label="Tangente", color=COLOR_TANGENTE),
            Curve(lambda x: -0.5 * x + 4, domain=(-2.5, 4.5),
                  label="Normale", color=COLOR_TANGENTE, linestyle="--"),
        ],
        xlim=(-3, 5),
        ylim=(-2, 9),
        points=[Point(2, 3, punkt("B", 2, 3), dx=10, dy=-18)],
        legend_loc="upper left",
    ),
    # Tangente an einer kubischen Funktion
    Plot(
        name="tangente-kubik",
        curves=[
            Curve(lambda x: x**3 - 3 * x, label=r"$f(x)=x^3-3x$", color=COLOR_F),
            Curve(lambda x: 9 * x - 16, domain=(1.2, 2.7),
                  label=r"Tangente $y=9x-16$", color=COLOR_TANGENTE),
        ],
        xlim=(-3, 3),
        ylim=(-6, 8),
        points=[Point(2, 2, punkt("B", 2, 2), dx=-60, dy=6)],
        legend_loc="upper left",
    ),
    # Anwendung: Gefälle einer Skaterrampe
    Plot(
        name="rampe",
        curves=[
            Curve(lambda x: -0.25 * x**2 + 4, domain=(-4, 4),
                  label=r"$h(x)=-0{,}25x^2+4$", color=COLOR_F),
            Curve(lambda x: -x + 5, domain=(0.5, 4.5),
                  label=r"Tangente $y=-x+5$", color=COLOR_TANGENTE),
        ],
        xlim=(-5, 6),
        ylim=(-1, 6),
        xlabel="x in m",
        ylabel="h(x) in m",
        points=[Point(2, 3, punkt("B", 2, 3), dx=10, dy=6)],
        legend_loc="lower left",
    ),
]
