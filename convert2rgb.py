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
print(r_array.dtype)

rgb_array = np.stack((r_array, g_array, b_array), axis=-1)


cv2.imshow('RGB Image', rgb_array)
cv2.imwrite('RGB_image_no_allignment.jpg', rgb_array)
cv2.waitKey(0)
cv2.destroyAllWindows()