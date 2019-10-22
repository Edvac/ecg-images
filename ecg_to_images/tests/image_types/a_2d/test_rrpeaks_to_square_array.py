import numpy as np
from gmpy2 import is_square

from ecg_to_images.image_types.a_2d.rrpeaks_to_square_array import convert_to_snake_two_dim_array, \
    convert_to_normal_two_dim_array, get_side_length


def test_get_side_length():
    options = {"image": {"size": "16384"}}
    if is_square(int(options['image']['size'])):
        rectangle_side = get_side_length(options)

        assert rectangle_side is not None, "Size is NoneType"
        assert isinstance(rectangle_side, int), "Size is not integer"


def test_convert_to_normal_two_dim_array_TwoDim():

    options = { "image": {"size": "36"} }
    test_array = np.arange(36)

    two_dim_array = convert_to_normal_two_dim_array(test_array, options)
    assert two_dim_array.ndim == 2, "Normal array is not 2D"

def test_convert_to_normal_two_dim_array_NotEmpty():
    options = {"image": {"size": "40000"}}
    test_array = np.arange(40000)

    two_dim_array = convert_to_normal_two_dim_array(test_array, options)
    assert two_dim_array.size != 0, "The array is empty"

def test_convert_to_snake_two_dim_array_TwoDim():

    options = { "image": {"size": "25"} }
    test_array = np.arange(25)

    two_dim_array = convert_to_snake_two_dim_array(test_array, options)
    assert two_dim_array.ndim == 2, "Snake array is not 2D"

def test_convert_to_snake_two_dim_array_NotEmpty():
    options = {"image": {"size": "9801"}}
    test_array = np.arange(9801)

    two_dim_array = convert_to_snake_two_dim_array(test_array, options)
    assert two_dim_array.size != 0, "The array is empty"

