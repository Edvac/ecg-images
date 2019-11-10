import numpy as np


def remove_range_outliers(patient_array: np.ndarray, options) -> np.ndarray:
    if options.get("preprocessing", "range") == 'fixed':
        patient_ar = rr_fixed_range(patient_array)
    elif options.get("preprocessing", "range") == 'mean_std':
        patient_ar = rr_mean_std_range(patient_array)
    return patient_ar


def rr_fixed_range(patient_array):
    it = 0
    # tested values with r script. At least 80% of the original population is left
    # after outlier removal
    min = 0.2
    max = 1.5
    values_in_range = []

    # Keep values within [0.2, 1.5] range
    # while it < patient_array.size:
    #
    #     if min <= patient_array[it] <= max:
    #         values_in_range = np.append(values_in_range, patient_array[it])
    #
    #     it += 1
    # return values_in_range
    test = np.delete(patient_array, np.argwhere((patient_array < 0.2) & (patient_array > 1.5)))
    return test

def rr_mean_std_range(patient_array):

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