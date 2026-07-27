#!/usr/bin/env python3
# Tool, download and privacy pages. Run: python3 content2.py
from build import (write, banner, guidance_box, keypoints, nonneg, pagenav, link, quote_band)
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
dpia_body = banner("Free resource", 'The <span class="accent">DPIA screening tool</span>',
  "A plain-English tool that runs in your browser, for any AI or digital product you’re thinking of buying. Tell me who you are, and it’s yours to keep.") + f"""
  <p class="lead">Assessing an AI tool before you buy it shouldn’t need a law degree. I’ve built this screening tool to ask the right questions in plain English, then tell you whether your answers are detailed enough to send to your Data Protection Officer for sign-off.</p>

  <h2>What it does</h2>
      <p>The <strong>AI &amp; Digital Tool DPIA Screening Tool</strong> walks you, section by section, through everything a Data Protection Impact Assessment needs to cover:</p>
      <ul>
        <li>Purpose and description, including new AI features inside tools you already use.</li>
        <li>Whose personal information the tool touches, and what can be typed, pasted or uploaded into it.</li>
        <li>Scale and volume of data.</li>
        <li>Roles (controller vs processor), the contract, sub-processors and international transfers.</li>
        <li>Lawful basis and retention.</li>
        <li>Automated decisions, biometrics and emotion inference.</li>
        <li>What the supplier does with the data: AI training, product development, analytics and logs.</li>
      </ul>
      <p>Each section has an <em>i</em> button that explains what it’s for and what a good answer looks like. When you’ve finished, <strong>Check readiness</strong> tells you whether it’s ready for your DPO. It runs entirely in your browser, so nothing you type is sent anywhere, and it prints cleanly for your records.</p>
      <p class="chart-note">It reflects the UK GDPR and Data Protection Act 2018 as amended by the Data (Use and Access) Act 2025, the DfE generative AI product safety standards (January 2026), DfE guidance on procuring edtech, the ICO Children’s Code and edtech guidance, and the ICO’s <em>Edtech examined</em> audit findings. It is a template to support a context-specific assessment; it is not legal advice and does not replace your DPO’s sign-off.</p>

  {quote_band("He works with you to shape sessions as you need and gives you confidence. I have recommended you already.",
              "Jo Fletcher-Saxon", "Assistant Principal, Ashton Sixth Form College")}

  <div class="card signup-card" style="border-top:4px solid var(--brand-teal);">
    <h3 class="mt-0">Get your copy</h3>
    <p>Tell me who you are and where you work, and the download unlocks. It’s free, and shared under a Creative&nbsp;Commons&nbsp;BY-NC-SA&nbsp;4.0 licence.</p>

    <div class="form-embed">
      <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdP7Mm92PqR36-Fs3Hk1DCPgEMnkkyJ7PDx02OUZuO9Wt1vPg/viewform?embedded=true"
              width="100%" height="1350" frameborder="0" marginheight="0" marginwidth="0"
              loading="lazy" title="Sign up to unlock the DPIA screening tool">Loading&hellip;</iframe>
    </div>
    <p style="font-size:.85rem;color:var(--ink-soft);margin:.8rem 0 0;"><strong>One important step:</strong> the link on the confirmation screen opens your download page, and the file saves straight to your device. Open the saved file in any browser. That’s how it runs. It needs no internet connection, and nothing you type into it is sent anywhere.</p>
  </div>

  <h2>How it works</h2>
  <ol>
    <li>Complete the short sign-up form above.</li>
    <li>When you submit it, the confirmation screen links to your download page, and the file saves straight to your device.</li>
    <li>Open the saved file in any browser on your own device. That’s how the tool runs. No internet connection needed.</li>
    <li>Complete a screening for any tool you’re considering.</li>
    <li>Print or save the finished assessment, and send it to your DPO for approval.</li>
  </ol>
  <p>I only hold your details as set out in the <a href="privacy.html">privacy notice</a>.</p>

  {guidance_box([link("UK GDPR", U['ukgdpr']) + " &amp; " + link("Data Protection Act 2018", U['dpa2018']) + " (as amended by the " + link("Data (Use and Access) Act 2025", U['duaa']) + "); " + link("ICO AI &amp; data protection risk toolkit", U['ico_toolkit']) + ".",
                 link("DfE generative AI product safety standards", U['dfe_safety']) + " (January 2026) and " + link("DfE guidance on procuring edtech", U['dp_schools']) + ".",
                 link("ICO Children’s Code", U['childrens']) + " and " + link("<em>Edtech examined</em> audit findings", U['edtech']) + "."])}
""" + pagenav(("references.html", "References"), ("policy-template.html", "Get the template"))

