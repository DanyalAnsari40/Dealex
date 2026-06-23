import re
with open('c:/Users/danya/OneDrive/Desktop/delx/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace primary brand colors (blues and reds) to #F04B14
content = content.replace('bg-blue-600', 'bg-[#F04B14]')
content = content.replace('hover:bg-blue-700', 'hover:bg-[#d83c0c]')
content = content.replace('text-blue-600', 'text-[#F04B14]')
content = content.replace('text-blue-500', 'text-[#F04B14]')
content = content.replace('hover:text-blue-500', 'hover:text-[#F04B14]')
content = content.replace('bg-blue-500', 'bg-[#F04B14]')
content = content.replace('shadow-blue-600/20', 'shadow-[#F04B14]/20')
content = content.replace('shadow-blue-600/10', 'shadow-[#F04B14]/10')
content = content.replace('shadow-blue-500', 'shadow-[#F04B14]')
content = content.replace('text-[#E31E2F]', 'text-[#F04B14]')
content = content.replace('bg-[#E31E2F]', 'bg-[#F04B14]')
content = content.replace('bg-[#1D4ED8]', 'bg-[#F04B14]') # Blue banner in moving rope
content = content.replace('text-[#1D4ED8]', 'text-[#F04B14]') # Text in moving rope

# Background colors to #2D2D2D
content = content.replace('bg-[#F4F7FB]', 'bg-[#2D2D2D]')
content = content.replace('<section class="bg-white', '<section class="bg-[#2D2D2D]')
content = content.replace('<section class="relative bg-white', '<section class="relative bg-[#2D2D2D]')
content = content.replace('<section class="w-full bg-white', '<section class="w-full bg-[#2D2D2D]')
content = content.replace('bg-[#050B14]', 'bg-[#2D2D2D]') # FAQ section
content = content.replace('<footer class="bg-white', '<footer class="bg-[#2D2D2D]')

# Card backgrounds
content = content.replace('bg-[#F8F9FB]', 'bg-[#1A1A1C]')
content = content.replace('bg-white p-8 rounded-3xl', 'bg-[#1A1A1C] p-8 rounded-3xl border border-white/5') # Why choose us cards
content = content.replace('bg-white rounded-[20px]', 'bg-[#1A1A1C] rounded-[20px] border border-white/5') # Moving divs
content = content.replace('bg-[#030812]', 'bg-[#1A1A1C]') # Footer inner capsule

# Text colors for dark mode
content = content.replace('text-[#0F172A]', 'text-white')
content = content.replace('text-[#0B408E]', 'text-white')
content = content.replace('text-gray-500', 'text-gray-400') # Lighten dark gray text

# Specific adjustments
# About us section button
content = content.replace('bg-[#111111] text-white', 'bg-[#F04B14] text-white')
content = content.replace('hover:bg-black', 'hover:bg-[#d83c0c]')

# Dealex Own Terminal 'Get A Quote' button
content = content.replace('bg-white text-white px-6 py-3 rounded-md font-semibold flex items-center gap-2 border border-gray-200 shadow-sm hover:bg-gray-50', 'bg-[#F04B14] text-white px-6 py-3 rounded-md font-semibold flex items-center gap-2 border border-transparent hover:bg-[#d83c0c]')

# Body tag text-white
content = content.replace('<body class="p-4 md:p-6 min-h-screen flex flex-col items-center justify-center">', '<body class="p-4 md:p-6 min-h-screen flex flex-col items-center justify-center bg-[#2D2D2D] text-white">')

with open('c:/Users/danya/OneDrive/Desktop/delx/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Theme replaced.")
