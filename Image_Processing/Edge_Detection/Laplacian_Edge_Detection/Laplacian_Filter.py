import cv2
import numpy as np

def laplacian_edge_detection(image, kernel_size):
    # Smooth the image using a Gaussian filter
    smoothed_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Define the Laplacian kernel
    laplacian_kernel = np.array([[0, 1, 0],
                                 [1, -4, 1],
                                 [0, 1, 0]])

    # Initialize a result image with zeros
    laplacian_result = np.zeros_like(image, dtype=np.uint8)

    # Loop through the image (excluding border pixels) to apply the Laplacian operator
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            region = smoothed_image[i-1:i+2, j-1:j+2]
            response = np.sum(region * laplacian_kernel)
            laplacian_result[i, j] = response

    # Convert to an image type compatible with display
    laplacian_result_8bit = np.uint8(np.absolute(laplacian_result))

    return laplacian_result_8bit

# Load the image in grayscale
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Set the kernel size for Gaussian smoothing
kernel_size = 5

# Apply Laplacian edge detection with configurable parameters
laplacian_result = laplacian_edge_detection(image, kernel_size)

# Display the original image
cv2.imshow('Original Image', image)

# Display the detected edge image using Laplacian operator
cv2.imshow('Laplacian Edge Detection', laplacian_result)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
