import numpy as np
from PIL import Image
import os

# Load the image
image = Image.open('Image.jpg')

# Convert the image to a NumPy array
image_array = np.array(image)

# Normalize values from 0-255 to 0-1
image_array = image_array / 255.0

# Define conversion functions for L*a*b*
def rgb_to_lab(rgb):
    r, g, b = rgb
    r, g, b = r / 0.95047, g / 1.00000, b / 1.08883
    r, g, b = [((c + 0.055) / 1.055) ** 2.4 if (c + 0.055) / 1.055 > 0.04045 else c / 12.92 for c in (r, g, b)]
    r, g, b = [c * 100.0 for c in (r, g, b)]
    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041
    x, y, z = [c / 95.047 if c > 0.008856 else (c * 903.3 + 16.0) / 116.0 for c in (x, y, z)]
    l = max(0.0, min(100.0, 116.0 * y - 16.0))
    a = max(-86.185, min(98.254, (x - y) * 500.0))
    b = max(-107.863, min(94.482, (y - z) * 200.0))
    return l, a, b

# Apply the conversion to each pixel of the image
image_lab = np.apply_along_axis(rgb_to_lab, 2, image_array)

# Separate the L*, a*, and b* channels
luminance, a, b = image_lab[:,:,0], image_lab[:,:,1], image_lab[:,:,2]

# Create the "output" directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

# Save the separated channels
luminance = (luminance * 255.0).astype(np.uint8)
a = (a + 128.0).astype(np.uint8)
b = (b + 128.0).astype(np.uint8)

Image.fromarray(luminance).save('output/image_luminance_lab.jpg')
Image.fromarray(a).save('output/image_a_lab.jpg')
Image.fromarray(b).save('output/image_b_lab.jpg')