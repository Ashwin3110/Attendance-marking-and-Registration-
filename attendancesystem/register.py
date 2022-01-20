# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:03:37 2022

@author: Ashwin D
"""

import cv2

cap = cv2.VideoCapture(0)
path = 'images'

while True:
    ret,frame = cap.read()
    cv2.imshow("Test", frame)
    
    k = cv2.waitKey(1)
    
    if k%256 == 27:
        print("Esc hit")
        break
    elif k%256 == 32:
        name = input("Enter Your Name")
        img_name = "{}.png".format(name)
        cv2.imwrite(f'{path}/{img_name}',frame)
        


cap.release()
cv2.destroyAllWindows()