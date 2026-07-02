"""Plots für funktionen/potenz-wurzel."""

import numpy as np

from plotstyle import COLOR_F, COLOR_F1, COLOR_F2, COLOR_ORT, Curve, Plot, Point, punkt

PAGE = "funktionen/potenz-wurzel"

PLOTS = [
    # Gerade Exponenten: achsensymmetrisch
    Plot(
        name="potenz-gerade-exponenten",
        curves=[
            Curve(lambda x: x**2, label=r"$f(x)=x^2$", color=COLOR_F),
            Curve(lambda x: x**4, label=r"$g(x)=x^4$", color=COLOR_F1),
        ],
        xlim=(-2, 2),
        ylim=(-1, 5),
        xtick_step=1,
        legend_loc="lower right",
    ),
    # Ungerade Exponenten: punktsymmetrisch
    Plot(
        name="potenz-ungerade-exponenten",
        curves=[
            Curve(lambda x: x**3, label=r"$f(x)=x^3$", color=COLOR_F),
            Curve(lambda x: x**5, label=r"$g(x)=x^5$", color=COLOR_F1),
        ],
        xlim=(-2, 2),
        ylim=(-4, 4),
        legend_loc="lower right",
    ),
    # Negative Exponenten: Hyperbeln mit Polstelle bei x = 0
    Plot(
        name="potenz-negative-exponenten",
        curves=[
            Curve(lambda x: 1.0 / x, label=r"$f(x)=x^{-1}=\frac{1}{x}$", color=COLOR_F),
            Curve(lambda x: 1.0 / x**2, label=r"$g(x)=x^{-2}=\frac{1}{x^2}$", color=COLOR_F1),
        ],
        xlim=(-4, 4),
        ylim=(-4, 4),
        legend_loc="lower right",
    ),
    # Wurzelfunktion als Umkehrung des rechten Parabelastes
    Plot(
        name="wurzel-und-quadrat",
        curves=[
            Curve(lambda x: x**2, label=r"$f(x)=x^2$ für $x\geq 0$", color=COLOR_F, domain=(0, 3)),
            Curve(lambda x: np.sqrt(np.clip(x, 0, None)), label=r"$g(x)=\sqrt{x}$", color=COLOR_F2, domain=(0, 6)),
            Curve(lambda x: x, label=r"$y=x$", color="#9e9e9e", linestyle="--", linewidth=1.6),
        ],
        xlim=(-1, 6),
        ylim=(-1, 6),
        legend_loc="upper left",
    ),
    # Alle Potenzfunktionen laufen durch (0|0) und (1|1)
    Plot(
        name="potenz-vergleich",
        curves=[
            Curve(lambda x: x, label=r"$y=x$", color=COLOR_F),
            Curve(lambda x: x**2, label=r"$y=x^2$", color=COLOR_F1),
            Curve(lambda x: x**3, label=r"$y=x^3$", color=COLOR_F2),
            Curve(lambda x: x**4, label=r"$y=x^4$", color=COLOR_ORT),
        ],
        xlim=(-0.25, 1.75),
        ylim=(-0.25, 2.25),
        xtick_step=0.5,
        ytick_step=0.5,
        points=[Point(1, 1, punkt("P", 1, 1), dx=10, dy=-14)],
        legend_loc="lower right",
    ),
]
