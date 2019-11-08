import numpy as np


def normalize_to_byte_img(filtered_patient_array, options):

    scale_conf = options.get("preprocessing", "scale")
    if scale_conf == "linear":
        # Normalize as an 8-bit integer [0,255]
        rescaled_patient_array = (255 * ((filtered_patient_array - np.min(filtered_patient_array))
                                         / np.ptp(filtered_patient_array))).astype(np.uint8)


    return rescaled_patient_array
