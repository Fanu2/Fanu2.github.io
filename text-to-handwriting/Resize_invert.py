from PIL import Image, ImageOps

# Open the image file
with Image.open('/home/jasvir/Music/jodha6/test1.jpg') as img:
    # Resize the image to 100x100
    img = img.resize((500, 500))

    # Invert the colors (negate)
    img = ImageOps.invert(img.convert('RGB'))

    # Save the result as 'out.jpg'
    img.save('/home/jasvir/Music/jodha6/1.jpg')
