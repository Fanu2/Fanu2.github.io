from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as mpy
import os

# Paths to the images
image1_path = '/home/jasvir/Music/Card/1.png'
image2_path = '/home/jasvir/Music/Card/2.png'

# Path to save the final video
output_video_path = '/home/jasvir/Music/Card/book_opening.mp4'

# Load the images
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Resize images to fit within the card's page dimensions
page_width = 300  # Width of each page
page_height = 400  # Height of each page

image1 = image1.resize((page_width, page_height))  # Resize the first image
image2 = image2.resize((page_width, page_height))  # Resize the second image

# Create a blank canvas for the card
spine_width = 50  # Space for the spine
card_width = (page_width * 2) + spine_width  # Total width (left + right + spine)
card_height = page_height
frame_duration = 0.1  # Duration of each frame in seconds

# Create frames directory to store individual frames
frames_dir = '/home/jasvir/Music/Card/frames'
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

# Create frames for the animation (book opening)
num_frames = 20
for i in range(num_frames):
    # Create a blank card for each frame
    card = Image.new('RGB', (card_width, card_height), (255, 255, 255))

    # Create a drawing object for decorations
    draw = ImageDraw.Draw(card)

    # Calculate the position of the images for this frame
    left_x = int(page_width * (1 - i / num_frames))  # Left image moves from the center to the left
    right_x = int(card_width - page_width * (1 - i / num_frames))  # Right image moves from the center to the right

    # Paste the images onto the card with varying positions
    card.paste(image1, (left_x, 0))  # Paste image 1 on the left
    card.paste(image2, (right_x, 0))  # Paste image 2 on the right

    # Draw the spine
    draw.line([(card_width // 2, 0), (card_width // 2, card_height)], fill="black", width=5)  # Spine line

    # Save each frame as an image
    frame_path = os.path.join(frames_dir, f'frame_{i:02d}.png')
    card.save(frame_path)

# Create a MoviePy video from the frames
frames = [os.path.join(frames_dir, f'frame_{i:02d}.png') for i in range(num_frames)]
clip = mpy.ImageSequenceClip(frames, fps=10)  # Create a video at 10 fps

# Add a fade-in effect to make the opening smooth
clip = clip.fadein(1)

# Save the final video
clip.write_videofile(output_video_path, codec='libx264')

print(f"Book-opening video saved at {output_video_path}")
