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
  "A plain-English tool that runs in your browser, for any AI or digital product you are thinking of buying. Tell us where to send it, and it is yours to keep.") + f"""
  <p class="lead">Assessing an AI tool before you buy it should not need a law degree. This screening tool asks the right questions in plain English, then tells you whether your answers are detailed enough to send to your Data Protection Officer for sign-off.</p>

  <div class="chart-figure">
    <div>
      <h2 class="mt-0">What it does</h2>
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
      <p>Each section has an <em>i</em> button that explains what it is for and what a good answer looks like. When you have finished, <strong>Check readiness</strong> tells you whether it is ready for your DPO. It runs entirely in your browser, so nothing you type is sent anywhere, and it prints cleanly for your records.</p>
      <p class="chart-note">It reflects the UK GDPR and Data Protection Act 2018 as amended by the Data (Use and Access) Act 2025, the DfE generative AI product safety standards (January 2026), DfE guidance on procuring edtech, the ICO Children’s Code and edtech guidance, and the ICO’s <em>Edtech examined</em> audit findings. It is a template to support a context-specific assessment; it is not legal advice and does not replace your DPO’s sign-off.</p>
    </div>

    <div>
      <div class="card" style="border-top:4px solid var(--brand-teal);">
        <h3 class="mt-0">Get your copy</h3>
        <p>Tell us who you are and where you work, and the download unlocks. It is free, and shared under a Creative&nbsp;Commons&nbsp;BY-NC-SA&nbsp;4.0 licence.</p>

        <!-- =====================================================================
             GOOGLE FORM GOES HERE.
             Replace this placeholder with your Google Form embed, e.g.:
             <iframe src="https://docs.google.com/forms/d/e/FORM_ID/viewform?embedded=true"
                     width="100%" height="720" frameborder="0" marginheight="0" marginwidth="0"
                     title="Sign up to unlock the DPIA screening tool">Loading…</iframe>
             In the Google Form's *confirmation message*, paste the download link so it
             appears the moment someone submits:
             https://aigovernance.ictevangelist.com/downloads/AI-DPIA-Screening-Tool.html
             ===================================================================== -->
        <div style="border:2px dashed var(--brand-teal);border-radius:10px;padding:1.2rem;background:var(--surface-2);text-align:center;">
          <p style="margin:.2rem 0;font-weight:600;color:var(--brand-deep);">[ Google Form embeds here ]</p>
          <p style="margin:.2rem 0;font-size:.9rem;color:var(--ink-soft);">Send Mark the form’s embed link and this placeholder is replaced with the live sign-up form.</p>
        </div>

        <hr class="divider">
        <p style="font-size:.9rem;color:var(--ink-soft);margin:0 0 .6rem;"><strong>After you submit the form</strong>, your download link appears. It is this file:</p>
        <a class="btn btn--solid" href="downloads/AI-DPIA-Screening-Tool.html" download style="width:100%;text-align:center;">Download the DPIA screening tool (HTML)</a>
        <p style="font-size:.8rem;color:var(--ink-soft);margin:.8rem 0 0;">Save the file and open it in any browser. No internet connection needed to use it.</p>
      </div>
    </div>
  </div>

  <h2>How it works</h2>
  <ol>
    <li>Complete the short sign-up form above.</li>
    <li>When you submit it, the confirmation screen shows your download link.</li>
    <li>Save the file, open it, and complete a screening for any tool you are considering.</li>
    <li>Print or save the finished assessment, and send it to your DPO for approval.</li>
  </ol>
  <p>We only hold your details as set out in the <a href="privacy.html">privacy notice</a>.</p>

  {guidance_box([link("UK GDPR", U['ukgdpr']) + " &amp; " + link("Data Protection Act 2018", U['dpa2018']) + " (as amended by the " + link("Data (Use and Access) Act 2025", U['duaa']) + "); " + link("ICO AI &amp; data protection risk toolkit", U['ico_toolkit']) + ".",
                 link("DfE generative AI product safety standards", U['dfe_safety']) + " (January 2026) and " + link("DfE guidance on procuring edtech", U['dp_schools']) + ".",
                 link("ICO Children’s Code", U['childrens']) + " and " + link("<em>Edtech examined</em> audit findings", U['edtech']) + "."])}
""" + pagenav(("references.html", "References"), ("policy-template.html", "Get the template"))

write("dpia-tool.html", "DPIA screening tool — " + build.BRAND_TITLE,
      "Unlock a free, plain-language, browser-based DPIA screening tool for assessing any AI or digital product before you procure it.",
      dpia_body, ORG_LD)

