import cv2
import sys

image = cv2.imread("Enter image file location")

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayImageInv = 255 - grayImage
grayImageInv = cv2.GaussianBlur(grayImageInv, (21,21), 0)
output = cv2.divide(grayImage, 255-grayImageInv, scale=256.0)
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("pencilsketch", cv2.WINDOW_AUTOSIZE)
cv2.imshow("image", image)
cv2.imshow("pencilsketch", output)
cv2.waitKey(0)  
cv2.destroyAllWindows() 
