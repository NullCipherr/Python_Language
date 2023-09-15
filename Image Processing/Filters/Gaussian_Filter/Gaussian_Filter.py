import cv2

# Load the image
image = cv2.imread('Image.jpg')

# Gaussian Filter (Smoothing/Gaussian Blur)
kernel_size = (5, 5)  # Kernel size (odd number)
sigma = 1.5  # Sigma parameter for the Gaussian filter

# Apply the Gaussian filter
gaussian_blur_image = cv2.GaussianBlur(image, kernel_size, sigma)

# Display the original image and the image with the Gaussian filter applied
cv2.imshow('Original Image', image)
cv2.imshow('Gaussian Filter', gaussian_blur_image)

# Wait for a key press and close the windows
cv2.waitKey()
cv2.destroyAllWindows()

