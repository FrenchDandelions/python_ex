from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib


def main() -> None:
    """
    This is the main function of the project, it
    loads the image animal.jpeg, put in in black and
    white and slice the array to have a zoom like
    effect when loading the new array. Before loading
    it we use the Image lib to rotate the image directly.
    """
    matplotlib.use('TkAgg')
    load = ft_load("animal.jpeg")

    gray_image = Image.fromarray(load).convert("L")
    gray_array = np.array(gray_image, copy=True)

    w, h = gray_image.size
    left = (w // 2) - 200
    right = left + 400
    upper = (h // 2) - 200
    lower = upper + 400

    zoomed_array = gray_array[upper:lower, left:right]

    # Add a new axis for consistency if needed
    shape = zoomed_array.shape
    len_shape = len(shape)
    r_zoom = zoomed_array[:, :, np.newaxis] if len_shape == 2 else zoomed_array

    new_axis_shape = r_zoom.shape
    print("The shape of image is:", new_axis_shape, "or", shape)
    print(r_zoom)

    img = Image.fromarray(zoomed_array).rotate(90)
    zoomed_array = np.array(img, copy=True)[::-1]
    img = Image.fromarray(zoomed_array)
    rotated_array = np.array(img, copy=True)
    transpose = rotated_array.T

    print("New shape after Transpose:", transpose.shape)
    print(transpose)

    img.save("rotated_img.jpeg")
    plt.imshow(img, cmap="gray")
    plt.axis('on')
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(type(e).__name__, e)
