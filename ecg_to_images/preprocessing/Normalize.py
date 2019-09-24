from statistics import mean


def normalize(patient_array):

    calc_mean = mean(patient_array)
    normalized_p_array = [(x - calc_mean) for x in patient_array]
    return normalized_p_array