write("dpia-tool.html", "DPIA screening tool | " + build.BRAND_TITLE,
      "Unlock a free, plain-English, browser-based DPIA screening tool for assessing any AI or digital product before you procure it.",
      dpia_body, ORG_LD)

# ------------------------------------------------ DOWNLOAD PAGE (reward delivery)
# Linked from the Google Form's confirmation message. Breaks out of the embedded
# iframe, then auto-starts the download from this domain. Kept out of the
# sitemap and marked noindex so search engines don't offer a form bypass.
download_body = banner("Free resource", 'Your <span class="accent">download</span>',
  "The DPIA screening tool is on its way to your device.", crumbs=False) + f"""
  <p class="lead">Thanks for signing up. Your download should start automatically. If it doesn’t, use the button below.</p>

  <p><a id="dl" class="btn btn--solid" href="downloads/AI-DPIA-Screening-Tool.html" download="AI-DPIA-Screening-Tool.html">Download the DPIA screening tool</a></p>

  <h2>What to do next</h2>
  <ol>
    <li>Save the file somewhere you’ll find it again.</li>
    <li>Open it in any browser on your own device. That’s how the tool runs. It needs no internet connection, and nothing you type into it is sent anywhere.</li>
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
write("download.html", "Your download | " + build.BRAND_TITLE,
      "Your DPIA screening tool download.", download_body, ORG_LD)
# Mark this page noindex: it's the reward step, not a landing page.
_dl = build.OUT / "download" / "index.html"
_dl.write_text(_dl.read_text(encoding="utf-8").replace(
    '<meta name="robots" content="index, follow">',
    '<meta name="robots" content="noindex, nofollow">'), encoding="utf-8")

# ------------------------------------------------ POLICY TEMPLATE (download)
tmpl_body = banner("Free resource", 'Get the <span class="accent">policy template</span>',
  "A completable Use of Artificial Intelligence (AI) Policy for schools, trusts and colleges: a staff-use spine with optional modules for pupil use and governed exceptions.") + f"""
  <p class="lead">This is the document this whole site is built around: my full, completable AI policy template, written for adoption from <strong>September 2026</strong> against the current framework of law and guidance.</p>

  <div style="margin:1.8rem 0;">
    <a class="btn btn--solid" href="downloads/Use-of-AI-Policy-Template.docx" download style="font-size:1.05rem;padding:.9rem 1.8rem;">Download the template (Word .docx)</a>
    <p style="font-size:.85rem;color:var(--ink-soft);margin-top:.7rem;">Free · Creative Commons BY-NC-SA 4.0 · complete it for your context before publishing</p>
  </div>

  <h2>What it is</h2>
  <p>A template, not a finished policy. It can’t be used as it stands: it needs completing for your context, aligning with your existing policies so it doesn’t contradict what you say elsewhere, agreeing with the right stakeholders, and formally ratifying. Placeholders in <strong>[BOLD BRACKETS]</strong> mark what you must decide; “HOW TO COMPLETE THIS SECTION” boxes explain what to insert; “OPTIONAL MODULE” boxes mark parts to switch on or delete.</p>

  <h2>What is inside</h2>
  <div class="card-grid">
    <div class="card"><h3>The spine</h3><p>Policy statement and scope; roles and oversight; approved tools and how tools are approved; what staff may and must not do; data protection; accuracy and human oversight; safeguarding; impact assessment; training; filtering and monitoring; breaches. There’s also an appendix listing every piece of legislation and guidance the policy rests on.</p></div>
    <div class="card"><h3>Optional modules</h3><p>Pupil use (only once a DPIA is complete and age-appropriate teaching about AI is in place) and governed exceptions for single, tightly-scoped purposes.</p></div>
    <div class="card"><h3>The non-negotiables</h3><p>The elements you may reword but must not weaken, because doing so would make the policy non-compliant.</p></div>
  </div>

  {quote_band("The fact you’ve been with us all year has shown that we <em>are</em> embedding AI, not just having a one-off session to tick a box.",
              "Sydney Jones-Jackson", "Digital Teaching &amp; Learning Mentor, Ashton Sixth Form College")}

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
    <p>What you can’t do is use it for commercial gain. And anything you adapt or share must credit me, <strong>Mark Anderson, ICT Evangelist</strong> (ictevangelist.com), and carry the same licence.</p>
  </div>

  <p>Feedback is always welcome, and I’d love to hear how the template has helped in your school or trust. If you need support writing or refining your AI policy, or training staff on AI, <a href="mailto:mark@ictevangelist.com?subject=AI%20policy%20support">get in touch</a>.</p>

  <p class="chart-note">This template is general information to support leaders in creating their own policy. It doesn’t constitute legal advice, responsibility for compliance and ratification rests with the adopting organisation, and I take no responsibility for what you take from the template and put into practice. Complete it for your context, and have it ratified, before you rely on it.</p>
