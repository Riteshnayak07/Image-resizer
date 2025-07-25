import os
from PIL import Image

# Define input and output folders
input_folder = "images"       # Folder where original images are stored
output_folder = "resized"     # Folder where resized images will be saved
size = (800, 800)             # Target size (width, height)

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):
        filepath = os.path.join(input_folder, filename)
        with Image.open(filepath) as img:
            resized_img = img.resize(size)
            resized_img.save(os.path.join(output_folder, filename))

print("✅ All images resized and saved to:", output_folder)
