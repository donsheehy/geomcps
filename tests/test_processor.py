import unittest
import os
import sys

currentdir = os.getcwd()
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
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

    def test_right_directory(self):
        self.assertEqual(self._dp.get_file_directory(),
                         "D:\\geomcps\\UserIDWalking")

    def test_right_extension(self):
        self.assertEqual(self._dp.get_file_extension(), "csv")

    def tearDown(self):
        os.chdir(mainDir)
        os.rename(os.path.join(os.getcwd(), ".config"),
                  os.path.join(os.getcwd(), "test.config"))
        os.rename(os.path.join(os.getcwd(), "perm.config"),
                  os.path.join(os.getcwd(), ".config"))



# def main():
#     ut = TestDataProcesor()
#
#     # ut.reset_config()
#     ut.test_set_config()


if __name__ == "__main__":
    unittest.main()
