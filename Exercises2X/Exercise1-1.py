import cv2
import sys
import numpy as np

def erosion (size, img1):
    imgOut= img1.copy()
    for row in range(img1.shape[0]):
        for colum in range (img1.shape[1]):
            elems= img1[0 if row-size < 0 else row-size:row+size if row+size > img1.shape[0] else row+size+1,\
                0 if colum-size < 0 else colum-size:colum+size if colum+size > img1.shape[1] else colum+size+1]
            imgOut[row,colum]= np.min(elems)
    return imgOut

def subtraction(img1, img2):
    imgOut= img1.copy()
    for row in range(img1.shape[0]):
        for colum in range (img1.shape[1]):
            imgOut[row, colum] = img1[row, colum] - img2[row, colum]
    return imgOut
    
if len(sys.argv) != 3:
    print("The call to the function is incorrect, 2 elements need to be introduced ")
    exit()

img1 = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)


# Do de erosion of the imagen
imgOutErosion = erosion(1, img1)

#subtract the images
imgOut = subtraction (img1, imgOutErosion)

cv2.imwrite(sys.argv[2], imgOut)

