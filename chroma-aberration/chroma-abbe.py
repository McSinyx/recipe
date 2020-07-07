from cv2 import imread, imshow, waitKey, merge
from numpy import asarray


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

                    # Replace the B or R value if the color difference of B/G and R/G is higher/lesser
                    # than maximum/minimum of color difference on range boundary
                    b[m] = bgmax + g[m] if bdiff > bgmax else bgmin + g[m] if bdiff < bgmin else b[m]
                    r[m] = rgmax + g[m] if rdiff > rgmax else rgmin + g[m] if rdiff < rgmin else r[m]
                j = rrange - 2


def chroma_abbe_corr(src, res):
    b, g, r = src[:, :, 0], src[:, :, 1], src[:, :, 2]
    threshold = 10

    chromabe(b, g, r, src.shape[0], src.shape[1], threshold)
    merge(asarray([b, g, r]), res)


img = imread('ca4_before.png')
res = None

imshow('Origin', img)

chroma_abbe_corr(img, res)
imshow('Corrected', res)
waitKey(0)
