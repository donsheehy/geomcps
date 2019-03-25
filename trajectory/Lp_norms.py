def L_infty(f, g):
    return max(a.dist(b) for a,b in zip(f, g))

def L_one(f, g):
    return sum(a.dist(b) for a,b in zip(f, g))

def L_two(f, g):
    return sum(a.dist(b) ** 2 for a,b in zip(f, g))**(0.5)
