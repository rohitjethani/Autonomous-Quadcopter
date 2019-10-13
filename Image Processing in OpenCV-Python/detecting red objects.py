import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #hsv=hue-saturation-value
    lower_red = np.array([150,150,10])
    upper_red = np.array([180,180,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF==ord('q'):
            break;

cv2.destroAllWindows()
cap.release()