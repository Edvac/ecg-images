import sys

import matplotlib.pyplot as plt
import numpy as np
import scipy
import seaborn as sns

from ecg_to_images.preprocessing.normalize import normalize


def dummy():
    print("test")
    try:
        patient_array = np.genfromtxt("/home/george/Dropbox/shareedb/RRouts/rr02062.txt", delimiter='\n', dtype=np.float64)
    except:
        e = sys.exc_info()[0]
        print("Error in create_images method: " + e)

    data = patient_array

    data_norm_by_std = [number / scipy.std(data) for number in data if not scipy.std(data) == 0]
    # data_norm_by_mean = normalize(data)


    # style.use('darkgrid')
    sns.set()

    y1 = data
    x1 = [i for i in range(len(y1))]

    y2 = data_norm_by_std
    x2 = [i for i in range(len(y2))]

    # y3 = data_norm_by_mean
    # x3 = [i for i in range(len(y3))]


    plt.figure(1)
    plt.ylim([-3, 23])
    plt.yticks(np.arange(-1,21,step=1))
    plt.plot([],[])
    plt.scatter(x1, y1 , marker=".", s=5)
    plt.title('Original RR peaks ')

    plt.figure(2)
    plt.ylim([-3, 23])
    plt.yticks(np.arange(-1, 21, step=1))
    plt.plot([], [])
    plt.scatter(x2, y2, marker=".", s=5)
    plt.gcf().autofmt_xdate()
    plt.title('Standardized RR peaks')

    # plt.figure(3)
    # plt.ylim([-3, 23])
    # plt.yticks(np.arange(-1, 21, step=1))
    # plt.plot([], [])
    # plt.scatter(x3, y3, marker=".", s=5)
    # plt.gcf().autofmt_xdate()

    plt.show()
    input()


dummy()