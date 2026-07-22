#!/usr/bin/env python3
# Tool, download and privacy pages. Run: python3 content2.py
from build import (write, banner, guidance_box, keypoints, nonneg, pagenav, link)
import build

U = {
 'ukgdpr':     'https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/',
 'dpa2018':    'https://www.legislation.gov.uk/ukpga/2018/12/contents',
 'duaa':       'https://www.legislation.gov.uk/ukpga/2025/18/contents',
 'ico_toolkit':'https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/ai-and-data-protection-risk-toolkit/',
 'childrens':  'https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/',
 'dfe_safety': 'https://www.gov.uk/government/publications/generative-ai-product-safety-standards/generative-ai-product-safety-standards',
 'dp_schools': 'https://www.gov.uk/guidance/data-protection-in-schools',
 'edtech':     'https://ico.org.uk/action-weve-taken/audits-and-overview-reports/2026/06/edtech/',
}

ORG_LD = {"@context": "https://schema.org", "@type": "Organization",
          "name": "ICT Evangelist", "url": "https://ictevangelist.com", "founder": "Mark Anderson"}

# ------------------------------------------------ DPIA SCREENING TOOL (value exchange)
dpia_body = banner("Free resource", "The DPIA screening tool",
  "A plain-English tool that runs in your browser, for any AI or digital product you’re thinking of buying. Tell me who you are, and it’s yours to keep.") + f"""
  <p class="lead">Assessing an AI tool before you buy it shouldn’t need a law degree. I’ve built this screening tool to ask the right questions in plain English, then tell you whether your answers are detailed enough to send to your Data Protection Officer for sign-off.</p>

  <h2>What it does</h2>
      <p>The <strong>AI &amp; Digital Tool DPIA Screening Tool</strong> walks you, section by section, through everything a Data Protection Impact Assessment needs to cover:</p>
      <ul>
        <li>Purpose and description — including new AI features inside tools you already use.</li>
        <li>Whose personal information the tool touches, and what can be typed, pasted or uploaded into it.</li>
        <li>Scale and volume of data.</li>
        <li>Roles (controller vs processor), the contract, sub-processors and international transfers.</li>
        <li>Lawful basis and retention.</li>
        <li>Automated decisions, biometrics and emotion inference.</li>
        <li>What the supplier does with the data — AI training, product development, analytics and logs.</li>
      </ul>
      <p>Each section has an <em>i</em> button that explains what it’s for and what a good answer looks like. When you’ve finished, <strong>Check readiness</strong> tells you whether it’s ready for your DPO. It runs entirely in your browser, so nothing you type is sent anywhere, and it prints cleanly for your records.</p>
      <p class="chart-note">It reflects the UK GDPR and Data Protection Act 2018 as amended by the Data (Use and Access) Act 2025, the DfE generative AI product safety standards (January 2026), DfE guidance on procuring edtech, the ICO Children’s Code and edtech guidance, and the ICO’s <em>Edtech examined</em> audit findings. It is a template to support a context-specific assessment; it is not legal advice and does not replace your DPO’s sign-off.</p>

  <div class="card signup-card" style="border-top:4px solid var(--brand-teal);">
    <h3 class="mt-0">Get your copy</h3>
    <p>Tell me who you are and where you work, and the download unlocks. It’s free, and shared under a Creative&nbsp;Commons&nbsp;BY-NC-SA&nbsp;4.0 licence.</p>

    <div class="form-embed">
      <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdP7Mm92PqR36-Fs3Hk1DCPgEMnkkyJ7PDx02OUZuO9Wt1vPg/viewform?embedded=true"
              width="100%" height="1350" frameborder="0" marginheight="0" marginwidth="0"
              loading="lazy" title="Sign up to unlock the DPIA screening tool">Loading&hellip;</iframe>
    </div>
    <p style="font-size:.85rem;color:var(--ink-soft);margin:.8rem 0 0;"><strong>One important step:</strong> the link on the confirmation screen opens your download page, and the file saves straight to your device. Open the saved file in any browser — that’s how it runs. It needs no internet connection, and nothing you type into it is sent anywhere.</p>
  </div>

  <h2>How it works</h2>
  <ol>
    <li>Complete the short sign-up form above.</li>
    <li>When you submit it, the confirmation screen links to your download page — the file saves straight to your device.</li>
    <li>Open the saved file in any browser on your own device — that’s how the tool runs. No internet connection needed.</li>
    <li>Complete a screening for any tool you’re considering.</li>
    <li>Print or save the finished assessment, and send it to your DPO for approval.</li>
  </ol>
  <p>I only hold your details as set out in the <a href="privacy.html">privacy notice</a>.</p>

  {guidance_box([link("UK GDPR", U['ukgdpr']) + " &amp; " + link("Data Protection Act 2018", U['dpa2018']) + " (as amended by the " + link("Data (Use and Access) Act 2025", U['duaa']) + "); " + link("ICO AI &amp; data protection risk toolkit", U['ico_toolkit']) + ".",
                 link("DfE generative AI product safety standards", U['dfe_safety']) + " (January 2026) and " + link("DfE guidance on procuring edtech", U['dp_schools']) + ".",
                 link("ICO Children’s Code", U['childrens']) + " and " + link("<em>Edtech examined</em> audit findings", U['edtech']) + "."])}
""" + pagenav(("references.html", "References"), ("policy-template.html", "Get the template"))

