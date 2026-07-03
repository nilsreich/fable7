"""Plots für steckbriefaufgaben/steckbriefaufgaben."""

from plotstyle import Curve, Plot, Point, punkt

PAGE = "steckbriefaufgaben/steckbriefaufgaben"

PLOTS = [
    # Parabel durch drei Punkte
    Plot(
        name="parabel-durch-punkte",
        curves=[Curve(lambda x: 2 * x**2 - 3 * x + 1, label=r"$f(x)=2x^2-3x+1$")],
        xlim=(-2, 3),
        ylim=(-2, 6),
        points=[
            Point(0, 1, punkt("A", 0, 1), dx=-58, dy=0),
            Point(1, 0, punkt("B", 1, 0), dx=8, dy=-20),
            Point(2, 3, punkt("C", 2, 3), dx=10, dy=-4),
        ],
        legend_loc="upper left",
    ),
    # Punktsymmetrische kubische Funktion aus zwei Bedingungen
    Plot(
        name="kubisch-punktsymmetrisch",
        curves=[Curve(lambda x: x**3 - 3 * x, label=r"$f(x)=x^3-3x$")],
        xlim=(-3, 3),
        ylim=(-4, 4),
        points=[Point(1, -2, punkt("T", 1, -2), dx=8, dy=-20)],
        legend_loc="upper left",
    ),
    # Kubische Funktion mit Wendepunkt-Bedingung
    Plot(
        name="kubisch-wendepunkt",
        curves=[Curve(lambda x: x**3 - 3 * x + 1, label=r"$f(x)=x^3-3x+1$")],
        xlim=(-3, 3),
        ylim=(-3, 5),
        points=[
            Point(-1, 3, punkt("H", -1, 3), dx=-24, dy=10),
            Point(0, 1, punkt("W", 0, 1), dx=10, dy=-2),
            Point(1, -1, punkt("T", 1, -1), dx=8, dy=-20),
        ],
        legend_loc="lower right",
    ),
    # Kontext: Krankenstand im Pflegeheim
    Plot(
        name="krankenstand",
        curves=[
            Curve(lambda t: t**3 / 8 - 1.5 * t**2 + 4.5 * t + 4, domain=(0, 8),
                  label=r"$K(t)=\frac{1}{8}t^3-\frac{3}{2}t^2+\frac{9}{2}t+4$"),
        ],
        xlim=(-1, 9),
        ylim=(-1, 10),
        xlabel="t in Monaten",
        ylabel="K(t) in %",
        points=[
            Point(2, 8, punkt("H", 2, 8), dx=8, dy=6),
            Point(6, 4, punkt("T", 6, 4), dx=6, dy=-20),
        ],
        legend_loc="lower right",
    ),
    # Aufgabe: Term aus dem Graphen rekonstruieren
    Plot(
        name="graph-rekonstruieren",
        curves=[Curve(lambda x: -0.5 * x**3 + 1.5 * x)],
        xlim=(-3, 3),
        ylim=(-3, 3),
        points=[
            Point(1, 1, punkt("H", 1, 1), dx=8, dy=8),
            Point(-1, -1, punkt("T", -1, -1), dx=-70, dy=-8),
            Point(0, 0, punkt("W", 0, 0), dx=8, dy=-18),
        ],
        ylabel="y",
    ),
]
