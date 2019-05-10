import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
from trajectories.trajectory import *

# Plots an any number of trajectories inputted in a 2D plane
def draw(*args):
	count = 0
	if type(args[0]) == Trajectory:
		for T in args:
			c = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
			x = [p[0] for p in T] # list of x coordinates
			y = [p[1] for p in T] # list of y coordinates
			plt.plot(x, y, label = "T" + str(count), color = c )
			plt.scatter(x,y, color = c)
			count += 1
		plt.legend()
		plt.show()
	else:
		arg2 = []
		for x in args:
			arg2.extend(tuple(x))
		draw(*arg2)

def draw3D(*args):
	count = 0
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d', aspect='equal')
	for T in args:
		c = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
		x = [p[0] for p in T] # list of x coordinates
		y = [p[1] for p in T] # list of y coordinates
		z = [p[2] for p in T] # list of z coordinates
		ax.plot(x, y, z, label = "Traj_" + str(count), color = c )
		ax.scatter(x,y,z, color = c)
		count += 1
	plt.legend()
	plt.show()