write("dpia-tool.html", "DPIA screening tool — " + build.BRAND_TITLE,
      "Unlock a free, plain-English, browser-based DPIA screening tool for assessing any AI or digital product before you procure it.",
      dpia_body, ORG_LD)

# ------------------------------------------------ DOWNLOAD PAGE (reward delivery)
# Linked from the Google Form's confirmation message. Breaks out of the embedded
# iframe, then auto-starts the download from this domain. Kept out of the
# sitemap and marked noindex so search engines don't offer a form bypass.
download_body = banner("Free resource", "Your download",
  "The DPIA screening tool is on its way to your device.", crumbs=False) + f"""
  <p class="lead">Thanks for signing up. Your download should start automatically — if it doesn’t, use the button below.</p>

  <p><a id="dl" class="btn btn--solid" href="downloads/AI-DPIA-Screening-Tool.html" download="AI-DPIA-Screening-Tool.html">Download the DPIA screening tool</a></p>

  <h2>What to do next</h2>
  <ol>
    <li>Save the file somewhere you’ll find it again.</li>
    <li>Open it in any browser on your own device — that’s how the tool runs. It needs no internet connection, and nothing you type into it is sent anywhere.</li>
    <li>Work through a screening for the tool you’re considering; the <em>i</em> buttons explain each section as you go.</li>
    <li>Use <strong>Check readiness</strong>, then print or save the finished assessment and send it to your DPO for approval.</li>
  </ol>
  <p>Wondering what the tool covers? It’s all on the <a href="dpia-tool.html">DPIA screening tool</a> page.</p>

  <script>
  (function () {{
    // If we've been opened inside the embedded form's iframe, break out to a full tab.
    if (window.top !== window.self) {{
      try {{ window.top.location.replace(window.location.href); return; }} catch (e) {{}}
    }}
    // Auto-start the download shortly after load; the button remains as fallback.
    setTimeout(function () {{
      var a = document.getElementById('dl');
      if (a) a.click();
    }}, 700);
  }})();
  </script>
"""
write("download.html", "Your download — " + build.BRAND_TITLE,
      "Your DPIA screening tool download.", download_body, ORG_LD)
# Mark this page noindex: it's the reward step, not a landing page.
_dl = build.OUT / "download" / "index.html"
_dl.write_text(_dl.read_text(encoding="utf-8").replace(
    '<meta name="robots" content="index, follow">',
    '<meta name="robots" content="noindex, nofollow">'), encoding="utf-8")

