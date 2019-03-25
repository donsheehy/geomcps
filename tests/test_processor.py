import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.getcwd()))
import dataprocessor

os.chdir("..")
mainDir = os.getcwd()


class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        os.chdir(mainDir)
        self._dp = dataprocessor.DataProcessor()
        os.rename(os.path.join(os.getcwd(), ".config"),
                  os.path.join(os.getcwd(), "perm.config"))
        os.rename(os.path.join(os.getcwd(), "test.config"),
                  os.path.join(os.getcwd(), ".config"))

    def tearDown(self):
        os.chdir(mainDir)
        os.rename(os.path.join(os.getcwd(), ".config"),
                  os.path.join(os.getcwd(), "test.config"))
        os.rename(os.path.join(os.getcwd(), "perm.config"),
                  os.path.join(os.getcwd(), ".config"))

    def test_right_directory(self):
        self.assertEqual(self._dp.get_file_directory(),
                         "D:\\geomcps\\UserIDWalking")

    def test_right_extension(self):
        self.assertEqual(self._dp.get_file_extension(), "csv")

    def test_collect_all_files(self):
        openme = os.path.join("tests", "test_file_collection.txt")
        f = open(openme, 'r')
        file_collection = f.read()[:-1]
        file_collection = file_collection.split(',')
        f.close()
        self._dp.collect_files()
        self.assertEqual(self._dp.get_files(), file_collection)

    def test_collect_data_files(self):
        openme = os.path.join("tests", "test_data_file_collection.txt")
        f = open(openme, 'r')
        file_collection = f.read()[:-1]
        file_collection = file_collection.split(',')
        f.close()
        # only data files depends on collect files
        self._dp.collect_files()
        self._dp.only_data_files()
        self.assertEqual(self._dp.get_files(), file_collection)


def pretest():
    pass


def posttest():
    pass


def main():
    pretest()
    unittest.main()
    posttest()


if __name__ == "__main__":
    main()
