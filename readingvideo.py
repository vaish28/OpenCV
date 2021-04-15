# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:06:16 2021

@author: Vaishnavi 
"""

import cv2 as cv

capture = cv.VideoCapture('dog.mp4') #specify full path

def rescaleFrame(frame,scale = 0.75):
    width = int((frame.shape[1]*scale))
    height = int((frame.shape[0]*scale))
    
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

while True:
    isTrue , frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video',frame)
    cv.imshow('Video1',frame_resized)
    
    if cv.waitKey(100) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()
    


