class Pos:
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []

class Walker:
    def __init__(self):
        self.times = []
        self.pos = Pos()

    def add_point(self,li):
        self.times.append(li[0])
        self.pos.x.append(li[1])
        self.pos.y.append(li[2])
        self.pos.z.append(li[3])

