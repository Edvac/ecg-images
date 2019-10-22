import numpy as np


def remove_rr_outliers(patient_array: np.ndarray) -> np.ndarray:
    patient_arr_up_thr = upper_threshold(patient_array)
    return patient_arr_up_thr


def upper_threshold(patient_array):
    index_to_delete = []
    it = 0
    while it < patient_array.size:

        # remove values more than 10mV
        if patient_array[it] > 10:
            index_to_delete.extend([it])
        it += 1

    return np.delete(patient_array, index_to_delete)
