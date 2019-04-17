import unittest
from trajectory.multidimensional_scaling import *
from trajectory.point import Point
from trajectory.trajectory import Trajectory

class TestDTW(unittest.TestCase):
    def test_MDS_1(self):
        x = [[0, 0, (2.0/3.0)**0.5],
            [-3**(-0.5), 0, 0],
            [3**0.5/6, -0.5, 0], 
            [3**0.5/6, 0.5, 0]]
        # draw.draw3D(x)
        # pts = multidimScale(x, sqrDist, 2)
        # tr = Trajectory(pts)
        # draw.draw(tr)


if __name__ == '__main__':
    unittest.main()