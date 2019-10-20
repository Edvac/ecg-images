import numpy as np


def normalize(patient_array):
    x = patient_array.copy().astype(np.float64)

    rescaled_pa = (x - np.min(x)) \
                  / (np.max(x) - np.min(x))

    return rescaled_pa
