import numpy as np
import matplotlib.pyplot as plt

def plot2DTraj(T):
    #x, y = zip([(p[0], p[1]) for p in T])
    x = [p[0] for p in T]
    y = [p[1] for p in T]
    plt.plot(x, y)
    plt.show()
