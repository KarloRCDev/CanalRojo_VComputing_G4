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
