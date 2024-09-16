from PIL import Image, ImageDraw

def create_lined_paper(width, height, line_spacing, line_color, background_color):
    # Create a new image with white background
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Draw horizontal lines
    y = 0
    while y < height:
        draw.line((0, y, width, y), fill=line_color)
        y += line_spacing

    # Save the image
    image.save('/home/jasvir/java/output/lined_paper.png')

# Parameters
width = 800  # Image width
height = 1000  # Image height
line_spacing = 40  # Spacing between lines
line_color = 'black'  # Color of the lines
background_color = 'white'  # Background color

create_lined_paper(width, height, line_spacing, line_color, background_color)
