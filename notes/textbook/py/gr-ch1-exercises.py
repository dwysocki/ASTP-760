#!/usr/bin/env python3

from sys import argv
from os import path
from itertools import chain

import numpy as np
import matplotlib.pyplot as plt


def spacetime_plot(xlim, tlim):
    fig, ax = plt.subplots()

    ax.set_xlabel(r"$x ({\rm m})$")
    ax.set_ylabel(r"$t ({\rm m})$")

    ax.grid(True)
    ax.set_xlim(xlim)
    ax.set_ylim(tlim)

    return fig, ax


def filename(problem, output, fmt):
    return path.join(output, "problem_{}.{}".format(problem, fmt))


def unravel_labels(iterable):
    return zip(*chain(*iterable))


def problem_3(output, fmt):
    xlim = [-10, +10]
    tlim = [-10, +10]

    x_min, x_max = xlim
    t_min, t_max = tlim

    t_range = np.arange(t_min, t_max, 0.01)
    x_range = np.arange(t_min, t_max, 0.01)

    v = 0.5
    gamma = (1 - v**2)**(-1/2)

    t_bar = (1/v)*x_range
    x_bar = v*x_range

    def a(fig, ax):
        x = 1*np.ones_like(t_range)

        line, *_ = ax.plot(x, t_range, color="blue")

        return [("(a)", line)]


    def b(fig, ax):
        x = 0.1*t_range + 0.5

        line, *_ = ax.plot(x, t_range, color="green")

        return [("(b)", line)]


    def c(fig, ax):
        line, *_ = ax.plot(x_range, x_bar,
                           x_range, t_bar,
                           color="red")

        return [("(c)", line)]


    def d(fig, ax):
        t = np.sqrt(x_range**2 + 1)
        color="olivedrab"

        line, *_ = ax.plot(x_range, +t,
                           x_range, -t,
                           color=color)

        return [("(d)", line)]


    def e(fig, ax):
        x = np.sqrt(t_range**2 + 1)
        color="darkgreen"

        line, *_ = ax.plot(+x, t_range,
                           -x, t_range,
                           color=color)

        return [("(e)", line)]


    def f(fig, ax):
        return []

    def g(fig, ax):
        color="gray"

        line, *_ = ax.plot(x_range, +t_range,
                           x_range, -t_range,
                           color=color)

        return [("(g)", line)]


    def h(fig, ax):
        t = 2 * np.ones_like(x_range)

        line, *_ = ax.plot(x_range, t,
                           color="darkorange")

        return [("(h)", line)]

    def i(fig, ax):
        t = x_bar + 2/gamma

        line, *_ = ax.plot(x_range, t,
                           color="darkgoldenrod")
        return [("(i)", line)]

    def j(fig, ax):
        return []

    def k(fig, ax):
        return []

    def l(fig, ax):
        return []


    problems = [a, b, c, d, e, f, g, h, i, j, k, l]

    fig, ax = spacetime_plot(xlim, tlim)

    ax.plot(np.zeros_like(t_range), t_range, color="black")
    ax.plot(x_range, np.zeros_like(x_range), color="black")

    labels, lines = unravel_labels(problem(fig, ax) for problem in problems)

    fig.legend(lines, labels)

    fig.savefig(filename("3", output, fmt))


def problem_5(output, fmt):
    xlim = [-10, +10]
    tlim = [-10, +10]

    x_min, x_max = xlim
    t_min, t_max = tlim

    t_range = np.arange(t_min, t_max, 0.01)
    x_range = np.arange(t_min, t_max, 0.01)

    fig, ax = spacetime_plot(xlim, tlim)

    ax.plot(np.zeros_like(t_range), t_range, color="black")
    ax.plot(x_range, np.zeros_like(x_range), color="black")


    # detectors
    d = 2*np.ones_like(t_range)
    d1_line, *_ = ax.plot(+d, t_range, color="green")
    d2_line, *_ = ax.plot(-d, t_range, color="orange")

    # outgoing signal
    x_out = np.arange(0, 2, 0.01)
    t_out = 2 * x_out - 2
    out_line, *_ = ax.plot(+x_out, t_out,
                           -x_out, t_out,
                           color="blue")

    # returning signal
    x_in = np.arange(-2, 0, 0.01)
    t_in = 4/3 * x_in + 31/6
    in_line, *_ = ax.plot(+x_in, t_in,
                          -x_in, t_in,
                          color="red")

    # O-bar's coordinates
    x_bar = -3/4 * x_range
    t_bar = -4/3 * x_range
    xbar_line, *_ = ax.plot(x_range, x_bar, color="grey")
    tbar_line, *_ = ax.plot(x_range, t_bar, color="silver")


    # lines of constant t-bar for the left & right emission events
    t_lf = -3/4 * x_range + 4
    t_rt = -3/4 * x_range + 1
    lf_line, *_ = ax.plot(x_range, t_lf, color="steelblue")
    rt_line, *_ = ax.plot(x_range, t_rt, color="navy")

    labels, lines = unravel_labels([
        [(r"$\bar{t}$", tbar_line), (r"$\bar{x}$", xbar_line)],
        [(r"$d_1$", d1_line), (r"$d_2$", d2_line)],
        [(r"$\gamma_{\rm out}$", out_line),
         (r"$\gamma_{\rm in}$", in_line)],
        [(r"$\bar{t}_{\rm left}$", lf_line),
         (r"$\bar{t}_{\rm right}$", rt_line)]
    ])

    fig.legend(lines, labels)

    fig.savefig(filename("5", output, fmt))



problems = [
    problem_3,
    problem_5
]



def main(output, fmt):
    for problem in problems:
        problem(output, fmt)


if __name__ == "__main__":
    program, output, fmt = argv
    exit(main(output, fmt))
