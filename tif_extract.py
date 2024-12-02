from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

file_path = 'test.tif'

image_data_opencv = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)

if image_data_opencv is None:
    print("No file.")
else:
    plt.title("OpenCV")
    plt.imshow(image_data_opencv, cmap='hot')
    plt.colorbar()
    plt.show()