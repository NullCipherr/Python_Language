import cv2
import numpy as np

# Load the image
image = cv2.imread('Image.jpg')

# Edge Detection Filter
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale

# Define the edge detection kernel
kernel_edge_detection = np.array([[-1,-1,-1],
                                  [-1, 8,-1],
                                  [-1,-1,-1]])

# Apply the edge detection filter
edges_detected_image = cv2.filter2D(gray_image, -1, kernel_edge_detection)

# Display the original image and the edges detected image
cv2.imshow('Original Image', image)
cv2.imshow('Edges Detected Image', edges_detected_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
