import cv2
import numpy as np
from pathlib import Path

current_directory = Path(__file__).resolve().parent

# Leer la imagen
img = cv2.imread(f'{current_directory}/imagen/puerta.png')
img_region = img.copy()
img_distancia = img.copy()

# Mostrar la imagen y esperar a que el usuario seleccione dos puntos de interés
puntos = []


def clic(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        puntos.append((x, y))
        cv2.circle(img_distancia, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow('Imagen', img_distancia)
        if len(puntos) == 2:
            cv2.destroyAllWindows()


cv2.imshow('Imagen', img_distancia)
cv2.setMouseCallback('Imagen', clic)
cv2.waitKey(0)

# Calcular la distancia en píxeles entre los puntos seleccionados
dist_pixeles = np.linalg.norm(np.array(puntos[0]) - np.array(puntos[1]))

# Calcular la relación entre la distancia en píxeles y la distancia en metros de referencia
dist_metros = 3
escala = dist_metros / dist_pixeles

# Mostrar la relación de escala en la consola
print(f"La relación de escala es: {escala:.6f} metros por píxel")

# Esperar a que el usuario seleccione dos puntos aleatorios
puntos = []
cv2.imshow('Imagen', img_distancia)
cv2.setMouseCallback('Imagen', clic)
cv2.waitKey(0)

# Calcular la distancia en metros entre los puntos aleatorios utilizando la relación de escala
dist_metros = np.linalg.norm(
    np.array(puntos[0]) - np.array(puntos[1])) * escala

# Mostrar la distancia en la imagen y en la consola
cv2.line(img_distancia, puntos[0], puntos[1], (0, 255, 0), 2)
cv2.putText(img_distancia, f"Distancia: {dist_metros:.2f} metros",
            (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
print(f"La distancia entre los puntos es: {dist_metros:.2f} metros")

cv2.imshow('Imagen', img_distancia)
cv2.waitKey(0)


# Esperar a que el usuario seleccione una región
roi = cv2.selectROI(img_region)

# Calcular el área de la región seleccionada utilizando la relación de escala
area_metros = (roi[2] * escala) * (roi[3] * escala)

# Mostrar el área en la imagen y en la consola
cv2.rectangle(img_region, (int(roi[0]), int(roi[1])), (int(
    roi[0]+roi[2]), int(roi[1]+roi[3])), (0, 255, 0), 2)
cv2.putText(img_region, f"Area: {area_metros:.2f} metros cuadrados",
            (25, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
print(
    f"El área de la región seleccionada es: {area_metros:.2f} m2")


# Mostrar la imagen con la distancia calculada
cv2.imshow('Imagen', img_region)
cv2.waitKey(0)
cv2.destroyAllWindows()
