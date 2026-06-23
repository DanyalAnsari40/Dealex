import os
from rembg import remove
from PIL import Image
import glob

img_dir = r'c:\Users\danya\OneDrive\Desktop\delx\assets\images'

# Get all truck and excavator images
patterns = ['truck_*.png', 'excavator_*.png', 'yellow_truck*.png']
files_to_process = []
for pattern in patterns:
    files_to_process.extend(glob.glob(os.path.join(img_dir, pattern)))

# Exclude truck_about.png because we already did it perfectly
files_to_process = [f for f in files_to_process if not f.endswith('truck_about.png')]

for i, img_path in enumerate(files_to_process):
    print(f"Processing {i+1}/{len(files_to_process)}: {os.path.basename(img_path)}")
    try:
        img = Image.open(img_path)
        out = remove(img, post_process=True)
        out.save(img_path)
    except Exception as e:
        print(f"Failed to process {img_path}: {e}")

print("All done!")
