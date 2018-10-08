import numpy as np
import cv2

class Color_Detection(object):
    def __init__(self,lowerh,lowers,lowerv,upperh,uppers,upperv):
        self.lower=np.array([lowerh,lowers,lowerv])
        self.upper=np.array([upperh,uppers,upperv])
        self.range=cv2.inRange(hsv,self.lower,self.upper)
        #morph
        kernal=np.ones((5,5),'uint8')
        self.range=cv2.dilate(self.range,kernal)
        res=cv2.bitwise_and(frame,frame,mask=self.range)
        #tracking
        (_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic,contour in enumerate(contours):
            area=cv2.contourArea(contour)
            if(area>2000):
                x,y,w,h=cv2.boundingRect(contour)
                frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
                frame=cv2.rectangle(frame,(int(x+w/2),int(y+h/2)),(int(x+w/2),int(y+h/2)),(255,255,255),2)

                Red=[int(x+w/2),int(y+h/2)]
                print("Red=",Red)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, "Red", (int(x+w/2)+5,int(y+h/2)), font, 1, (255,255,255), 2, cv2.LINE_AA)

