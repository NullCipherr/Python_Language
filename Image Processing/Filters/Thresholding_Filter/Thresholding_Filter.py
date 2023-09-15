import cv2

# Load the image in grayscale
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Set the threshold value
threshold_value = 128

# Apply thresholding
_, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Display the original image and the binary image
cv2.imshow('Original Image', image)
cv2.imshow('Binary Image', binary_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()