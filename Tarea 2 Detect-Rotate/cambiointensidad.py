import cv2
from pathlib import Path
import numpy as np


current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/imagenes/image.jpg"
image = cv2.imread(path)
image2 = cv2.imread(path)
# Muestra la imagen original
cv2.imshow("Original", image)
cv2.waitKey(0) # Espera a que el usuario presione una tecla
#######################################################################
# Obtener el canal deseado
channel = image[:, :, 2]

# Cambiar la intensidad del canal a 16 niveles
channel = (channel / 16).astype(np.uint8)

# Reinsertar el canal modificado en la imagen
image[:, :, 2] = channel

# Muestra la imagen alterada
cv2.imshow("Alterado a 16", image)

cv2.waitKey(0) # Espera a que el usuario presione una tecla
########################################################################
# Obtener el canal deseado
channel2 = image2[:, :, 2]

# Cambiar la intensidad del canal a 2 niveles
channel2 = (channel2 > 128).astype(np.uint8)

# Reinsertar el canal modificado en la imagen
image2[:, :, 2] = channel2
# Muestra la imagen alterada
cv2.imshow("Alterado a 2", image2)

cv2.waitKey(0) # Espera a que el usuario presione una tecla