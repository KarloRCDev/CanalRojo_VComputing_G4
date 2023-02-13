import cv2
import numpy as np
from pathlib import Path

current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/imagen/bordes.png"
path1 = f"{current_directory}/imagen/bordes2doMetodo.png"

# Cargar la imagen
img=cv2.imread(path)

# Aplicar el filtro para suavizar imagenes Filtro Non-local Means
ksize = 15 # Tamaño del kernel
smoothed = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, ksize)

# Aplicar el operador de Sobel en dirección horizontal y vertical
sobel_x = cv2.Sobel(smoothed, cv2.CV_64F, 1, 0,ksize=3)
sobel_y = cv2.Sobel(smoothed, cv2.CV_64F, 0, 1,ksize=3)
# Se usa para convertir la matriz a un tipo de datos de 8 bits sin signo (unsigned int).
sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))
sobelU = cv2.bitwise_or(sobel_x,sobel_y)

#Mostrar imagen original
cv2.imshow("Imagen original", img)
cv2.waitKey(0)

#Mostrar imagen suavizada
cv2.imshow("Imagen suavizada", smoothed)
cv2.waitKey(0)

#Sobel horizontal
cv2.imshow("sobel x", sobel_x)
cv2.waitKey(0)

#sobel vertical
cv2.imshow("sobel y", sobel_y)
cv2.waitKey(0)

#Mostrar la imagen resultante
cv2.imshow("Sobel Segundo Metodo", sobelU)
cv2.imwrite(path1, sobelU)
cv2.waitKey(0)
cv2.destroyAllWindows()

