import cv2 as cv
import numpy as np

img = cv.imread('/home/ai3/Desktop/common/ML/Day13/man.jpg',0)
kernel = np.ones((2,2),np.uint8)

open1 = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
img = cv.imshow('dst',open1)
cv.waitKey(0)