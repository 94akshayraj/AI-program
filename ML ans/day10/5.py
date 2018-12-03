import numpy as np
import cv2 as cv
apple = cv.imread('/home/ai3/Desktop/common/ML/Day10/Questions/apple.jpg',0)
applec = cv.imread('/home/ai3/Desktop/common/ML/Day10/Questions/apple.jpg')
#orange = cv.imread('/home/ai3/Desktop/common/ML/Day10/Questions/orange.jpg')
arow,acol = apple.shape
row,col,_ = applec.shape

print apple.shape
#print orange.shape

neg = apple[:,:]-255
applec = neg

cv.imshow('result',applec)
cv.waitKey(0)
cv.destroyAllWindows()
