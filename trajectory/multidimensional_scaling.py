import numpy
import scipy.linalg as scipy_linalg

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
    valsAndVec = numpy.linalg.eig(res)
    eVals = valsAndVec[0].tolist()
    eVecs = valsAndVec[1].tolist()
    DVals = []
    for i in range(outputDim):
        DVals.append([])
        for j in range(outputDim):
            if i == j:
                DVals[i].append(eVals[i])
            else:
                DVals[i].append(0)
    DVals = scipy_linalg.fractional_matrix_power(DVals, 0.5)
    DVecs = []
    for i in range(outputDim):
        DVecs.append([])
        for j in range(outputDim):
            DVecs[i].append(eVecs[i][j])
    coords = numpy.matmul(DVecs, DVals).tolist()
    return coords


def squareL2(f, g):
    return sum(a.dist_sq(b) for a, b in zip(f, g))