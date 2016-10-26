"""
"""

from __future__ import division
import datetime
import numpy
from math import pi, cos, sin, acos
from oyb import anomaly, rot, earth

class Orbit(object):
    """
    """
    
    def __init__(self, a_m=None, e=None, i_rad=None, O_rad=None, w_rad=None, M_rad=None, tEpoch_dt=None):
        self.a_m = a_m if a_m is not None else ((earth.tSidDay_s / (2 * pi))**2 * earth.mu_m3ps2)**(1/3)
        self.e = e if e is not None else 0
        self.i_rad = i_rad if i_rad is not None else 0
        self.O_rad = O_rad if O_rad is not None else 0
        self.w_rad = w_rad if w_rad is not None else 0
        self.M_rad = M_rad if M_rad is not None else 0
        self.tEpoch_dt = tEpoch_dt if tEpoch_dt is not None else datetime.datetime.utcnow()
        
    def __str__(self):
        """
        """
        hPer_m, hApo_m = self.getShape()
        return '<%g x %g [km] orbit.Orbit at 0x%08x>' % (hPer_m * 1e-3, hApo_m * 1e-3, id(self))
        
    def getPeriod(self):
        """
        """
        T_s = 2 * pi * (self.a_m**3 / earth.mu_m3ps2)**0.5
        return T_s
        
    def getTrue(self, t_dt=None):
        """
        """
        if t_dt is None:
            t_dt = self.tEpoch_dt
        dt_s = (t_dt - self.tEpoch_dt).total_seconds() * 86400
        dM_rad = dt_s * 2 * pi / self.getPeriod()
        M_rad = (self.M_rad + dM_rad) % (2 * pi)
        return anomaly.mean2true(M_rad, self.e)
        
    def getQpqw2eci(self):
        """
        """
        w = rot.Z(self.w_rad)
        i = rot.X(self.i_rad)
        O = rot.Z(self.O_rad)
        return w.dot(i).dot(O)
        
    def getRpqw(self, t_dt=None):
        tht_rad = self.getTrue(t_dt)
        d = 1 + self.e * cos(tht_rad)
        p_m = self.a_m * (1 - self.e**2) * cos(tht_rad) / d
        q_m = self.a_m * (1 - self.e**2) * sin(tht_rad) / d
        return numpy.array([p_m, q_m, 0])
    
    def getReci(self, t_dt=None):
        """
        """
        rPqw = self.getRpqw(t_dt)
        Qpqw2eci = self.getQpqw2eci()
        return Qpqw2eci.dot(rPqw)
        
    def getAngMom(self):
        """
        """
        return (earth.mu_m3ps2 * self.a_m * (1 - self.e**2))**0.5
        
    def getShape(self):
        hPer_m = self.a_m * (1 - self.e) - earth.eqRad_m
        hApo_m = self.a_m * (1 + self.e) - earth.eqRad_m
        return (hPer_m, hApo_m)
        
    @staticmethod
    def fromRV(rEci_m, vEci_mps):
        """
        """
        r_m = rEci_m.dot(rEci_m)**0.5
        v_mps = vEci_mps.dot(vEci_mps)**0.5
        vr_mps = rEci_m.dot(vEci_mps) / r_m
        hEci_m2ps = numpy.cross(rEci_m, vEci_mps)
        h_m2ps = hEci_m2ps.dot(hEci_m2ps)**0.5
        i_rad = acos(hEci_m2ps[2] / h_m2ps)
        Neci = numpy.cross(numpy.array([0,0,1]), hEci_m2ps)
        N = Neci.dot(Neci)**0.5
        O_rad = acos(Neci[0] / N)
        if Neci[1] < 0:
            O_rad = 2 * pi - O_rad
        eEci = (numpy.cross(vEci_mps, hEci_m2ps) - earth.mu_m3ps2 * rEci_m / r_m) / earth.mu_m3ps2
        e = eEci.dot(eEci)**0.5
        w_rad = acos(Neci.dot(eEci) / N / e)
        if eEci[2] < 0:
            w_rad = 2 * pi - w_rad
        tht_rad = acos(eEci.dot(rEci_m) / e / r_m)
        if vr_mps < 0:
            tht_rad = 2 * pi - tht_rad
        M_rad = anomaly.true2mean(tht_rad, e)
        a_m = h_m2ps**2 / (earth.mu_m3ps2 * (1 - e**2))
        return Orbit(a_m=a_m, e=e, i_rad=i_rad, O_rad=O_rad, w_rad=w_rad, M_rad=M_rad)
