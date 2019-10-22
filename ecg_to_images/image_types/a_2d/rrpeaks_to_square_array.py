import numpy as np
import math

from gmpy2 import is_square


def get_side_length(options):
    size = int(options['image']['size'])
    # side of the rectangle
    if is_square(size):
        side = math.sqrt(size)
        return math.floor(side)
    else:
        raise str(size)+"Is not a perfect square"

def convert_to_snake_two_dim_array(one_dim_array, options):
    """Convert 1d array to 2d using snake pattern

    :param ndarray one_dim_array: 40 value array.
    :returns: ndarray two_dim_array: two_dim_array20x20 which will be used for image creation.
    :rtype: ndarray

    """

    # if two_dim_array is not set to zero will include values
    # from the previous image because rr_array.size $ 400 != 0
    side = int(get_side_length(options)) # width and height of the image
    two_dim_array = np.zeros((side, side), dtype=np.float64)

    one_dim_array_size = one_dim_array.size

    k = 0
    turn = False
    for i in range(0, side):
        if turn is True:
            for j in range(side - 1, -1, -1):
                two_dim_array[i][j] = one_dim_array[k]
                # check if one_dim_array < 20x20, for the last chunk
                if k + 1 < one_dim_array_size:
                    k += 1
                else:
                    return two_dim_array
            turn = False
        elif turn is False:
            for j in range(0, side):
                two_dim_array[i][j] = one_dim_array[k]
                if k + 1 < one_dim_array_size:
                    k += 1
                else:
                    return two_dim_array
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
    two_dim_array = np.zeros((side, side), dtype=np.float64)
    k = 0
    for i in range(0, side):
        for j in range(0, side):
            two_dim_array[i][j] = one_dim_array[k]
            if k + 1 < one_dim_array_size:
                k += 1
            else:
                return two_dim_array