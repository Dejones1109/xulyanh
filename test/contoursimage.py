import numpy as np
import cv2 as cv


img = cv.imread('../image/img1.png',0)
ret,thresh = cv.threshold(img,127,255,0)
cnt = cv.contours[0]
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img,[box],0,(0,0,255),2)



