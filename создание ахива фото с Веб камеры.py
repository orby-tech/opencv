import cv2
import numpy as np
import time
import sys, select, os

import time
import threading


i=1
cam = cv2.VideoCapture(0)
while (cam.isOpened()):
    s, im = cam.read() # captures image
    cv2.imshow("Test Picture", im) # displays captured image
    key = cv2.waitKey(10)
    if key==ord('1'):
        print("dd")
        break
    if key==ord('2'):
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        
        print(cv2.imwrite('C:\opencv'+str(i)+'.png', im))
        i+=1
