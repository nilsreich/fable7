"""Plots für funktionen/exponential-logarithmus."""

import numpy as np

from plotstyle import COLOR_F, COLOR_F1, COLOR_F2, Curve, Plot, Point, punkt

PAGE = "funktionen/exponential-logarithmus"

PLOTS = [
    # Wachstum vs. Zerfall
    Plot(
        name="wachstum-zerfall",
        curves=[
            Curve(lambda x: 2.0**x, label=r"$f(x)=2^x$", color=COLOR_F),
            Curve(lambda x: 0.5**x, label=r"$g(x)=\left(\frac{1}{2}\right)^x$", color=COLOR_F1),
        ],
        xlim=(-3, 3),
        ylim=(-1, 8),
        legend_loc="upper center",
    ),
    # Verschiedene Basen im Vergleich
    Plot(
        name="basis-vergleich",
        curves=[
            Curve(lambda x: 1.5**x, label=r"$y=1{,}5^x$", color=COLOR_F2),
            Curve(lambda x: 2.0**x, label=r"$y=2^x$", color=COLOR_F),
            Curve(lambda x: 3.0**x, label=r"$y=3^x$", color=COLOR_F1),
        ],
        xlim=(-3, 3),
        ylim=(-1, 9),
        legend_loc="upper left",
    ),
    # Bakterienwachstum (Kontext Biologie)
    Plot(
        name="bakterien-wachstum",
        curves=[
            Curve(lambda t: 2 * 1.5**t, domain=(0, 8), label=r"$N(t)=2 \cdot 1{,}5^t$"),
        ],
        xlim=(-1, 9),
        ylim=(-5, 55),
        xlabel="t in h",
        ylabel="N(t) in Tsd.",
        ytick_step=10,
        points=[Point(0, 2, punkt("A", 0, 2), dx=8, dy=8)],
    ),
    # Medikamentenabbau mit Halbwertszeit 6 h
    Plot(
        name="medikament-halbwertszeit",
        curves=[
            Curve(lambda t: 80 * 0.5 ** (t / 6), domain=(0, 24),
                  label=r"$K(t)=80 \cdot 0{,}5^{t/6}$"),
        ],
        xlim=(-2, 26),
        ylim=(-10, 90),
        xlabel="t in h",
        ylabel="K(t) in mg",
        xtick_step=6,
        ytick_step=20,
        points=[
            Point(0, 80, punkt("A", 0, 80), dx=10, dy=4),
            Point(6, 40, punkt("P", 6, 40), dx=10, dy=6),
            Point(12, 20, punkt("Q", 12, 20), dx=10, dy=6),
        ],
    ),
    # Logarithmus als Umkehrung der Exponentialfunktion
    Plot(
        name="logarithmus-umkehrung",
        curves=[
            Curve(lambda x: 2.0**x, label=r"$f(x)=2^x$", color=COLOR_F, domain=(-3, 2.3)),
            Curve(lambda x: np.log2(np.clip(x, 1e-9, None)), label=r"$g(x)=\log_2 x$",
                  color=COLOR_F2, domain=(0.01, 5)),
            Curve(lambda x: x, label=r"$y=x$", color="#9e9e9e", linestyle="--", linewidth=1.6),
        ],
        xlim=(-3, 5),
        ylim=(-3, 5),
        legend_loc="lower right",
    ),
]
