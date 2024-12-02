from PIL import Image
import numpy as np
import cv2

r_band = Image.open("image_red.tif")
g_band = Image.open("image_green.tif")
b_band = Image.open("image_blue.tif")

r_array = np.array(r_band)
g_array = np.array(g_band)
b_array = np.array(b_band)

r_array = (r_array >> 8).astype('uint8')
g_array = (g_array >> 8).astype('uint8')
b_array = (b_array >> 8).astype('uint8')

def align_channels(base, shift):
    # ORB (Oriented FAST and Rotated BRIEF)
    orb = cv2.ORB_create()

    keypoints1, descriptors1 = orb.detectAndCompute(base, None)
    keypoints2, descriptors2 = orb.detectAndCompute(shift, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)

    src_pts = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)

    M, mask = cv2.estimateAffinePartial2D(src_pts, dst_pts)

    shifted = cv2.warpAffine(shift, M, (base.shape[1], base.shape[0]))

    return shifted

aligned_g_array = align_channels(r_array, g_array)
aligned_b_array = align_channels(r_array, b_array)

rgb_array = np.stack((r_array, aligned_g_array, aligned_b_array), axis=-1)

cv2.imshow('Aligned RGB Image', rgb_array)
cv2.imwrite('RGB_image.jpg', rgb_array)
cv2.waitKey(0)
cv2.destroyAllWindows()