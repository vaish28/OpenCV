# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:40:26 2021

@author: Vaishnavi
"""

import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#img = cv.imread('cat.jpg') #specify full path
#cv.imshow('Cat',img)

#1. paint  a box to a certain color

blank[20:30,30:400] = 0,255,0
cv.imshow('Green',blank)

cv.waitKey(0)
