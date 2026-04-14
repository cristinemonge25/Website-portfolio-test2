document.addEventListener('DOMContentLoaded', () => {
    const carousels = document.querySelectorAll('.carousel-wrapper');

    carousels.forEach(carousel => {
        const track = carousel.querySelector('.carousel-track');
        const slides = Array.from(track.children);
        const nextButton = carousel.querySelector('.carousel-next');
        const prevButton = carousel.querySelector('.carousel-prev');

        let currentIndex = 0;

        const updateSlidePosition = () => {
            track.style.transform = `translateX(-${currentIndex * 100}%)`;
            
            // Handle disabled state for buttons
            if (currentIndex === 0) {
                prevButton.classList.add('disabled');
            } else {
                prevButton.classList.remove('disabled');
            }
            
            if (currentIndex === slides.length - 1) {
                nextButton.classList.add('disabled');
            } else {
                nextButton.classList.remove('disabled');
            }
        };

        // Initialize button states
        updateSlidePosition();

        // View Toggle Logic
        const btnCarousel = document.getElementById('btn-carousel');
        const btnScroll = document.getElementById('btn-scroll');

        if (btnCarousel && btnScroll) {
            btnCarousel.addEventListener('click', () => {
                carousel.classList.remove('scroll-mode');
                btnCarousel.classList.add('active');
                btnScroll.classList.remove('active');
                // Recalculate transform
                updateSlidePosition();
            });

            btnScroll.addEventListener('click', () => {
                carousel.classList.add('scroll-mode');
                btnScroll.classList.add('active');
                btnCarousel.classList.remove('active');
                track.style.transform = ''; // Clear inline transform so CSS overrides work
            });
        }

        nextButton.addEventListener('click', () => {
            if (currentIndex < slides.length - 1) {
                currentIndex++;
                updateSlidePosition();
            }
        });

        prevButton.addEventListener('click', () => {
            if (currentIndex > 0) {
                currentIndex--;
                updateSlidePosition();
            }
        });
        
        // Ensure slides resize correctly when window is resized
        window.addEventListener('resize', () => {
            updateSlidePosition();
        });
    });
});
