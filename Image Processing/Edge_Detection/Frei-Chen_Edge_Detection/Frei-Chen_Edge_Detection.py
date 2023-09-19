import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur for noise reduction (you can adjust the kernel size)
smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)

# Define the masks for the three Frei-Chen filter banks (R1, R2, and R3)
# You can adjust the mask values as needed
frei_chen_r1 = np.array([[1, -2, 1],
                         [-2, 4, -2],
                         [1, -2, 1]])

frei_chen_r2 = np.array([[-1, 0, 1],
                         [-1, 0, 1],
                         [-1, 0, 1]])

frei_chen_r3 = np.array([[-1, -1, 2],
                         [-1, 2, -1],
                         [2, -1, -1]])

# Apply convolution using each Frei-Chen filter
frei_chen_result_r1 = cv2.filter2D(smoothed_image, -1, frei_chen_r1)
frei_chen_result_r2 = cv2.filter2D(smoothed_image, -1, frei_chen_r2)
frei_chen_result_r3 = cv2.filter2D(smoothed_image, -1, frei_chen_r3)

# Combine the results from the three filter banks to obtain the final result
frei_chen_gradient = np.sqrt(frei_chen_result_r1**2 + frei_chen_result_r2**2 + frei_chen_result_r3**2)

# Convert to an image type compatible with display
frei_chen_gradient_8bit = np.uint8(frei_chen_gradient)

# Display the gradient image detected by the Frei-Chen operator
cv2.imshow('Frei-Chen Edge Detection', frei_chen_gradient_8bit)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
