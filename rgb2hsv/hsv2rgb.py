import numpy as np
# hsv_opencv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow(hsv_opencv)
# cv2.waitKey()

def hsv2rgb(h, s, v):
	c = np.multiply(v,s)
	x = np.multiply (c, (1 - abs(h / 60) mod 2 - 1))

	if h > 0 and h < 60:
		r_, g_, b_ = c, x, 0 
	if h > 60 and h < 120:
		r_, g_, b_ = x, c, 0
	if h > 120 and h < 180:
		r_, g_, b_ = 0, c, x
	if h > 180 and h < 240:
		r_, g_, b_ = 0, x, c
	if h > 240 and h < 300:
		r_, g_, b_ = x, 0, c
	if h > 300 and h < 360:
		r_, g_, b_ = c, 0, x

	m = np.subtract(v, c)
	r, g, b = r_ + m, g_ + m, b_ + m
		return r, g, b