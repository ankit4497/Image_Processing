import cv2 as cv
import numpy as np

img = cv.imread('Photos\monarch.png')

cv.imshow('original' , img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#blur the image 
blur = cv.GaussianBlur(gray, (5,5) , cv.ADAPTIVE_THRESH_GAUSSIAN_C, borderType= cv.BORDER_DEFAULT)

#Binarization of image
ret ,threshold = cv.threshold(blur, 125, 255 , cv.THRESH_BINARY)
cv.imshow('threshold' , threshold)

#canny edge
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny edges', canny)
#drawing contour on blank image
blank = np.zeros(img.shape, 'uint8')
blank1 = np.zeros(img.shape, 'uint8')
#getting contour with threshold
contours , hierarchy = cv.findContours(threshold , cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank , contours , -1 , (0,0,255) , 1)
#getting contour with canny
contours1 , hierarchy1 = cv.findContours(canny , cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank1 , contours1 , -1 , (0,0,255) , 1)

cv.imshow('contours with threshold', blank)
cv.imshow('contours with canny', blank1)
cv.waitKey(0)