import cv2 as cv
import numpy as np

img=cv.imread('/home/ai3/Desktop/common/ML/Day13/building.png',0)

sobelx=cv.Sobel(img,cv.CV_64F,1,0,ksize=1)
sobely=cv.Sobel(img,cv.CV_64F,0,1,ksize=1)

img=cv.addWeighted(sobelx,0.5,sobely,0.5,0)
#img=np.hstack((sobelx,sobely))
#lower = cv.pyrDown(img)
cv.imshow('dst',img)
cv.waitKey(0)

