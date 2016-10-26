"""Defines vector rotation (lower case) and frame tranformations (upper case).
   Both transformations can be concatenated to be performed in right-to-left
   upon a given vector operator. Note that the *dot()* method must be used,
   since these functions return a 2d *numpy.array* object.
"""

import numpy
from math import sin, cos

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
        