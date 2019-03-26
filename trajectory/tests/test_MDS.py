import unittest
from trajectory.multidimensional_scaling import *

class TestDTW(unittest.TestCase):
    def test_MDS_1(self):
        x = Trajectory([Point([1]), Point([1])])
        self.assertEqual([[1.0, 0.0], [0.0, 1.0]], mds([x, x]))


if __name__ == '__main__':
    unittest.main()