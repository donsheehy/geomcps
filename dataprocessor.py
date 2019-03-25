import os
import datasample as ds
import config


class DataProcessor:

    def __init__(self):
        '''
        Initialize Data Processor objects. Declare class-wide variables.
        Adding input for directory to facilitate unit testing.
        '''
        self._directory = ""
        self._data = []
        self._ext = ""
        self._track_folder_name = 0
        self._track_file_name = 0
        self._fileList = []
        self._debugMode = False
        self._folder = ''
        self._file = ''
        self._data_samples = ds.DataSamples()
        self.read_config()

    def read_config(self):
        '''
        Get configuration from config file.
        '''
        res = config.read_config()
        self._directory = os.fspath(res[0][:-1])
        ext = res[1][:-1]
        if ext[0] == ".":
            ext = ext[1:]
        self._ext = ext
        self._track_folder_name = int(res[2][:-1])
        self._track_file_name = int(res[3][:-1])
        if res[4][:-1] == 'f':
            self._debugMode = False
        else:
            self._debugMode = True

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

    def only_data_files(self):
        '''
        Restrict the files in the directory to those with the data extension
        '''
        # print(self._fileList)
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
                self._folder = file.split(os.sep[-2])
            if self._track_file_name:
                tmpfile = file.split(os.sep)[-1]
                self._file = tmpfile.split(os.extsep[0])
            self.read_file_to_obj(file, file_num)
            file_num += 1

    def read_file_to_obj(self, file_name, file_num):
        '''
        Inputs: file name of data to import, file number to act as data id
        Pulls data into nested list. Each file becomes a first-level item,
        each line in the file becomes a list of the items on that line.
        '''
        # once = False
        # if file_num == 0:
        #     once = True
        full_file_name = os.path.join(self._directory, file_name)
        dsname = self.name_handling()
        if dsname == '':
            dsname = file_num
        ds_dict = self._data_samples.get_data_samples()
        if (dsname in ds_dict):
            dsamp = ds_dict[dsname]
        else:
            dsamp = self._data_samples.newDataSample(dsname)
        f = open(full_file_name)
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
            # if once:
            #     print(line_data)
            #     once = False
            di = dsamp.add_instance()
            di.add_data(line_data)
        f.close()

    def name_handling(self):
        a = self._folder[:self._track_folder_name]
        b = self._file[:self._track_file_name]
        b = ''.join(b)
        tmp = b.split('-')
        b = tmp[0]
        dsname = [a, b]
        dsname = '-'.join(dsname)
        return dsname

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


def main():
    '''
    Sequence through the process of instantiating a data processor and
    importing data from the relevant computer directory
    '''
    dp = DataProcessor()
    dp.collect_files()
    dp.only_data_files()
    dp.read_files_to_obj()
    all_data_samples = dp._data_samples.get_data_samples()
    print(all_data_samples.get('-03'))
    print(all_data_samples.get('-03').get_instances())
    print(all_data_samples.get('-03').get_instances()[0].get_data())
    # dp.print_data(2)


if __name__ == '__main__':
    main()
