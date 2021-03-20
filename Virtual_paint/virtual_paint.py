import cv2 
import numpy as np
## HSV range         green,blue
mycolor = [[62,123,63,85,255,235],[95,176,75,179,255,255]]
## BGR color        green,blue
mycolorvalues = [(2,222,132),(255,166,77)]


def Main_process():
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # bgr to hsv
    count=0
    for color in mycolor:
        # for each color getting mask
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(hsv,lower,upper)
        # here x and y are center point of tip of marker
        x,y=getcontours(mask)
        if x!= 0 and y!=0:
            # this is used to see the center of marker
            # cv2.circle(mask,(x,y),3,mycolorvalues[count],2)
            ## appending center of marker
            plot_points.append([x,y])
            ## appending color used to mark the center
            plot_points_color.append(mycolorvalues[count])
        count=count+1

def getcontours(img):
    contours,_=cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    x,y,w=0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>700:
            x,y,w,h = cv2.boundingRect(cnt)
    return x+w//2,y


cap = cv2.VideoCapture(0)
plot_points = []
plot_points_color = []


## mainloop
while True:
    _,img = cap.read()
    img = cv2.flip(img,1) # flip horizontally

    Main_process()

    if len(plot_points)>0:
        for point in enumerate(plot_points):
                # here point form is (200,[449,263])
                # where 200 is the iteration and and [449,263]
                # is the point in plot_points
            cv2.circle(img,(point[1][0],point[1][1]),8,plot_points_color[point[0]],cv2.FILLED)


    cv2.imshow('original',img)
    k=cv2.waitKey(1)
    if k == ord('q'):
        break
cv2.destroyAllWindows()