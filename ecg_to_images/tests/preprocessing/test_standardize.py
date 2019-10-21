import statistics
from functools import reduce

import cv2
import numpy as np
import pytest
import scipy as sp
from sklearn.preprocessing import scale, StandardScaler

from ecg_to_images.preprocessing.standardize import standardize


@pytest.fixture(scope="module")
def read_array():
    try:
        patient_array = np.genfromtxt("/home/george/Dropbox/shareedb/RRouts/rr02032.txt", delimiter='\n',
                                      dtype=np.float64)
    except Exception as err:
        print("Error in create_images method: " + err)
    return patient_array, standardize(patient_array)


@pytest.mark.skip(reason="Each library calculates mean differently")
def test_calc_mean(read_array):
    pa, std_pa = read_array

    # Compare against nunpy's mean
    assert np.array_equal(sp.mean(pa), statistics.mean(pa))
    assert np.array_equal(sp.mean(pa), cv2.mean(pa)[0])
    assert np.array_equal(sp.mean(pa), reduce(lambda x, y: x + y, pa) / len(pa))
    assert np.array_equal(sp.mean(pa), sum(pa) / float(len(pa)))


@pytest.mark.skip(reason="Each library calculates standard deviation differently")
def test_calc_std(read_array):
    pa, std_pa = read_array

    mean = sum(pa) / len(pa)
    std_dev_custom = (1 / len(pa) * sum([(x - mean) ** 2 for x in pa])) ** 0.5

    assert np.array_equal(pa.std(), std_dev_custom), "Numpy calculated std differently from custom code"
    assert np.array_equal(pa.std(), statistics.stdev(pa)), "Numpy calculated std differently from statistics package"


@pytest.mark.skip(reason="Each library calculates standardization differently")
def test_standardization(read_array):
    pa, std_pa = read_array

    # second assertion with custom implementation of zero mean and unit variance (z-score)
    pa_stnd_scale = pa.copy()
    stsc_pa = StandardScaler()
    pa_stnd_scale = np.array(pa_stnd_scale).reshape(-1, 1)
    pa_stnd_scale = stsc_pa.fit_transform(pa_stnd_scale)

    assert np.array_equal(std_pa, pa_stnd_scale), "The manual method does not match the StandardScaler"


@pytest.mark.skip(reason="Each method calculates standardization differently")
def test_standardization_custom(read_array):
    pa, std_pa = read_array

    mean = pa.mean(axis=0)
    pa -= mean
    std = pa.std(axis=0)
    pa /= std

    assert np.array_equal(pa, std_pa), "Custom implemtations for standardization differ"


@pytest.mark.skip(reason="Each method calculates standardization differently")
def test_standardization_scale(read_array):
    pa, std_pa = read_array

    to_scale = pa.copy()
    scaled_pa = scale(to_scale)
    assert np.array_equal(scaled_pa, std_pa)


@pytest.mark.skip(reason="Each method calculates standardization differently")
def test_standardization3(read_array):
    pa, std_pa = read_array

    means = pa.mean()
    stds = pa.std()
    patient_array = pa - means[:]
    patient_array = pa / stds[:]
    np.nan_to_num(patient_array)
    assert np.array_equal(patient_array, std_pa)


@pytest.mark.skip(reason="Each method calculates standardization differently")
def test_standardization4(read_array):
    pa, std_pa = read_array

    mean = sum(pa) / len(pa)
    std_dev = (1 / len(pa) * sum([(x_i - mean) ** 2 for x_i in pa])) ** 0.5
    z_scores = [(x_i - mean) / std_dev for x_i in x]
    np.array_equal(z_scores, std_pa)