# ------------------------------------------------ POLICY TEMPLATE (download)
tmpl_body = banner("Free resource", "Get the policy template",
  "A completable Use of Artificial Intelligence (AI) Policy for schools, trusts and colleges — a staff-use spine with optional modules for pupil use and governed exceptions.") + f"""
  <p class="lead">This is the document the whole site is built around: a full, completable AI policy template, written for adoption from <strong>September 2026</strong> against the current framework of law and guidance.</p>

  <div style="text-align:center;margin:1.8rem 0;">
    <a class="btn btn--solid" href="downloads/Use-of-AI-Policy-Template.docx" download style="font-size:1.05rem;padding:.9rem 1.8rem;">Download the template (Word .docx)</a>
    <p style="font-size:.85rem;color:var(--ink-soft);margin-top:.7rem;">Free · Creative Commons BY-NC-SA 4.0 · complete it for your context before publishing</p>
  </div>

  <h2>What it is</h2>
  <p>A template — not a finished policy. It cannot be used as it stands: it requires completion for your context, alignment with your existing policies, agreement by the right stakeholders, and formal ratification. Placeholders in <strong>[BOLD BRACKETS]</strong> mark what you must decide; “HOW TO COMPLETE THIS SECTION” boxes explain what to insert; “OPTIONAL MODULE” boxes mark parts to switch on or delete.</p>

  <h2>What is inside</h2>
  <div class="card-grid">
    <div class="card"><h3>The spine</h3><p>Policy statement and scope; roles and oversight; the approval gate; what staff may and must not do; data protection; accuracy and human oversight; safeguarding; impact assessment; training; filtering and monitoring; breaches.</p></div>
    <div class="card"><h3>Optional modules</h3><p>Pupil use (only once a DPIA and an age-appropriate AI education plan are in place) and governed exceptions for single, tightly-scoped purposes.</p></div>
    <div class="card"><h3>The non-negotiables</h3><p>The elements you may reword but must not weaken — because doing so would make the policy non-compliant.</p></div>
  </div>

  <h2>How to use it well</h2>
  <ol>
    <li>Read the <a href="landscape.html">landscape</a> and the <a href="guidance-map.html">guidance map</a> first, so the choices make sense.</li>
    <li>Work through the template in order; each step has a “how to complete” box.</li>
    <li>Keep the non-negotiables intact. Tailor the wording to your own voice, but leave the substance alone.</li>
    <li>If you are a multi-academy trust, adopt it once, centrally, with school-level detail in local appendices.</li>
    <li>Delete every guidance and optional-flag box, and the front cover, before publishing.</li>
  </ol>

  <div class="commentary">
    <h3>Licence &amp; attribution</h3>
    <p>Shared under a <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0</a> licence: adapt it for non-commercial purposes, credit <strong>Mark Anderson, ICT Evangelist</strong> (ictevangelist.com), and license adapted versions you share under the same terms.</p>
  </div>

  <p class="chart-note">This template is general information to support leaders in creating their own policy. It does not constitute legal advice, and responsibility for compliance and ratification rests with the adopting organisation.</p>
""" + pagenav(("dpia-tool.html", "DPIA screening tool"), ("privacy.html", "Privacy notice"))

write("policy-template.html", "Get the policy template — " + build.BRAND_TITLE,
      "Download a free, completable Use of AI Policy template for schools, trusts and colleges. Written for September 2026. Creative Commons licensed.",
      tmpl_body, ORG_LD)

# ------------------------------------------------ PRIVACY NOTICE
priv_body = banner("Legal", "Privacy notice",
  "How this site handles information, including the sign-up you complete to unlock the DPIA screening tool.", crumbs=True) + f"""
  <p class="lead">This is a site about data protection, so it ought to hold itself to the same standard. In plain terms, here is what we do and do not collect.</p>

  <h2>The site itself</h2>
  <p>These pages are plain, self-contained static files. They set <strong>no cookies</strong>, run <strong>no analytics or tracking</strong>, and make no advertising or profiling calls. Your reading-controls preferences (text size, contrast, spacing) are stored only in your own browser’s local storage, on your device, and are never sent anywhere.</p>
  <p>The <strong>DPIA screening tool</strong> you download runs entirely in your browser. Nothing you type into it is transmitted to us or anyone else; it stays on your device unless you choose to save, print or send it.</p>

  <h2>The sign-up form</h2>
  <p>To unlock the DPIA screening tool we ask you to complete a short form. That form is a <strong>Google Form</strong>, and the information you enter is processed by Google on our behalf as a data processor. Here is the detail:</p>
  <div class="data-table-wrap">
  <table class="data">
    <tbody>
      <tr><th scope="row">Who is responsible (controller)</th><td>Mark Anderson, ICT Evangelist — the data controller for sign-ups.</td></tr>
      <tr><th scope="row">What we collect</th><td>Only what the form asks — typically your name, work email and organisation. We do not ask for special-category data; please do not enter any.</td></tr>
      <tr><th scope="row">Why (purpose)</th><td>To provide the resource you requested and, where you have agreed, to contact you about related AI-in-education resources.</td></tr>
      <tr><th scope="row">Lawful basis</th><td>Consent, which you give by submitting the form. You can withdraw it at any time (see below).</td></tr>
      <tr><th scope="row">Who processes it</th><td>Google (Google Forms) as our processor. Data may be handled under Google’s standard data-processing terms and approved international-transfer safeguards.</td></tr>
      <tr><th scope="row">How long we keep it</th><td>No longer than we need it for the purpose above; you may ask us to delete it sooner.</td></tr>
      <tr><th scope="row">Your rights</th><td>Access, correction, deletion, objection, and withdrawal of consent. Contact us and we will action it.</td></tr>
    </tbody>
  </table>
  </div>

  <h2>Contact &amp; complaints</h2>
  <p>To exercise any right, or to ask a question about this notice, contact <strong>Mark Anderson (ICT Evangelist)</strong> via <a href="https://ictevangelist.com">ictevangelist.com</a>. If you are unhappy with how we have handled your information, you can complain to the Information Commissioner’s Office (ICO) at <a href="https://ico.org.uk">ico.org.uk</a>.</p>

  <p class="chart-note">This notice covers this website and its sign-up form. The exact fields, retention period and contact route should be confirmed by the site owner before launch — the placeholders here reflect the intended, privacy-first design.</p>
""" + pagenav(("policy-template.html", "Get the template"), None)

write("privacy.html", "Privacy notice — " + build.BRAND_TITLE,
      "How this site handles information: no cookies or tracking on the pages, and a plain-language notice for the Google Form sign-up used to unlock the DPIA tool.",
      priv_body, ORG_LD)

print("Tool, template and privacy pages written.")
