import os
import walker

class DataProcessor:

    def __init__(self):
        '''
        Initialize Data Processor objects. Declare class-wide variables.
        '''
        # default file directory is just where I personally keep the data on my
        # computer.
        #self._directory = r"C:\Users\Abhinna Adhikari\PycharmProjects\Geomcps\UserIDWalking"
        self._directory = os.fspath("D:\\geomcps\\UserIDWalking\\UserIDWalkingData")
        self._data = []
        # self._ext = "tsd"
        self._ext = "csv"
        self._fileList = []
        self._debugMode = True

    def set_file_directory(self):
        '''
        Sets the absolute file directory path for files to import.
        '''
        go = True
        while (go):
            # get file directory from users or accept default
            if self._debugMode:
                dir = ""
            else:
                dir = input("Enter directory: ")
            # dir = input("Enter directory of files (default is\n"
            #              "D:/geomcps/UserIDWalking/UserIDWalkingData): ")
            # dir = ""
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
            if self._debugMode:
                ext = ""
            else:
                ext = input("File extension of data files (default .csv): ")
            # ext = ""
            if ext == "":
                go = False
            else:
                if ext[0] == ".":
                    ext = ext[1:]
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
        Pulls data into nested listsself. Each file becomes a first-level item,
        each line in the file becomes a list of the items on that line.
        '''
        fullFileName = self._directory + "\\" + file_name
        self._data.append([])
        walker_data = walker.Walker()
        f = open(fullFileName)
        for line in f:
            line_data = []
            if self._ext == 'tsd':
                # split by whitespace
                line_data = line.split()
            if self._ext == 'csv':
                # split by comma
                line_data = line.split(',')
            # if the line of data ends with a newline, cut it off
            if str(line_data[-1])[-1] == '\n':
                line_data[-1] = str(line_data[-1])[:-1]
            # confirm all data is float
            for i in range(len(line_data)):
                line_data[i] = float(line_data[i])
            walker_data.add_point(line_data)
        f.close()
        print("File ", file_name, " processed.")
        self._data[file_num] = walker_data


    def print_data(self, data_id):
        '''
        Input: data_id for data to print
        Prints data, one line per line.
        '''
        walker = self._data[data_id]
        for i in range(len(walker.times)):
            print(walker.times[i], walker.pos.x[i], walker.pos.y[i],walker.pos.z[i],end="")
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
    dp.print_data(1)


if __name__ == '__main__':
    main()
