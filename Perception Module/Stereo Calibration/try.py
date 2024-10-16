import cv2
import numpy as np

img_left = cv2.imread('left_image.png', 0)
img_right = cv2.imread('right_image.png', 0)

stereo = cv2.createStereoBM(numDisparities=16, blockSize=15)
disparity = stereo.compute(img_left, img_right)

cv2.imshow('Disparity Map', disparity)
cv2.waitKey()
cv2.destroyAllWindows()