
def standardize():
    data_norm_by_std = [number / scipy.std(data) for number in data]

    data_norm_by_std = [number / scipy.std(data) for number in data if not scipy.std(data) == 0]