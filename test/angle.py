import cv2
import numpy as np
import math

img = cv2.imread('../image/test1.png', cv2.IMREAD_UNCHANGED)
kernel = np.ones((3,3),np.uint8)
erosion_1 = cv2.erode(img,kernel,iterations = 20)
cv2.imshow("1",erosion_1)
# convert img to grey
img_grey = cv2.cvtColor(erosion_1, cv2.COLOR_BGR2GRAY)
# set a thresh
thresh = 1
# get threshold image
ret, thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
# find contours
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# create an empty image for contours
img_contours = np.zeros(erosion_1.shape)
# draw the contours on the empty image
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 3)
# corners = cv2.goodFeaturesToTrack(img_grey, 4, 0.1, 1)
# corners = np.int0(corners)
# data = np.array(corners)
# for i in data:
#     x, y = i.ravel()
#     cv2.circle(img_contours, (x, y), 5, (0, 0, 255), -1)


pointsList = []
def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        if (len(pointsList) <3 ):
            cv2.circle(img_contours, (x, y), 5, (0, 0, 255), cv2.FILLED)
            pointsList.append([x,y])
        else:
            angle =getAngle(pointsList)
            print(" The angle is ",angle,"degrees")
            return pointsList
def gradient(pt1,pt2):
    return (pt2[1] -pt1[1])/(pt2[0]-pt1[0])
def getAngle(points):
    pt1,pt2,pt3 = pointsList[-3:]
    m1 = gradient(pt2,pt1)
    m2 = gradient(pt2,pt3)
    angR = math.atan((m1-m2)/(1+m1*m2))
    angD = round(math.degrees(angR))
    return angD
    pass
while True:
    cv2.imshow("img", img_contours)
    cv2.setMouseCallback("img",mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pointsList = []
        img_contours



# save image
# cv2.imwrite('D:/contours.png',img_contours)
cv2.destroyAllWindows()