import numpy as np

def normalize_for_pixels(normalized_and_filtered_patient_array):
    nf_patient_array = normalized_and_filtered_patient_array

    # Normalize [0,255] as integer
    rescaled_patient_array = 255 * (nf_patient_array - np.min(nf_patient_array)) \
                             / np.ptp(nf_patient_array).astype(np.uint8)


    # ALTERNATIVE approach
    # interpolate data
    # np.interp(patient_array, (patient_array.min(), patient_array.max()), (0, 255))
    return rescaled_patient_array