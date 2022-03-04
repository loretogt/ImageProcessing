import queue
import cv2
import sys
import numpy as np

def regMax (img1,rowPixel, columPixel):
    imgAux= np.zeros((img1.shape[0],img1.shape[1]), np.uint32)
    #--- We create the flatzone ----
    # The value of pixel x is output image is labeled as flat zone
    imgAux[rowPixel,columPixel]= 1

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
                if ((img1[row,colum] == img1[rowPixel,columPixel]) and (imgAux [row,colum] == 0 )):
                    imgAux [row,colum] = 1
                    flatzone.append((row,colum))

    # --- We check all neighbours of the flazone and check ----
    for row in range(imgAux.shape[0]):
        for colum in range (imgAux.shape[1]):
            #if is inside the flatzone
            if imgAux[row,colum] != 0:
                for rowFlatZone in range(0 if row == 0 else row-1, row+1 if row == img1.shape[0]-1 else row+2):
                    for columFlatZone in range(0 if colum == 0 else colum-1, colum+1 if colum == img1.shape[1]-1 else colum+2):
                        if img1[rowFlatZone,columFlatZone] > img1[row,colum]:
                            return False
    return True

if len(sys.argv) != 3:
    print("The call to the function is incorrect, 2 elements need to be introduced ")
    exit()
  
# Output image is created and initialized 
img1 = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
imgOut= np.zeros((img1.shape[0],img1.shape[1]), np.uint8)

for row in range(img1.shape[0]):
    if (row%10 ==0):
        print("Row: " + str(row))
    for colum in range (img1.shape[1]):
        if regMax (img1,row, colum) == True:
            imgOut[row,colum] = 255

cv2.imwrite(sys.argv[2], imgOut)