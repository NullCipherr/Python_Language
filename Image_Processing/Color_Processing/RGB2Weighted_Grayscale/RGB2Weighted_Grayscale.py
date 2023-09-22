import cv2
import numpy as np

# Load the image
image = cv2.imread('Image.jpg')

# Get the image dimensions
height, width, _ = image.shape

# Create an empty matrix for the weighted grayscale image
weighted_grayscale_image = np.zeros((height, width, 1), dtype=np.uint8)

# Define the weights for each channel (R, G, and B)
weights = [0.2989, 0.5870, 0.1140]

# Iterate through the pixels of the image and calculate the weighted grayscale value
for i in range(height):
    for j in range(width):
        pixel = image[i, j]
        grayscale_value = int(np.sum(pixel * weights))
        weighted_grayscale_image[i, j] = grayscale_value

# Save the weighted grayscale image
cv2.imwrite('Weighted_Grayscale_Image.jpg', weighted_grayscale_image)
