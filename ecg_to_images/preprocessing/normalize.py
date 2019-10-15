from statistics import mean
import numpy as np


def normalize(patient_array):

    '''
    Normalize values between 0-1
    '''


    # Normalised [0,255] as integer
    rescaled = 255 * (patient_array - np.min(patient_array)) / np.ptp(patient_array).astype(np.uint8)
    # d *= 255.0 / np.max(patient_array)

    # Normalised [0,1]
    pa_zero_one = (patient_array - np.min(patient_array)) / np.ptp(patient_array)


    # rounds up to the closest int so might all values turn to zero o 1
    patient_array_byte = patient_array.astype(np.uint8, copy=False)
    means = patient_array.mean()
    stds = patient_array.std()
    patient_array = patient_array - means[:]
    patient_array = patient_array / stds[:]
    return np.nan_to_num(patient_array)


'''
Todo
- Normalize between 0-255 to map grayscale
'''