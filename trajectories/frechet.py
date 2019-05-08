import math
from trajectories.point import Point
from trajectories.trajectory import Trajectory


class Frechet:
    def __init__(self, traj1, traj2):
        self.P = traj1
        self.Q = traj2
        self.LF = dict()
        self.LR = dict()
        self.BF = dict()
        self.BR = dict()
        self.eps = []


# Derivative of distance from point to convex combination w.r.t. time
    def epsDot(self, p1, p2, q, t):
        x, y = [w-z for w, z in zip(p1, p2)], [m-n for m, n in zip(p2, q)]
        return 2 * (p1.dist_sq(p2)*t + dot(x, y))


# generate the type (b) critical value on left edge of cell (i,j) in [0,p]x[0,q]
    def _critL(self, i, j):
        dirv = Point([x-y for x, y in zip(self.P[i+1], self.P[i])])
        mag = math.sqrt(dot(dirv, dirv))
        n = Point([x / mag for x in dirv])
        qp = Point([w-z for w,z in zip(self.P[i], self.Q[j])])
        c = dot(n, qp)
        v = Point([c * x for x in n])
        return qp.dist_sq(v)


# generate the type (b) critical value on bottom edge of cell (i,j) in [0,p]x[0,q]
    def _critB(self, i, j):
        dirv = Point([x - y for x, y in zip(self.Q[j + 1], self.Q[j])])
        mag = math.sqrt(dot(dirv, dirv))
        n = Point([x / mag for x in dirv])
        qp = Point([w - z for w, z in zip(self.Q[j], self.P[i])])
        c = dot(n, qp)
        v = Point([c * x for x in n])
        return qp.dist_sq(v)

# generate the type (c) critical value on equal a_kj and b_lj
    def _critCP(self, k, l):
        p = Point([0.5 * x + 0.5 * y for x, y in zip(self.P[k], self.P[l])])
        n = Point([y - x for x, y in zip(self.P[k], self.P[l])])
        d = dict()
        B = getBasis(p, n)
        for x in range(len(self.Q) - 1):
            M, M2 = getMatrix(B, self.Q[x]), getMatrix(B, self.Q[x+1])
            d1, d2 = getMatrixDeterminant(M), getMatrixDeterminant(M2)
            #print(d1, d2)
            if d1 * d2 <= 0:
                d1, d2 = abs(d1), abs(d2)
                if d1 - d2 == 0:
                    q = Point([0.5 * x + 0.5 * y for x, y in zip(self.Q[x], self.Q[x+1])])
                else:
                    q = Point([(d2 * x + d1 * y)/(d1 + d2) for x, y in zip(self.Q[x], self.Q[x+1])])
                d[x] = q.dist_sq(self.P[k])
        return d

    def _critCQ(self, k, l):
        p = Point([0.5 * x + 0.5 * y for x, y in zip(self.Q[k], self.Q[l])])
        n = Point([y - x for x, y in zip(self.Q[k], self.Q[l])])
        d = dict()
        B = getBasis(p, n)
        for x in range(len(self.P) - 1):
            M, M2 = getMatrix(B, self.P[x]), getMatrix(B, self.P[x+1])
            d1, d2 = getMatrixDeterminant(M), getMatrixDeterminant(M2)
            if d1 * d2 <= 0:
                d1, d2 = abs(d1), abs(d2)
                if d1 - d2 == 0:
                    q = Point([0.5 * x + 0.5 * y for x, y in zip(self.P[x], self.P[x+1])])
                else:
                    q = Point([(d2 * x + d1 * y)/(d1 + d2) for x, y in zip(self.P[x], self.P[x+1])])
                d[x] = q.dist_sq(self.Q[k])
        return d


# compute all critical values and store them in self.eps [type (a) and (b)]
    def _generateCrits(self):
        s = set()
        for i in range(len(self.P) - 1):
            for j in range(len(self.Q) - 1):
                s.add(self._critL(i, j))
                s.add(self._critB(i, j))
        for k in range(len(self.P)):
            for l in range(len(self.P)):
                d = self._critCP(k, l)
                for key, value in d.items():
                    s.add(value)
        for k in range(k+1, len(self.Q)):
            for l in range(k+1, len(self.Q)):
                d = self._critCQ(k, l)
                for key, value in d.items():
                    s.add(value)
        s.add(self.P[0].dist_sq(self.Q[0]))
        s.add(self.P[len(self.P) - 1].dist_sq(self.Q[len(self.Q) - 1]))
        self.eps = list(s)
        self.eps.sort()


# helper function to edit left or bottom value of interval
    def _editLB(self, value, loop, d, epsilon, prime):
        v = value
        if d > epsilon:
            if prime < 0:
                v += 0.5 ** loop
            else:
                v -= 0.5 ** loop
        else:
            v -= 0.5 ** loop
        return v


