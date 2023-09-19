import cv2
import numpy as np

# Load the image
image = cv2.imread('Image.jpg')

# Get the shape of the image
height, width, channels = image.shape

# Create an empty image with the same dimensions
negative_image = np.zeros((height, width, channels), dtype=np.uint8)

# Invert the colors manually
for i in range(height):
    for j in range(width):
        for c in range(channels):
            negative_image[i, j, c] = 255 - image[i, j, c]

# Display the negative image
cv2.imshow('Inverse Image', negative_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
