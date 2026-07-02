"""Plots für kurvendiskussion/vollstaendig."""

from plotstyle import Curve, Plot, Point, punkt

PAGE = "kurvendiskussion/vollstaendig"

PLOTS = [
    # Beispiel 1: kubische Musterdiskussion
    Plot(
        name="beispiel-kubisch",
        curves=[Curve(lambda x: x**3 - 3 * x**2, label=r"$f(x)=x^3-3x^2$")],
        xlim=(-2, 4),
        ylim=(-5, 4),
        points=[
            Point(0, 0, punkt("H", 0, 0), dx=-30, dy=10),
            Point(2, -4, punkt("T", 2, -4), dx=8, dy=-18),
            Point(1, -2, punkt("W", 1, -2), dx=10, dy=0),
            Point(3, 0, r"$N$", dx=10, dy=6),
        ],
        legend_loc="upper left",
    ),
    # Beispiel 2: symmetrische Funktion vierten Grades
    Plot(
        name="beispiel-quartisch",
        curves=[Curve(lambda x: 0.25 * x**4 - 2 * x**2, label=r"$f(x)=\frac{1}{4}x^4-2x^2$")],
        xlim=(-4, 4),
        ylim=(-5, 5),
        points=[
            Point(0, 0, punkt("H", 0, 0), dx=6, dy=8),
            Point(-2, -4, punkt("T", -2, -4), dx=-76, dy=0),
            Point(2, -4, punkt("T", 2, -4), dx=10, dy=0),
        ],
        legend_loc="upper center",
    ),
    # Beispiel 3: negativer Leitkoeffizient, doppelte Nullstelle
    Plot(
        name="beispiel-negativ",
        curves=[Curve(lambda x: -(x**3) + 3 * x + 2, label=r"$f(x)=-x^3+3x+2$")],
        xlim=(-3, 3),
        ylim=(-3, 6),
        points=[
            Point(-1, 0, punkt("T", -1, 0), dx=-56, dy=8),
            Point(1, 4, punkt("H", 1, 4), dx=-20, dy=10),
            Point(0, 2, punkt("W", 0, 2), dx=-52, dy=-6),
            Point(2, 0, r"$N$", dx=10, dy=6),
        ],
        legend_loc="lower left",
    ),
    # Beispiel 4: Fieberanstieg über der Grundtemperatur
    Plot(
        name="fieberanstieg",
        curves=[
            Curve(lambda t: -(t**3) / 40 + 9 * t**2 / 40, domain=(0, 9),
                  label=r"$E(t)=-\frac{1}{40}t^3+\frac{9}{40}t^2$"),
        ],
        xlim=(-1, 10),
        ylim=(-0.5, 3.5),
        xlabel="t in h",
        ylabel="E(t) in °C",
        ytick_step=0.5,
        points=[
            Point(6, 2.7, punkt("H", 6, 2.7), dx=-24, dy=10),
            Point(3, 1.35, punkt("W", 3, 1.35), dx=-70, dy=6),
        ],
        legend_loc="lower right",
    ),
    # Anwendung: Medikamentenkonzentration
    Plot(
        name="medikament",
        curves=[
            Curve(lambda t: 0.1 * t * (t - 12) ** 2, domain=(0, 12),
                  label=r"$K(t)=0{,}1t(t-12)^2$"),
        ],
        xlim=(-1, 14),
        ylim=(-4, 30),
        xlabel="t in h",
        ylabel="K(t) in mg/l",
        ytick_step=5,
        points=[
            Point(4, 25.6, punkt("H", 4, 25.6), dx=8, dy=6),
            Point(8, 12.8, punkt("W", 8, 12.8), dx=10, dy=4),
        ],
        legend_loc="upper right",
    ),
    # Zuordnungsaufgabe: vier Graphen ohne Term
    Plot(
        name="zuordnung-a",
        curves=[Curve(lambda x: x**3 - 3 * x)],
        xlim=(-3, 3), ylim=(-4, 4),
        ylabel="y",
    ),
    Plot(
        name="zuordnung-b",
        curves=[Curve(lambda x: -(x**3) + 3 * x)],
        xlim=(-3, 3), ylim=(-4, 4),
        ylabel="y",
    ),
    Plot(
        name="zuordnung-c",
        curves=[Curve(lambda x: x**4 - 2 * x**2)],
        xlim=(-2.5, 2.5), ylim=(-2, 4),
        ylabel="y",
    ),
    Plot(
        name="zuordnung-d",
        curves=[Curve(lambda x: x**3 + 1)],
        xlim=(-2.5, 2.5), ylim=(-3, 4),
        ylabel="y",
    ),
    # Ablesen: Graph mit markierten Punkten, ohne Term
    Plot(
        name="ablesen",
        curves=[Curve(lambda x: x**3 - 6 * x**2 + 9 * x)],
        xlim=(-1, 5),
        ylim=(-3, 6),
        points=[
            Point(1, 4, punkt("H", 1, 4), dx=-24, dy=10),
            Point(3, 0, punkt("T", 3, 0), dx=8, dy=-20),
            Point(2, 2, punkt("W", 2, 2), dx=10, dy=2),
        ],
        ylabel="y",
    ),
]
