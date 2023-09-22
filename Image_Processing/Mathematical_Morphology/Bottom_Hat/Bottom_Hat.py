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
input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

# Definir um kernel (elemento estruturante)
kernel = np.ones((5, 5), np.uint8)

# Realizar o fechamento
closing = cv2.morphologyEx(input_image, cv2.MORPH_CLOSE, kernel)

# Calcular o Bottom Hat (diferença entre o fechamento e a imagem original)
bottom_hat = cv2.subtract(closing, input_image)

# Caminhos de saída
closing_output_path = os.path.join(output_folder, 'Closing_Image.jpg')
bottom_hat_output_path = os.path.join(output_folder, 'Bottom_Hat_Image.jpg')

# Salvar as imagens resultantes
cv2.imwrite(closing_output_path, closing)
cv2.imwrite(bottom_hat_output_path, bottom_hat)

# Aguardar até que uma tecla seja pressionada e fechar janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
