import unittest
from trajectory.point import Point
from trajectory.trajectory import Trajectory

class TestLp(unittest.TestCase):
    def testL_one_simple(self):
        a = Trajectory([Point((1,2))])
        b = Trajectory([Point((5,5))])


if __name__ == '__main__':
    unittest.main()
