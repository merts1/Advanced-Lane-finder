'''
Mert Hacıahmetoğlu

Advanced lane finder project 

03.09.2019
'''
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


'''
*****************************
2-  Color and Gradient Space:
*****************************
'''


# This code is just used by me to test pipeline with an image it's not necessary,
# since this script is mainly about creating pipeline function.

# image = cv2.imread('color_gradient.jpg')

# Here is the pipeline function to apply;
# 	1-Camera calibration
# 	2-Distortion correction
# 	3-Color/gradient threshold
# 	at once on single image.


# Default values for threshold of x gradient (sx_thresh) and color 
# channel (s_thresh) are given in the parantheses.
def pipeline(img, s_thresh=(170, 255), sx_thresh=(20, 100)):
    img = np.copy(img)

    # Convert to HLS color space and separate the V channel
    hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    l_channel = hls[:,:,1]
    s_channel = hls[:,:,2]

    # Sobel x operator
    sobelx = cv2.Sobel(l_channel, cv2.CV_64F, 1, 0) # Take the derivative in x
    abs_sobelx = np.absolute(sobelx) # Absolute x derivative to accentuate lines away from horizontal
    scaled_sobel = np.uint8(255*abs_sobelx/np.max(abs_sobelx))
    
    # Threshold x gradient:
    sxbinary = np.zeros_like(scaled_sobel)
    sxbinary[(scaled_sobel >= sx_thresh[0]) & (scaled_sobel <= sx_thresh[1])] = 1
    
    # Threshold color channel:
    s_binary = np.zeros_like(s_channel)
    s_binary[(s_channel >= s_thresh[0]) & (s_channel <= s_thresh[1])] = 1

    # Stack each channel:
    color_binary = np.dstack(( np.zeros_like(sxbinary), sxbinary, s_binary)) * 255

    # Now we have the drawings of both binary thresholding the S channel 
    # and sobel operator in the x direction on the image.

    # Let's combine them.
    combined_binary = np.zeros_like(sxbinary)
    combined_binary[(s_binary == 1) | (sxbinary == 1)] = 1
    
    return combined_binary
    
# result = pipeline(image)
# plt.imshow(result, cmap='gray')
# plt.show()
# plt.imsave("color_gradient_end.png",result, cmap='gray')