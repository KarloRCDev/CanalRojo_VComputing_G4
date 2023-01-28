import cv2
from pathlib import Path
import numpy as np

current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/imagenes/image.jpg"
path2 = f"{current_directory}/imagenesRotated"
path3 = f"{current_directory}/imagenesReflected"

img = cv2.imread(path)
cv2.imshow("Original", img)
cv2.waitKey(0)

# Rotar la imagen 90 grados
img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Guardar y mostrar la imagen
cv2.imwrite(f"{path2}/rotated_image.jpg", img_rotated)
cv2.imshow("Rotated", img_rotated)
cv2.waitKey(0)  # Espera a que el usuario presione una tecla

#Reflejar la imagen
img_reflected = cv2.flip(img, 1)

# Guardar y mostrar la imagen
cv2.imwrite(f"{path3}/rotated_image.jpg", img_reflected)
cv2.imshow("Reflected", img_reflected)
cv2.waitKey(0)  # Espera a que el usuario presione una tecla