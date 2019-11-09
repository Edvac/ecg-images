import numpy as np


def normalize_to_byte_img(filtered_patient_array, options):
    """This function rescales the filtered values into [0,255] interval.
    .. math::
        f(n)=\\frac{255\\times log_{10}n}{\\log_{10}max-\\log_{10}min}

    Args:
        filtered_patient_array (ndarray): removed negatives and values in placed in range
        options (file): config file
built
    Returns: an rescaled integer numpy array

    References: log scale conversion is based on: https://math.stackexchange.com/questions/970094/convert-a-linear-scale-to-a-logarithmic-scale
    and https://www.youtube.com/watch?v=sBhEi4L91Sg
    """
    scale_conf = options.get("preprocessing", "scale")
    if scale_conf == "linear":
        return linear_scale(filtered_patient_array)
    else:
        return log_scale(filtered_patient_array, scale_conf)

def linear_scale(filtered_patient_array):
    return (255 * ((filtered_patient_array - np.min(filtered_patient_array))
                   / np.ptp(filtered_patient_array))).astype(np.uint8)


def log_scale(fltrd_pa, scale):
    if scale == "log2":
        return ((255 * np.log2(fltrd_pa))
                / np.log2(np.max(fltrd_pa)) - np.log2(np.min(fltrd_pa))).astype(np.uint8)

    elif scale == "loge":
        return ((255 * np.log(fltrd_pa))
                / np.log(np.max(fltrd_pa)) - np.log(np.min(fltrd_pa))).astype(np.uint8)

    elif scale == "log10":
        return ((255 * np.log10(fltrd_pa))
                / np.log10(np.max(fltrd_pa)) - np.log10(np.min(fltrd_pa))).astype(np.uint8)
