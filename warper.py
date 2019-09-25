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
3-  Warper function:
*****************************
'''

# image = cv2.imread('pics/to_be_warped.jpg')
# img_size = (image.shape[1], image.shape[0])

# source (src) and destination (dst) points
# will be hardcoded here for my purpose

# src = np.float32(
#     [[(img_size[0] / 2) - 55, img_size[1] / 2 + 100],
#     [((img_size[0] / 6) - 10), img_size[1]],
#     [(img_size[0] * 5 / 6) + 60, img_size[1]],
#     [(img_size[0] / 2 + 55), img_size[1] / 2 + 100]])
# dst = np.float32(
#     [[(img_size[0] / 4), 0],
#     [(img_size[0] / 4), img_size[1]],
#     [(img_size[0] * 3 / 4), img_size[1]],
#     [(img_size[0] * 3 / 4), 0]])



def warper(img, src, dst):


    # Compute and apply perpective transform
    img_size = (img.shape[1], img.shape[0])

    src = np.float32(
        [[(img_size[0] / 2) - 55, img_size[1] / 2 + 100],
        [((img_size[0] / 6) - 10), img_size[1]],
        [(img_size[0] * 5 / 6) + 60, img_size[1]],
        [(img_size[0] / 2 + 55), img_size[1] / 2 + 100]])
    dst = np.float32(
        [[(img_size[0] / 4), 0],
        [(img_size[0] / 4), img_size[1]],
        [(img_size[0] * 3 / 4), img_size[1]],
        [(img_size[0] * 3 / 4), 0]])

    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, M, img_size, flags=cv2.INTER_NEAREST)  # keep same size as input image

    return warped

# final_image = warper(image)


# plt.imshow(final_image)
# plt.show()
# plt.imsave("pics/warped.jpg",final_image, cmap='gray')