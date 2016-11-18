"""
"""

from __future__ import division
import unittest
import numpy
from math import pi
from oyb import orb, earth, anomaly

class ClassTests(unittest.TestCase):
    def test_default(self):
        o = orb.Orbit()
        
    def test_args(self):
        o = orb.Orbit(a_m=1.064e7, e=0.42607, i_rad=39.687*pi/180, O_rad=130.32*pi/180, w_rad=42.373*pi/180, M_rad=4.2866)
        
    def test_example4p3(self):
        rEci_m = numpy.array([-6.045e6, -3.490e6, 2.5e6])
        vEci_mps = numpy.array([-3.457e3, 6.618e3, 2.533e3])
        o = orb.Orbit.fromRV(rEci_m, vEci_mps)
        h_m2ps = o.getAngMom()
        tht_rad = anomaly.mean2true(o.M_rad, o.e)
        T_s = o.getPeriod()
        self.assertTrue(abs(h_m2ps - 5.831e10) / h_m2ps < 1e-3)
        self.assertTrue(abs(o.i_rad - 153.2 * pi / 180) / o.i_rad < 1e-3)
        self.assertTrue(abs(o.O_rad - 255.3 * pi / 180) / o.O_rad < 1e-3)
        self.assertTrue(abs(o.e - 0.1712) / o.e < 1e-3)
        self.assertTrue(abs(o.w_rad - 20.07 * pi / 180) / o.w_rad < 1e-3)
        self.assertTrue(abs(tht_rad - 28.45 * pi / 180) / tht_rad < 1e-3)
        self.assertTrue(abs(T_s - 2.278 * 3600) / T_s < 1e-3)
        
    def test_example2p8(self):
        o = orb.Orbit.fromHTht(1.545e6, 126 * pi / 180, 8.52e5, 58 * pi / 180)
        hPer_m, hApo_m = o.getShape()
        T_s = o.getPeriod()
        self.assertTrue(abs(o.a_m - 7.593e6) / o.a_m < 1e-3)
        self.assertTrue(abs(o.e - 0.08164) / o.e < 1e-3)
        self.assertTrue(abs(hPer_m - 5.955e5) / hPer_m < 1e-3)
        self.assertTrue(abs(T_s - 1.829 * 3600) / T_s < 1e-3)
        
class FrameTests(unittest.TestCase):
    def test_pqw(self):
        o = orb.Orbit(e=0.5, M_rad=0.5*pi)
        rPqw_m = o.getRpqw()
        
    def test_example4p7(self):
        e = 0.4
        a_m = 8e10 / (earth.mu_m3ps2 * (1 - e**2))
        M_rad = anomaly.true2mean(30 * pi / 180, e)
        o = orb.Orbit(a_m=a_m, e=e, i_rad=30*pi/180, O_rad=40*pi/180, w_rad=60*pi/180, M_rad=M_rad)
        rEci_m = o.getReci()
        
class PropertyTests(unittest.TestCase):
    def setUp(self):
        hPer_km = 400
        hApo_km = 4000
        self.o = orb.Orbit()
        self.o.setShape(1e3 * hPer_km, 1e3 * hApo_km)
        
    def test_a(self):
        self.assertTrue(abs(self.o.e - 0.2098) / self.o.e < 1e-3)
        
    def test_b(self):
        h_m2ps = self.o.getAngMom()
        self.assertTrue(abs(h_m2ps - 5.7172e10) / h_m2ps < 1e-3)
        
    def test_cd(self):
        vPer_mps, vApo_mps = self.o.getShapeVel()
        self.assertTrue(abs(vPer_mps - 8.435e3) / vPer_mps < 1e-3)
        self.assertTrue(abs(vApo_mps - 5.509e3) / vApo_mps < 1e-3)
        
    def test_e(self):
        self.assertTrue(abs(self.o.a_m - 8.578e6) / self.o.a_m < 1e-3)
        
    def test_f(self):
        T_s = self.o.getPeriod()
        self.assertTrue(abs(T_s - 2.196 * 3600) / T_s < 1e-3)
        
    def test_g(self):
        rTaa_m = self.o.getTaaRad()
        self.assertTrue(abs(rTaa_m - 8.387e6) / rTaa_m < 1e-3)

if __name__ == '__main__':
    unittest.main()