# ------------------------------------------------ POLICY TEMPLATE (download)
tmpl_body = banner("Free resource", "Get the policy template",
  "A completable Use of Artificial Intelligence (AI) Policy for schools, trusts and colleges — a staff-use spine with optional modules for pupil use and governed exceptions.") + f"""
  <p class="lead">This is the document this whole site is built around: my full, completable AI policy template, written for adoption from <strong>September 2026</strong> against the current framework of law and guidance.</p>

  <div style="margin:1.8rem 0;">
    <a class="btn btn--solid" href="downloads/Use-of-AI-Policy-Template.docx" download style="font-size:1.05rem;padding:.9rem 1.8rem;">Download the template (Word .docx)</a>
    <p style="font-size:.85rem;color:var(--ink-soft);margin-top:.7rem;">Free · Creative Commons BY-NC-SA 4.0 · complete it for your context before publishing</p>
  </div>

  <h2>What it is</h2>
  <p>A template — not a finished policy. It can’t be used as it stands: it needs completing for your context, aligning with your existing policies so it doesn’t contradict what you say elsewhere, agreeing with the right stakeholders, and formally ratifying. Placeholders in <strong>[BOLD BRACKETS]</strong> mark what you must decide; “HOW TO COMPLETE THIS SECTION” boxes explain what to insert; “OPTIONAL MODULE” boxes mark parts to switch on or delete.</p>

  <h2>What is inside</h2>
  <div class="card-grid">
    <div class="card"><h3>The spine</h3><p>Policy statement and scope; roles and oversight; approved tools and how tools are approved; what staff may and must not do; data protection; accuracy and human oversight; safeguarding; impact assessment; training; filtering and monitoring; breaches — plus an appendix listing every piece of legislation and guidance the policy rests on.</p></div>
    <div class="card"><h3>Optional modules</h3><p>Pupil use (only once a DPIA is complete and age-appropriate teaching about AI is in place) and governed exceptions for single, tightly-scoped purposes.</p></div>
    <div class="card"><h3>The non-negotiables</h3><p>The elements you may reword but must not weaken — because doing so would make the policy non-compliant.</p></div>
  </div>

  <h2>How to use it well</h2>
  <ol>
    <li>Read the <a href="landscape.html">landscape</a> and the <a href="guidance-map.html">guidance map</a> first, so the choices make sense.</li>
    <li>Work through the template in order; each step has a “how to complete” box.</li>
    <li>Keep the non-negotiables intact. Tailor the wording to your own voice, but leave the substance alone.</li>
    <li>If you’re a multi-academy trust, adopt it once, centrally, with school-level detail in local appendices.</li>
    <li>Delete every guidance and optional-flag box, and the front cover, before publishing.</li>
  </ol>

  <div class="commentary">
    <h3>Licence &amp; attribution</h3>
    <p>I share the template under a <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0</a> licence. In simple terms, you’re free to:</p>
    <ul style="margin:.5rem 0;">
      <li>adapt it,</li>
      <li>copy it, and</li>
      <li>reuse it.</li>
    </ul>
    <p>What you can’t do is use it for commercial gain. And anything you adapt or share must credit me — <strong>Mark Anderson, ICT Evangelist</strong> (ictevangelist.com) — and carry the same licence.</p>
  </div>

  <p>Feedback is always welcome — and I’d love to hear how the template has helped in your school or trust. If you need support writing or refining your AI policy, or training staff on AI, <a href="mailto:mark@ictevangelist.com?subject=AI%20policy%20support">get in touch</a>.</p>

  <p class="chart-note">This template is general information to support leaders in creating their own policy. It doesn’t constitute legal advice, responsibility for compliance and ratification rests with the adopting organisation, and I take no responsibility for what you take from the template and put into practice. Complete it for your context, and have it ratified, before you rely on it.</p>
""" + pagenav(("dpia-tool.html", "DPIA screening tool"), ("privacy.html", "Privacy notice"))

