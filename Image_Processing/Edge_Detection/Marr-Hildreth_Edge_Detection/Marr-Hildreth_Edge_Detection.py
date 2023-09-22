import cv2

# Load the image in grayscale
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the kernel size for Gaussian blur (adjustable)
gaussian_kernel_size = (5, 5)

# Apply Gaussian blur for noise reduction
smoothed_image = cv2.GaussianBlur(image, gaussian_kernel_size, 0)

# Define the kernel size for Laplacian (1, 3, 5, 7, ...)
laplacian_kernel_size = 1

# Apply Laplacian operator to the smoothed image
laplacian = cv2.Laplacian(smoothed_image, cv2.CV_64F, ksize=laplacian_kernel_size)

# Convert the resulting image to values between 0 and 255
laplacian_abs = cv2.convertScaleAbs(laplacian)

# Display the Laplacian of Gaussian image
cv2.imshow('Marr-Hildreth Edge Detection', laplacian_abs)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
