import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the Sobel convolution kernels for the x and y directions
sobel_kernel_x = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])

sobel_kernel_y = np.array([[-1, -2, -1],
                           [0, 0, 0],
                           [1, 2, 1]])

# Apply convolution manually using the cv2.filter2D function
sobel_image_x = cv2.filter2D(image, -1, sobel_kernel_x)
sobel_image_y = cv2.filter2D(image, -1, sobel_kernel_y)

# Combine the resulting images to obtain the total gradient
sobel_gradient = np.sqrt(sobel_image_x**2 + sobel_image_y**2)

# Convert to an image type compatible with display
sobel_gradient_8bit = np.uint8(sobel_gradient)

# Display the gradient image detected by the Sobel operator
cv2.imshow('Sobel Edge Detection - X', sobel_image_x)
cv2.imshow('Sobel Edge Detection - Y', sobel_image_y)
cv2.imshow('Sobel Edge Detection - Result', sobel_gradient_8bit)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
