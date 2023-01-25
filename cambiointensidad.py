import cv2
from pathlib import Path
import numpy as np


current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/imagenes/image.jpg"
image = cv2.imread(path)
# Muestra la imagen original
cv2.imshow("Original", image)
cv2.waitKey(0) # Espera a que el usuario presione una tecla
# Obtener el canal deseado
channel = image[:, :, 2]

# Cambiar la intensidad del canal a 16 niveles
channel = (channel / 16).astype(np.uint8)

# Reinsertar el canal modificado en la imagen
image[:, :, 2] = channel

# Muestra la imagen original
cv2.imshow("Alterado", image)
cv2.waitKey(0) # Espera a que el usuario presione una tecla