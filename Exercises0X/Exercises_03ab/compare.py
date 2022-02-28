# import cv2 as cv
import cv2
import sys

if len(sys.argv) != 3:
    print("The call to the function is incorrect, 3 elements need to be introduced ")
    exit()

img1 = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)

#If the images have diferent size
if img1.size != img2.size :
    with open('exercise_02b_output_01.txt', 'w') as f:
        f.write(str(0))
        exit()

#Compare de images
for row in range(img1.shape[0]):
    for colum in range (img1.shape[1]):
        if img1[row,colum] != img2[row,colum]:
            with open('exercise_02b_output_01.txt', 'w') as f:
                f.write(str(0))
                exit()

#If the images are equal 
with open('exercise_02b_output_01.txt', 'w') as f:
    f.write(str(1))