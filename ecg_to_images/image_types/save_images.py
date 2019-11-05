import logging
import math
import os
import numpy as np
import scipy
import imageio
import cv2
import mahotas as mh
import skimage
import png


def save_image(image_array_2d, folder_name, filename):
# def save_image(img, folder_name, filename):
    """Create directories for each patient and store their's image files"""

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

    # img.save(folder_name + "/" + filename + ".png")
    # skimage.io.imsave(folder_name + "/" + filename + ".png", image_array_2d)


    # side = image_array_2d.shape[0]
    # f = open(folder_name + "/" + filename + ".png", 'wb')
    # w = png.Writer(side, side, greyscale=True)
    # w.write(f, image_array_2d)
    # f.close()
    # cv2.imwrite(folder_name + "/" + filename + ".png", image_array_2d)

    # mh.imsave(folder_name + "/" + filename + ".png", image_array_2d.astype(np.uint8))

    # imageio.imsave(folder_name + "/" + filename + ".png", image_array_2d.astype(np.uint8))
    print("Saving image for patient: " + filename)

def get_absolute_file_names(directory_name):
    return [os.path.join(directory_name, f) for f in os.listdir(directory_name) if f.endswith('.txt')]

