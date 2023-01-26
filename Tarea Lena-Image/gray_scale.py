import cv2
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

current_directory = Path(__file__).resolve().parent
img = cv2.imread(f"{current_directory}/imagenes/Lenna.jpg")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(f"{current_directory}/imagenes/gray_image_Lenna.jpg", gray_image)
cv2.imshow("image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(gray_image.ravel(), 256, [0, 256], color="black")
plt.show()


alpha = 1.5
beta = 0
gamma = 0
contrast_image = cv2.addWeighted(gray_image, alpha, np.zeros(
    gray_image.shape, gray_image.dtype), 0, beta)
p1, p2 = np.percentile(gray_image, (50, 50))
gray_image = np.interp(gray_image, (p1, p2), (0, 255))
cv2.imshow("image", gray_image)
cv2.waitKey(0)

plt.hist(gray_image.ravel(), 256, [0, 256], color="black")
plt.show()
