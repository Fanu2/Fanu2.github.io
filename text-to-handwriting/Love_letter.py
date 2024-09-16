from PIL import Image

# Paths to the images
image1_path = '/home/jasvir/Music/letter/1.png'
image2_path = '/home/jasvir/Music/letter/2.png'

# Open the two images
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Get the size of the images (assuming both images have the same height)
width1, height1 = image1.size
width2, height2 = image2.size

# Create a new image with a width that's the sum of both widths (side-by-side)
total_width = width1 + width2
max_height = max(height1, height2)

# Create a blank canvas with the combined width and max height
card_image = Image.new('RGB', (total_width, max_height), (255, 255, 255))  # White background

# Paste the images onto the canvas
card_image.paste(image1, (0, 0))  # Paste the first image at the left (0,0)
card_image.paste(image2, (width1, 0))  # Paste the second image to the right of the first

# Save the combined image as a card
output_path = '/home/jasvir/Music/letter/card.png'
card_image.save(output_path)

print(f'Card image saved at {output_path}')
