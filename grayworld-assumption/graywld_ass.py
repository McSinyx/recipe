from cv2 import (COLOR_BGR2LAB, COLOR_LAB2BGR, cvtColor,
                 imread, imshow, merge, split, waitKey)


def avg_a_b(lab_img, w, h):
    sum_a = 0
    sum_b = 0
    l, a, b = split(lab_img)
    # first find average color in CIE Lab space
    for y in range(h - 1):
        for x in range(w - 1):
            sum_a, sum_b = sum_a + a[x, y], sum_b + b[x, y]

    avg_a = sum_a / (w * h)
    avg_b = sum_b / (w * h)
    return avg_a, avg_b


def shift_a_b(lab_img, a_shift, b_shift, w, h):
    l, a, b = split(lab_img)

    for y in range(h):
        for x in range(w):
            # scale the chroma distance shifted according to amount of
            # luminance. The 1.1 overshoot is because we cannot be sure
            # to have gotten the data in the first place.
            a_delta = a_shift * (l[x, y] / 100) * 1.1
            b_delta = b_shift * (l[x, y] / 100) * 1.1
            a[x, y], b[x, y] = a[x, y] + a_delta, b[x, y] + b_delta
    gwa = merge((l, a, b))
    return cvtColor(gwa, COLOR_LAB2BGR)


def grayworld_assumption(img):
    lab_img = cvtColor(img, COLOR_BGR2LAB)
    w, h = lab_img.shape[0], lab_img.shape[1]
    avg_a, avg_b = avg_a_b(lab_img, w, h)
    return shift_a_b(lab_img, -avg_a, -avg_b, w, h)


img = imread('before_img.png')
imshow('Origin', img)
waitKey()

res = grayworld_assumption(img)
imshow('Grayworld Assumption', res)
waitKey()
