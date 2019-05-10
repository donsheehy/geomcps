import math
from trajectories.trajectory import Trajectory
from trajectories.point import Point


def contL_p(P, Q, p):
    P0 = P[0].t
    for x in range(len(P)):
        if P[x].t == 0:
            P[x].t = x / (len(P)-1)
        else:
            P[x].t = P[x].t - P0
    Q0 = Q[0].t
    for y in range(len(Q)):
        if Q[y].t == 0:
            Q[y].t = y / (len(Q)-1)
        else:
            Q[y].t = Q[y].t - Q0
    i, j, prev, total = 0, 0, 0, 0
    mark = 0
    if P[-1].t < Q[-1].t:
        P.pts.append(Point(P[-1].coords, Q[-1].t))
        mark = 1
    elif Q[-1].t < P[-1].t:
        Q.pts.append(Point(Q[-1].coords, P[-1].t))
        mark = 2
    while i < len(P) - 1 or j < len(Q) - 1:
        if P[i+1].t < Q[j+1].t:
            for k in range(len(P[i+1])):
                fdir, gdir = (P[i+1][k] - P[i][k])/(P[i+1].t - P[i].t), (Q[j+1][k] - Q[j][k])/(Q[j+1].t - Q[j].t)
                fstart, gstart = P[i][k] - P[i].t * fdir, Q[j][k] - Q[j].t * gdir
                b = fstart - gstart
                a = fdir - gdir
                if p % 2 == 0:
                    total += _integral_p(prev, P[i+1].t, p, a, b)
                elif a != 0 and prev < (0 - b)/a < P[i+1].t:
                    if a * prev + b < 0:
                        total += _integral_p((0 - b)/a, prev, p, a, b) + _integral_p((0 - b)/a, P[i+1].t, p, a, b)
                    else:
                        total += _integral_p(prev, (0 - b)/a, p, a, b) + _integral_p(P[i+1].t, (0 - b)/a, p, a, b)
                else:
                    if a * (prev + P[i+1].t)/2 + b > 0:
                        total += _integral_p(prev, P[i+1].t, p, a, b)
                    else:
                        total += _integral_p(P[i+1].t, prev, p, a, b)
            prev = P[i+1].t
            i += 1
        else:
            for k in range(len(Q[j+1])):
                fdir, gdir = (P[i+1][k] - P[i][k])/(P[i+1].t - P[i].t), (Q[j+1][k] - Q[j][k])/(Q[j+1].t - Q[j].t)
                fstart, gstart = P[i][k] - P[i].t * fdir, Q[j][k] - Q[j].t * gdir
                b = fstart - gstart
                a = fdir - gdir
                if p % 2 == 0:
                    total += _integral_p(prev, Q[j+1].t, p, a, b)
                elif a != 0 and prev < (0 - b)/a < Q[j+1].t:
                    if a * prev + b < 0:
                        total += _integral_p((0 - b)/a, prev, p, a, b) + _integral_p((0 - b)/a, Q[j+1].t, p, a, b)
                    else:
                        total += _integral_p(prev, (0 - b)/a, p, a, b) + _integral_p(Q[j+1].t, (0 - b)/a, p, a, b)
                else:
                    if a * (prev + Q[j+1].t)/2 + b > 0:
                        total += _integral_p(prev, Q[j+1].t, p, a, b)
                    else:
                        total += _integral_p(Q[j+1].t, prev, p, a, b)
            prev = Q[j+1].t
            if P[i+1].t == Q[j+1].t:
                i += 1
            j += 1
    if mark == 1:
        P.pts.pop()
    elif mark == 2:
        Q.pts.pop()
    if P0 != 0:
        for x in range(len(P)):
            P[x].t += P0
    if Q0 != 0:
        for y in range(len(Q)):
            Q[y].t += Q0
    return total ** (1/p)


def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))


def _integral_p(lower, upper, p, a, b):
    return sum(nCr(p, k) * (a ** k) * (b ** (p-k)) * (upper ** (k+1) - lower ** (k+1)) / (k+1) for k in range(p+1))
