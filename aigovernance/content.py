#!/usr/bin/env python3
# Content + page assembly for aigovernance.ictevangelist.com
# Run: python3 content.py   (imports the engine in build.py, writes all pages)
from build import (write, banner, guidance_box, keypoints, nonneg, pagenav,
                   FOOTER, head, nav_html, SITE, BRAND_TITLE, AUTHOR, link,
                   tie_orphans, clean_urls)
import html as _h

# ---- Verified official source URLs (open in a new tab via build.link) ----
U = {
 'kcsie':      'https://www.gov.uk/government/publications/keeping-children-safe-in-education--2',
 'ukgdpr':     'https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/',
 'dpa2018':    'https://www.legislation.gov.uk/ukpga/2018/12/contents',
 'duaa':       'https://www.legislation.gov.uk/ukpga/2025/18/contents',
 'ico_ai':     'https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/',
 'ico_toolkit':'https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/ai-and-data-protection-risk-toolkit/',
 'childrens':  'https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/',
 'equality':   'https://www.legislation.gov.uk/ukpga/2010/15/contents',
 'psed':       'https://www.gov.uk/government/publications/public-sector-equality-duty-guidance-for-public-authorities/public-sector-equality-duty-guidance-for-public-authorities',
 'dfe_genai':  'https://www.gov.uk/government/publications/generative-artificial-intelligence-in-education',
 'dfe_safety': 'https://www.gov.uk/government/publications/generative-ai-product-safety-standards/generative-ai-product-safety-standards',
 'jcq':        'https://www.jcq.org.uk/knowledge-hub/ai-use-in-assessments-your-role-in-protecting-the-integrity-of-qualifications/',
 'dfe_stds':   'https://www.gov.uk/guidance/meeting-digital-and-technology-standards-in-schools-and-colleges',
 'dfe_filter': 'https://www.gov.uk/guidance/meeting-digital-and-technology-standards-in-schools-and-colleges/filtering-and-monitoring-core-standard',
 'dfe_cyber':  'https://www.gov.uk/guidance/meeting-digital-and-technology-standards-in-schools-and-colleges/cyber-security-core-standard',
 'dfe_gov':    'https://www.gov.uk/guidance/meeting-digital-and-technology-standards-in-schools-and-colleges/digital-leadership-and-governance-standards',
 'osa':        'https://www.legislation.gov.uk/ukpga/2023/50/contents',
 'ofcom':      'https://www.ofcom.org.uk/online-safety/protecting-children/protection-of-children-duties-under-the-online-safety-act',
 'prevent':    'https://www.gov.uk/government/publications/prevent-duty-guidance',
 'wttsc':      'https://www.gov.uk/government/publications/working-together-to-safeguard-children--2',
 'ath':        'https://www.gov.uk/guidance/academy-trust-handbook',
 'sfvs':       'https://www.gov.uk/government/publications/schools-financial-value-standard-sfvs',
 'dp_schools': 'https://www.gov.uk/guidance/data-protection-in-schools',
 'edtech':     'https://ico.org.uk/action-weve-taken/audits-and-overview-reports/2026/06/edtech/',
}

ORG_LD = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "ICT Evangelist",
    "url": "https://ictevangelist.com",
    "founder": "Mark Anderson",
}

