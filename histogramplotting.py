import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Photos\monarch.png')
blank = np.zeros(img.shape[0:2],dtype='uint8')

mask = cv.rectangle(blank, (50,50), (700,500), 255, -1)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('masked', masked)

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bin')
plt.ylabel('no of pixels')
 
colors = ('b' , 'g' , 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([masked], [i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)