import cv2
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/imagenes/image.jpg"
path2 = f"{current_directory}/imagenesshear/imageshear.jpg"

# leer la imagen de entrada
img = cv2.imread(path)
# convertir de BGR a RGB para que podamos utilizar matplotlib
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# deshabilitar el eje x e y
plt.axis('off')
# mostrar la imagen original
plt.imshow(img)
plt.show()

# determinar el eje y la inclinacion de la imagen
eje = input("En q direccion desea aplicar el efecto shear? (X/Y): ")
if eje in ["y", "Y"]:
    inclinacion = input("Inclinar hacia la derecha(R) o hacia la izquierda(L)?: ")
    if inclinacion in ["r","R"]:
        img = cv2.copyMakeBorder(img, 380, 0, 40, 40, cv2.BORDER_CONSTANT, value = (0, 0, 0)) # Añadiendo un borde negro para q se visualice mejor el efecto shear
        rows, cols, dim = img.shape # obtener la forma de la imagen
        # matriz de transformación para Shearing
        # shearing aplicado al eje x
        M = np.float32([[1, 0, 0],
            	        [-0.5, 1, 0],
           	            [0, 0, 1]])
    if inclinacion in ["l","L"]:
        img = cv2.copyMakeBorder(img, 0, 380, 40, 40, cv2.BORDER_CONSTANT, value = (0, 0, 0)) # Añadiendo un borde negro para q se visualice mejor el efecto shear
        rows, cols, dim = img.shape
        M = np.float32([[1, 0, 0],
            	        [0.5, 1, 0],
           	            [0, 0, 1]])
if eje in ["x", "X"]:
    inclinacion = input("Inclinar hacia arriba(U) o hacia abajo(D)?: ")
    if inclinacion in ["d","D"]:
        img = cv2.copyMakeBorder(img, 40, 40, 0, 360, cv2.BORDER_CONSTANT, value = (0, 0, 0)) # Añadiendo un borde negro para q se visualice mejor el efecto shear
        rows, cols, dim = img.shape 
        # matriz de transformación para Shearing
        # shearing aplicado al eje y
        M = np.float32([[1, 0.5, 0],
            	        [0, 1, 0],
           	            [0, 0, 1]])
    if inclinacion in ["u","U"]:
        img = cv2.copyMakeBorder(img, 40, 40, 360, 0, cv2.BORDER_CONSTANT, value = (0, 0, 0)) # Añadiendo un borde negro para q se visualice mejor el efecto shear
        rows, cols, dim = img.shape 
        M = np.float32([[1, -0.5, 0],
            	        [0, 1, 0],
           	            [0, 0, 1]])
# aplicar una transformación de perspectiva a la imagen               
sheared_img = cv2.warpPerspective(img,M,(int(cols),int(rows)))
# deshabilitar el eje x e y
plt.axis('off')
# mostrar la imagen resultante
plt.imshow(sheared_img)
plt.show()
# guardar la imagen resultante en el disco
plt.imsave(path2, sheared_img)



'''
current_directory = Path(__file__).resolve().parent
# Load an image
image = cv2.imread(f"{current_directory}/imagenes/image.jpg")

# Define the region of interest (ROI)
x, y, w, h = 200, 30, 250, 250
roi = image[y:y+h, x:x+w]

# Define the shear transformation matrix
shear_matrix = np.float32([[1, 0.5, 0], [0, 1, 0]])

# Apply the shear transformation to the ROI
sheared_roi = cv2.warpAffine(roi, shear_matrix, (w, h))

# Replace the original ROI with the sheared ROI
image[y:y+h, x:x+w] = sheared_roi

# Display the image
cv2.imshow("Sheared Image", image)
cv2.waitKey(0)
'''
