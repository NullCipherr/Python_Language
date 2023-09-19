import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Initialize the result images for x and y gradients with zeros
roberts_image_x = np.zeros_like(image, dtype=np.int32)
roberts_image_y = np.zeros_like(image, dtype=np.int32)

# Define the Roberts Cross convolution kernels for the two directions
roberts_kernel_x = np.array([[1, 0],
                             [0, -1]])

roberts_kernel_y = np.array([[0, 1],
                             [-1, 0]])

# Loop through the image (excluding border pixels) to apply Roberts Cross
for i in range(1, image.shape[0] - 1):
    for j in range(1, image.shape[1] - 1):
        # Extract a 2x2 region from the image
        region = image[i-1:i+1, j-1:j+1]
        
        # Apply the Roberts Cross kernels
        gradient_x = np.sum(region * roberts_kernel_x)
        gradient_y = np.sum(region * roberts_kernel_y)
        
        # Set the gradient values in the result images
        roberts_image_x[i, j] = gradient_x
        roberts_image_y[i, j] = gradient_y

# Calculate the gradient magnitude
roberts_gradient = np.sqrt(roberts_image_x**2 + roberts_image_y**2)

# Convert to an image type compatible with display
roberts_gradient_8bit = np.uint8(roberts_gradient)

# Display the gradient image detected by the Roberts operator
cv2.imshow('Roberts Edge Detection', roberts_gradient_8bit)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
