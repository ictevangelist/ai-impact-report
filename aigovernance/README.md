# AI Governance in Education — `aigovernance.ictevangelist.com`

A self-contained static mini-site that acts as a plain-language companion to the
**Use of Artificial Intelligence (AI) Policy** template (Mark Anderson / ICT Evangelist),
written for adoption from **September 2026**. Each page follows a *what it is / why it
matters / what guidance it speaks to* structure and maps to a section of the policy template.

Built on the proven Woodland Academy review kit: vendored fonts (Poppins + Exo 2), the
ICT Evangelist chevron brand, a WCAG-minded reading-controls widget, and no external requests.

## Two take-away tools

- **The policy template** (`downloads/Use-of-AI-Policy-Template.docx`) — a completable Word template.
- **The DPIA screening tool** (`downloads/AI-DPIA-Screening-Tool.html`) — a browser-only screening
  tool, delivered as the reward for a short sign-up (Google Form) on `dpia-tool.html`.

## Structure

| File | Content |
| --- | --- |
| `index.html` | Home — the pitch, the non-negotiables, both tools, FAQ |
| `landscape.html` | Why govern AI + scope + the guidance stack (policy §1–2) |
| `roles.html` | Roles, responsibilities & oversight (§3) |
| `approved-tools.html` | Approved tools & how tools are approved (§4, 4a) |
| `acceptable-use.html` | What staff may / must not do (§5–6) |
| `data-protection.html` | Data protection & information security (§7) |
| `accuracy-oversight.html` | Accuracy, bias & human oversight (§8) |
| `safeguarding.html` | Safeguarding, online safety & Prevent (§9) |
| `impact-assessment.html` | Impact assessment & product safety (§10) |
| `training.html` | Training & awareness (§11) |
| `filtering-monitoring.html` | Filtering, monitoring & assurance (§12) |
| `breaches.html` | Breaches & serious incidents (§13) |
| `pupil-use.html` | Pupil use (optional module) |
| `guidance-map.html` | Every framework, what it requires, where it lands |
| `dpia-tool.html` | DPIA screening tool — sign-up (Google Form) → download |
| `policy-template.html` | Download the policy template |
| `privacy.html` | Privacy notice (no cookies/tracking; Google Form sign-up covered) |

## Editing

Pages are generated from `build.py` (engine) + `content.py` / `content2.py` (content).
Edit the content modules, then regenerate:

```bash
python3 content.py && python3 content2.py
```

Static HTML is committed so the site needs no build step to host.

## To go live

1. Create the empty `ictevangelist/aigovernance` repo on GitHub and push these files to its root.
2. Repo **Settings → Pages** → deploy from the default branch.
3. The `CNAME` file already contains `aigovernance.ictevangelist.com`; add a DNS `CNAME`
   record for `aigovernance` → `ictevangelist.github.io` at the domain host.
4. On the Google Form, set the **confirmation message** to include the download link
   `https://aigovernance.ictevangelist.com/downloads/AI-DPIA-Screening-Tool.html`, and
   paste the form's embed `<iframe>` into the marked placeholder in `dpia-tool.html`.

## Credit & licence

Produced by **Mark Anderson (ICT Evangelist)**. The policy template and DPIA tool are shared
under **Creative Commons BY-NC-SA 4.0**.
