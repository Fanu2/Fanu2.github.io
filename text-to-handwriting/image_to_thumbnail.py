from PIL import Image
import sys

def main():
    # Check if a path argument is provided; default to 'test.png' if not.
    path = sys.argv[1] if len(sys.argv) > 1 else '/home/jasvir/Music/jodha6/test.png'

    # Open the image file
    with Image.open(path) as img:
        # Resize the image to a width of 64 pixels while maintaining the aspect ratio.
        img = img.resize((864, int((img.height / img.width) * 864)))

        # Save the image as 'thumbnail.png'
        img.save('/home/jasvir/Music/jodha6/thumbnail.png')

if __name__ == '__main__':
    main()
