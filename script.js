document.querySelectorAll('.faq-item').forEach(item => {
    item.addEventListener('click', () => {
        const content = item.querySelector('.faq-content');
        const arrow = item.querySelector('.arrow-icon');
        const heading = item.querySelector('.faq-heading');

        // Check if current item is open
        const isOpen = content.style.maxHeight && content.style.maxHeight !== '0px';

        // Close all items safely
        document.querySelectorAll('.faq-content').forEach(c => c.style.maxHeight = null);
        document.querySelectorAll('.arrow-icon').forEach(a => {
            a.classList.remove('rotate-180', 'text-[#00A1FF]');
            a.classList.add('text-gray-400');
        });
        document.querySelectorAll('.faq-heading').forEach(h => {
            h.classList.remove('text-[#00A1FF]');
            if (!h.closest('.group')) {
                h.classList.add('text-white');
            }
        });

        // Toggle selected element nodes if it wasn't open
        if (!isOpen) {
            content.style.maxHeight = content.scrollHeight + "px";
            arrow.classList.add('rotate-180', 'text-[#00A1FF]');
            heading.classList.add('text-[#00A1FF]');
        }
    });
});


// Dynamic Hero Background Images (3-Image Carousel)
const heroImages = [
    './images/bg3.webp',
    './images/bg4.webp',
    './images/bg5.webp'
];

let currentHeroImageIndex = 0;
const heroSection = document.getElementById('hero-section');
const heroDotsContainer = document.getElementById('hero-dots');

function updateHeroImage(index) {
    if (!heroSection) return;
    currentHeroImageIndex = index;
    heroSection.style.backgroundImage = `url('${heroImages[currentHeroImageIndex]}')`;
    
    // Update active dot indicator styling
    if (heroDotsContainer) {
        const dots = heroDotsContainer.querySelectorAll('.hero-dot');
        dots.forEach((dot, i) => {
            if (i === currentHeroImageIndex) {
                dot.classList.remove('opacity-40');
                dot.classList.add('opacity-100', 'scale-125');
            } else {
                dot.classList.add('opacity-40');
                dot.classList.remove('opacity-100', 'scale-125');
            }
        });
    }
}

if (heroSection) {
    // Preload images to prevent flickering
    heroImages.forEach(src => {
        const img = new Image();
        img.src = src;
    });

    // Create dot indicators dynamically for 3 images
    if (heroDotsContainer) {
        heroDotsContainer.innerHTML = '';
        heroImages.forEach((_, i) => {
            const dot = document.createElement('span');
            dot.className = `w-2.5 h-2.5 rounded-full bg-white ${i === 0 ? 'opacity-100 scale-125' : 'opacity-40'} hover:opacity-100 cursor-pointer transition-all duration-300 hero-dot`;
            dot.addEventListener('click', () => {
                updateHeroImage(i);
            });
            heroDotsContainer.appendChild(dot);
        });
    }

    setInterval(() => {
        const nextIndex = (currentHeroImageIndex + 1) % heroImages.length;
        updateHeroImage(nextIndex);
    }, 4500); // Change image every 4.5 seconds
}
