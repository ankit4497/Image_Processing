import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype= 'uint8')

#color range of pixel from 200 to 300 and 300 to 400 pixel
blank[200:300 , 300:400] = 0,0,255

#drawing Rectangle
cv.rectangle(blank, (0,0) , (50,50) , (0,0,255) ,thickness = 2)

#fill rectangle with green color
cv.rectangle(blank, (50,100) , (0,50) , (0,255,0) ,thickness = cv.FILLED)

#filled circle 
cv.circle(blank, (250,250), 100 , (225,225,0) , thickness= 1)

#draw line
cv.line(blank, (100, 100) , (200 , 200) , (255,255,0) , thickness= 1)

#draw text
cv.putText(blank , 'text' , (250,250) ,cv.FONT_HERSHEY_SIMPLEX , 2.0, (255,0,0) , 5)


cv.imshow('Rectangle', blank) 
cv.waitKey(0)