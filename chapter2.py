
#BASICS FUNCTIONS

import cv2
import numpy as np

img = cv2.imread("Resource/Screenshot_2.png")
kernel=np.ones((5,5),np.uint8) #Create Matrix made by Integer
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imgGray)

imgBlur= cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur Image",imgBlur)

imgCanny= cv2.Canny(img,100,100)
cv2.imshow("Canny Image",imgCanny)

imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
cv2.imshow("Dialation  Image",imgDialation)

cv2.waitKey(0)
