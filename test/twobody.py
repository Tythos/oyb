"""
"""

import numpy
import unittest
from scipy import integrate
from oyb import twobody, dynamics

class BasicIntegrate(unittest.TestCase):
    def test_ex2p2(self):
        R = numpy.array([3e7, 0, 0])
        V = numpy.array([0, 5e3, 0])
        RVi = integrate.odeint(twobody.f, numpy.append(R, V, axis=0), t=numpy.arange(0, 480, 10))
        
    def test_ex2p3(self):
        RV = numpy.array([8e6, 0, 6e6, 0, 7e3, 0])
        RVi = integrate.odeint(twobody.f, RV, t=numpy.arange(0, 4*60*60, 10))
        Ri = [dynamics.mag(RVi[i,0:3]) for i in range(RVi.shape[0])]
        hMin = min(Ri) - twobody.rEarth_m
        hMax = max(Ri) - twobody.rEarth_m
        self.assertTrue(abs(hMin - 3.622e6) / hMin < 1e-4)
        self.assertTrue(abs(hMax - 9.560e6) / hMax < 1e-2)

if __name__ == '__main__':
    unittest.main()
