import unittest
from trajectories.trajectory import Trajectory
from trajectories.point import Point
from trajectories.discreteFrechet import frechetDist

class TestDiscreteFrechet(unittest.TestCase):
    def testdiscretefrechet(self):
        L1 = [Point([1,1]), Point([2, 1]), Point([2,2])]
        L2 = [Point([2,2]), Point([0,1]), Point([2,4])]
        P = Trajectory(L1)
        Q = Trajectory(L1)
        R = Trajectory(L2)
        self.assertEqual(frechetDist(P, Q), 0.0)
        self.assertEqual(frechetDist(P, R), 2.0)

if __name__ == '__main__':
    unittest.main()
