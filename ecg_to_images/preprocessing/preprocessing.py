import numpy as np

from ecg_to_images.preprocessing.filtering import remove_range_outliers
from ecg_to_images.preprocessing.linear_to_log import log_scale
from ecg_to_images.preprocessing.normalize import normalize
from ecg_to_images.preprocessing.normalize_to_byte_img import normalize_to_byte_img
from ecg_to_images.preprocessing.remove_negative_values import remove_negative_values
from ecg_to_images.preprocessing.standardize import standardize


def preprocessing(patient_array, options) -> np.ndarray:

    positive_pa = remove_negative_values(patient_array)
    filtered_pa = remove_range_outliers(positive_pa, options)

    scale_conf = options.get("preprocessing", "scale")
    if scale_conf != "linear":
        filtered_pa = log_scale(filtered_pa, scale_conf)

    rescale_conf = options.get("preprocessing", "rescale_type")

    if rescale_conf == 'normalize':
       rescaled_pa = normalize(filtered_pa)
    elif rescale_conf == 'normalize_to_byte_image':
        rescaled_pa = normalize_to_byte_img(filtered_pa)
    elif rescale_conf == 'standardize':
        rescaled_pa = standardize(filtered_pa)
    else:
        raise Exception("Acceptable values are \"normalize\", \"standardize\" and \"normalize_to_byte_image\""
                        ". Entered: " + rescale_conf)
    return rescaled_pa
