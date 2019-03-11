class DataSamples:

    def __init__(self):
        '''
        Initialize Data Samples object. Declare class-wide variables.
        '''
        self._data_samples = {}   # dict of data samples

    def newDataSample(self, name):
        '''
        Add new Data Sample objects.
        '''
        ds = DataSample(name)
        self._data_samples.update({name: ds})
        return ds

    def get_data_samples(self):
        '''
        Return data samples list to outside functions
        '''
        return self._data_samples


class DataSample:

    def __init__(self, name):
        '''
        Initialize Data Sample objects. Declare class-wide variables.
        '''
        self._name = name
        self._instances = []

    def add_instance(self):
        newInstance = DataInstance(self)
        self._instances.append(newInstance)
        return newInstance

    def get_instances(self):
        return self._instances


class DataInstance:

    def __init__(self, dataSample):
        '''
        Takes a data sample object as input
        Initialize Data Instance object. Declare class-wide variables.
        '''
        self._instanceOf = dataSample   # keep track of what data this is
        self._data = []   # list of data

    def add_data(self, data):
        self._data += data

    def get_data(self):
        return self._data

    def get_instance_of(self):
        return self._instanceOf
