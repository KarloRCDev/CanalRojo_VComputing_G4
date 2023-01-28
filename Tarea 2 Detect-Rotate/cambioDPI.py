from PIL import Image
from pathlib import Path

current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/imagenes/image.jpg"
path2 = f"{current_directory}/imagenesDPI/image_dpi.jpg"
# Abrir la imagen
im = Image.open(path)

# Establecer la resolución DPI (en puntos por pulgada)
im.info["dpi"] = (72,72)

# Guardar la imagen con la nueva resolución DPI
im.save(path2, "JPEG", dpi=im.info["dpi"])