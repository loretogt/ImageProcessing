# import cv2 as cv
import cv2
import sys

def maxElems (listElems):
    res = listElems[0][0]
    for pair in listElems:
        for elem in pair: 
            if elem > res :
                res = elem
    return res

def minElems (listElems):
    res = listElems[0][0]
    for pair in listElems:
        for elem in pair: 
            if elem < res :
                res = elem
    return res

def ero (image, size):
    imgOut= image.copy()
    for row in range(image.shape[0]):
        for colum in range (image.shape[1]):
            elems= image[0 if row-size < 0 else row-size:row+size if row+size > image.shape[0] else row+size+1,\
                0 if colum-size < 0 else colum-size:colum+size if colum+size > image.shape[1] else colum+size+1]
            imgOut[row,colum]= minElems(elems)
    return imgOut

def dil (image, size):
    imgOut= image.copy()
    for row in range(image.shape[0]):
        for colum in range (image.shape[1]):
            elems= image[0 if row-size < 0 else row-size:row+size if row+size > image.shape[0] else row+size+1,\
                0 if colum-size < 0 else colum-size:colum+size if colum+size > image.shape[1] else colum+size+1]
            imgOut[row,colum]= maxElems(elems)
    return imgOut

if len(sys.argv) != 4:
    print("The call to the function is incorrect, 3 elements need to be introduced ")
    exit()

size = int(sys.argv[1])
img1 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)


erosion = ero (img1, size)
dilation= dil(erosion, size)


cv2.imwrite(sys.argv[3], dilation)
