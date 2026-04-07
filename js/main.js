document.addEventListener('DOMContentLoaded', () => {
    // Header Scroll Effect
    const header = document.getElementById('header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileCloseBtn = document.getElementById('mobile-close-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileCloseBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.remove('translate-x-full');
            document.body.style.overflow = 'hidden';
        });

        mobileCloseBtn.addEventListener('click', () => {
            mobileMenu.classList.add('translate-x-full');
            document.body.style.overflow = '';
        });
    }

    // Mobile Menu Accordion
    const accordionBtns = document.querySelectorAll('.mobile-accordion-btn');
    accordionBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const content = btn.nextElementSibling;
            const icon = btn.querySelector('i');
            const iconWrapper = btn.querySelector('.icon-wrapper');
            
            if (content.classList.contains('hidden')) {
                content.classList.remove('hidden');
                icon.classList.remove('fa-plus');
                icon.classList.add('fa-minus');
                iconWrapper.classList.add('rotate-180');
            } else {
                content.classList.add('hidden');
                icon.classList.remove('fa-minus');
                icon.classList.add('fa-plus');
                iconWrapper.classList.remove('rotate-180');
            }
        });
    });

    // Intersection Observer for Fade-in Animations
    const fadeElements = document.querySelectorAll('.fade-in-up');
    if (fadeElements.length > 0) {
        const fadeObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    fadeObserver.unobserve(entry.target);
                }
            });
        }, {
            rootMargin: '0px 0px -100px 0px',
            threshold: 0.1
        });
        fadeElements.forEach(el => fadeObserver.observe(el));
    }

    // Intersection Observer for Counters
    const counters = document.querySelectorAll('.counter');
    if (counters.length > 0) {
        const speed = 150; // Animation speed

        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const speed = 100; // ステップ数（100 * 20ms = 2秒）
                    const target = +counter.getAttribute('data-target');
                    let currentCount = 0;
                    const inc = target / speed;

                    const updateCount = () => {
                        currentCount += inc;
                        if (currentCount < target) {
                            counter.innerText = Math.floor(currentCount);
                            setTimeout(updateCount, 20);
                        } else {
                            counter.innerText = target;
                        }
                    };
                    updateCount();
                    counterObserver.unobserve(counter);
                }
            });
        }, { threshold: 0.1 });
        counters.forEach(counter => counterObserver.observe(counter));
    }

    // Intersection Observer for Animated Underline
    const underlines = document.querySelectorAll('.border-b-gradient');
    if (underlines.length > 0) {
        const underlineObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // 要素がフェードインした後に線を引くよう、少し遅延させる
                    setTimeout(() => {
                        entry.target.classList.add('drawn');
                    }, 600);
                    underlineObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        underlines.forEach(underline => underlineObserver.observe(underline));
    }

    // Intersection Observer for Scroll Text Gradient
    const scrollTexts = document.querySelectorAll('.scroll-text-gradient');
    if (scrollTexts.length > 0) {
        const textObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    textObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        scrollTexts.forEach(text => textObserver.observe(text));
    }

    // Intersection Observer for Staggered Reveal
    const staggerReveals = document.querySelectorAll('.stagger-reveal');
    if (staggerReveals.length > 0) {
        const staggerObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    staggerObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        staggerReveals.forEach(el => staggerObserver.observe(el));
    }

    // EV Slider Logic (Carousel with scaling)
    const evSliderTrack = document.getElementById('ev-slider-track');
    const evSlides = document.querySelectorAll('.ev-carousel-slide');
    const evDots = document.querySelectorAll('.ev-dot');
    const evPrevBtn = document.getElementById('ev-prev');
    const evNextBtn = document.getElementById('ev-next');
    let evCurrentIndex = 0;
    let evSliderInterval;

    if (evSliderTrack && evSlides.length > 0) {
        const centerActiveSlide = (index) => {
            if (evSlides.length === 0) return;
            
            const ww = window.innerWidth;
            let activeVw, inactiveVw, gapPx;
            
            if (ww >= 1024) {
                // lg: w-[55vw] / w-[25vw], md:gap-8 (32px)
                activeVw = 55; inactiveVw = 25; gapPx = 32;
            } else if (ww >= 768) {
                // md: w-[65vw] / w-[30vw], md:gap-8 (32px)
                activeVw = 65; inactiveVw = 30; gapPx = 32;
            } else {
                // mobile: w-[80vw] / w-[50vw], gap-4 (16px)
                activeVw = 80; inactiveVw = 50; gapPx = 16;
            }
            
            const vwToPx = (vw) => (vw * ww) / 100;
            const activeWidth = vwToPx(activeVw);
            const inactiveWidth = vwToPx(inactiveVw);
            
            const leftWidth = index * inactiveWidth;
            const leftGaps = index * gapPx;
            
            const offset = (ww / 2) - leftWidth - leftGaps - (activeWidth / 2);
            evSliderTrack.style.transform = `translateX(${offset}px)`;
        };

        const updateEVSlider = (index) => {
            // Clamp index
            if (index < 0) index = evSlides.length - 1;
            if (index >= evSlides.length) index = 0;
            
            // Update active state class on slides (Width animation)
            evSlides.forEach((slide, i) => {
                if (i === index) {
                    slide.className = 'ev-carousel-slide flex-shrink-0 transition-all duration-700 ease-[cubic-bezier(0.25,1,0.5,1)] opacity-100 w-[80vw] md:w-[65vw] lg:w-[55vw] shadow-[0_4px_20px_rgba(0,0,0,0.08)] rounded-none relative z-10';
                } else {
                    slide.className = 'ev-carousel-slide flex-shrink-0 transition-all duration-700 ease-[cubic-bezier(0.25,1,0.5,1)] opacity-40 w-[50vw] md:w-[30vw] lg:w-[25vw] shadow-[0_4px_20px_rgba(0,0,0,0.08)] rounded-none relative z-0';
                }
            });

            // Update dots
            evDots.forEach((dot, i) => {
                if (i === index) {
                    dot.classList.remove('bg-gray-200', 'hover:bg-gray-300');
                    dot.classList.add('bg-main-gradient');
                } else {
                    dot.classList.remove('bg-main-gradient');
                    dot.classList.add('bg-gray-200', 'hover:bg-gray-300');
                }
            });

            centerActiveSlide(index);
            evCurrentIndex = index;
        };

        const startEVSlider = () => {
            clearInterval(evSliderInterval);
            evSliderInterval = setInterval(() => {
                const nextIndex = (evCurrentIndex + 1) % evSlides.length;
                updateEVSlider(nextIndex);
            }, 5000); 
        };

        // Resize observer to recenter on window resize
        window.addEventListener('resize', () => centerActiveSlide(evCurrentIndex));

        // Intersection Observer for Start EV Slider on Scroll
        const evSliderTarget = document.getElementById('ev-slider');
        if (evSliderTarget) {
            const evObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        // Center immediately as it enters view
                        updateEVSlider(0);
                        
                        // Wait a few seconds before starting the auto-slide interval
                        setTimeout(() => {
                            startEVSlider();
                        }, 3000);
                        
                        evObserver.unobserve(evSliderTarget);
                    }
                });
            }, { threshold: 0.1 });
            evObserver.observe(evSliderTarget);
        } else {
             updateEVSlider(0);
        }

        // Dot Navigation
        evDots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                updateEVSlider(index);
                startEVSlider(); // Reset timer
            });
        });

        // Prev/Next Navigation
        if (evPrevBtn) {
            evPrevBtn.addEventListener('click', () => {
                updateEVSlider(evCurrentIndex - 1);
                startEVSlider();
            });
        }
        if (evNextBtn) {
            evNextBtn.addEventListener('click', () => {
                updateEVSlider(evCurrentIndex + 1);
                startEVSlider();
            });
        }
    }
});
