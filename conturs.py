import sys
import numpy as np
import cv2

# параметры цветового фильтра
hsv_min = np.array((0,0,0), np.uint8)
hsv_max = np.array((200, 255, 255), np.uint8)


cam = cv2.VideoCapture(0)
while True:
    s, img = cam.read()
    gray =  cv2.cvtColor( img,  cv2.COLOR_BGR2GRAY)

    if __name__ == '__main__':
        print(__doc__)

        
        hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV 
        thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
        # ищем контуры и складируем их в переменную contours
        contours, hierarchy = cv2.findContours( thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # отображаем контуры поверх изображения
        cv2.drawContours( gray, contours, -1, (255,255,255), 1, cv2.LINE_AA, hierarchy, 1 )
        cv2.imshow('contours', gray) # выводим итоговое изображение в окно

        key = cv2.waitKey(10)
        if key==ord('1'):
            print("dd")
            break
    
cv2.destroyAllWindows()