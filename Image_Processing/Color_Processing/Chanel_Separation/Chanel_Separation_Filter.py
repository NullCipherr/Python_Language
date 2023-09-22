import cv2

# Load the image
image = cv2.imread('Image.jpg')

# Invert the RGB channels
inverted_image = cv2.merge([image[:, :, 2], image[:, :, 1], image[:, :, 0]])

# Display the concatenated image in the same window
cv2.imshow('Inverted Color Channels', inverted_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()