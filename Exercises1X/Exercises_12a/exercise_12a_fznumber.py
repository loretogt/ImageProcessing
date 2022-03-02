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
connectivity = int(lines[0].split("\n")[0])

# Variable to count the result 
flatZoneLabel= 1

# Output image is created and initialized 
img1 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)
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

with open(sys.argv[3],'w') as f:
    f.write(str(flatZoneLabel-1))


#cv2.imwrite("ejemplo.pgm", imgOut)