#!/usr/bin/env python3
from cv2 import imread, imshow, merge, waitKey


def chromabe(blue, green, red, h, w, threshold):
    for i in range(0, h):
        b, g, r = blue[:, i], green[:, i], red[:, i]
        for j in range(1, w-1):
            if abs(g[j + 1] - g[j - 1]) < threshold: continue
            sign = 1 if (g[j+1] - g[j-1]) > 0 else -1
            lrange, rrange = j-1, j+1
            while lrange > 0:
                lrange -= 1
                bgrad = sign * (b[lrange+1] - b[lrange-1])
                ggrad = sign * (g[lrange+1] - g[lrange-1])
                rgrad = sign * (r[lrange+1] - r[lrange-1])
                if max(bgrad, ggrad, rgrad) < threshold: break
            lrange -= 1
            while rrange < w - 1:
                rrange += 1
                bgrad = sign * (b[rrange+1] - b[rrange-1])
                ggrad = sign * (g[rrange+1] - g[rrange-1])
                rgrad = sign * (r[rrange+1] - r[rrange-1])
                if max(bgrad, ggrad, rgrad) < threshold: break
            rrange += 1
            bgmax = max(b[lrange]-g[lrange], b[rrange]-g[rrange])
            bgmin = min(b[lrange]-g[lrange], b[rrange]-g[rrange])
            rgmax = max(r[lrange]-g[lrange], r[rrange]-g[rrange])
            rgmin = min(r[lrange]-g[lrange], r[rrange]-g[rrange])
            for m in range(lrange, rrange + 1):
                bdiff, rdiff = b[m] - g[m], r[m] - g[m]
                if bdiff > bgmax:
                    b[m] = bgmax + g[m]
                elif bdiff < bgmin:
                    b[m] = bgmin + g[m]
                if rdiff > rgmax:
                    r[m] = rgmax + g[m]
                elif rdiff < rgmin:
                    r[m] = rgmin + g[m]
            j = rrange - 2


def chroma_abbe_corr(src, res):
    b, g, r = src[:, :, 0], src[:, :, 1], src[:, :, 2]
    threshold = 10

    chromabe(b, g, r, src.shape[0], src.shape[1], threshold)
    merge([b, g, r], res)


img = imread('ca4_before.png')
res = None

imshow('Origin', img)

chroma_abbe_corr(img, res)
imshow('Corrected', res)
waitKey(0)
