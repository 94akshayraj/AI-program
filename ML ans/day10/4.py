import numpy as np
import cv2 as cv
apple = cv.imread('/home/ai3/Desktop/common/ML/Day10/Questions/apple.jpg')
orange = cv.imread('/home/ai3/Desktop/common/ML/Day10/Questions/orange.jpg')
arow,acol,_ = apple.shape
orow,ocol,_ = orange.shape

print apple.shape
print orange.shape


org=orange[:256,:]
apple[:256,:] = org


cv.imshow('result',apple)
cv.waitKey(0)
cv.destroyAllWindows()
