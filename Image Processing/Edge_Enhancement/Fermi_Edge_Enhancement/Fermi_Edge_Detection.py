import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Define Fermi filter parameters (adjust as needed)
sigma = 75.0  # Smoothing parameter
alpha = 0.4   # Contrast parameter

# Apply Fermi function manually
fermi_image = 1 / (1 + np.exp(-(image - 128) / (sigma + 1e-5)))  # Fermi function

# Adjust contrast
fermi_image = alpha * (fermi_image - 0.5) + 0.5

# Convert to a display-compatible image type
fermi_image = np.uint8(255 * fermi_image)

# Display the enhanced image
cv2.imshow('Fermi Edge Enhancement', fermi_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
