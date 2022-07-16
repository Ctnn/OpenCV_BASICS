
#Import Picture
import cv2

img= cv2.imread("Resource/Screenshot_2.png")

cv2.imshow("Output",img)
cv2.waitKey(0)


#Import Video

#cap= cv2.VideoCapture(".....")

# while True:
#   success,img=cap.read() #Succes is boolean parameters
#   cv2.imshow("Video",img)
#   if cv2.waitKey(1) & 0xFF ==ord('q):
#      break