import numpy as np
import scipy.linalg as slinalg
from trajectories.point import Point

# Input is a list of n > 1 "trajectories", a distance function/metric and the desired output dimension
# Returns a list of points in the desired dimensione, scaled using the classical MDS algorithm
def multidimScale(L1, func, dim):
    n = len(L1)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i <= j:
                D[i][j] = func(L1[i], L1[j])
            else:
                D[i][j] = D[j][i]
    C = np.identity(n) - (1./n) * np.ones((n, n))
    B = -0.5 * np.matmul(C, np.matmul(D, C))
    evals, evecs = np.linalg.eig(B)
    evals = np.ndarray.tolist(evals)
    evecs = np.ndarray.tolist(np.matrix.transpose(evecs))
    print(evals)
    evaltemp = []
    evectemp = []
    for i in range(len(evals)):
        if np.imag(evals[i]) == 0:
            evaltemp.append(np.real(evals[i]))
            evectemp.append(evecs[i])
    evals = evaltemp
    evecs = evectemp
    print(evals)
    zipped = sorted(zip(evals, evecs), reverse=True)[:dim]
    evals = [x[0] for x in zipped]
    evecs = np.real(np.asarray([x[1] for x in zipped]))
    for i in range(dim):
        if evals[i] >= 0:
            evecs[i] *= evals[i]**0.5
    evecs = np.matrix.transpose(evecs)
    pts = [Point(np.ndarray.tolist(x)[:dim]) for x in evecs]
    return pts
