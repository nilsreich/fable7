"""Plots für differentialrechnung/ableitungsregeln."""

from plotstyle import COLOR_F, COLOR_F1, Curve, Plot, Point, punkt

PAGE = "differentialrechnung/ableitungsregeln"

PLOTS = [
    # Parabel und ihre (lineare) Ableitung
    Plot(
        name="parabel-und-ableitung",
        curves=[
            Curve(lambda x: x**2 - 4 * x + 3, label=r"$f(x)=x^2-4x+3$", color=COLOR_F),
            Curve(lambda x: 2 * x - 4, label=r"$f'(x)=2x-4$", color=COLOR_F1),
        ],
        xlim=(-2, 6),
        ylim=(-6, 8),
        points=[Point(2, -1, punkt("S", 2, -1), dx=6, dy=-18)],
        legend_loc="upper center",
    ),
    # Kubische Funktion und Ableitung: waagerechte Tangenten sichtbar
    Plot(
        name="kubisch-und-ableitung",
        curves=[
            Curve(lambda x: x**3 - 3 * x, label=r"$f(x)=x^3-3x$", color=COLOR_F),
            Curve(lambda x: 3 * x**2 - 3, label=r"$f'(x)=3x^2-3$", color=COLOR_F1),
        ],
        xlim=(-3, 3),
        ylim=(-5, 7),
        points=[
            Point(-1, 2, punkt("H", -1, 2), dx=-62, dy=8),
            Point(1, -2, punkt("T", 1, -2), dx=8, dy=-18),
        ],
        legend_loc="upper left",
    ),
]
