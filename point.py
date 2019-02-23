import math

# A point in time.
class Point:
    def __init__(self, coords, time = 0):
        self.coords = coords
        self.t = time

    def eq_degree(self, other):
        return len(self) == len(other)
    
    def dist_sq(self, other):
        return sum((a-b)**2 for a,b in zip(self, other))

    def dist(self, other):
        return math.sqrt(self.dist_sq(other))
    
    def __getitem__(self, item):
        return self.coords[item]

    def __len__(self):
        return len(self.coords)

    def __iter__(self):
        return iter(self.coords)
