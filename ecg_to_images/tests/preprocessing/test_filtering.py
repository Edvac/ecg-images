import logging
import os
import sys
import unittest
from unittest import TestCase
import numpy as np

from ecg_to_images.image_types.save_images import get_absolute_file_names
from ecg_to_images.preprocessing.filtering import upper_threshold
from ecg_to_images.utils.parse_cmd_args import parse_cmd_arguments
from ecg_to_images.utils.parse_conf_file import parse_config_file

logger = logging.getLogger(__name__)


class TestFiltering(TestCase):

    def main(self):

        ns = parse_cmd_arguments()
        # pass the namespace containing the args to read the config file
        config_file = parse_config_file(ns)

        path_filenames = get_absolute_file_names(config_file.get("ecg_data", "ecg_txt_data"))
        return path_filenames

    def test_remove_rr_outliers_ArrayNotEmpty(self):
        tf = TestFiltering()
        filepaths = tf.main()

        ns = parse_cmd_arguments()
        # pass the namespace containing the args to read the config file
        config_file = parse_config_file(ns)

        filepaths = get_absolute_file_names(config_file.get("ecg_data", "ecg_txt_data"))

        for fn in filepaths:
            if not os.path.isfile(fn):
                print("Warning in create_images method: " + fn + " does not exists.")
                continue

            try:
                # can be used float16 for gpu usage, lowers memory to train larger models
                # less time for data transfers
                patient_array = np.genfromtxt(fn, delimiter='\n', dtype=np.float64)
            except Exception as err:
                print("Error in create_images method: " + err)
                logging.exception("txt couldn't properly parsed")
                raise err

        returned_array = upper_threshold(patient_array)
        assert returned_array.size != 0, "the patient arrays was empty after filtering from upper_threshold()"

    def test_upper_threshold(self):
        tf = TestFiltering()
        filepaths = tf.main()

        for fn in filepaths:
            if not os.path.isfile(fn):
                print(fn + ": file does not exist.")
                continue

            try:
                patient_array = np.genfromtxt(fn, delimiter='\n', dtype=np.float64)
            except Exception as err:
                print("Error while reading text file: " + err)
                logging.exception("txt couldn't properly parsed")
                raise err

        processed_array = upper_threshold(patient_array)
        check_values = np.where(processed_array > 10)[0]  # first position of the array has the values
        assert check_values.size == 0, "There are values in the array above the threshold of 10"


if __name__ == '__main__':
    TestFiltering.main()
