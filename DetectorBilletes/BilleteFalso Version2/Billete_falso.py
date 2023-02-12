import cv2
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
current_directory = Path(__file__).resolve().parent
A = cv2.imread(f'{current_directory}/image/billete_100_Real.jpg')
P = cv2.imread(f'{current_directory}/image/billete_falso.jpg')

# Convert images to grayscale
a = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)
p = cv2.cvtColor(P, cv2.COLOR_BGR2GRAY)

# Crop the regions of interest
a2tr = a[330:1200, 1016:1927]
b2tr = p[170:1040, 716:1627]

a2_str = a[5:1100, 2080:2151]
p2_str = p[5:1100, 1666:1729]

# Convert images to HSV
hsvImageReal = cv2.cvtColor(A, cv2.COLOR_BGR2HSV)
hsvImageFake = cv2.cvtColor(P, cv2.COLOR_BGR2HSV)

# Display the images

plt.imshow(hsvImageReal)
cv2.imwrite(f"{current_directory}/image/billete_real_detected.jpg", hsvImageReal)
plt.show()

plt.imshow(hsvImageFake)
cv2.imwrite(f"{current_directory}/image/billete_false_detected.jpg", hsvImageFake)
plt.show()
