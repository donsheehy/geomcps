import math

class Point:
    def __init__(self, coords, time):
        self.coords = coords
        self.t = time

    def eq_degree(self, other):
        return len(self.coords) == len(other.coords)

    def dist(self, other):
        if not self.eq_degree(other):
            return -1
        sum = 0
        for i in range(len(self.coords)):
            sum += (self.coords[i] - other.coords[i])**2
        return math.sqrt(sum)


if __name__ == '__main__':
    coords1 = [-1, 2, 3]
    coords2 = [4, 0, -3]
    p1 = Point(coords1, 0)
    p2 = Point(coords2, 0)
    print(p1.dist(p2))
