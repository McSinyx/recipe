#!/usr/bin/env python3
from cv2 import imread, imshow, waitKey
from numpy import transpose


def chromabe(blue, green, red, h, w, threshold):
    for i in range(0, h):
        b, g, r = blue[:, i], green[:, i], red[:, i]
        for j in range(1, w - 1):
            # find the edge base on green channel
            if abs(g[j + 1] - g[j - 1]) >= threshold:
                # Sign of the edge
                sign = 1 if (g[j + 1] - g[j - 1]) > 0 else -1
                # find correction range on boundary
                lrange, rrange = j - 1, j + 1
                while lrange > 0:
                    bgrad = sign * (b[lrange + 1] - b[lrange - 1])
                    ggrad = sign * (g[lrange + 1] - g[lrange - 1])
                    rgrad = sign * (r[lrange + 1] - r[lrange - 1])
                    if max(bgrad, ggrad, rgrad) < threshold: break
                    lrange -= 1
                lrange += 1
                while rrange < w - 1:
                    bgrad = sign * (b[rrange + 1] - b[rrange - 1])
                    ggrad = sign * (g[rrange + 1] - g[rrange - 1])
                    rgrad = sign * (r[rrange + 1] - r[rrange - 1])
                    if max(bgrad, ggrad, rgrad) < threshold: break
                    rrange += 1
                rrange -= 1
                bgmax = max(b[lrange] - g[lrange], b[rrange] - g[rrange])
                bgmin = min(b[lrange] - g[lrange], b[rrange] - g[rrange])
                rgmax = max(r[lrange] - g[lrange], r[rrange] - g[rrange])
                rgmin = min(r[lrange] - g[lrange], r[rrange] - g[rrange])
                for m in range(lrange, rrange):
                    bdiff, rdiff = b[m] - g[m], r[m] - g[m]
                    # Replace the B or R value if the color difference
                    # of B/G and R/G is higher/lesser than the max/min
                    # color difference on range boundary
                    if bdiff > bgmax:
                        b[m] = bgmax + g[m]
                    elif bdiff < bgmin:
                        b[m] = bgmin + g[m]
                    if rdiff > rgmax:
                        r[m] = rgmax + g[m]
                    elif rdiff < rgmin:
                        r[m] = rgmin + g[m]
                j = rrange - 2


def chroma_abbe_corr(src):
    b, g, r = src[:, :, 0], src[:, :, 1], src[:, :, 2]
    threshold = 20

    chromabe(b, g, r, src.shape[0], src.shape[1], threshold)

    b = transpose(b)
    g = transpose(g)
    r = transpose(r)

    chromabe(b, g, r, src.shape[0], src.shape[1], threshold)

    src[:, :, 0], src[:, :, 1], src[:, :, 2] = b, g, r
    return src


img = imread('ca4_before.png')

imshow('Origin', img)
waitKey()

res = chroma_abbe_corr(img)
imshow('Corrected', res)
waitKey()
