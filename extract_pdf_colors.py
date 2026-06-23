import fitz
import json
from collections import Counter

doc = fitz.open(r'DEALEX TRANSPORT & LOGISTICS SERVICES.pdf')

print(f"Total pages: {len(doc)}")
print("=" * 80)

# Extract text from all pages
for i, page in enumerate(doc):
    print(f"\n--- PAGE {i+1} ---")
    print(page.get_text())

# Extract colors from drawings/annotations
print("\n" + "=" * 80)
print("EXTRACTING COLORS FROM DRAWINGS/SHAPES")
print("=" * 80)

all_colors = []
for i, page in enumerate(doc):
    drawings = page.get_drawings()
    for d in drawings:
        if d.get("fill"):
            r, g, b = d["fill"]
            hex_color = "#{:02x}{:02x}{:02x}".format(int(r*255), int(g*255), int(b*255))
            all_colors.append(hex_color)
        if d.get("color"):
            r, g, b = d["color"]
            hex_color = "#{:02x}{:02x}{:02x}".format(int(r*255), int(g*255), int(b*255))
            all_colors.append(hex_color)

# Extract text colors
print("\n" + "=" * 80)
print("EXTRACTING TEXT COLORS")
print("=" * 80)

text_colors = []
for i, page in enumerate(doc):
    blocks = page.get_text("dict")["blocks"]
    for block in blocks:
        if "lines" in block:
            for line in block["lines"]:
                for span in line["spans"]:
                    color_int = span.get("color", 0)
                    r = (color_int >> 16) & 0xFF
                    g = (color_int >> 8) & 0xFF
                    b = color_int & 0xFF
                    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
                    text_colors.append(hex_color)
                    if hex_color not in ["#000000", "#ffffff"]:
                        print(f"  Text: '{span['text'][:50]}' -> Color: {hex_color}")

print("\n" + "=" * 80)
print("COLOR SUMMARY")
print("=" * 80)

all_unique = set(all_colors + text_colors)
print(f"\nAll unique colors found: {sorted(all_unique)}")

color_counts = Counter(all_colors + text_colors)
print(f"\nTop colors by frequency:")
for color, count in color_counts.most_common(20):
    print(f"  {color}: {count} occurrences")

# Also extract images info
print("\n" + "=" * 80)
print("IMAGES IN PDF")
print("=" * 80)
for i, page in enumerate(doc):
    images = page.get_images()
    for img in images:
        print(f"  Page {i+1}: Image xref={img[0]}, size={img[2]}x{img[3]}")

doc.close()
