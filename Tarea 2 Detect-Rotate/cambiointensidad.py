import cv2
from pathlib import Path
import numpy as np

current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/imagenes/per.jpg"
path2 = f"{current_directory}/imagenesChangeIntensify"

# Cargar la imagen de entrada
img = cv2.imread(path)
# Separa la imagen en sus tres canales blue,green,red
b16, g16, r16 = cv2.split(img)
b2, g2, r2 = cv2.split(img)
canal = input('Que canal desea editar la intensidad? (R),(G),(B): ')

# Permite limitar los valores de una matriz NumPy a un intervalo determinado. En este caso, iguala la intensidad a 16 y 2, respectivamente
if canal in ['r', 'R']:
    r16 = np.clip(r16, 16, 16)
    r2 = np.clip(r2, 2, 2)
if canal in ['g', 'G']:
    g16 = np.clip(g16, 16, 16)
<<<<<<< HEAD
    r2 = np.clip(r2, 2, 2)
if canal in ['b', 'B']:
    b16 = np.clip(b16, 16, 16)
    r2 = np.clip(r2, 2, 2)
# r = np.where(r > 16, 16, r) #Metodo opcional donde se transforma la intensidad de cada pixel mayor a 16 del canal rojo a 16
# r = np.where(r < 16, 16, r) #Metodo opcional donde se transforma la intensidad de cada pixel menor a 16 del canal rojo a 16
=======
    g2 = np.clip(r2, 2, 2)
if canal in ['b','B']:
    b16 = np.clip(b16, 16, 16)
    b2 = np.clip(r2, 2, 2)
#r = np.where(r > 16, 16, r) #Metodo opcional donde se transforma la intensidad de cada pixel mayor a 16 del canal rojo a 16
#r = np.where(r < 16, 16, r) #Metodo opcional donde se transforma la intensidad de cada pixel menor a 16 del canal rojo a 16
>>>>>>> f88c054450bbf3cf51a348b873ddad72d3688938

# MUESTRA LOS 3 CANALES POR SEPARADO a un nivel de intensidad 16
cv2.imshow('Blue - 16', b16)
cv2.imshow('Green - 16', g16)
cv2.imshow('Red - 16', r16)

# MUESTRA LA IMAGEN DONDE SE RECOMBINA LOS 3 CANALES a un nivel de intensidad 16
merged_img_16 = cv2.merge([b16, g16, r16])
cv2.imshow("Merged - 16", merged_img_16)
cv2.imwrite(f"{path2}/change_intensity_image16.jpg", merged_img_16)
cv2.waitKey(0)
cv2.destroyAllWindows()

# MUESTRA LOS 3 CANALES POR SEPARADADO a un nivel de intensidad 2
cv2.imshow('Blue - 2', b2)
cv2.imshow('Green - 2', g2)
cv2.imshow('Red - 2', r2)

# MUESTRA LA IMAGEN DONDE SE RECOMBINA LOS 3 CANALES a un nivel de intensidad 2
merged_img_2 = cv2.merge([b2, g2, r2])
cv2.imshow("Merged - 2", merged_img_2)
cv2.imwrite(f"{path2}/change_intensity_image2.jpg", merged_img_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
