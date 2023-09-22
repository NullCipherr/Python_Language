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

# Definir um kernel (elemento estruturante)
kernel = np.ones((3, 3), np.uint8)

# Gradiente Externo (diferença entre dilatação e imagem original)
external_gradient = cv2.dilate(image, kernel, iterations=1) - image

# Gradiente Interno (diferença entre imagem original e erosão)
internal_gradient = image - cv2.erode(image, kernel, iterations=1)

# Salva os gradientes externo e interno
output_image_path = os.path.join(output_folder, 'Extern_Image.jpg')
cv2.imwrite(output_image_path, external_gradient)
output_image_path = os.path.join(output_folder, 'Internal_Image.jpg')
cv2.imwrite(output_image_path, internal_gradient)

#
cv2.waitKey(0)
cv2.destroyAllWindows()