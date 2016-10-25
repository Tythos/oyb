"""
"""

import numpy
import unittest
from oyb import dynamics

class MagTests(unittest.TestCase):
    def test_one(self):
        A = numpy.array([1,2,3])
        a = dynamics.mag(A)
        self.assertTrue(abs(a - 3.741657386) / a < 1e-4)

    def test_two(self):
        A = numpy.array([1])
        a = dynamics.mag(A)
        self.assertTrue(abs(a - 1) / a < 1e-4)

    def test_three(self):
        A = numpy.array([1,-2,3,-4,5,-6])
        a = dynamics.mag(A)
        self.assertTrue(abs(a - 9.53939201) / a < 1e-4)

if __name__ == '__main__':
    unittest.main()
