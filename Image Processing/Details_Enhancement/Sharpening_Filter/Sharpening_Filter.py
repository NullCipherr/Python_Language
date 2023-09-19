import cv2
import numpy as np

# Load the image
image = cv2.imread('Image.jpg')

# Sharpening Filter
kernel_sharpening = np.array([[-1,-1,-1],
                              [-1, 9,-1],
                              [-1,-1,-1]])

# Apply the sharpening filter
sharpened_image = cv2.filter2D(image, -1, kernel_sharpening)

# Display the original image and the sharpened image
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)

# Wait for a key press and close the windows
cv2.waitKey()
cv2.destroyAllWindows()
