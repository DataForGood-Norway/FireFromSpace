# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:27:24 2019

@author: ankhek

a toy example to detect fire by localizing colours

python 3.6.5
opencv 3.4.1
"""

import cv2

import os


import numpy as np

wDir = r"your image directory"

img= cv2.imread(os.path.join(wDir,'Sentinel-2 image on 2018-11-18.jpg'))
cv2.imshow('Original',img)
cv2.waitKey(1)

"""convert to HSV space"""
cimg = cv2.cvtColor(img, cv2.COLOR_RGB2HSV) 
cv2.imshow('HSV',cimg)
cv2.waitKey(1)

lower_bound = np.array([110,50,50]) 
upper_bound = np.array([150,255,255]) 

mask = cv2.inRange(cimg, lower_bound, upper_bound) 
res = cv2.bitwise_and(img,img, mask= mask) 

cv2.imshow('Thresholded',res)
cv2.waitKey(1)