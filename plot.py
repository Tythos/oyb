"""
"""

import numpy
from mpl_toolkits import mplot3d
from matplotlib import pyplot, image
from oyb import earth, data

def plot2d(o, hx=None):
    """
    """
    if hx is None:
        hf = pyplot.figure()
        hx = hf.add_subplot(111)
        plotEarthSurf(hx)
        annotateEarthSurf(hx)
    return hx
        
def plotEarthSurf(hx):
    """
    """
    img = image.imread(data.get_path('blueMarble.png'))
    hx.imshow(img, aspect='equal', origin='upper', extent=(-180,180,-90,90), alpha=0.2)
    
def annotateEarthSurf(hx):
    """
    """
    hx.set_xlabel('Longitude [deg]')
    hx.set_ylabel('Latitude [deg]')
    
def plot3d(o, hx=None):
    """
    """
    r = 1e-3 * o.propagate()
    if hx is None:
        hf = pyplot.figure()
        hx = hf.add_subplot(111, projection='3d')
        hx.plot(r[:,0], r[:,1], r[:,2])
        plotEarthSphere(hx)
        annotateEarthSphere(hx)
    lim = (
        min(min(r[:,0]), min(r[:,1]), min(r[:,2])),
        max(max(r[:,0]), max(r[:,1]), max(r[:,2])) )
    hx.plot([0,lim[0]], [0,0], [0,0], c=(0.6,0.6,0.6,0.2))
    hx.plot([0,lim[1]], [0,0], [0,0], c=(1.0,0.0,0.0,0.2))
    hx.plot([0,0], [0,lim[0]], [0,0], c=(0.6,0.6,0.6,0.2))
    hx.plot([0,0], [0,lim[1]], [0,0], c=(0.0,1.0,0.0,0.2))
    hx.plot([0,0], [0,0], [0,lim[0]], c=(0.6,0.6,0.6,0.2))
    hx.plot([0,0], [0,0], [0,lim[1]], c=(0.0,0.0,1.0,0.2))
    return hx

def plotEarthSphere(hx):
    """
    """
    u, v = numpy.mgrid[0:2*numpy.pi:20j, 0:numpy.pi:10j]
    x = numpy.cos(u) * numpy.sin(v)
    y = numpy.sin(u) * numpy.sin(v)
    z = numpy.cos(v)
    r = 1e-3 * earth.eqRad_m
    hx.plot_wireframe(r * x, r * y, r * z, color=(0.5,0.5,0.5,0.5))

def annotateEarthSphere(hx):
    """
    """
    hx.set_xlabel('X ECI [km]')
    hx.set_ylabel('Y ECI [km]')
    hx.set_zlabel('Z ECI [km]')
