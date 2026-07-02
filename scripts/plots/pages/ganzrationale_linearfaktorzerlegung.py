"""Plots für ganzrationale/linearfaktorzerlegung."""

from plotstyle import Curve, Plot, Point, punkt

PAGE = "ganzrationale/linearfaktorzerlegung"

PLOTS = [
    # Einfache vs. doppelte Nullstelle
    Plot(
        name="vielfachheiten",
        curves=[
            Curve(lambda x: x**3 - 3 * x + 2,
                  label=r"$f(x)=(x+2)(x-1)^2$"),
        ],
        xlim=(-3, 3),
        ylim=(-3, 5),
        points=[
            Point(-2, 0, "einfach", dx=-30, dy=-24),
            Point(1, 0, "doppelt", dx=6, dy=-22),
        ],
        legend_loc="upper left",
    ),
    # Dreifache Nullstelle: Sattel-Durchgang
    Plot(
        name="dreifache-nullstelle",
        curves=[
            Curve(lambda x: (x - 1) ** 3, label=r"$f(x)=(x-1)^3$"),
        ],
        xlim=(-2, 4),
        ylim=(-4, 4),
        points=[Point(1, 0, "dreifach", dx=8, dy=10)],
        legend_loc="upper left",
    ),
    # Aufgabe: Term aus dem Graphen rekonstruieren
    Plot(
        name="term-aus-graph",
        curves=[
            Curve(lambda x: -0.5 * (x + 1) * (x - 2) ** 2),
        ],
        xlim=(-3, 4),
        ylim=(-5, 5),
        points=[
            Point(-1, 0, r"$N_1$", dx=-26, dy=8),
            Point(2, 0, r"$N_2$", dx=10, dy=8),
            Point(0, -2, punkt("P", 0, -2), dx=-70, dy=-8),
        ],
    ),
]
