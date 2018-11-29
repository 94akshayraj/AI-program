import numpy as np
import cv2 as cv
img = cv.imread('/home/ai3/Desktop/common/ML/Day10/Questions/apple.jpg')
#rows,cols = img.shape
#M = np.float32([[1,0,200],[0,1,100]])
dst = cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()
