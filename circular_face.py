import cv2
from pathlib import Path
import numpy as np
# current_directory = Path(__file__).resolve().parent
# image = cv2.imread(f"{current_directory}/imagenes/image.jpg")
# mask = np.zeros(image.shape[:2], dtype=np.uint8)
# (x, y) = (image.shape[1]//2, image.shape[0]//2)
# radius = image.shape[1]//4
# cv2.circle(mask, (x, y), radius, (255, 255, 255), -1)
# output = cv2.bitwise_and(image, image, mask=mask)
# cv2.imshow("Output", output)
# cv2.waitKey(0)
# # import the necessary packages
# import cv2

# load the image and convert it to grayscale

current_directory = Path(__file__).resolve().parent
# Load the image
img = cv2.imread(f"{current_directory}/imagenes/per.jpg")
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the face detector
face_cascade = cv2.CascadeClassifier("C:\Python311\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

# Iterate over the faces
for (x, y, w, h) in faces:
    # Create a mask with a circular shape
    mask = np.zeros_like(img)
    mask = cv2.circle(mask, (x + w//2, y + h//2), (w + h)//4, (255, 255, 255), -1)
    # Apply the mask to the face
    img = cv2.addWeighted(img, 0.7, mask, 0.3, 0)

# Display the image
cv2.imshow("Face Masked", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

