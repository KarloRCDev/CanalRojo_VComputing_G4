import cv2
from pathlib import Path

current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/imagenes/image.jpg"
path2 = f"{current_directory}/imagenesDPI/image_72dpi.jpg"

# Carga la imagen
image = cv2.imread(path) #La funcion devuelve un numpy ndarray

# Calcula la relación de aspecto de la imagen
height, width = image.shape[:2] #Se obtiene las dimensiones de una imagen en formato numpy ndarray
aspect_ratio = width / height
#Dimensiones de una hoja A4: 8,27 x 11,67

# Calcula las dimensiones de la imagen de 72 dpi
anchopA4 = 8.27
alturapA4 = 11.67
dpi = 72
new_width = int(dpi*anchopA4)
new_height = int(dpi*alturapA4)

# Cambia el tamaño de la imagen a las dimensiones de 72 dpi
resized_image = cv2.resize(image, (new_width, new_height), interpolation = cv2.INTER_LINEAR)

# Guarda la imagen con resolución de 72 dpi
cv2.imwrite(path2, resized_image)