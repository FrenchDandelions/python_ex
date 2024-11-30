from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def main() -> None:
    load = ft_load("animal.jpeg")
    print(load)
    gray_image = Image.fromarray(load).convert("L")
    gray_array = np.array(gray_image)
    w, h = gray_image.size
    left = (w // 2) - 200
    right = left + 400
    upper = (h // 2) - 200
    lower = upper + 400
    img = gray_image.crop((left, upper, right, lower))
    img.show()
    zoomed_array = gray_array[upper:lower, left:right]
    
    # Add a new axis for consistency if needed
    r_zoom = zoomed_array[:, :, np.newaxis] if len(zoomed_array.shape) == 2 else zoomed_array
    
    # Print the new shape and its content
    shape = r_zoom.shape
    print("New shape after slicing:", shape, "or", shape[:2])
    print(r_zoom)
    img = Image.fromarray(zoomed_array).convert("RGB")
    img.save("zoomed_img.jpeg")
    plt.imshow(Image.fromarray(zoomed_array),cmap='Greys',  interpolation='nearest')
    plt.axis('on')
    plt.show()
    # img = img.crop((400, 100, 800, 500))
    # img.show()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(type(e).__name__, e)
