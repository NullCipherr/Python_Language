import cv2
import numpy as np

# Load the image
image = cv2.imread('Image.jpg')

# Adjustment parameters
kernel_size = (25, 25)  # Smoothing kernel size
invert_intensity = 200  # Intensity for inverting colors (higher values result in a lighter effect)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a smoothing operation to reduce noise and improve the result
smoothed_image = cv2.GaussianBlur(gray_image, kernel_size, sigmaX=0, sigmaY=0)

# Apply edge detection using the Laplacian filter
edge_image = cv2.Laplacian(smoothed_image, cv2.CV_8U, ksize=5)

# Invert the colors of the edge image to create a pencil sketch effect
sketch_image = 255 - edge_image

# Create a blank image with the same size as the original
sketch_drawing = np.zeros_like(image)

# Copy the pixels from the original image to the blank image where the sketch is darker
sketch_drawing[sketch_image > invert_intensity] = image[sketch_image > invert_intensity]

# Concatenate the input image and the sketch image side by side
comparison = np.hstack((image, sketch_drawing))

# Display the comparison
cv2.imshow('Image Comparasion', comparison)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()