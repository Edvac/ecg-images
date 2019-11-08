import numpy as np


def remove_rr_outliers(patient_array: np.ndarray) -> np.ndarray:
    patient_arr_up_thr = rr_range(patient_array)
    return patient_arr_up_thr


def rr_range(patient_array):

    it = 0
    pa_mean = np.mean(patient_array)
    pa_std = np.std(patient_array)
    values_in_range = []

    # Keep values within [mean +- 2 * standard deviation] range
    while it < patient_array.size:

        if patient_array[it] < pa_mean:
            if patient_array[it] >= (pa_mean - (2 * pa_std)):
                values_in_range = np.append(values_in_range, patient_array[it])
        elif patient_array[it] >= pa_mean:
            if patient_array[it] <= (pa_mean + (2 * pa_std)):
                values_in_range = np.append(values_in_range, patient_array[it])

        it += 1

    return values_in_range
