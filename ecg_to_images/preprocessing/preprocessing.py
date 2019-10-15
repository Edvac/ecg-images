from ecg_to_images.preprocessing.remove_negative_values import remove_negative_values
from ecg_to_images.preprocessing.filtering import remove_rr_outliers

def preprocessing(patient_array, filename):
    positive_pa = remove_negative_values(patient_array)
    filtered_pa = remove_rr_outliers(positive_pa, filename)
    # normalize
    # standardize
    return positive_pa