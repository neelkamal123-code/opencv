## INVISIBLE OBJECT

import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
_,init_frame = cap.read() # picture of background
while True:
    _,img = cap.read()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([0,116,156])     ## orange color
    upper = np.array([36,255,255])
    mask = cv2.inRange(hsv,lower,upper)

    ## inverse of mask 0-255,255-0
    maskinv = 255-mask 

    b,g,r = cv2.split(img)
    b = cv2.bitwise_and(maskinv,b)
    g = cv2.bitwise_and(maskinv,g)
    r = cv2.bitwise_and(maskinv,r)
    frame_inv = cv2.merge((b,g,r))   # black mark on green rest is image

    # initial frame 
    b,g,r = cv2.split(init_frame)

    b= cv2.bitwise_and(mask,b)
    g= cv2.bitwise_and(mask,g)
    r= cv2.bitwise_and(mask,r)
    blanket_area = cv2.merge((b,g,r))

    invisible_cloak = cv2.bitwise_or(frame_inv,blanket_area)

    # cv2.imshow('img',img)
    # cv2.imshow('Mask',mask)
    # cv2.imshow('maskiv',maskinv)
    # cv2.imshow('frameinv',frame_inv)
    # cv2.imshow('blanket',blanket_area)
    cv2.imshow('invisible_cloak',invisible_cloak)
    k = cv2.waitKey(1)
    if k==ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()