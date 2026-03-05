document.addEventListener('DOMContentLoaded', () => {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ─── GSAP SETUP ───────────────────────────────────────────────
  gsap.registerPlugin(ScrollTrigger);

  // ─── NAVIGATION: transparent → scrolled ───────────────────────
  const nav = document.getElementById('site-nav');
  if (nav) {
    ScrollTrigger.create({
      start: 'top -80',
      onUpdate: (self) => {
        nav.classList.toggle('scrolled', self.scroll() > 80);
      }
    });
  }

  // ─── MOBILE NAV TOGGLE ─────────────────────────────────────────
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.getElementById('nav-menu');
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      const isOpen = navMenu.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', String(isOpen));
    });
    navMenu.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('is-open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  if (!prefersReducedMotion) {
    // ─── HERO ANIMATIONS (on load) ─────────────────────────────────
    const heroTl = gsap.timeline();
    heroTl
      .from('.hero__tagline',     { opacity: 0, duration: 0.8, ease: 'power2.out' })
      .from('.hero__title',       { opacity: 0, y: 40, duration: 1.2, ease: 'power3.out' }, '-=0.4')
      .from('.hero__subtitle',    { opacity: 0, y: 20, duration: 1, ease: 'power3.out' }, '-=0.7')
      .from('.hero__institution', { opacity: 0, duration: 0.6, ease: 'power2.out' }, '-=0.5')
      .from('.scroll-cue',        { opacity: 0, duration: 0.5, ease: 'power2.out' }, '-=0.3');

    // ─── HERO BACKGROUND PARALLAX ──────────────────────────────────
    const heroBg = document.querySelector('.hero-bg');
    if (heroBg) {
      gsap.to(heroBg, {
        yPercent: 30,
        ease: 'none',
        scrollTrigger: {
          trigger: '.hero',
          start: 'top top',
          end: 'bottom top',
          scrub: true
        }
      });
    }

    // ─── HERO BACKGROUND KEN BURNS ─────────────────────────────────
    if (heroBg) {
      gsap.from(heroBg, { scale: 1.06, duration: 8, ease: 'power1.out' });
    }

    // ─── GLOBAL REVEAL (.reveal elements) ──────────────────────────
    document.querySelectorAll('.reveal').forEach(el => {
      gsap.from(el, {
        opacity: 0,
        y: 40,
        duration: 0.9,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 88%',
          toggleActions: 'play none none none'
        }
      });
    });

    // ─── STAGGER CHILDREN (.stagger-children containers) ──────────
    document.querySelectorAll('.stagger-children').forEach(container => {
      gsap.from(Array.from(container.children), {
        opacity: 0,
        y: 40,
        duration: 0.7,
        ease: 'power2.out',
        stagger: 0.12,
        scrollTrigger: {
          trigger: container,
          start: 'top 80%',
          toggleActions: 'play none none none'
        }
      });
    });

    // ─── TIMELINE DOTS DRAW IN ─────────────────────────────────────
    const timelineItems = document.querySelectorAll('.timeline-item');
    if (timelineItems.length > 0) {
      gsap.from(timelineItems, {
        opacity: 0,
        x: -20,
        duration: 0.5,
        ease: 'power2.out',
        stagger: 0.1,
        scrollTrigger: {
          trigger: '.timeline',
          start: 'top 80%',
          toggleActions: 'play none none none'
        }
      });
    }

    // ─── EXPULSION NUMBER COUNTERS ─────────────────────────────────
    const statEls = document.querySelectorAll('.stat-number[data-target]');
    if (statEls.length > 0) {
      ScrollTrigger.create({
        trigger: '.expulsion-stats',
        start: 'top 70%',
        once: true,
        onEnter: () => animateCounters(statEls)
      });
    }

    // ─── MAP PANELS PARALLAX ───────────────────────────────────────
    document.querySelectorAll('.map-panel').forEach(panel => {
      const img = panel.querySelector('.map-panel__img');
      if (img) {
        gsap.to(img, {
          yPercent: -15,
          ease: 'none',
          scrollTrigger: {
            trigger: panel,
            start: 'top bottom',
            end: 'bottom top',
            scrub: true
          }
        });
      }
    });

    // ─── EXPULSION BACKGROUND PARALLAX ────────────────────────────
    const expulsionBg = document.querySelector('.expulsion-bg');
    if (expulsionBg) {
      gsap.to(expulsionBg, {
        yPercent: -25,
        ease: 'none',
        scrollTrigger: {
          trigger: '.expulsion-section',
          start: 'top bottom',
          end: 'bottom top',
          scrub: true
        }
      });
    }

    // ─── STRATEGIES QUADRANT ENTRY ─────────────────────────────────
    const quadrants = document.querySelectorAll('.strategy-quadrant');
    if (quadrants.length === 4) {
      const directions = [
        { x: -60, y: -40 },
        { x:  60, y: -40 },
        { x: -60, y:  40 },
        { x:  60, y:  40 }
      ];
      quadrants.forEach((q, i) => {
        gsap.from(q, {
          opacity: 0,
          x: directions[i].x,
          y: directions[i].y,
          duration: 0.8,
          ease: 'power3.out',
          scrollTrigger: {
            trigger: '#strategies',
            start: 'top 70%',
            toggleActions: 'play none none none'
          }
        });
      });
    }

    // ─── CHAPTER IMAGE SUBTLE PARALLAX ────────────────────────────
    document.querySelectorAll('.chapter-image img').forEach(img => {
      gsap.to(img, {
        yPercent: -10,
        ease: 'none',
        scrollTrigger: {
          trigger: img.closest('.chapter-section'),
          start: 'top bottom',
          end: 'bottom top',
          scrub: true
        }
      });
    });

  } // end if (!prefersReducedMotion)

  // ─── COUNTER ANIMATION ─────────────────────────────────────────
  function animateCounters(els) {
    els.forEach(el => {
      const target = parseInt(el.dataset.target, 10);
      const duration = 1800;
      const startTime = performance.now();

      function step(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        const current = Math.round(eased * target);

        if (target >= 10000) {
          el.textContent = '~' + current.toLocaleString();
        } else {
          el.textContent = current;
        }

        if (progress < 1) {
          requestAnimationFrame(step);
        }
      }
      requestAnimationFrame(step);
    });
  }

  // ─── ACTIVE NAV LINK HIGHLIGHTING ────────────────────────────
  const sections = document.querySelectorAll('section[id]');
  if (sections.length > 0) {
    sections.forEach(section => {
      ScrollTrigger.create({
        trigger: section,
        start: 'top 50%',
        end: 'bottom 50%',
        onEnter: () => updateActiveSection(section.id),
        onEnterBack: () => updateActiveSection(section.id)
      });
    });
  }

  function updateActiveSection(id) {
    // No per-section nav highlighting needed beyond what aria-current handles
  }

});
