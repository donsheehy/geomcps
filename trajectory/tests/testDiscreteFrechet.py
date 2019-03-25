import unittest

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from trajectory import Trajectory
from point import Point as point
from discreteFrechet import frechetDist

class TestDiscreteFrechet(unittest.TestCase):
    def testdiscretefrechet(self):
        L1 = [point([1,1]), point([2, 1]), point([2,2])]
        L2 = [point([2,2]), point([0,1]), point([2,4])]
        P = Trajectory(L1)
        Q = Trajectory(L1)
        R = Trajectory(L2)
        self.assertEqual(frechetDist(P, Q), 0.0)
        self.assertEqual(frechetDist(P, R), 2.0)

if __name__ == '__main__':
    unittest.main()
