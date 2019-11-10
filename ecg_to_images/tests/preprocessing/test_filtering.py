import logging

import numpy as np
import pytest

from ecg_to_images.preprocessing.filtering import rr_fixed_range, rr_mean_std_range

logger = logging.getLogger(__name__)


@pytest.fixture(scope='module')
def read_array():
    try:
        patient_array = np.genfromtxt("/home/george/Data/RR intervals/shareedb/RR-no-neg/", delimiter='\n',
                                      dtype=np.float64)
    except Exception as err:
        print("Error in create_images method: " + err)

    return patient_array


# different way to create the filtered array
def test_rr_range(read_array):
    patient_array = read_array
    range_pa = rr_mean_std_range(patient_array)

    pa_mean = np.mean(patient_array)
    pa_std = np.std(patient_array)
    index_to_delete = []

    it = 0
    while it < patient_array.size:

        if patient_array[it] >= pa_mean:
            if patient_array[it] > (pa_mean + (2 * pa_std)):
                index_to_delete.extend([it])

        elif patient_array[it] < pa_mean:
            if patient_array[it] < (pa_mean - (2 * pa_std)):
                index_to_delete.extend([it])

        it += 1

    assert np.array_equal(np.delete(patient_array, index_to_delete), range_pa), "arrays should be same"


def test_rr_fixed_range(read_array):
    patient_array = read_array
    fixed_range = rr_fixed_range(patient_array)

    min = 0.2
    max = 1.5
    values_in_range = []

    # Keep values within [0.2, 1.5] range
    it = 0
    while it < patient_array.size:

        if min <= patient_array[it] <= max:
            values_in_range = np.append(values_in_range, patient_array[it])

        it += 1

    assert np.array_equal(fixed_range, values_in_range), "arrays should be same"
