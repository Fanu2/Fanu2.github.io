from PIL import Image, ImageDraw, ImageFont

# Paths to the images
image1_path = '/home/jasvir/Music/Card/1.png'
image2_path = '/home/jasvir/Music/Card/2.png'

# Path to save the final card
output_path = '/home/jasvir/Music/Card/book_love_card.png'

# Load the images
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Resize images to fit within the card's page dimensions (you can adjust these values)
page_width = 300  # Width of each page
page_height = 400  # Height of each page

image1 = image1.resize((page_width, page_height))  # Resize the first image
image2 = image2.resize((page_width, page_height))  # Resize the second image

# Create a blank canvas for the book, including space for the spine
spine_width = 50  # Space between the images to simulate the spine
card_width = (page_width * 2) + spine_width  # Total width (two pages + spine)
card_height = page_height  # Height of the card (same as the image height)
card = Image.new('RGB', (card_width, card_height), (255, 255, 255))  # White background

# Create a drawing object to add text and decorations
draw = ImageDraw.Draw(card)

# Paste the images onto the card, with a gap between them for the spine
card.paste(image1, (0, 0))  # Paste image 1 on the left page
card.paste(image2, (page_width + spine_width, 0))  # Paste image 2 on the right page

# Optional: Add decorations or a "spine" line in the middle to simulate the book's fold
draw.line([(page_width + spine_width // 2, 0), (page_width + spine_width // 2, card_height)], fill="black", width=5)  # Draw a black spine line

# Add some decoration (hearts) near the top and bottom of the spine
heart_symbol = "♥"
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust path if needed
font = ImageFont.truetype(font_path, 50)

# Add hearts at the top and bottom of the spine
draw.text(((card_width // 2) - 25, 20), heart_symbol, font=font, fill="red")
draw.text(((card_width // 2) - 25, card_height - 70), heart_symbol, font=font, fill="red")

# Optional: Add a romantic message in the middle, near the spine
message = "Together Forever"
message_font = ImageFont.truetype(font_path, 30)
text_width, text_height = draw.textsize(message, font=message_font)
draw.text(((card_width - text_width) // 2, (card_height - text_height) // 2), message, font=message_font, fill="black")

# Save the final card image
card.save(output_path)

print(f"Book-style love card saved at {output_path}")
