#!/usr/bin/env python3
from cv2 import COLOR_BGR2LAB, COLOR_LAB2BGR, cvtColor, imread, imshow, waitKey
from numpy import average


def grayworld_assumption(img):
    result = cvtColor(img, COLOR_BGR2LAB)
    avg_a = average(result[:, :, 1])
    avg_b = average(result[:, :, 2])
    result[:, :, 1] = (result[:, :, 1]
                       - (avg_a - 128)*(result[:, :, 0] / 255)*1.1)
    result[:, :, 2] = (result[:, :, 2]
                       - (avg_b - 128)*(result[:, :, 0] / 255)*1.1)
    result = cvtColor(result, COLOR_LAB2BGR)
    return result


if __name__ == '__main__':
    img = imread('before_img.png')
    imshow('Origin', img)
    waitKey()

    res = grayworld_assumption(img)
    imshow('Grayworld Assumption', res)
    waitKey()