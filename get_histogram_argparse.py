import argparse
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Process image and display various plots.")
parser.add_argument('--row', type=int, default=0, help="Row index for plotting pixel values.")
parser.add_argument('--column', type=int, default=0, help="Column index for plotting pixel values.")
parser.add_argument('--file_path', type=str, default='IMG_0000_1.tif', help="Path to the image file.")
args = parser.parse_args()

column = args.column
row = args.row
file_path = args.file_path

image_data_opencv = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
img_height, img_width = image_data_opencv.shape[:2]

if image_data_opencv is None:
    print("No file.")

if row >= img_height or column >= img_width:
    print(f"Error: Provided row or column exceeds image dimensions. "
          f"Image size: {img_height}x{img_width}, Provided row: {row}, column: {column}")


else:
    fig, axes = plt.subplots(3, 2, figsize=(20, 30))
    overall_mean = np.mean(image_data_opencv)
    overall_mean = round(overall_mean, 2)
    print("Overall Mean Pixel Value:", overall_mean)


    axes[0, 0].imshow(image_data_opencv, cmap='hot')
    axes[0, 0].set_title("Image Display")
    fig.colorbar(axes[0, 0].imshow(image_data_opencv, cmap='hot'), ax=axes[0, 0])

    row_mean = np.mean(image_data_opencv, axis=1)  # Mean for each row
    axes[1, 0].plot(row_mean)
    axes[1, 0].set_title("Row-wise Pixel Mean")
    axes[1, 0].set_xlabel("Row Index")
    axes[1, 0].set_ylabel("Average Pixel Value")
    axes[1, 0].grid(True)

    col_mean = np.mean(image_data_opencv, axis=0)  # Mean for each column
    axes[1, 1].plot(col_mean)
    axes[1, 1].set_title("Column-wise Pixel Mean")
    axes[1, 1].set_xlabel("Column Index")
    axes[1, 1].set_ylabel("Average Pixel Value")
    axes[1, 1].grid(True)

    axes[2, 0].plot(image_data_opencv[:, row])
    axes[2, 0].set_title(f"Pixel Values for Row {row}")
    axes[2, 0].set_xlabel("Column Index")
    axes[2, 0].set_ylabel("Pixel Value")
    axes[2, 0].grid(True)

    axes[2, 1].plot(image_data_opencv[column, :])
    axes[2, 1].set_title(f"Pixel Values for Column {column}")
    axes[2, 1].set_xlabel("Row Index")
    axes[2, 1].set_ylabel("Pixel Value")
    axes[2, 1].grid(True)

    axes[0, 1].axis('off')

    fig.subplots_adjust(hspace=0.6, wspace=0.4)
    plt.show()