# Specify at the pytest runner the configuration file

import logging
import os
import sys
from unittest import TestCase

import numpy as np

from ecg_to_images.image_types.save_images import get_absolute_file_names
from ecg_to_images.preprocessing.remove_negative_values import remove_negative_values
from ecg_to_images.utils.parse_cmd_args import parse_cmd_arguments
from ecg_to_images.utils.parse_conf_file import parse_config_file

logger = logging.getLogger(__name__)


class TestRemove_negative_values(TestCase):

    def init(self):

        ns = parse_cmd_arguments()
        # pass the namespace containing the args to read the config file
        config_file = parse_config_file(ns)

        path_filenames = get_absolute_file_names(config_file.get("ecg_data", "ecg_txt_data"))
        return path_filenames

    def testArray_NotEmpty(self):
        t = TestRemove_negative_values()
        filepaths = t.init()

        for fn in filepaths:
            if not os.path.isfile(fn):
                print("Warning in create_images method: " + fn + " does not exists.")
                continue

            try:
                # can be used float16 for gpu usage, lowers memory to train larger models
                # less time for data transfers
                patient_array = np.genfromtxt(fn, delimiter='\n', dtype=np.float32)
            except:
                e = sys.exc_info()[0]
                print("Error in create_images method: " + e)
                continue

        assert len(remove_negative_values(patient_array)) is not 0, "the patient array is empty"

    def testValues_NoNegatives(self):
        neg = TestRemove_negative_values()
        filepaths = neg.init()

        for fn in filepaths:
            if not os.path.isfile(fn):
                print("Warning in create_images method: " + fn + " does not exists.")
                continue

            try:
                # can be used float16 for gpu usage, lowers memory to train larger models
                # less time for data transfers
                patient_array = np.genfromtxt(fn, delimiter='\n', dtype=np.float32)
            except:
                e = sys.exc_info()[0]
                print("Error in create_images method: " + e)
                continue

            assert remove_negative_values(patient_array).all() >= 0, "the patient array does not contain negative values"


    def testMostOfTxtData_AreSame(self):
        test_obj = TestRemove_negative_values()
        filepaths = test_obj.init()

        for fn in filepaths:
            if not os.path.isfile(fn):
                print("Warning in create_images method: " + fn + " does not exists.")
                continue

            try:
                # can be used float16 for gpu usage, lowers memory to train larger models
                # less time for data transfers
                patient_array = np.genfromtxt(fn, delimiter='\n', dtype=np.float32)
            except:
                e = sys.exc_info()[0]
                print("Error in create_images method: " + e)
                continue


            # point a copy instead of the having a reference to the actual patient array
            positive_pa_aligned = np.copy(patient_array)
            positive_pa_aligned[positive_pa_aligned < 0] = 0

            print("Total values without original values but adjusted: " + str(len(positive_pa_aligned))
                  + "| Total values with negatives: "
                  + str(len(patient_array)) +" "+  str(np.allclose(patient_array, positive_pa_aligned,1,1)))

            if np.allclose(patient_array, positive_pa_aligned, 1, 1):
                print("OK")
            else:
                print("Original Shape: " + str(patient_array.shape) + "aligned: " + str(positive_pa_aligned.shape))

            try:
                similarity_percentage = np.sum(patient_array == positive_pa_aligned) * 100 / patient_array.size
                # similarity_percentage = np.sum(patient_array == positive_patient_array) * 100 / patient_array.size
            except ZeroDivisionError as err:
                logger.error(err.args, exc_info=True)
                raise

            print("Initial version is :" + str(similarity_percentage) + "% similar in terms of same values"
                                                                        "with the array without negative values")
            assert similarity_percentage > 99.99