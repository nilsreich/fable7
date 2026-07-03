"""Plots für funktionen/gebrochenrationale."""

from plotstyle import COLOR_F, COLOR_F1, Curve, Plot, punkt, Point

PAGE = "funktionen/gebrochenrationale"

_ASYMPTOTE = dict(color="#999999", linestyle="--", linewidth=1.6, zorder=1)


def _asymptoten(senkrecht=(), waagerecht=()):
    def extras(ax):
        for x in senkrecht:
            ax.axvline(x, **_ASYMPTOTE)
        for y in waagerecht:
            ax.axhline(y, **_ASYMPTOTE)
    return extras


PLOTS = [
    # Verschobene Polstelle: f(x) = 1/(x-2) mit senkrechter Asymptote x = 2
    Plot(
        name="polstelle",
        curves=[
            Curve(lambda x: 1.0 / (x - 2), label=r"$f(x)=\frac{1}{x-2}$", color=COLOR_F),
        ],
        xlim=(-3, 7),
        ylim=(-4, 4),
        extras=_asymptoten(senkrecht=(2,)),
        legend_loc="upper left",
    ),
    # Mit und ohne Vorzeichenwechsel an der Polstelle
    Plot(
        name="pol-vergleich",
        curves=[
            Curve(lambda x: 1.0 / (x - 1), label=r"$f(x)=\frac{1}{x-1}$", color=COLOR_F),
            Curve(lambda x: 1.0 / (x - 1) ** 2, label=r"$g(x)=\frac{1}{(x-1)^2}$", color=COLOR_F1),
        ],
        xlim=(-3, 5),
        ylim=(-4, 6),
        extras=_asymptoten(senkrecht=(1,)),
        legend_loc="upper left",
    ),
    # Waagerechte Asymptote y = 2 bei g(x) = (2x+1)/x = 2 + 1/x
    Plot(
        name="waagerechte-asymptote",
        curves=[
            Curve(lambda x: (2 * x + 1) / x, label=r"$g(x)=\frac{2x+1}{x}=2+\frac{1}{x}$", color=COLOR_F),
        ],
        xlim=(-6, 6),
        ylim=(-2, 6),
        extras=_asymptoten(waagerecht=(2,)),
        legend_loc="lower right",
    ),
    # Verschobene Hyperbel: 1/x gegen 1/(x-2) + 1 (Transformations-Blick)
    Plot(
        name="hyperbel-verschoben",
        curves=[
            Curve(lambda x: 1.0 / x, label=r"$f(x)=\frac{1}{x}$", color=COLOR_F),
            Curve(lambda x: 1.0 / (x - 2) + 1, label=r"$g(x)=\frac{1}{x-2}+1$", color=COLOR_F1),
        ],
        xlim=(-4, 6),
        ylim=(-3, 5),
        extras=_asymptoten(senkrecht=(2,), waagerecht=(1,)),
        legend_loc="lower right",
    ),
    # Sachkontext: Stückkosten k(x) = (0,5x + 400)/x nähern sich 0,50 €
    Plot(
        name="stueckkosten",
        curves=[
            Curve(
                lambda x: (0.5 * x + 400) / x,
                label=r"$k(x)=\frac{0{,}5x+400}{x}$",
                color=COLOR_F,
                domain=(80, 3000),
            ),
        ],
        xlim=(0, 3000),
        ylim=(0, 6),
        xtick_step=500,
        ytick_step=1,
        xlabel="x (Stück)",
        ylabel="k(x) in €",
        extras=_asymptoten(waagerecht=(0.5,)),
        points=[Point(1000, 0.9, punkt("P", 1000, 0.9), dx=8, dy=10)],
        legend_loc="upper right",
    ),
]
