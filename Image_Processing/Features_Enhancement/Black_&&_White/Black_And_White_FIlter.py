import cv2

# Load the image
image = cv2.imread('Image.jpg')

# Get the dimensions of the image
height, width, _ = image.shape

# Create an empty black and white image
bw_image = image.copy()

# Convert the image to black and white manually
for y in range(height):
    for x in range(width):
        # Get the pixel value at the current position
        pixel = image[y, x]

        # Calculate the grayscale value using the average of RGB channels
        gray_value = sum(pixel) // 3

        # Set the pixel in the black and white image to the grayscale value
        bw_image[y, x] = (gray_value, gray_value, gray_value)

# Display the original and black & white images
cv2.imshow('Original Image', image)
cv2.imshow('Black & White Image', bw_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
