import argparse
import time

from ecg_to_images import image_types
from .image_types.a_2d import create_images
from .image_types.a_1d import create_images
from .image_types.b_2d import create_images
from .image_types.b_1d import create_images
from .image_types.c_2d import create_images
from .image_types.c_1d import create_images

from .config_parser import read_config_file
from enum import Enum

def main():

    start = time.perf_counter()
    ap = argparse.ArgumentParser(description='Ecg-to-image converter tool')
    # use the default configuration files that it is inside the package
    ap.add_argument('-c',
                    '--config',
                    dest='config',
                    nargs = '?',
                    required=True,
                    help='You have to specify the full absolute path to the configuration file')
    ns = ap.parse_args()

    # pass the namespace to read the file
    options = read_config_file(ns)

    # test if the dictionary with the config is empty
    if not options:

        # get the type of the image specified at the configuration file
        image_type = options.get('i_type')
        # call the method of the module dynamically using reflection to avoid typing 6 ifs
        getattr(image_type.lower(),create_images())()


    end = time.perf_counter()
    elapsed = end - start
    print('The convetion took: {} seconds'.format(elapsed))

class ImageType(Enum):
    A_2D = 1
    A_1D = 2
    B_2D = 3
    B_1D = 4
    C_2D = 5
    C_1D = 6

    @classmethod
    def has_value(cls, value):
        return value in cls.__members__