#!/usr/bin/env python3
# =====================================================================
# Static-site generator for aigovernance.ictevangelist.com
# Companion mini-site to the "Use of AI Policy" template (ICT Evangelist).
# Emits self-contained static HTML using the shared kit (css/js/assets).
# Run:  python3 build.py    (writes *.html into this folder)
# =====================================================================
import html, pathlib, json

SITE = "https://aigovernance.ictevangelist.com"
BRAND_TITLE = "AI Governance in Education"
BRAND_SUB = "ICT Evangelist"
AUTHOR = "Mark Anderson (ICT Evangelist)"
OUT = pathlib.Path(__file__).parent

# Content fingerprint for cache-busting: changes whenever css/js change, so
# GitHub Pages' 10-minute asset cache can never serve stale styles.
import hashlib as _hashlib
ASSET_V = _hashlib.md5(b"".join(
    (OUT / p).read_bytes() for p in ("css/styles.css", "js/nav.js", "js/a11y.js", "js/consent.js")
)).hexdigest()[:8]

# ---- Navigation: the waffle grid (topic pages, in reading order) ----
NAV = [
    ("landscape.html",          "The landscape"),
    ("roles.html",              "Roles & oversight"),
    ("approved-tools.html",     "Approved tools"),
    ("acceptable-use.html",     "Acceptable use"),
    ("data-protection.html",    "Data protection"),
    ("accuracy-oversight.html", "Accuracy & oversight"),
    ("safeguarding.html",       "Safeguarding & Prevent"),
    ("impact-assessment.html",  "Impact assessment"),
    ("training.html",           "Training"),
    ("filtering-monitoring.html","Filtering & monitoring"),
    ("breaches.html",           "Breaches"),
    ("pupil-use.html",          "Pupil use"),
    ("guidance-map.html",       "The guidance map"),
    ("references.html",         "References"),
    ("dpia-tool.html",          "DPIA screening tool"),
    ("policy-template.html",    "Get the template"),
]

def nav_html(current):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return "\n        ".join(items)

