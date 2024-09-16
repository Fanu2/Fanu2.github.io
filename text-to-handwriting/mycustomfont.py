import fontforge

# Create a new font object
font = fontforge.font()

# Set font properties
font.fontname = "MyCustomFont"
font.fullname = "My Custom Font"
font.familyname = "My Custom Font Family"
font.weight = "Regular"

# Define the Unicode code points for each glyph
characters = {
    "A": 65,  # Unicode code point for 'A'
    "B": 66,  # Unicode code point for 'B'
}

# Define the drawing paths for each character (as an example)
def draw_A(glyph):
    pen = glyph.glyphPen()
    pen.moveTo((100, 0))
    pen.lineTo((200, 700))
    pen.lineTo((300, 0))
    pen.closePath()
    pen.moveTo((150, 350))
    pen.lineTo((250, 350))
    pen.closePath()

def draw_B(glyph):
    pen = glyph.glyphPen()
    pen.moveTo((100, 0))
    pen.lineTo((100, 700))
    pen.lineTo((200, 700))
    pen.lineTo((250, 600))
    pen.lineTo((200, 500))
    pen.lineTo((150, 400))
    pen.closePath()

# Add glyphs to the font
for char, code in characters.items():
    glyph = font.createChar(code, char)
    glyph.width = 600

    if char == "A":
        draw_A(glyph)
    elif char == "B":
        draw_B(glyph)

# Generate the TTF file
output_ttf = "/home/jasvir/Music/MyCustomFont.ttf"
font.generate(output_ttf)
font.close()

print(f"Font generated and saved to {output_ttf}")
