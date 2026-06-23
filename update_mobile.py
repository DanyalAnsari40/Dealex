import re

file_path = r'c:\Users\danya\OneDrive\Desktop\delx\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero section minimum height
content = content.replace(
    'min-h-[780px] lg:min-h-[85vh] xl:min-h-[90vh]',
    'min-h-[550px] md:min-h-[780px] lg:min-h-[85vh] xl:min-h-[90vh]'
)

# 2. Update Header for Hamburger Menu and hidden sm on button
old_button = '''<a href="#"
                    class="bg-[#F04B14] hover:bg-[#d83c0c] text-white px-5 py-2.5 rounded-full text-xs font-bold tracking-wide transition-all flex items-center gap-2 shadow-lg shadow-[#F04B14]/20 border border-[#F04B14]">
                    Get In Touch <span class="text-xs font-normal">↗</span>
                </a>'''
new_button = '''<a href="#"
                    class="bg-[#F04B14] hover:bg-[#d83c0c] text-white px-5 py-2.5 rounded-full text-xs font-bold tracking-wide transition-all hidden sm:flex items-center gap-2 shadow-lg shadow-[#F04B14]/20 border border-[#F04B14]">
                    Get In Touch <span class="text-xs font-normal">↗</span>
                </a>
                <!-- Hamburger Button -->
                <button id="mobile-menu-btn" class="lg:hidden text-white hover:text-[#F04B14] transition-colors p-2 ml-2">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>'''
content = content.replace(old_button, new_button)

# Add mobile menu right before </body>
mobile_menu = '''
    <!-- Mobile Menu Overlay -->
    <div id="mobile-menu" class="fixed inset-0 bg-[#1A1A1C]/95 backdrop-blur-xl z-50 transform translate-x-full transition-transform duration-300 flex flex-col items-center justify-center space-y-8">
        <button id="close-menu-btn" class="absolute top-8 right-8 text-white hover:text-[#F04B14] transition-colors p-2">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
        </button>
        <nav class="flex flex-col items-center space-y-6 text-xl font-bold tracking-wider text-white uppercase">
            <a href="#" class="text-[#F04B14]">Home</a>
            <a href="#" class="hover:text-[#F04B14] transition-colors">Pages</a>
            <a href="#" class="hover:text-[#F04B14] transition-colors">Services</a>
            <a href="#" class="hover:text-[#F04B14] transition-colors">Blog</a>
            <a href="#" class="hover:text-[#F04B14] transition-colors">Contact</a>
        </nav>
        <div class="flex space-x-6 text-white/70">
            <a href="#" class="hover:text-[#F04B14] transition-colors">FB</a>
            <a href="#" class="hover:text-[#F04B14] transition-colors">X</a>
            <a href="#" class="hover:text-[#F04B14] transition-colors">IG</a>
            <a href="#" class="hover:text-[#F04B14] transition-colors">YT</a>
        </div>
        <a href="#" class="bg-[#F04B14] hover:bg-[#d83c0c] text-white px-8 py-4 rounded-full text-sm font-bold tracking-wide transition-all shadow-lg shadow-[#F04B14]/20 mt-4">
            Get In Touch
        </a>
    </div>

    <!-- Mobile Menu Script -->
    <script>
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const closeMenuBtn = document.getElementById('close-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');

        if(mobileMenuBtn && closeMenuBtn && mobileMenu) {
            mobileMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.remove('translate-x-full');
            });
            closeMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.add('translate-x-full');
            });
        }
    </script>
</body>'''
if '<!-- Mobile Menu Overlay -->' not in content:
    content = content.replace('</body>', mobile_menu)

# 3. Products Scroll Spy Mobile Sticky
old_sticky = '''class="w-full md:w-1/2 md:sticky md:top-0 h-[40vh] md:h-screen flex items-center justify-center p-4 md:p-8 z-10 pt-16 md:pt-0"'''
new_sticky = '''class="w-full md:w-1/2 sticky top-0 h-[35vh] md:h-screen flex items-center justify-center p-4 md:p-8 z-30 pt-4 md:pt-0 bg-[#2D2D2D]/95 md:bg-transparent backdrop-blur-md md:backdrop-blur-none border-b border-white/5 md:border-none"'''
content = content.replace(old_sticky, new_sticky)

# 4. Footer Columns
# Replace exactly the 4 occurrences
content = content.replace('<div class="lg:col-span-4 flex flex-col space-y-8">', '<div class="md:col-span-6 lg:col-span-3 flex flex-col space-y-8">')
content = content.replace('<div class="lg:col-span-4 flex flex-col space-y-6">', '<div class="md:col-span-6 lg:col-span-3 flex flex-col space-y-6">')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully.")
