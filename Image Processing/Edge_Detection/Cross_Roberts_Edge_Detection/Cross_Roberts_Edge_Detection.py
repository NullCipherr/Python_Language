import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Initialize the result image with zeros
roberts_result = np.zeros_like(image, dtype=np.uint8)

# Define the Roberts Cross convolution kernels for the two directions
roberts_x = np.array([[1, 0],
                      [0, -1]])

roberts_y = np.array([[0, 1],
                      [-1, 0]])

# Loop through the image (excluding border pixels) to apply Roberts Cross
for i in range(1, image.shape[0] - 1):
    for j in range(1, image.shape[1] - 1):
        # Extract a 2x2 region from the image
        region = image[i-1:i+1, j-1:j+1]
        
        # Apply the Roberts Cross kernels
        gradient_x = np.sum(region * roberts_x)
        gradient_y = np.sum(region * roberts_y)
        
        # Calculate the gradient magnitude and set it in the result image
        gradient_magnitude = int(np.sqrt(gradient_x**2 + gradient_y**2))
        roberts_result[i, j] = gradient_magnitude

# Display the Roberts Cross edge detection result
cv2.imshow('Roberts Cross Edge Detection', roberts_result)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
