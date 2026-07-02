"""Plots für funktionen/trigonometrische."""

import numpy as np

from plotstyle import COLOR_F, COLOR_F1, COLOR_F2, Curve, Plot, Point, punkt

PAGE = "funktionen/trigonometrische"

_PI = np.pi


def _pi_ticks(*ks):
    """x-Ticks bei Vielfachen von π/2 mit π-Beschriftung setzen."""
    labels = {
        -2.0: r"$-2\pi$", -1.5: r"$-\frac{3\pi}{2}$", -1.0: r"$-\pi$",
        -0.5: r"$-\frac{\pi}{2}$", 0.5: r"$\frac{\pi}{2}$", 1.0: r"$\pi$",
        1.5: r"$\frac{3\pi}{2}$", 2.0: r"$2\pi$",
    }

    def extras(ax):
        ax.set_xticks([k * _PI for k in ks])
        ax.set_xticklabels([labels.get(k, "") for k in ks])

    return extras


PLOTS = [
    # Sinus und Kosinus im Vergleich
    Plot(
        name="sinus-kosinus",
        curves=[
            Curve(np.sin, label=r"$f(x)=\sin(x)$", color=COLOR_F),
            Curve(np.cos, label=r"$g(x)=\cos(x)$", color=COLOR_F1),
        ],
        xlim=(-2 * _PI, 2 * _PI),
        ylim=(-1.6, 1.6),
        ytick_step=1,
        legend_loc="upper left",
        extras=_pi_ticks(-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2),
    ),
    # Amplitude: Faktor a
    Plot(
        name="amplitude",
        curves=[
            Curve(lambda x: 2 * np.sin(x), label=r"$y=2\sin(x)$", color=COLOR_F1),
            Curve(np.sin, label=r"$y=\sin(x)$", color=COLOR_F),
            Curve(lambda x: 0.5 * np.sin(x), label=r"$y=0{,}5\sin(x)$", color=COLOR_F2),
        ],
        xlim=(-2 * _PI, 2 * _PI),
        ylim=(-2.6, 2.6),
        ytick_step=1,
        legend_loc="upper left",
        extras=_pi_ticks(-2, -1, 1, 2),
    ),
    # Periode: Faktor b
    Plot(
        name="periode",
        curves=[
            Curve(np.sin, label=r"$y=\sin(x)$", color=COLOR_F),
            Curve(lambda x: np.sin(2 * x), label=r"$y=\sin(2x)$", color=COLOR_F1),
        ],
        xlim=(-2 * _PI, 2 * _PI),
        ylim=(-1.6, 1.6),
        ytick_step=1,
        legend_loc="upper left",
        extras=_pi_ticks(-2, -1, 1, 2),
    ),
    # Kombination: Amplitude + Mittellinie
    Plot(
        name="amplitude-mittellinie",
        curves=[
            Curve(lambda x: 2 * np.sin(x) + 1, label=r"$f(x)=2\sin(x)+1$", color=COLOR_F),
            Curve(lambda x: 0 * x + 1, label=r"Mittellinie $y=1$",
                  color="#9e9e9e", linestyle="--", linewidth=1.6),
        ],
        xlim=(-2 * _PI, 2 * _PI),
        ylim=(-2.6, 3.9),
        ytick_step=1,
        legend_loc="lower left",
        extras=_pi_ticks(-2, -1, 1, 2),
    ),
    # Kontext: Riesenrad
    Plot(
        name="riesenrad",
        curves=[
            Curve(lambda t: 6 - 5 * np.cos(_PI / 6 * t), domain=(0, 24),
                  label=r"$h(t)=6-5\cos\left(\frac{\pi}{6}t\right)$"),
        ],
        xlim=(-2, 26),
        ylim=(-2, 13),
        xlabel="t in min",
        ylabel="h(t) in m",
        xtick_step=3,
        ytick_step=2,
        points=[
            Point(0, 1, punkt("A", 0, 1), dx=8, dy=-18),
            Point(6, 11, punkt("H", 6, 11), dx=-14, dy=10),
        ],
        legend_loc="lower right",
    ),
]
