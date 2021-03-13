import cv2 as cv
import numpy as np

img = cv.imread('Photos\monarch.png')

blank = np.zeros(img.shape[0:2], dtype= 'uint8')

mask = cv.rectangle(blank, (30,30), (170,170), 255, -1)

masked_img = cv.bitwise_and(img, img , mask = mask)

cv.imshow('masked image', masked_img)

cv.waitKey(0)
