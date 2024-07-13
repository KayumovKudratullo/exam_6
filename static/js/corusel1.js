let currentIndexes = {};

function showSlide(carouselId, index) {
    const carouselInner = document.querySelector(`#reviews-${carouselId} .carousel-inner`);
    const slides = carouselInner.querySelectorAll('.carousel-item');
    
    if (!currentIndexes[carouselId]) {
        currentIndexes[carouselId] = 0;
    }
    
    if (index >= slides.length) {
        currentIndexes[carouselId] = 0;
    } else if (index < 0) {
        currentIndexes[carouselId] = slides.length - 1;
    } else {
        currentIndexes[carouselId] = index;
    }
    
    slides.forEach((slide, i) => {
        slide.classList.toggle('active', i === currentIndexes[carouselId]);
    });
}

function nextSlide(carouselId) {
    showSlide(carouselId, currentIndexes[carouselId] + 1);
}

function prevSlide(carouselId) {
    showSlide(carouselId, currentIndexes[carouselId] - 1);
}

// Initialize all carousels
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.reviews').forEach((carousel, index) => {
        showSlide(index + 1, 0);
    });
});
