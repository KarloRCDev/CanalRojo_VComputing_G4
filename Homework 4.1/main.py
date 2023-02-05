import cv2
from pathlib import Path
import numpy as np

current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/imagenes/imagenborrosa.jpg"
path2 = f"{current_directory}/imagenes/imagenecualizada.jpg"
path3 = f"{current_directory}/imagenes/imagenAND.jpg" 

image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Convertimos la imagen en escala de grises
cv2.imshow('Original',gray)
cv2.waitKey(0)

# Se procesa la imagen para obtener un fondo negro
fondo = gray
_, fondo = cv2.threshold(fondo,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Se aplica la ecualizacion del histograma lineal
ecualizada = cv2.equalizeHist(gray)
cv2.imwrite(path2, ecualizada)
cv2.imshow('Ecualizada',ecualizada)
cv2.waitKey(0)

cv2.imshow('Fondo',fondo)
cv2.waitKey(0)

# Se realiza la operación lógica "AND" para generar una imagen que contiene sólo la información común a ambas imágenes
imageAND = cv2.bitwise_and(fondo , ecualizada)
cv2.imwrite(path3, imageAND)
cv2.imshow('Imagen Operacion Logica AND',imageAND)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''# Se calcula el histograma de la imagen en escala de grises (Funcionamiento de cv2.equalizeHist )
#El método np.histogram devuelve dos resultados: una lista hist que contiene el número de 
#pixels con cada intensidad, y una lista bins que contiene los límites de los bins.
hist, bins = np.histogram(gray.flatten(), 256, [0, 256]) 

# Se calcula la función de distribución acumulativa(CFD)
cdf = hist.cumsum() #se utiliza para calcular la suma acumulativa de los valores del histograma
cdf_normalized = cdf * hist.max() / cdf.max() #se normaliza la función de distribución acumulativa(CDF) para mejorar la apariencia y la claridad de la imagen

# Se crea una tabla de look-up para la ecualización de histograma lineal
cdf_m = np.ma.masked_equal(cdf, 0) #se crea una máscara en la función de distribución acumulativa (CDF) 
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min()) #para que los valores en la CDF estén en el rango de 0 a 255
cdf = np.ma.filled(cdf_m, 0).astype('uint8')#convierte los valores de la función de distribución acumulativa escalada (CDF) en un array de tipo entero sin signo de 8 bits 

# Se aplica la ecualización del histograma a la imagen
ecualizada = cdf[gray]'''