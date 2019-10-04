from statistics import mean
import numpy as np


def normalize(patient_array, ):

    means = patient_array.mean()
    stds = patient_array.std()
    patient_array = patient_array - means[:]
    patient_array = patient_array / stds[:]
    return np.nan_to_num(patient_array)


'''
Todo
- (V - min V)/(max V - min V) 
- Binning
'''