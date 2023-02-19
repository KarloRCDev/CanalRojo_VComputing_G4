import cv2
import numpy as np
from pathlib import Path

current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/imagenes/San marcos v5.jpg"
path1 = f"{current_directory}/imagenes/San marcos segmentada.jpg"
path2 = f"{current_directory}/imagenes/San marcos segmentada pintado de verde.jpg"

# Cargamos la imagen de San Marcos
image = cv2.imread(path)
 
# Creamos una copia para poderla manipularla
image_copy = np.copy(image)
 
# Mostramos la imagen y esperamos que el usuario presione cualquier tecla para continuar.
cv2.imshow('Imagen original', image)
cv2.waitKey(0)
 
# Convertiremos la imagen en un arreglo de ternas, las cuales representan el valor de cada pixel. En pocas palabras,
# estamos aplanando la imagen, volviéndola un vector de puntos en un espacio 3D.
pixel_values = image_copy.reshape((-1, 3))
pixel_values = np.float32(pixel_values)
 
# Aplicamos la segmentacion por K-Means.
 
# Definimos el criterio de terminación del algoritmo. En este caso, terminaremos cuando la última actualización de los
# centroides sea menor a *epsilon* (cv2.TERM_CRITERIA_EPS), donde epsilon es 1.0 (último elemento de la tupla), o bien
# cuando se hayan completado 10 iteraciones (segundo elemento de la tupla, criterio cv2.TERM_CRITERIA_MAX_ITER).
stop_criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
 
# Este es el número de veces que se correrá K-Means con diferentes inicializaciones. La función retornará los mejores
# resultados.
number_of_attempts = 10
 
# Esta es la estrategia para inicializar los centroides. En este caso, optamos por inicialización aleatoria.
centroid_initialization_strategy = cv2.KMEANS_RANDOM_CENTERS
 
# Ejecutamos K-Means con los siguientes parámetros:
# - El arreglo de pixeles.
# - K o el número de clusters a hallar.
# - None indicando que no pasaremos un arreglo opcional de las mejores etiquetas.
# - Condición de parada.
# - Número de ejecuciones.
# - Estrategia de inicialización.
#
# El algoritmo retorna las siguientes salidas:
# - Un arreglo con la distancia de cada punto a su centroide. Aquí lo ignoramos.
# - Arreglo de etiquetas.
# - Arreglo de centroides.
_, labels, centers = cv2.kmeans(pixel_values,
                                3,
                                None,
                                stop_criteria,
                                number_of_attempts,
                                centroid_initialization_strategy)
 
# Aplicamos las etiquetas a los centroides para segmentar los pixeles en su grupo correspondiente.
centers = np.uint8(centers)
segmented_data = centers[labels.flatten()]
 
# Debemos reestructurar el arreglo de datos segmentados con las dimensiones de la imagen original.
segmented_image = segmented_data.reshape(image_copy.shape)
 
# Mostramos la imagen segmentada resultante.
cv2.imshow('Imagen segmentada', segmented_image)
cv2.imwrite(path1, segmented_image)
cv2.waitKey(0)

# Creamos una máscara para el cluster 2
mask = np.zeros_like(labels)

# Asignamos 1 a los píxeles que pertenecen al cluster 2
mask[labels == 2] = 1

# Redimensionamos la máscara para que tenga la misma forma que la imagen original
mask = mask.reshape(image_copy.shape[0], image_copy.shape[1])

# Creamos una copia de la imagen segmentada
segmented_image_copy = np.copy(segmented_image)

# Pintamos de verde los píxeles que pertenecen al cluster 2
segmented_image_copy[mask == 1] = [0, 128, 0]

# Mostramos la imagen segmentada con el cluster 2 pintado de verde
cv2.imshow('Cluster 2 en verde => Areas verdes', segmented_image_copy)
cv2.imwrite(path2, segmented_image_copy)
cv2.waitKey(0)