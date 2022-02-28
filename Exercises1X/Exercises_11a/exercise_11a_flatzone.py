# import cv2 as cv
import queue
import cv2
import sys
import numpy as np

if len(sys.argv) != 4:
    print("The call to the function is incorrect, 3 elements need to be introduced ")
    exit()

#parameters inside the txt 
file = open(sys.argv[1], 'r')
lines = file.readlines()

columPixel = int(lines[0].split("\n")[0])
rowPixel = int(lines[1].split("\n")[0])
connectivity = int(lines[2].split("\n")[0])
label = int(lines[3].split("\n")[0])

# Output image is created and initialized 
img1 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)
imgOut= np.zeros((img1.shape[0],img1.shape[1]), np.uint8)

# The value of pixel x is output image is labeled as flat zone
imgOut[rowPixel,columPixel]= label

#Creation of the flatzone waiting queue 
flatzone =[]

#Initialization of flatozne with pixel x
flatzone.append((rowPixel,columPixel))

#while the flatzone is not empty
while len(flatzone)!=0:
    p = flatzone.pop()
    #for all neighbors p'
    for row in range(0 if p[0] == 0 else p[0]-1, p[0] if p[0] == img1.shape[0]-1 else p[0]+2):
        for colum in range(0 if p[1] == 0 else p[1]-1, p[1] if p[1] == img1.shape[1]-1 else p[1]+2):
            if row==rowPixel and colum == columPixel: #the elem
                continue
            # the the pixel p' belongs to x's flat zone and has not been treated
            # the pixel p' is labeld as flat zone and inserted into the queue
            if ((img1[row,colum] == img1[rowPixel,columPixel]) and (imgOut [row,colum] != label )):
                imgOut [row,colum] = label
                flatzone.append((row,colum))
        

cv2.imwrite(sys.argv[3], imgOut)