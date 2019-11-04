import logging
import os
import numpy as np
from PIL import Image


def save_image(image_array, folder_name, filename, options):
    """Create directories for each patient and store their's image files"""

    # if options['preprocessing']['rescale'] == 'normalize_to_byte_image':
    #     img = Image.fromarray(np.uint8(image_array), "L")
    # else:
    img = Image.fromarray(image_array, "L")

    if not os.path.isdir(folder_name):
        try:
            # Check if the a patient's directory exists
            os.makedirs(folder_name)
        except OSError:
            if not os.path.isdir(folder_name):
                logging.getLogger().exception("The directory for file: " + filename + " Already exists: ", OSError)
                raise

    # setting decimal precision to 3 as initial dataset
    # np.savetxt("/home/george/Data/RR peaks/shareedb/RR-no-neg/" + filename, positive_pa, fmt='%1.3f')
    img.save(folder_name + "/" + filename + ".png")
    print("Saving image for patient: " + filename)
