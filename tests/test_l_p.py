import unittest
from point import Point
from trajectory import Trajectory, L_one

class TestLp(unittest.TestCase):
    def testL_one_simple(self):
        a = Trajectory([Point((1,2))])
        b = Trajectory([Point((5,5))])
        self.assertEqual(L_one(a, b), 5)


if __name__ == '__main__':
    unittest.main()
