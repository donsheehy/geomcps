import os


class DataProcessor:

    def __init__(self, name):
        self._name = name
        self._directory = "D:/geomcps/UserIDWalking/UserIDWalkingData"

    def set_file_directory(self):
        # Get file directory from user
        go = True
        while(go):
            directory = input("Enter directory of files (default is \n"
                              "D:/geomcps/UserIDWalking/UserIDWalkingData): ")
            if directory == "":
                go = False
            if os.path.exists(directory):
                self._directory = directory
                go = False
        print("Directory set to : ", self._directory)

    def collect_files(self):
        # os.chdir(self._directory)
        for dirName, subdirList, fileList in os.walk(self._directory):
            print('Found directory: ', dirName)
            for fname in fileList:
                print("\t", fname)


def main():
    dp = DataProcessor("dp")
    dp.set_file_directory()
    dp.collect_files()


if __name__ == '__main__':
    main()
