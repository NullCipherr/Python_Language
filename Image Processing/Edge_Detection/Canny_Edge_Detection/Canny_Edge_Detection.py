import cv2
import numpy as np

# Threshold values
threshold1_Value = 100
threshold2_Value = 150

# Load the image in grayscale
image = cv2.imread('Image.jpg', cv2.IMREAD_GRAYSCALE)

# Gaussian Smoothing
smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)

# Compute gradients using Sobel
gradient_x = cv2.Sobel(smoothed_image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(smoothed_image, cv2.CV_64F, 0, 1, ksize=3)

# Compute gradient magnitude
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

# Compute gradient direction
gradient_direction = np.arctan2(gradient_y, gradient_x)

# Non-Maximum Suppression
def non_max_suppression(magnitude, direction):
    height, width = magnitude.shape
    suppressed = np.zeros_like(magnitude)
    
    # Convert radians to degrees
    angle_degrees = direction * (180.0 / np.pi)
    angle_degrees[angle_degrees < 0] += 180
    
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # Determine the gradient direction
            angle = angle_degrees[i, j]
            
            # Comparison with neighbors in the gradient direction
            if (0 <= angle < 22.5) or (157.5 <= angle <= 180):
                neighbors = [magnitude[i, j-1], magnitude[i, j+1]]
            elif (22.5 <= angle < 67.5):
                neighbors = [magnitude[i-1, j-1], magnitude[i+1, j+1]]
            elif (67.5 <= angle < 112.5):
                neighbors = [magnitude[i-1, j], magnitude[i+1, j]]
            else:
                neighbors = [magnitude[i-1, j+1], magnitude[i+1, j-1]]
            
            # If the current value is the maximum among the neighbors, keep it; otherwise, set it to 0
            if magnitude[i, j] >= max(neighbors):
                suppressed[i, j] = magnitude[i, j]
    
    return suppressed

# Step 7: Edge Tracking by Hysteresis
def edge_tracking_by_hysteresis(magnitude, threshold1, threshold2):
    height, width = magnitude.shape
    strong_edge = 255
    weak_edge = 50
    
    # Classify pixels as strong edge, weak edge, or non-edge
    strong_edges = np.zeros_like(magnitude)
    weak_edges = np.zeros_like(magnitude)
    
    strong_edges[magnitude >= threshold2] = strong_edge
    weak_edges[(magnitude >= threshold1) & (magnitude < threshold2)] = weak_edge
    
    # Edge tracking by hysteresis
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if weak_edges[i, j] == weak_edge:
                if (strong_edges[i-1:i+2, j-1:j+2] == strong_edge).any():
                    strong_edges[i, j] = strong_edge
                else:
                    weak_edges[i, j] = 0
    
    return strong_edges

# Call the functions for non-maximum suppression and edge tracking by hysteresis
canny_edges = edge_tracking_by_hysteresis(gradient_magnitude, threshold1=threshold1_Value, threshold2=threshold2_Value)

# Display the original image
cv2.imshow('Original Image', image)

# Display the image with detected edges
cv2.imshow('Canny Image', canny_edges)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
