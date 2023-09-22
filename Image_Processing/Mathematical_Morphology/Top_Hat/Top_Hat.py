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

# Realizar a abertura
opening = cv2.morphologyEx(input_image, cv2.MORPH_OPEN, kernel)

# Calcular o Top Hat (diferença entre a imagem original e a abertura)
top_hat = cv2.subtract(input_image, opening)


# Caminhos de saída
opening_output_path = os.path.join(output_folder, 'Opening_Image.jpg')
top_hat_output_path = os.path.join(output_folder, 'Top_Hat_Image.jpg')

# Salvar as imagens resultantes
cv2.imwrite(opening_output_path, opening)
cv2.imwrite(top_hat_output_path, top_hat)

# Aguardar até que uma tecla seja pressionada e fechar janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
