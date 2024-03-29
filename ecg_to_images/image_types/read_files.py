import os
import sys
import numpy as np

from ecg_to_images.image_types.save_images import get_absolute_file_names


def read_patient_rr_intervals(self, options):
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
        self.create_window_image(self, patient_array, filename_base_name, options)
