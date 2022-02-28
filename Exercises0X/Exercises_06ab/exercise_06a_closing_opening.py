# import cv2 as cv
import cv2
import sys
import numpy as np

def ero (image, size):
    imgOut= image.copy()
    for row in range(image.shape[0]):
        for colum in range (image.shape[1]):
            elems= image[0 if row-size < 0 else row-size:row+size if row+size > image.shape[0] else row+size+1,\
                0 if colum-size < 0 else colum-size:colum+size if colum+size > image.shape[1] else colum+size+1]
            imgOut[row,colum]= np.min(elems)
    return imgOut

def dil (image, size):
    imgOut= image.copy()
    for row in range(image.shape[0]):
        for colum in range (image.shape[1]):
            elems= image[0 if row-size < 0 else row-size:row+size if row+size > image.shape[0] else row+size+1,\
                0 if colum-size < 0 else colum-size:colum+size if colum+size > image.shape[1] else colum+size+1]
            imgOut[row,colum]= np.max(elems)
    return imgOut


def com (image):
    imgOut= image.copy()
    for row in range(image.shape[0]):
        for colum in range (image.shape[1]):
            imgOut[row,colum]= 255-image[row,colum]
    return imgOut

def closing (image,size):
    complement1 = com (image)
    erosion = ero (complement1, size)
    dilation= dil(erosion, size)
    complement2= com (dilation)
    return complement2

def opening (image, size):
    erosion = ero (image, size)
    dilation= dil(erosion, size)
    return dilation

size = int(sys.argv[1])
img1 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)

op = opening(img1, size)
clos = closing (op, size)

cv2.imwrite(sys.argv[3], clos)
