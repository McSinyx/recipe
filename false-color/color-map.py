#!/usr/bin/env python3
from cv2 import (COLORMAP_TURBO, IMREAD_GRAYSCALE,
                 IMWRITE_PNG_COMPRESSION, applyColorMap as colormap,
                 imread, imshow, imwrite, waitKey as wait_key)
from numpy import uint8


def disp(image, name):
    """Display the given image."""
    imshow(name, image.astype(uint8))
    wait_key()


heightmapper = imread('heightmapper.png', IMREAD_GRAYSCALE)
heightmapper_turbo = colormap(heightmapper, COLORMAP_TURBO)
disp(heightmapper, 'original')
disp(heightmapper_turbo, 'colormapped')
imwrite('heightmapper-turbo.png', heightmapper_turbo,
        (IMWRITE_PNG_COMPRESSION, 9))