# helper function to edit right or top value of interval
    def _editRT(self, value, loop, d, epsilon, prime):
        v = value
        if d > epsilon:
            if prime < 0:
                v += 0.5 ** loop
            else:
                v -= 0.5 ** loop
        else:
            v += 0.5 ** loop
        return v


# interval of convex combinations of P[i] and P[i+1] w/ distance at most epsilon from Q[j]
# if there is no such point, return [2,2]
    def _BF_ij(self, i, j, epsilon):
        left, right = 0, 1
        lp = Point([left * x + (1-left) * y for x, y in zip(self.P[i+1], self.P[i])])
        rp = Point([right * x + (1-right) * y for x, y in zip(self.P[i+1], self.P[i])])
        d, loop = lp.dist_sq(self.Q[j]), 1
        prime = self.epsDot(self.P[i+1], self.P[i], self.Q[j], left)
        while d != epsilon and loop < 52:
            if d < epsilon and left == 0:
                loop = 52
            else:
                left = self._editLB(left, loop, d, epsilon, prime)
            loop += 1
            lp = Point([left * x + (1 - left) * y for x, y in zip(self.P[i + 1], self.P[i])])
            prime = self.epsDot(self.P[i + 1], self.P[i], self.Q[j], left)
            d = lp.dist_sq(self.Q[j])
        if abs(d - epsilon) > 0.00000000002 and left != 0:
            left = 2
        d, loop = rp.dist_sq(self.Q[j]), 1
        prime = self.epsDot(self.P[i + 1], self.P[i], self.Q[j], right)
        while d != epsilon and loop < 52:
            if d < epsilon and right == 1:
                loop = 52
            else:
                right = self._editRT(right, loop, d, epsilon, prime)
            loop += 1
            rp = Point([right * x + (1-right) * y for x,y in zip(self.P[i+1], self.P[i])])
            prime = self.epsDot(self.P[i + 1], self.P[i], self.Q[j], right)
            d = rp.dist_sq(self.Q[j])
        if abs(d - epsilon) > 0.00000000002 and right != 1:
            right = 2
        return (left, right)


# interval of convex combinations of Q[j] and Q[j+1] w/ distance at most epsilon from P[i]
# if there is no such point, return [2,2]
    def _LF_ij(self, i, j, epsilon):
        bottom, top = 0, 1
        bp = Point([bottom * x + (1 - bottom) * y for x, y in zip(self.Q[j + 1], self.Q[j])])
        tp = Point([top * x + (1 - top) * y for x, y in zip(self.Q[j + 1], self.Q[j])])
        d, loop = bp.dist_sq(self.P[i]), 1
        prime = self.epsDot(self.Q[j + 1], self.Q[j], self.P[i], bottom)
        while d != epsilon and loop < 52:
            if d < epsilon and bottom == 0:
                loop = 52
            else:
                bottom = self._editLB(bottom, loop, d, epsilon, prime)
            loop += 1
            bp = Point([bottom * x + (1 - bottom) * y for x, y in zip(self.Q[j + 1], self.Q[j])])
            prime = self.epsDot(self.Q[j + 1], self.Q[j], self.P[i], bottom)
            d = bp.dist_sq(self.P[i])
        if abs(d - epsilon) > 0.00000000002 and bottom != 0:
            bottom = 2
        d, loop = tp.dist_sq(self.P[i]), 1
        prime = self.epsDot(self.Q[j + 1], self.Q[j], self.P[i], top)
        while d != epsilon and loop < 52:
            if d < epsilon and top == 1:
                loop = 52
            else:
                top = self._editRT(top, loop, d, epsilon, prime)
            loop += 1
            tp = Point([top * x + (1 - top) * y for x, y in zip(self.Q[j + 1], self.Q[j])])
            prime = self.epsDot(self.Q[j + 1], self.Q[j], self.P[i], top)
            d = tp.dist_sq(self.P[i])
        if abs(d - epsilon) > 0.00000000002 and top != 1:
            top = 2
        return (bottom, top)


# Compute all LF and BF intervals for all critical values epsilon
    def _LFBF_eps_gen(self, epsilon):
        self.LF[epsilon] = dict()
        self.BF[epsilon] = dict()
        for i in range(len(self.P) - 1):
            for j in range(len(self.Q) - 1):
                self.LF[epsilon][(i, j)] = self._LF_ij(i, j, epsilon)
                self.BF[epsilon][(i, j)] = self._BF_ij(i, j, epsilon)
        for j in range(len(self.Q) - 1):
            self.LF[epsilon][(len(self.P) - 1, j)] = self._LF_ij(len(self.P) - 1, j, epsilon)
        for i in range(len(self.P) - 1):
            self.BF[epsilon][(i, len(self.Q) - 1)] = self._BF_ij(i, len(self.Q) - 1, epsilon)


