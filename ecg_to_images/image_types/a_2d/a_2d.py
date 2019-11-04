"""
.. module:: project_documentation
    :platform: Win 64bit
    :synopsis: module creating images from 24h RR intervals

.. moduleauthor:: George Politis <g-politis@outlook.com>
"""
import logging
import os
import numpy as np
from enum import Enum

from PIL import Image
from gmpy2 import is_square

from ecg_to_images.image_types.a_2d.rrpeaks_to_square_array import convert_to_snake_two_dim_array, \
    convert_to_normal_two_dim_array
from ecg_to_images.image_types.custom_exceptions import ImagePatternError
from ecg_to_images.image_types.read_files import read_patient_rrppeaks
from ecg_to_images.image_types.save_images import save_image

logger = logging.getLogger(__name__)


class EcgImagesA_2D:

    def __init__(self, size, pattern):
        if size < 0:
            raise TypeError("size must be a positive number")
        k = 0 <= size <= 1000000
        r = is_square(size)
        if 0 <= size <= 1000000 and is_square(size):
            self._size = size
        else:
            logger.error("size must be a perfect square and between 0 and 1000000")
            raise ValueError("size must be a perfect square and between 0 and 1000000")

        if pattern == "NORMAL":
            self._pattern = ImagePattern.NORMAL
        elif pattern == "SNAKE":
            self._pattern = ImagePattern.SNAKE
        else:
            try:
                raise ImagePatternError('Attribute should be NORMAL or SNAKE')
            except ImagePatternError as err:
                logger.error(err.args, exc_info=True)
                raise

    @property
    def size(self):
        return self._size

    @property
    def pattern(self):
        return self._pattern

    @size.setter
    def size(self, value):
        if value < 0:
            raise TypeError("size must be a positive number")
        if 0 <= value <= 1000000 & is_square(value):
            self._size = int(value)
        else:
            raise ValueError("size must be a perfect square and between 0 and 1000000")

    @pattern.setter
    def pattern(self, value):
        if value == "NORMAL":
            self._pattern = ImagePattern.NORMAL
        elif value == "SNAKE":
            self._pattern = ImagePattern.SNAKE
        else:
            logging.debug("attributer should be NORMAL OR SNAKE -_---<-")
            logging.getLogger().exception("Attribute should be normal or snake")
            raise AttributeError("Attribute should be normal or snake")

    @size.deleter
    def size(self):
        del self._size

    @pattern.deleter
    def pattern(self):
        del self._pattern

    def create_images(self, options):

        if int(options['image']['size']) > 0:
            read_patient_rrppeaks(self, options)
        else:
            raise Exception("image size should be > 0")

    def create_window_image(self, processed_pa, filename_base_name, options):
        it = 0
        while it < processed_pa.size:
            # slices go only until the last value, even if it + image_array_size > patient_array.size
            img = EcgImagesA_2D(int(options['image']['size']), options['image']['pattern'])

            image_array = processed_pa[it: it + img.size]

            if img.pattern == ImagePattern.NORMAL:
                image_array_2d = convert_to_normal_two_dim_array(image_array, options)
                save_folder_name = os.path.join(os.path.join(os.path.join(options.get('output', 'img_dir'),
                                                                          "normal_pattern"), "a_2d"), filename_base_name)
            elif img.pattern == ImagePattern.SNAKE:
                image_array_2d = convert_to_snake_two_dim_array(image_array, options)
                save_folder_name = os.path.join(os.path.join(os.path.join(options.get('output', 'img_dir'),
                                                                          "snake_pattern"), 'a_2d'), filename_base_name)
            else:
                print("Warning: unknown image pattern (use NORMAL or SNAKE) ")
                continue

            # or cv2.imwrite(filename,array)
            save_image(image_array_2d,
                       save_folder_name,
                       filename_base_name + str(it + 1) + "-" + str(it + img.size),
                       options)

            it = it + img.size  # moving the 'offset'


class ImagePattern(Enum):
    NORMAL = 1
    SNAKE = 2

    @classmethod
    def has_value(cls, value):
        return value in cls.__members__
