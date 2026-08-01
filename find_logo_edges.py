from PIL import Image, ImageFilter
import numpy as np

img = Image.open('media/robot_ai_humanoid_transparent.png').transpose(Image.FLIP_LEFT_RIGHT)
crop = img.crop((820, 580, 920, 680)).convert('L')

# Find edges using simple gradient
arr = np.array(crop, dtype=float)
gy, gx = np.gradient(arr)
edges = np.sqrt(gx**2 + gy**2)

print("Edge density grid (X=820..920, Y=580..680) - higher numbers mean lettering/logo lines:")
h, w = edges.shape
for y in range(0, h, 5):
    row = []
    for x in range(0, w, 5):
        val = np.mean(edges[y:y+5, x:x+5])
        row.append(f"{val:4.1f}")
    print(f"Y={580+y:3d} | " + " ".join(row))
