"""Defines vector rotation (lower case) and frame tranformations (upper case).
   Both transformations can be concatenated to be performed in right-to-left
   upon a given vector operator. Note that the *dot()* method must be used,
   since these functions return a 2d *numpy.array* object.
"""

import numpy
from math import sin, cos, atan2

def x(tht_rad):
    return numpy.array([
        [1, 0, 0],
        [0, cos(tht_rad), -sin(tht_rad)],
        [0, sin(tht_rad), cos(tht_rad)]])

def y(tht_rad):
    return numpy.array([
        [cos(tht_rad), 0, sin(tht_rad)],
        [0, 1, 0],
        [-sin(tht_rad), 0, cos(tht_rad)]])

def z(tht_rad):
    return numpy.array([
        [cos(tht_rad), -sin(tht_rad), 0],
        [sin(tht_rad), cos(tht_rad), 0],
        [0, 0, 1]])
        
def X(tht_rad):
    return numpy.array([
        [1, 0, 0],
        [0, cos(tht_rad), sin(tht_rad)],
        [0, -sin(tht_rad), cos(tht_rad)]])

def Y(tht_rad):
    return numpy.array([
        [cos(tht_rad), 0, -sin(tht_rad)],
        [0, 1, 0],
        [sin(tht_rad), 0, cos(tht_rad)]])

def Z(tht_rad):
    return numpy.array([
        [cos(tht_rad), sin(tht_rad), 0],
        [-sin(tht_rad), cos(tht_rad), 0],
        [0, 0, 1]])

def xyz2sph(xyz):
    xy = (xyz[0]**2 + xyz[1]**2)**0.5
    phi_rad = atan2(xyz[1], xyz[0])
    tht_rad = atan2(xyz[2], xy)
    r = (xyz[0]**2 + xyz[1]**2 + xyz[2]**2)**0.5
    return numpy.array([phi_rad, tht_rad, r])
    
def sph2xyz(sph):
    x = cos(sph[0]) * cos(sph[1])
    y = sin(sph[0]) * cos(sph[1])
    z = sin(sph[1])
    return sph[2] * numpy.array([x, y, z])
