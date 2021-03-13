import cv2 as cv
import numpy as np

img = cv.imread('Photos\monarch.png')
cv.imshow('original image' , img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
#cv.imshow('gray', gray)

#blur image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('blur image' , blur)

#Edge Cascade
canny = cv.Canny(blur, 125, 200)
#cv.imshow('canny Edges' , canny) 

#dilate image
dilated = cv.dilate(canny, (7,7) , iterations = 3)
#cv.imshow('dilated' , dilated)

#erod image
eroded = cv.erode(dilated , (7,7) , iterations= 3)
#cv.imshow('eroded' , eroded)

#resize image
#resized image is smaller than original 
resized_Area = cv.resize(img , (200,200), interpolation= cv.INTER_AREA)
#cv.imshow('resized Area', resized_Area)

#Resize image is bigger than original . it is slow but retain quality
resized_Cubic = cv.resize(img , (1000,1000), interpolation= cv.INTER_CUBIC)
#cv.imshow('resized Cubic', resized_Cubic)

#if resized is bigger than original
resized_Linear = cv.resize(img , (1000,1000), interpolation= cv.INTER_LINEAR)
#cv.imshow('resize linear' , resized_Linear)

#crop image
cropped = img[100:300 , 200:400]
cv.imshow('cropped' , cropped)



cv.waitKey(0)
