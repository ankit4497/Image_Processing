import cv2 as cv
import numpy as np

img = cv.imread('Photos\noisy.png')
cv.imshow('Original', img)

#blur
blur = cv.blur(img, (5,5))
cv.imshow('averaging', blur)

#gaussian blur
gaussian_blur = cv.GaussianBlur(img, (5,5), 0)
cv.imshow('gaussian blur', gaussian_blur)

#bilateral 
bilateral = cv.bilateralFilter(img, 5, 5, 15)
cv.imshow('bilateral', bilateral)
cv.waitKey(0)