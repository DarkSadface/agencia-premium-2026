from PIL import Image
import numpy as np

img = Image.open('media/robot_ai_humanoid_transparent.png').transpose(Image.FLIP_LEFT_RIGHT)

# Let's check X: 820 to 930, Y: 580 to 690
crop = img.crop((820, 580, 930, 690)).convert('RGB')
arr = np.array(crop)
gray = np.mean(arr, axis=2)

# Let's print average brightness per 10x10 tile to see where the dark spot / logo is located!
h, w = gray.shape
print("Brightness 10x10 grid from X=820..930, Y=580..690:")
for y in range(0, h, 10):
    row = []
    for x in range(0, w, 10):
        val = np.mean(gray[y:y+10, x:x+10])
        row.append(f"{val:5.1f}")
    print(f"Y={580+y:3d} | " + " ".join(row))

# Also let's check a wider area to be certain of where the shoulder plate center is!
crop_wide = img.crop((750, 550, 950, 720)).convert('RGB')
gw = np.mean(np.array(crop_wide), axis=2)
# Find minimum brightness in each column/row to find the logo inscription
print("\nMin brightness in Y rows (550 to 720):")
print([(y+550, int(np.min(gw[y, :]))) for y in range(0, gw.shape[0], 10)])
