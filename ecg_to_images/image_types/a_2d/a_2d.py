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


from ecg_to_images.preprocessing.preprocessing import preprocessing as preproc
from ecg_to_images.image_types.a_2d.rr_intervals_to_square_array import convert_to_snake_two_dim_array, \
    convert_to_normal_two_dim_array
from ecg_to_images.image_types.custom_exceptions import ImagePatternError
from ecg_to_images.image_types.read_files import read_patient_rr_intervals
from ecg_to_images.image_types.save_images import save_image

logger = logging.getLogger(__name__)


class EcgImageA_2D:

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
            logging.debug("attribute should be NORMAL OR SNAKE -_---<-")
            logging.getLogger().exception("Attribute should be normal or snake")
            raise AttributeError("Attribute should be normal or snake")

    @size.deleter
    def size(self):
        del self._size

    @pattern.deleter
    def pattern(self):
        del self._pattern

    def create_images(self, options):
        read_patient_rr_intervals(self, options)

    def create_window_image(self, patient_array, filename_base_name, options):

        processed_pa = preproc(patient_array, options)
        
        it = 0
        while it < processed_pa.size:
            # slices go only until the last value, even if it + image_array_size > patient_array.size
            img = EcgImageA_2D(int(options['image']['size']), options['image']['pattern'])

            image_array = processed_pa[it: it + img.size]

            if img.pattern == ImagePattern.NORMAL:
                image_array_2d = convert_to_normal_two_dim_array(image_array, options)
                save_folder_name = os.path.join(os.path.join(options.get('output', 'img_dir'), "normal_pattern"),
                                                filename_base_name)

            elif img.pattern == ImagePattern.SNAKE:
                image_array_2d = convert_to_snake_two_dim_array(image_array, options)
                save_folder_name = os.path.join(os.path.join(options.get('output', 'img_dir'), "snake_pattern"),
                                                filename_base_name)
            else:
                print("Warning: unknown image pattern (use NORMAL or SNAKE) ")
                continue

            image = Image.fromarray(np.uint8(image_array_2d), "L")

            save_image(image, save_folder_name, filename_base_name + str(it + 1) + "-" + str(it + img.size))

            it = it + img.size  # moving the 'offset'


class ImagePattern(Enum):
    NORMAL = 1
    SNAKE = 2

    @classmethod
    def has_value(cls, value):
        return value in cls.__members__
