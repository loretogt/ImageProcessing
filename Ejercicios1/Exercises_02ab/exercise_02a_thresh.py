# import cv2 as cv
import cv2
import sys

img1 = cv2.imread("cam_74.pgm", cv2.IMREAD_GRAYSCALE)

# Copy of image
img2 = img1.copy()

nrows = img1.shape[0]
ncols = img1.shape[1]

for row in range(img1.shape[0]):
    for colum in range (img1.shape[1]):
        if img2[row,colum] >