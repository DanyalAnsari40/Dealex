import re

file_path = r'c:\Users\danya\OneDrive\Desktop\delx\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the 8 Why Choose Us cards
target_div = '<div class="relative flex flex-col items-center text-center px-4 group overflow-visible">'

delay = 100
for _ in range(8):
    replacement = f'<div class="relative flex flex-col items-center text-center px-4 group overflow-visible transition-all duration-700 ease-out opacity-0 -translate-x-[50px] why-choose-card" style="transition-delay: {delay}ms;">'
    content = content.replace(target_div, replacement, 1)
    delay += 100

# Add the observer script
script_insertion = """            // Why Choose Us Cards Animation
            const whyChooseCards = document.querySelectorAll('.why-choose-card');
            if (whyChooseCards.length > 0) {
                const whyChooseObserver = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.remove('opacity-0', '-translate-x-[50px]');
                            entry.target.classList.add('opacity-100', 'translate-x-0');
                            setTimeout(() => entry.target.style.transitionDelay = '0ms', 1000);
                            whyChooseObserver.unobserve(entry.target);
                        }
                    });
                }, { threshold: 0.1 });
                whyChooseCards.forEach(card => whyChooseObserver.observe(card));
            }
"""

# Insert right before the end of the DOMContentLoaded block
target_script_end = "        });\n    </script>"
if target_script_end in content:
    content = content.replace(target_script_end, script_insertion + target_script_end)
else:
    print("Could not find script end tag.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")
