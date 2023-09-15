import cv2

# Load the image
image = cv2.imread('Image.jpg')

# Median Filter for noise removal
median_filtered_image = cv2.medianBlur(image, 5)

# Display the original image and the image with the Median filter applied
cv2.imshow('Original Image', image)
cv2.imshow('Median Filter', median_filtered_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()