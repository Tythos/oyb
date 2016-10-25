"""
"""

import numpy
from oyb import dynamics

mu_m3ps2 = 3.986e14
rEarth_m = 6.3781e6

def f(Y, t):
    R = Y[0:3]
    V = Y[3:6]
    r = dynamics.mag(R)
    A = -R * mu_m3ps2 / r**3
    return numpy.append(V, A, axis=0)
