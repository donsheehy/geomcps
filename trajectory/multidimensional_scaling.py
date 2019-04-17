import numpy as np
import scipy.linalg as slinalg
from point import Point
from trajectory import Trajectory
import draw

# Input is a list of n > 1 "trajectories", a distance function/metric
# Returns a tuple with the first element being the list of eigen-values and the second being a list containing the eigen-vectors
# (both sorted in order of corresponding eigen-value) of the Gram Matrix B = -0.5 * C * D2 * C where D2 is the squared distance matrix between the "trajectories"
def gramMatrixDecomp(L1, func):
    n = len(L1)
    D2 = []
    for i in range(n):
        D2.append([])
        for j in range(n):
            if i == j:
                D2[i].append(0)
            elif i <= j:
                D2[i].append(func(L1[i], L1[j]))
            else:
                D2[i].append(D2[j][i])
    D2 = np.asarray(D2)
    C = np.identity(n) - (1./n) * np.ones((n, n))
    B = -0.5 * np.matmul(C, np.matmul(D2, C))
    ePair = np.linalg.eig(B)
    eVals = ePair[0]
    eVecs = np.matrix.transpose(ePair[1])
    sorted = [[a, b] for a, b in zip(eVals, eVecs)]
    sorted.sort(key=lambda x: x[0])
    eVals = np.asarray([x[0] for x in sorted])
    eVecs = np.asarray([x[1] for x in sorted])
    for i in range(len(eVals)):
        if eVals[i] < 10**(-10):
            eVals[i] = 0
    return (eVals, eVecs)

# Input is a list of n > 1 "trajectories", a distance function/metric and the desired output dimension
# Returns a list of points in the desired dimensioned scaled using the classical MDS algorithm
def multidimScale(L1, func, dim):
    n = len(L1)
    if dim > n:
        raise ValueError("Output Dimension Is Larger Than Trajectory List")
    ePair = gramMatrixDecomp(L1, func)
    eVals = np.ndarray.tolist(ePair[0])
    eVecs = np.ndarray.tolist(ePair[1])
    # Get rid of negative eigen-values and corresponding vectors
    for i in range(len(eVals)):
        if type(eVals[n - i - 1]) is complex or eVals[n - i - 1] < 0:
            del eVals[n-i-1]
            del eVecs[n-i-1]
    if len(eVals) < dim:
        raise ValueError("Too many complex eigenvectors")
    eValMatrix = np.identity(dim)
    eVecs = np.asarray(eVecs)
    return [Point(y[:dim]) for y in eVecs]
    # for i in range(dim):
    #     eValMatrix[i][i] = eVals[i]
    # points = np.matmul(eVecs[:,:dim], slinalg.fractional_matrix_power(eValMatrix, 0.5))
    # points = np.ndarray.tolist(points)
    # pts = [Point(y) for y in points]
    # return pts


def squareL2(f, g):
    return sum(a.dist_sq(b) for a, b in zip(f, g))

def dist(a, b):
    return abs(a-b)

def sqrDist(x, y):
    return sum((a-b)**2 for a, b in zip(x, y))

x = [[0, 0, (2.0/3.0)**0.5],
    [-3**(-0.5), 0, 0],
    [3**0.5/6, -0.5, 0], 
    [3**0.5/6, 0.5, 0]]
#draw.draw3D(x)

pts = multidimScale(x, sqrDist, 2)
tr = Trajectory(pts)
draw.draw(tr)