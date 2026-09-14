// Preloader Logic
const preloader = document.querySelector('.preloader');
const loadingPercentage = document.querySelector('.loading-percentage');
const loadingBar = document.querySelector('.loading-bar');
let progress = 0;

if (preloader) {
    // Disable scrolling while loading
    document.body.style.overflow = 'hidden';

    // Simulate loading progress
    const simulateLoading = setInterval(() => {
        // Random increment for a more organic feel
        const increment = Math.floor(Math.random() * 5) + 1;
        progress += increment;

        if (progress > 90) {
            // Hold at 90-99% until window is fully loaded
            progress = 90 + Math.floor(Math.random() * 9);
        }

        updateProgress(progress);
    }, 100);

    function updateProgress(value) {
        if (loadingPercentage) loadingPercentage.textContent = `${value}%`;
        if (loadingBar) loadingBar.style.width = `${value}%`;
    }

    // When window actually loads, force to 100% and fade out
    window.addEventListener('load', () => {
        clearInterval(simulateLoading);
        updateProgress(100);

        setTimeout(() => {
            preloader.classList.add('fade-out');
            document.body.style.overflow = ''; // Restore scrolling

            // Optional: remove preloader from DOM after fade out to keep it clean
            setTimeout(() => {
                preloader.remove();
            }, 800);
        }, 500); // Short delay at 100% for visual satisfaction
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const prevBtn = document.querySelector('.nav-arrow.prev');
    const nextBtn = document.querySelector('.nav-arrow.next');
    const heroWrapper = document.querySelector('.hero-wrapper');

    // Slider
    const images = [
        'linear-gradient(rgba(15, 15, 15, 0.4), rgba(15, 15, 15, 0.6)), url("./img/slide/slide1.jpg")',
        'linear-gradient(rgba(15, 15, 15, 0.4), rgba(15, 15, 15, 0.6)), url("./img/slide/slide2.jpg")',
        'linear-gradient(rgba(15, 15, 15, 0.4), rgba(15, 15, 15, 0.6)), url("./img/slide/slide3.jpg")'
    ];

    let currentIndex = 0;

    // Drag/Swipe Variables
    let isDragging = false;
    let startPos = 0;
    let currentTranslate = 0;
    const threshold = 100; // minimum distance in pixels to trigger a slide

    function updateBackground() {
        heroWrapper.style.backgroundImage = images[currentIndex];
        heroWrapper.style.transition = 'background-image 0.5s ease-in-out';
    }

    function slideNext() {
        currentIndex = (currentIndex + 1) % images.length;
        updateBackground();
    }

    function slidePrev() {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateBackground();
    }

    if (nextBtn) nextBtn.addEventListener('click', slideNext);
    if (prevBtn) prevBtn.addEventListener('click', slidePrev);

    // Drag events for mouse and touch
    function dragStart(e) {
        if (e.target.closest('.nav-arrow') || e.target.closest('.primary-btn') || e.target.closest('.outline-btn')) return;
        isDragging = true;
        startPos = getPositionX(e);
        heroWrapper.classList.add('grabbing');
    }

    function dragMove(e) {
        if (!isDragging) return;
        const currentPosition = getPositionX(e);
        currentTranslate = currentPosition - startPos;
    }

    function dragEnd() {
        if (!isDragging) return;
        isDragging = false;
        heroWrapper.classList.remove('grabbing');

        if (currentTranslate < -threshold) {
            slideNext();
        } else if (currentTranslate > threshold) {
            slidePrev();
        }
        currentTranslate = 0;
    }

    function getPositionX(e) {
        return e.type.includes('mouse') ? e.pageX : e.touches[0].clientX;
    }

    // Touch events
    heroWrapper.addEventListener('touchstart', dragStart);
    heroWrapper.addEventListener('touchmove', dragMove);
    heroWrapper.addEventListener('touchend', dragEnd);

    // Mouse events
    heroWrapper.addEventListener('mousedown', dragStart);
    heroWrapper.addEventListener('mousemove', dragMove);
    heroWrapper.addEventListener('mouseup', dragEnd);
    heroWrapper.addEventListener('mouseleave', dragEnd);

    // Custom Gallery JS removed to use Bootstrap Carousel

    // Make Bootstrap Carousels Draggable
    function makeCarouselDraggable(carouselId, excludeSelectors = []) {
        const carouselElement = document.querySelector(carouselId);
        if (!carouselElement) return;

        let isDragging = false;
        let startX = 0;
        let currentTranslate = 0;
        const dragThreshold = 50;
        const carouselInner = carouselElement.querySelector('.carousel-inner');

        carouselElement.addEventListener('mousedown', (e) => {
            // Prevent drag if clicking on specified controls
            if (excludeSelectors.some(selector => e.target.closest(selector))) return;

            isDragging = true;
            startX = e.pageX;
            carouselElement.style.cursor = 'grabbing';
            carouselElement.style.userSelect = 'none'; // Prevent selection lag
            carouselInner.style.transition = 'none'; // Disable transition for instant drag
            e.preventDefault(); // Prevent default image dragging
        });

        carouselElement.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            currentTranslate = e.pageX - startX;
            // Smoothly move the track following the mouse
            carouselInner.style.transform = `translateX(${currentTranslate}px)`;
        });

        const handleDragEnd = () => {
            if (!isDragging) return;
            isDragging = false;
            carouselElement.style.cursor = '';
            carouselElement.style.userSelect = '';

            const carousel = bootstrap.Carousel.getInstance(carouselElement) || new bootstrap.Carousel(carouselElement);

            // Smoothly animate the physical snap-back exactly alongside Bootstrap's slide transition
            carouselInner.style.transition = 'transform 0.6s ease-in-out';
            carouselInner.style.transform = 'translateX(0px)';

            if (currentTranslate < -dragThreshold) {
                carousel.next();
            } else if (currentTranslate > dragThreshold) {
                carousel.prev();
            }

            // Clean up transition property after it finishes
            setTimeout(() => {
                carouselInner.style.transition = '';
            }, 600);

            currentTranslate = 0;
        };

        carouselElement.addEventListener('mouseup', handleDragEnd);
        carouselElement.addEventListener('mouseleave', handleDragEnd);
    }

    makeCarouselDraggable('#galleryCarousel', ['.gallery-nav', '.gallery-pagination']);
    makeCarouselDraggable('#roomsCarouselDesktop', ['.room-nav-arrows', '.intro-pagination', '.favorite-btn']);
    makeCarouselDraggable('#roomsCarouselMobile', ['.room-nav-arrows', '.favorite-btn']);

    // Sticky Header
    const mainHeader = document.querySelector('.main-header');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            mainHeader.classList.add('sticky');
        } else {
            mainHeader.classList.remove('sticky');
        }
    });

    // Mobile Menu Toggle
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (mobileMenuToggle && mainNav) {
        mobileMenuToggle.addEventListener('click', () => {
            mainNav.classList.toggle('active');
        });

        // Close menu when a link is clicked
        const navLinks = mainNav.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                mainNav.classList.remove('active');
            });
        });
    }
});
