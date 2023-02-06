import cv2
import os
import numpy as np
from pathlib import Path

current_directory = Path(__file__).resolve().parent
# path = f"{current_directory}/imagenes/imagen10.jpg"


path = f"{current_directory}\\imagenes\\"


def masks(img):
    # Conversión de imagen a HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Obtener el número de filas y columnas de la imagen
    rows, cols, _ = img.shape

    # Calcular el número total de píxeles
    num_pixels = rows * cols

    # Definir un rango de colores en HSV (10 soles)
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])
    # Aplicar una máscara para determinar si un color está dentro del rango
    maskverde = cv2.inRange(hsv, lower_green, upper_green)
    # Aplicar la máscara a la imagen original

    # Definir el rango de tonos marrones (20 soles)
    lower_marron = np.array([10, 50, 50])
    upper_marron = np.array([20, 255, 255])
    # Crear una máscara que identifique el color amarillo ocre
    maskMarron = cv2.inRange(hsv, lower_marron, upper_marron)
    # Aplicar la máscara a la imagen original

    # Definir un rango de colores en HSV (50 soles)
    lower_pink = np.array([150, 50, 50])
    upper_pink = np.array([180, 255, 255])
    # Aplicar una máscara para determinar si un color está dentro del rango
    maskRosa = cv2.inRange(hsv, lower_pink, upper_pink)
    # Aplicar la máscara a la imagen original

    # Definir un rango de colores en HSV (100 soles)
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])
    # Aplicar una máscara para determinar si un color está dentro del rango
    maskAzul = cv2.inRange(hsv, lower_blue, upper_blue)
    # Aplicar la máscara a la imagen original

    if np.count_nonzero(maskverde) > 0.1*num_pixels:
        print("El billete es de 10 soles")
        maskFinal = maskverde

    # Condicional para enviar un mensaje si se detecta un billete de color marron
    if np.count_nonzero(maskMarron) > 0.05*num_pixels:
        print("El billete es de 20 soles")
        maskFinal = maskMarron

    # Condicional para enviar un mensaje si se detecta un billete de color rosa
    if np.count_nonzero(maskRosa) > 0.05*num_pixels:
        print("El billete es de 50 soles")
        maskFinal = maskRosa

    # Condicional para enviar un mensaje si se detecta un billete de color azul
    if np.count_nonzero(maskAzul) > 0.05*num_pixels:
        print("El billete es de 100 soles")
        maskFinal = maskAzul

    resultado = cv2.bitwise_and(img, img, mask=maskFinal)

    # Mostrar la imagen resultante
    cv2.imshow("Imagen original\n", img)
    cv2.waitKey(0)
    cv2.imshow("Resultado de imagen: ", resultado)
    cv2.waitKey(0)


for filename in os.listdir(path):
    if filename.endswith('.jpg'):
        path_image = os.path.join(path, filename)
        img = cv2.imread(path_image)
        masks(img)
        # print(path_image)

cv2.destroyAllWindows()
