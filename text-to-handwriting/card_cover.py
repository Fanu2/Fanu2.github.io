from PIL import Image, ImageDraw, ImageFont

# Paths to the images
image1_path = '/home/jasvir/Music/Card/1.png'
image2_path = '/home/jasvir/Music/Card/2.png'

# Path to save the final card
output_path = '/home/jasvir/Music/Card/foldable_love_card.png'

# Load the images
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Resize images to fit inside the card (you can adjust these values)
image1 = image1.resize((300, 400))  # Width, Height
image2 = image2.resize((300, 400))

# Create a blank card (double width for the fold)
card_width = (image1.width + image2.width + 100) * 2  # Double width for the front/back and inside pages
card_height = max(image1.height, image2.height) + 200  # Space for images and top/bottom margin
card = Image.new('RGB', (card_width, card_height), (255, 255, 255))  # White background

# Create a drawing object
draw = ImageDraw.Draw(card)

# Load fonts for the text
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Use any font you prefer
cover_font = ImageFont.truetype(font_path, 50)
inside_font = ImageFont.truetype(font_path, 40)

# 1. Add text to the front and back cover (the left and right halves of the folded outside)

# Front cover text (right side)
front_message = "Our Love Story"
text_width, text_height = draw.textsize(front_message, font=cover_font)
draw.text(((card_width // 2 + card_width // 4 - text_width // 2), card_height // 4), front_message, font=cover_font, fill="black")

# Back cover text (left side)
back_message = "To: The One I Love\nFrom: Your Name"
draw.text((card_width // 4 - 150, card_height // 4), back_message, font=inside_font, fill="black")

# 2. Add decorations (hearts) on the front cover
heart_symbol = "♥"
draw.text(((card_width // 2 + card_width // 4 - 25), card_height // 4 + text_height + 20), heart_symbol, font=cover_font, fill="red")

# 3. Paste the two images inside the card (on the left and right halves of the inside)

# Inside layout (open card)
card.paste(image1, (50, 100))  # Left image on the left side (inside)
card.paste(image2, (card_width // 2 + 50, 100))  # Right image on the right side (inside)

# 4. Add inside message (optional)
inside_message = "Together Forever"
text_width, text_height = draw.textsize(inside_message, font=inside_font)
draw.text(((card_width - text_width) // 2, (card_height - text_height) // 2), inside_message, font=inside_font, fill="black")

# Save the card
card.save(output_path)

print(f"Foldable love card saved at {output_path}")