# ---------------------------------------------------------------- HOME
home_body = f"""<section class="hero">
  <div class="container">
    <p class="eyebrow">AI governance in education</p>
    <h1>Get AI governance right in your school or trust.</h1>
    <p class="lede">I’ve put this site together as a plain-English companion to my <strong>Use of Artificial Intelligence (AI) Policy</strong> template. It walks you through what you’ll need to decide, why each decision matters, and the law and guidance that sits behind it all. Written for adoption from <strong>September 2026</strong>.</p>
    <div class="btn-row">
      <a class="btn btn--solid" href="policy-template.html">Get the policy template</a>
      <a class="btn btn--ghost" href="dpia-tool.html">Unlock the DPIA screening tool</a>
    </div>
    <div class="partner-lockup">
      <span>By</span>
      <img src="assets/ict-evangelist-logo-white.png" alt="ICT Evangelist">
    </div>
  </div>
</section>

<section class="section"><div class="container">
  <p class="lead section-intro">AI is already in your classrooms and your offices: inside the everyday software your staff use, and a browser tab away for anyone who wants it. Good governance makes sure your use of AI is <strong>safe, lawful and defensible</strong>, so you get the benefits without putting at risk the safety of children and adults, the privacy of their data, fairness, or professional integrity.</p>

  <h2 style="margin-top:2.4rem;">Where this work comes from</h2>
  <p>Back in 2023 I published a free {link("Use of AI in Education policy template", "https://ictevangelist.com/free-resource-use-of-artificial-intelligence-ai-in-education-school-policy-template/")} that I hoped would be useful. What I didn’t expect was just how many schools would download it and put it to work. When Ofsted set out its approach to AI in 2024, I responded with {link("ten actionable insights to build on it", "https://ictevangelist.com/enhancing-ofsteds-policy-paper-on-ai-with-actionable-insights/")}, and in 2025 I {link("updated the template", "https://ictevangelist.com/ai-policy-template-2025/")} against the DfE’s policy paper on generative AI.</p>
  <p>Over the last decade I’ve worked with hundreds of schools, trusts and organisations worldwide on digital strategy, governance, policy and training — and before I first published that template, I’d already helped dozens of schools and trusts develop their own. This site brings all of that together: everything I’ve learned about AI policy, rewritten for the framework that applies from September 2026.</p>

  <h2 class="mt-0" style="margin-top:2rem;">Start wherever suits you</h2>
  <div class="card-grid" style="margin-top:1.2rem;">
    <a class="card card--link" href="landscape.html"><h3>The landscape</h3><p>Why you need a policy now, what counts as “AI”, and the law and guidance that applies to you.</p><span class="more">Read &rsaquo;</span></a>
    <a class="card card--link" href="approved-tools.html"><h3>Approved tools</h3><p>The heart of the policy: how a tool becomes approved, and why “not approved” is the starting point.</p><span class="more">Read &rsaquo;</span></a>
    <a class="card card--link" href="data-protection.html"><h3>Data protection</h3><p>The rule on personal data, your lawful basis, controllers and processors, and how long data is kept.</p><span class="more">Read &rsaquo;</span></a>
    <a class="card card--link" href="impact-assessment.html"><h3>Impact assessment</h3><p>When you need a DPIA, what a product-safety check covers, and a free tool to get you started.</p><span class="more">Read &rsaquo;</span></a>
    <a class="card card--link" href="safeguarding.html"><h3>Safeguarding &amp; Prevent</h3><p>Deepfakes, online-safety duties, and how an AI concern reaches your designated safeguarding lead.</p><span class="more">Read &rsaquo;</span></a>
    <a class="card card--link" href="pupil-use.html"><h3>Pupil use</h3><p>The optional module, and the two conditions to meet before pupils use AI at all.</p><span class="more">Read &rsaquo;</span></a>
  </div>

  <h2>The non-negotiables</h2>
  <p>As with many policies there need to be non-negotiables that help colleagues understand what they can and what they can’t do. In this AI policy there are 5 distinct areas which really must be non-negotiables. I’ve explained below what each of them are and why they are so important that they are, non-negotiable…</p>
  <div class="card-grid">
    <div class="card"><h3>No personal data in</h3><p>Personal or special-category data doesn’t go into AI tools. The only exception is a tool that’s been approved for that exact processing. Once information about a real child or colleague is inside a tool you don’t control, you can’t get it back.</p></div>
    <div class="card"><h3>A person always decides</h3><p>AI never makes a decision about a person. A named member of staff makes, and owns, any decision that affects someone. Accountability has to sit with a person; it can’t sit with a piece of software.</p></div>
    <div class="card"><h3>A DPIA before you deploy</h3><p>You should complete a data protection impact assessment before deploying AI that processes personal data. An assessment completed after a tool is in use can’t change the decision to use it.</p></div>
    <div class="card"><h3>Approved tools only</h3><p>Staff use approved tools only, through organisation accounts. Anything else, including public chatbots on a personal login, isn’t approved. Without that approval process, none of the other rules in the policy can be enforced.</p></div>
    <div class="card"><h3>Safeguarding duties hold</h3><p>Your Prevent, safeguarding and online-safety duties apply to AI-assisted work exactly as they do to everything else. New technology doesn’t change those duties.</p></div>
  </div>

  <h2>Two resources to take away</h2>
  <div class="card-grid">
    <a class="card card--link" href="policy-template.html"><h3>The policy template &darr;</h3><p>My completable <em>Use of AI Policy</em> for schools, trusts and colleges: a staff-use core, with optional modules for pupil use and governed exceptions.</p><span class="more">Download &rsaquo;</span></a>
    <a class="card card--link" href="dpia-tool.html"><h3>The DPIA screening tool &darr;</h3><p>A plain-English tool that runs in your browser, for any AI or digital product you’re thinking of buying. Complete it, save it, and send it to your DPO.</p><span class="more">Unlock &rsaquo;</span></a>
  </div>

  <h2>Need more than a template?</h2>
  <p>If your school or trust needs support writing or refining your AI policy, or training staff to use AI well, that’s exactly the work I do. <a href="mailto:mark@ictevangelist.com?subject=AI%20policy%20support">Get in touch</a> or find me at {link("ictevangelist.com", "https://ictevangelist.com/contact/")}. And if the template or the screening tool has helped you, I’d love to hear about it — feedback is always welcome.</p>

  <h2>Your questions, answered</h2>
  <div class="faq">
    <details><summary>Does every school need its own AI policy?</summary><div class="faq__a"><p>You need a position that’s yours, and that your stakeholders have agreed. If you’re a multi-academy trust, adopt one policy centrally and hold school-level detail in local appendices rather than running separate versions. The template is written to be completed for your setting, not used as it stands.</p></div></details>
    <details><summary>Are pupils covered by the policy?</summary><div class="faq__a"><p>Not by default. Pupils come into scope only when you switch on the optional pupil-use module, and only once a DPIA is complete and age-appropriate teaching about AI is in place.</p></div></details>
    <details><summary>Can staff just use ChatGPT for work?</summary><div class="faq__a"><p>Only if your organisation has approved it, and only through an organisation-provided account. Personal accounts aren’t used for work, and public consumer chatbots aren’t approved by default.</p></div></details>
    <details><summary>When do we need a DPIA?</summary><div class="faq__a"><p>Before you deploy AI that processes personal data, and wherever a tool is likely to create a high risk to people. Doing it early, before the decision is made, is what the DfE guidance expects. The <a href="dpia-tool.html">screening tool</a> helps you judge whether you’re ready.</p></div></details>
  </div>
</div></section>"""

home_ld = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": "Does every school need its own AI policy?",
         "acceptedAnswer": {"@type": "Answer", "text": "You need a position that's yours and that your stakeholders have agreed. If you're a multi-academy trust, adopt one policy centrally and hold school-level detail in local appendices. The template is completed for your setting, not used as it stands."}},
        {"@type": "Question", "name": "Are pupils covered by the policy?",
         "acceptedAnswer": {"@type": "Answer", "text": "Not by default. Pupils come into scope only when you switch on the optional pupil-use module, and only once a DPIA is complete and age-appropriate teaching about AI is in place."}},
        {"@type": "Question", "name": "Can staff just use ChatGPT for work?",
         "acceptedAnswer": {"@type": "Answer", "text": "Only if your organisation has approved it, and only through an organisation-provided account. Personal accounts aren't used for work, and public consumer chatbots aren't approved by default."}},
        {"@type": "Question", "name": "When do we need a DPIA?",
         "acceptedAnswer": {"@type": "Answer", "text": "Before you deploy AI that processes personal data, and wherever a tool is likely to create a high risk to people. Doing it early, before the decision is made, is what DfE guidance expects."}},
    ],
}

home_doc = head(BRAND_TITLE + " — a companion to the Use of AI Policy template",
                "Plain-English guidance on AI governance for schools, trusts and colleges: tool approval, data protection, safeguarding, DPIAs and a free policy template. Written for September 2026.",
                SITE + "/", home_ld).replace("{NAV_PLACEHOLDER}", nav_html("index.html")) + home_body + FOOTER
(__import__("pathlib").Path(__file__).parent / "index.html").write_text(clean_urls(tie_orphans(home_doc)), encoding="utf-8")
print("wrote index.html")

# ---------------------------------------------------------------- TOPIC PAGES
# Each: (slug, nav_title, kicker, h1, sub, body_inner_html, guidance_items, prev, next)
G_DP = (link("UK GDPR", U['ukgdpr']) + " &amp; " + link("Data Protection Act 2018", U['dpa2018'])
        + " (as amended by the " + link("Data (Use and Access) Act 2025", U['duaa']) + "); "
        + link("ICO guidance on AI", U['ico_ai']) + " and the "
        + link("ICO AI &amp; data protection risk toolkit", U['ico_toolkit']) + ".")
G_CC = link("ICO Children’s Code", U['childrens']) + ", wherever children’s data is involved."
G_KCSIE = link("Keeping Children Safe in Education 2026", U['kcsie']) + " — the statutory safeguarding baseline from 1 September 2026."
G_DFE_SAFETY = (link("DfE position on generative AI in education", U['dfe_genai']) + " and the "
                + link("DfE generative AI product safety standards", U['dfe_safety']) + " (January 2026).")
