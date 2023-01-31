import cv2
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

current_directory = Path(__file__).resolve().parent

gray_scale_image = cv2.imread(
    f"{current_directory}/imagenes/gray_image_Lenna.jpg")


# Mostrando la imagen en formato binario
binary_image = cv2.imread(
    f"{current_directory}/imagenes/binary_image_Lenna.jpg")
cv2.imshow("Binary Image", binary_image)
cv2.waitKey(0)

# Mostrando el histograma de la imagen en formato binario
plt.hist(binary_image.ravel(), 256, [0, 256], color="black")
plt.show()

# Mostrando la imagen de la escala de grises con contraste AUMENTADO
alpha = 1.5
beta = 0
gamma = 0
contrast_image = gray_scale_image.copy()
cv2.addWeighted(contrast_image, alpha, np.zeros(
    contrast_image.shape, contrast_image.dtype), 0, beta)
p1, p2 = np.percentile(contrast_image, (50, 50))
contrast_image = np.interp(contrast_image, (p1, p2), (0, 255))
cv2.imwrite(
    f"{current_directory}/imagenes/contrast_image_Lenna.jpg", contrast_image)
cv2.imshow("image", contrast_image)
cv2.waitKey(0)

# Mostrando el histograma de la imagen de la escala de grises con contraste AUMENTADO
plt.hist(contrast_image.ravel(), 256, [0, 256], color="black")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
