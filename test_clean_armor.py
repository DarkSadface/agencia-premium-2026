from PIL import Image
import numpy as np

# Load and flip
img = Image.open('media/robot_ai_humanoid_transparent.png').transpose(Image.FLIP_LEFT_RIGHT)
arr = np.array(img).astype(float)

# Let's inspect the bounding rectangle to clean: X=848..884, Y=640..664
x1, x2 = 848, 884
y1, y2 = 640, 664

# Perform smooth bilinear interpolation across the rectangle from its boundaries
for y in range(y1, y2):
    ty = (y - y1) / float(y2 - y1)
    for x in range(x1, x2):
        tx = (x - x1) / float(x2 - x1)
        # 4 corners
        c_ul = arr[y1, x1, :]
        c_ur = arr[y1, x2-1, :]
        c_ll = arr[y2-1, x1, :]
        c_lr = arr[y2-1, x2-1, :]
        
        top = c_ul * (1 - tx) + c_ur * tx
        bottom = c_ll * (1 - tx) + c_lr * tx
        val = top * (1 - ty) + bottom * ty
        
        # We only interpolate if the pixel is darker than normal titanium armor (e.g. logo lines)
        # or we blend smoothly to eradicate all traces of AETHER
        arr[y, x, :] = arr[y, x, :] * 0.15 + val * 0.85

clean_img = Image.fromarray(arr.astype(np.uint8))
clean_img.save('media/robot_cleaned_test.png')

# Let's check brightness in that box now to verify zero dark spots remain
gray = np.mean(arr[y1:y2, x1:x2, :3], axis=2)
print("Min brightness after cleaning:", np.min(gray), "Max:", np.max(gray), "Mean:", np.mean(gray))
print("Saved robot_cleaned_test.png successfully!")
