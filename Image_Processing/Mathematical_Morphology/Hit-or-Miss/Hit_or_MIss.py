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

# Transformada Hit-or-Miss
kernel_hit_miss = np.array([[-1, -1, -1],
                            [-1,  1, -1],
                            [-1, -1, -1]], dtype=np.int8)

hit_or_miss = cv2.morphologyEx(image, cv2.MORPH_HITMISS, kernel_hit_miss)
hit_or_miss_output_path = os.path.join(output_folder, 'hit_or_miss.jpg')
cv2.imwrite(hit_or_miss_output_path, hit_or_miss)  # Salvar a imagem da transformada Hit-or-Miss
