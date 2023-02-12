import cv2
from pathlib import Path
import numpy as np

current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/imagenes/imagenborrosa.jpg"
path2 = f"{current_directory}/imagenes/imagenecualizada.jpg"
path3 = f"{current_directory}/imagenes/imagenAND.jpg"

image = cv2.imread(path)
# Convertimos la imagen en escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', gray)
cv2.waitKey(0)

# Se procesa la imagen para obtener un fondo negro
fondo = gray
_, fondo = cv2.threshold(fondo, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Se aplica la ecualizacion del histograma lineal
ecualizada = cv2.equalizeHist(gray)
cv2.imwrite(path2, ecualizada)
cv2.imshow('Ecualizada', ecualizada)
cv2.waitKey(0)

cv2.imshow('Fondo', fondo)
cv2.waitKey(0)

# Se realiza la operación lógica "AND" para generar una imagen que contiene sólo la información común a ambas imágenes
imageAND = cv2.bitwise_and(fondo, ecualizada)
cv2.imwrite(path3, imageAND)
cv2.imshow('Imagen Operacion Logica AND', imageAND)
cv2.waitKey(0)
cv2.destroyAllWindows()
