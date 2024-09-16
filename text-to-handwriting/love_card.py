from PIL import Image, ImageDraw, ImageFont

# Paths to the images
image1_path = '/home/jasvir/Music/Card/1.png'
image2_path = '/home/jasvir/Music/Card/2.png'

# Path to save the final card
output_path = '/home/jasvir/Music/Card/love_card.png'

# Load the images
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Resize images to fit inside the card (you can adjust these values)
image1 = image1.resize((300, 400))  # Width, Height
image2 = image2.resize((300, 400))

# Create a blank card background
card_width = image1.width + image2.width + 100  # Space for both images and margin
card_height = max(image1.height, image2.height) + 200  # Space for images and top/bottom margin
card = Image.new('RGB', (card_width, card_height), (255, 255, 255))  # White background

# Create a drawing object
draw = ImageDraw.Draw(card)

# Add decorations (heart symbols) around the card
heart_symbol = "♥"
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Use any font you prefer
font = ImageFont.truetype(font_path, 50)

# Draw hearts at the top and bottom of the card
draw.text((card_width // 2 - 25, 50), heart_symbol, font=font, fill="red")
draw.text((card_width // 2 - 25, card_height - 100), heart_symbol, font=font, fill="red")

# Paste the two images facing each other
card.paste(image1, (50, 100))  # Image1 on the left
card.paste(image2, (image1.width + 100, 100))  # Image2 on the right

# Add a message in the middle of the card (optional)
message = "Together Forever"
message_font = ImageFont.truetype(font_path, 40)
text_width, text_height = draw.textsize(message, font=message_font)
draw.text(((card_width - text_width) // 2, (card_height - text_height) // 2), message, font=message_font, fill="black")

# Save the card
card.save(output_path)

print(f"Love card saved at {output_path}")
