import cv2
from pathlib import Path
import numpy as np

current_directory = Path(__file__).resolve().parent
'''path = f"{current_directory}/imagenesDPI/image_72dpi.jpg"
path2 = f"{current_directory}/imagenesDPI"

img = cv2.imread(path)

# Rotate the image by 90 degrees clockwise
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Save the rotated image
cv2.imwrite(f"{path2}/rotated_image.jpg", img)
cv2.imshow("Rotated", img)
cv2.waitKey(0)  # Espera a que el usuario presione una tecla

img_reflected = cv2.flip(img, 1)
cv2.imshow("Reflected", img_reflected)
cv2.waitKey(0)  # Espera a que el usuario presione una tecla
'''

# Load an image
image = cv2.imread(f"{current_directory}/imagenes/image.jpg")

# Define the shear transformation matrix
shear_matrix = np.float32([[1, 0.5, 0], [0, 1, 0]])

# Apply the shear transformation
sheared_image = cv2.warpAffine(
    image, shear_matrix, (image.shape[1], image.shape[0]))

# Display the image
cv2.imshow("Sheared Image", sheared_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
