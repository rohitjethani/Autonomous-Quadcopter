import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #hsv=hue-saturation-value
    lower_red0 = np.array([0,50,0])
    upper_red0 = np.array([10,255,255])
    
    lower_red1 = np.array([170,50,0])
    upper_red1 = np.array([180,255,255])

    lower_green = np.array([50,100,0])
    upper_green = np.array([180,255,255])

    lower_blue = np.array([100,150,0])
    upper_blue = np.array([140,255,255])

    red_mask0 = cv2.inRange(hsv, lower_red0, upper_red0)
    red_mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    red_mask = red_mask0 + red_mask1
    red = cv2.bitwise_and(frame, frame, mask = red_mask)

    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    green = cv2.bitwise_and(frame, frame, mask = green_mask)

    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    blue = cv2.bitwise_and(frame, frame, mask = blue_mask)

    cv2.imshow('frame', frame)

    cv2.imshow('red_mask', red_mask)
    cv2.imshow('red', red)

    #cv2.imshow('blue_mask', blue_mask)
    #cv2.imshow('blue', blue)

    #cv2.imshow('green_mask', green_mask)
    #cv2.imshow('green', green)

    if cv2.waitKey(1) & 0xFF==ord('q'):
         break;

cv2.destroyAllWindows()
cap.release()
