import cv2 as cv
import numpy as np

img = cv.imread('/home/ai3/Desktop/common/ML/Day13/girl.jpg',0)
kernel = np.ones((2,2),np.uint8)


open1 = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
open2 = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
open3 = cv.morphologyEx(open1,cv.MORPH_CLOSE,kernel)
img=np.hstack((open1,open2,open3))
img = cv.imshow('dst',img)
cv.waitKey(0)