G_EQ = (link("Equality Act 2010", U['equality']) + " and, for public bodies, the "
        + link("public sector equality duty", U['psed']) + ".")
G_JCQ = link("JCQ guidance on AI use in assessments", U['jcq']) + ", where qualifications are involved."
G_OSA = (link("Online Safety Act 2023", U['osa']) + " and the "
         + link("Ofcom Protection of Children code of practice", U['ofcom']) + ".")
G_PREVENT = (link("Prevent duty guidance (2023)", U['prevent']) + " and "
             + link("Working Together to Safeguard Children 2026", U['wttsc']) + ".")
G_STANDARDS = ("the DfE " + link("filtering &amp; monitoring", U['dfe_filter']) + ", "
               + link("cyber security", U['dfe_cyber']) + ", and "
               + link("digital leadership &amp; governance", U['dfe_gov']) + " standards.")

PAGES = []

PAGES.append(("landscape.html", "The landscape", "Sections 1–2 of the template",
  "The landscape: why govern AI, and what applies to you",
  "Before any rule: why you’d govern AI at all, what counts as “AI” here, and the law and guidance the policy sits within.",
  f"""
  <p class="lead">A good AI policy starts with why you’re adopting AI in the first place: what it’s there to help with in your setting, whether that’s teaching, workload or inclusion. Set that out before any rule appears. The governance is there to serve that purpose, not to get in its way.</p>

  <h2>What it is</h2>
  <p>The policy statement sets out how your organisation uses AI: by whom, for what, and within what limits, so you get the benefits without putting at risk the safety of children and adults, data security and privacy, fairness, or professional and academic integrity. It sits within your wider digital strategy. You should review it on a set cycle, and again whenever the law, the guidance, or your own use of AI changes in any material way. AI develops at pace, so treat that cycle as a minimum rather than a formality. At the time of writing, amendments to bring AI chatbots within the Online Safety Act are expected; treat their passage, or any change to KCSIE or the DfE’s AI guidance, as a trigger for review ahead of your normal cycle.</p>
  <p><strong>What counts as AI here.</strong> Generative AI tools, and any software feature that creates content, or that makes or informs decisions or predictions about people. That holds whether the feature is a standalone product, built into software you already approve, or reached through a browser. In practice, it means chatbots, image and content generators, and the AI features now appearing inside everyday software. It also includes AI reached through personal and wearable devices — smart glasses and other recording-capable kit — whenever it’s used in connection with the organisation’s work. Long-established automation such as spellcheck or predictive text is out of scope, unless it starts doing one of those things.</p>

  <h2>Why it’s important</h2>
  <p>AI rarely arrives through one obvious route. It turns up inside the platforms you already license, and it’s a browser tab away for any member of staff. If your policy only covers “the AI tool we bought”, it’ll miss most of your real exposure. The template therefore defines scope by what a tool <em>does</em>: does it generate content, or make or inform decisions about people? Scoped that way, your policy stays relevant as products change around you.</p>
  <p>There’s an inspection angle too. When Ofsted visits, schools and trusts will increasingly need to show how they manage the risks that come with AI — data privacy, intellectual property, bias and ethics — how they comply with safeguarding and data governance duties, and how they use AI to support workload, accessibility and equity. Similar expectations apply to British Schools Overseas and to independent schools inspected by ISI, whose frameworks follow the same lines.</p>
  <p>If you’re a multi-academy trust, my advice is to adopt one policy centrally and hold school-level detail in local appendices. I’ve seen separate versions drift apart over time, and they become very hard to assure.</p>

  {keypoints("What you decide here", [
    "Your reasons for adopting AI: a sentence or two on what it’s there to help with in your setting.",
    "Your organisation name, review cycle, and who is in scope (usually all staff, governors, trustees, volunteers and contractors).",
    "Any platform AI features that are governed by a separate assessment, noted so the boundary is clear.",
    "Whether pupils are in scope. They aren’t, by default, until the optional module’s conditions are met.",
  ])}

  {guidance_box([G_KCSIE, G_DP, G_CC, G_EQ, G_DFE_SAFETY, G_JCQ, G_STANDARDS, G_OSA, G_PREVENT,
                 "The financial governance framework that applies to you: the " + link("Academy Trust Handbook", U['ath']) + "; the scheme for financing schools and the " + link("Schools Financial Value Standard", U['sfvs']) + "; or a college’s corporation framework.",
                 "You can see them all, with what each one requires, on the <a href='guidance-map.html'>guidance map</a>."])}
  """,
  None, None, ("index.html", "Home"), ("roles.html", "Roles & oversight")))

PAGES.append(("roles.html", "Roles & oversight", "Section 3 of the template",
  "Roles, responsibilities &amp; oversight",
  "Governance only works when every responsibility has a name against it. Treat this list of roles as a menu, and cut it to the ones you have.",
  f"""
  <p class="lead">Governance only works when every responsibility has somebody’s name against it. Section 3 sets out who owns what, so nothing important falls into the gap between roles.</p>

  <h2>What it is</h2>
  <p>A list of roles and what each one owns. Delete the roles you don’t have, merge them where one person carries several, and reassign anything left over to whoever will pick it up. The usual owners are:</p>
  <ul>
    <li><strong>Trustees or the governing board</strong> — strategic oversight and assurance; making sure AI is on the risk register; receiving regular reporting on adoption, incidents, breaches and changes to the approved list.</li>
    <li><strong>Senior leadership</strong> — approving the policy and any material changes; approving tools where named as the approver; commissioning the periodic AI risk review.</li>
    <li><strong>AI or digital lead</strong> — owning the approved list and the approval process; keeping the policy and staff guidance current; being the first point of contact for questions.</li>
    <li><strong>Data protection officer or lead</strong> — coordinating impact assessments; advising on lawful basis and processing agreements; receiving reports of data entered in error.</li>
    <li><strong>Designated safeguarding lead</strong> — receiving safeguarding and Prevent concerns that involve AI; advising on the safeguarding implications of proposed uses.</li>
    <li><strong>Filtering and monitoring lead</strong> — the senior named owner of your filtering and monitoring arrangements.</li>
    <li><strong>IT or network lead</strong> — running access, security, filtering and monitoring controls; blocking unapproved services; including AI in cyber reviews.</li>
  </ul>

  <h2>Why it’s important</h2>
  <p>The DfE governance standards expect clear lines of accountability, and the ICO’s edtech audits found, time and again, responsibilities that everyone assumed somebody else was holding. Putting a name against each line means you can assure it properly, and report on it to your board with confidence.</p>

  {keypoints("What you decide here", [
    "A named owner for every responsibility you keep.",
    "Your reporting cycle to trustees or governors, for example each term.",
    "Where the AI or digital lead and the DPO sit, and how they hand work over to each other.",
  ])}

  {guidance_box([G_STANDARDS, G_DP, link("Academy Trust Handbook", U['ath']) + ", and your wider financial governance framework, for oversight and assurance duties."])}
  """,
  None, None, ("landscape.html", "The landscape"), ("approved-tools.html", "Approved tools")))

