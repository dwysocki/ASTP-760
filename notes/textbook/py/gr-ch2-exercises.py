#!/usr/bin/env python3

from sys import argv
from os import path

import numpy as np
import matplotlib.pyplot as plt

from sr import *




def problem_6(dir, fmt):
    def t_x_quiver(e):
        return ([0, 0],
                [0, 0],
                e[:,0],
                e[:,1])

    # axis label offset
    offset = 0.1

    # relative velocity between O -> O' and O' -> O''
    v = -0.6
    # basis vectors in O frame
    e = np.eye(4)
    e_ = transformed_bases_x(e, v)
    e__ = transformed_bases_x(e_, v)

    fig, ax = plt.subplots()

    for basis, color, bars in zip([e, e_, e__],
                                  ["black", "red", "blue"],
                                  range(3)):
        # unpack vector components
        e_0t, e_1t, e_0x, e_1x = basis[0,0], basis[1,0], basis[0,1], basis[1,1]

        # plot vectors
        ax.arrow(0, 0, e_0x, e_0t, color=color)
        ax.arrow(0, 0, e_1x, e_1t, color=color)

        # label vectors
        ax.text(e_0x, e_0t+offset, r"$\vec{{e}}_{}$".format(barred("0", bars)))
        ax.text(e_1x+offset, e_1t, r"$\vec{{e}}_{}$".format(barred("1", bars)))

    ## invariant hyperbola ##
    # time-like
    x_tl = np.arange(-1, 4, 0.01)
    t_tl = np.sqrt(x_tl**2 + 1)
    # space-like
    t_sl = np.arange(-1, 4, 0.01)
    x_sl = np.sqrt(t_sl**2 + 1)
    # plot them
    ax.plot(x_tl, t_tl, color="lightgray", linestyle='--', zorder=1)
    ax.plot(x_sl, t_sl, color="lightgray", linestyle='--', zorder=1)

    ## null line ##
    null = np.arange(-1, 4, 0.01)
    ax.plot(null, null, color="lightgray", linestyle="--", zorder=1)

    ax.set_xlim([-1, 4])
    ax.set_ylim([-1, 4])

    ax.set_aspect('equal')

    fig.savefig(path.join(dir, "problem6."+fmt))



def main(dir, fmt):
    problem_6(dir, fmt)


if __name__ == "__main__":
    exit(main(*argv[1:]))
