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

# Erosão
erosion = cv2.erode(image, kernel, iterations=1)
erosion_output_path = os.path.join(output_folder, 'erosion.jpg')
cv2.imwrite(erosion_output_path, erosion)  # Salvar a imagem erodida