PAGES.append(("approved-tools.html", "Approved tools", "Sections 4 &amp; 4a of the template",
  "Approved tools &amp; how tools are approved",
  "The heart of the whole policy. If you keep only one thing intact, keep this.",
  f"""
  <p class="lead">Staff may use AI for work only through tools your organisation has approved, and only through organisation-provided accounts. Everything else is off-limits by default. That starting point is deliberate.</p>

  <h2>What it is</h2>
  <p>A single, clear approval process that every tool goes through before it’s used for work. The approved list names each tool and what it’s approved <em>for</em>. Anything not on that list, including public consumer chatbots and anything reached through a personal login, isn’t approved and isn’t used. One point catches people out: <strong>a new AI feature that appears inside a product you already approve isn’t approved by default</strong>. It goes back through the same process before anyone uses it. (The policy template refers to this process as the approval gate.)</p>
  <p><strong>Governed exceptions (section 4a, optional).</strong> Include these only if you choose to permit named tools for single, tightly-defined purposes, with the same scrutiny applied and the exception written down rather than assumed.</p>

  <h2>Why it’s important</h2>
  <p>Without an approval process, rules like “no personal data into AI” or “a DPIA before deployment” can’t be enforced. With one, the important questions — what data the tool uses, your lawful basis for it, and what the supplier does with it — are answered before the tool is in daily use, not discovered afterwards. The DfE product safety standards and the ICO’s audit findings both point the same way: assess before you adopt.</p>

  {nonneg("Tool approval is a non-negotiable, and so is the rule that a new AI feature inside an existing product comes back through it. “We already use this supplier” isn’t the same as approval.")}

  {keypoints("What you decide here", [
    "Which tools you approve, and the specific purpose each one is approved for.",
    "Who approves additions, and how a member of staff requests one.",
    "Whether you permit any governed exceptions (4a), and how they’re recorded.",
    "How the approved list is published, and how staff know what’s blocked.",
  ])}

  <p>Assessing a particular product? The <a href="dpia-tool.html">DPIA screening tool</a> takes you through the questions your approval process should be asking.</p>

  {guidance_box([G_DFE_SAFETY, G_DP, G_STANDARDS, link("DfE guidance on procuring edtech and data protection in schools", U['dp_schools']) + "."])}
  """,
  None, None, ("roles.html", "Roles & oversight"), ("acceptable-use.html", "Acceptable use")))

PAGES.append(("acceptable-use.html", "Acceptable use", "Sections 5 &amp; 6 of the template",
  "Acceptable use: what staff may and must not do",
  "The everyday rules. Tailor the examples to your setting, and keep the rule on data input and the high-risk prohibitions intact.",
  f"""
  <p class="lead">This is the part of the policy your staff will read most, so make the examples concrete and local, and keep the boundaries firm.</p>

  <h2>What staff may do</h2>
  <p>Set out the low-risk, genuinely helpful uses you want to encourage: drafting and adapting resources, summarising, planning, routine administrative writing. Always through approved tools and organisation accounts, and always with a person checking the output before it’s used.</p>

  <h2>What staff must not do</h2>
  <ul>
    <li>Use AI tools that haven’t been approved, or try to get around filtering or monitoring to reach a blocked service.</li>
    <li>Enter personal or special-category data, meaning information about real, identifiable people, into an AI tool, unless it’s been approved for that specific purpose.</li>
    <li>Let AI make a decision about a person. In sensitive areas, even assistive use is prohibited unless it’s been expressly authorised, with a named person making and owning the decision.</li>
    <li>Pass off AI-generated material as their own unaided work where that would mislead, or break the JCQ rules on AI in assessments (which also rule out relying on AI as the sole marker of a student’s work).</li>
    <li>Upload third-party copyrighted or licensed material, such as published schemes of work, textbooks or exam papers, without the rights to do so.</li>
  </ul>

  <h2>Why it’s important</h2>
  <p>In my experience, by far the most common way personal data ends up in an AI tool isn’t a technical breach. It’s a well-meaning colleague pasting a name, a report or a case note into a chatbot to save a bit of time.</p>
  <p>A common misconception makes this worse: that once a tool has been through a DPIA, personal names and details can go into it. That isn’t what approval means. A DPIA approves a tool for specific, defined processing — if entering personal data wasn’t part of that assessment, it isn’t approved, however safe the tool feels to use.</p>
  <p>And the reasons for keeping personal information out go well beyond compliance. A name on its own can skew what a model produces: names carry signals about gender, ethnicity, religion and background, and outputs can shift with them — a difference in treatment nobody would accept from a member of staff, and no more acceptable from a tool. Then the data protection problems stack on top: once information about a real person is inside a tool you don’t control, you can’t reliably retrieve or delete it, you may have no lawful basis for putting it there, and the person it describes has no idea it’s happened.</p>
  <p>So the working rule is simple, and worth teaching explicitly: no personal information goes in. Draft with initials, pseudonyms or placeholders, and add the personal detail after the output comes back. That’s why the rule on what goes in is the one boundary you shouldn’t soften locally — and why the high-risk prohibitions exist: these are the decisions where an automated shortcut can cause the biggest problems.</p>

  {nonneg("The rule against entering personal or special-category data into AI tools, and the principle that a person always decides, are non-negotiable. Tailor the examples around them; don’t remove the substance.")}

  {guidance_box([G_DP, G_JCQ, G_EQ, "Copyright and licensing law, for third-party materials.",
                 "Your acceptable-use, data protection and academic-integrity policies, read alongside this one."])}
  """,
  None, None, ("approved-tools.html", "Approved tools"), ("data-protection.html", "Data protection")))

