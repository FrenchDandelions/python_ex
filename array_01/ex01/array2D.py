import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """slice_me takes as parameters a 2D array, prints its shape, and returns a
truncated version of the array based on the provided start and end arguments"""
    if isinstance(family, list) is not True:
        raise ValueError("The 'family' element should be a list")
    if isinstance(start, int) is not True or isinstance(end, int) is not True:
        raise ValueError("'start' and 'end' elements should be integers")
    family = np.array(family)
    print("My shape is :", np.shape(family))
    family = np.array(family)[start: end]
    print("My new shape is :", np.shape(family))
    return family.tolist()
