import trajectory.trajectory as trajectory
# import trajectory


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
            sample_list = self._data_samples[sample]  # sample object
            for instance in sample_list:
                # data = sample_obj[instance]
                trajectories.append(instance.make_trajectory())
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

    def make_trajectory(self):
        pts = []
        for pt in self._instances:
            instance = self._instances[pt]
            pts.append(instance.get_data())
        return trajectory.Trajectory(pts)


class DataInstance:

    def __init__(self, dataSample):
        '''
        Takes a data sample object as input
        Initialize Data Instance object. Declare class-wide variables.
        '''
        self._instanceOf = dataSample   # keep track of what data this is
        self._data = []   # list of data

    def add_point(self, data):
        self._data.append(data)

    def get_data(self):
        return self._data

    def get_instance_of(self):
        return self._instanceOf