PAGES.append(("data-protection.html", "Data protection", "Section 7 of the template",
  "Data protection &amp; information security",
  "Whose data, on what lawful basis, in whose hands, and for how long. These are the questions that decide whether a tool is lawful to use.",
  f"""
  <p class="lead">Data protection is where most of the risk in AI-for-education sits. Get four things clear — whose data it is, your lawful basis, the supplier’s role, and how long data is kept — and most of the rest follows.</p>

  <h2>What it is</h2>
  <p>The section that fixes how personal data is handled when AI is involved: the rule that personal and special-category data stays out of AI tools; your lawful basis for any processing you do approve; the controller and processor relationship with each supplier; retention and deletion; and the route by which data entered in error is reported and dealt with.</p>

  <h2>Why it’s important</h2>
  <p><strong>Controller or processor is the sector’s most common failing.</strong> Normally your school or trust decides why and how data is used (the controller) and the supplier only acts on your instructions (the processor). But the label in the contract doesn’t settle it; what the supplier actually does settles it. If a supplier uses the data for its own purposes, such as product development, analytics or improving its AI, it’s acting as a controller for that use, extra rules apply (including the Children’s Code where pupils are involved), and you should be asking why it needs to do this at all.</p>
  <p><strong>Your lawful basis is rarely consent.</strong> For most of what a school does, the basis is public task: part of running the school and educating pupils. Don’t confuse a tool’s terms requiring parent or guardian agreement with your lawful basis. They’re two different things.</p>
  <p><strong>Free text is easy to overlook.</strong> A tool that only asks for a name and email can still process sensitive information the moment someone types into a free-text box. The protection comes from the rule on what staff may enter, not from the sign-up form.</p>
  <p><strong>Recording and transcription need their own rules.</strong> AI note-takers and meeting transcription features capture people’s words and voices: personal data gathered at source, and often special category data in pastoral, SEND or safeguarding discussions. The policy permits them only where approved for that purpose, expects everyone present to be told before recording begins, offers an alternative to anyone who objects, and treats transcripts as organisational records held under your retention arrangements — not left sitting on the provider’s platform.</p>

  {keypoints("What good looks like", [
    "Personal data stays out of AI tools by default; any exception is approved and written down.",
    "Each supplier’s role, controller or processor, is settled by what it actually does.",
    "A valid lawful basis is recorded, usually public task, rarely consent.",
    "Retention is configurable and kept short where possible, and the exit position (data deleted or returned) is in the contract.",
    "International transfers are covered by an approved arrangement, and you know who the sub-processors are and are told when they change.",
  ])}

  {nonneg("A DPIA is completed before you deploy AI that processes personal data. Complete it as part of making the decision, not as paperwork afterwards.")}

  <p>The <a href="dpia-tool.html">DPIA screening tool</a> helps you work through roles, transfers, retention and sub-processors for a particular product.</p>

  {guidance_box([G_DP, G_CC, link("DfE guidance on procuring edtech and data protection in schools", U['dp_schools']) + "; the ICO’s " + link("<em>Edtech examined</em> audit findings", U['edtech']) + ".", G_DFE_SAFETY])}
  """,
  None, None, ("acceptable-use.html", "Acceptable use"), ("accuracy-oversight.html", "Accuracy & oversight")))

PAGES.append(("accuracy-oversight.html", "Accuracy & oversight", "Section 8 of the template",
  "Accuracy, bias, accountability &amp; human oversight",
  "AI produces drafts, not decisions. This section keeps a named person accountable for everything that leaves the building.",
  f"""
  <p class="lead">Generative AI produces fluent, plausible text, and it’s wrong often enough that nothing should go out on its say-so. Treat what it produces as a first draft that a professional checks, corrects and takes responsibility for.</p>

  <h2>What it is</h2>
  <p>The commitments on accuracy and human oversight: outputs are reviewed by a competent person before use; AI is never the sole basis of a decision about a person; bias and fairness are considered rather than assumed away; and accountability for any AI-assisted work stays with the person who used the tool. Where AI has done substantial drafting of something that matters, the section sets out what should be disclosed.</p>

  <h2>Why it’s important</h2>
  <p>“Meaningful human involvement” is a legal test. If a member of staff genuinely reads what a tool suggests and is free to change it, then it’s the member of staff who’s deciding, and that’s fine. If the output is waved through unread, it’s really the tool deciding, and the law treats it accordingly. The Equality Act and the public sector equality duty apply to AI-assisted work just as they do to everything else, so bias that would be unlawful coming from a person is no more acceptable coming from a model.</p>

  {keypoints("What good looks like", [
    "A competent person reviews AI output before it’s used or shared.",
    "No decision affecting a pupil, family or member of staff rests on AI alone.",
    "The bias and the accessibility of outputs are considered as a matter of course.",
    "The person who used the tool stays accountable for the result.",
  ])}

  {guidance_box([G_EQ, G_DP + " The automated decision-making rules (UK GDPR Articles 22A–22D) apply where a tool decides on its own.", G_JCQ])}
  """,
  None, None, ("data-protection.html", "Data protection"), ("safeguarding.html", "Safeguarding & Prevent")))

PAGES.append(("safeguarding.html", "Safeguarding & Prevent", "Section 9 of the template",
  "Safeguarding, online safety &amp; Prevent",
  "AI changes the shape of some safeguarding risks, deepfakes chief among them, but not the duties, and not the route a concern travels.",
  f"""
  <p class="lead">Your safeguarding duties apply to AI-assisted work exactly as they do to everything else. The policy makes the AI-specific risks explicit, and points every concern down the route staff already know, to your designated safeguarding lead.</p>

  <h2>What it is</h2>
  <p>The section that connects AI to your existing safeguarding framework: KCSIE’s four areas of online risk, the Prevent duty, and the Online Safety Act. It names the AI-specific behaviours that are prohibited and treats them as conduct matters, and, where relevant, as safeguarding matters.</p>
  <p><strong>Fabricated media and deepfakes.</strong> Creating or sharing fabricated media intended to mislead, harass, distress or harm anyone in the community is prohibited. Where such material is sexual it may be criminal, and <strong>AI-generated sexual imagery of a child is a criminal matter in every circumstance</strong>. It’s reported to the designated safeguarding lead, handled under the child protection policy, and referred to the police where required, in line with the Online Safety Act 2023 and the Ofcom Protection of Children code. Multi-agency action follows Working Together to Safeguard Children 2026.</p>
  <p><strong>Nudification tools.</strong> Making, adapting, supplying or offering nudification tools — tools designed to remove clothing from images of real people — is a criminal offence under the {link("Crime and Policing Act 2026", "https://www.legislation.gov.uk/ukpga/2026/20/contents")}. Any encounter with such a tool involving a member of the community is a safeguarding matter, reported by the usual route.</p>
  <p><strong>Voice cloning and fraud.</strong> Staff must not use AI to clone or simulate the voice or likeness of any pupil, parent or colleague. And because cloned voices and fabricated messages are increasingly used in fraud, any unusual or urgent request — particularly one involving payments, credentials or personal data — is verified through a known channel before anyone acts on it, in line with the DfE cyber security standards.</p>
  <p><strong>Published images of pupils.</strong> Automated tools can harvest photographs of children from public webpages and social media, including your own, for use in fabricated or abusive material. The policy expects you to keep your publication of identifiable pupil images, and the consent behind it, under review with that risk in mind.</p>

  <h2>Why it’s important</h2>
  <p>The tools to fabricate convincing images, audio and video are now widely available and simple to use. The schools that struggle most when this lands are the ones that never named the risk in their policy. Making the reporting route explicit, and the same one staff already use, means an AI-enabled incident is dealt with as quickly, and as seriously, as any other.</p>

  {nonneg("Your Prevent, safeguarding and online-safety duties are non-negotiable, and apply to AI exactly as they apply to everything else.")}

  {guidance_box([G_KCSIE, G_OSA, G_PREVENT])}
  """,
  None, None, ("accuracy-oversight.html", "Accuracy & oversight"), ("impact-assessment.html", "Impact assessment")))

