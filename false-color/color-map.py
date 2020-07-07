#!/usr/bin/env python3
from csv import reader

from cv2 import (COLORMAP_TURBO, IMREAD_GRAYSCALE,
                 IMWRITE_PNG_COMPRESSION, applyColorMap as colormap,
                 imread, imshow, imwrite, waitKey as wait_key)
from numpy import stack, uint8, vectorize

PNG_COMPRESSION = IMWRITE_PNG_COMPRESSION, 9
with open('turbo.csv') as turbo: TURBO = list(reader(turbo))


def disp(image, name):
    """Display the given image."""
    imshow(name, image)
    wait_key()


def map_color(grey, mapping):
    """Return a color image from the given grey image and mapping."""
    r = vectorize(lambda i: mapping[i][0])
    g = vectorize(lambda i: mapping[i][1])
    b = vectorize(lambda i: mapping[i][2])
    # OpenCV uses BGR by default for whatever reason.
    return stack((b(grey), g(grey), r(grey)), axis=-1).astype(uint8)


if __name__ == '__main__':
    heightmapper = imread('heightmapper.png', IMREAD_GRAYSCALE)
    heightmapper_opencv = colormap(heightmapper, COLORMAP_TURBO)
    heightmapper_manual = map_color(heightmapper, TURBO)
    disp(heightmapper, 'original')
    disp(heightmapper_opencv, "OpenCV's turbo")
    disp(heightmapper_manual, 'manually mapped turbo')
    imwrite('heightmapper-opencv.png', heightmapper_opencv, PNG_COMPRESSION)
    imwrite('heightmapper-manual.png', heightmapper_manual, PNG_COMPRESSION)
