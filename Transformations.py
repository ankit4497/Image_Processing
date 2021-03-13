import cv2 as cv
import numpy as np

img = cv.imread('Photos\monarch.png')
cv.imshow('original image' , img)

def translation(img , x , y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img , transmat , dimensions)

translated = translation(img , 100 , 100)
cv.imshow('translated image' , translated)

#rotation
def rotate(img , angle , rotpoint = None):
    (width, height) = img.shape[0:2]

    if rotpoint == None:
        rotpoint = (width//2 , height//2)
    
    rotmat = cv.getRotationMatrix2D(rotpoint , angle , scale= 1.0)
    dimention = (width , height)

    return cv.warpAffine(img , rotmat , dimention)

rotated = rotate(img, -45)
cv.imshow('rotated' , rotated)

#flip image
flipped = cv.flip(img, -1)
cv.imshow('flipped' , flipped)



cv.waitKey(0)