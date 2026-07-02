"""Plots für ganzrationale/nullstellen."""

from plotstyle import Curve, Plot, Point, punkt

PAGE = "ganzrationale/nullstellen"

PLOTS = [
    # Beispiel Polynomdivision: drei einfache Nullstellen
    Plot(
        name="kubisch-drei-nullstellen",
        curves=[
            Curve(lambda x: x**3 - 2 * x**2 - 5 * x + 6,
                  label=r"$f(x)=x^3-2x^2-5x+6$"),
        ],
        xlim=(-3, 4),
        ylim=(-7, 9),
        ytick_step=2,
        points=[
            Point(-2, 0, r"$N_1$", dx=-26, dy=8),
            Point(1, 0, r"$N_2$", dx=-8, dy=10),
            Point(3, 0, r"$N_3$", dx=10, dy=6),
        ],
        legend_loc="lower right",
    ),
    # Beispiel Substitution: biquadratische Funktion
    Plot(
        name="biquadratisch",
        curves=[
            Curve(lambda x: x**4 - 5 * x**2 + 4, label=r"$f(x)=x^4-5x^2+4$"),
        ],
        xlim=(-3, 3),
        ylim=(-3, 6),
        points=[
            Point(-2, 0, r"$N_1$", dx=-26, dy=8),
            Point(-1, 0, r"$N_2$", dx=-12, dy=-24),
            Point(1, 0, r"$N_3$", dx=2, dy=-24),
            Point(2, 0, r"$N_4$", dx=12, dy=8),
        ],
    ),
    # Ausklammern: doppelte Nullstelle berührt die Achse
    Plot(
        name="doppelte-nullstelle",
        curves=[
            Curve(lambda x: x**3 - 4 * x**2 + 4 * x, label=r"$f(x)=x^3-4x^2+4x$"),
        ],
        xlim=(-1, 4),
        ylim=(-2, 4),
        points=[
            Point(0, 0, r"$N_1$", dx=-24, dy=8),
            Point(2, 0, punkt("N", 2, 0) + " (doppelt)", dx=8, dy=-20),
        ],
    ),
    # Kombination: x² ausklammern, dann 3. binomische Formel
    Plot(
        name="ausklammern-x-quadrat",
        curves=[
            Curve(lambda x: x**4 - 4 * x**2, label=r"$f(x)=x^4-4x^2$"),
        ],
        xlim=(-3, 3),
        ylim=(-5, 6),
        points=[
            Point(-2, 0, r"$N_1$", dx=-26, dy=8),
            Point(0, 0, punkt("N", 0, 0) + " (doppelt)", dx=-36, dy=-26),
            Point(2, 0, r"$N_3$", dx=12, dy=8),
        ],
    ),
]
