import numpy as np


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