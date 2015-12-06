#!/usr/bin/env python3

from os import path
from sys import argv

import numpy as np
import matplotlib.pyplot as plt


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

    print("a)")
    print("    (i) phi =", phi(M_s, R_s))
    print("   (ii) phi =", phi(M_s,  AU))
    print("  (iii) phi =", phi(M_e, R_e))
    print("   (iv)   v =",   v(M_s,  AU))

    print()

    print("b)")
    print("    (Sun) a =", a(M_s,  AU))
    print("  (Earth) a =", a(M_e, R_e))



problems = [
    problem_3
]

def main(dir, fmt):
    for problem in problems:
        problem(dir, fmt)


if __name__ == "__main__":
    exit(main(*argv[1:]))
