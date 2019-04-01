import numpy as np
import matplotlib.pyplot as plt
import random

# Plots an any number of trajectories inputted in a 2D plane
def draw(*args):
    count = 0
    for T in args:
        c = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        x = [p[0] for p in T] # list of x coordinates
        y = [p[1] for p in T] # list of y coordinates
        plt.plot(x, y, label = "T" + str(count), color = c )
        plt.scatter(x,y, color = c)
        count += 1
    plt.legend()
    plt.show()
