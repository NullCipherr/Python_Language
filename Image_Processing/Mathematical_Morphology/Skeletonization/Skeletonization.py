import cv2
import numpy as np
import os

def skeletonize(image):
    size = np.size(image)
    skel = np.zeros(image.shape, np.uint8)

    ret, image = cv2.threshold(image, 127, 255, 0)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    done = False

    while not done:
        eroded = cv2.erode(image, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(image, temp)
        skel = cv2.bitwise_or(skel, temp)
        image = eroded.copy()

        zeros = size - cv2.countNonZero(image)
        if zeros == size:
            done = True

    return skel

# Pasta de entrada e saída
input_folder = 'Input'
output_folder = 'Output'

# Certifique-se de que a pasta de saída existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Carregar a imagem de entrada
input_image_path = os.path.join(input_folder, 'Image.jpg')

# Carregar a imagem de entrada
input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

# Aplicar a esqueletização
skeleton = skeletonize(input_image)

skeleton_output_path = os.path.join(output_folder, 'Skeleton.jpg')

# Salvar a imagem esqueletizada
cv2.imwrite(skeleton_output_path, skeleton)
