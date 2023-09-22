import numpy as np
from PIL import Image
import os

# Load the image
image = Image.open('Image.jpg')

# Convert the image to a NumPy array
image_array = np.array(image)

# Function to convert RGB to LCH
def rgb_to_lch(rgb):
    r, g, b = rgb
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    max_value = max(r, g, b)
    min_value = min(r, g, b)
    luminance = (max_value + min_value) / 2.0

    if max_value == min_value:
        chroma = 0.0
        hue = 0.0  # Default to 0 for achromatic colors
    else:
        delta = max_value - min_value
        chroma = delta
        if max_value == r:
            hue = 60.0 * (((g - b) / delta) % 6)
        elif max_value == g:
            hue = 60.0 * (((b - r) / delta) + 2)
        else:
            hue = 60.0 * (((r - g) / delta) + 4)

    if hue < 0:
        hue += 360.0  # Ensure hue is in the range [0, 360)

    return luminance * 100, chroma * 100, hue

# Apply the conversion to each pixel of the image
image_lch = np.apply_along_axis(rgb_to_lch, 2, image_array)

# Separate the L, C, and H channels
luminance = image_lch[:,:,0]
chroma = image_lch[:,:,1]
hue = image_lch[:,:,2]

# Create the "output" directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

# Save the separated channels
luminance = luminance.astype(np.uint8)
chroma = chroma.astype(np.uint8)
hue = hue.astype(np.uint8)

Image.fromarray(luminance).save('output/Image_Luminance_LCH.jpg')
Image.fromarray(chroma).save('output/Image_Chroma_LCH.jpg')
Image.fromarray(hue).save('output/Image_HUE_LCH.jpg')
