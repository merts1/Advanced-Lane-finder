'''
Mert Hacıahmetoğlu

Advanced lane finder project 

03.09.2019
'''
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle
import glob


'''
*****************************
1-  Calibrating camera code:
*****************************
'''

# prepare object points
objp = np.zeros((6*8,3), np.float32)
objp[:,:2] = np.mgrid[0:8, 0:6].T.reshape(-1,2)

# arrays to store them
objpoints = [] # 3d points in real world
imgpoints = [] # 2d points in image

# Gopro pictures are uploaded to system
images = glob.glob('calibration_wide/GO*.jpg')

# for loop to iterate through images
for idx, fname in enumerate(images):
	img = cv2.imread(fname) #read the file
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #gray scale

	ret, corners = cv2.findChessboardCorners(gray, (8,6), None)
	#here trying to find the chessboard corners for each image

	#and if found:
	if ret == True:
		objpoints.append(objp)
		imgpoints.append(corners)
		# append the neccesity data

		#no need to draw and show images here if you want you
		#can create a section to do.

# now we have objpoints and imgpoints needed for camera calibration
#calibration_wide/test_image.jpg
# let's read the initial undistortion
img = cv2.imread('mytest.jpg')
img_size = (img.shape[1], img.shape[0])

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size,None,None)
# camera calibration with the help of obtained object and image points

# apply this distortion correction
dst = cv2.undistort(img, mtx, dist, None, mtx)
cv2.imwrite('calibration_wide/test_undist.jpg',dst)
# test it on the datum

# now if we had accurate results we can save the model for later use
# it's your choice to save it, I will comment down the code here.

#	dist_pickle = {}
#	dist_pickle["mtx"] = mtx
#	dist_pickle["dist"] = dist
#	pickle.dump( dist_pickle, open( "calibration_wide/wide_dist_pickle.p", "wb" ) )

# * uncomment this part if you want to save the camera calibration

