import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
import math
import os
import io

class CircularAnimation(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set up window
        self.title("Circular Image Animation")
        self.canvas = Canvas(self, width=800, height=600)
        self.canvas.pack()

        # Load and resize the image
        self.image_path = "/home/jasvir/Music/jodha5/2.jpg"
        self.image = Image.open(self.image_path)
        self.image = self.resize_image(self.image, 100, 100)
        self.image_tk = ImageTk.PhotoImage(self.image)

        # Animation parameters
        self.angle = 0
        self.radius = 100
        self.center_x = 300
        self.center_y = 300
        self.image_diameter = 100
        self.frame_number = 0
        self.max_frames = 360

        # Create directory for output images
        self.output_dir = "/home/jasvir/java/output/"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # Start the animation
        self.update_frame()

    def update_frame(self):
        # Compute new position
        x = int(self.center_x + self.radius * math.cos(math.radians(self.angle)) - self.image_diameter / 2)
        y = int(self.center_y + self.radius * math.sin(math.radians(self.angle)) - self.image_diameter / 2)

        # Create a circular clip and draw the image
        self.canvas.delete("all")
        self.canvas.create_oval(x, y, x + self.image_diameter, y + self.image_diameter, outline="", fill="white", tags="clip")
        self.canvas.create_image(x + self.image_diameter / 2, y + self.image_diameter / 2, image=self.image_tk, anchor=tk.CENTER)

        # Save the frame if the condition is met
        if self.frame_number < self.max_frames:
            self.save_frame()
            self.frame_number += 1

        # Update angle and schedule next frame
        self.angle = (self.angle + 1) % 360
        self.after(30, self.update_frame)

    def resize_image(self, img, new_w, new_h):
        return img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    def save_frame(self):
        try:
            # Create a PIL image of the current frame
            self.canvas.update_idletasks()
            canvas_postscript = self.canvas.postscript(colormode='color')
            frame = Image.open(io.BytesIO(canvas_postscript.encode('utf-8')))
            # Save the image to the output directory
            output_path = os.path.join(self.output_dir, f"frame{self.frame_number:04d}.png")
            frame.save(output_path)
        except Exception as e:
            print(f"Error saving frame: {e}")

if __name__ == "__main__":
    app = CircularAnimation()
    app.mainloop()
