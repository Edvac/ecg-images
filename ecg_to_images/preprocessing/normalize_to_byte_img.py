import numpy as np


def normalize_to_byte_img(filtered_patient_array):
    """This function rescales the filtered values into [0,255] interval.
    If the scale is linear:

    .. math::
        f(n)=\\frac{255\\times n - min}{max-min}

    If the scale is logarithmic:

    .. math::
        f(n)=\\frac{255\\times log_{2}n - log_{2}min}{\\log_{2}max-\\log_{2}min}

    Args:
        filtered_patient_array (ndarray): removed negatives and values in placed in range
        options (file): config file

    Returns: an rescaled integer numpy array
    """
    return (255 * ((filtered_patient_array - np.min(filtered_patient_array))
                   / np.ptp(filtered_patient_array))).astype(np.uint8)


