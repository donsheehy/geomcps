import math
from point import Point
from trajectory import Trajectory


# The basic 1-Dimensional case of dynamic time warping used in the independent DTW function
# Can take either trajectories or lists DEPENDING ON THE GIVEN METRIC
# Takes two lists, a radius r, and a metric
# (r) represents the maximum "warp" our function can produce
# SET r = -1 for no bound on warping distance
def dtw(T1, T2, r, metric):
    table = [[] for x in range(len(T1))]
    for i in range(len(T1)):
        for j in range(len(T2)):
            temp = []
            if i > 0: temp.append(table[i-1][j])
            if j > 0: temp.append(table[i][j-1])
            if i > 0 and j > 0: temp.append(table[i-1][j-1])
            if len(temp) == 0: temp.append(0)
            table[i].append(metric(T1[i], T2[j]) + min(i for i in temp))
    # for i in range(len(table)):
    #     print(table[len(table) - i - 1])
    # print()
    i = len(T1) - 1
    j = len(T2) - 1
    sum = table[i][j]
    while i >= 0 or j >= 0:
        minVal = -1
        dec = 0
        if i > 0 and (r == -1 or abs(i-j-1)<=r):
            minVal = table[i - 1][j]
            dec = 1
        if j > 0 and (r == -1 or abs(j-i-1)<=r):
            if table[i][j - 1] < minVal or minVal == -1:
                minVal = table[i][j - 1]
                dec = 2
        if i > 0 and j > 0 and (r == -1 or abs(i-j)<=r):
            if table[i - 1][j - 1] < minVal or minVal == -1:
                minVal = table[i - 1][j - 1]
                dec = 3
        if dec == 1: i -= 1
        elif dec == 2: j -= 1
        elif dec == 3:
            i -= 1
            j -= 1
        sum += minVal
        # print(i, j, minVal)
        if i == 0 and j == 0: break
    return sum


def trajectoryToDataset(traj):
    dataset = [[] for x in range(len(traj[0]))]
    for j in range(len(traj[0])):
        for i in range(len(traj)):
            dataset[j].append(traj[i][j])
    return dataset


def metricI(a, b):
    return abs(a-b)

def metricD(p1, p2):
    return sum(metricI(a, b) for a, b in zip(p1, p2))
    # return sum(abs(a-b) for a, b in zip(p1, p2))


# This is the INDEPENDENT multi-dimensional time warp where each set of coordinates is warped independently
# Input of two trajectories which are then converted to two seperate Multi-dimensional time series (MDT)
# Each MDT is a list of m lists of size n, where m is the dimension of the points in the trajectory and n is the size of the trajectory
def dtwI(T1, T2, r = -1):
    sum = 0
    if type(T1[0]) != int:
        mdt1 = trajectoryToDataset(T1)
        mdt2 = trajectoryToDataset(T2)
        for i in range(len(mdt1)):
            sum += dtw(mdt1[i], mdt2[i], r, metricI)
    else:
        sum = dtw(T1, T2, -1, metricI)
    return sum

# Dependent version which simply passes the two trajectories to the one dimensional function with
# squared euclidean metric
def dtwD(T1, T2, r = -1):
    return dtw(T1, T2, r, metricD)