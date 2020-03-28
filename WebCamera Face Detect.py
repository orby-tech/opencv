import numpy as np
import cv2

face_cascade =  cv2.CascadeClassifier(r'C:\Users\1\Desktop\программы\openCV practise\haarcascade_frontalface_default.xml') 
eye_cascade =  cv2.CascadeClassifier('haarcascade_eye.xml') 
cam = cv2.VideoCapture(0)
while True:
    s, img = cam.read()
    gray =  cv2.cvtColor( img,  cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h//2, x:x+w]
        roi_color = img[y:y+h//2, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        i=0
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            i+=1
            if i>1:
                break

    cv2.imshow('img',img)
    key = cv2.waitKey(10)
    if key==ord('1'):
        print("dd")
        break
cv2.destroyAllWindows()