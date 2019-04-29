import os
import trajectory.datasample as ds
# import datasample as ds
# import config as config
import trajectory.config as config
import sys


class DataProcessor:

    def __init__(self, directory):
        '''
        Initialize Data Processor objects. Declare class-wide variables.
        Adding input for directory to facilitate unit testing.
        '''
        self._directory = directory
        self._data = []
        self._ext = ""
        self._track_folder_name = 0
        self._track_file_name = 0
        self._fileList = []
        self._debugMode = False
        self._folder = ''
        self._file = ''
        self._data_samples = ds.DataSamples()
        self.runTheThings()

    def runTheThings(self):
        self.read_config()
        self.collect_files()
        self.only_data_files()
        self.read_files_to_obj()

    def read_config(self):
        '''
        Get configuration from config file.
        '''
        filename = os.path.join(self._directory, '.config')
        res = config.read_config(filename)
        ext = res[0][:-1]
        if ext[0] == ".":
            ext = ext[1:]
        self._ext = ext
        self._track_folder_name = int(''.join(res[1][:-1]))
        self._track_file_name = int(''.join(res[2][:-1]))
        if res[3][:-1] == 't':
            self._debugMode = True
        else:
            self._debugMode = False

    def get_file_directory(self):
        return self._directory

    def get_file_extension(self):
        return self._ext

    def collect_files(self):
        '''
        Goes to the directory defined by the user and collect list of files
        '''
        for dirName, subdirList, fileList in os.walk(self._directory):
            for fname in fileList:
                newFile = os.path.join(dirName, fname)
                self._fileList.append(newFile)

    def get_files(self):
        return self._fileList

    def only_data_files(self):
        '''
        Restrict the files in the directory to those with the data extension
        '''
        newFileList = []
        for file in self._fileList:
            file_ext = file.split(os.extsep)
            if file_ext[-1] == self._ext:
                newFileList.append(file)
        self._fileList = newFileList

    def read_files_to_obj(self):
        '''
        Input: List of data files in readable format
        Calls read_file_to_obj for each
        '''
        file_num = 0
        for file in self._fileList:
            if self._track_folder_name:
                self._folder = file.split(os.sep)[-2]
            if self._track_file_name:
                tmpfile = file.split(os.sep)[-1]
                self._file = tmpfile.split(os.extsep)[0]
            self.read_file_to_obj(file, file_num)
            file_num += 1

    def read_file_to_obj(self, file_name, file_num):
        '''
        Inputs: file name of data to import, file number to act as data id
        Pulls data into nested list. Each file becomes a first-level item,
        each line in the file becomes a list of the items on that line.
        '''
        full_file_name = os.path.join(self._directory, file_name)
        dsname = self.sample_name()
        if dsname == '':
            dsname = file_num
        ds_dict = self._data_samples.get_data_samples()
        if (dsname in ds_dict):
            dsamp = self._data_samples.newDataSample(dsname)
        else:
            dsamp = self._data_samples.initDataSamples(dsname)
        f = open(full_file_name)
        # create an "instance" for the file
        di = dsamp.add_instance(self.instance_name())
        for line in f:
            line_data = []
            if self._ext == 'csv':
                # split by comma
                line_data = line.split(',')
            else:
                # default to split by whitespace
                line_data = line.split()
            # if the line of data ends with a newline, cut it off
            if str(line_data[-1])[-1] == '\n':
                line_data[-1] = str(line_data[-1])[:-1]
            # confirm all data is float
            for i in range(len(line_data)):
                line_data[i] = float(line_data[i])
            di.add_point(line_data)
        f.close()

    def sample_name(self):
        return self._folder[:self._track_folder_name]

    def instance_name(self):
        b1 = self._folder[:self._track_folder_name]
        b2 = self._file[:self._track_file_name]
        b2 = ''.join(b2)
        tmp = b2.split('-')
        b2 = tmp[0]
        dsname = [b1, b2]
        dsname = '-'.join(dsname)
        return dsname

    def get_data_samples_obj(self):
        return self._data_samples

    def get_data_samples_dict(self):
        return self._data_samples.get_data_samples()

    def print_data(self, data_id):
        '''
        Input: data_id for data to print
        Prints data, one line per line.
        '''
        for file in self._data[data_id]:
            for line in file:
                print(line)
                # for position in time:
                #     print(position, end="")
            print("\n", end="")

    def make_set_of_trajectories(self):
        return self._data_samples.make_trajectories()


def main():
    '''
    Sequence through the process of instantiating a data processor and
    importing data from the relevant computer directory
    '''
    directory = sys.argv[1]
    # directory = os.path.join(os.getcwd(), 'examples', 'example_data')
    # dp = DataProcessor(directory)
    # dp.collect_files()
    # dp.only_data_files()
    # dp.read_files_to_obj()
    print(dp.get_data_samples_obj().make_trajectories())
    print(dp.make_set_of_trajectories())


if __name__ == '__main__':
    main()
