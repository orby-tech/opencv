import cv2

import numpy as np


# Create a black image
img = np.zeros((512,512,3), np.uint8)


# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img, (0,0), (511,511), (255, 0, 0), 5)

# Draw a rectangle green line with thickness of 3 px
img= cv2.rectangle(img, ( 384 , 0 ),( 510 , 128 ),( 0 , 255 , 0 ), 3)

# Draw a circele red line with thickness of 1 px inside
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

#Draw an ellipse with center: 256 256 axis lenght 100 50 rotation ellipse 0 rotation of ellipse from to 0 180 and cthickness 1 px inside 
img = cv2.ellipse( img ,( 256 , 256 ),( 100 , 50 ), 0 , 0 , 180 , 255 , - 1)

cv2.imshow("image", img )
cv2.waitKeyEx()

# we can drawing poligon
#            and write text
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html