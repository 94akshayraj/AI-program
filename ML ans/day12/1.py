import numpy as np
import pandas as pd
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('/home/ai3/Desktop/common/ML/Day12/walking.png',0)

ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

titles = ['OriginalImg','BINARY']
images = [img,thresh1]

imgx = np.hstack([thresh1])

cv.imshow("desd",imgx)
cv.waitKey(0)

cv.write("walking binary.jpg")	