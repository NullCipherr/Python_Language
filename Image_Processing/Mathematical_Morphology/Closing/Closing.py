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

# Fechamento (dilatação seguida de erosão)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
closing_output_path = os.path.join(output_folder, 'closing.jpg')
cv2.imwrite(closing_output_path, closing)  # Salvar a imagem após o fechamento
