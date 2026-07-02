"""Plots für differentialrechnung/graphisches-differenzieren.

Die Aufgaben-Plots zeigen bewusst KEINEN Funktionsterm – der Term steht
nur in den Lösungs-Plots bzw. Lösungen.
"""

from plotstyle import COLOR_F, COLOR_F1, Curve, Plot, Point, punkt

PAGE = "differentialrechnung/graphisches-differenzieren"


def _senkrechte(*xs):
    def extras(ax):
        for x in xs:
            ax.axvline(x, color="#999999", linestyle=":", linewidth=1.3, zorder=1)
    return extras


PLOTS = [
    # Schema: f und f' übereinander gedacht
    Plot(
        name="schema-f-und-fstrich",
        curves=[
            Curve(lambda x: x**3 - 3 * x, label=r"$f$", color=COLOR_F),
            Curve(lambda x: 3 * x**2 - 3, label=r"$f'$", color=COLOR_F1),
        ],
        xlim=(-3, 3),
        ylim=(-5, 7),
        points=[
            Point(-1, 2, "H", dx=-8, dy=10),
            Point(1, -2, "T", dx=4, dy=-20),
            Point(-1, 0, "", dx=0, dy=0),
            Point(1, 0, "", dx=0, dy=0),
        ],
        legend_loc="upper center",
        extras=_senkrechte(-1, 1),
    ),
    # Aufgabe 3: Parabel (ohne Term!)
    Plot(
        name="aufgabe-parabel",
        curves=[Curve(lambda x: x**2 - 2 * x, label=r"$f$")],
        xlim=(-2, 4),
        ylim=(-2, 6),
        points=[Point(1, -1, punkt("T", 1, -1), dx=8, dy=-16)],
        legend_loc="upper left",
    ),
    "PAIR-loesung-parabel",
    # Aufgabe 4: nach unten geöffnete Parabel (ohne Term)
    Plot(
        name="aufgabe-parabel-unten",
        curves=[Curve(lambda x: -0.5 * x**2 + 2, label=r"$f$")],
        xlim=(-4, 4),
        ylim=(-4, 4),
        points=[Point(0, 2, punkt("H", 0, 2), dx=8, dy=8)],
        legend_loc="lower left",
    ),
    "PAIR-loesung-parabel-unten",
    # Aufgabe 5: kubische Funktion (ohne Term)
    Plot(
        name="aufgabe-kubisch",
        curves=[Curve(lambda x: 0.5 * x**3 - 1.5 * x, label=r"$f$")],
        xlim=(-3, 3),
        ylim=(-4, 4),
        points=[
            Point(-1, 1, punkt("H", -1, 1), dx=-56, dy=6),
            Point(1, -1, punkt("T", 1, -1), dx=8, dy=-18),
        ],
        legend_loc="upper left",
    ),
    "PAIR-loesung-kubisch",
    # Aufgabe 6: kubische Funktion mit H(0|2), T(2|−2) (ohne Term)
    Plot(
        name="aufgabe-kubisch2",
        curves=[Curve(lambda x: x**3 - 3 * x**2 + 2, label=r"$f$")],
        xlim=(-2, 4),
        ylim=(-4, 5),
        points=[
            Point(0, 2, punkt("H", 0, 2), dx=-30, dy=10),
            Point(2, -2, punkt("T", 2, -2), dx=8, dy=-18),
        ],
        legend_loc="lower right",
    ),
    "PAIR-loesung-kubisch2",
    # Aufgabe 7: W-förmige Funktion (ohne Term)
    Plot(
        name="aufgabe-w-form",
        curves=[Curve(lambda x: 0.25 * x**4 - 2 * x**2, label=r"$f$")],
        xlim=(-3.5, 3.5),
        ylim=(-5, 5),
        points=[
            Point(-2, -4, punkt("T", -2, -4), dx=-70, dy=0),
            Point(0, 0, punkt("H", 0, 0), dx=8, dy=8),
            Point(2, -4, punkt("T", 2, -4), dx=10, dy=0),
        ],
        legend_loc="upper center",
    ),
    "PAIR-loesung-w-form",
    # Aufgabe 8: gegeben ist f' – gesucht ist f
    Plot(
        name="aufgabe-rueckwaerts",
        curves=[Curve(lambda x: x + 1, label=r"$f'$", color=COLOR_F1)],
        xlim=(-4, 3),
        ylim=(-3, 4),
        points=[Point(-1, 0, punkt("N", -1, 0), dx=-30, dy=10)],
        legend_loc="upper left",
    ),
    "PAIR-loesung-rueckwaerts",
]

