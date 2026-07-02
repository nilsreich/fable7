"""Zwei Demo-Plots, die den Stil-Leitfaden belegen (Phase 0, Gate 0).

1. Einzelkurve: Parabel mit markierten Nullstellen und Scheitelpunkt.
2. Mehrfachkurve: f und f' mit Legende sowie beschriftetem Hoch- und Tiefpunkt.
"""

from plotstyle import COLOR_F, COLOR_F1, Curve, Plot, Point, punkt

PAGE = "demo"

PLOTS = [
    # f(x) = x² − 2x − 3 = (x + 1)(x − 3): Nullstellen −1 und 3, Scheitel S(1|−4)
    Plot(
        name="parabel-nullstellen",
        curves=[
            Curve(lambda x: x**2 - 2 * x - 3, label=r"$f(x)=x^2-2x-3$"),
        ],
        xlim=(-3, 5),
        ylim=(-5, 6),
        points=[
            Point(-1, 0, r"$N_1$", dx=-26, dy=8),
            Point(3, 0, r"$N_2$", dx=10, dy=8),
            Point(1, -4, punkt("S", 1, -4), dx=10, dy=-6),
        ],
    ),
    # f(x) = x³ − 3x mit Ableitung f'(x) = 3x² − 3; H(−1|2), T(1|−2)
    Plot(
        name="kubik-mit-ableitung",
        curves=[
            Curve(lambda x: x**3 - 3 * x, label=r"$f(x)=x^3-3x$", color=COLOR_F),
            Curve(lambda x: 3 * x**2 - 3, label=r"$f'(x)=3x^2-3$", color=COLOR_F1),
        ],
        xlim=(-3, 3),
        ylim=(-5, 7),
        points=[
            Point(-1, 2, punkt("H", -1, 2), dx=-60, dy=10),
            Point(1, -2, punkt("T", 1, -2), dx=8, dy=-18),
        ],
    ),
]
