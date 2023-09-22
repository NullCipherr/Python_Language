import cv2
import numpy as np
import os

# Pasta de entrada e saída
input_folder = 'Input'
output_folder = 'Output'

# Certifique-se de que a pasta de saída existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Carregar a imagem binária
input_image_path = os.path.join(input_folder, 'Image.jpg')
image = cv2.imread(input_image_path, 0)  # Certifique-se de que a imagem é binária

# Realizar a rotulagem dos componentes conectados
ret, labels = cv2.connectedComponents(image)

# Retornar o número de componentes conectados (objetos)
num_objects = ret - 1  # O fundo é considerado um componente

# Salva a Imagem
output_folder_path = os.path.join(output_folder, 'CCL_Image.jpg')
cv2.imwrite(output_folder_path, np.uint8(labels / num_objects * 255))

cv2.waitKey(0)
cv2.destroyAllWindows()