# Return reachable points from (0,0) with monotone curve on left interval ij
    def _LR_ij(self, i, j, epsilon):
        if i == 0 and j == 0:
            if self.LF[epsilon][(0, 0)][0] == 0:
                return self.LF[epsilon][(0, 0)]
            return (2, 2)
        elif i == 0:
            Lbelow = self.LR[epsilon][(i, j-1)]
            if Lbelow[1] == 1 and self.LF[epsilon][(0, j)][0] == 0:
                return self.LF[epsilon][(0, j)]
            return (2, 2)
        prevL = self.LR[epsilon][(i - 1, j)]
        prevB = self.BR[epsilon][(i - 1, j)]
        if prevB != (2, 2):
            return self.LF[epsilon][(i, j)]
        elif prevL[0] > self.LF[epsilon][(i, j)][1]:
            return (2, 2)
        elif prevL[0] > self.LF[epsilon][(i, j)][0]:
            return (prevL[0], self.LF[epsilon][(i, j)][1])
        return self.LF[epsilon][(i, j)]


# Return reachable points from (0,0) with monotone curve on bottom interval ij
    def _BR_ij(self, i, j, epsilon):
        if i == 0 and j == 0:
            if self.BF[epsilon][(i, j)][0] == 0:
                return self.BF[epsilon][(i, j)]
            return (2, 2)
        elif j == 0:
            Bleft = self.BR[epsilon][(i-1, j)]
            if Bleft[1] == 1 and self.BF[epsilon][(i, 0)][0] == 0:
                return self.BF[epsilon][(i, 0)]
            return (2, 2)
        prevB = self.BR[epsilon][(i, j - 1)]
        prevL = self.LR[epsilon][(i, j - 1)]
        if prevL != (2,2):
            return self.BF[epsilon][(i, j)]
        elif prevB[0] > self.BF[epsilon][(i, j)][1]:
            return (2,2)
        elif prevB[0] > self.BF[epsilon][(i, j)][0]:
            return (prevB[0], self.BF[epsilon][(i, j)][0])
        return self.BF[epsilon][(i, j)]


# generate intervals of each left and bottom line segment reachable from (0,0) for each critical value epsilon
    def _LRBR_eps_gen(self, epsilon):
        self.LR[epsilon] = dict()
        self.BR[epsilon] = dict()
        for i in range(len(self.P) - 1):
            for j in range(len(self.Q) - 1):
                self.LR[epsilon][(i, j)] = self._LR_ij(i, j, epsilon)
                self.BR[epsilon][(i, j)] = self._BR_ij(i, j, epsilon)
        for j in range(len(self.Q) - 1):
            self.LR[epsilon][(len(self.P) - 1, j)] = self._LR_ij(len(self.P) - 1, j, epsilon)
        for i in range(len(self.P) - 1):
            self.BR[epsilon][(i, len(self.Q) - 1)] = self._BR_ij(i, len(self.Q) - 1, epsilon)


# Compute Frechet distance using above functions
    def dist(self):
        self._generateCrits()
        left, right, e = 0, len(self.eps) - 1, self.eps[0]
        while left != right:
            mid = math.ceil((left+right)/2)
            e = self.eps[mid]
            self._LFBF_eps_gen(e)
            self._LRBR_eps_gen(e)
            if self.LR[e][(len(self.P)-1, len(self.Q)-2)][1] == 1 or self.BR[e][(len(self.P)-2, len(self.Q)-1)][1] == 1:
                right = mid - 1
            else:
                left = mid

        if left != mid:
            e1 = self.eps[left]
            self._LFBF_eps_gen(e1)
            self._LRBR_eps_gen(e1)
            if self.LR[e1][(len(self.P)-1, len(self.Q)-2)][1] == 1 or self.BR[e1][(len(self.P)-2, len(self.Q)-1)][1] == 1:
                return math.sqrt(self.eps[left])
        return math.sqrt(e)

#------------------------------------------------END OF FRECHET CLASS---------------------------------------------------


# standard dot product
def dot(p, q):
    return sum(x*y for x, y in zip(p, q))


# returns d defining points of the d-1 dimensional subspace
def getBasis(origin, normal):
    d, temp = [tuple(origin)], dict()
    l = []
    for i in range(len(normal)):
        l.append(0)
    for x in range(1, len(normal)):
        l[0], l[x] = -1 * normal[x], normal[0]
        temp[x] = tuple(l)
        l[0], l[x] = 0, 0
    for k, v in temp.items():
        d.append(tuple([x + y for x, y in zip(v, origin)]))
    return tuple(d)


# returns d+1 dimensional matrix for orientation test
def getMatrix(basis, pt):
    l = [list(x) for x in basis]
    for x in l:
        x.append(1)
    p = list(pt)
    p.append(1)
    l.append(p)
    M1 = [tuple(x) for x in l]
    M = tuple(M1)
    return tuple(zip(*M))


# helper for computing determinant
def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


# compute determinant of matrix m, assuming m is square (only used for type (c) critical values)
def getMatrixDeterminant(m):
    if len(m) == 1:
        return m[0][0]
    elif len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeterminant(getMatrixMinor(m,0,c))
    return determinant
