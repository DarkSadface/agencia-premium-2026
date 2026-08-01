from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import os, math

# 1. Create high-resolution logo template (600x600)
logo_size = 600
logo = Image.new('RGBA', (logo_size, logo_size), (0, 0, 0, 0))
draw = ImageDraw.Draw(logo)

# Center of icon
cx, cy = 300, 230
hex_radius = 135

# Calculate 6 vertices of regular hexagon (flat-topped or pointy-topped)
# In the user's screenshot, it has flat top and bottom! So vertices are at angles 0, 60, 120, 180, 240, 300
points = []
for i in range(6):
    angle_deg = 60 * i
    angle_rad = math.radians(angle_deg)
    px = cx + hex_radius * math.cos(angle_rad)
    py = cy + hex_radius * math.sin(angle_rad)
    points.append((px, py))
points.append(points[0]) # Close loop

# Draw glowing cyan hexagon (#38e6ff -> (56, 230, 255))
# Outer glow
for r_off in range(15, 0, -2):
    alpha = int(80 * (15 - r_off) / 15)
    draw.line(points, fill=(56, 230, 255, alpha), width=24 + r_off)

# Sharp solid core hexagon line
draw.line(points, fill=(56, 230, 255, 255), width=22)

# Draw inner emerald green circle (#00ff88 -> (0, 255, 136))
circle_radius = 52
bbox = [cx - circle_radius, cy - circle_radius, cx + circle_radius, cy + circle_radius]
# Glow for circle
for c_off in range(12, 0, -2):
    alpha = int(70 * (12 - c_off) / 12)
    cb = [cx - circle_radius - c_off, cy - circle_radius - c_off, cx + circle_radius + c_off, cy + circle_radius + c_off]
    draw.ellipse(cb, fill=None, outline=(0, 255, 136, alpha), width=c_off)

draw.ellipse(bbox, fill=(0, 255, 136, 255))

# Draw text "JARVIS" below the icon in bright cyan
# Find an appropriate crisp bold system font
font_paths = [
    r'C:\Windows\Fonts\consola.ttf',
    r'C:\Windows\Fonts\arialbd.ttf',
    r'C:\Windows\Fonts\segoeuib.ttf',
    r'C:\Windows\Fonts\impact.ttf',

]
font = None
for fp in font_paths:
    if os.path.exists(fp):
        try:
            font = ImageFont.truetype(fp, 110)
            print("Loaded font:", fp)
            break
        except Exception as e:
            pass
if not font:
    font = ImageFont.load_default()

text = "J A R V I S"
# Get text bounding box to center it
t_left, t_top, t_right, t_bottom = draw.textbbox((0, 0), text, font=font)
tw = t_right - t_left
th = t_bottom - t_top

tx = cx - tw // 2
ty = cy + hex_radius + 35

# Draw glow around text
for off in [(-2,0), (2,0), (0,-2), (0,2), (-2,-2), (2,2)]:
    draw.text((tx + off[0], ty + off[1]), text, font=font, fill=(0, 180, 220, 100))

# Main crisp cyan text
draw.text((tx, ty), text, font=font, fill=(56, 230, 255, 255))

# Let's save a preview of the standalone high-res emblem just in case
logo.save('media/jarvis_emblem_preview.png')
print("Generated high-res JARVIS emblem!")

# 2. Load robot image and flip left-right
img = Image.open('media/robot_ai_humanoid_transparent.png').transpose(Image.FLIP_LEFT_RIGHT).convert('RGBA')
arr = np.array(img).astype(float)

# 3. Clean existing AETHER logo cleanly (X=846..886, Y=638..668)
x1, x2 = 846, 886
y1, y2 = 638, 668
for y in range(y1, y2):
    ty = (y - y1) / float(y2 - y1)
    for x in range(x1, x2):
        tx = (x - x1) / float(x2 - x1)
        c_ul = arr[y1, x1, :3]
        c_ur = arr[y1, x2-1, :3]
        c_ll = arr[y2-1, x1, :3]
        c_lr = arr[y2-1, x2-1, :3]
        val = (c_ul * (1 - tx) + c_ur * tx) * (1 - ty) + (c_ll * (1 - tx) + c_lr * tx) * ty
        # Blend out darker letters completely while keeping titanium sheen
        arr[y, x, :3] = arr[y, x, :3] * 0.1 + val * 0.9

cleaned_robot = Image.fromarray(arr.astype(np.uint8))

# 4. Rotate logo slightly to match shoulder armor slope (~ 16 degrees clockwise)
rotated_logo = logo.rotate(-16, resample=Image.BICUBIC, expand=True)

# 5. Scale logo to fit the shoulder armor plate perfectly (~58x58 pixels)
target_size = (58, 58)
final_logo = rotated_logo.resize(target_size, Image.Resampling.LANCZOS)

# 6. Paste onto cleaned armor plate (centered on X=866, Y=652)
paste_x = 866 - target_size[0] // 2
paste_y = 652 - target_size[1] // 2

cleaned_robot.alpha_composite(final_logo, (paste_x, paste_y))

# Save the new master image!
output_path = 'media/robot_ai_humanoid_jarvis.png'
cleaned_robot.save(output_path)
print("Successfully generated master image:", output_path)

# Let's save a zoomed-in crop of the shoulder armor for inspection!
crop_check = cleaned_robot.crop((800, 580, 940, 720))
crop_check.save('media/jarvis_shoulder_inspection.png')
print("Saved inspection crop jarvis_shoulder_inspection.png!")
