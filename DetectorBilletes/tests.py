import os
from pathlib import Path

current_directory = Path(__file__).resolve().parent
path = f"{current_directory}\\imagenes\\"

print(path)

for filename in os.listdir(path):
    if filename.endswith('.jpg'):
        file_path = os.path.join(path, filename)
        print(file_path)
