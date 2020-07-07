#!/usr/bin/env python3
from itertools import starmap

from cv2 import imread, imshow, waitKey as wait_key
from numpy import reshape, uint8


def hhu(func):
    return lambda a, b, c: [int(i*255) for i in func(a/255, b/255, c/255)]


@hhu
def bgr_to_hsv(b, g, r):
    """Convert a pixel in BGR to HSV."""
    minc, maxc = min(r, g, b), max(r, g, b)
    if minc == maxc: return 0.0, 0.0, maxc
    diff = maxc - minc
    sat = diff / maxc
    rc, gc, bc = (maxc-r)/diff, (maxc-g)/diff, (maxc-b)/diff
    if r == maxc: return (bc-gc)/6%1, sat, maxc
    if g == maxc: return (2.0+rc-bc)/6%1, sat, maxc
    if b == maxc: return (4.0+gc-rc)/6%1, sat, maxc


@hhu
def hsv_to_bgr(h, s, v):
    """Convert a pixel in HSV to BGR."""
    if s == 0.0: return v, v, v
    f = h * 6 % 1
    p = v * (1 - s)
    q = v * (1 - s*f)
    t = v * (1 - s*(1 - f))
    i = int(h*6%6)
    if i == 0: return p, t, v
    if i == 1: return p, v, q
    if i == 2: return t, v, p
    if i == 3: return v, q, p
    if i == 4: return v, p, t
    if i == 5: return q, p, v


def convert_color(image, func):
    x, y, z = image.shape
    return reshape(list(starmap(func, reshape(image, (x*y, z)))), (x, y, z))


def disp(image, name):
    """Display the given image."""
    imshow(name, image.astype(uint8))
    wait_key()


if __name__ == '__main__':
    im = imread('heightmapper.png')
    disp(im, 'original')
    disp(convert_color(convert_color(im, bgr_to_hsv), hsv_to_bgr),
         'converted to HSV back and forth')
