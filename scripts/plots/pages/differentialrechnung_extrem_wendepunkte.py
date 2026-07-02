"""Plots für differentialrechnung/extrem-wendepunkte."""

from plotstyle import COLOR_F, COLOR_F1, COLOR_F2, Curve, Plot, Point, punkt

PAGE = "differentialrechnung/extrem-wendepunkte"

PLOTS = [
    # Hoch- und Tiefpunkt
    Plot(
        name="extrempunkte",
        curves=[Curve(lambda x: x**3 - 3 * x, label=r"$f(x)=x^3-3x$")],
        xlim=(-3, 3),
        ylim=(-4, 4),
        points=[
            Point(-1, 2, punkt("H", -1, 2), dx=-64, dy=4),
            Point(1, -2, punkt("T", 1, -2), dx=8, dy=-18),
        ],
        legend_loc="upper left",
    ),
    # Sattelpunkt: notwendige Bedingung erfüllt, kein Extremum
    Plot(
        name="sattelpunkt",
        curves=[Curve(lambda x: x**3, label=r"$f(x)=x^3$")],
        xlim=(-2, 2),
        ylim=(-4, 4),
        points=[Point(0, 0, punkt("S", 0, 0) + " (Sattelpunkt)", dx=10, dy=-6)],
        legend_loc="upper left",
    ),
    # Vollbild: Extrema und Wendepunkt einer kubischen Funktion
    Plot(
        name="wendepunkt",
        curves=[Curve(lambda x: x**3 - 6 * x**2 + 9 * x, label=r"$f(x)=x^3-6x^2+9x$")],
        xlim=(-1, 5),
        ylim=(-3, 6),
        points=[
            Point(1, 4, punkt("H", 1, 4), dx=-24, dy=10),
            Point(3, 0, punkt("T", 3, 0), dx=8, dy=-20),
            Point(2, 2, punkt("W", 2, 2), dx=10, dy=2),
        ],
        legend_loc="lower right",
    ),
    # f, f' und f'' im selben Bild
    Plot(
        name="f-fstrich-fzweistrich",
        curves=[
            Curve(lambda x: x**3 - 3 * x, label=r"$f(x)=x^3-3x$", color=COLOR_F),
            Curve(lambda x: 3 * x**2 - 3, label=r"$f'(x)=3x^2-3$", color=COLOR_F1),
            Curve(lambda x: 6 * x, label=r"$f''(x)=6x$", color=COLOR_F2),
        ],
        xlim=(-3, 3),
        ylim=(-6, 8),
        legend_loc="upper left",
    ),
    # Kontext: Laktatkurve beim Belastungstest
    Plot(
        name="laktatkurve",
        curves=[
            Curve(lambda t: 6 * t**2 - t**3, domain=(0, 6),
                  label=r"$L(t)=6t^2-t^3$"),
        ],
        xlim=(-1, 7),
        ylim=(-5, 38),
        xlabel="t in min",
        ylabel="L(t)",
        ytick_step=5,
        points=[
            Point(4, 32, punkt("H", 4, 32), dx=-20, dy=10),
            Point(2, 16, punkt("W", 2, 16), dx=-46, dy=8),
        ],
        legend_loc="lower right",
    ),
]
