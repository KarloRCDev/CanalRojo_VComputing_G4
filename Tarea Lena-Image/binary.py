import cv2
from pathlib import Path
# Load the image
current_directory = Path(__file__).resolve().parent
img = cv2.imread(f"{current_directory}/imagenes/Lenna.jpg",0)

# Create the mask (2^1 = 2)
ret, binary_img = cv2.threshold(img, 128, 128, cv2.THRESH_BINARY)

# set the pixels less than 128 to 64
binary_img[binary_img == 0] = 2

cv2.imshow("Binary Image", binary_img)
cv2.imwrite(f"{current_directory}/imagenes/binary_image_Lenna.jpg",binary_img)
# Wait for a key to be pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()