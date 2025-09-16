import cv2 as cv
import numpy as np
import sys

img = cv.imread('image.jpg')

if img is None:
    sys.exit("Could not read the image.")
 
cv.imshow("Display window", img)
k = cv.waitKey(0)
 


