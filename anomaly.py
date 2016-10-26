"""
"""

from math import pi, atan2, sin, cos, tan

def mean2ecc(M_rad, e):
    """
    """
    E_rad = M_rad + 0.5 * e
    if M_rad > pi:
        E_rad = M_rad - 0.5 * e
    r = 1
    tol = 1e-8
    n = 0
    max = 1e3
    while abs(r) > tol and n < max:
        n = n + 1
        f = E_rad - e * sin(E_rad) - M_rad
        df = 1 - e * cos(E_rad)
        r = f / df
        E_rad = E_rad - r
    if abs(r) > tol:
        raise Exception('Failed to converge within %u iterations' % n)
    return E_rad

def ecc2true(E_rad, e):
    """
    """
    n = (1 + e)**0.5 * tan(0.5 * E_rad)
    d = (1 - e)**0.5
    return 2 * atan2(n, d)
    
def true2ecc(tht_rad, e):
    """
    """
    n = (1 - e)**0.5 * tan(0.5 * tht_rad)
    d = (1 + e)**0.5
    return 2 * atan2(n, d)
    
def ecc2mean(E_rad, e):
    """
    """
    return E_rad - e * sin(E_rad)
    
def true2mean(tht_rad, e):
    """
    """
    E_rad = true2ecc(tht_rad, e)
    return ecc2mean(E_rad, e)

def mean2true(M_rad, e):
    """
    """
    E_rad = mean2ecc(M_rad, e)
    return ecc2true(E_rad, e)
