import cv2 as cv

def resizing(frame , scale = 0.75):

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width ,  height)

    return cv.resize(frame , dimension, interpolation=cv.INTER_AREA)

img = cv.imread('Photos\monarch.png')

cv.imshow('butterfly',img)
img = resizing(img, scale= 0.5)
cv.imshow('resized butterfly',img)

cv.waitKey(0)