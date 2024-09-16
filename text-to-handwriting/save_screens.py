import pyautogui
from PIL import Image

# Define the coordinates and dimensions of the region you want to capture
# (left, top, width, height)
region = (100, 100, 800, 600)  # Example values, adjust as needed

# Capture the region
screenshot = pyautogui.screenshot(region=region)

# Save the screenshot
screenshot.save('selected_area.png')

print('Screenshot saved successfully.')
