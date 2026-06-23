import os
import shutil

base_dir = r'c:\Users\danya\OneDrive\Desktop\delx'
old_img_dir = os.path.join(base_dir, 'assets', 'images')
new_img_dir = os.path.join(base_dir, 'images')

if not os.path.exists(new_img_dir):
    os.makedirs(new_img_dir)

print("Copying images...")
for root, dirs, files in os.walk(old_img_dir):
    for f in files:
        src = os.path.join(root, f)
        dst = os.path.join(new_img_dir, f)
        shutil.copy2(src, dst)
        print(f"Copied {f}")

print("Updating HTML, CSS, and JS files...")
files_to_update = ['index.html', 'delivar.html', 'faq_new.html', 'style.css', 'script.js']
for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace('./assets/images/', './images/')
        content = content.replace('/assets/images/', '/images/')
        content = content.replace('assets/images/', 'images/')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

print("Done copying images and updating paths!")
