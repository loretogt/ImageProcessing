import cv2
import sys

if len(sys.argv) != 4:
    print("The call to the function is incorrect, 3 elements need to be introduced ")
    exit()

img1 = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)

# Copy of image
img3 = img1.copy()
# Thresholding operation
for row in range(img1.shape[0]):
    for colum in range (img1.shape[1]):
        img3[row,colum] = min(img1[row,colum], img2[row,colum])

# Save the result 
cv2.imwrite(sys.argv[3], img3)