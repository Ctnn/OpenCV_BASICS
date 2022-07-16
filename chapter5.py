#warp perspective === crop that image body size

import cv2
import numpy as np

img=cv2.imread("Resources/Screenshot_2.png")

witdth,height=250,350
pts1=np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2=np.float32([[0,0],[witdth,0],[0,height],[witdth,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput =cv2.warpPerspective(img,matrix,(witdth,height))
cv2.imshow("Image Warped",imgOutput)
cv2.imshow("Image0",img)