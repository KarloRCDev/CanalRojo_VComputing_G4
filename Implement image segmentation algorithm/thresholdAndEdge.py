import cv2
import numpy as np
from pathlib import Path

current_directory = Path(__file__).resolve().parent

# Load the image
image = cv2.imread(f'{current_directory}/images/image.jpg')

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to segment the image
threshold_value = 127
max_value = 255
_, thresholded_image = cv2.threshold(
    img_gray, threshold_value, max_value, cv2.THRESH_BINARY)

# Display the original and segmented images
cv2.imshow('Original Image', img_gray)
cv2.imshow('Segmented Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
