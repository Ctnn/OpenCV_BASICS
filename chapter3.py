#Resize a image

import cv2
import numpy as np

img=cv2.imread("Resource/Screenshot_2.png")
print(img.shape) #(width,height,vgr)

imgResize=cv2.resize(img,(300,200))
print(imgResize.shape) #(width,height,vgr)

imgCropped = img[0:200,200:500] #Your want to selected area size

cv2.imshow("Image",img)
cv2.imshow("ResizedImage",imgResize)
cv2.imshow("Image Cropped ",imgCropped)
cv2.waitKey(0)