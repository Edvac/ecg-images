import numpy as np

from ecg_to_images.image_types.a_2d.rrpeaks_to_square_array import convert_to_snake_two_dim_array, \
    convert_to_normal_two_dim_array

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

