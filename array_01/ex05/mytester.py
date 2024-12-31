from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey


array = ft_load("landscape.jpg")

print(ft_invert.__doc__)
print("The shape of image for ft_invert is:", ft_invert(array).shape)

print(ft_red.__doc__)
print("The shape of image for ft_red is:", ft_red(array).shape)

print(ft_green.__doc__)
print("The shape of image for ft_green is:", ft_green(array).shape)

print(ft_blue.__doc__)
print("The shape of image for ft_blue is:", ft_blue(array).shape)

print(ft_grey.__doc__)
print("The shape of image for ft_grey is:", ft_grey(array).shape)
