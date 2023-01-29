import cv2
from pathlib import Path

current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/imagenes/image.jpg"


# Carga la imagen
image = cv2.imread(path)
b, g, r = cv2.split(image) # Separa la imagen en sus 3 canales blue, green, red en escala de grises


# Crea una copia de la imagen solo con el canal rojo
red = image.copy()
red[:, :, 0] = 0
red[:, :, 1] = 0

# Muestra la imagen original
cv2.imshow("Original", image)
cv2.waitKey(0) # Espera a que el usuario presione una tecla
# Muestra el canal rojo de la imagen en escala de grises
cv2.imshow("Canal rojo en escala de grises", r)
cv2.waitKey(0) # Espera a que el usuario presione una tecla
cv2.imshow("Canal rojo 2", red)
cv2.waitKey(0)
cv2.destroyAllWindows()