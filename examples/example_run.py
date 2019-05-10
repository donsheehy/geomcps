import os
from trajectories.point import *
from trajectories.trajectory import *
from trajectories.dataprocessor import *
from trajectories.Lp_norms import *
from trajectories.draw import *
from trajectories.continuous_Lp import *
from trajectories.discreteFrechet import *
from trajectories.dynamic_time_warper import *
from trajectories.frechet import *
from trajectories.multidimensional_scaling import *


directory = os.path.join(os.getcwd(), 'example_data')
dp = DataProcessor(directory)

z = dp.make_set_of_trajectories()

draw(z)

'''
z is meant to test the dataprocessor. The resulting object stored in z is a list of lists of trajectories
'''



y = []
y.append(Trajectory([Point([10, 3], 0), Point([9, 3], 1), Point([1, 3], 3), Point([0, 3], 4)]))
y.append(Trajectory([Point([10, 5], 1), Point([4, 5], 2), Point([2, 5], 5), Point([0, 5], 6)]))
y.append(Trajectory([Point([0, 3], 0), Point([1, 3], 1), Point([4, 3], 4)]))
y.append(Trajectory([Point([0, 1], 0), Point([2, 1], 2), Point([4, 1], 4)]))
y.append(Trajectory([Point([0, 1], 0), Point([1, 1], 1), Point([2, 1], 2), Point([3, 1], 3), Point([4, 1], 4)]))
y.append(Trajectory([Point([0, 2], 0), Point([2, 2], 2), Point([4, 2], 4), Point([5, 2], 5)]))

tin1, tin2 = [], []
for x in range(2):
    tin1.append(Point([x % 2, x % 2]))
    tin1.append(Point([(x + 1) % 2, x % 2]))
    tin2.append(Point([x % 2, x % 2]))
    tin2.append(Point([(x + 1) % 2, x % 2]))
for x in range(2, 4):
    tin1.append(Point([x % 2, x % 2]))
    tin1.append(Point([(x + 1) % 2, x % 2]))
tin1.append(Point([0, 0]))
tin2.append(Point([0, 0]))
t1, t2 = Trajectory(tin1), Trajectory(tin2)
y.append(t1)
y.append(t2)

L1 = [Point([1,1]), Point([2, 1]), Point([2,2])]
L2 = [Point([2,2]), Point([0,1]), Point([2,4])]
y.append(Trajectory(L1))
y.append(Trajectory(L2))
draw(y)


for j in range(len(z)):
    for i in range(j):
        traj1, traj2 = z[i][0], z[j][0]
        print('z(', i, ',', j, ')')
        F = Frechet(traj1, traj2)
        for k in range(15):
            print('Continuous L_' + str(k+1) + ': ', contL_p(traj1, traj2, k+1))
        print('Discrete Frechet: ', frechetDist(traj1, traj2))
        print('Continuous Frechet: ', F.dist())
        print('\n\n')


for j in range(len(y)):
    for i in range(j):
        print('y(', i, ',', j, ')')
        F = Frechet(y[i], y[j])
        for k in range(15):
            print('Continuous L_' + str(k+1) + ': ', contL_p(y[i], y[j], 1))
        print('Discrete Frechet: ', frechetDist(y[i], y[j]))
        print('Continuous Frechet: ', F.dist())
        print('\n\n')