""" + pagenav(("dpia-tool.html", "DPIA screening tool"), ("privacy.html", "Privacy notice"))

write("policy-template.html", "Get the policy template | " + build.BRAND_TITLE,
      "Download a free, completable Use of AI Policy template for schools, trusts and colleges. Written for September 2026. Creative Commons licensed.",
      tmpl_body, ORG_LD)

# ------------------------------------------------ THE AUTUMN COHORT
cohort_body = banner("Work with me", 'The <span class="accent">autumn cohort</span>',
  "Complete, approve and ratify your Use of AI Policy this term, working through it with me and a small group of schools, trusts and colleges.") + f"""
  <p class="lead">The template is free, and it always will be. But a template on its own isn’t a policy: it needs completing for your context, taking through your stakeholders, and ratifying. That’s the real work, and this cohort is how we do it together, so you start the spring term with it done.</p>

  <figure class="fig-break"><img src="assets/cohort-journey.png" alt="The journey: from the free downloaded template, through five cohort sessions worked through together, to a policy ratified by your governors or board and in force for the spring term." width="1120" height="270" loading="lazy"></figure>

  <h2>What it is</h2>
  <p>A small group, capped at <strong>twelve organisations</strong>, working through the policy together across the autumn term: five live online sessions of ninety minutes, each one taught, structured, and built so that every question answered helps the whole room. Bring your digital lead, your DPO or DSL, and a senior leader: whoever carries the policy in your context. Policies get ratified faster when more than one person carries them home.</p>

  <figure class="fig-break"><img src="assets/cohort-glance.png" alt="The autumn cohort at a glance: five Thursday sessions, 4.00 to 5.30pm, online, capped at twelve organisations. Session 1 on 24 September covers scope, the landscape and who owns what. Session 2 on 15 October covers approved tools and acceptable use. Session 3 on 22 October covers data protection and a live DPIA. Session 4 on 12 November covers safeguarding, oversight and enforcement. Session 5 on 26 November covers training, pupils and ratification." width="1120" height="420" loading="lazy"></figure>

  <p>Open each session for exactly what it covers:</p>
  <div class="faq">

    <details><summary>Session 1 &middot; Thu 24 September &middot; Scope, the landscape, and who owns what</summary><div class="faq__a"><p>The policy statement and scope, including what counts as AI: chatbots and content generators, the AI features inside software you already use, and AI reached through personal and wearable devices. The legal and statutory landscape your policy sits in, from KCSIE 2026 and the Data (Use and Access) Act amendments to the DfE standards, the Online Safety Act and Ofcom’s codes. Then roles and oversight: what your trustees or governors own, what sits with senior leadership, your AI or digital lead, DPO, DSL, filtering and monitoring lead and IT lead, and how AI gets onto your risk register and into assurance reporting. Between sessions you complete these sections in the workbook.</p></div></details>

    <details><summary>Session 2 &middot; Thu 15 October &middot; Approved tools and acceptable use</summary><div class="faq__a"><p>How a tool gets approved: the route from request through DPIA to the approved list, who approves, and how changes are communicated. Then what staff may and must not do: organisation accounts rather than personal ones, the rule that no personal or special category data goes into AI tools and the reasons behind it (including why a name alone can skew what a model produces), the high-risk prohibitions, and the five non-negotiables you may reword but mustn’t weaken.</p></div></details>

    <details><summary>Session 3 &middot; Thu 22 October &middot; Data protection, and a live DPIA</summary><div class="faq__a"><p>The data protection spine: whose data it is, lawful basis, controller and processor roles, contracts and sub-processors, international transfers, retention, and the rules for AI note-takers, meeting transcription and recording. Then impact assessment done properly: when a DPIA is required, the DfE generative AI product safety checks, and a <strong>live DPIA screening, start to finish, on a real product</strong> using the screening tool, so you’ve seen the whole process before you run your own.</p></div></details>

    <details><summary>Session 4 &middot; Thu 12 November &middot; Safeguarding, oversight and enforcement</summary><div class="faq__a"><p>Safeguarding and Prevent as they apply to AI: deepfakes, nudification tools, voice cloning and fraud, and how AI concerns travel your existing safeguarding routes. Accuracy and human oversight: meaningful human involvement as a legal test, bias and the Equality Act, and who owns an AI-assisted decision. Then enforcement: filtering and monitoring, shadow AI and how to stop it becoming the norm, and the assurance your board should receive.</p></div></details>

    <details><summary>Session 5 &middot; Thu 26 November &middot; Training, incidents, pupils, and ratification</summary><div class="faq__a"><p>The training and awareness your staff actually need and how to evidence it. Breach and incident routes, decided before you need them. Whether to switch on the optional pupil-use module, and what the ICO Children’s Code and JCQ rules require if you do. Then the finish line: taking the policy through your stakeholders, presenting it to governors or trustees using the ratification pack, and keeping it current as guidance moves.</p></div></details>

  </div>

  <p>Sessions aren’t recorded, deliberately, so people can speak freely about where their organisation actually is. The slides, workbook and weekly round-up carry everything you need if you have to miss one. Finishing in November is deliberate: your completed policy reaches your governors or trustees before Christmas, and the spring term starts with it in force. A single training day gives you momentum; a term of structured sessions gets the policy finished, approved and in force. It’s the work I’ve been doing with schools, trusts and colleges for years, at a fraction of what one-to-one consultancy costs.</p>

  <h2>What you get</h2>
  <p>For one price, your organisation gets all of this:</p>
  <ul>
    <li><strong>Five live ninety-minute sessions</strong>, for every seat in your tier, with the slides and workbook pages following every session.</li>
    <li><strong>The cohort workbook</strong>: a section-by-section completion checklist for the entire policy, so at every stage you know exactly what “done” looks like and can check your own draft against it.</li>
    <li><strong>Your questions answered, every week</strong>: send them in by Friday and I answer the themes for the whole cohort, at the start of the next session and in a short written round-up. If you’re wondering it, someone else in the room is too.</li>
    <li><strong>A live DPIA screening on a real product</strong> in session three, using the free screening tool you may already have.</li>
    <li><strong>The ratification pack</strong>: a model paper for presenting the policy to your governors or trustees, and an adoption checklist for the weeks after ratification.</li>
    <li><strong>For large trusts</strong>: a private one-to-one session with me on your trust-specific rollout.</li>
  </ul>

  <h2>The investment</h2>
  <p>Five tiers, priced by the size of the job. If you’re genuinely unsure which fits, email me and I’ll tell you straight.</p>
  <div class="pricing-wrap">
  <table class="pricing">
    <thead>
      <tr><th scope="col">Tier</th><th scope="col">Who it&rsquo;s for</th><th scope="col" class="num">Seats</th><th scope="col" class="num">Price</th></tr>
    </thead>
    <tbody>
      <tr><td class="tier">Small school</td><td>Primaries of one-form entry or smaller, first, infant and junior schools, and special schools</td><td class="num">2</td><td class="num price">&pound;495</td></tr>
      <tr><td class="tier">Larger primary</td><td>Primaries of two-form entry or more</td><td class="num">2</td><td class="num price">&pound;695</td></tr>
      <tr><td class="tier">Secondary, all-through or college</td><td>Any secondary or all-through school, sixth form or FE college</td><td class="num">3</td><td class="num price">&pound;995</td></tr>
      <tr><td class="tier">Small trust</td><td>Multi-academy trusts and federations of two to seven schools, adopting one policy centrally</td><td class="num">3</td><td class="num price">&pound;1,450</td></tr>
      <tr><td class="tier">Large trust</td><td>Trusts of eight schools or more. Includes a private one-to-one session with me on your trust-specific rollout</td><td class="num">3</td><td class="num price">&pound;1,950</td></tr>
    </tbody>
  </table>
  </div>
  <p>The price is <strong>one-off, for the whole programme</strong>: all five sessions, the workbook, the weekly round-ups, and everything above. Nothing recurs, and there’s nothing else to buy. The programme runs across the autumn term, late September to early December.</p>
  <p><strong>Reserve and invoice by Friday 11 September and take 10% off any tier.</strong> I don’t charge VAT, so the price is the price, and your invoice confirms your place. One policy, one organisation, one booking: the trust tiers exist so a trust doesn’t buy a school place and share it around.</p>

  <h2>Reserve your place</h2>
  <p>Email me with your organisation’s name and which tier fits, and I’ll come back to you with everything you need. No payment until you’ve seen the dates and confirmed.</p>
  <p><a class="btn btn--solid" href="mailto:mark@ictevangelist.com?subject=Autumn%20cohort%20place">Reserve a place</a></p>

  <p class="chart-note">The cohort supports you in completing and ratifying your own policy; it isn’t legal advice, and responsibility for compliance rests with the adopting organisation, as it does for the template itself.</p>
