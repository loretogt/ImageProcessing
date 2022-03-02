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

# Output image is created and initialized 
img1 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)
imgOut= np.zeros((img1.shape[0],img1.shape[1]), np.uint32)

#--- We create the flatzone ----
# The value of pixel x is output image is labeled as flat zone
imgOut[rowPixel,columPixel]= 1

#Creation of the flatzone waiting queue 
flatzone =[]

#Initialization of flatozne with pixel x
flatzone.append((rowPixel,columPixel))

#while the flatzone is not empty
while len(flatzone)!=0:
    p = flatzone.pop()
    #for all neighbors p'
    for row in range(0 if p[0] == 0 else p[0]-1, p[0]+1 if p[0] == img1.shape[0]-1 else p[0]+2):
        for colum in range(0 if p[1] == 0 else p[1]-1, p[1]+1 if p[1] == img1.shape[1]-1 else p[1]+2):
            if row==rowPixel and colum == columPixel: #the elem
                continue
            # the the pixel p' belongs to x's flat zone and has not been treated
            # the pixel p' is labeld as flat zone and inserted into the queue
            if ((img1[row,colum] == img1[rowPixel,columPixel]) and (imgOut [row,colum] == 0 )):
                imgOut [row,colum] = 1
                flatzone.append((row,colum))

# --- We check all neighbours of the flazone and check ----
for row in range(imgOut.shape[0]):
    for colum in range (imgOut.shape[1]):
        #if is inside the flatzone
        if imgOut[row,colum] != 0:
            for rowFlatZone in range(0 if row == 0 else row-1, row+1 if row == img1.shape[0]-1 else row+2):
                for columFlatZone in range(0 if colum == 0 else colum-1, colum+1 if colum == img1.shape[1]-1 else colum+2):
                    if img1[rowFlatZone,columFlatZone] > img1[row,colum]:
                        with open(sys.argv[3],'w') as f:
                            f.write(str(0))
                            exit()

# write the result 
with open(sys.argv[3],'w') as f:
    f.write(str(1))