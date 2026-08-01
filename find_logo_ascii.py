from PIL import Image
import numpy as np

img = Image.open('media/robot_ai_humanoid_transparent.png').transpose(Image.FLIP_LEFT_RIGHT)
w, h = img.size

# We investigate the region around X=750 to 1000, Y=500 to 720
crop = img.crop((750, 520, 1000, 720)).convert('L')
arr = np.array(crop)

# Let's print an ASCII map to locate the darker logo on the bright white armor plate
# Map characters by brightness
chars = "@%#*+=-:. "
cw, ch = 70, 30
resized = crop.resize((cw, ch), Image.NEAREST)
res_arr = np.array(resized)

print("ASCII representation of shoulder region (X: 750-1000, Y: 520-720):")
print("    " + "".join([str((750 + int(i * 250 / cw)) // 10)[-1] for i in range(cw)]))
for y in range(ch):
    line = ""
    for x in range(cw):
        val = res_arr[y, x]
        # map 0-255 to chars
        idx = int((val / 255.0) * (len(chars) - 1))
        line += chars[idx]
    actual_y = 520 + int(y * 200 / ch)
    print(f"{actual_y:3d}|{line}")
