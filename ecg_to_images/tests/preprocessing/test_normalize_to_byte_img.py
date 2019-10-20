import pytest
import numpy as np

from sklearn.preprocessing import MinMaxScaler

from ecg_to_images.preprocessing.normalize_to_byte_img import normalize_to_byte_img
#------------- ALL TESTS ARE FAILING using float64, due to rounding errors---------------
@pytest.fixture(scope='module')
def read_array():
    try:
        patient_array = np.genfromtxt("/home/george/Dropbox/shareedb/RRouts/rr02012.txt", delimiter='\n',
                                      dtype=np.float64)
    except Exception as err:
        print("Error in create_images method: " + err)

    return patient_array, normalize_to_byte_img(patient_array)


def test_interpolate_normalize_to_byte_img_EqualArrays(read_array):

    # Normalize [0-255] by interpolating data
    filtered_patient_array, normalized_byte_pa = read_array
    interpolated_pa = np.interp(filtered_patient_array, (filtered_patient_array.min(), filtered_patient_array.max()), (0, 255))

    assert np.array_equal(normalized_byte_pa.astype(np.uint8), interpolated_pa.astype(np.uint8)), \
        "Normalized to byte array is not equal with interpolated version"


def test_scikit_normalize_to_byte_img_EqualArrays(read_array):

    # Normalization [0 - 255]
    filtered_patient_array, normalized_byte_pa = read_array
    pa_norm = filtered_patient_array.copy()
    pa_norm = np.array(pa_norm).reshape(-1, 1)
    min_max_scaler = MinMaxScaler(feature_range=(0, 255), copy=False)
    pa_norm_custom_scaled = min_max_scaler.fit_transform(pa_norm)

    assert np.array_equal(normalized_byte_pa.astype(np.uint8), pa_norm_custom_scaled.astype(np.uint8)), \
        "Normalized to byte array is not equal sci-kit version"

    # # VISUALIZE DIFFERENCES
    # i = 0
    # k = True
    # for interp, custom in zip(interpolated_pa, normalized_byte_pa):
    #     if interp != custom:
    #         if k:
    #             diff_interp = np.array([interp], dtype=np.float64)
    #             diff_pa = np.array([custom], dtype=np.float64)
    #             k = False
    #         else:
    #             diff_interp = np.concatenate((diff_interp[:i], [interp], diff_interp[i:]))
    #             diff_pa = np.concatenate((diff_pa[:i], [custom], diff_pa[i:]))
    #
    #     i = i + 1
    #
    # diff_total = np.column_stack((diff_interp, diff_pa))