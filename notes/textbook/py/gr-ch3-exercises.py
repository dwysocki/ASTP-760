#!/usr/bin/ipython

from os import path
from sys import argv

import numpy as np
import matplotlib.pyplot as plt

from sr import *

def problem_4(*args):
    print("Problem 3.4:")

    A = [ 2, 1, 1, 0]
    B = [ 1, 2, 0, 0]
    C = [ 0, 0, 1, 1]
    D = [-3, 2, 0, 0]
    E = [ 1, 1, 0, 0]

    X = np.vstack((A,B,C,D))

    P = [ 1, -1, -1,  0]
    Q = [ 0,  0,  1, -1]
    R = [ 2,  0,  0,  0]
    S = [-1, -1,  0,  0]

    p, q, r, s = np.linalg.solve(X, np.column_stack([P, Q, R, S])).T

    Y = np.column_stack((p,q,r,s))

    print("p =", p)
    print("q =", q)
    print("r =", r)
    print("s =", s)

    print()

    print("p(E) =", np.dot(p, E))

    print()

    print("det([p,q,r,s]) =", np.linalg.det(Y))

    print()


def problem_6(*args):
    print("Problem 3.6:")

    p = [1, 1, 1, 1]

    l_0 = [ 1,  1,  0,  0]
    l_1 = [ 1, -1,  0,  0]
    l_2 = [ 0,  0,  1, -1]
    l_3 = [ 0,  0,  1,  1]

    L = np.vstack((l_0, l_1, l_2, l_3))

    l = np.linalg.solve(L, p)

    print("l =", l)


def problem_8(dir, fmt):
    fig, ax = plt.subplots()

    ax.set_xlim([0, 5])
    ax.set_ylim([0, 5])

    ax.xaxis.grid(True, color="red",  linestyle="-")
    ax.yaxis.grid(True, color="blue", linestyle="-")

    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$t$")

    fig.savefig(path.join(dir, "ch3_problem_8."+fmt))


def problem_34(dir, fmt):
    fig, ax = plt.subplots()

    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])

    ax.set_aspect('equal')

    # axis variables
    t = x = np.linspace(-3, 3, 100)

    # basis vectors
    e_x = np.array([1, 0])
    e_t = np.array([0, 1])
    e_u = (e_t - e_x) / 2
    e_v = (e_t + e_x) / 2
    basis_vectors = [e_x, e_t, e_u, e_v]

    # values of t where {u,v} = {0,1}
    t_u_eq_0 = 0 + x
    t_u_eq_1 = 1 + x
    t_v_eq_0 = 0 - x
    t_v_eq_1 = 1 - x

    # plot the lines of constant u and v
    for t in [t_u_eq_0, t_u_eq_1, t_v_eq_0, t_v_eq_1]:
        ax.plot(x, t, color="gray", linestyle="--", zorder=1)

    # label the lines of constant u and v
    for label, loc_x, loc_t in zip(["$u = 0$", "$u = 1$", "$v = 0$", "$v = 1$"],
                                   [-2.85, -2.85, +2.55, +2.55],
                                   [-2.50, -1.50, -2.50, -1.50]):
        ax.text(loc_x, loc_t, label)

    # plot the basis vectors
    for e, color in zip(basis_vectors,
                        ["black", "black", "blue", "blue"]):
        ax.arrow(0, 0, e[0], e[1], color=color)

    # label the basis vectors
    for e, offset_x, offset_t, name in zip(basis_vectors,
                                           #    x,     t,     u,     v
                                           [+0.00, -0.05, +0.10, -0.05],
                                           [+0.10, +0.15, -0.10, +0.15],
                                           ["x", "t", "u", "v"]):
        ax.text(e[0]+offset_x, e[1]+offset_t, "$\\vec{e}_"+name+"$")

    fig.savefig(path.join(dir, "ch3_problem_34a."+fmt))

problems = [
    problem_4,
    problem_6,
    problem_8,
    problem_34
]


def main(dir, fmt):
    for problem in problems:
        problem(dir, fmt)


if __name__ == "__main__":
    exit(main(*argv[1:]))
