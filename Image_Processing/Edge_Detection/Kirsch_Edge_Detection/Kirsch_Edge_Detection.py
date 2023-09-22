import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the Kirsch masks for the eight directions
kirsch_masks = [
    np.array([[-3, -3, 5],
              [-3, 0, 5],
              [-3, -3, 5]]),
    
    np.array([[-3, 5, 5],
              [-3, 0, 5],
              [-3, -3, -3]]),
    
    np.array([[5, 5, 5],
              [-3, 0, -3],
              [-3, -3, -3]]),
    
    np.array([[5, 5, -3],
              [5, 0, -3],
              [-3, -3, -3]]),
    
    np.array([[5, -3, -3],
              [5, 0, -3],
              [5, -3, -3]]),
    
    np.array([[-3, -3, -3],
              [5, 0, -3],
              [5, 5, -3]]),
    
    np.array([[-3, -3, -3],
              [-3, 0, -3],
              [5, 5, 5]]),
    
    np.array([[-3, -3, -3],
              [-3, 0, 5],
              [-3, 5, 5]])
]

# Initialize the result image with zeros
kirsch_result = np.zeros_like(image, dtype=np.uint8)

# Loop through the image (excluding border pixels) to apply Kirsch masks
for i in range(1, image.shape[0] - 1):
    for j in range(1, image.shape[1] - 1):
        region = image[i-1:i+2, j-1:j+2]
        responses = [np.sum(region * mask) for mask in kirsch_masks]
        max_response = max(responses)
        kirsch_result[i, j] = max_response

# Display the gradient image detected by the Kirsch operator
cv2.imshow('Kirsch Edge Detection', kirsch_result)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
