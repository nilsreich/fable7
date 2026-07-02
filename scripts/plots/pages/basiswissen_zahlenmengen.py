"""Plots für basiswissen/zahlenmengen."""

import numpy as np

from plotstyle import Plot, Point, fmt_de

PAGE = "basiswissen/zahlenmengen"

_SQRT2 = float(np.sqrt(2.0))
_PI = float(np.pi)

PLOTS = [
    # Zahlengerade mit Vertretern der verschiedenen Zahlenmengen
    Plot(
        name="zahlengerade",
        curves=[],
        xlim=(-4, 4),
        ylim=(-1, 1),
        numberline=True,
        xlabel="x",
        points=[
            Point(-3, 0, r"$-3 \in \mathbb{Z}$", dx=-30, dy=14),
            Point(0.75, 0, r"$\frac{3}{4} \in \mathbb{Q}$", dx=-24, dy=14),
            Point(2, 0, r"$2 \in \mathbb{N}$", dx=-6, dy=14),
            Point(_SQRT2, 0, r"$\sqrt{2}$", dx=-8, dy=-30),
            Point(_PI, 0, r"$\pi$", dx=6, dy=-30),
        ],
    ),
]
