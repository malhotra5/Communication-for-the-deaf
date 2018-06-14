import cv2
import numpy as np
import os


a = ["E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "nothing", "O", "P", "Q", "R", "S", "space", "T", "U", "V", "W", "X", "Y","Z"]
for x in range(len(a)): 
    os.chdir(a[x])
    for i in range(3000):
        img = cv2.imread(a[x] + str(i+1) + ".jpg")
        gray = gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(a[x] + str(i+1) + ".jpg", gray )
    os.chdir("..")
    
