import sys
from PIL import Image

def remove_white_bg_flood(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    
    # We will use flood fill to find the background
    # Since PIL doesn't have a direct flood fill to alpha, we create a mask
    from PIL import ImageDraw
    
    # Create a mask image (L mode), initialize with 0
    mask = Image.new("L", img.size, 0)
    
    # The flood fill will start from 0,0 and fill with 255
    # any pixel that is close to the color at 0,0 (which should be the white background)
    ImageDraw.floodfill(img, (0, 0), (255, 255, 255, 0), thresh=30)
    ImageDraw.floodfill(img, (img.width-1, 0), (255, 255, 255, 0), thresh=30)
    ImageDraw.floodfill(img, (0, img.height-1), (255, 255, 255, 0), thresh=30)
    ImageDraw.floodfill(img, (img.width-1, img.height-1), (255, 255, 255, 0), thresh=30)
    
    img.save(output_path)
    print("Background removed and saved to", output_path)

input_path = r'C:\Users\danya\.gemini\antigravity-ide\brain\082ac422-0a96-46e3-a95e-0713cd2684a7\dealex_truck_1782211774133.png'
output_path = r'c:\Users\danya\OneDrive\Desktop\delx\assets\images\truck_about.png'
remove_white_bg_flood(input_path, output_path)
