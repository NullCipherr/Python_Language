import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the Prewitt convolution kernels for the x and y directions
prewitt_kernel_x = np.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]])

prewitt_kernel_y = np.array([[-1, -1, -1],
                             [0, 0, 0],
                             [1, 1, 1]])

# Apply convolution manually using the cv2.filter2D function
prewitt_image_x = cv2.filter2D(image, -1, prewitt_kernel_x)
prewitt_image_y = cv2.filter2D(image, -1, prewitt_kernel_y)

# Combine the resulting images to obtain the total gradient
prewitt_gradient = np.sqrt(prewitt_image_x**1 + prewitt_image_y**1)

# Convert to an image type compatible with display
prewitt_gradient_8bit = np.uint8(prewitt_gradient)

# Display the gradient image detected by the Prewitt operator
cv2.imshow('Prewitt Edge Detection', prewitt_gradient_8bit)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
