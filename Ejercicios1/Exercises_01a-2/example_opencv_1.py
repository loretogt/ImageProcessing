#! /usr/bin/python


# import cv2 as cv
import cv2


# https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/
# img1 = cv2.imread("cam_74.pgm")
img1 = cv2.imread("cam_74.pgm", cv2.IMREAD_GRAYSCALE)



# https://docs.opencv.org/4.x/d3/df2/tutorial_py_basic_ops.html




# Print the image dimensions: tuple of the number of rows and columns
# (and if several bands, number of bands or channels)
print(img1.shape)

nrows = img1.shape[0]
ncols = img1.shape[1]


# Number of pixels
print(img1.size)

# Image type
print(img1.dtype)


# 2D image: [row,column]
# print(img1[row,column]): for graylevel image, the intensity is printed;
# for color images, an array of BGR values is printed.


# Copy of image
img2 = img1.copy()


print("--------------------------------")
print("img2[0,0]:", img2[0,0])
print("img2[0,1]:", img2[0,1])
print("img2[0,ncols-1]:", img2[0,ncols-1])
print("img2[nrows-1,0]:", img2[nrows-1,0])
print("img2[nrows-1,ncols-1]:", img2[nrows-1,ncols-1])


img2[0,0] = 1
img2[0,1] = 2
img2[0,ncols-1] = 3
img2[nrows-1,0] = 4
img2[nrows-1,ncols-1] = 5


print("--------------------------------")
print("After modifying those pixel values:")
print("img2[0,0]:", img2[0,0])
print("img2[0,1]:", img2[0,1])
print("img2[0,ncols-1]:", img2[0,ncols-1])
print("img2[nrows-1,0]:", img2[nrows-1,0])
print("img2[nrows-1,ncols-1]:", img2[nrows-1,ncols-1])
print("--------------------------------")


print("Saving image to file output1.pgm ...")
cv2.imwrite("output1.pgm", img2);
# Saving to .png :
# cv2.imwrite("output1.png", img2);


print("Showing image in window... Press a key to finish.")
cv2.imshow("Window: img2", img2)
cv2.waitKey(0) # waiting for a key


# cv2.destroyAllWindows()


########################################
########################################


# # In Linux, to install (Ubuntu):
# sudo apt install libopencv-dev python3-opencv

# # Note: to check the installed version:
# python3 -c "import cv2; print(cv2.__version__)"


########################################
########################################
