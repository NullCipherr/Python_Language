import cv2

# Load the image
image = cv2.imread('Image.jpg')

# Set the kernel size for the mean filter
kernel_size = 5

# Apply the mean filter
smoothed_image = cv2.blur(image, (kernel_size, kernel_size))

# Display the original image and the image with the filter applied
cv2.imshow('Original Image', image)
cv2.imshow('Image with Filter', smoothed_image)

# Wait for a key press and close the windows
cv2.waitKey()
cv2.destroyAllWindows()