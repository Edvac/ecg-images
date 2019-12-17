import csv
import numpy as np
import pandas as pd

def calc_desc_stats(patient_array):
    """ This function is responsible for calculating the descriptive statistics
        of a give dataset

    Args: file to calculate the descriptive statistics
    """
    max = np.max(patient_array)
    min = np.min(patient_array)
    mean = np.mean(patient_array)
    median = np.median(patient_array)
    range = max - min
    total_observations = len(patient_array)
    Q1 = np.percentile(patient_array, 25)
    Q2 = np.percentile(patient_array, 50)
    Q3 = np.percentile(patient_array, 75)
    IQR = Q3 - Q1
    ds_list = [total_observations, min, max, mean, median, range, Q1, Q2, Q3, IQR]
    return ds_list

def save_csv(df: pd.DataFrame):
    df.to_csv('descriptive_statistics.csv', index=False, index_label=False)
