import unittest
from trajectories.frechet import *


class TestFrechet(unittest.TestCase):
    def testfrechetline(self):
        t1 = Trajectory([Point([10, 3]), Point([9, 3]), Point([1, 3]), Point([0, 3])])
        t2 = Trajectory([Point([10, 5]), Point([4, 5]), Point([2, 5]), Point([0, 5])])
        f1 = Frechet(t1, t2)
        self.assertEqual(f1.dist(), 2.0)

    def testfrechetbox(self):
        tin1, tin2 = [], []
        for x in range(2):
            tin1.append(Point([x % 2, x % 2]))
            tin1.append(Point([(x + 1) % 2, x % 2]))
            tin2.append(Point([x % 2, x % 2]))
            tin2.append(Point([(x + 1) % 2, x % 2]))
        for x in range(2, 4):
            tin1.append(Point([x % 2, x % 2]))
            tin1.append(Point([(x + 1) % 2, x % 2]))
        tin1.append(Point([0, 0]))
        tin2.append(Point([0, 0]))
        t1, t2 = Trajectory(tin1), Trajectory(tin2)
        f2 = Frechet(t1, t2)
        self.assertEqual(f2.dist(), (5 ** 0.5)/2)


if __name__ == '__main__':
    unittest.main()
