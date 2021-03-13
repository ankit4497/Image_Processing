import cv2 as cv
import numpy as np

img = cv.imread('Photos\monarch.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#canny edge

canny = cv.Canny(gray, 150, 175)
cv.imshow('canny edges', canny)

#Laplacian edge

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian' , lap)

#sobel edge
sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel = cv.bitwise_or(sobelX, sobelY)
cv.imshow('Sobel edge', sobel)

cv.waitKey(0)