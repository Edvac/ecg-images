import os
import sys
import numpy as np

from ecg_to_images.preprocessing.preprocessing import preprocessing as preproc


def read_patient_rrppeaks(self, options):

    filenames = get_absolute_file_names(options.get("ecg_data", "ecg_txt_data"))

    for fn in filenames:
        if not os.path.isfile(fn):
            print("file:" + fn + " does not exists.")
            continue

        try:
            patient_array = np.genfromtxt(fn, delimiter='\n', dtype=np.float64)
        except Exception:
            e = sys.exc_info()[0]
            print("Error while reading RR peaks to numpy array: " + e)
            continue

        filename_base_name = os.path.basename(fn)
        processed_pa = preproc(patient_array, options)
        self.create_window_image(self, processed_pa, filename_base_name, options)

def get_absolute_file_names(directory_name):
    return [os.path.join(directory_name, f) for f in os.listdir(directory_name) if f.endswith('.txt')]