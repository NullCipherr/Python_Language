import cv2
import numpy as np

# Load the image
image = cv2.imread('Image.jpg')

# Create a variable to control sepia intensity (0 to 1)
sepia_intensity = 0.4

# Apply sepia filter with adjustable intensity
sepia_filter = np.array([[0.393, 0.769, 0.189],
                         [0.349, 0.686, 0.168],
                         [0.272, 0.534, 0.131]])

sepia_image = cv2.transform(image, sepia_filter)
sepia_image = sepia_intensity * sepia_image + (1 - sepia_intensity) * image
sepia_image = np.clip(sepia_image, 0, 255).astype(np.uint8)

# Concatenate the two images horizontally
concatenated_image = cv2.hconcat([image, sepia_image])

# Create a custom window
cv2.namedWindow('Original Image and Sepia Effect', cv2.WINDOW_NORMAL)

# Resize the window
cv2.resizeWindow('Original Image and Sepia Effect', 800, 800)

# Display the concatenated image in the same window
cv2.imshow('Original Image and Sepia Effect', concatenated_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()