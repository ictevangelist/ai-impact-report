/* Consent-first Google Analytics.
   Nothing loads and no cookies are set until the visitor accepts; the choice
   is remembered in localStorage and can be changed on the privacy page. */
(function () {
  "use strict";
  var KEY = "aigov-analytics-consent";
  var GA_ID = "G-Q6J9FDTD7Y";

  function getChoice() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function setChoice(v) {
    try { localStorage.setItem(KEY, v); } catch (e) {}
  }
  function clearChoice() {
    try { localStorage.removeItem(KEY); } catch (e) {}
  }

  function loadAnalytics() {
    if (window.__aigovGaLoaded) return;
    window.__aigovGaLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", GA_ID);
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_ID;
    document.head.appendChild(s);
  }

  function removeBanner() {
    var b = document.getElementById("consent-banner");
    if (b) b.parentNode.removeChild(b);
  }

  function showBanner() {
    if (document.getElementById("consent-banner")) return;
    var div = document.createElement("div");
    div.id = "consent-banner";
    div.className = "consent-banner";
    div.setAttribute("role", "region");
    div.setAttribute("aria-label", "Analytics choice");
    div.innerHTML =
      '<h2>A quick word about analytics</h2>' +
      '<p>I use Google Analytics to see which pages are helping people. It won’t run unless you’re happy for it to, and you can change your mind at any time on the <a href="/privacy/">privacy notice</a> page.</p>' +
      '<div class="consent-actions">' +
      '<button type="button" id="consent-accept">That’s fine</button>' +
      '<button type="button" id="consent-decline">No thanks</button>' +
      '</div>';
    document.body.appendChild(div);
    document.getElementById("consent-accept").addEventListener("click", function () {
      setChoice("granted");
      removeBanner();
      loadAnalytics();
      updateStatus();
    });
    document.getElementById("consent-decline").addEventListener("click", function () {
      setChoice("denied");
      removeBanner();
      updateStatus();
    });
  }

  function updateStatus() {
    var status = document.getElementById("consent-status");
    if (!status) return;
    var c = getChoice();
    status.textContent =
      c === "granted" ? "Your current choice in this browser: analytics is on." :
      c === "denied"  ? "Your current choice in this browser: analytics is off." :
                        "You haven’t made a choice in this browser yet.";
  }

  function init() {
    var c = getChoice();
    if (c === "granted") {
      loadAnalytics();
    } else if (c !== "denied") {
      showBanner();
    }
    updateStatus();
    var manage = document.getElementById("consent-manage");
    if (manage) {
      manage.addEventListener("click", function () {
        clearChoice();
        updateStatus();
        showBanner();
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
