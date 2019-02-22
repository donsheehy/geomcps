#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from point import Point

class TestLp(unittest.TestCase):
    def test_2D_point(self):
        coords1 = [-7, -4]
        coords2 = [17, 6]
        coords3 = [3, 4]
        coords4 = [0, 0]
        p1 = Point(coords1)
        p2 = Point(coords2)
        p3 = Point(coords3)
        p4 = Point(coords4)
        self.assertEqual(p1.dist(p2), 26.0)
        self.assertEqual(p1.dist(p1), 0.0)
        self.assertEqual(p3.dist(p4), 5.0)


    def test_3D_point(self):
        coords1 = [-1, 2, 3]
        coords2 = [4, 0, -3]
        coords3 = [7, 4, 3]
        coords4 = [17, 6, 2]
        p1 = Point(coords1, 0)
        p2 = Point(coords2, 0)
        p3 = Point(coords3, 0)
        p4 = Point(coords4, 0)
        self.assertEqual(p1.dist(p2), 65 ** (0.5))
        self.assertEqual(p1.dist(p1), 0.0)
        self.assertEqual(p3.dist(p4), 105**0.5)

if __name__ == '__main__':
    unittest.main()
