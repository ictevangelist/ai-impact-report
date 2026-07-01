/* Header behaviour: waffle menu toggle + autohide-on-scroll. No dependencies. */
(function () {
  var header = document.querySelector('.site-header');
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (!header || !toggle || !nav) return;

  function isOpen() { return nav.classList.contains('open'); }
  function close() { nav.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); }
  function open() {
    header.classList.remove('is-hidden');
    nav.classList.add('open');
    toggle.setAttribute('aria-expanded', 'true');
  }

  toggle.addEventListener('click', function (e) {
    e.stopPropagation();
    isOpen() ? close() : open();
  });
  // Close when a section link is chosen
  nav.addEventListener('click', function (e) { if (e.target.closest('a')) close(); });
  // Close on outside click / Escape
  document.addEventListener('click', function (e) {
    if (isOpen() && !nav.contains(e.target) && !toggle.contains(e.target)) close();
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });

  // Autohide: hide header when scrolling down, reveal when scrolling up.
  var lastY = window.pageYOffset || 0;
  var ticking = false;
  function onScroll() {
    var y = window.pageYOffset || 0;
    if (isOpen()) { lastY = y; ticking = false; return; }
    if (y > 100 && y > lastY + 4) {
      header.classList.add('is-hidden');
    } else if (y < lastY - 4 || y <= 60) {
      header.classList.remove('is-hidden');
    }
    lastY = y;
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { window.requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
})();
