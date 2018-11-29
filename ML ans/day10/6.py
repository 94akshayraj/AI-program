import numpy as np
import cv2 as cv
apple = cv.imread('/home/ai3/Desktop/common/ML/Day10/Questions/apple.jpg',0)
#orange = cv.imread('/home/ai3/Desktop/common/ML/Day10/Questions/orange.jpg')
arow,acol = apple.shape
#orow,ocol,_ = orange.shape

print apple.shape
#print orange.shape

neg = cv.bitwise_not(apple)
image = np.hstack([neg,apple])


cv.imshow('result',image)
cv.waitKey(0)
cv.destroyAllWindows()
