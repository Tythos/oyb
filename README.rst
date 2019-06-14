oyb
===

Oy vey! So many orbit models. Here's another one.

Largely based on Howard Curtis' excellent text, *Orbital Mechanics for
Engineering Students*, second edition. Contains the minimum components needed to
model and propagate restricted two-body orbits, with time values leveraging the
core Python module *datetime*.

Primary components (modules) of the package are as follows:

anomaly
-------

Defines conversions between various anomalies.

earth
-----

Defines earth parameters and key earth-specific calculations (ECF/ENU frame
conversions, latitude/longitude, GMST, etc.).

orb
---

The heart of the *oyb* package; these module contents are imported with the top
package-level *oyb* object. Contains orbital models and conversions.

plot
----

Contains various plotting methods (both main plot functions and their specific
rendering and annotation behaviors) for Orbit-derived objects in 2d (i.e.,
ground track) and 3d (i.e., orbital) plots.

rot
---

Defines vector rotation (lower case) and frame tranformations (upper case). Both
transformations can be concatenated to be performed in right-to-left upon a
given vector operator. Note that the *dot()* method must be used, since these
functions return a 2d *numpy.array* object.
