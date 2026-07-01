# Embedding AI in Education — Woodland Academy Trust

A multi-page static website presenting *Embedding AI in Education: A Strategic Review of Practice
at Woodland Academy Trust* (Woodland Academy Trust with Mark Anderson / ICT Evangelist and Sync,
September 2025).

## Overview

The site disseminates the findings of the Trust's AI-supported lesson-planning initiative across
its five primary schools. It is built as plain, self-contained static HTML files sharing a single
stylesheet, with no external API calls, so it can be opened directly from disk or served by any
static host.

## Structure

| File | Content |
| --- | --- |
| `index.html` | Home — title, authors, date, report summary, headline findings, navigation |
| `teaching-learning.html` | Teaching &amp; Learning Transformation |
| `staff-development.html` | Staff Development &amp; Professional Learning |
| `inclusive-practice.html` | Inclusive Practice &amp; Accessibility |
| `workload-wellbeing.html` | Workload, Efficiency &amp; Wellbeing |
| `role-of-ai.html` | The Role of AI (input vs output paradigms) |
| `ethics-safeguarding.html` | Ethical, Safeguarding &amp; Data Considerations |
| `conditions-success.html` | Conditions for Success |
| `reflections-recommendations.html` | Reflections &amp; Recommendations |
| `data-findings.html` | Data &amp; Findings — headline metrics visualised as charts |
| `css/styles.css` | Shared stylesheet |
| `privacy.html` | Privacy notice (no cookies / tracking / data collection) |
| `js/nav.js` | Header waffle-menu toggle + autohide-on-scroll |
| `js/a11y.js` | Reading-controls widget (text size, contrast, spacing, listen-aloud) |
| `js/charts.js` | Chart definitions with all data values hard-coded |
| `js/chart.umd.min.js` | Vendored [Chart.js](https://www.chartjs.org/) v4.4.1 (UMD, MIT licence) |
| `assets/ict-evangelist-logo*.png` | ICT Evangelist logo (colour + white-knockout) |
| `assets/fonts/poppins-*.woff2` | Vendored [Poppins](https://fonts.google.com/specimen/Poppins) — body text (SIL OFL) |
| `assets/fonts/exo2-*.woff2` | Vendored [Exo 2](https://fonts.google.com/specimen/Exo+2) — H1/H2 headings (SIL OFL) |
| `js/chartjs-plugin-datalabels.min.js` | Vendored [chartjs-plugin-datalabels](https://chartjs-plugin-datalabels.netlify.app/) (MIT) |

## Branding

The visual design follows the **ICT Evangelist** brand: a clean white base with near-black text, the
teal-to-green chevron gradient as the signature accent, charcoal dark surfaces and buttons. Typography pairs
**Poppins** for body text with **Exo 2** for H1/H2 headings (both vendored locally). The ICT Evangelist
logo appears in the header and footer. All fonts and images are local, so the site still makes no
external requests.

## Charts

The Data &amp; Findings page renders charts with [Chart.js](https://www.chartjs.org/) v4.4.1. The
library is vendored locally (`js/chart.umd.min.js`) so the site is fully self-contained and makes no
external requests. Every data value is hard-coded into `js/charts.js` and mirrored in an accessible
data table on the page, so the figures remain available even if scripting is disabled.

## Accessibility

Designed against WCAG 2.1 AA and audited with axe-core (no violations). Features include a skip link,
semantic landmarks and headings, keyboard-operable menu with focus management, chart `aria-label`s plus
a full data-table fallback, honouring of the OS reduced-motion and increased-contrast settings, and a
**Reading controls** widget offering adjustable text size, a high-contrast theme, extra spacing, and a
"listen to this page" option (using the browser's built-in speech synthesiser — no external service).
Preferences are stored locally on the visitor's device.

## Viewing

Open `index.html` in any modern browser, or serve the folder with any static file server, e.g.:

```bash
python3 -m http.server
```

## Credits

Produced by **Woodland Academy Trust** with **Mark Anderson (ICT Evangelist)** and **Sync**.
September 2025.
