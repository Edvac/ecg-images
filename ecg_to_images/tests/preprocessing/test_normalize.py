import pytest
import numpy as np
from sklearn.preprocessing import MinMaxScaler

from ecg_to_images.preprocessing.normalize import normalize

@pytest.mark.incremental
class TestNormalization:

    @pytest.fixture(scope='module')
    def read_array(self):
        try:
            patient_array = np.genfromtxt("/home/george/Dropbox/shareedb/RRouts/rr02012.txt", delimiter='\n',
                                          dtype=np.float64)
        except Exception as err:
            print("Error in create_images method: " + err)

        return patient_array, normalize(patient_array)


    def test_normalize_custom_EqualArray(self, read_array):

        patient_array, normalized_patient_array = read_array
        normalized_pa = normalized_patient_array.copy()

        # custom normalization [0,1]
        pa_normalized2 = (patient_array - np.min(patient_array)) / np.ptp(patient_array)
        assert np.array_equal(pa_normalized2, normalized_pa), "Not equal due to values or shape"

        # custom variant 2
        np_minmax = (patient_array - patient_array.min()) / (patient_array.max() - patient_array.min())

        assert np.array_equal(np_minmax, normalized_pa), "Not equal due to values or shape"


    def test_normalize_scikit_EqualArray(self, read_array):
        # ----------- TEST IS FAILING --------------
        # assert against sci-kit Min-Max scaling
        patient_array, normalized_patient_array = read_array
        normalized_pa = normalized_patient_array.copy()

        pa_scikit = patient_array.copy()
        pa_scikit = np.array(pa_scikit).reshape(-1, 1)

        minmax_scaler = MinMaxScaler(feature_range=(0, 1), copy=True)
        min_max_scaled = minmax_scaler.fit_transform(pa_scikit)

        scikit_pa_reshaped = np.reshape(min_max_scaled, min_max_scaled.size)
        assert np.sum(scikit_pa_reshaped == normalized_pa) == scikit_pa_reshaped.size,\
            "Arrays not identical, the sum of equal elements between the two arrays is different from the array size, "
        assert np.array_equal(scikit_pa_reshaped, normalized_pa), \
            "Not equal due to values or shape, Sci-kit normalization creates different values"

        # VISUALIZE THE DIFFERENCES
        # i = 0
        # k = True
        # for scikit, custom in zip(scikit_pa_reshaped, normalized_pa):
        #     if scikit != custom:
        #         if k:
        #             diff_sci = np.array([scikit], dtype=np.float64)
        #             diff_pa = np.array([custom], dtype=np.float64)
        #             k = False
        #         else:
        #             diff_sci = np.concatenate((diff_sci[:i], [scikit], diff_sci[i:]))
        #             diff_pa = np.concatenate((diff_pa[:i], [custom], diff_pa[i:]))
        #
        #     i = i + 1
        #
        # diff_total = np.column_stack((diff_sci, diff_pa))