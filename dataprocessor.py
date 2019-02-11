import os


class DataProcessor:

    def __init__(self):
        '''
        Initialize Data Processor objects. Declare class-wide variables.
        '''
        # default file directory is just where I personally keep the data on my
        # computer.
        self._directory = "D:/geomcps/UserIDWalking/UserIDWalkingData"
        self._data = []
        self._ext = ".csv"
        self._fileList = []

    def set_file_directory(self):
        '''
        Sets the absolute file directory path for files to import.
        '''
        go = True
        while(go):
            # get file directory from users or accept default
            dir = input("Enter directory: ")
            # dir = input("Enter directory of files (default is\n"
            #              "D:/geomcps/UserIDWalking/UserIDWalkingData): ")
            if dir == "":  # user accepts default directory
                go = False
            # if user selects a different directory, let's check that it's a
            # valid place on the computer.
            if os.path.exists(dir):
                # if the new directory is valid, stop bothering user.
                self._directory = dir
                go = False
        # report the directory for the data
        print("Directory set to : ", self._directory)

    def set_file_extension(self):
        '''
        set file extension to use
        '''
        go = True
        while(go):
            ext = input("File extension of data files (default .csv): ")
            if ext == "":
                go = False
            else:
                if ext[0] != ".":
                    ext = "." + ext
                self._ext = ext
                go = False
        print("Files with extension: ", self._ext)

    def collect_files(self):
        '''
        Goes to the directory defined by the user and collect list of files
        '''
        nfiles = 0
        for dirName, subdirList, fileList in os.walk(self._directory):
            nfiles += 1
            # print('Found directory: ', dirName)
            for fname in fileList:
                # print("\t", fname)
                self._fileList.append(dirName + "\\" + fname)

    def only_data_files(self):
        '''
        Restrict the files in the directory to those with the data extension
        '''
        newFileList = []
        for file in self._fileList:
            if file[len(self._ext):] == self._ext:
                newFileList.append(file)
        self._fileList = newFileList

    def read_files(self):
        '''
        Input: List of data files in readable format
        Calls read_file for each
        '''
        file_num = 0
        for file in self._fileList:
            self.read_file(file, file_num)
            file_num += 1

    def read_file(self, file_name, file_num):
        '''
        Inputs: file name of data to import, file number to act as data id
        Pulls data into nested list. Each file becomes a first-level item,
        each line in the file becomes a list of the items on that line.
        '''
        fullFileName = self._directory + '\\' + file_name
        self._data.append([])
        id_data = []
        f = open(fullFileName)
        for line in f:
            line_data = []
            for item in line:
                line_data.append(item)
            id_data.append(line_data)
        f.close()
        print("File ", file_name, " processed.")
        self._data[file_num].append(id_data)

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
    dp.set_file_directory()
    dp.set_file_extension()
    dp.collect_files()
    dp.only_data_files()
    dp.read_files()
    dp.print_data(2)


if __name__ == '__main__':
    main()
