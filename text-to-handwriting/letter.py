from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np


# Function to draw lines on the notebook page
def create_notebook_page(width, height, line_height=40, line_color=(200, 200, 200)):
    # Create a blank white page
    page = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Draw lines
    for y in range(line_height, height, line_height):
        cv2.line(page, (0, y), (width, y), line_color, thickness=2)

    return page


# Function to write text on the page
def write_handwritten_text(page, text, font_path, font_size=32, text_color=(0, 0, 0), margin=40):
    # Convert the page back to a Pillow image for drawing text
    pil_image = Image.fromarray(page)
    draw = ImageDraw.Draw(pil_image)

    # Load a handwritten font (ensure you have a .ttf font)
    font = ImageFont.truetype(font_path, font_size)

    # Coordinates to start writing text
    x, y = margin, margin

    # Write each line of text
    for line in text.split('\n'):
        draw.text((x, y), line, font=font, fill=text_color)
        y += font_size + 10  # Move to the next line

    # Convert back to OpenCV format
    page_with_text = np.array(pil_image)

    return page_with_text


# Main function
def main():
    # Notebook page size
    width, height = 800, 1000

    # Sample handwritten letter text
    text = """Dear Friend,

I hope this letter finds you well. It's been quite a while since we last spoke, and I wanted to take a moment to catch up. 

Life has been busy on my end, but I've been thinking about the times we've shared. I miss those days, and I hope we can reconnect soon.

Take care and stay safe. Looking forward to hearing from you.

Best regards,
Your Name
"""

    # Path to a handwritten font file (.ttf)
    font_path = "/usr/share/fonts/truetype/dancing_script/DancingScript-Regular.ttf" # Replace with the path to your font

    # Create a blank notebook page with lines
    notebook_page = create_notebook_page(width, height)

    # Write the text on the page
    final_image = write_handwritten_text(notebook_page, text, font_path)

    # Save the final image
    output_path = "handwritten_letter.png"
    cv2.imwrite(output_path, final_image)

    print(f"Handwritten letter saved to {output_path}")


if __name__ == "__main__":
    main()
