import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import math
import os
from moviepy.editor import ImageSequenceClip

class ImageAnimation(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.title("Circular Image Animation")
        self.canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack()

        # Load and resize the image
        self.image_path = "/home/jasvir/Music/jodha5/1.jpg"
        self.image = Image.open(self.image_path).convert("RGBA")  # Ensure image has an alpha channel
        self.image = self.resize_image(self.image, 300, 300)
        self.image_tk = ImageTk.PhotoImage(self.image)

        # Animation parameters
        self.angle = 0
        self.radius = 100
        self.center_x = 300
        self.center_y = 300
        self.image_diameter = 100

        # Directory to save frames
        self.frames_dir = "frames"
        if not os.path.exists(self.frames_dir):
            os.makedirs(self.frames_dir)

        # Create Save button
        self.save_button = tk.Button(self, text="Save Animation", command=self.save_animation)
        self.save_button.pack()

        # Start the animation
        self.update_frame()

    def update_frame(self):
        # Compute new position
        x = int(self.center_x + self.radius * math.cos(math.radians(self.angle)) - self.image_diameter / 2)
        y = int(self.center_y + self.radius * math.sin(math.radians(self.angle)) - self.image_diameter / 2)

        # Create a circular clip and draw the image
        self.canvas.delete("all")
        self.canvas.create_oval(x, y, x + self.image_diameter, y + self.image_diameter, outline="", fill="white")
        self.canvas.create_image(x + self.image_diameter / 2, y + self.image_diameter / 2, image=self.image_tk, anchor=tk.CENTER)

        # Save the frame
        self.save_frame()

        # Update angle and schedule next frame
        self.angle = (self.angle + 1) % 360
        self.after(10, self.update_frame)

    def resize_image(self, img, new_w, new_h):
        return img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    def save_frame(self):
        # Create a buffered image of the current frame
        x = int(self.center_x + self.radius * math.cos(math.radians(self.angle)) - self.image_diameter / 2)
        y = int(self.center_y + self.radius * math.sin(math.radians(self.angle)) - self.image_diameter / 2)

        # Create a temporary canvas to draw the image
        temp_canvas = Image.new('RGBA', (800, 600), (255, 255, 255, 0))
        temp_draw = ImageDraw.Draw(temp_canvas)
        temp_draw.rectangle([x, y, x + self.image_diameter, y + self.image_diameter], fill="white")
        temp_canvas.paste(self.image, (x, y), self.image)  # Ensure this line works with transparency

        # Save the image
        frame_number = int(self.angle) % 360
        file_path = os.path.join(self.frames_dir, f"frame{frame_number:03d}.png")
        temp_canvas.save(file_path)

    def save_animation(self):
        # Compile images into a video
        frame_files = [os.path.join(self.frames_dir, f) for f in sorted(os.listdir(self.frames_dir)) if f.endswith('.png')]
        clip = ImageSequenceClip(frame_files, fps=30)

        # Ask for the output file path
        file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if file_path:
            clip.write_videofile(file_path, codec='libx264')

if __name__ == "__main__":
    app = ImageAnimation()
    app.mainloop()
