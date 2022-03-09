import cv2
import sys
import numpy as np

def erosion (img1, size):
    imgOut= img1.copy()
    for row in range(img1.shape[0]):
        for colum in range (img1.shape[1]):
            elems= img1[0 if row-size < 0 else row-size:row+size if row+size > img1.shape[0] else row+size+1,\
                0 if colum-size < 0 else colum-size:colum+size if colum+size > img1.shape[1] else colum+size+1]
            imgOut[row,colum]= np.min(elems)
    return imgOut

def dilation (image, size):
    imgOut= image.copy()
    for row in range(image.shape[0]):
        for colum in range (image.shape[1]):
            elems= image[0 if row-size < 0 else row-size:row+size if row+size > image.shape[0] else row+size+1,\
                0 if colum-size < 0 else colum-size:colum+size if colum+size > image.shape[1] else colum+size+1]
            imgOut[row,colum]= np.max(elems)
    return imgOut

def subtraction(img1, img2):
    imgOut= img1.copy()
    for row in range(img1.shape[0]):
        for colum in range (img1.shape[1]):
            imgOut[row, colum] = img1[row, colum] - img2[row, colum]
    return imgOut

def coutnFlatZones (img1):
        # Variable to count the result 
    flatZoneLabel= 1

    # Output image is created and initialized 
    imgOut= np.zeros((img1.shape[0],img1.shape[1]), np.uint32)

    #We itereate over the image
    for row in range(img1.shape[0]):
        for colum in range (img1.shape[1]):

            #if the pixel has not been treated we do the flatzone of these one 
            if imgOut [row,colum] == 0: 

                # The value of pixel t is output image is labeled as flat zone
                imgOut[row,colum]= flatZoneLabel

                #Creation of the flatzone waiting queue 
                flatzone =[]

                #Initialization of flatozne with pixel t
                flatzone.append((row,colum))

                #while the flatzone is not empty
                while len(flatzone)!=0:
                    p = flatzone.pop()
                    #for all neighbors p'
                    for rowFlatZone in range(0 if p[0] == 0 else p[0]-1, p[0]+1 if p[0] == img1.shape[0]-1 else p[0]+2):
                        for columFlatZone in range(0 if p[1] == 0 else p[1]-1, p[1]+1 if p[1] == img1.shape[1]-1 else p[1]+2):
                            # the the pixel p' belongs to x's flat zone and has not been treated
                            # the pixel p' is labeld as flat zone and inserted into the queue
                            if ((img1[rowFlatZone,columFlatZone] == img1[row,colum]) and (imgOut[rowFlatZone,columFlatZone] == 0)):
                                imgOut [rowFlatZone,columFlatZone] = flatZoneLabel
                                flatzone.append((rowFlatZone,columFlatZone))
                # Increment of flatZoneLabel
                flatZoneLabel +=1
    return flatZoneLabel-1

'''
if len(sys.argv) != 2:
    print("The call to the function is incorrect, 1 elements need to be introduced ")
    exit()
'''

img1 = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

ero = erosion(img1, 2)
ero2 = dilation(ero, 1)
sub = subtraction (img1, ero2)
imgOut = erosion(sub, 1)

print("The number of teeth is " + str(coutnFlatZones(imgOut)))

cv2.imwrite(sys.argv[2], imgOut)