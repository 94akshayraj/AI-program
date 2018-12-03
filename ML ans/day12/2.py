import numpy as np
import cv2 as cv

ml = cv.imread('/home/ai3/Desktop/common/ML/Day10/ml.png')
opencv = cv.imread('/home/ai3/Desktop/common/ML/Day10/opencv-logo.png')

img = cv.addWeighted(opencv,0.7,ml,0.3,0)

cv.imshow("dt",img)
cv.waitKey(0)