def head(title, desc, canonical, jsonld=None):
    ld = ""
    if jsonld:
        ld = '\n<script type="application/ld+json">' + json.dumps(jsonld, ensure_ascii=False) + '</script>'
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="author" content="{html.escape(AUTHOR)}">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{html.escape(BRAND_TITLE)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="stylesheet" href="css/styles.css?v={ASSET_V}">{ld}
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="index.html" aria-label="{html.escape(BRAND_TITLE)} — home">
      <img class="brand__logo" src="assets/ict-evangelist-logo.png" alt="ICT Evangelist">
      <span class="brand__divider" aria-hidden="true"></span>
      <span class="brand__text">
        <span class="brand__title">AI Governance</span>
        <span class="brand__sub">in Education</span>
      </span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="main-nav">
      <svg class="waffle" width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><rect x="0" y="0" width="4" height="4" rx="1"/><rect x="7" y="0" width="4" height="4" rx="1"/><rect x="14" y="0" width="4" height="4" rx="1"/><rect x="0" y="7" width="4" height="4" rx="1"/><rect x="7" y="7" width="4" height="4" rx="1"/><rect x="14" y="7" width="4" height="4" rx="1"/><rect x="0" y="14" width="4" height="4" rx="1"/><rect x="7" y="14" width="4" height="4" rx="1"/><rect x="14" y="14" width="4" height="4" rx="1"/></svg>
      <span class="nav-toggle__label">Menu</span>
    </button>
  </div>
  <nav class="main-nav" id="main-nav" aria-label="Sections">
    <ul class="nav-grid">
        {{NAV_PLACEHOLDER}}
    </ul>
  </nav>
</header>
<main id="main">
"""

FOOTER = f"""</main>
<section class="cta-band">
  <div class="container">
    <h2>Working on your AI policy?</h2>
    <p>Support with writing or refining it, and with training your staff, is exactly the work I do. And if the template or the screening tool has helped in your school or trust, I’d love to hear&nbsp;about&nbsp;it.</p>
    <div class="btn-row">
      <a class="btn" href="mailto:mark@ictevangelist.com?subject=AI%20policy%20support">Email me</a>
      <a class="btn btn--ghost" href="https://ictevangelist.com/contact/" target="_blank" rel="noopener noreferrer">More at ictevangelist.com</a>
    </div>
  </div>
</section>
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <img src="assets/ict-evangelist-logo-white.png" alt="ICT Evangelist">
    </div>
    <div class="footer-grid">
      <div>
        <h2>About this site</h2>
        <p style="color:#c4cfd8;font-size:.9rem;max-width:52ch;margin:0;">My plain-English companion to the <em>Use of Artificial Intelligence (AI) Policy</em> template — breaking down what schools, trusts and colleges need to decide, why it matters, and the law and guidance it speaks to. Written for adoption from September 2026.</p>
      </div>
      <div>
        <h2>Sections</h2>
        <ul>
          <li><a href="landscape.html">The landscape</a></li>
          <li><a href="approved-tools.html">Approved tools</a></li>
          <li><a href="data-protection.html">Data protection</a></li>
          <li><a href="safeguarding.html">Safeguarding &amp; Prevent</a></li>
          <li><a href="guidance-map.html">The guidance map</a></li>
          <li><a href="references.html">References</a></li>
          <li><a href="dpia-tool.html">DPIA screening tool</a></li>
          <li><a href="policy-template.html">Get the template</a></li>
          <li><a href="privacy.html">Privacy notice</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-credit">
      <p>Produced by <strong>{html.escape(AUTHOR)}</strong>. The policy template and DPIA screening tool are shared under a
      <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" style="color:#cfe0ea;">Creative Commons BY-NC-SA 4.0</a>&nbsp;licence.</p>
      <p class="footer-legal">This site offers general information, not legal advice. Responsibility for compliance rests with the adopting organisation.
      <a href="privacy.html">Privacy notice</a>.</p>
    </div>
  </div>
</footer>
<script src="js/nav.js?v={ASSET_V}" defer></script>
<script src="js/a11y.js?v={ASSET_V}" defer></script>
<script src="js/consent.js?v={ASSET_V}" defer></script>
</body>
</html>
"""

def banner(kicker, title, sub, crumbs=True):
    import re as _re2
    plain = _re2.sub(r'<[^>]+>', '', title)   # crumbs carry no accent markup
    c = '<p class="crumbs"><a href="index.html">Home</a> &rsaquo; ' + plain + '</p>' if crumbs else ''
    return f"""<section class="page-banner">
  <div class="container">
    <p class="kicker">{kicker}</p>
    <h1>{title}</h1>
    <p>{sub}</p>
  </div>
</section>
<section class="section"><div class="container prose">
{c}
"""

def link(text, url):
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{text}</a>'

def guidance_box(items):
    lis = "\n".join(f"<li>{i}</li>" for i in items)
    return f"""<div class="commentary">
  <h3>Guidance it speaks to</h3>
  <ul style="margin:.4rem 0 0;">{lis}</ul>
</div>"""

def keypoints(title, items):
    lis = "\n".join(f"<li>{i}</li>" for i in items)
    return f'<div class="keypoints"><h3>{title}</h3><ul style="margin:.4rem 0 0;">{lis}</ul></div>'

def nonneg(text):
    return f'<div class="commentary" style="border-left-color:#c0392b;"><h3 style="color:#a04000;">A non-negotiable</h3><p>{text}</p></div>'

def pagenav(prev, nxt):
    p = f'<a href="{prev[0]}"><span class="dir">Previous</span><span class="ttl">{prev[1]}</span></a>' if prev else '<span></span>'
    n = f'<a class="next" href="{nxt[0]}"><span class="dir">Next</span><span class="ttl">{nxt[1]}</span></a>' if nxt else ''
    return f'<nav class="page-nav" aria-label="Between sections">{p}{n}</nav>'

import re as _re

def tie_orphans(doc):
    """Join a short final word (<=3 letters) to the word before it in paragraphs
    and list items, so it can't wrap onto a line of its own."""
    return _re.sub(r'(\S) (\S{1,3})([.!?…]?)</(p|li)>', r'\1&nbsp;\2\3</\4>', doc)

def clean_urls(doc):
    """Rewrite internal links and asset paths for extensionless URLs.
    Pages are emitted as <slug>/index.html and served at /<slug>/, so links
    drop .html and assets become root-relative."""
    doc = doc.replace('href="index.html"', 'href="/"')
    doc = doc.replace("href='index.html'", 'href="/"')
    doc = _re.sub(r'href="([a-z0-9-]+)\.html(#[^"]*)?"',
                  lambda m: f'href="/{m.group(1)}/{m.group(2) or ""}"', doc)
    doc = _re.sub(r"href='([a-z0-9-]+)\.html(#[^']*)?'",
                  lambda m: f'href="/{m.group(1)}/{m.group(2) or ""}"', doc)
    doc = doc.replace('href="css/styles.css', 'href="/css/styles.css')
    doc = _re.sub(r'src="(js|assets)/', r'src="/\1/', doc)
    doc = _re.sub(r'href="(downloads|assets)/', r'href="/\1/', doc)
    doc = doc.replace('href="favicon', 'href="/favicon')
    doc = doc.replace('href="apple-touch-icon', 'href="/apple-touch-icon')
    return doc

def write(slug, title, desc, body, jsonld=None):
    stem = slug[:-5] if slug.endswith(".html") else slug
    canonical = f"{SITE}/{stem}/"
    doc = head(title, desc, canonical, jsonld).replace("{NAV_PLACEHOLDER}", nav_html(slug)) + body + "</div></section>\n" + FOOTER
    outdir = OUT / stem
    outdir.mkdir(exist_ok=True)
    (outdir / "index.html").write_text(clean_urls(tie_orphans(doc)), encoding="utf-8")
    print("wrote", stem + "/")

# =====================================================================
#  CONTENT
# =====================================================================
print("Content defined in build_content.py")
