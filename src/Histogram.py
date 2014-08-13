"""
    File: Histogram.py
    By: Fredrick Stakem
    Date: 8.11.14

    Purpose: To perform histogram on image data
"""

# Libraries
from __future__ import division

import os
from scipy.misc import imread
from scipy.misc import imsave
import matplotlib.pyplot as plt
import ipdb



# Main
print os.path.dirname(os.path.abspath(__file__))
filename = './img/outside_1.jpg'
output_filename = './img/outside_gray_1.jpg'

filename = './img/left_1.jpg'
output_filename = './img/left_gray_1.jpg'

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
#ipdb.set_trace()

imsave(output_filename, scaled_luminance_image)

# Luminance histogram
# This method is not really needed is you use numpy flatten
#hist_data = [0 for x in range(256)]
#for x in range(len(scaled_luminance_image[:, 0])):
#    for y in range(len(scaled_luminance_image[0, :])):
#        hist_data[ scaled_luminance_image[x, y] ] += 1

#assert sum(hist_data) == 921600

flat_data = scaled_luminance_image.flatten()
plt.hist(flat_data, 256)

plt.show()
#ipdb.set_trace()


# Serarate color channel histogram




#plt.hist(image_data.flatten(), 256, range=(0.0,1.0), fc='k', ec='k')
#plt.show()

