import unittest
from trajectory.multidimensional_scaling import *
from trajectory.point import Point
from trajectory.trajectory import Trajectory

class TestDTW(unittest.TestCase):
    def test_MDS_1(self):
        x = Trajectory([Point([1]), Point([1])])
        y = Trajectory([Point([1]), Point([2])])
        self.assertEqual([[0.0, 0.0], [0.0, 0.0]], mds([x, x]))
        self.assertEqual([[0.5, 0.0], [-0.5, 0.0]], mds([x, y]))


if __name__ == '__main__':
    unittest.main()