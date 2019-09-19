"""
.. module:: project_documentation
    :platform: Win 64bit
    :synopsis: module creating images from 24h RR intervals

.. moduleauthor:: George Politis <gpolitis@protonmail.com>
"""
import os
import sys
import numpy as np
import ntpath
import logging
from PIL import Image
from enum import Enum


class EcgImagesA_2D:

    def __init__(self, size, pattern):
        self._size = size
        if pattern == "NORMAL":
            self._pattern = ImagePattern.NORMAL
        elif pattern == "SNAKE":
            self._pattern = ImagePattern.SNAKE
        else:
            raise AttributeError("Attribute should be NORMAL or SNAKE")

    @property
    def size(self):  # implements the get - this name is *the* name
        return self._size

    @property
    def pattern(self):  # implements the get - this name is *the* name
        return self._pattern

    @size.setter
    def size(self, value):  # name must be the same
        if value != int(value):
            raise TypeError("protected_value must be an integer")
        if 0 <= value <= 1000:
            self._size = int(value)
        else:
            raise ValueError("protected_value must be " +
                             "between 0 and 100 inclusive")

    @pattern.setter
    def pattern(self, value):  # name must be the same
        if value == "NORMAL":
            self._pattern = ImagePattern.NORMAL
        elif value == "SNAKE":
            self._pattern = ImagePattern.SNAKE
        else:
            logging.getLogger().exception("Attribute should be normal or snake")
            raise AttributeError("Attribute should be normal or snake")

    #
    @size.deleter
    def size(self):  # again, name must be the same
        del self._size

    @pattern.deleter
    def pattern(self):  # again, name must be the same
        del self._pattern

    def create_images(self, options):
        # def create_images(filenames, image_pattern, folder_name):
        """
        :param folder_name:
        :param image_pattern:
        :param filenames: the name of the file
        :returns two_dim_array: two_dim_array20x20 which will be used for image creation.
        :rtype: ndarray
        :raises FileNotFoundError: The filename does not correspond to a patient.
        """

        # n is the number of chunk arrays.size = 400
        # rr_array: patient RRs in an array
        # array_1_of_400: smaller array, size = p
        image_array_size = 400

        filenames = self.get_absolute_file_names(options.get("ecg_data", "ecg_txt_data"))

        for fn in filenames:
            if not os.path.isfile(fn):
                print("Warning in create_images method: " + fn + " does not exists.")
                continue

            try:
                patient_array = np.genfromtxt(fn, delimiter='\n', dtype=np.float64)
            except:
                e = sys.exc_info()[0]
                print("Error in create_images method: " + e)
                continue

            file_name_base_name = ntpath.basename(fn)

            it = 0
            # global image_array_2d
            while it < patient_array.size:
                # slices go only until the last value, even if it + image_array_size > patient_array.size
                image_array = patient_array[it: it + image_array_size]

                img_obj = EcgImagesA_2D(int(options['image']['size']), options['image']['pattern'])
                img_obj.pattern = options['image']['pattern']

                if (img_obj.pattern == ImagePattern.NORMAL):
                    image_array_2d = self.convert_to_snake_two_dim_array(image_array)
                    save_folder_name = os.path.join(os.path.join
                                                    (options.get('output', 'img_dir'), "normal_pattern"),
                                                     file_name_base_name)
                elif img_obj.pattern == ImagePattern.SNAKE:
                    image_array_2d = self.convert_to_normal_two_dim_array(image_array)
                    save_folder_name = os.path.join(os.path.join
                                                    (options.get('output', 'img_dir'), "snake_pattern"),
                                                    file_name_base_name)

                else:
                    print("Warning: unknown image pattern (use NORMAL or SNAKE) ")
                    continue

                # clear the variable

                image = Image.fromarray(image_array_2d, "L")
                self.save_image(image, save_folder_name,
                                file_name_base_name + str(it + 1) + "-" + str(it + image_array_size))

                it = it + image_array_size  # moving the 'offset'

    def save_image(img, folder_name, filename):
        """Create directories for each patient and store their's image files"""

        if not os.path.isdir(folder_name):
            try:
                # Check if the a patient's directory exists
                os.makedirs(folder_name)
            except OSError:
                if not os.path.isdir(folder_name):
                    logging.getLogger().exception("The directory for file: " +filename+ " Already exists: ", OSError)
                    raise

        img.save(folder_name + "/" + filename + ".png")
        print("Saving image for patient: " + filename)
    def convert_to_snake_two_dim_array(one_dim_array):
        """Convert 1d array to 2d using snake pattern

        :param ndarray one_dim_array: 40 value array.
        :returns: ndarray two_dim_array: two_dim_array20x20 which will be used for image creation.
        :rtype: ndarray

        """

        # if two_dim_array is not set to zero will include values
        # from the previous image because rr_array.size $ 400 != 0
        two_dim_array = np.zeros((20, 20), dtype=np.float64)

        one_dim_array_size = one_dim_array.size

        k = 0
        turn = False
        for i in range(0, 20):
            if turn is True:
                for j in range(19, -1, -1):
                    two_dim_array[i][j] = one_dim_array[k]
                    # check if one_dim_array < 20x20, for the last chunk
                    if k + 1 < one_dim_array_size:
                        k += 1
                    else:
                        return two_dim_array
                turn = False
            elif turn is False:
                for j in range(0, 20):
                    two_dim_array[i][j] = one_dim_array[k]
                    if k + 1 < one_dim_array_size:
                        k += 1
                    else:
                        return two_dim_array
                turn = True

    def convert_to_normal_two_dim_array(one_dim_array):
        """Convert 1d array to 2d using normal pattern

        :param ndarray one_dim_array: 40 value array.
        :returns: ndarray two_dim_array: two_dim_array20x20 which will be used for image creation.
        :rtype: ndarray
        """

        # if two_dim_array is not set to zero will include values
        # from the previous image because rr_array.size $ 400 != 0

        one_dim_array_size = one_dim_array.size

        two_dim_array = np.zeros((20, 20), dtype=np.float64)
        k = 0
        for i in range(0, 20):
            for j in range(0, 20):
                two_dim_array[i][j] = one_dim_array[k]
                if k + 1 < one_dim_array_size:
                    k += 1
                else:
                    return two_dim_array

    def get_absolute_file_names(directory_name):
        """
        :param directory_name:
        """
        return [os.path.join(directory_name, f) for f in os.listdir(directory_name) if f.endswith('.txt')]


class ImagePattern(Enum):
    SNAKE = 1
    NORMAL = 2

    @classmethod
    def has_value(cls, value):
        return value in cls.__members__
