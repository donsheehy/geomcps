import unittest
from trajectories.multidimensional_scaling import *
from trajectories.point import Point
from trajectories.trajectory import Trajectory

class TestDTW(unittest.TestCase):
    def test_MDS_1(self):
        x = [[0, 0, (2.0/3.0)**0.5],
            [-3**(-0.5), 0, 0],
            [3**0.5/6, -0.5, 0],
            [3**0.5/6, 0.5, 0]]


if __name__ == '__main__':
    unittest.main()
