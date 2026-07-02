"""Plots für ganzrationale/eigenschaften."""

from plotstyle import COLOR_F, COLOR_F1, Curve, Plot, Point, punkt

PAGE = "ganzrationale/eigenschaften"

PLOTS = [
    # Kontext: Wirkstoffkonzentration im Blut
    Plot(
        name="wirkstoff-verlauf",
        curves=[
            Curve(lambda t: 0.1 * t * (t - 12) ** 2, domain=(0, 12),
                  label=r"$K(t)=0{,}1t(t-12)^2$"),
        ],
        xlim=(-1, 14),
        ylim=(-4, 30),
        xlabel="t in h",
        ylabel="K(t) in mg/l",
        ytick_step=5,
        points=[Point(4, 25.6, punkt("H", 4, 25.6), dx=8, dy=6)],
        legend_loc="upper right",
    ),
    # Randverhalten bei geradem Grad
    Plot(
        name="verlauf-gerader-grad",
        curves=[
            Curve(lambda x: x**4 - 3 * x**2, label=r"$f(x)=x^4-3x^2$", color=COLOR_F),
            Curve(lambda x: -(x**4) + 3 * x**2, label=r"$g(x)=-x^4+3x^2$", color=COLOR_F1),
        ],
        xlim=(-3, 3),
        ylim=(-4, 4),
        legend_loc="lower right",
    ),
    # Randverhalten bei ungeradem Grad
    Plot(
        name="verlauf-ungerader-grad",
        curves=[
            Curve(lambda x: x**3 - 3 * x, label=r"$f(x)=x^3-3x$", color=COLOR_F),
            Curve(lambda x: -(x**3) + 3 * x, label=r"$g(x)=-x^3+3x$", color=COLOR_F1),
        ],
        xlim=(-3, 3),
        ylim=(-4, 4),
        legend_loc="lower right",
    ),
    # Gemischte Exponenten: keine Symmetrie
    Plot(
        name="keine-symmetrie",
        curves=[
            Curve(lambda x: x**3 - 3 * x**2, label=r"$h(x)=x^3-3x^2$"),
        ],
        xlim=(-2, 4),
        ylim=(-5, 3),
    ),
    # Grad 3, drei Nullstellen
    Plot(
        name="nullstellen-anzahl",
        curves=[
            Curve(lambda x: x**3 - 4 * x, label=r"$f(x)=x^3-4x$"),
        ],
        xlim=(-3, 3),
        ylim=(-4, 4),
        points=[
            Point(-2, 0, r"$N_1$", dx=-26, dy=8),
            Point(0, 0, r"$N_2$", dx=8, dy=8),
            Point(2, 0, r"$N_3$", dx=10, dy=-4),
        ],
    ),
]
