from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.array:
    """ft_load loads an image, prints its format,
and its pixels content in RGB format.
This function handles JPG and JPEG format.
An exception is raised if the given path does not exist,
if the given path is not a file and if the given file
is not a JPEG or JPG"""
    if os.path.exists(path) is not True:
        raise FileExistsError("The given path doesn't exist.")
    if os.path.isfile(path) is not True:
        raise TypeError("The given path is not a file.")
    check = path.lower().split(".")
    if check[-1] != "jpeg" and check[-1] != "jpg":
        raise TypeError("The given file is not a .jpg or .jpeg file")
    img = Image.open(path).convert('RGB')
    arr = np.array(img)
    # print("The shape of image is:", arr.shape)
    return arr
