from trajectory.point import Point
from trajectory.trajectory import Trajectory

# Takes two trajectories and returns a list of two trajectories such that both have the same number of points
def snipTrajectory(t1, t2):
    maxLen = max(len(t1), len(t1))
    return [Trajectory([t1[i] for i in range(maxLen)]), Trajectory([t2[i] for i in range(maxLen)])]

# Takes two (SORTED BY TIME) trajectories with points in time and then re-samples both inserting interpolated points
# to have both trajectories line up in time
def doubleTrajResample(t1, t2):
    if len(t1) > 0 and len(t2) > 0 and t1.dim() == t2.dim():
        n1 = Trajectory(t1.pts)
        n2 = Trajectory(t2.pts)
        # Ensuring start elements are the same
        if n1[0].t > n2[0].t:
            if sub1(n1, n2) is None:
                raise ValueError("Trajectories Do Not Overlap")
        elif n1[0].t < n2[0].t:
            if sub1(n2, n1) is None:
                raise ValueError("Trajectories Do Not Overlap")

        # Ensuring end times are the same
        if n1[len(n1)-1].t < n2[len(n2)-1].t:
            sub2(n1, n2)
        elif n1[len(n1)-1].t > n2[len(n2)-1].t:
            sub2(n2, n1)

        # Now cycle over next elements
        l1 = len(n1)
        l2 = len(n2)
        i = j = 1
        while i < l1-1 and j < l2-1:
            if n1[i].t < n2[j].t:
                n2.pts.insert(j, interpolateBetweenPoints(n2[j-1],n2[j], n1[i].t))
                l2 += 1
            elif n2[j].t < n1[i].t:
                n1.pts.insert(i, interpolateBetweenPoints(n1[i - 1], n1[i], n2[j].t))
                l1 += 1
            i += 1
            j += 1
        return n1, n2
    else:
        raise TypeError("Trajectories Not Valid")

# Assuming t1 start time is after t2 start time
def sub1(t1, t2):
    x = findPoint(t2, t1[0].t)
    if x is not None:
        t2.pts = t2.pts[x:]
    else:
        x = -1
        for i in range(len(t2)):
            if t2[i].t > t1[0].t:
                x = i
                break
        if x == -1:
            return None
        t2.pts = [interpolateBetweenPoints(t2[x-1], t2[x], t1[0].t)] + t2.pts[x:]
        return 1

# Assuming t1 end time is before t2 end time
def sub2(t1, t2):
    x = findPoint(t2, t1[len(t1)-1].t)
    if x is not None:
        t2.pts = t2.pts[:x+1]
    else:
        x = -1
        for i in range(len(t2)):
            if t2[i].t > t1[len(t1)-1].t:
                x = i
                break
        t2.pts = t2.pts[:x] + [interpolateBetweenPoints(t2[x-1], t2[x], t1[len(t1)-1].t)]

# given two points and a time t between p1.t and p2.t, return a new point with values through interpolation at t
def interpolateBetweenPoints(p1, p2, t):
    coords = []
    dT = p2.t - p1.t
    for i in range(len(p1)):
        slope = (p2[i] - p1[i]) / dT
        coords.append(p1[i] + slope * (t - p1.t))
    return Point(coords, t)

# Given a trajectory and a point tries to find a point with a given time
# returns index if found and returns null otherwise
# (delta can be added if you want)
def findPoint(traj, time, delta = 0):
    if delta == 0:
        for i in range(len(traj)):
            if traj[i].t == time:
                return i
        return None
    else:
        for i in range(len(traj)):
            if abs(traj[i].t - time) < delta:
                return i
        return None