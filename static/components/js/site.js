(() => {
    const menus = document.querySelectorAll('.site-nav-group');
    menus.forEach((menu) => {
        menu.addEventListener('toggle', () => {
            if (!menu.open) return;
            menus.forEach((other) => {
                if (other !== menu) other.open = false;
            });
        });
    });

    document.addEventListener('click', (event) => {
        if (event.target.closest('.site-nav')) return;
        menus.forEach((menu) => { menu.open = false; });
    });

    document.querySelectorAll('[data-carousel]').forEach((carousel) => {
        const slides = Array.from(carousel.querySelectorAll('.carousel-slide'));
        const previous = carousel.querySelector('[data-carousel-previous]');
        const next = carousel.querySelector('[data-carousel-next]');
        const pause = carousel.querySelector('[data-carousel-pause]');
        const position = carousel.querySelector('[data-carousel-position]');
        if (!slides.length) return;

        let activeIndex = Math.max(0, slides.findIndex((slide) => slide.classList.contains('is-active')));
        let userPaused = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        let videoPlaying = false;
        let timer = null;

        const render = (index) => {
            activeIndex = (index + slides.length) % slides.length;
            slides.forEach((slide, slideIndex) => {
                const active = slideIndex === activeIndex;
                slide.hidden = !active;
                slide.classList.toggle('is-active', active);
                slide.setAttribute('aria-hidden', String(!active));
                if (!active) slide.querySelectorAll('video').forEach((video) => video.pause());
            });
            if (position) position.textContent = `${activeIndex + 1} / ${slides.length}`;
        };

        const stopTimer = () => {
            if (timer) window.clearInterval(timer);
            timer = null;
        };
        const startTimer = () => {
            stopTimer();
            if (!userPaused && !videoPlaying && slides.length > 1) {
                timer = window.setInterval(() => render(activeIndex + 1), 6000);
            }
        };
        const syncPauseButton = () => {
            if (!pause) return;
            pause.setAttribute('aria-pressed', String(userPaused));
            pause.setAttribute('aria-label', userPaused ? 'Reprendre le carrousel' : 'Mettre le carrousel en pause');
            pause.innerHTML = userPaused
                ? '<i class="fa fa-play" aria-hidden="true"></i><span>Reprendre</span>'
                : '<i class="fa fa-pause" aria-hidden="true"></i><span>Pause</span>';
        };

        previous?.addEventListener('click', () => { render(activeIndex - 1); startTimer(); });
        next?.addEventListener('click', () => { render(activeIndex + 1); startTimer(); });
        pause?.addEventListener('click', () => {
            userPaused = !userPaused;
            syncPauseButton();
            startTimer();
        });
        carousel.addEventListener('mouseenter', stopTimer);
        carousel.addEventListener('mouseleave', startTimer);
        carousel.addEventListener('focusin', stopTimer);
        carousel.addEventListener('focusout', (event) => {
            if (!carousel.contains(event.relatedTarget)) startTimer();
        });
        slides.forEach((slide) => {
            slide.querySelectorAll('video').forEach((video) => {
                video.addEventListener('play', () => { videoPlaying = true; stopTimer(); });
                const resumeAfterVideo = () => { videoPlaying = false; startTimer(); };
                video.addEventListener('pause', resumeAfterVideo);
                video.addEventListener('ended', resumeAfterVideo);
            });
        });

        if (slides.length < 2) {
            if (previous) previous.disabled = true;
            if (next) next.disabled = true;
        }
        render(activeIndex);
        syncPauseButton();
        startTimer();
    });
})();
