import cv2
from pathlib import Path
import numpy as np

current_directory = Path(__file__).resolve().parent


# Load an image
image = cv2.imread(f"{current_directory}/imagenes/image.jpg")

# Define the region of interest (ROI)
x, y, w, h = 200, 30, 250, 250
roi = image[y:y+h, x:x+w]

# Define the shear transformation matrix
shear_matrix = np.float32([[1, 0.5, 0], [0, 1, 0]])

# Apply the shear transformation to the ROI
sheared_roi = cv2.warpAffine(roi, shear_matrix, (w, h))

# Replace the original ROI with the sheared ROI
image[y:y+h, x:x+w] = sheared_roi

# Display the image
cv2.imshow("Sheared Image", image)
cv2.waitKey(0)
