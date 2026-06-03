(function () {
    const slider = document.querySelector('.slider');
    if (!slider) return;

    const slides = slider.querySelectorAll('.slider__slide');
    const dots = slider.querySelectorAll('.slider__dot');
    const prevBtn = slider.querySelector('.slider__btn--prev');
    const nextBtn = slider.querySelector('.slider__btn--next');
    const total = slides.length;
    let current = 0;
    let timer = null;
    const INTERVAL = 3000;

    function show(index) {
        current = (index + total) % total;
        slides.forEach((slide, i) => {
            slide.classList.toggle('is-active', i === current);
        });
        dots.forEach((dot, i) => {
            const active = i === current;
            dot.classList.toggle('is-active', active);
            dot.setAttribute('aria-selected', active ? 'true' : 'false');
        });
    }

    function next() {
        show(current + 1);
    }

    function prev() {
        show(current - 1);
    }

    function startAutoplay() {
        stopAutoplay();
        timer = setInterval(next, INTERVAL);
    }

    function stopAutoplay() {
        if (timer) {
            clearInterval(timer);
            timer = null;
        }
    }

    prevBtn.addEventListener('click', function () {
        prev();
        startAutoplay();
    });

    nextBtn.addEventListener('click', function () {
        next();
        startAutoplay();
    });

    dots.forEach(function (dot, i) {
        dot.addEventListener('click', function () {
            show(i);
            startAutoplay();
        });
    });

    slider.addEventListener('mouseenter', stopAutoplay);
    slider.addEventListener('mouseleave', startAutoplay);

    startAutoplay();
})();
