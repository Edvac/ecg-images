import sys
import unittest
import numpy as np
from sklearn.preprocessing import scale, StandardScaler

from ecg_to_images.preprocessing.standardize import standardize


class MyTestCase(unittest.TestCase):

    def test_calc_mean():
        try:
            patient_array = np.genfromtxt("/home/george/Dropbox/shareedb/RRouts/rr01911.txt", delimiter='\n',
                                          dtype=np.float64)
        except:
            e = sys.exc_info()[0]
            print("Error in create_images method: " + e)

        # Mean used as a reference from the statistics package
        mean_value = mean(patient_array)

        # test that mean is calculated correctly
        assert mean_value == np.mean(patient_array)
        assert mean_value == stat.mean(patient_array)
        assert mean_value == sp.mean(patient_array)

        # custom_mean = (sum(patient_array)/len(patient_array))
        assert mean_value == statistics.mean(patient_array)

    def test_something(self):
        try:
            patient_array = np.genfromtxt("/home/george/Dropbox/shareedb/RRouts/rr01911.txt",
                                          delimiter = '\n',
                                          dtype = np.float64)
        except:
            e = sys.exc_info()[0]
            print("Error in create_images method: " + e)

        # tests that the values have been properly standardized
        pa_to_scale = patient_array.copy()
        assert standardize(patient_array) == scale(pa_to_scale), \
            "The base scale method does not match the StandardScaler"

        # second assertion with custom implementation of zero mean and unit variance (z-score)
        pa_stnd_scale = patient_array.copy()
        stsc_pa = StandardScaler()
        pa_stnd_scale = np.array(pa_stnd_scale).reshape(-1, 1)
        pa_stnd_scale = stsc_pa.fit_transform(pa_stnd_scale)

        assert standardize(patient_array) == pa_stnd_scale, "The manual method does not match the StandardScaler"



if __name__ == '__main__':
    unittest.main()