document.querySelectorAll('.faq-item').forEach(item => {
    item.addEventListener('click', () => {
        const content = item.querySelector('.faq-content');
        const arrow = item.querySelector('.arrow-icon');
        const heading = item.querySelector('.faq-heading');

        // Check if current item is open
        const isOpen = content.style.maxHeight && content.style.maxHeight !== '0px';

        // Close all items safely
        document.querySelectorAll('.faq-content').forEach(c => c.style.maxHeight = '0px');
        document.querySelectorAll('.arrow-icon').forEach(a => {
            a.classList.remove('rotate-180', 'text-[#F04B14]');
            a.classList.add('text-gray-400');
        });
        document.querySelectorAll('.faq-heading').forEach(h => {
            h.classList.remove('text-[#F04B14]');
            if (!h.closest('.group')) {
                h.classList.add('text-white');
            }
        });

        // Toggle selected element nodes if it wasn't open
        if (!isOpen) {
            content.style.maxHeight = content.scrollHeight + "px";
            arrow.classList.add('rotate-180', 'text-[#F04B14]');
            heading.classList.add('text-[#F04B14]');
        }
    });
});


// Dynamic Hero Background Images
const heroImages = [
    './images/herobg1.jpg',
    './images/herobg2.jpg',
    './images/herobg3.jpg'
];

let currentHeroImageIndex = 0;
const heroSection = document.getElementById('hero-section');

if (heroSection) {
    // Preload images to prevent flickering
    heroImages.forEach(src => {
        const img = new Image();
        img.src = src;
    });

    setInterval(() => {
        currentHeroImageIndex = (currentHeroImageIndex + 1) % heroImages.length;
        heroSection.style.backgroundImage = `url('${heroImages[currentHeroImageIndex]}')`;
    }, 4500); // Change image every 4.5 seconds
}
