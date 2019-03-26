import numpy
from trajectory.point import Point
from trajectory.trajectory import Trajectory

# Assumed input is an array of n > 1 trajectories
# Output is then the first n points in the dimension specified (default is 2)
# The given dimension can be at most the number of given trajectories
def mds(trajs, outputDim = 2):
    n = len(trajs)
    if (outputDim > n):
        raise ValueError("Output Dimension Is Larger Than Trajectory List")
    D2 = []
    for i in range(n):
        D2.append([])
        for j in range(n):
            D2[i].append(squareL2(trajs[i], trajs[j]))
    J = []
    for i in range(n):
        J.append([])
        for j in range(n):
            if i == j:
                J[i].append(1-(1.0/n))
            else:
                J[i].append(-(1.0/n))
    res = numpy.matmul(D2, J)
    res = numpy.matmul(J, res)
    for i in range(n):
        for j in range(n):
            res[i][j] = -0.5 * res[i][j]
    eVectors = numpy.linalg.eig(res)[1].tolist()
    pCoords = []
    for i in range(n):
        pCoords.append([])
        for j in range(outputDim):
            pCoords[i].append(eVectors[i][j])
    print(pCoords)
    return pCoords


def squareL2(f, g):
    return sum(a.dist_sq(b) for a, b in zip(f, g))