import cv2
import numpy as np
from pathlib import Path

current_directory = Path(__file__).resolve().parent


# Carga de imagen desde la ruta especificada
path = f"{current_directory}/images/unmsm.jpg"

img = cv2.imread(path)

# Define the RGB values to segment
rgb_values = [(103, 122, 103), (34, 44, 45), (87, 105, 89), (107, 122, 101), (99, 124, 102),
              (39, 55, 44), (50, 63, 54), (81, 87, 77), (49, 70, 55)]

# Convert the RGB values to a NumPy array
rgb_array = np.array(rgb_values)

# Find the maximum and minimum values for each channel
min_values = np.min(rgb_array, axis=0)
max_values = np.max(rgb_array, axis=0)

# Apply the thresholding
mask = cv2.inRange(img, min_values, max_values)

# Apply a median blur to remove small noise
mask = cv2.medianBlur(mask, 5)

# Apply the mask to the duplicate image
img_copy = img.copy()
result = cv2.bitwise_and(img_copy, img_copy, mask=mask)


# Display the result

cv2.imshow("Original", img)

cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
