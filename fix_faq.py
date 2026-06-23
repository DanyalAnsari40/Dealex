import sys

with open('c:/Users/danya/OneDrive/Desktop/delx/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<div class="grid lg:grid-cols-12 gap-16 items-start pt-8 relative z-20">'
start_idx = text.find(start_marker)

section_end_idx = text.find('</section>', start_idx)
last_div_idx = text.rfind('</div>', start_idx, section_end_idx)

if start_idx != -1 and last_div_idx != -1:
    before = text[:start_idx]
    after = text[last_div_idx + 6:]
    
    with open('c:/Users/danya/OneDrive/Desktop/delx/faq_new.html', 'r', encoding='utf-8') as newf:
        new_faq = newf.read()
        
    new_text = before + new_faq + after
    
    with open('c:/Users/danya/OneDrive/Desktop/delx/index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced successfully.")
else:
    print("Could not find markers.")
    print("start_idx:", start_idx)
    print("last_div_idx:", last_div_idx)
