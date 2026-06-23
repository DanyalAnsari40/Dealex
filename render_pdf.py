import fitz
import os

doc = fitz.open(r'DEALEX TRANSPORT & LOGISTICS SERVICES.pdf')
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pdf_pages')
os.makedirs(output_dir, exist_ok=True)

for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=150)
    output_path = os.path.join(output_dir, f'page_{i+1}.png')
    pix.save(output_path)
    print(f"Saved page {i+1} to {output_path}")

doc.close()
print("Done!")
