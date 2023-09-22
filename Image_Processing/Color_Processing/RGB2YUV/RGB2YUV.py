import numpy as np
from PIL import Image
import os

# Load the image
image = Image.open('Image.jpg')

# Convert the image to a NumPy array
image_array = np.array(image)

# Normalize values from 0-255 to 0-1
image_array = image_array / 255.0

# Function to convert RGB to YUV
def rgb_to_yuv(rgb):
    r, g, b = rgb
    y = 0.299 * r + 0.587 * g + 0.114 * b
    u = -0.14713 * r - 0.28886 * g + 0.436 * b
    v = 0.615 * r - 0.51498 * g - 0.10001 * b
    return y, u, v

# Apply the conversion to each pixel of the image
image_yuv = np.apply_along_axis(rgb_to_yuv, 2, image_array)

# Separate the YUV channels
luminance = image_yuv[:,:,0]
chrominance_u = image_yuv[:,:,1]
chrominance_v = image_yuv[:,:,2]

# Normalize the Y, U, and V channels back to the range of 0-255
luminance = (luminance * 255.0).astype(np.uint8)
chrominance_u = ((chrominance_u + 0.5) * 255.0).astype(np.uint8)
chrominance_v = ((chrominance_v + 0.5) * 255.0).astype(np.uint8)

# Create the "output" directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

# Save the separated channels
Image.fromarray(luminance).save('output/Image_Luminance_YUV.jpg')
Image.fromarray(chrominance_u).save('output/Image_Chrominance_U.jpg')
Image.fromarray(chrominance_v).save('output/Image_Chrominance_V.jpg')