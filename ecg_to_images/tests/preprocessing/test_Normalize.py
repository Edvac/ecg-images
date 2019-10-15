import statistics
import sys
from statistics import mean

import numpy as np


def test_normalize():

    try:
        patient_array = np.genfromtxt("/home/george/Dropbox/shareedb/RRouts/rr01911.txt", delimiter='\n', dtype=np.float64)
    except:
        e = sys.exc_info()[0]
        print("Error in create_images method: " + e)

    # sklearn_normalized_p_array = pre.normalize(patient_array, norm='l1')
    # patient_array_normalized = normalize(patient_array)
    # assert sklearn_normalized_p_array == patient_array_normalized

def test_calc_mean():
    try:
        patient_array = np.genfromtxt("/home/george/Dropbox/shareedb/RRouts/rr01911.txt", delimiter='\n', dtype=np.float64)
    except:
        e = sys.exc_info()[0]
        print("Error in create_images method: " + e)

    # Mean used as a reference from the statistics package
    mean_value = mean(patient_array)

    # test that mean is calculated correctly
    # assert mean_value == np.mean(patient_array)
    # assert mean_value == stat.mean(patient_array)
    # assert mean_value == sp.mean(patient_array)

    # custom_mean = (sum(patient_array)/len(patient_array))
    assert mean_value == statistics.mean(patient_array)


