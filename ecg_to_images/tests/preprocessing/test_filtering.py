import logging

import numpy as np
import pytest

from ecg_to_images.preprocessing.filtering import rr_range

logger = logging.getLogger(__name__)


@pytest.fixture(scope='module')
def read_array():
    try:
        patient_array = np.genfromtxt("/home/george/Dropbox/shareedb/RRouts/rr02012.txt", delimiter='\n',
                                      dtype=np.float64)
    except Exception as err:
        print("Error in create_images method: " + err)

    return patient_array, rr_range(patient_array)

# different way to create the filtered array
def test_rr_range(read_array):
    patient_array, range_pa  = read_array

    index_to_delete = []
    it = 0
    pa_mean = np.mean(patient_array)
    pa_std = np.std(patient_array)
    while it < patient_array.size:
        if patient_array[it] >= pa_mean:
            if patient_array[it] > (pa_mean + (2 * pa_std)):
                index_to_delete.extend([it])
        elif patient_array[it] < pa_mean:
            if patient_array[it] < (pa_mean - (2 * pa_std)):
                index_to_delete.extend([it])

        it += 1

    assert np.array_equal(np.delete(patient_array, index_to_delete), range_pa), "arrays should be same"
