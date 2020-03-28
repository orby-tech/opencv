import numpy as np
import cv2

cascade =  cv2.CascadeClassifier('/home/tim/All_to_programming/opencv/build/x64/vc14/bin/haarcascade/cascade.xml') 
cam = cv2.VideoCapture(0)
while True:
    s, img = cam.read()
    gray =  cv2.cvtColor( img,  cv2.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(gray, 3, 14)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        

    cv2.imshow('img',img)
    key = cv2.waitKey(10)
    if key==ord('1'):
        print("dd")
        break
cv2.destroyAllWindows()
