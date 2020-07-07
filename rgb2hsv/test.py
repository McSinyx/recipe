import numpy as np
import matplotlib.pyplot as plt
import cv2
from rgb2hsv import rgb2hsv
#import image using opencv
img = cv2.imread('../waifu white.jfif')

# hsv_opencv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow(hsv_opencv)
# cv2.waitKey()

width = img.shape[1]
height = img.shape[0]
b, g, r    = img[:, :, 0], img[:, :, 1], img[:, :, 2]
for x in range(0, height):
	for y in range(0,width):
		hsv_imp = rgb2hsv(r, g, b)
print(hsv_imp)