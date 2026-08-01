from PIL import Image
import os

img_path = 'media/robot_ai_humanoid_transparent.png'
img = Image.open(img_path)
print("Original size:", img.size, "Mode:", img.mode)

# Let's check dimensions
w, h = img.size

# Flip horizontally to match website view (facing left)
flipped = img.transpose(Image.FLIP_LEFT_RIGHT)

# Let's crop several candidates around the shoulder area to find the exact box
# Based on screenshot: shoulder is roughly X: 60% to 85%, Y: 55% to 80%
crop_box = (int(w * 0.60), int(h * 0.55), int(w * 0.88), int(h * 0.82))
cropped = flipped.crop(crop_box)
cropped.save('media/shoulder_crop.png')
print("Saved shoulder_crop.png with box:", crop_box)
