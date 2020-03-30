#delect blue objects in images

import cv2
import numpy as np

def nothing(x):
    pass

while True:
    frame = cv2.imread('smarties.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_b = np.array([102,165,183])
    u_b = np.array([139,255,255])


    mask = cv2.inRange (hsv,l_b,u_b)
    res = cv2.bitwise_and(frame, frame,mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()