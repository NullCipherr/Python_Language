import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur for noise reduction (you can adjust the kernel size)
smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Laplacian operator to the smoothed image
laplacian = cv2.Laplacian(smoothed_image, cv2.CV_64F)

# Initialize an empty image to store zero-crossings
zero_crossings = np.zeros_like(laplacian, dtype=np.uint8)

# Define a threshold for zero-crossings (you can adjust this threshold)
threshold = 10

# Loop through the image to find zero-crossings
for i in range(1, laplacian.shape[0] - 1):
    for j in range(1, laplacian.shape[1] - 1):
        neighbors = [
            laplacian[i - 1, j - 1], laplacian[i - 1, j], laplacian[i - 1, j + 1],
            laplacian[i, j - 1], laplacian[i, j], laplacian[i, j + 1],
            laplacian[i + 1, j - 1], laplacian[i + 1, j], laplacian[i + 1, j + 1]
        ]
        
        # Check if there are positive and negative values among neighbors
        positive_count = sum(1 for neighbor in neighbors if neighbor > threshold)
        negative_count = sum(1 for neighbor in neighbors if neighbor < -threshold)
        
        # If there are both positive and negative values, it's a zero-crossing
        if positive_count > 0 and negative_count > 0:
            zero_crossings[i, j] = 255

# Display the zero-crossing image
cv2.imshow('Zero Crossing Edge Detection', zero_crossings)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
