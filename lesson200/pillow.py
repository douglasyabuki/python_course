# Pillow: resizing images with Python
# This library is Python's Photoshop 😂
from pathlib import Path

from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.JPG'
NEW_IMAGE = ROOT_FOLDER / 'new.JPG'

# Open the original image
pil_image = Image.open(ORIGINAL)
width, height = pil_image.size
exif = pil_image.info['exif']

# Calculate new dimensions maintaining the aspect ratio
new_width = 640
new_height = round(height * new_width / width)

# Resize the image
new_image = pil_image.resize(size=(new_width, new_height))

# Save the resized image with optimization and adjusted quality
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    # exif=exif,  # Optional: preserve EXIF metadata
)