PAGES.append(("impact-assessment.html", "Impact assessment", "Section 10 of the template",
  "Impact assessment &amp; product safety checks",
  "When you need a DPIA, what a product-safety check covers, and a free tool to get the assessment started.",
  f"""
  <p class="lead">A DPIA, or Data Protection Impact Assessment, is simply the structured assessment the law requires whenever a tool is likely to create a high risk to people. Done early, before decisions are made, it’s exactly what the DfE guidance expects.</p>

  <h2>What it is</h2>
  <p>The trigger and the process: a DPIA before you deploy AI that processes personal data; the product-safety checks that align to the DfE generative AI product safety standards; and the point in procurement where these happen, which is during tool approval, not after go-live. It sets out who coordinates the assessment (your DPO or data protection lead) and who signs it off.</p>

  <h2>Why it’s important</h2>
  <p>A DPIA completed after a tool is already embedded changes very little; the decisions have been made. Completed early, it brings the controller and processor question, international transfers, retention, sub-processors, and any training on your data into view before you’re committed. A tool that lacks a particular compliance feature isn’t ruled out automatically: the question is whether you can put sensible operational safeguards around it, and record them.</p>

  <div class="commentary" style="border-left-color:#0ea3ab;">
    <h3>Get the screening tool</h3>
    <p>The <a href="dpia-tool.html">AI &amp; Digital Tool DPIA Screening Tool</a> is a plain-English questionnaire that runs in your browser, for any AI or digital product you’re thinking of buying. It works through purpose, data, roles, transfers, retention, automated decisions and what the supplier does with the data, then tells you whether your answers are detailed enough to send to your DPO for sign-off. Unlock a copy to keep and reuse.</p>
  </div>

  {nonneg("A DPIA before you deploy AI that processes personal data is a non-negotiable. The screening tool supports that assessment; it doesn’t replace your DPO’s sign-off.")}

  {guidance_box([G_DP, G_DFE_SAFETY, G_CC, link("DfE guidance on procuring edtech and data protection in schools", U['dp_schools']) + "."])}
  """,
  None, None, ("safeguarding.html", "Safeguarding & Prevent"), ("training.html", "Training")))

PAGES.append(("training.html", "Training", "Section 11 of the template",
  "Training &amp; awareness",
  "A policy is only as good as the understanding behind it. This section sets out the training your people complete.",
  f"""
  <p class="lead">Colleagues follow rules they understand and, in my experience, work around the ones they don’t. Training moves the policy off the page and into everyday practice.</p>

  <h2>What it is</h2>
  <p>The training expectation for everyone in scope: the AI literacy staff need, how the rule on data input and the approval process are explained, and how understanding is refreshed as tools and guidance change. Where pupil use is permitted, it also calls for age-appropriate teaching about AI within the curriculum.</p>

  <h2>Why it’s important</h2>
  <p>Most AI mishaps in schools aren’t deliberate. They come from a well-meaning member of staff who didn’t know where the line was. Short, concrete training on the few things that matter most — no personal data in, approved tools only, and a person always checks and owns the output — repeated regularly, does more to prevent harm than any block list. It also gives you evidence of the “meaningful human involvement” the law expects.</p>

  {keypoints("What you decide here", [
    "The training your staff complete, and how often it’s refreshed.",
    "How you tell people when the approved list changes, or a new AI feature appears.",
    "For pupil use: age-appropriate teaching about AI, covering literacy, misinformation, deepfakes and responsible use.",
  ])}

  {guidance_box([G_KCSIE, G_DFE_SAFETY, G_STANDARDS])}
  """,
  None, None, ("impact-assessment.html", "Impact assessment"), ("filtering-monitoring.html", "Filtering & monitoring")))

PAGES.append(("filtering-monitoring.html", "Filtering & monitoring", "Section 12 of the template",
  "Filtering, monitoring &amp; assurance",
  "The controls that make tool approval real, and the senior named owner accountable for them.",
  f"""
  <p class="lead">The policy sets the rules; filtering and monitoring enforce them. This section names who owns those arrangements, and how assurance reaches your leadership.</p>

  <h2>What it is</h2>
  <p>Your filtering and monitoring arrangements as they apply to AI: blocking unapproved services, monitoring in line with your existing duties, and the senior named owner accountable for all of it. The annual review also considers access routes that bypass network controls altogether — personal devices with their own connectivity, including smart glasses and other wearables. It ties into the DfE filtering and monitoring standard and your wider cyber-security position, and it feeds the assurance reporting that trustees or governors receive.</p>

  <h2>Why it’s important</h2>
  <p>If unapproved services aren’t actually blocked, the approved list becomes advisory and unofficial use gradually becomes the norm. Blocking and monitoring, in line with your existing duties, prevent that. The DfE standards expect a senior named owner, rather than a shared inbox, so that filtering and monitoring is somebody’s clear responsibility, reviewed and reported, rather than an assumption.</p>

  {keypoints("What you decide here", [
    "Your named filtering and monitoring lead.",
    "How unapproved AI services are blocked, and how those blocks are reviewed.",
    "How assurance on all of this reaches your board.",
  ])}

  {guidance_box([G_STANDARDS, G_KCSIE, G_OSA])}
  """,
  None, None, ("training.html", "Training"), ("breaches.html", "Breaches")))

PAGES.append(("breaches.html", "Breaches", "Section 13 of the template",
  "Breaches &amp; serious incidents",
  "What happens when something goes wrong: the disciplinary and escalation routes, set out before you need them.",
  f"""
  <p class="lead">Your policy needs to be clear about what happens when it’s broken. Set the routes out in advance and you can respond calmly and consistently when you’re under pressure.</p>

  <h2>What it is</h2>
  <p>The consequences and the escalation routes: how a breach of the policy is handled through your disciplinary framework; how a personal-data breach is reported and, where required, escalated to the ICO; and how a serious incident, such as a safeguarding matter or a significant data loss, is escalated internally and to the relevant authorities.</p>

  <h2>Why it’s important</h2>
  <p>Personal-data breaches carry statutory reporting deadlines, and safeguarding incidents carry duties of their own. Deciding the routes now — who’s told, in what order, and within what time — means a stressful event is handled as a process you already have, rather than one you invent on the day. It also makes clear to staff that the rules are real, which is a deterrent in itself.</p>

  {keypoints("What you decide here", [
    "Your disciplinary route for the misuse of AI.",
    "Your personal-data breach reporting route, including escalation to the ICO where required.",
    "Your serious-incident escalation route, aligned to your safeguarding and cyber procedures.",
  ])}

  {guidance_box([G_DP + " Personal-data breach reporting duties to the ICO.", G_KCSIE, G_PREVENT])}
  """,
  None, None, ("filtering-monitoring.html", "Filtering & monitoring"), ("pupil-use.html", "Pupil use")))

