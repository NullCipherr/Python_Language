import cv2
import numpy as np

# Load the image
image = cv2.imread('Image.jpg')

# Define a custom kernel for weighted average filtering
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]], dtype=np.float32) / 16

# Apply the weighted average filter
weighted_average_image = cv2.filter2D(image, -1, kernel)

# Display the original image and the image with the weighted average filter applied
cv2.imshow('Original Image', image)
cv2.imshow('Weighted Average Image', weighted_average_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()