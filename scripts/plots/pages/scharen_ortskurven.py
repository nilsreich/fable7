"""Plots für scharen/ortskurven: Scharen + gestrichelte violette Ortskurven."""

from plotstyle import COLOR_F, COLOR_F1, COLOR_F2, COLOR_ORT, Curve, Plot, Point

PAGE = "scharen/ortskurven"

_FARBEN = [COLOR_F, COLOR_F1, COLOR_F2]


def _ortskurve(fn, domain):
    return Curve(fn, label="Ortskurve", color=COLOR_ORT, linestyle="--",
                 linewidth=2.6, domain=domain)


PLOTS = [
    # Tiefpunkte von f_t(x) = x² − tx wandern auf y = −x²
    Plot(
        name="tiefpunkte-parabel",
        curves=[
            Curve(lambda x: x**2 + 3 * x, label=r"$t=-3$", color=_FARBEN[0]),
            Curve(lambda x: x**2, label=r"$t=0$", color=_FARBEN[1]),
            Curve(lambda x: x**2 - 3 * x, label=r"$t=3$", color=_FARBEN[2]),
            _ortskurve(lambda x: -(x**2), (-2.4, 2.4)),
        ],
        xlim=(-4, 4),
        ylim=(-4, 5),
        points=[
            Point(-1.5, -2.25, "", dx=0, dy=0),
            Point(0, 0, "", dx=0, dy=0),
            Point(1.5, -2.25, "", dx=0, dy=0),
        ],
        legend_loc="lower right",
    ),
    # Extrempunkte von f_t(x) = x³ − 3tx wandern auf y = −2x³
    Plot(
        name="extrempunkte-kubisch",
        curves=[
            Curve(lambda x: x**3 - 1.5 * x, label=r"$t=0{,}5$", color=_FARBEN[0]),
            Curve(lambda x: x**3 - 3 * x, label=r"$t=1$", color=_FARBEN[1]),
            Curve(lambda x: x**3 - 6 * x, label=r"$t=2$", color=_FARBEN[2]),
            _ortskurve(lambda x: -2 * x**3, (-1.7, 1.7)),
        ],
        xlim=(-3, 3),
        ylim=(-7, 7),
        ytick_step=2,
        points=[
            Point(0.70710678, -0.70710678, "", dx=0, dy=0),
            Point(-0.70710678, 0.70710678, "", dx=0, dy=0),
            Point(1, -2, "", dx=0, dy=0),
            Point(-1, 2, "", dx=0, dy=0),
            Point(1.41421356, -5.65685425, "", dx=0, dy=0),
            Point(-1.41421356, 5.65685425, "", dx=0, dy=0),
        ],
        legend_loc="lower left",
    ),
    # Wendepunkte von f_t(x) = x³ − 3tx² wandern auf y = −2x³
    Plot(
        name="wendepunkte-kubisch",
        curves=[
            Curve(lambda x: x**3 + 3 * x**2, label=r"$t=-1$", color=_FARBEN[0]),
            Curve(lambda x: x**3 - 1.5 * x**2, label=r"$t=0{,}5$", color=_FARBEN[1]),
            Curve(lambda x: x**3 - 3 * x**2, label=r"$t=1$", color=_FARBEN[2]),
            _ortskurve(lambda x: -2 * x**3, (-1.4, 1.4)),
        ],
        xlim=(-3, 3),
        ylim=(-5, 5),
        points=[
            Point(-1, 2, "", dx=0, dy=0),
            Point(0.5, -0.25, "", dx=0, dy=0),
            Point(1, -2, "", dx=0, dy=0),
        ],
        legend_loc="lower left",
    ),
    # Tiefpunkte von f_t(x) = tx² − 4x wandern auf der Geraden y = −2x
    Plot(
        name="tiefpunkte-gerade",
        curves=[
            Curve(lambda x: x**2 - 4 * x, label=r"$t=1$", color=_FARBEN[0]),
            Curve(lambda x: 2 * x**2 - 4 * x, label=r"$t=2$", color=_FARBEN[1]),
            Curve(lambda x: 4 * x**2 - 4 * x, label=r"$t=4$", color=_FARBEN[2]),
            _ortskurve(lambda x: -2 * x, (-0.5, 2.6)),
        ],
        xlim=(-2, 5),
        ylim=(-5, 5),
        points=[
            Point(2, -4, "", dx=0, dy=0),
            Point(1, -2, "", dx=0, dy=0),
            Point(0.5, -1, "", dx=0, dy=0),
        ],
        legend_loc="upper right",
    ),
    # Scheitel der Wurfparabeln liegen auf y = x/2
    Plot(
        name="wurfparabel-scheitel",
        curves=[
            Curve(lambda x: x - (10 / 25) * x**2, domain=(0, 2.5),
                  label=r"$v=5$ m/s", color=_FARBEN[0]),
            Curve(lambda x: x - (10 / 49) * x**2, domain=(0, 4.9),
                  label=r"$v=7$ m/s", color=_FARBEN[1]),
            Curve(lambda x: x - (10 / 100) * x**2, domain=(0, 10),
                  label=r"$v=10$ m/s", color=_FARBEN[2]),
            _ortskurve(lambda x: 0.5 * x, (0, 5.6)),
        ],
        xlim=(-1, 11),
        ylim=(-0.5, 3.5),
        xlabel="x in m",
        ylabel="h(x) in m",
        ytick_step=0.5,
        points=[
            Point(1.25, 0.625, "", dx=0, dy=0),
            Point(2.45, 1.225, "", dx=0, dy=0),
            Point(5, 2.5, "", dx=0, dy=0),
        ],
        legend_loc="upper right",
    ),
]
