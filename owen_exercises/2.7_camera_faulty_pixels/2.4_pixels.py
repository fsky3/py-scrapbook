#!/usr/bin/python3

# exercise 2.7 in Owen's Practical Signal Processing

from PIL import Image
import random as rand

# luminance mode constants
L_WHITE = 255
L_BLACK = 0

# proportion - tuple, (0.5, 0.5) -> half white, half black
# coverage - 0.1 -> 10% pixels broken
def scatter_bad_pixels(image, proportion = (0.5, 0.5), coverage = 0.5):
    for column in range(image.size[0]):
        for row in range(image.size[1]):
            # is it time to put bad pixel?
            if rand.choices((False, True), (1 - coverage, coverage)).pop():
                # which kind of bad pixel, white or black?
                image.putpixel((column, row), rand.choices((L_WHITE, L_BLACK), proportion).pop())

def scatter_neighbor_pixels(image, coverage = 0.5):
    for column in range(image.size[0]):
        for row in range(image.size[1]):
            # is it time to put neighbor pixel?
            if rand.choices((False, True), (1 - coverage, coverage)).pop():
                image.putpixel((column, row), image.getpixel((column - 1, row)))

region = Image.open("mosque.png")
scatter_bad_pixels(region, (0, 1), 0.19)
region.save("region_bad_pixels.ppm")
region.close()

region = Image.open("mosque.png")
scatter_neighbor_pixels(region, 0.19)
region.save("region_neighbor_pixels.ppm")
region.close()