PAGES.append(("pupil-use.html", "Pupil use", "Optional module",
  "Pupil use of AI",
  "Off by default. Switched on only when two conditions are genuinely met, because enabling it carelessly is the most common way a sound policy becomes indefensible.",
  f"""
  <p class="lead">Pupils aren’t covered by the staff policy. Bringing them into scope is a deliberate, carefully guarded decision. It shouldn’t happen by default, and it shouldn’t be allowed to creep in.</p>

  <h2>What it is</h2>
  <p>An optional module that extends the policy to pupil use of AI, but only once <strong>both</strong> conditions are in place: first, a DPIA completed for the specific tools and processing; and second, age-appropriate teaching about AI within your curriculum and online safety provision, covering AI literacy, misinformation, deepfakes and responsible use, in line with the whole-school approach to online safety in KCSIE 2026. If pupil use isn’t permitted, you should delete the module, and pupils stay out of scope.</p>

  <h2>Why it’s important</h2>
  <p>Two things are easy to confuse, and mustn’t be. A tool’s terms may require parent or guardian agreement for younger users; a named person obtains and records that. Separately, your UK GDPR lawful basis for processing pupils’ data comes from the DPIA, and will rarely be consent. Where a pupil-facing tool processes children’s data, the ICO Children’s Code applies: the child’s best interests come first, settings default to high privacy, and profiling is off by default. Using a tool below its stated minimum age, or without the agreement it requires, is likely to breach both the tool’s terms and data protection law.</p>
  <p>Pupils are taught what AI can and can’t do: how to recognise deepfakes, misinformation and impersonation, and how to avoid over-reliance, including on tools that simulate conversation or companionship. Web-enabled or recording-capable devices, including smart glasses and earpieces, must not be taken into examinations or controlled assessments, in line with JCQ regulations. Declining pupil use, where meeting these conditions isn’t practical, is a perfectly reasonable and defensible choice.</p>

  {nonneg("Don’t bring pupils into scope until a DPIA is complete and age-appropriate teaching about AI is embedded in your curriculum. Enabling pupil use without them is the most common way a sound policy becomes indefensible.")}

  {guidance_box([G_CC, G_KCSIE, G_DP, G_OSA, G_DFE_SAFETY])}
  """,
  None, None, ("breaches.html", "Breaches"), ("guidance-map.html", "The guidance map")))

# ---- Guidance map (reference) ----
gmap_rows = [
    ("Keeping Children Safe in Education 2026", U['kcsie'], "The statutory safeguarding baseline from 1 September 2026; addresses AI within its four areas of online risk.", "Safeguarding, pupil use, filtering &amp; monitoring, breaches"),
    ("UK GDPR &amp; Data Protection Act 2018 — as amended by the Data (Use and Access) Act 2025", U['ukgdpr'], "The core data protection law: lawful basis, roles, transfers, retention, automated decision-making, breach reporting.", "Data protection, impact assessment, acceptable use"),
    ("ICO guidance on AI &amp; the AI and data protection risk toolkit", U['ico_ai'], "How the regulator expects AI risk to data to be assessed and managed.", "Data protection, impact assessment"),
    ("ICO Children’s Code", U['childrens'], "Applies wherever children’s data is processed: best interests first, high-privacy defaults, profiling off by default.", "Pupil use, data protection"),
    ("Equality Act 2010 &amp; the public sector equality duty", U['equality'], "Applies to AI-assisted work as to everything else; bias and discrimination duties.", "Accuracy &amp; oversight, acceptable use"),
    ("DfE position on generative AI &amp; the DfE generative AI product safety standards (January 2026)", U['dfe_safety'], "The Department’s expectations for safe AI products in education, including on training on personal data.", "Approved tools, impact assessment, product safety"),
    ("JCQ guidance on AI use in assessments", U['jcq'], "Where qualifications are involved: malpractice, disclosure, and not relying on AI as the sole marker.", "Acceptable use, accuracy &amp; oversight"),
    ("DfE filtering &amp; monitoring, cyber security, and digital leadership &amp; governance standards", U['dfe_stds'], "The technical and governance standards that make tool approval enforceable and assured.", "Filtering &amp; monitoring, roles &amp; oversight"),
    ("Online Safety Act 2023 &amp; the Ofcom Protection of Children code", U['osa'], "Illegal and harmful content duties, including AI-generated sexual imagery of children.", "Safeguarding &amp; Prevent"),
    ("Prevent duty guidance (2023) &amp; Working Together to Safeguard Children 2026", U['prevent'], "The counter-radicalisation duty and multi-agency safeguarding action.", "Safeguarding &amp; Prevent, breaches"),
    ("Academy Trust Handbook / scheme for financing schools / Schools Financial Value Standard", U['ath'], "The financial governance framework that applies to procurement and oversight.", "Roles &amp; oversight, approved tools"),
]
rows_html = "\n".join(
    f"<tr><th scope='row'>{link(n, u)}</th><td>{w}</td><td>{s}</td></tr>" for n, u, w, s in gmap_rows)
PAGES.append(("guidance-map.html", "The guidance map", "Reference",
  "The guidance map",
  "Every framework the policy sits within, what each one requires, and the pages on this site that speak to it.",
  f"""
  <p class="lead">The <em>Use of AI Policy</em> doesn’t stand on its own. It sits within a body of law, statutory guidance and sector standards. This page maps the whole of it in one place.</p>
  <div class="data-table-wrap">
  <table class="data">
    <caption>Law, statutory guidance and standards referenced by the policy</caption>
    <thead><tr><th scope="col">Framework</th><th scope="col">What it requires</th><th scope="col">Where it lands on this site</th></tr></thead>
    <tbody>
    {rows_html}
    </tbody>
  </table>
  </div>
  <p class="chart-note">Frameworks and their commencement dates change. Confirm the current version of each one before you rely on it, and take your own professional or legal advice where there’s any doubt. This map is a signpost, not a statement of the law.</p>
  """,
  None, None, ("pupil-use.html", "Pupil use"), ("references.html", "References")))

