import numpy as np
from sklearn.preprocessing import MinMaxScaler, scale
from matplotlib import pyplot as plt


def plot_normalization():
    try:
        patient_array = np.genfromtxt("/home/george/Dropbox/shareedb/RRouts/rr01911.txt",
                                      delimiter='\n',
                                      dtype=np.float64)
    except Exception as err:
        print("Error while reading txt file into numpy array: " + err)

    #  Standardization
    pa_custom = patient_array.copy()
    mean = pa_custom.mean(axis=0)
    pa_custom -= mean
    std = pa_custom.std(axis=0)
    pa_custom /= std


    # Standardization
    to_scale = patient_array.copy()
    scaled_pa3 = scale(patient_array)


    # Normalization
    pa_norm = patient_array.copy()
    pa_norm = np.array(pa_norm).reshape(-1, 1)
    min_max_scaler = MinMaxScaler(copy = True, feature_range = (0, 1))
    pa_norm_custom_scaled = min_max_scaler.fit_transform(pa_norm)

    # Normalization
    pa_norm_custom = patient_array.copy()
    xmin = np.amin(pa_norm_custom)
    xmax = np.amax(pa_norm_custom)
    pa_norm_custom -= xmin
    pa_norm_custom /= (xmax - xmin)

    plt.figure(figsize=(20,5))

    plt.scatter( [i+5 for i in range(len(patient_array))],patient_array[:], color='orange', label='input scale', alpha=0.5)
    plt.scatter( [i+5 for i in range(len(pa_custom))],pa_custom[:], color='grey', label='Standardized', alpha=0.5)
    plt.scatter( [i+5 for i in range(len(pa_norm_custom))], pa_norm_custom[:], color='purple', label='min-max scaled [min = 0, max = 1]', alpha=0.5)

    plt.title("RR peaks of the SHAREE DB")
    plt.xlabel("time")
    plt.ylabel("milliVolt")
    plt.legend(loc = 'upper left')
    plt.grid()
    plt.gcf().autofmt_xdate()

    plt.tight_layout()
    plt.show()
    input()

plot_normalization()