from moviepy.editor import *
import numpy as np
from scipy.ndimage import gaussian_filter

# Define image paths
image1_path = '/home/jasvir/Music/Card/1.png'
image2_path = '/home/jasvir/Music/Card/2.png'

# Load images
img1 = ImageClip(image1_path).resize(height=100)
img2 = ImageClip(image2_path).resize(height=100)

# Define canvas size and duration
canvas_width = 640
canvas_height = 480
duration = 10  # Duration of the video in seconds

# Function to create a romantic gradient background
def create_background():
    gradient = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)
    for y in range(canvas_height):
        for x in range(canvas_width):
            r = int(255 * (1 - y / canvas_height))
            g = int(182 + 73 * (x / canvas_width))
            b = int(193 + 87 * (y / canvas_height))
            gradient[y, x] = [min(max(r, 0), 255), min(max(g, 0), 255), min(max(b, 0), 255)]
    return gradient

# Function to add soft glow to an image
def add_glow(image, intensity=0.5):
    image = image.astype(np.float32)
    blurred_image = gaussian_filter(image, sigma=10)
    return np.clip(blurred_image * intensity + image, 0, 255).astype(np.uint8)

# Create a function to move images in a circular path
def make_frame(t):
    frame = create_background()

    # Center of the canvas
    cx, cy = canvas_width // 2, canvas_height // 2

    # Radius for circular movement
    radius = 150

    # Angle increment based on time
    angle = 2 * np.pi * t / duration

    # Image 1 position
    x1 = int(cx + radius * np.cos(angle)) - img1.w // 2
    y1 = int(cy + radius * np.sin(angle)) - img1.h // 2

    # Image 2 position
    x2 = int(cx + radius * np.cos(angle + np.pi)) - img2.w // 2
    y2 = int(cy + radius * np.sin(angle + np.pi)) - img2.h // 2

    # Ensure images fit within the frame
    img1_frame = add_glow(img1.get_frame(0))
    img2_frame = add_glow(img2.get_frame(0))

    if 0 <= x1 < canvas_width and 0 <= y1 < canvas_height:
        frame[y1:y1+img1.h, x1:x1+img1.w] = img1_frame[
            max(0, -y1):min(img1.h, canvas_height - y1),
            max(0, -x1):min(img1.w, canvas_width - x1)
        ]

    if 0 <= x2 < canvas_width and 0 <= y2 < canvas_height:
        frame[y2:y2+img2.h, x2:x2+img2.w] = img2_frame[
            max(0, -y2):min(img2.h, canvas_height - y2),
            max(0, -x2):min(img2.w, canvas_width - x2)
        ]

    return frame

# Create a video clip
video = VideoClip(make_frame, duration=duration)

# Set video properties
video = video.set_duration(duration).set_fps(24)

# Write the video to a file
video.write_videofile('/home/jasvir/Music/Card/lovers_circular_motion.mp4', codec='libx264')
