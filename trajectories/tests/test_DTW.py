import unittest
from trajectories.dynamic_time_warper import *
from trajectories.trajectory import Trajectory
from trajectories.point import Point

class TestDTW(unittest.TestCase):
    def test_1D_DTW(self):
        t1 = [1,2,2,10,2,1]
        t2 = [3,3,5,5,2]
        self.assertEqual(45, dtw(t1, t2, -1, metricI))
        self.assertEqual(0, dtw(t1, t1, -1, metricI))
        t1 = Trajectory([Point([1]),Point([2]),Point([2]),Point([10]),Point([2]),Point([1])])
        t2 = Trajectory([Point([3]),Point([3]),Point([5]),Point([5]),Point([2])])
        self.assertEqual(45, dtw(t1, t2, -1, metricD))
        self.assertEqual(0, dtw(t1, t1, -1, metricD))

    def test_DTWI(self):
        p1 = Point([-7, -4])
        p2 = Point([5, 6])
        p3 = Point([3, 4])
        p4 = Point([-3, 5])
        t1 = Trajectory([p1, p2])
        t2 = Trajectory([p3, p4])
        self.assertEqual(45, dtwI(t1, t2))
        t1 = Trajectory([p1, p2, p3, p4])
        self.assertEqual(0, dtwI(t1, t1))

    def test_ITWD(self):
        p1 = Point([-7, -4])
        p2 = Point([5, 6])
        p3 = Point([3, 4])
        p4 = Point([-3, 5])
        t1 = Trajectory([p1, p2])
        t2 = Trajectory([p3, p4])
        self.assertEqual(45, dtwD(t1, t2))
        t1 = Trajectory([p1, p2, p3, p4])
        self.assertEqual(0, dtwD(t1, t1))

if __name__ == '__main__':
    unittest.main()
