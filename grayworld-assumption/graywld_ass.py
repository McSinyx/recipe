from cv2 import imread, imshow, waitKey, cvtColor, COLOR_BGR2LAB, COLOR_LAB2BGR
from numpy import average


def grayworld_assumption(img):
    result = cvtColor(img, COLOR_BGR2LAB)
    avg_a = average(result[:, :, 1])
    avg_b = average(result[:, :, 2])
    result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result = cvtColor(result, COLOR_LAB2BGR)
    return result


img = imread('before_img.png')
imshow('Origin', img)
res = grayworld_assumption(img)
imshow('Grayworld Assumption', res)
waitKey()
