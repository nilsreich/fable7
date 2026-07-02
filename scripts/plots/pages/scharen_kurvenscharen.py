"""Plots für scharen/kurvenscharen (Scharplots mit beschrifteten Parameterwerten)."""

from plotstyle import COLOR_F, COLOR_F1, COLOR_F2, COLOR_ORT, COLOR_TANGENTE, Curve, Plot, Point, punkt

PAGE = "scharen/kurvenscharen"

_FARBEN = [COLOR_F, COLOR_F1, COLOR_F2, COLOR_ORT, COLOR_TANGENTE]

PLOTS = [
    # Verschiebungsschar
    Plot(
        name="schar-verschiebung",
        curves=[
            Curve(lambda x: x**2 - 2, label=r"$t=-2$", color=_FARBEN[0]),
            Curve(lambda x: x**2 + 0, label=r"$t=0$", color=_FARBEN[1]),
            Curve(lambda x: x**2 + 1, label=r"$t=1$", color=_FARBEN[2]),
            Curve(lambda x: x**2 + 2, label=r"$t=2$", color=_FARBEN[3]),
        ],
        xlim=(-3, 3),
        ylim=(-3, 6),
        legend_loc="lower right",
    ),
    # Streckungsschar
    Plot(
        name="schar-streckung",
        curves=[
            Curve(lambda x: -(x**2), label=r"$t=-1$", color=_FARBEN[0]),
            Curve(lambda x: 0.5 * x**2, label=r"$t=0{,}5$", color=_FARBEN[1]),
            Curve(lambda x: x**2, label=r"$t=1$", color=_FARBEN[2]),
            Curve(lambda x: 2 * x**2, label=r"$t=2$", color=_FARBEN[3]),
        ],
        xlim=(-3, 3),
        ylim=(-4, 5),
        legend_loc="lower right",
    ),
    # Formänderung: Fallunterscheidung sichtbar
    Plot(
        name="schar-fallunterscheidung",
        curves=[
            Curve(lambda x: x**3 + 3 * x, label=r"$t=-3$", color=_FARBEN[0]),
            Curve(lambda x: x**3, label=r"$t=0$", color=_FARBEN[1]),
            Curve(lambda x: x**3 - 3 * x, label=r"$t=3$", color=_FARBEN[2]),
        ],
        xlim=(-3, 3),
        ylim=(-5, 5),
        legend_loc="lower right",
    ),
    # Gemeinsame Punkte aller Scharkurven
    Plot(
        name="schar-gemeinsame-punkte",
        curves=[
            Curve(lambda x: -(x**2) + 2, label=r"$t=-1$", color=_FARBEN[0]),
            Curve(lambda x: 0.5 * x**2 + 0.5, label=r"$t=0{,}5$", color=_FARBEN[1]),
            Curve(lambda x: 2 * x**2 - 1, label=r"$t=2$", color=_FARBEN[2]),
        ],
        xlim=(-3, 3),
        ylim=(-3, 5),
        points=[
            Point(-1, 1, punkt("P", -1, 1), dx=-64, dy=-4),
            Point(1, 1, punkt("Q", 1, 1), dx=12, dy=-4),
        ],
        legend_loc="lower right",
    ),
    # Wurfparabeln mit variabler Abwurfgeschwindigkeit
    Plot(
        name="wurfparabel-schar",
        curves=[
            Curve(lambda x: x - (10 / 25) * x**2, domain=(0, 2.5),
                  label=r"$v=5$ m/s", color=_FARBEN[0]),
            Curve(lambda x: x - (10 / 49) * x**2, domain=(0, 4.9),
                  label=r"$v=7$ m/s", color=_FARBEN[1]),
            Curve(lambda x: x - (10 / 100) * x**2, domain=(0, 10),
                  label=r"$v=10$ m/s", color=_FARBEN[2]),
        ],
        xlim=(-1, 11),
        ylim=(-0.5, 3.5),
        xlabel="x in m",
        ylabel="h(x) in m",
        ytick_step=0.5,
        legend_loc="upper right",
    ),
    # Medikamentendosierung als Parameter
    Plot(
        name="medikamenten-schar",
        curves=[
            Curve(lambda t: 0.1 * 0.5 * t * (t - 12) ** 2, domain=(0, 12),
                  label=r"$d=0{,}5$", color=_FARBEN[0]),
            Curve(lambda t: 0.1 * 1.0 * t * (t - 12) ** 2, domain=(0, 12),
                  label=r"$d=1$", color=_FARBEN[1]),
            Curve(lambda t: 0.1 * 1.5 * t * (t - 12) ** 2, domain=(0, 12),
                  label=r"$d=1{,}5$", color=_FARBEN[2]),
        ],
        xlim=(-1, 14),
        ylim=(-5, 45),
        xlabel="t in h",
        ylabel="K(t) in mg/l",
        ytick_step=10,
        legend_loc="upper right",
    ),
]
