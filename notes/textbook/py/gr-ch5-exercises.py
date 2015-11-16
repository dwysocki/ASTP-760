#!/usr/bin/ipython

from os import path
from sys import argv

import numpy as np
import matplotlib.pyplot as plt

from sr import *

def problem_21(dir, fmt):
    limit = 5
    n_points = 100
    t = np.linspace(-limit, limit, n_points)

    def hyperbola_xs(a):
        x = np.sqrt(t**2 + a**2)

        return x

    def linear_xs(lamb):
        x = t / np.tanh(lamb)

        return x

    fig, ax = plt.subplots()

    ax.set_xlim([-limit, +limit])
    ax.set_ylim([-limit, +limit])

    ax.tick_params(axis='both', which='both',
                   top='off', bottom='off',
                   labelbottom='off', labelleft='off',
                   right='off', left='off')

    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$t$")

    a_s = np.linspace(0, limit, 11)[1:]
    lambda_s = np.linspace(-limit, limit, 50)

    for a in a_s:
        hyp_x = hyperbola_xs(a)

        ax.plot(+hyp_x, t, "r-", zorder=2)
        ax.plot(-hyp_x, t, "r-", zorder=2)

    for lamb in lambda_s:
        lin_x = linear_xs(lamb)

        ax.plot(+lin_x, t, "b-", zorder=1)
        ax.plot(-lin_x, t, "b-", zorder=1)



    ax.plot(t, +t, "k--", linewidth=4, zorder=3)
    ax.plot(t, -t, "k--", linewidth=4, zorder=3)



    fig.savefig(path.join(dir, "ch5_problem_21."+fmt))

problems = [
    problem_21
]

def main(dir, fmt):
    for problem in problems:
        problem(dir, fmt)

if __name__ == "__main__":
    exit(main(*argv[1:]))
