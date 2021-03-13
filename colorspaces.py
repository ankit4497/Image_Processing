import cv2 as cv
import numpy as np

img = cv.imread('Photos\monarch.png')
cv.imshow('original BGR' , img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB' , rgb)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#NOTE : You can convert back image to BGR or any other form but you can't convert gray to HSV and HSV to gray
cv.waitKey(0)
