document.addEventListener('DOMContentLoaded', function() {
  // Burger Menu Logic
  const burger = document.querySelector('.burger');
  const navLinks = document.querySelector('.nav-links');
  const closeIcon = document.querySelector('.close-icon');

  burger.addEventListener('click', toggleNav);
  closeIcon.addEventListener('click', closeNav);
  window.addEventListener('resize', closeNavOnResize);

  function toggleNav() {
      navLinks.classList.toggle('nav-active');
      closeIcon.style.display = navLinks.classList.contains('nav-active') ? "block" : "none";
      burger.classList.toggle('toggle');
  }

  function closeNav() {
      navLinks.classList.remove('nav-active');
      closeIcon.style.display = "none";
      burger.classList.remove('toggle');
  }

  function closeNavOnResize() {
      if (window.innerWidth > 768) {
          closeNav();
      }
  }
    // Cookie Consent Banner Logic
    const cookieBanner = document.getElementById('cookie-consent-banner');
    const acceptButton = document.getElementById('accept-cookies');
    const rejectButton = document.getElementById('reject-cookies');

    function checkCookieConsent() {
        let cookieConsent = localStorage.getItem('cookieConsent');
        if (cookieConsent === 'accepted') {
            loadGoogleAnalytics();
            cookieBanner.classList.add('cookie-banner-hidden');
        } else {
            cookieBanner.classList.remove('cookie-banner-hidden');
        }
    }

    acceptButton.addEventListener('click', function() {
        localStorage.setItem('cookieConsent', 'accepted');
        loadGoogleAnalytics();
        cookieBanner.classList.add('cookie-banner-hidden');
    });

    rejectButton.addEventListener('click', function() {
        localStorage.setItem('cookieConsent', 'rejected');
        cookieBanner.classList.add('cookie-banner-hidden');
    });

    function loadGoogleAnalytics() {
      window.dataLayer = window.dataLayer || [];
      function gtag() { dataLayer.push(arguments); }
      gtag('js', new Date());
      gtag('config', '');

      var gaScript = document.createElement('script');
      gaScript.async = true;
      gaScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-W1MPRTMY0G';
      document.head.appendChild(gaScript);
    }

    // Esegui il controllo al caricamento della pagina
    checkCookieConsent();
});