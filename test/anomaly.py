"""
"""

import unittest
from math import pi
from oyb import anomaly

class MeanToTrue(unittest.TestCase):
    def test_example3p2(self):
        tht_rad = anomaly.mean2true(3.6029, 0.37255)
        tht_deg = (tht_rad * 180 / pi) % 360
        self.assertTrue(abs(tht_deg - 193.2) < 1e-1)

    def test_example3p2_inv(self):
        M_rad = anomaly.true2mean(193.2 * pi / 180, 0.37255)
        self.assertTrue(abs((M_rad % (2 * pi)) - 3.6029) < 1e-1)
        
if __name__ == '__main__':
    unittest.main()
