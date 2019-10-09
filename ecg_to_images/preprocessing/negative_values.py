import sys
import numpy as np
import os

from ecg_to_images.image_types.save_images import get_absolute_file_names


def negative_values(options):

    path_filenames = get_absolute_file_names(options.get("ecg_data", "ecg_txt_data"))

    negative = {}

    for fn in path_filenames:
        if not os.path.isfile(fn):
            print("Warning in create_images method: " + fn + " does not exists.")
            continue

        try:
            patient_array = np.genfromtxt(fn, delimiter='\n', dtype=np.float64)
        except:
            e = sys.exc_info()[0]
            print("Error in create_images method: " + e)
            continue

        filename = os.path.basename(fn)


        if sum(n < 0 for n in patient_array) >= 1:
            negative[filename] = "----negative-----"
        else:
            negative[filename] = "positive"

        print([n for n in patient_array if n < 0])

    return negative