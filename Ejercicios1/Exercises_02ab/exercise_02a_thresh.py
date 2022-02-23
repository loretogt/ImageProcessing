# import cv2 as cv
import cv2
import sys

if len(sys.argv) != 4:
    print("The call to the function is incorrect, 3 elements need to be introduced ")
    exit()

img1 = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

value = int(sys.argv[2])

# Copy of image
img2 = img1.copy()

# Thresholding operation
for row in range(img1.shape[0]):
    for colum in range (img1.shape[1]):
        if img2[row,colum] >= value:
            img2[row,colum] = 255
        else:
            img2[row,colum] = 0

# Save the result 
cv2.imwrite(sys.argv[3], img2);

print("Showing image in window... Press a key to finish.")
cv2.imshow("Window: img2", img2)
cv2.waitKey(0) # waiting for a key