import cv2
import numpy as np

# Load the image
image = cv2.imread('Image.jpg')

# Laplacian Filter (Edge Enhancement/Laplacian)
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Convert the Laplacian image back to uint8
laplacian = np.uint8(np.absolute(laplacian))

# Display the original image and the image with the Laplacian filter applied
cv2.imshow('Original Image', image)
cv2.imshow('Laplacian Filter', laplacian)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()