# Lösungs-Plots (mit Term)
_LOESUNGEN = {
    "PAIR-loesung-parabel": Plot(
        name="loesung-parabel",
        curves=[
            Curve(lambda x: x**2 - 2 * x, label=r"$f(x)=x^2-2x$", color=COLOR_F,
                  linestyle="--", linewidth=1.8),
            Curve(lambda x: 2 * x - 2, label=r"$f'(x)=2x-2$", color=COLOR_F1),
        ],
        xlim=(-2, 4),
        ylim=(-4, 6),
        points=[Point(1, 0, "", dx=0, dy=0)],
        legend_loc="upper left",
    ),
    "PAIR-loesung-parabel-unten": Plot(
        name="loesung-parabel-unten",
        curves=[
            Curve(lambda x: -0.5 * x**2 + 2, label=r"$f(x)=-0{,}5x^2+2$", color=COLOR_F,
                  linestyle="--", linewidth=1.8),
            Curve(lambda x: -x, label=r"$f'(x)=-x$", color=COLOR_F1),
        ],
        xlim=(-4, 4),
        ylim=(-4, 4),
        legend_loc="lower left",
    ),
    "PAIR-loesung-kubisch": Plot(
        name="loesung-kubisch",
        curves=[
            Curve(lambda x: 0.5 * x**3 - 1.5 * x, label=r"$f(x)=0{,}5x^3-1{,}5x$",
                  color=COLOR_F, linestyle="--", linewidth=1.8),
            Curve(lambda x: 1.5 * x**2 - 1.5, label=r"$f'(x)=1{,}5x^2-1{,}5$", color=COLOR_F1),
        ],
        xlim=(-3, 3),
        ylim=(-4, 5),
        legend_loc="upper center",
    ),
    "PAIR-loesung-kubisch2": Plot(
        name="loesung-kubisch2",
        curves=[
            Curve(lambda x: x**3 - 3 * x**2 + 2, label=r"$f(x)=x^3-3x^2+2$",
                  color=COLOR_F, linestyle="--", linewidth=1.8),
            Curve(lambda x: 3 * x**2 - 6 * x, label=r"$f'(x)=3x^2-6x$", color=COLOR_F1),
        ],
        xlim=(-2, 4),
        ylim=(-4, 6),
        legend_loc="lower right",
    ),
    "PAIR-loesung-w-form": Plot(
        name="loesung-w-form",
        curves=[
            Curve(lambda x: 0.25 * x**4 - 2 * x**2, label=r"$f(x)=0{,}25x^4-2x^2$",
                  color=COLOR_F, linestyle="--", linewidth=1.8),
            Curve(lambda x: x**3 - 4 * x, label=r"$f'(x)=x^3-4x$", color=COLOR_F1),
        ],
        xlim=(-3.5, 3.5),
        ylim=(-5, 6),
        legend_loc="upper center",
    ),
    "PAIR-loesung-rueckwaerts": Plot(
        name="loesung-rueckwaerts",
        curves=[
            Curve(lambda x: x + 1, label=r"$f'(x)=x+1$", color=COLOR_F1),
            Curve(lambda x: 0.5 * x**2 + x, label=r"$f(x)=0{,}5x^2+x$", color=COLOR_F,
                  linestyle="--", linewidth=1.8),
            Curve(lambda x: 0.5 * x**2 + x + 1.5, label=r"$f(x)=0{,}5x^2+x+1{,}5$",
                  color="#74a9d8", linestyle="--", linewidth=1.8),
        ],
        xlim=(-4, 3),
        ylim=(-3, 5),
        legend_loc="upper left",
    ),
}

PLOTS = [_LOESUNGEN[p] if isinstance(p, str) else p for p in PLOTS]
