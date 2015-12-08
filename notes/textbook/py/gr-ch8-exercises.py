#!/usr/bin/env python3

from os import path
from sys import argv

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants.constants import c


def problem_3(dir, fmt):
    c   = 1.000e+00
    G   = 1.000e+00
    M_s = 1.476e+03
    M_e = 4.434e-03
    R_s = 6.960e+08
    R_e = 6.371e+06
    AU  = 1.496e+11

    def phi(M, r):
        return - G * M / r

    def v(M, r):
        return np.sqrt(-phi(M, r))

    def a(M, r):
        return phi(M, r) / r

    print("P 8.3.")

    print("a)")
    print("    (i) phi =", phi(M_s, R_s))
    print("   (ii) phi =", phi(M_s,  AU))
    print("  (iii) phi =", phi(M_e, R_e))
    print("   (iv)   v =",   v(M_s,  AU))

    print()

    print("b)")
    print("    (Sun) a =", a(M_s,  AU))
    print("  (Earth) a =", a(M_e, R_e))


def problem_17(dir, fmt):
    M_s = 1.476e+03

    C = np.array([2.5e+6, 6.3e+6, 6.3e+7, 3.1e+8, 6.3e+9])
    T = np.array([8.4e-3, 5.5e-2, 2.1e+0, 2.3e+1, 2.1e+3]) * c

    def M(C, T):
        return C**3 / (2 * np.pi * T**2) / M_s

    M_bh_est = M(C, T)

    fig, ax = plt.subplots()

    ax.scatter(C, M_bh_est)

    ax.set_xlabel("Circumference (m)")
    ax.set_ylabel(r"$M_\bullet$ ($M_\odot$)")

    ax.set_xlim([0, 7e9])

    fig.savefig(path.join(dir, "ch8_problem_17b."+fmt))
    plt.close(fig)

    print("P 8.17.")

    print("b)")

    print("C_sat =", C[-1])
    print("M_bh  =", M_bh_est[-1])


problems = [
    problem_3,
    problem_17
]

def main(dir, fmt):
    for problem in problems:
        problem(dir, fmt)


if __name__ == "__main__":
    exit(main(*argv[1:]))
