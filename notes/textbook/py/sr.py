import numpy as np

def lorentz_factor(v):
    """Returns the lorentz factor for velocity v."""
    return (1 - v**2)**(-1/2)


def Lambda_matrix_x(v):
    """Returns the Lambda matrix for velocity v in the x-direction."""
    gamma = lorentz_factor(v)
    neg_v_gamma = -v*gamma

    return np.array([
        [gamma,       neg_v_gamma, 0, 0],
        [neg_v_gamma, gamma,       0, 0],
        [0,           0,           1, 0],
        [0,           0,           0, 1]])


def transformed_bases_x(bases, v):
    """Given a set of basis vectors, `bases`, which are moving with some
    velocity `v` in the +x direction, returns the set of basis vectors in the
    transformed system."""
    return np.dot(Lambda_matrix_x(v), bases.T)


def transformed_components_x(components, v):
    return np.dot(Lambda_matrix_x(v), components)


def barred(string, bars):
    """Takes a LaTeX string and applies `bars` bars to it."""
    if bars == 0:
        return string
    else:
        return barred("\\bar{"+string+"}", bars-1)
