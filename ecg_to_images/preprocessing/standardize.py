def standardize(filtered_patient_data):
    filt_pa = filtered_patient_data.copy()
    z_score_pa = (filt_pa - filt_pa.mean()) / filt_pa.std()

    return z_score_pa
