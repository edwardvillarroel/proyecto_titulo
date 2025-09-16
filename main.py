import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

while True:
    ret,frame=cap.read()

    if ret==False:
        continue

    cv.imshow("video frame", frame)

    key_pressed = cv.waitKey(1) & 0xFF

    if key_pressed == ord('q'):
        break

cap.release()
cv.destroyAllWindows()