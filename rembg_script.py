from rembg import remove
from PIL import Image

input_path = r'C:\Users\danya\.gemini\antigravity-ide\brain\082ac422-0a96-46e3-a95e-0713cd2684a7\dealex_truck_1782211774133.png'
output_path = r'c:\Users\danya\OneDrive\Desktop\delx\assets\images\truck_about.png'

print("Loading image...")
img = Image.open(input_path)

print("Removing background using AI...")
# post_process=True helps clean up edges
out = remove(img, post_process=True)

print("Saving image...")
out.save(output_path)
print("Done! Background perfectly removed.")