""" + pagenav(("policy-template.html", "Get the template"), None)

write("cohort.html", "The autumn cohort | " + build.BRAND_TITLE,
      "Work through the Use of AI Policy template with Mark Anderson and a small group of schools, trusts and colleges: five sessions to a completed, ratified policy.",
      cohort_body, ORG_LD)
# Unlisted until launch: reachable only by direct link, invisible to search.
_ch = build.OUT / "cohort" / "index.html"
_ch.write_text(_ch.read_text(encoding="utf-8").replace(
    '<meta name="robots" content="index, follow">',
    '<meta name="robots" content="noindex, nofollow">'), encoding="utf-8")

# ------------------------------------------------ PRIVACY NOTICE
priv_body = banner("Legal", '<span class="accent">Privacy notice</span>',
  "How this site handles information, including the sign-up you complete to unlock the DPIA screening tool.", crumbs=True) + f"""
  <p class="lead">This is a site about data protection, so it ought to hold itself to the same standard. In plain terms, here’s what I do and don’t collect.</p>

  <h2>The site itself</h2>
  <p>These pages are plain, self-contained static files. They make no advertising or profiling calls. Your reading-controls preferences (text size, contrast, spacing) are stored only in your own browser’s local storage, on your device, and are never sent anywhere.</p>
  <p>The <strong>DPIA screening tool</strong> you download runs entirely in your browser. Nothing you type into it is transmitted to me or anyone else; it stays on your device unless you choose to save, print or send it.</p>

  <h2>Analytics, only with your agreement</h2>
  <p>I use <strong>Google Analytics</strong> to understand how the site is being used: how many people visit, which pages they read, and roughly where in the world they’re reading from. It doesn’t run by default. On your first visit you’re asked whether you’re happy for it to, and <strong>nothing loads, and no cookies are set, unless you say yes</strong>. Saying no thanks changes nothing about what you can read or download.</p>
  <p>If you do agree, Google Analytics sets cookies in your browser and sends usage data to Google, which processes it on my behalf. What I see is aggregated (page views, visit counts, general location, device type) and I can’t identify you from it. Google Analytics 4 doesn’t log or store visitors’ IP addresses. Your choice, whichever way you make it, is kept in your browser’s local storage so you aren’t asked again on every visit.</p>
  <p id="consent-status">With JavaScript switched off, analytics never loads at all.</p>
  <p><button type="button" id="consent-manage" class="btn btn--solid">Change my analytics choice</button></p>

  <h2>The sign-up form</h2>
  <p>To unlock the DPIA screening tool I ask you to complete a short form. That form is a <strong>Google Form</strong>, and the information you enter is processed by Google on my behalf as a data processor. Here’s the detail:</p>
  <div class="data-table-wrap">
  <table class="data">
    <tbody>
      <tr><th scope="row">Who is responsible (controller)</th><td>Me, Mark Anderson (ICT Evangelist), the data controller for sign-ups.</td></tr>
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
  <p>To exercise any right, or to ask a question about this notice, contact me, <strong>Mark Anderson (ICT Evangelist)</strong>, via <a href="https://ictevangelist.com">ictevangelist.com</a>. If you’re unhappy with how I’ve handled your information, you can complain to the Information Commissioner’s Office (ICO) at <a href="https://ico.org.uk">ico.org.uk</a>.</p>

  <p class="chart-note">This notice covers this website, its analytics and its sign-up form. It was last reviewed when analytics was added, and will be updated whenever what’s collected, or how it’s processed, changes.</p>
""" + pagenav(("policy-template.html", "Get the template"), None)

write("privacy.html", "Privacy notice | " + build.BRAND_TITLE,
      "How this site handles information: analytics that only runs with your agreement, and a plain-English notice for the Google Form sign-up used to unlock the DPIA tool.",
      priv_body, ORG_LD)

print("Tool, template and privacy pages written.")
