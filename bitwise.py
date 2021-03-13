import numpy as np
import cv2 as cv

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370) , 255 , -1)
circle = cv.circle(blank, (200,200), 180, 255, -1)

#draw rectangle and circle
cv.imshow('rectangle', rectangle)
cv.imshow('circle',circle)

#bitwise and
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise And', bitwise_and)

#bitwise or
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise Or',bitwise_or)

#bitwise not
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise Not',bitwise_not)

cv.waitKey(0)