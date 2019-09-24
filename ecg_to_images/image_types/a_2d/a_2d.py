"""
.. module:: project_documentation
    :platform: Win 64bit
    :synopsis: module creating images from 24h RR intervals

.. moduleauthor:: George Politis <g-politis@outlook.com>
"""
import os
import sys
import numpy as np
import ntpath
import logging

from ecg_to_images.image_types.a_2d.signal_to_array import convert_to_snake_two_dim_array, \
    convert_to_normal_two_dim_array
from ecg_to_images.image_types.save_images import get_absolute_file_names, save_image
from PIL import Image
from enum import Enum

from ecg_to_images.preprocessing.Normalize import normalize


class EcgImagesA_2D:


    def __init__(self, size, pattern):
        if 0 <= size <= 10000:
            self._size = size
        else:
            raise ValueError("protected_value must be " +
                             "between 0 and 1000 inclusive")

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
                             "between 0 and 1000 inclusive")

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
        image_array_size = int(options.get("image","size"))

        filenames = get_absolute_file_names(options.get("ecg_data", "ecg_txt_data"))

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

            patient_array_array = normalize(patient_array)
            file_name_base_name = ntpath.basename(fn)

            it = 0
            # global image_array_2d
            while it < patient_array.size:
                # slices go only until the last value, even if it + image_array_size > patient_array.size
                image_array = patient_array[it: it + image_array_size]

                img_obj = EcgImagesA_2D(int(options['image']['size']), options['image']['pattern'])
                # img_obj.pattern = options['image']['pattern']

                if (img_obj.pattern == ImagePattern.NORMAL):
                    image_array_2d = convert_to_snake_two_dim_array(image_array)
                    save_folder_name = os.path.join(os.path.join
                                                    (options.get('output', 'img_dir'), "normal_pattern"),
                                                     file_name_base_name)
                elif img_obj.pattern == ImagePattern.SNAKE:
                    image_array_2d = convert_to_normal_two_dim_array(image_array)
                    save_folder_name = os.path.join(os.path.join
                                                    (options.get('output', 'img_dir'), "snake_pattern"),
                                                    file_name_base_name)
                else:
                    print("Warning: unknown image pattern (use NORMAL or SNAKE) ")
                    continue

                # clear the variable
                image = Image.fromarray(image_array_2d, "L")
                save_image(image, save_folder_name,
                                file_name_base_name + str(it + 1) + "-" + str(it + image_array_size))

                it = it + image_array_size  # moving the 'offset'


class ImagePattern(Enum):
    SNAKE = 1
    NORMAL = 2

    @classmethod
    def has_value(cls, value):
        return value in cls.__members__