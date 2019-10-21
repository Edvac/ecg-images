
def standardize(filtered_patient_data):
    pa_custom = patient_array.copy()
    mean = pa_custom.mean(axis=0)
    pa_custom -= mean
    std = pa_custom.std(axis=0)
    pa_custom /= std

    to_scale = patient_array.copy()
    scaled_pa3 = scale(patient_array)

    means = patient_array.mean()
    stds = patient_array.std()
    patient_array = patient_array - means[:]
    patient_array = patient_array / stds[:]
    np.nan_to_num(patient_array)


    filtered_patient_data.mean(axis=0)
    data_norm_by_std = [number / scipy.std(filtered_patient_data) for number in filtered_patient_data]

    data_norm_by_std = [number / scipy.std(filtered_patient_data) for number in filtered_patient_data if not scipy.std(filtered_patient_data) == 0]

    # assert 5
    x = [1, 4, 5, 6, 6, 2, 3]
    mean = sum(x) / len(x)
    std_dev = (1 / len(x) * sum([(x_i - mean) ** 2 for x_i in x])) ** 0.5

    z_scores = [(x_i - mean) / std_dev for x_i in x]

    # assert 6

    x_np = np.asarray(x)
    z_scores_np = (x_np - x_np.mean()) / x_np.std()

    return