import  numpy as np
import cv2
img_second = cv2.imread("../image/test.png")
kernel = np.ones((5,5),np.uint8)
erosion_1 = cv2.erode(img_second,kernel,iterations = 500)
cv2.imshow("img",img_second)
cv2.waitKey(0)
cv2.destroyAllWindows()