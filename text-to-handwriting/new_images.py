from PIL import Image
import numpy as np

# Create a 256x256 RGB image
width, height = 256, 256
image = Image.new("RGB", (width, height))

# Load the pixel data into a numpy array for easy manipulation
pixels = np.array(image)

# Iterate over each pixel and set red and green values
for y in range(height):
    for x in range(width):
        pixels[y, x] = (x, y, 0)  # Red is x value, Green is y value, Blue is 0

# Convert the numpy array back to an image
image = Image.fromarray(pixels)

# Save the image to a PNG file
image.save("/home/jasvir/Music/jodha6/image.png")
