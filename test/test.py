# import numpy
# import cv2 as cv2
# #contour = numpy.array([[[0,0]], [[10,0]], [[10,10]], [[5,4]]]) matrix 2x4
# contour = numpy.array([[[0,0]], [[10,0]], [[0,0]], [[10,10]]])
# #tinh goc cua 2 duong thang
# area = cv2.contourArea(contour)
# print("area",area)
import numpy as np

new_array = np.array([[14, 26],
      [6, 8]])
new_array2 = np.array([[15, 23],
      [73, 118]])
result= np.matmul(new_array,new_array2)
print('Multiplication of two matrices:',result)