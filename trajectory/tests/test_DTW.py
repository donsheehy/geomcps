import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from point import Point
from trajectory import Trajectory
from dynamic_time_warper import *

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


# class TestLp(unittest.TestCase):
#     def test_2D_point(self):
#         coords1 = [-7, -4]
#         coords2 = [17, 6]
#         coords3 = [3, 4]
#         coords4 = [0, 0]
#         p1 = Point(coords1)
#         p2 = Point(coords2)
#         p3 = Point(coords3)
#         p4 = Point(coords4)
#         self.assertEqual(p1.dist(p2), 26.0)
#         self.assertEqual(p1.dist(p1), 0.0)
#         self.assertEqual(p3.dist(p4), 5.0)
#
#
#     def test_3D_point(self):
#         coords1 = [-1, 2, 3]
#         coords2 = [4, 0, -3]
#         coords3 = [7, 4, 3]
#         coords4 = [17, 6, 2]
#         p1 = Point(coords1, 0)
#         p2 = Point(coords2, 0)
#         p3 = Point(coords3, 0)
#         p4 = Point(coords4, 0)
#         self.assertEqual(p1.dist(p2), 65 ** (0.5))
#         self.assertEqual(p1.dist(p1), 0.0)
#         self.assertEqual(p3.dist(p4), 105**0.5)

if __name__ == '__main__':
    unittest.main()
