##Object detection and tracking by COLOR

import cv2
import numpy as np

def nothing(x):
    pass


cap = cv2.VideoCapture(0)


while True:

    #frame = cv2.imread('smarties2.png')
    _, frame = cap.read()

    #convert a image to HSV

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    

    l_b= np.array([55, 67, 90])
    u_b = np.array([114, 255, 255])

    mask = cv2.inRange (hsv,l_b,u_b)
    res = cv2.bitwise_and(frame, frame,mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()