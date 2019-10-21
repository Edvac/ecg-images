def remove_negative_values(patient_array):
    patient_array = patient_array[patient_array >= 0]
    return patient_array