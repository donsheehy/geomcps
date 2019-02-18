import math

# A point in time.
class Point:
    def __init__(self, coords, time = 0):
        self.coords = coords
        self.t = time

    def eq_degree(self, other):
        return len(self) == len(other)

    def dist(self, other):
        return math.sqrt(sum((a-b)**2 for a,b in zip(self, other)))

    def __len__(self):
        return len(self.coords)

    def __iter__(self):
        return iter(self.coords)


if __name__ == '__main__':
    coords1 = [-1, 2, 3]
    coords2 = [4, 0, -3]
    p1 = Point(coords1, 0)
    p2 = Point(coords2, 0)
    print(p1.dist(p2))

    print(list(zip(p1,p2)))
