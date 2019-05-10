import unittest
from trajectories.continuous_Lp import *
from trajectories.trajectory import Trajectory

class TestContinuous_Lp(unittest.TestCase):
    def testcontinuousLp1(self):
        t1 = Trajectory([Point([10, 3], 0), Point([9, 3], 1), Point([1, 3], 3), Point([0, 3], 4)])
        t2 = Trajectory([Point([10, 5], 1), Point([4, 5], 2), Point([2, 5], 5), Point([0, 5], 6)])
        self.assertEqual(contL_p(t1, t2, 1), 19.5)

    def testcontinuousLp2(self):
        t3 = Trajectory([Point([0, 3], 0), Point([1, 3], 1), Point([4, 3], 4)])
        t4 = Trajectory([Point([0, 1], 0), Point([2, 1], 2), Point([4, 1], 4)])
        self.assertEqual(contL_p(t3, t4, 1), 8.0)

    def testcontinuousLp3(self):
        t5 = Trajectory([Point([0, 1]), Point([1, 1]), Point([2, 1]), Point([3, 1]), Point([4, 1])])
        t6 = Trajectory([Point([0, 2]), Point([2, 2]), Point([4, 2]), Point([5, 2])])
        self.assertEqual(contL_p(t5, t6, 1), 11.0/6.0)

    def testcontinuousLp4(self):
        t5 = Trajectory([Point([0, 1], 0), Point([1, 1], 1), Point([2, 1], 2), Point([3, 1], 3), Point([4, 1], 4)])
        t6 = Trajectory([Point([0, 2], 0), Point([2, 2], 2), Point([4, 2], 4), Point([5, 2], 5)])
        self.assertEqual(contL_p(t5, t6, 1), 5.5)


if __name__ == '__main__':
    unittest.main()
