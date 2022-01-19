import cv2
import numpy as np
import math

img = cv2.imread('../image/img1.png', cv2.IMREAD_UNCHANGED)
cv2.imshow("origin",img)
scale_percent = 30  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resizedOrigin = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#Median Blur
# filteredMedianImg = cv2.medianBlur(resizedOrigin, ksize=5)
# cv2.imshow('Median Blur image', filteredMedianImg)
#erosion image
kernel = np.ones((7,7),np.uint8)
erosion_1 = cv2.erode(resizedOrigin,kernel,iterations = 7)
cv2.imshow("erosion image",erosion_1)
# kernel1 = np.ones((5,5),np.uint8)
# dilate = cv2.dilate(erosion_1,kernel1,iterations = 5)
# cv2.imshow("dilate image",dilate)
# convert img to grey
img_grey = cv2.cvtColor(erosion_1, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_grey,120,220)
cv2.imshow("edges image",edges)
# set a thresh : xác định ngưỡng để lấy bao viên
thresh = 60
# get threshold image
ret, thresh_img = cv2.threshold(edges, thresh, 255, cv2.THRESH_BINARY)
# find contours
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# create an empty image for contours
img_contours = np.zeros(erosion_1.shape)
# draw the contours on the empty image
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 3)

cv2.imshow("contours imagle",img_contours)
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
    return (pt2[1] -pt1[1])/(pt2[0]-pt1[0]) #công thức tính tan của góc tạo bởi giữa đường thẳng và trục Ox
def getAngle(points):
    pt1,pt2,pt3 = pointsList[-3:]
    m1 = gradient(pt2,pt1)
    m2 = gradient(pt2,pt3)
    angR = math.atan((m1-m2)/(1+m1*m2)) # công thức tính tiếp tuyến giữa 2 đường thẳng
    angD = math.fabs(round(math.degrees(angR))) #trị tuyết đối và đổi ra độ
    return angD
    pass
while True:
    cv2.imshow("img final", img_contours)
    cv2.setMouseCallback("img final",mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pointsList = []
        img_contours



# save image
# cv2.imwrite('D:/contours.png',img_contours)
cv2.destroyAllWindows()