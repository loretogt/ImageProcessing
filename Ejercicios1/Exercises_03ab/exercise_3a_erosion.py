# import cv2 as cv
import cv2
import sys
import numpy as np

if len(sys.argv) != 4:
    print("The call to the function is incorrect, 3 elements need to be introduced ")
    exit()

size = int(sys.argv[1])
img1 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)
imgOut= img1.copy()

# we go through the image
for row in range(img1.shape[0]):
    for colum in range (img1.shape[1]):
        elems= img1[0 if row-size < 0 else row-size:row+size if row+size > img1.shape[0] else row+size+1,\
             0 if colum-size < 0 else colum-size:colum+size if colum+size > img1.shape[1] else colum+size+1]
        imgOut[row,colum]= np.min(elems)

cv2.imwrite(sys.argv[3], imgOut)
