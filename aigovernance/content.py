#!/usr/bin/env python3
# Content + page assembly for aigovernance.ictevangelist.com
# Run: python3 content.py   (imports the engine in build.py, writes all pages)
from build import (write, banner, guidance_box, keypoints, nonneg, pagenav,
                   FOOTER, head, nav_html, SITE, BRAND_TITLE, AUTHOR)
import html as _h

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
    <h1>Govern AI in your school or trust with confidence.</h1>
    <p class="lede">A plain-language companion to the <strong>Use of Artificial Intelligence (AI) Policy</strong> template — breaking down what leaders need to decide, why each decision matters, and the law and guidance it answers to. Written for adoption from <strong>September 2026</strong>.</p>
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
  <p class="lead section-intro">AI is already in your classrooms and offices — inside the everyday software staff use, and in the browser tabs they open. Governance is not about slowing that down. It is about making adoption <strong>safe, lawful and defensible</strong>, so the benefits are realised without compromising the safety of children and adults, data privacy, fairness, or professional integrity.</p>

  <h2 class="mt-0" style="margin-top:2rem;">Start where it makes sense for you</h2>
  <div class="card-grid" style="margin-top:1.2rem;">
    <a class="card card--link" href="landscape.html"><h3>The landscape</h3><p>Why a policy now, what counts as “AI”, and the framework of law and guidance that binds you.<span class="more">Read &rsaquo;</span></p></a>
    <a class="card card--link" href="approval-gate.html"><h3>The approval gate</h3><p>The compliance backbone: how a tool becomes approved, and why “not approved” is the default.<span class="more">Read &rsaquo;</span></p></a>
    <a class="card card--link" href="data-protection.html"><h3>Data protection</h3><p>The default rule on personal data, lawful basis, controllers and processors, and retention.<span class="more">Read &rsaquo;</span></p></a>
    <a class="card card--link" href="impact-assessment.html"><h3>Impact assessment</h3><p>When a DPIA is required, product-safety checks, and the free screening tool to get you started.<span class="more">Read &rsaquo;</span></p></a>
    <a class="card card--link" href="safeguarding.html"><h3>Safeguarding &amp; Prevent</h3><p>Deepfakes, online-safety duties, and how AI concerns reach your designated safeguarding lead.<span class="more">Read &rsaquo;</span></p></a>
    <a class="card card--link" href="pupil-use.html"><h3>Pupil use</h3><p>The optional module — and the two preconditions to meet before pupils use AI at all.<span class="more">Read &rsaquo;</span></p></a>
  </div>

  <h2>The non-negotiables</h2>
  <p>Most of the template is yours to shape. Five things are not — weaken them and the policy stops being defensible:</p>
  <div class="card-grid">
    <div class="card"><h3>No personal data in</h3><p>Personal or special-category data is not entered into AI tools by default — lifted only for a tool expressly approved for that processing through the gate.</p></div>
    <div class="card"><h3>A human always decides</h3><p>AI never takes a decision about a person. A named person makes and owns any decision that affects someone.</p></div>
    <div class="card"><h3>DPIA before deployment</h3><p>A data protection impact assessment is completed before deploying AI that processes personal data — early, before decisions are locked in.</p></div>
    <div class="card"><h3>The approval gate</h3><p>Only approved tools, through organisation accounts. Anything else — including public chatbots on a personal login — is not approved.</p></div>
    <div class="card"><h3>Safeguarding duties hold</h3><p>Prevent, safeguarding and online-safety duties apply to AI-assisted activity exactly as they do to everything else.</p></div>
  </div>

  <h2>Two tools to take away</h2>
  <div class="card-grid">
    <a class="card card--link" href="policy-template.html"><h3>The policy template &darr;</h3><p>A completable <em>Use of AI Policy</em> for schools, trusts and colleges — a staff-use spine with optional modules for pupil use and governed exceptions.<span class="more">Download &rsaquo;</span></p></a>
    <a class="card card--link" href="dpia-tool.html"><h3>The DPIA screening tool &darr;</h3><p>A plain-language, browser-based screening tool for any AI or digital product you are thinking of procuring. Complete it, save it, send it to your DPO.<span class="more">Unlock &rsaquo;</span></p></a>
  </div>

  <h2>Key questions answered</h2>
  <div class="faq">
    <details><summary>Does every school need its own AI policy?</summary><div class="faq__a"><p>You need a position that is yours and that your stakeholders have agreed. A multi-academy trust should adopt one policy centrally, with school-level detail held in local appendices rather than separate versions. The template is written to be completed for your context, not used as it stands.</p></div></details>
    <details><summary>Are pupils covered by the policy?</summary><div class="faq__a"><p>By default, no. Pupils come into scope only when the optional pupil-use module is switched on — and only once a DPIA and an age-appropriate AI education plan are both in place.</p></div></details>
    <details><summary>Can staff just use ChatGPT for work?</summary><div class="faq__a"><p>Only if it has been approved through the gate and is used through an organisation-provided account. Personal accounts must not be used for work, and public consumer chatbots are not approved by default.</p></div></details>
    <details><summary>When do we need a DPIA?</summary><div class="faq__a"><p>Before deploying AI that processes personal data, and wherever a tool is likely to create a high risk to people. Completing it early — before decisions are made — is what the DfE guidance expects. The <a href="dpia-tool.html">screening tool</a> helps you judge readiness.</p></div></details>
  </div>
