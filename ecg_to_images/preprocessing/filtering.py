import numpy as np


def remove_rr_outliers(patient_array: np.ndarray) -> np.ndarray:
    patient_arr_up_thr = rr_range(patient_array)
    return patient_arr_up_thr


def rr_range(patient_array):
    index_to_delete = []
    it = 0
    pa_mean = np.mean(patient_array)
    pa_std = np.std(patient_array)

    # filter values mean +- 2 * standard deviation
    while it < patient_array.size:
        if patient_array[it] >= pa_mean:
            if patient_array[it] > (pa_mean + (2 * pa_std)):
                index_to_delete.extend([it])
        else:
            if patient_array[it] < (pa_mean - (2 * pa_std)):
                index_to_delete.extend([it])

        it += 1

    return np.delete(patient_array, index_to_delete)
