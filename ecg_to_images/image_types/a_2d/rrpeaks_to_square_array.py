import numpy as np
import math
from gmpy2 import is_square


def get_side_length(options):

    size = int(options['image']['size'])
    # side of the square
    if is_square(size):
        side = math.sqrt(size)
        return math.floor(side)
    else:
        raise str(size)+"Is not a perfect square"


def convert_to_normal_two_dim_array(one_dim_array: np.ndarray, options) -> np.ndarray:
    """Creates square images and pads with zeros the last image if needed.
    Every patient has images with same size, but different number of images.

    Args:
        one_dim_array (ndarray): numpy 1d array with the preproccesed rr peaks
        options (ConfigParser):  configuration file
    Returns:
        ndarray: two dimentional numpy array
    """
    side = int(get_side_length(options)) # width and height of the image
    two_dim_array = np.zeros((side, side), dtype=np.float64)
    k = 0
    for i in range(0, side):
        for j in range(0, side):
            two_dim_array[i][j] = one_dim_array[k]
            if k + 1 < one_dim_array.size:
                k += 1
            else:
                return two_dim_array


def convert_to_snake_two_dim_array(one_dim_array, options):
    """Creates square images and pads with zeros the last image if needed.
    Every patient has images with same size, but different number of images.
    The first row of the image is filled with rr peak info from left to right.
    Next row from right to left. Next after from left to right and so on.

    Args:
        one_dim_array (ndarray): numpy 1d array with the preproccesed rr peaks
        options (ConfigParser): configuration file

    Returns:
        ndarray: a 2d array
    """
    side = int(get_side_length(options)) # width and height of the image
    two_dim_array = np.zeros((side, side), dtype=np.float64)

    k = 0
    for i in range(0, side):
        # check if 'i' is even or odd to 'turn' like a snake
        if i % 2 == 0:
            for j in range(0, side):
                two_dim_array[i][j] = one_dim_array[k]
                if k + 1 < one_dim_array.size:
                    k += 1
                else:
                    return two_dim_array
        else:
            for j in range((side-1), -1, -1):
                two_dim_array[i][j] = one_dim_array[k]
                if k + 1 < one_dim_array.size:
                    k += 1
                else:
                    return two_dim_array
<<<<<<< HEAD
            turn = True


def convert_to_normal_two_dim_array(one_dim_array, options):
    """Convert 1d array to 2d using normal pattern

    :param ndarray one_dim_array: 40 value array.
    :returns: ndarray two_dim_array: two_dim_array20x20 which will be used for image creation.
    :rtype: ndarray
    """

    # if two_dim_array is not set to zero will include values
    # from the previous image because rr_array.size $ 400 != 0

    one_dim_array_size = one_dim_array.size
    side = int(get_side_length(options)) # width and height of the image
    two_dim_array = np.zeros((side, side), dtype=one_dim_array.dtype)
    k = 0
    for i in range(0, side):
        for j in range(0, side):
            two_dim_array[i][j] = one_dim_array[k]
            if k + 1 < one_dim_array_size:
                k += 1
            else:
                return two_dim_array
=======
>>>>>>> c9932bc5aaf8f078381f3122eb7dc4ba08d4b633
