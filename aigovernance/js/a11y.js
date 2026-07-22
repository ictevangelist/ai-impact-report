/* =====================================================================
   Reading controls + listen-aloud — AI Governance in Education (ICT Evangelist)
   UDL "multiple means of representation & expression": lets each visitor
   adjust text size, contrast and spacing, and hear the page read aloud.
   Preferences are saved in localStorage on the visitor's own device.
   No external requests; speech uses the browser's built-in synthesiser.
   ===================================================================== */
(function () {
  var DOC = document.documentElement;
  var KEY = { size: 'aig-a11y-size', contrast: 'aig-a11y-contrast', spacing: 'aig-a11y-spacing' };
  var SIZES = ['100%', '110%', '120%', '130%'];

  function get(k, d) { try { var v = localStorage.getItem(k); return v === null ? d : v; } catch (e) { return d; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  var sizeStep = Math.max(0, Math.min(SIZES.length - 1, parseInt(get(KEY.size, '0'), 10) || 0));
  var contrastOn = get(KEY.contrast, '0') === '1';
  var spacingOn = get(KEY.spacing, '0') === '1';

  function apply() {
    DOC.style.fontSize = SIZES[sizeStep];
    DOC.classList.toggle('a11y-contrast', contrastOn);
    DOC.classList.toggle('a11y-spacing', spacingOn);
  }
  apply(); // apply saved prefs as early as possible

  /* ---------- Build the widget ---------- */
  function el(tag, attrs, html) {
    var e = document.createElement(tag);
    if (attrs) for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (html != null) e.innerHTML = html;
    return e;
  }

  var ACCESS_ICON = '<svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false" fill="currentColor"><circle cx="12" cy="4" r="2"/><path d="M12 7c-3 0-6 .6-6 .6a1 1 0 0 0 .3 2s2-.3 3.4-.5V13l-1.8 6.3a1 1 0 0 0 1.9.6L11.6 15h.8l1.8 5a1 1 0 0 0 1.9-.6L14.3 9.1c1.4.2 3.4.5 3.4.5a1 1 0 1 0 .3-2S15 7 12 7z"/></svg>';

  var fab = el('button', {
    'class': 'a11y-fab', 'id': 'a11yFab', 'aria-expanded': 'false',
    'aria-controls': 'a11yPanel', 'aria-label': 'Accessibility and reading controls'
  }, ACCESS_ICON);

  var panel = el('div', { 'class': 'a11y-panel', 'id': 'a11yPanel', 'role': 'group', 'aria-label': 'Reading controls', 'hidden': '' });
  panel.innerHTML =
    '<h2 class="a11y-panel__title">Reading controls</h2>' +
    '<div class="a11y-row"><span class="a11y-row__label" id="a11yTextLbl">Text size</span>' +
      '<div class="a11y-btns" role="group" aria-labelledby="a11yTextLbl">' +
        '<button type="button" class="a11y-ctl" data-act="text-dec" aria-label="Decrease text size">A&minus;</button>' +
        '<span class="a11y-size-ind" id="a11ySizeInd" aria-live="polite">100%</span>' +
        '<button type="button" class="a11y-ctl" data-act="text-inc" aria-label="Increase text size">A+</button>' +
      '</div></div>' +
    '<div class="a11y-row"><span class="a11y-row__label">High contrast</span>' +
      '<button type="button" class="a11y-toggle" data-act="contrast" aria-pressed="false">Off</button></div>' +
    '<div class="a11y-row"><span class="a11y-row__label">Extra spacing</span>' +
      '<button type="button" class="a11y-toggle" data-act="spacing" aria-pressed="false">Off</button></div>' +
    '<div class="a11y-row"><span class="a11y-row__label">Listen to this page</span>' +
      '<button type="button" class="a11y-toggle" data-act="listen" aria-pressed="false">Play</button></div>' +
    '<button type="button" class="a11y-reset" data-act="reset">Reset all</button>' +
    '<p class="a11y-note">Preferences are saved on your device only. <a href="/privacy/">Privacy notice</a>.</p>';

  var wrap = el('div', { 'class': 'a11y-widget' });
  wrap.appendChild(panel);
  wrap.appendChild(fab);
  document.body.appendChild(wrap);

  /* ---------- Reflect state into the controls ---------- */
  var sizeInd = panel.querySelector('#a11ySizeInd');
  function refresh() {
    sizeInd.textContent = SIZES[sizeStep];
    var c = panel.querySelector('[data-act="contrast"]');
    c.setAttribute('aria-pressed', contrastOn ? 'true' : 'false'); c.textContent = contrastOn ? 'On' : 'Off';
    var s = panel.querySelector('[data-act="spacing"]');
    s.setAttribute('aria-pressed', spacingOn ? 'true' : 'false'); s.textContent = spacingOn ? 'On' : 'Off';
  }
  refresh();

  /* ---------- Open / close ---------- */
  function openPanel() { panel.hidden = false; fab.setAttribute('aria-expanded', 'true'); }
  function closePanel(focusBack) { panel.hidden = true; fab.setAttribute('aria-expanded', 'false'); if (focusBack) fab.focus(); }
  fab.addEventListener('click', function (e) { e.stopPropagation(); panel.hidden ? openPanel() : closePanel(false); });
  document.addEventListener('click', function (e) { if (!panel.hidden && !wrap.contains(e.target)) closePanel(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !panel.hidden) closePanel(true); });

  /* ---------- Listen aloud (Web Speech API, on-device) ---------- */
  var synth = window.speechSynthesis;
  var speaking = false, keepAlive = null;
  function listenBtn() { return panel.querySelector('[data-act="listen"]'); }
  function setListen(on) {
    var b = listenBtn();
    b.setAttribute('aria-pressed', on ? 'true' : 'false');
    b.textContent = on ? 'Stop' : 'Play';
    speaking = on;
  }
  function stopSpeech() {
    if (synth) synth.cancel();
    if (keepAlive) { clearInterval(keepAlive); keepAlive = null; }
    setListen(false);
  }
  function startSpeech() {
    if (!synth) return;
    synth.cancel();
    var main = document.getElementById('main') || document.body;
    var nodes = main.querySelectorAll('h1, h2, h3, h4, p, li, blockquote, cite, figcaption, caption, th, td');
    var blocks = [];
    nodes.forEach(function (n) {
      if (n.closest('.a11y-widget')) return;
      var t = (n.innerText || n.textContent || '').replace(/\s+/g, ' ').trim();
      if (t) blocks.push(t);
    });
    if (!blocks.length) return;
    setListen(true);
    blocks.forEach(function (t, i) {
      var u = new SpeechSynthesisUtterance(t);
      u.lang = 'en-GB'; u.rate = 1;
      if (i === blocks.length - 1) u.onend = function () { stopSpeech(); };
      synth.speak(u);
    });
    // Chrome pauses long queues; nudge it to keep going.
    keepAlive = setInterval(function () { if (synth.speaking) { synth.pause(); synth.resume(); } }, 9000);
  }

  /* ---------- Control actions ---------- */
  panel.addEventListener('click', function (e) {
    var btn = e.target.closest('[data-act]'); if (!btn) return;
    switch (btn.getAttribute('data-act')) {
      case 'text-inc': sizeStep = Math.min(SIZES.length - 1, sizeStep + 1); set(KEY.size, sizeStep); apply(); refresh(); break;
      case 'text-dec': sizeStep = Math.max(0, sizeStep - 1); set(KEY.size, sizeStep); apply(); refresh(); break;
      case 'contrast': contrastOn = !contrastOn; set(KEY.contrast, contrastOn ? '1' : '0'); apply(); refresh(); break;
      case 'spacing': spacingOn = !spacingOn; set(KEY.spacing, spacingOn ? '1' : '0'); apply(); refresh(); break;
      case 'listen': speaking ? stopSpeech() : startSpeech(); break;
      case 'reset':
        sizeStep = 0; contrastOn = false; spacingOn = false;
        set(KEY.size, 0); set(KEY.contrast, '0'); set(KEY.spacing, '0');
        stopSpeech(); apply(); refresh();
        break;
    }
  });

  // Hide the Listen control if the browser has no speech synthesis.
  if (!('speechSynthesis' in window)) {
    var lb = listenBtn(); if (lb) lb.closest('.a11y-row').style.display = 'none';
  }
  // Stop speech if the page is left.
  window.addEventListener('beforeunload', function () { if (synth) synth.cancel(); });
})();
