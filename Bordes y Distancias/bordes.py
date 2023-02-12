import cv2
import numpy as np
from pathlib import Path

current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/imagen/bordes.png"
path1 = f"{current_directory}/imagen/bordessuavizados.png"
path2 = f"{current_directory}/imagen/bordesyaidentificados.png"

# Cargar la imagen
img=cv2.imread(path)

# Aplicar el filtro para suavizar imagenes Filtro Non-local Means
ksize = 15 # Tamaño del kernel
smoothed = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, ksize)

#Transformar la imagen en escala de grises
gray = cv2.cvtColor(smoothed, cv2.COLOR_BGR2GRAY)

# Aplicar el operador de Sobel en dirección horizontal y vertical
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Calcular la magnitud y dirección de los bordes
magnitude = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
direction = np.arctan2(sobel_y, sobel_x)

# Umbralizar la imagen para aislar los bordes
_, thresholded = cv2.threshold(magnitude, 112, 255, cv2.THRESH_BINARY)

#Mostrar imagen original
cv2.imshow("Imagen original", img)
cv2.waitKey(0)

#Mostrar imagen suavizada
cv2.imshow("Imagen suavizada", smoothed)
cv2.imwrite(path1, smoothed)
cv2.waitKey(0)

#Sobel horizontal
cv2.imshow("sobel x", sobel_x)
cv2.waitKey(0)

#sobel vertical
cv2.imshow("sobel y", sobel_y)
cv2.waitKey(0)

# Mostrar la imagen resultante
cv2.imshow("Bordes detectados con Sobel", thresholded)
cv2.imwrite(path2, thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# Filtro de bordes en una dirección específica(segundo metodo)
angle = np.pi / 4  # Dirección deseada en radianes
threshold = 0.1  # Umbral para incluir un borde en el resultado
result = np.zeros_like(gray)
result[(direction >= angle - threshold) & (direction <= angle + threshold)] = thresholded[(direction >= angle - threshold) & (direction <= angle + threshold)]
# Mostrar la imagen resultante
cv2.imshow("Bordes filtrados en dirección", result)
cv2.waitKey(0)
'''