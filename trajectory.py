class Trajectory:
    def __init__(self, pts):
        self.pts = list(pts)

    def resample(self, n):
        pass

    def __len__(self):
        return len(self.pts)

    def dim(self):
        return len(self.pts[0])

    def duration(self):
        return self.pts[-1].t - self.pts[0].t

    def __iter__(self):
        return iter(self.pts)

    def __getitem__(self, item):
        return self.pts[item]


def L_infty(f, g):
    return max(a.dist(b) for a,b in zip(f, g))

def L_one(f, g):
    return sum(a.dist(b) for a,b in zip(f, g))

def L_two(f, g):
    return sum(a.dist(b) ** 2 for a,b in zip(f, g))**(0.5)
