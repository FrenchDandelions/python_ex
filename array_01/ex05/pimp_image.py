import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib


def _show_image(array):
    """This function is used to plot an image based on a array"""
    matplotlib.use("TkAgg")
    plt.imshow(Image.fromarray(array))
    plt.axis('on')
    plt.show()


def ft_invert(array) -> np.array:
    """This function inverts the values of the pixels of the array
    like 0 -> 255 or 90 -> 165"""
    n_array = 255 - array
    _show_image(n_array)
    return n_array


def ft_red(array) -> np.array:
    """This function turns the array into a red-only image"""
    n_array = np.array(array)
    n_array[:, :, 1] = 0
    n_array[:, :, 2] = 0
    _show_image(n_array)
    return n_array


def ft_green(array) -> np.array:
    """This function turns the array into a green-only image"""
    n_array = np.array(array)
    n_array[:, :, 0] = 0
    n_array[:, :, 2] = 0
    _show_image(n_array)
    return n_array


def ft_blue(array) -> np.array:
    """This function turns the array into a blue-only image"""
    n_array = np.array(array)
    n_array[:, :, 0] = 0
    n_array[:, :, 1] = 0
    _show_image(n_array)
    return n_array


def ft_grey(array) -> np.array:
    """This function turns the array into a greyscale image"""
    red = array[:, :, 0] / (1 / 0.2989)
    green = array[:, :, 1] / (1 / 0.5870)
    blue = array[:, :, 2] / (1 / 0.1140)
    grey = red + green + blue
    n_array = np.stack([grey] * 3, axis=-1).astype(np.uint8)
    _show_image(n_array)
    return n_array
