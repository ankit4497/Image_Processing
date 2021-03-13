import cv2 as cv
import numpy as np

img = cv.imread(r'Photos\noisy.png')
cv.imshow('Original', img)

#blur
#simple blur
blur = cv.blur(img, (7,7))
cv.imshow('averaging', blur)

#gaussian blur
#retain quality while blurring
gaussian_blur = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('gaussian blur', gaussian_blur)

#median
median = cv.medianBlur(img, 7)
cv.imshow('median', median)

#bilateral 
#retain edges while blurring
bilateral = cv.bilateralFilter(img, 15, 35, 15)
cv.imshow('bilateral', bilateral)
cv.waitKey(0)

#NOTE median is useful in reducing salt pepper noise and edge retention 