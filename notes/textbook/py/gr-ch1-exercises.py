#!/usr/bin/env python3

from sys import argv
from os import path

import numpy as np
import matplotlib.pyplot as plt

def spacetime_plot(x, t):
    fig, ax = plt.subplots()

    ax.set_xlabel(r"$x ({\rm m})$")
    ax.set_ylabel(r"$t ({\rm m})$")

    ax.grid(True)

    ax.plot(x, t)

    return fig, ax


def problem_3(output, fmt):
    def filename(problem):
        return path.join(output, "problem_{}.{}".format(problem, fmt))

    def a():
        t = np.arange(0, 5, 0.01)
        x = 1*np.ones_like(t)

        return x, t

    def b():
        t = np.arange(-5, 5, 0.01)
        x = 0.1*t + 0.5

        return x, t

    problems = [a, b]


    for problem in problems:
        x, t = problem()

        fig, ax = spacetime_plot(x, t)

        fig.savefig(filename("3{}".format(problem.__name__)))


problems = [
    problem_3
]



def main(output, fmt):
    for problem in problems:
        problem(output, fmt)


if __name__ == "__main__":
    program, output, fmt = argv
    exit(main(output, fmt))