# ---- References (all 17 sources cited by the template, current versions) ----
REFS = [
 (link("Keeping Children Safe in Education 2026", U['kcsie']),
  "Statutory safeguarding guidance for schools and colleges in England — the baseline from 1 September 2026, addressing AI within its four areas of online risk."),
 (link("The UK GDPR", U['ukgdpr']) + ", as amended by the " + link("Data (Use and Access) Act 2025", U['duaa']),
  "The core data-protection regime governing the processing of personal data."),
 (link("The Data Protection Act 2018", U['dpa2018']) + ", as amended by the " + link("Data (Use and Access) Act 2025", U['duaa']),
  "The UK’s implementing data-protection statute, read alongside the UK GDPR."),
 (link("ICO guidance on AI", U['ico_ai']),
  "The Information Commissioner’s guidance on artificial intelligence and data protection."),
 (link("The ICO AI and data protection risk toolkit", U['ico_toolkit']),
  "A practical toolkit for identifying and managing data-protection risk across an AI project’s lifecycle."),
 (link("The ICO Children’s Code", U['childrens']),
  "The age-appropriate design code for online services likely to be accessed by children."),
 (link("The DfE position on generative AI in education", U['dfe_genai']),
  "The Department for Education’s policy position on the use of generative AI in schools and colleges."),
 (link("The DfE generative AI product safety standards", U['dfe_safety']) + " (January 2026)",
  "The Department’s expectations for the safety of generative AI products used in education settings."),
 (link("JCQ AI Use in Assessments", U['jcq']) + " (Revision 2)",
  "Joint Council for Qualifications guidance on AI use where qualifications are involved, including malpractice and marking."),
 (link("The DfE filtering and monitoring standard", U['dfe_filter']),
  "The core standard for filtering and monitoring arrangements in schools and colleges."),
 (link("The DfE cyber security standard", U['dfe_cyber']),
  "The core standard for cyber security in schools and colleges."),
 (link("The DfE digital leadership and governance standard", U['dfe_gov']),
  "The standard for digital leadership and governance, including a senior digital lead and governor oversight."),
 (link("The Online Safety Act 2023", U['osa']),
  "The statute establishing online-safety duties for user-to-user and search services."),
 (link("The Ofcom Protection of Children code of practice", U['ofcom']),
  "Ofcom’s codes setting out measures to protect children online under the Online Safety Act."),
 (link("The Prevent duty guidance (2023)", U['prevent']),
  "Statutory guidance on the Prevent duty for specified authorities in England and Wales."),
 (link("Working Together to Safeguard Children 2026", U['wttsc']),
  "The statutory framework for multi-agency working to safeguard and promote the welfare of children."),
 (link("The Academy Trust Handbook 2026", U['ath']),
  "The financial and governance framework for academy trusts, relevant to procurement and oversight."),
]
_ref_items = "\n".join(
    f'<li><span class="ref-title">{t}</span><span class="ref-desc">{d}</span></li>' for t, d in REFS)

# ---- The wider legal framework (from the template's appendix) ----
LEGAL = [
 (link("Crime and Policing Act 2026", "https://www.legislation.gov.uk/ukpga/2026/20/contents"),
  "Creates the offence of making, adapting, supplying or offering nudification tools. Royal Assent 29 April 2026; commencement is staged."),
 (link("Sexual Offences Act 2003", "https://www.legislation.gov.uk/ukpga/2003/42/contents"),
  "The intimate image offences, including — from 6 February 2026 — creating, or requesting the creation of, purported intimate images."),
 (link("Protection of Children Act 1978", "https://www.legislation.gov.uk/ukpga/1978/37/contents") + " and the " + link("Coroners and Justice Act 2009", "https://www.legislation.gov.uk/ukpga/2009/25/contents"),
  "Together make indecent and prohibited images of children criminal in all forms, including pseudo-photographs and AI-generated imagery."),
 (link("Counter-Terrorism and Security Act 2015", "https://www.legislation.gov.uk/ukpga/2015/6/contents"),
  "Places the Prevent duty on schools and colleges; the Prevent duty guidance is issued under it."),
 (link("Protection of Freedoms Act 2012", "https://www.legislation.gov.uk/ukpga/2012/9/contents"),
  "Requires written parental consent before processing a child’s biometric information, with an alternative for those who refuse."),
 (link("Freedom of Information Act 2000", "https://www.legislation.gov.uk/ukpga/2000/36/contents"),
  "AI prompts, outputs and interaction logs held by the organisation are potentially disclosable."),
 (link("Copyright, Designs and Patents Act 1988", "https://www.legislation.gov.uk/ukpga/1988/48/contents"),
  "The framework for the third-party rights engaged when material is entered into, or produced by, an AI tool."),
 (link("UK Safer Internet Centre: appropriate filtering and monitoring definitions", "https://saferinternet.org.uk/guide-and-resource/teachers-and-school-staff/appropriate-filtering-and-monitoring"),
  "The definitions the annual filtering and monitoring review is checked against."),
]
_legal_items = "\n".join(
    f'<li><span class="ref-title">{t}</span><span class="ref-desc">{d}</span></li>' for t, d in LEGAL)
references_body = banner("Reference list", "References",
  "Every source cited by the Use of AI Policy template, at its current version, in one place, each linked to the official document.") + f"""
  <p class="lead">The <em>Use of AI Policy</em> template sits within a body of statute, statutory guidance and sector standards. These are the sources it draws on, listed in the order they appear in the template’s opening section. Each link opens the official document in a new tab.</p>
  <ol class="reflist">
  {_ref_items}
  </ol>

  <h2>The wider legal framework</h2>
  <p>The template also carries an appendix setting out the full range of legislation behind the policy, including the criminal law behind its safeguarding section. Those instruments are:</p>
  <ol class="reflist">
  {_legal_items}
  </ol>
  <div class="commentary">
    <h3>A note on versions</h3>
    <p>Law and guidance change, and commencement dates move. The links above point to the official landing page for each source, which the publisher keeps at the current version; the edition named is the one the template was written against, for adoption from September 2026. Always confirm the current version before you rely on it, and take your own professional or legal advice where there’s any doubt.</p>
  </div>
  <p>Would you rather see what each source governs, and where it lands on this site? The <a href="guidance-map.html">guidance map</a> sets that out.</p>
""" + pagenav(("guidance-map.html", "The guidance map"), ("dpia-tool.html", "DPIA screening tool"))
write("references.html", "References — " + BRAND_TITLE,
      "Every source cited by the Use of AI Policy template, at its current version, linked to the official document: KCSIE, UK GDPR, ICO, DfE standards, Online Safety Act and more.",
      references_body, ORG_LD)

# ---- Build the standard topic pages ----
for slug, navt, kicker, h1, sub, body, _gi, _extra, prev, nxt in PAGES:
    inner = banner(kicker, h1, sub) + body + pagenav(prev, nxt)
    write(slug, f"{h1.replace('&amp;','&')} — {BRAND_TITLE}",
          sub.replace('“','').replace('”','')[:180], inner, ORG_LD)

print("All topic pages written.")
