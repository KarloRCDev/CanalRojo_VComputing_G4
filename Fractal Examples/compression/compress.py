from skimage.io import imread
import matplotlib.pyplot as plt

from skimage.color import rgb2gray
from skimage.transform import resize
import numpy as np
from pathlib import Path

path = Path(__file__).parent.resolve()


# Read the image
image = imread(f'{path}/images/lenna.jpg')

# Resize the image
image_resized = resize(image, (400, 300))

# Convert to grayscale
image_grayscale = rgb2gray(image_resized)

# Compress the image using fractal compression
image_fractal = np.fft.fft2(image_grayscale)

# Save the compressed image
np.save(f'{path}/images/lenna_compressed.npy', image_fractal)

image_fractal = np.load(f'{path}/images/lenna_compressed.npy')

# Aplicar la transformada inversa de Fourier para descomprimir la imagen
image_reconstructed = np.fft.ifft2(image_fractal).real

# Mostrar la imagen reconstruida
plt.imshow(image_reconstructed, cmap='gray')
plt.show()
