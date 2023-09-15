import cv2

# Carregue a imagem
image = cv2.imread('Image.jpg')

# Filtro de Sobel para detecção de bordas em direção X
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

# Filtro de Sobel para detecção de bordas em direção Y
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

# Exibir a imagem original, a imagem com o filtro Sobel X, a imagem com o filtro Sobel Y
cv2.imshow('Original Image', image)
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)

# Aguarde até que uma tecla seja pressionada e feche as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()