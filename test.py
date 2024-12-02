from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

column = 0
row = 0
file_path = 'IMG_0000_1.tif'

image_data_opencv = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)

if image_data_opencv is None:
    print("No file.")
else:
    plt.imshow(image_data_opencv, cmap='hot')
    plt.colorbar()
    plt.show()

    row_mean = np.mean(image_data_opencv, axis=1)  # 각 행에 대해 평균
    plt.figure(figsize=(12, 6))
    plt.plot(row_mean)
    plt.title("Row-wise Pixel Mean")
    plt.xlabel("Row Index")
    plt.ylabel("Average Pixel Value")
    plt.grid(True)
    plt.show()

    col_mean = np.mean(image_data_opencv, axis=0)  # 각 열에 대해 평균
    plt.figure(figsize=(12, 6))
    plt.plot(col_mean)
    plt.title("Column-wise Pixel Mean")
    plt.xlabel("Column Index")
    plt.ylabel("Average Pixel Value")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.plot(image_data_opencv[:, row])
    plt.xlabel("Row Index")
    plt.ylabel("Pixel Value")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.plot(image_data_opencv[column, :])
    plt.xlabel("Column Index")
    plt.ylabel("Pixel Value")
    plt.grid(True)
    plt.show()