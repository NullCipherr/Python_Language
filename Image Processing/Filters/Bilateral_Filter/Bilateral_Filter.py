import cv2

# Load the image
image = cv2.imread('Image.jpg')

# Apply the Bilateral Filter
bilateral_filtered_image = cv2.bilateralFilter(image, 9, 75, 75)

# Display the original image and the binary image
cv2.imshow('Original Image', image)
cv2.imshow('Bilateral Image', bilateral_filtered_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()