

import cv2
import numpy as np
import matplotlib.pyplot as plt

# import required module
from PIL import Image
img = cv2.imread("../image/test.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 20, 0.1, 1)

corners = np.int0(corners)
data = np.array(corners)


print(data)


# for i in range(data.shape[0]):
for i in data:
	x, y = i.ravel()
	# x = data[i,0,0]
	# print("x :%s %s",i,x)
	# y = data[i,0,1]
	# print("y :%s %s", i, y)
	# color = list(np.random.choice(range(256), size=3))
	# print("color :%s %s",i,color)
	cv2.circle(img, (x,y), 5, (0, 0, 255), -1)
# mean = np.empty((0))
# mean, eigenvectors, eigenvalues = cv2.PCACompute2(data, mean)
# cntr = (int(mean[0, 0]), int(mean[0, 1]))
# cv2.circle(img, cntr, 5, (0, 0, 255), -1)

# plt.scatter(data[:, 0], data[:, 1],"x", "red", s=200)
# cv2.circle(img, (x,y), 5, (0, 0, 255), -1)
# cv2.circle(img, (x,y), 1, (0, 0, 255), -1)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# import cv2
# import numpy as np
#
# img = cv2.imread('../image/test1.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray,5,3,0.04)
# ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
# dst = np.uint8(dst)
# ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
# corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
# for i in range(1, len(corners)):
#     print(corners[i])
# img[dst>0.1*dst.max()]=[0,0,255]
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows

# import numpy as np1
# import cv2
# img_1 = cv2.imread('../image/test1.png')
# print ("The Gray scale image is /n")
# imgray_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(imgray_1, 127, 255, 0)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# print("The Total Number of Contours in the Image = ")
# #command len used to calculate the number of contours in the image
# print (str(len(contours)))
# print(contours[0])
# cv2.drawContours(img_1, contours, -1,(0,255,0),1)
# cv2.drawContours(imgray_1, contours, -1,(0,255,0),1)
# print ("The original image is: /n")
# cv2.imshow('Image', img_1)
# cv2.imshow('Image GRAY', imgray_1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
