from PIL import Image, ImageDraw, ImageFont
import pyperclip

# Get text from clipboard
text = pyperclip.paste()

# Create an image with white background
image = Image.new('RGB', (800, 600), color = 'white')
draw = ImageDraw.Draw(image)

# Define a font and size
try:
    font = ImageFont.truetype("arial.ttf", 40)
except IOError:
    font = ImageFont.load_default()

# Draw the text on the image
draw.text((10, 10), text, font=font, fill='black')

# Save the image
image.save('clipboard_text.png')
print('Text saved as image successfully.')
