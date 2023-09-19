import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the parameters for the Frangi Vesselness filter
sigma = 1.0
scale_range = (1, 10)  # Range of scales to apply the filter
scale_step = 1  # Step between scales
beta = 3  # Beta parameter used in the calculation of the Frangi Vesselness filter
c = 100  # C parameter used in the calculation of the Frangi Vesselness filter

# Initialize an output image with zeros
vesselness = np.zeros_like(image, dtype=np.float32)

# Calculate the Frangi Vesselness filter for various scales
for scale in range(scale_range[0], scale_range[1], scale_step):
    # Calculate the Hessian matrix
    sigma_x = sigma * scale
    sigma_y = sigma * scale
    ksize = int(6 * max(sigma_x, sigma_y)) 
    ksize = min(ksize, 10)
    ksize = ksize | 1  # Odd-sized kernel (required for GaussianBlur function)

    # Apply derivative operators (Sobel) and Gaussian blur to calculate the components of the Hessian matrix
    Ixx = cv2.GaussianBlur(cv2.Sobel(image, cv2.CV_64F, 2, 0, ksize=ksize), (0, 0), sigma_x)
    Iyy = cv2.GaussianBlur(cv2.Sobel(image, cv2.CV_64F, 0, 2, ksize=ksize), (0, 0), sigma_y)
    Ixy = cv2.GaussianBlur(cv2.Sobel(image, cv2.CV_64F, 1, 1, ksize=ksize), (0, 0), sigma_x)

    # Calculate the eigenvalues of the Hessian matrix
    lambda1 = (Ixx + Iyy) / 2 + np.sqrt(4 * Ixy ** 2 + (Ixx - Iyy) ** 2) / 2
    lambda2 = (Ixx + Iyy) / 2 - np.sqrt(4 * Ixy ** 2 + (Ixx - Iyy) ** 2) / 2

    # Calculate the Frangi Vesselness filter
    Rb = lambda1 / (lambda2 + 1e-5)  # Avoid division by zero
    S2 = lambda1 ** 2 + lambda2 ** 2

    vesselness_scale = np.exp(-Rb ** 2 / (2 * beta ** 2)) * (1 - np.exp(-S2 / (2 * c ** 2)))

    # Update the output image using the maximum value from the filter at each scale
    vesselness = np.maximum(vesselness, vesselness_scale)

# Enhance contrast in the output image
vesselness = (vesselness - np.min(vesselness)) / (np.max(vesselness) - np.min(vesselness))

# Convert to an image type suitable for display
vesselness = np.uint8(vesselness * 255)

# Display the enhanced image
cv2.imshow('Frangi Vesselness Enhancement', vesselness)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
