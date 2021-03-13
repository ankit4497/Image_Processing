import numpy as np
import cv2 as cv

img = cv.imread('Photos\monarch.png')

b,g,r = cv.split(img)

blank = np.zeros(img.shape[0:2], dtype='uint8')

red = cv.merge([blank, blank,  r])
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red' , red)

cv.waitKey(0)