</div></section>"""

home_ld = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": "Does every school need its own AI policy?",
         "acceptedAnswer": {"@type": "Answer", "text": "You need a position that is yours and that your stakeholders have agreed. A multi-academy trust should adopt one policy centrally, with school-level detail in local appendices. The template is completed for your context, not used as-is."}},
        {"@type": "Question", "name": "Are pupils covered by the policy?",
         "acceptedAnswer": {"@type": "Answer", "text": "By default no. Pupils come into scope only when the optional pupil-use module is switched on, and only once a DPIA and an age-appropriate AI education plan are both in place."}},
        {"@type": "Question", "name": "Can staff just use ChatGPT for work?",
         "acceptedAnswer": {"@type": "Answer", "text": "Only if approved through the gate and used through an organisation-provided account. Personal accounts must not be used for work and public consumer chatbots are not approved by default."}},
        {"@type": "Question", "name": "When do we need a DPIA?",
         "acceptedAnswer": {"@type": "Answer", "text": "Before deploying AI that processes personal data, and wherever a tool is likely to create a high risk to people. Completing it early is what DfE guidance expects."}},
    ],
}

home_doc = head(BRAND_TITLE + " — a companion to the Use of AI Policy template",
                "Plain-language guidance on AI governance for schools, trusts and colleges: the approval gate, data protection, safeguarding, DPIAs and a free policy template. Written for September 2026.",
                SITE + "/", home_ld).replace("{NAV_PLACEHOLDER}", nav_html("index.html")) + home_body + FOOTER
(__import__("pathlib").Path(__file__).parent / "index.html").write_text(home_doc, encoding="utf-8")
print("wrote index.html")

# ---------------------------------------------------------------- TOPIC PAGES
# Each: (slug, nav_title, kicker, h1, sub, body_inner_html, guidance_items, prev, next)
G_DP = "UK GDPR &amp; Data Protection Act 2018 (as amended by the Data (Use and Access) Act 2025); ICO guidance on AI and the ICO AI &amp; data protection risk toolkit."
G_CC = "ICO Children’s Code, wherever children’s data is involved."
G_KCSIE = "Keeping Children Safe in Education 2026 — the statutory safeguarding baseline from 1 September 2026."
G_DFE_SAFETY = "DfE position on generative AI in education and the DfE generative AI product safety standards (January 2026)."
G_EQ = "Equality Act 2010 and, for public bodies, the public sector equality duty."
G_JCQ = "JCQ guidance on AI use in assessments, where qualifications are involved."
G_OSA = "Online Safety Act 2023 and the Ofcom Protection of Children code of practice."
G_PREVENT = "Prevent duty guidance (2023) and Working Together to Safeguard Children 2026."
G_STANDARDS = "DfE filtering &amp; monitoring, cyber security, and digital &amp; governance standards."

PAGES = []

PAGES.append(("landscape.html", "The landscape", "Sections 1–2 of the template",
  "The landscape: why govern AI, and what binds you",
  "Before any rule, the case for governing AI at all — plus what counts as “AI” here and the framework of law and guidance the policy sits within.",
  f"""
  <p class="lead">A good AI policy opens with a <em>why</em> that is yours: what AI adoption is in service of in your setting — teaching, workload, inclusion — before any rule appears. Governance follows the purpose; it does not replace it.</p>

  <h2>What it is</h2>
  <p>The policy statement sets out how your organisation uses AI: by whom, for what, and within what limits, so its benefits are realised without compromising the safety of children and adults, data security and privacy, fairness, or professional and academic integrity. It forms part of your wider digital strategy and is reviewed on a set cycle and whenever the law, guidance or your use of AI materially changes.</p>
  <p><strong>What counts as AI here.</strong> Generative AI tools and any software feature that creates content, or that makes or informs decisions or predictions about people — whether standalone, built into approved software, or reached through a browser. In practice: chatbots, image and content generators, and AI features inside everyday software. Long-established automation such as spellcheck or predictive text is out of scope unless it does one of those things.</p>

  <h2>Why it matters</h2>
  <p>AI does not arrive by a single front door. It appears inside the platforms you already license and behind any browser tab. A policy scoped to “the AI tool we bought” misses most of the real exposure. Defining scope by <em>behaviour</em> — does it generate content, or make or inform decisions about people? — is what keeps the policy honest as products change under you.</p>
  <p>Multi-academy trusts should adopt one policy centrally, with school-level detail in local appendices rather than divergent versions that drift apart and become impossible to assure.</p>

  {keypoints("What you decide here", [
    "Your <em>why</em>: one or two sentences on what AI adoption serves in your setting.",
    "Your organisation name, review cycle, and the audiences in scope (typically all staff, governors, trustees, volunteers and contractors).",
    "Any platform AI features governed by a separate assessment, noted so the boundary is clear.",
    "Whether pupils are in scope — off by default until the optional module’s preconditions are met.",
  ])}

  {guidance_box([G_KCSIE, G_DP, G_CC, G_EQ, G_DFE_SAFETY, G_JCQ, G_STANDARDS, G_OSA, G_PREVENT,
                 "The financial governance framework that applies to you: the Academy Trust Handbook; the scheme for financing schools and the Schools Financial Value Standard; or a college’s corporation framework.",
                 "See them all, with what each requires, on the <a href='guidance-map.html'>guidance map</a>."])}
  """,
  None, None, ("index.html", "Home"), ("roles.html", "Roles & oversight")))

PAGES.append(("roles.html", "Roles & oversight", "Section 3 of the template",
  "Roles, responsibilities & oversight",
  "Governance only works when every responsibility has a name against it. This is the menu — cut it to the roles you actually have.",
  f"""
  <p class="lead">A policy no one owns is a policy no one follows. Section 3 assigns each responsibility to a named person or group, so nothing important is left in the gaps between jobs.</p>

  <h2>What it is</h2>
  <p>A menu of roles and what each one owns. Delete roles you do not have, merge where one person carries several, and re-home any orphaned responsibility to whoever picks it up. Typical owners include:</p>
  <ul>
    <li><strong>Trustees / governing board</strong> — strategic oversight and assurance; ensures AI is on the risk register; receives regular reporting on adoption, incidents, breaches and changes to the approved list.</li>
    <li><strong>Senior leadership</strong> — approves the policy and material changes; approves tool additions where named as approver; commissions the periodic AI risk review.</li>
    <li><strong>AI / digital lead</strong> — owns the approved list and the approval gate; keeps the policy and staff guidance current; first contact for queries.</li>
    <li><strong>Data protection officer / lead</strong> — coordinates impact assessments; advises on lawful basis and processing agreements; receives reports of data entered in error.</li>
    <li><strong>Designated safeguarding lead</strong> — receives safeguarding and Prevent concerns involving AI; advises on safeguarding implications of proposed uses.</li>
    <li><strong>Filtering &amp; monitoring lead</strong> — senior named owner of filtering and monitoring arrangements.</li>
    <li><strong>IT / network lead</strong> — operates access, security, filtering and monitoring controls; blocks unapproved services; includes AI in cyber reviews.</li>
  </ul>

  <h2>Why it matters</h2>
  <p>The DfE governance standards expect clear lines of accountability, and the ICO’s edtech audits repeatedly found responsibilities that everyone assumed someone else held. Naming an owner against each line turns good intentions into something you can actually assure — and report on to your board.</p>

  {keypoints("What you decide here", [
    "A named owner for every responsibility you keep.",
    "Your reporting cycle to trustees or governors (for example, termly).",
    "Where the AI / digital lead and the DPO roles sit, and how they hand off to each other.",
  ])}

  {guidance_box([G_STANDARDS, G_DP, "Academy Trust Handbook / financial governance framework for oversight and assurance duties."])}
  """,
  None, None, ("landscape.html", "The landscape"), ("approval-gate.html", "The approval gate")))

PAGES.append(("approval-gate.html", "The approval gate", "Sections 4 &amp; 4a of the template",
  "The approval gate &amp; approved tools",
  "The compliance backbone of the whole policy. If you keep only one thing intact, keep this.",
  f"""
  <p class="lead">Staff may use AI for work only through tools the organisation has approved, and only through organisation-provided accounts. Everything else is not approved — that is the default, and it is deliberate.</p>

  <h2>What it is</h2>
  <p>A single, explicit gate that every tool passes through before it is used for work. The approved list names each tool and what it is approved <em>for</em>. Anything not on that list — including public consumer chatbots and anything reached through a personal login — is not approved and must not be used. Crucially, <strong>a new AI feature appearing inside an already-approved product is not approved by default</strong>; it goes back through the gate before use.</p>
  <p><strong>Governed exceptions (4a, optional).</strong> Only if you choose to permit named tools for single, tightly-scoped purposes — with the same scrutiny applied and the exception written down, not assumed.</p>

  <h2>Why it matters</h2>
  <p>The gate is what makes every other promise in the policy enforceable. Without it, “no personal data into AI” and “a DPIA before deployment” have nowhere to bite. With it, the questions — what data, what lawful basis, what the supplier does with it — are answered <em>before</em> a tool is in daily use, not discovered afterwards. The DfE product safety standards and the ICO’s audit findings both point the same way: assess before you adopt.</p>

  {nonneg("The tool-approval gate is a non-negotiable. So is the rule that a new AI feature inside an existing product returns through the gate — “we already use this vendor” is not approval.")}

  {keypoints("What you decide here", [
    "Which tools you approve, and the specific purpose each is approved for.",
    "Who approves additions, and how a request is made.",
    "Whether you permit any governed exceptions (4a), and how they are recorded.",
    "How the approved list is published, and how staff know what is blocked.",
  ])}

  <p>Assessing a specific product? The <a href="dpia-tool.html">DPIA screening tool</a> walks you through the questions the gate should ask.</p>

  {guidance_box([G_DFE_SAFETY, G_DP, G_STANDARDS, "DfE guidance on procuring edtech and data protection in schools."])}
  """,
  None, None, ("roles.html", "Roles & oversight"), ("acceptable-use.html", "Acceptable use")))

PAGES.append(("acceptable-use.html", "Acceptable use", "Sections 5 &amp; 6 of the template",
  "Acceptable use: what staff may and must not do",
  "The everyday rules — tailored to your examples, but with the data-input rule and the high-risk prohibitions kept intact.",
  f"""
  <p class="lead">This is the part staff actually read. Keep the examples concrete and local; keep the boundaries firm.</p>

  <h2>What staff may do</h2>
  <p>Set out the genuinely useful, low-risk uses you want to encourage — drafting and adapting resources, summarising, planning, routine administrative text — always through approved tools and organisation accounts, and always with a person reviewing the output before it is used. The point is permission with judgement, not a list of hoops.</p>

  <h2>What staff must not do</h2>
  <ul>
    <li>Use AI tools other than those approved under the gate, or try to get round filtering or monitoring to reach a blocked service.</li>
    <li>Enter personal or special-category data — information about real, identifiable people — into an AI tool, unless it is expressly approved for that processing.</li>
    <li>Let AI take a decision about a person. In sensitive areas even assistive use is prohibited unless expressly authorised, with a named person making and owning the decision.</li>
    <li>Pass off AI-generated material as their own unaided work where that would mislead, or breach JCQ rules on AI in assessments (which also bar relying on AI as the sole marker of student work).</li>
    <li>Upload third-party copyrighted or licensed material — published schemes of work, textbooks, exam papers — without the rights to do so.</li>
  </ul>

  <h2>Why it matters</h2>
  <p>The single most common way personal data leaks into an AI tool is not a data breach in the technical sense — it is a member of staff pasting a name, a report or a case note into a chatbot to “save time”. The data-input rule is the front line, which is why it is not up for local softening. The high-risk prohibitions exist because these are exactly the decisions where an automated shortcut does the most harm.</p>

  {nonneg("The default prohibition on entering personal or special-category data into AI tools, and the human-in-the-loop principle, are non-negotiable. Tailor the examples around them; do not remove the substance.")}

  {guidance_box([G_DP, G_JCQ, G_EQ, "Copyright and licensing law for third-party materials.",
                 "Your acceptable-use, data protection and academic-integrity policies, read alongside this one."])}
  """,
  None, None, ("approval-gate.html", "The approval gate"), ("data-protection.html", "Data protection")))

PAGES.append(("data-protection.html", "Data protection", "Section 7 of the template",
  "Data protection &amp; information security",
  "Whose data, on what lawful basis, in whose hands, and for how long — the questions that decide whether a tool is lawful to use.",
  f"""
  <p class="lead">Data protection is where most AI-in-education risk actually lives. Get four things straight — subjects, basis, roles, retention — and most of the rest follows.</p>

  <h2>What it is</h2>
  <p>The section that fixes how personal data is handled when AI is involved: the default that personal and special-category data stays out of AI tools; your lawful basis for any processing that is approved; the controller/processor relationship with each supplier; retention and deletion; and the route by which data entered in error is reported and dealt with.</p>

  <h2>Why it matters</h2>
  <p><strong>Controller vs processor is the sector’s most common failing.</strong> Normally your school or trust decides why and how data is used (the controller) and the supplier only acts on your instructions (the processor). But the contract label does not settle it — what the supplier actually does settles it. If a supplier uses the data for its own purposes, such as product development, analytics or improving its AI, it is acting as a controller for that use, extra rules apply (including the Children’s Code where pupils are involved), and you should ask why it needs to do this at all.</p>
  <p><strong>Lawful basis is rarely consent.</strong> For most of what a school does, the basis is public task — part of running the school and educating pupils. Do not confuse a tool’s terms requiring parent or guardian agreement with your lawful basis; they are different things.</p>
  <p><strong>Free text is a hidden data surface.</strong> A tool that only collects a name and email can still process sensitive data the moment someone types free text. The input rule, not just the sign-up form, is what protects you.</p>

  {keypoints("What good looks like", [
    "Personal data stays out of AI tools by default; exceptions are approved and documented.",
    "Each supplier’s role (controller or processor) is established from what it actually does.",
    "A valid lawful basis is recorded — usually public task, rarely consent.",
    "Retention is configurable and short where possible; the exit position (deletion or return of data) is written into the contract.",
    "International transfers are covered by an approved arrangement, and sub-processors are known and notified on change.",
  ])}

  {nonneg("A DPIA is completed before deploying AI that processes personal data. It is not paperwork after the fact — it is how the decision is made.")}

  <p>Use the <a href="dpia-tool.html">DPIA screening tool</a> to work through roles, transfers, retention and sub-processors for a specific product.</p>

  {guidance_box([G_DP, G_CC, "DfE guidance on procuring edtech and data protection in schools; the ICO’s <em>Edtech examined</em> audit findings.", G_DFE_SAFETY])}
  """,
  None, None, ("acceptable-use.html", "Acceptable use"), ("accuracy-oversight.html", "Accuracy & oversight")))

PAGES.append(("accuracy-oversight.html", "Accuracy & oversight", "Section 8 of the template",
  "Accuracy, bias, accountability &amp; human oversight",
  "AI outputs are drafts, not decisions. This section keeps a person accountable for everything that leaves the building.",
  f"""
  <p class="lead">Generative AI is confident and frequently wrong. Governance treats its output as a starting point that a professional checks, corrects and owns.</p>

  <h2>What it is</h2>
  <p>The commitments on accuracy and human oversight: outputs are reviewed by a competent person before use; AI is never the sole basis of a decision about a person; bias and fairness are actively considered, not assumed away; and accountability for any AI-assisted work stays with the human who used it. Where AI has done substantial drafting of something consequential, disclosure expectations are set out.</p>

  <h2>Why it matters</h2>
  <p>“Meaningful human involvement” is a legal test, not a slogan. If a member of staff genuinely reviews what a tool suggests and is free to change it, then it is the staff member deciding — and that is fine. If the tool’s output is waved through unchecked, it is really the tool deciding, and that is where both the law and fairness bite. The Equality Act and the public sector equality duty apply to AI-assisted activity exactly as to everything else, so bias that would be unlawful from a person is no more acceptable from a model.</p>

  {keypoints("What good looks like", [
    "A competent person reviews AI output before it is used or shared.",
    "No decision affecting a pupil, family or staff member rests on AI alone.",
    "Bias and accessibility of outputs are considered as a matter of course.",
    "The person who used the tool remains accountable for the result.",
  ])}

  {guidance_box([G_EQ, G_DP + " Automated decision-making rules (UK GDPR Articles 22A–22D) apply where a tool decides on its own.", G_JCQ])}
  """,
  None, None, ("data-protection.html", "Data protection"), ("safeguarding.html", "Safeguarding & Prevent")))

PAGES.append(("safeguarding.html", "Safeguarding & Prevent", "Section 9 of the template",
  "Safeguarding, online safety &amp; Prevent",
  "AI changes the shape of some safeguarding risks — deepfakes chief among them — but not the duties, or the route a concern travels.",
  f"""
  <p class="lead">Safeguarding duties apply to AI-assisted activity exactly as to everything else. The policy makes the AI-specific risks explicit and points every concern down the usual route to your designated safeguarding lead.</p>

  <h2>What it is</h2>
  <p>The section that connects AI to your existing safeguarding framework: KCSIE’s four areas of online risk, the Prevent duty, and the Online Safety Act. It names the AI-specific behaviours that are prohibited and treats them as conduct and, where relevant, safeguarding matters.</p>
  <p><strong>Fabricated media and deepfakes.</strong> Creating or sharing fabricated media intended to mislead, harass, distress or harm anyone in the community is prohibited. Where such material is sexual it may be criminal, and <strong>AI-generated sexual imagery of a child is a criminal matter in all circumstances</strong> — reported to the designated safeguarding lead, handled under the child protection policy, and referred to the police where required, in line with the Online Safety Act 2023 and the Ofcom Protection of Children code. Multi-agency action follows Working Together to Safeguard Children 2026.</p>

  <h2>Why it matters</h2>
  <p>The tools to fabricate convincing images, audio and video are now in every pocket. Schools that have not named this risk in policy are the ones caught flat-footed when it materialises. Making the reporting route explicit — and identical to the one staff already know — means an AI-enabled incident is handled with the same speed and seriousness as any other.</p>

  {nonneg("The Prevent, safeguarding and online-safety duties are non-negotiable and apply to AI exactly as they apply to everything else.")}

  {guidance_box([G_KCSIE, G_OSA, G_PREVENT])}
  """,
  None, None, ("accuracy-oversight.html", "Accuracy & oversight"), ("impact-assessment.html", "Impact assessment")))

PAGES.append(("impact-assessment.html", "Impact assessment", "Section 10 of the template",
  "Impact assessment &amp; product safety checks",
  "When a DPIA is required, what a product-safety check covers — and a free tool to get the assessment started.",
  f"""
  <p class="lead">A DPIA — a Data Protection Impact Assessment — is simply the structured assessment the law requires wherever a tool is likely to create a high risk to people. Done early, before decisions are made, it is what the DfE guidance expects.</p>

  <h2>What it is</h2>
  <p>The trigger and the process: a DPIA before deploying AI that processes personal data; the product-safety checks aligned to the DfE generative AI product safety standards; and the point in procurement where these happen — at the approval gate, not after go-live. It sets who coordinates the assessment (your DPO or data protection lead) and who signs it off.</p>

  <h2>Why it matters</h2>
  <p>A DPIA completed after a tool is embedded is a formality that changes nothing. Completed early, it is a genuine decision aid: it surfaces the controller/processor question, international transfers, retention, sub-processors and training-on-your-data <em>before</em> you are committed. A tool missing a particular compliance feature is not automatically ruled out — what matters is whether you can put robust operational mitigations around it, and document them.</p>

  <div class="commentary" style="border-left-color:#0ea3ab;">
    <h3>Get the screening tool</h3>
    <p>The <a href="dpia-tool.html">AI &amp; Digital Tool DPIA Screening Tool</a> is a plain-language, browser-based questionnaire you run against any AI or digital product you are thinking of procuring. It checks readiness across purpose, data, roles, transfers, retention, automated decisions and supplier AI-training — then tells you whether it is detailed enough to send to your DPO for sign-off. Unlock your own copy to keep and reuse.</p>
  </div>

  {nonneg("A DPIA before deploying AI that processes personal data is a non-negotiable. The screening tool supports that assessment — it does not replace your DPO’s sign-off.")}

  {guidance_box([G_DP + " ICO AI &amp; data protection risk toolkit.", G_DFE_SAFETY, G_CC, "DfE guidance on procuring edtech and data protection in schools."])}
  """,
  None, None, ("safeguarding.html", "Safeguarding & Prevent"), ("training.html", "Training")))

PAGES.append(("training.html", "Training", "Section 11 of the template",
  "Training &amp; awareness",
  "A policy is only as good as the understanding behind it. This section names the training people actually complete.",
  f"""
  <p class="lead">Rules that staff have not been helped to understand are rules that get worked around. Training is what turns the policy from a document into practice.</p>

  <h2>What it is</h2>
  <p>The training expectation for everyone in scope: what AI literacy staff need, how the data-input rule and the approval gate are explained, and how understanding is refreshed as tools and guidance change. Where pupil use is permitted, it also requires an age-appropriate AI education plan.</p>

  <h2>Why it matters</h2>
  <p>Most AI mishaps in schools are not malicious — they are the product of a well-meaning member of staff who did not know where the line was. Brief, concrete, repeated training on the handful of things that matter most (no personal data in; approved tools only; a human checks and owns the output) prevents far more harm than any block list. It also evidences the “meaningful human involvement” the law expects.</p>

  {keypoints("What you decide here", [
    "The training staff complete, and how often it is refreshed.",
    "How new AI features and tools are communicated when the approved list changes.",
    "For pupil use: the age-appropriate AI education plan covering literacy, misinformation, deepfakes and responsible use.",
  ])}

  {guidance_box([G_KCSIE, G_DFE_SAFETY, G_STANDARDS])}
  """,
  None, None, ("impact-assessment.html", "Impact assessment"), ("filtering-monitoring.html", "Filtering & monitoring")))

PAGES.append(("filtering-monitoring.html", "Filtering & monitoring", "Section 12 of the template",
  "Filtering, monitoring &amp; assurance",
  "The technical controls that make the approval gate real — and the named senior owner accountable for them.",
  f"""
  <p class="lead">Policy sets the rules; filtering and monitoring enforce them. This section names who owns those arrangements and how assurance flows back to leadership.</p>

  <h2>What it is</h2>
  <p>Your filtering and monitoring arrangements as they apply to AI: blocking unapproved services, monitoring in line with your existing duties, and the senior named owner accountable for it all. It ties into the DfE filtering and monitoring standards and your cyber-security posture, and feeds the assurance reporting that trustees or governors receive.</p>

  <h2>Why it matters</h2>
  <p>An approval gate with nothing behind it is a suggestion. Blocking unapproved AI services and monitoring appropriately is what stops shadow use quietly becoming the norm. The DfE standards expect a senior named owner — not a shared inbox — precisely so that filtering and monitoring is somebody’s explicit job, reviewed and reported, rather than an assumption.</p>

  {keypoints("What you decide here", [
    "Your named filtering and monitoring lead.",
    "How unapproved AI services are blocked, and how blocks are reviewed.",
    "How assurance on all of this reaches your board.",
  ])}

  {guidance_box([G_STANDARDS + " (filtering &amp; monitoring; cyber security).", G_KCSIE, G_OSA])}
  """,
  None, None, ("training.html", "Training"), ("breaches.html", "Breaches")))

PAGES.append(("breaches.html", "Breaches", "Section 13 of the template",
  "Breaches &amp; serious incidents",
  "What happens when something goes wrong — the disciplinary and escalation routes, set out before you need them.",
  f"""
  <p class="lead">Every policy needs a clear answer to “what happens if this is broken?”. Setting the routes out in advance is what lets you respond calmly and consistently under pressure.</p>

  <h2>What it is</h2>
  <p>The consequences and escalation paths: how a breach of the policy is handled through your disciplinary framework; how a personal-data breach is reported and, where required, escalated to the ICO; and how a serious incident — a safeguarding matter, a significant data loss — is escalated internally and to external authorities.</p>

  <h2>Why it matters</h2>
  <p>Personal-data breaches carry statutory reporting timescales, and safeguarding incidents carry their own duties. Deciding the routes now — who is told, in what order, within what time — turns a stressful event into a followed process. It also signals to staff that the rules are real, which is itself a deterrent.</p>

  {keypoints("What you decide here", [
    "Your disciplinary route for misuse of AI.",
    "Your personal-data breach reporting route, including ICO escalation where required.",
    "Your serious-incident escalation route, aligned to safeguarding and cyber procedures.",
  ])}

  {guidance_box([G_DP + " Personal-data breach reporting duties to the ICO.", G_KCSIE, G_PREVENT])}
  """,
  None, None, ("filtering-monitoring.html", "Filtering & monitoring"), ("pupil-use.html", "Pupil use")))

PAGES.append(("pupil-use.html", "Pupil use", "Optional module",
  "Pupil use of AI",
  "Off by default. Switched on only when two preconditions are genuinely met — because enabling it carelessly is the commonest way a sound policy becomes indefensible.",
  f"""
  <p class="lead">Pupils are not in scope of the staff policy. Bringing them in is a deliberate, guarded decision — never a default, and never a drift.</p>

  <h2>What it is</h2>
  <p>An optional module that extends the policy to pupil use of AI — but only once <strong>both</strong> preconditions are in place: (1) a DPIA completed for the specific tools and processing; and (2) an age-appropriate AI education plan covering AI literacy, misinformation, deepfakes and responsible use. If pupil use is not permitted, the module is deleted and pupils remain out of scope.</p>

  <h2>Why it matters</h2>
  <p>Two things are easy to conflate and must not be. A tool’s terms may require parent or guardian agreement for younger users — someone named obtains and records that. Separately, your UK GDPR lawful basis for processing pupils’ data comes from the DPIA and will rarely be consent. Where a pupil-facing tool processes children’s data, the ICO Children’s Code applies: the child’s best interests come first, settings default to high privacy, and profiling is off by default. Using a tool below its stated minimum age, or without the required agreement, is likely to breach both the tool’s terms and data protection law.</p>
  <p>Pupils are taught AI’s capabilities and limits — to recognise deepfakes, misinformation and impersonation, and to avoid over-reliance, including on tools that simulate conversation or companionship. Declining pupil use where the preconditions are impractical is a perfectly defensible choice.</p>

  {nonneg("Do not bring pupils into scope until a DPIA and an age-appropriate AI education plan are both in place. Enabling pupil use without the preconditions is the commonest way a sound policy becomes indefensible.")}

  {guidance_box([G_CC, G_KCSIE, G_DP, G_OSA, G_DFE_SAFETY])}
  """,
  None, None, ("breaches.html", "Breaches"), ("guidance-map.html", "The guidance map")))

# ---- Guidance map (reference) ----
gmap_rows = [
    ("Keeping Children Safe in Education 2026", "Statutory safeguarding baseline from 1 September 2026; addresses AI within its four areas of online risk.", "Safeguarding, pupil use, filtering &amp; monitoring, breaches"),
    ("UK GDPR &amp; Data Protection Act 2018 — as amended by the Data (Use and Access) Act 2025", "The core data protection law: lawful basis, roles, transfers, retention, automated decision-making, breach reporting.", "Data protection, impact assessment, acceptable use"),
    ("ICO guidance on AI &amp; the AI and data protection risk toolkit", "How the regulator expects AI risk to data to be assessed and mitigated.", "Data protection, impact assessment"),
    ("ICO Children’s Code", "Applies wherever children’s data is processed: best interests first, high-privacy defaults, profiling off by default.", "Pupil use, data protection"),
    ("Equality Act 2010 &amp; the public sector equality duty", "Applies to AI-assisted activity as to everything else; bias and discrimination duties.", "Accuracy &amp; oversight, acceptable use"),
    ("DfE position on generative AI &amp; the DfE generative AI product safety standards (January 2026)", "The Department’s expectations for safe AI products in education, including on training on personal data.", "The approval gate, impact assessment, product safety"),
    ("JCQ guidance on AI use in assessments", "Where qualifications are involved: malpractice, disclosure, and not relying on AI as sole marker.", "Acceptable use, accuracy &amp; oversight"),
    ("DfE filtering &amp; monitoring, cyber security, and digital &amp; governance standards", "The technical and governance standards that make the approval gate enforceable and assured.", "Filtering &amp; monitoring, roles &amp; oversight"),
    ("Online Safety Act 2023 &amp; Ofcom Protection of Children code", "Illegal and harmful content duties, including AI-generated sexual imagery of children.", "Safeguarding &amp; Prevent"),
    ("Prevent duty guidance (2023) &amp; Working Together to Safeguard Children 2026", "Counter-radicalisation duty and multi-agency safeguarding action.", "Safeguarding &amp; Prevent, breaches"),
    ("Academy Trust Handbook / scheme for financing schools / Schools Financial Value Standard", "The financial governance framework that applies to procurement and oversight.", "Roles &amp; oversight, the approval gate"),
]
rows_html = "\n".join(
    f"<tr><th scope='row'>{n}</th><td>{w}</td><td>{s}</td></tr>" for n, w, s in gmap_rows)
PAGES.append(("guidance-map.html", "The guidance map", "Reference",
  "The guidance map",
  "Every framework the policy sits within, what each one requires, and the pages on this site that speak to it.",
  f"""
  <p class="lead">The <em>Use of AI Policy</em> does not sit on its own — it sits within a stack of law, statutory guidance and sector standards. This is the whole map in one place.</p>
  <div class="data-table-wrap">
  <table class="data">
    <caption>Law, statutory guidance and standards referenced by the policy</caption>
    <thead><tr><th scope="col">Framework</th><th scope="col">What it requires</th><th scope="col">Where it lands on this site</th></tr></thead>
    <tbody>
    {rows_html}
    </tbody>
  </table>
  </div>
  <p class="chart-note">Frameworks and their commencement dates change. Confirm the current version of each before you rely on it, and take your own professional or legal advice where there is any doubt. This map is a signpost, not a statement of the law.</p>
  """,
  None, None, ("pupil-use.html", "Pupil use"), ("dpia-tool.html", "DPIA screening tool")))

# ---- Build the standard topic pages ----
for slug, navt, kicker, h1, sub, body, _gi, _extra, prev, nxt in PAGES:
    inner = banner(kicker, h1, sub) + body + pagenav(prev, nxt)
    write(slug, f"{h1.replace('&amp;','&')} — {BRAND_TITLE}",
          sub.replace('“','').replace('”','')[:180], inner, ORG_LD)

print("All topic pages written.")