write("policy-template.html", "Get the policy template — " + build.BRAND_TITLE,
      "Download a free, completable Use of AI Policy template for schools, trusts and colleges. Written for September 2026. Creative Commons licensed.",
      tmpl_body, ORG_LD)

# ------------------------------------------------ PRIVACY NOTICE
priv_body = banner("Legal", "Privacy notice",
  "How this site handles information, including the sign-up you complete to unlock the DPIA screening tool.", crumbs=True) + f"""
  <p class="lead">This is a site about data protection, so it ought to hold itself to the same standard. In plain terms, here’s what I do and don’t collect.</p>

  <h2>The site itself</h2>
  <p>These pages are plain, self-contained static files. They set <strong>no cookies</strong>, run <strong>no analytics or tracking</strong>, and make no advertising or profiling calls. Your reading-controls preferences (text size, contrast, spacing) are stored only in your own browser’s local storage, on your device, and are never sent anywhere.</p>
  <p>The <strong>DPIA screening tool</strong> you download runs entirely in your browser. Nothing you type into it is transmitted to me or anyone else; it stays on your device unless you choose to save, print or send it.</p>

  <h2>The sign-up form</h2>
  <p>To unlock the DPIA screening tool I ask you to complete a short form. That form is a <strong>Google Form</strong>, and the information you enter is processed by Google on my behalf as a data processor. Here’s the detail:</p>
  <div class="data-table-wrap">
  <table class="data">
    <tbody>
      <tr><th scope="row">Who is responsible (controller)</th><td>Me — Mark Anderson, ICT Evangelist — the data controller for sign-ups.</td></tr>
      <tr><th scope="row">What I collect</th><td>Only what the form asks: your name, work email, your school, trust or organisation, your role if you choose to give it, and whether you’d be interested in hearing about future cohort work. I don’t ask for special-category data; please don’t enter any.</td></tr>
      <tr><th scope="row">Why (purpose)</th><td>To provide the resource you requested and, where you’ve agreed, to contact you about related AI-in-education resources.</td></tr>
      <tr><th scope="row">Lawful basis</th><td>Consent, which you give by submitting the form. You can withdraw it at any time (see below).</td></tr>
      <tr><th scope="row">Who processes it</th><td>Google (Google Forms) as my processor. Data may be handled under Google’s standard data-processing terms and approved international-transfer safeguards.</td></tr>
      <tr><th scope="row">How long I keep it</th><td>The list is reviewed annually and details no longer needed are deleted. You can ask me to delete yours sooner at any time.</td></tr>
      <tr><th scope="row">Your rights</th><td>Access, correction, deletion, objection, and withdrawal of consent. Contact me and I’ll action it.</td></tr>
    </tbody>
  </table>
  </div>

  <h2>Contact &amp; complaints</h2>
  <p>To exercise any right, or to ask a question about this notice, contact me — <strong>Mark Anderson (ICT Evangelist)</strong> — via <a href="https://ictevangelist.com">ictevangelist.com</a>. If you’re unhappy with how I’ve handled your information, you can complain to the Information Commissioner’s Office (ICO) at <a href="https://ico.org.uk">ico.org.uk</a>.</p>

  <p class="chart-note">This notice covers this website and its sign-up form. It was last reviewed when the sign-up form went live, and will be updated whenever what the form collects, or how it’s processed, changes.</p>
""" + pagenav(("policy-template.html", "Get the template"), None)

write("privacy.html", "Privacy notice — " + build.BRAND_TITLE,
      "How this site handles information: no cookies or tracking on the pages, and a plain-English notice for the Google Form sign-up used to unlock the DPIA tool.",
      priv_body, ORG_LD)

print("Tool, template and privacy pages written.")
