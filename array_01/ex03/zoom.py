from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib


def main() -> None:
    matplotlib.use('TkAgg')
    load = ft_load("animal.jpeg")
    print(load)

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

    print("New shape after slicing:", new_axis_shape, "or", shape)
    print(r_zoom)

    img = Image.fromarray(zoomed_array)
    img.save("zoomed_img.jpeg")
    plt.imshow(Image.fromarray(zoomed_array), cmap="gray")
    plt.axis('on')
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(type(e).__name__, e)
