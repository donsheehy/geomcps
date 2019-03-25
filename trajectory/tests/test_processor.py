import unittest
import os
import sys
import trajectory.dataprocessor as dataprocessor
import trajectory.datasample as datasample


class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        f = open("constant.txt", "r")
        topDir = f.read()
        print(topDir)
        f.close()
        os.chdir(topDir)
        exampleDir = os.path.join(topDir,
                                  'examples',
                                  'example_data')
        self._dp = dataprocessor.DataProcessor(exampleDir)

    def test_right_directory(self):
        topDir = os.getcwd()
        exampleDir = os.path.join(topDir,
                                  'examples',
                                  'example_data')
        self.assertEqual(self._dp.get_file_directory(),
                         exampleDir)

    def test_right_extension(self):
        self.assertEqual(self._dp.get_file_extension(), "csv")

    def test_collect_all_files(self):
        topDir = os.getcwd()
        openme = os.path.join(topDir,
                              "trajectory",
                              "tests",
                              "test_file_collection.txt")
        f = open(openme, 'r')
        file_collection = f.read()[:-1]
        file_collection = file_collection.split(',')
        f.close()
        self._dp.collect_files()
        self.assertEqual(self._dp.get_files(), file_collection)

    def test_collect_data_files(self):
        topDir = os.getcwd()
        openme = os.path.join(topDir,
                              "trajectory",
                              "tests",
                              "test_data_file_collection.txt")
        f = open(openme, 'r')
        file_collection = f.read()[:-1]
        file_collection = file_collection.split(',')
        f.close()
        # only data files depends on collect files
        self._dp.collect_files()
        self._dp.only_data_files()
        self.assertEqual(self._dp.get_files(), file_collection)

    def test_get_extension(self):
        self.assertEqual(self._dp._ext, self._dp.get_file_extension)


def pretest():
    curDir = os.getcwd()
    # if self._testDir == None:
    #     self._testDir = curDir
    parentDir = os.path.dirname(curDir)
    topDir = os.path.dirname(parentDir)
    return topDir


def posttest():
    pass


def main():
    f = open("constant.txt", "wt")
    topDir = pretest()
    f.write(topDir)
    unittest.main()
    posttest()
    f.close()
    os.remove('constant.txt')


if __name__ == "__main__":
    main()
