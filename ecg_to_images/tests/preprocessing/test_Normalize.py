import statistics
import sys
from statistics import mean

import numpy as np
import scipy


import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tools




def test_normalize():

    try:
        patient_array = np.genfromtxt("/home/george/Dropbox/shareedb/RRouts/rr01911.txt", delimiter='\n', dtype=np.float64)
    except:
        e = sys.exc_info()[0]
        print("Error in create_images method: " + e)

    # sklearn_normalized_p_array = pre.normalize(patient_array, norm='l1')
    # patient_array_normalized = normalize(patient_array)
    # assert sklearn_normalized_p_array == patient_array_normalized

def test_calc_mean():
    try:
        patient_array = np.genfromtxt("/home/george/Dropbox/shareedb/RRouts/rr01911.txt", delimiter='\n', dtype=np.float64)
    except:
        e = sys.exc_info()[0]
        print("Error in create_images method: " + e)

    # Mean used as a reference from the statistics package
    mean_value = mean(patient_array)

    # test that mean is calculated correctly
    # assert mean_value == np.mean(patient_array)
    # assert mean_value == stat.mean(patient_array)
    # assert mean_value == sp.mean(patient_array)

    # custom_mean = (sum(patient_array)/len(patient_array))
    assert mean_value == statistics.mean(patient_array)


# def test_plot_normalize_by_std():

    # try:
    #     patient_array = np.genfromtxt("/home/george/Dropbox/shareedb/RRouts/rr01911.txt", delimiter='\n', dtype=np.float64)
    # except:
    #     e = sys.exc_info()[0]
    #     print("Error in create_images method: " + e)
    #
    # data = patient_array
    #
    # data_norm_by_std = [number / scipy.std(data) for number in data]
    #
    # trace1 = go.Histogram(
    #     x=data,
    #     opacity=0.75,
    #     name='data'
    # )
    #
    # trace2 = go.Histogram(
    #     x=data_norm_by_std,
    #     opacity=0.75,
    #     name='normalized by std = ' + str(scipy.std(data)),
    # )
    #
    # fig = tools.make_subplots(rows=2, cols=1)
    #
    # fig.append_trace(trace1, 1, 1)
    # fig.append_trace(trace2, 2, 1)
    #
    # fig['layout'].update(height=600, width=800, title='Normalize by a Constant')
    # # py.iplot(fig, filename='apple-data-normalize-constant')
    #
    # fig.show()

