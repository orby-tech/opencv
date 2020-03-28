import cv2
import numpy as np
import time
import sys, select, os

import time
import threading



cam = cv2.VideoCapture(0)
while True:
    s, im = cam.read() # captures image
    cv2.imshow("Test Picture", im) # displays captured image
    key = cv2.waitKey(10)
    if key==ord('1'):
        print("dd")
        break
    

