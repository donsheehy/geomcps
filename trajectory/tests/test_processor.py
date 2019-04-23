import unittest
import os
import trajectory.dataprocessor as dataprocessor


class TestDataProcessor(unittest.TestCase):
    def return_topDir(self):
        curDir = os.path.dirname(os.path.realpath(__file__))
        parentDir = os.path.dirname(curDir)
        topDir = os.path.dirname(parentDir)
        return topDir

    def setUp(self):
        exampleDir = os.path.join(self.return_topDir(),
                                  'examples',
                                  'example_data')
        self._dp = dataprocessor.DataProcessor(exampleDir)

    def test_right_directory(self):
        exampleDir = os.path.join(self.return_topDir(),
                                  'examples',
                                  'example_data')
        self.assertEqual(self._dp.get_file_directory(),
                         exampleDir)

    def test_right_extension(self):
        self.assertEqual(self._dp.get_file_extension(), "csv")

    def test_collect_all_files(self):
        openme = os.path.join(self.return_topDir(),
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
        openme = os.path.join(self.return_topDir(),
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
        self.assertEqual(self._dp._ext, self._dp.get_file_extension())

    def test_get_file_directory(self):
        self.assertEqual(self._dp._directory, self._dp.get_file_directory())

    def setData(self):
        self._dp.collect_files()
        self._dp.only_data_files()
        self._dp.read_files_to_obj()

    def file2data(self, file):
        fullFile = os.path.join(os.curdir,
                                'examples',
                                'example_data',
                                file)
        f = open(fullFile, 'r')
        data = f.readlines()
        f.close()
        return data

    def test_get_data_samples(self):
        self._dp.collect_files()
        self._dp.only_data_files()
        self.assertEqual(self._dp._data_samples,
                         self._dp.get_data_samples_obj())

    def test_get_data_samples_sub(self):
        self.setData()
        # loop through Samples
        for key in self._dp.get_data_samples_dict():  # key = sample_letter
            # loop through runs
            for i in range(2):
                run = "run" + str(i + 1) + ".csv"
                file = os.path.join(key, run)
                data = self.file2data(file)
                # loop through lines of data
                for line in range(len(data)):
                    sampleObj = self._dp.get_data_samples_dict().get(key)[i]
                    instanceObjs = sampleObj.get_instances()
                    for j in instanceObjs:
                        instanceObj = instanceObjs.get(j)
                        traj = instanceObj.get_data()
                        point = traj[line]
                        pointString = []
                        for coord in point:
                            pointString.append(str(coord))
                        pointString = ','.join(pointString)
                        with self.subTest(sample=key,
                                          line=line,
                                          run=run):
                            self.assertEqual(data[line][:-1], pointString)

    def test_make_set_of_trajectories(self):
        self.setData()
        trajSets = self._dp.make_set_of_trajectories()
        self.assertEqual(len(trajSets), 6)

    def test_make_set_of_trajectories_sub(self):
        self.setData()
        allTraj = self._dp.make_set_of_trajectories()
        # loop through Samples
        for k in range(3):  # key = sample_letter
            # loop through runs
            for i in range(2):
                index = 2 * k + i
                run = "run" + str(i + 1) + ".csv"
                if k == 0:
                    key = 'sample_a'
                elif k == 1:
                    key = 'sample_b'
                else:
                    key = 'sample_c'
                file = os.path.join(key, run)
                data = self.file2data(file)
                data2 = []
                for point in data:
                    tmp = point[:-1].split(',')
                    tmp2 = []
                    for t in tmp:
                        tmp2.append(float(t))
                    data2.append(tmp2)
                traj = allTraj[index][0]  # trajectories have pts property
                with self.subTest(file=file,
                                  index=index):
                    self.assertEqual(data2, traj)


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
