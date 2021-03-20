## AIR_CANVAS

import cv2 
import numpy as np

# colors
blue = (255,0,0)
green = (0,255,0)
red = (0,0,255)
white = (255,255,255)
black = (0,0,0)


def getcontours(img):
    contours,_=cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    x,y,w=0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>600:
            x,y,w,h = cv2.boundingRect(cnt)
    # returning middle point of contoured rect
    return x+w//2,y

def image_conversions_and_contours():
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # bgr to hsv
    lower = np.array([62,123,62])     ## green color
    upper = np.array([85,255,235])
    mask = cv2.inRange(hsv,lower,upper)
    # here x and y are center point of tip of marker
    x,y=getcontours(mask)


    if x!= 0 and y!=0: # checking if area is greater than 600
        # # # # # # cv2.circle(img,(x,y),10,white,-1)
        # indicate marker on white screen
        cv2.circle(paintwindow,(x,y),10,black,2)
        if stop>0: # if status is +ve then append
            plot_points.append([x,y])

def draw_boxes_and_status(image):
    cv2.rectangle(image,(30,20),(100,60),green,-1)
    cv2.rectangle(image,(120,20),(190,60),blue,-1)
    cv2.rectangle(image,(210,20),(280,60),red,-1)
    cv2.rectangle(image,(300,20),(370,60),black,-1)
    cv2.putText(image,"Green",(40,15),cv2.FONT_HERSHEY_SIMPLEX,0.5,black)
    cv2.putText(image,"Blue",(140,15),cv2.FONT_HERSHEY_SIMPLEX,0.5,black)
    cv2.putText(image,"Red",(220,15),cv2.FONT_HERSHEY_SIMPLEX,0.5,black)
    cv2.putText(image,"Clear all",(300,15),cv2.FONT_HERSHEY_SIMPLEX,0.5,black)
    if stop>0:
        status = "Write"
    else:
        status = "Stop"
    cv2.putText(image,f"Status:{status}",(500,15),cv2.FONT_HERSHEY_SIMPLEX,0.5,black)


cap = cv2.VideoCapture(0)
plot_points = []
paintwindow = np.zeros((700,1000,3))


def getcolor(color):
    y = 20<=point[1]<=60
    if (30<=point[0]<=100) and y:
        color = green
    elif (120<=point[0]<=190) and y:
        color = blue
    elif (210<=point[0]<=280) and y:
        color = red
    return color

## mainloop
stop=-1    #status Stop/-ve

while True:
    # reading & arranging img
    _,img = cap.read()
    img=cv2.resize(img,(1000,700))
    img = cv2.flip(img, 1 ) #flip horizontally

    # white paintwindow
    paintwindow[:] = 255

    draw_boxes_and_status(img)
    draw_boxes_and_status(paintwindow)


    image_conversions_and_contours()

    color=black    # default
    if len(plot_points)>0:
        for point in plot_points:
            color = getcolor(color)  # function get color
            # clear all functionality
            cv2.circle(img,(point[0],point[1]),8,color,cv2.FILLED)
            cv2.circle(paintwindow,(point[0],point[1]),8,color,cv2.FILLED)
            if (300<=point[0]<=370) and 20<=point[1]<=60:
                plot_points = []


    # # # # # cv2.imshow('img',img)
    cv2.imshow('PaintWindow',paintwindow)
    
    k2=cv2.waitKey(1)
    if k2 == ord('s'):
        stop = -1*stop
    if k2 == ord('q'):
        break
cv2.destroyAllWindows()