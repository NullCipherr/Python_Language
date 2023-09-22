import cv2
import numpy as np
import os

# Pasta de entrada e saída
input_folder = 'Input'
output_folder = 'Output'

# Certifique-se de que a pasta de saída existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Carregar a imagem de entrada
input_image_path = os.path.join(input_folder, 'Image.jpg')
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)  # Converter para tons de cinza

# Definir um kernel (elemento estruturante)
kernel = np.ones((5, 5), np.uint8)

# Abertura (erosão seguida de dilatação)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
opening_output_path = os.path.join(output_folder, 'opening.jpg')
cv2.imwrite(opening_output_path, opening)  # Salvar a imagem após a abertura
