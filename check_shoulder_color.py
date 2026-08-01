from PIL import Image
import numpy as np

img = Image.open('media/robot_ai_humanoid_transparent.png').transpose(Image.FLIP_LEFT_RIGHT)
w, h = img.size

# Let's search in X=800..950, Y=580..720 for pixels that belong to the lettering (relatively dark compared to bright armor)
crop = img.crop((820, 580, 930, 690))
arr = np.array(crop)

# Let's check where brightness is < 150 inside the bright armor region (where average surrounding is > 170)
brightness = np.mean(arr[:, :, :3], axis=2)

# Print out a character map of dark (<140) vs bright (>=140) pixels in X=850..920, Y=610..680
print("Logo silhouette map (X=850..920, Y=610..680): '#' = dark/logo pixel, '.' = bright armor:")
for y in range(30, 100, 2):  # Y=610 to 680
    line = ""
    for x in range(30, 100, 2):  # X=850 to 920
        b = brightness[y, x]
        line += "#" if b < 145 else "."
    print(f"Y={580+y:3d} | " + line)
