import cv2 as cv
import numpy as np

img = cv.imread('Photos\monarch.png')
cv.imshow('Original image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image', gray)

threshold, thresh = cv.threshold(gray , 150, 255, cv.THRESH_BINARY)
cv.imshow('threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255 , cv.THRESH_BINARY_INV)
cv.imshow('Threshold Inversion', thresh_inv)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 0)

cv.waitKey(0)
