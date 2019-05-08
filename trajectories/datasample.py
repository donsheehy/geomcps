# import trajectory.trajectory as trajectory
# from trajectory.point import Point
# import trajectory
import trajectories.trajectory as trajectory
from trajectories.point import Point


class DataSamples:

    def __init__(self):
        '''
        Initialize Data Samples object. Declare class-wide variables.
        '''
        self._data_samples = {}   # dict of data samples

    def initDataSamples(self, name):
        '''create new data samples object; list of length 1'''
        ds = DataSample(name)
        self._data_samples.update({name: [ds]})
        return ds

    def newDataSample(self, name):
        '''
        Add new Data Sample objects.
        '''
        ds = DataSample(name)
        toUpdate = self._data_samples[name]
        toUpdate.append(ds)
        self._data_samples.update({name: toUpdate})
        return ds

    def get_data_samples(self):
        '''
        Return data samples list to outside functions
        '''
        return self._data_samples

    def make_trajectories(self):
        trajectories = []
        for sample in self._data_samples:
            runList = self._data_samples[sample]  # sample object
            # trajectories.append(runList.make_sample_trajectories())
            for runs in runList:
                # data = sample_obj[instance]
                trajectories.append(runs.make_sample_trajectories())
        return trajectories


class DataSample:

    def __init__(self, name):
        '''
        Initialize Data Sample objects. Declare class-wide variables.
        '''
        self._name = name
        self._instances = {}

    def add_instance(self, instance_name):
        newInstance = DataInstance(self)
        self._instances.update({instance_name: newInstance})
        return newInstance

    def get_instances(self):
        return self._instances

    def make_sample_trajectories(self):
        trajs = []
        for run in self._instances:
            instance = self._instances[run]
            # traj = trajectory.Trajectory(instance.get_points())
            traj = instance.make_single_traj()
            trajs.append(traj)
        return trajs


class DataInstance:

    def __init__(self, dataSample):
        '''
        Takes a data sample object as input
        Initialize Data Instance object. Declare class-wide variables.
        '''
        self._instanceOf = dataSample   # keep track of what data this is
        self._data = []   # list of data
        self._points = []  # list of point objects

    def add_point(self, data):
        self.make_pt_obj(data)
        self._data.append(data)

    def make_pt_obj(self, data):
        pt = Point(data[1:], data[0])
        self._points.append(pt)

    def get_points(self):
        return self._points

    def get_data(self):
        return self._data

    def get_instance_of(self):
        return self._instanceOf

    def make_single_traj(self):
        return trajectory.Trajectory(self._points)
