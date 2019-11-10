import numpy as np


def log_scale(fltrd_pa, scale) -> np.ndarray:
    """Converts a patient array to logarithmic scale

    Args:
        fltrd_pa: the array without negative and out of specified range values
        scale: The base of the logarithm

    Returns: The patient array in the specified logarithmic scale
    """
    try:
        if scale == "log2":
            pa = np.log2(fltrd_pa)
            i = None
        elif scale == "loge":
            pa = np.log(fltrd_pa)
            i = None
        elif scale == "log10":
            pa = np.log10(fltrd_pa)
            i = None
    except RuntimeWarning as err:
        print
        print(err)
        print(err.args, exc_info=True)

    return pa