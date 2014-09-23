"""
    File: AutoContrast.py
    By: Fredrick Stakem
    Date: 9.22.14

    Purpose: To perform auto contrast on image data
"""

# Libraries
from __future__ import division

import os
import ipdb
from scipy.misc import imread
from scipy.misc import imsave

# Main
print os.path.dirname(os.path.abspath(__file__))

filename = './img/left_1.jpg'

color_image_data = imread(filename)
red_data = color_image_data[:, :, 0]
green_data = color_image_data[:, :, 1]
blue_data = color_image_data[:, :, 2]

scaled_red_data = red_data / 255 * .2126
scaled_green_data = green_data / 255 * .7152
scaled_blue_data = blue_data / 255 * .0722

luminance_image = scaled_red_data + scaled_green_data + scaled_blue_data

scaled_luminance_image = luminance_image * 255
scaled_luminance_image = scaled_luminance_image.astype(int)

flat_data = scaled_luminance_image.flatten()

ipdb.set_trace()