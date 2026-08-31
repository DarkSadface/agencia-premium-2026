/**
 * safe-animations.js
 * Safe GSAP animations for elegant fade-ins and scroll-reveals.
 * Designed to avoid DOM breakage and opacity conflicts.
 * 
 * Dependencies (include in HTML before this file):
 * - GSAP core: <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
 * - ScrollTrigger: <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
 */

document.addEventListener('DOMContentLoaded', () => {
    // Remove fallback class since JS is running
    document.documentElement.classList.remove('no-js');
  
    // Safety check: verify GSAP is loaded
    if (typeof gsap === 'undefined') {
      console.warn('safe-animations.js: GSAP is not loaded. Falling back to making all elements visible.');
      document.querySelectorAll('.gsap-reveal, .gsap-fade-in').forEach(el => {
        el.style.opacity = '1';
        el.style.visibility = 'visible';
      });
      return;
    }
  
    // Register ScrollTrigger if available
    const hasScrollTrigger = typeof ScrollTrigger !== 'undefined';
    if (hasScrollTrigger) {
      gsap.registerPlugin(ScrollTrigger);
    } else {
      console.warn('safe-animations.js: ScrollTrigger is not loaded. Animations will play immediately on load.');
    }
  
    const initAnimations = () => {
      // 1. Reveal Up Animation (.gsap-reveal)
      const revealElements = document.querySelectorAll('.gsap-reveal');
      revealElements.forEach((el) => {
        // Use autoAlpha for better performance and visibility handling
        gsap.set(el, { autoAlpha: 0, y: 40 });
        
        const config = {
          autoAlpha: 1,
          y: 0,
          duration: 0.9,
          ease: 'power3.out',
          clearProps: 'transform', // Clean up transform property after animation to avoid z-index/layout issues
        };
  
        if (hasScrollTrigger) {
          gsap.to(el, {
            ...config,
            scrollTrigger: {
              trigger: el,
              start: 'top 85%', // Triggers when top of element reaches 85% of viewport
              toggleActions: 'play none none none' // Play once, don't reverse
            }
          });
        } else {
          gsap.to(el, config);
        }
      });
  
      // 2. Simple Fade In Animation (.gsap-fade-in)
      const fadeElements = document.querySelectorAll('.gsap-fade-in');
      fadeElements.forEach((el) => {
        gsap.set(el, { autoAlpha: 0 });
        
        const config = {
          autoAlpha: 1,
          duration: 1.2,
          ease: 'power2.inOut',
        };
  
        if (hasScrollTrigger) {
          gsap.to(el, {
            ...config,
            scrollTrigger: {
              trigger: el,
              start: 'top 90%',
              toggleActions: 'play none none none'
            }
          });
        } else {
          gsap.to(el, config);
        }
      });
    };
  
    // Wrap in requestAnimationFrame to ensure the browser has parsed and painted the initial layout
    requestAnimationFrame(() => {
      initAnimations();
    });
  });
