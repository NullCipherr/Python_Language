import cv2
import numpy as np

# Load the image
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Get the shape of the image
height, width = image.shape

# Create an empty binary image with the same dimensions
binary_image = np.zeros((height, width), dtype=np.uint8)

# Set the threshold value
threshold_value = 120

# Apply thresholding manually
for i in range(height):
    for j in range(width):
        if image[i, j] > threshold_value:
            binary_image[i, j] = 255

# Display the binary image
cv2.imshow('Binary Image', binary_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
