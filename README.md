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
| `js/nav.js` | Mobile navigation toggle |
| `js/charts.js` | Chart definitions with all data values hard-coded |
| `js/chart.umd.min.js` | Vendored [Chart.js](https://www.chartjs.org/) v4.4.1 (UMD, MIT licence) |
| `assets/ict-evangelist-logo*.png` | ICT Evangelist logo (colour + white-knockout) |
| `assets/fonts/jost-*.woff2` | Vendored [Jost](https://github.com/indestructible-type/Jost) font (SIL OFL) |

## Branding

The visual design follows the **ICT Evangelist** brand: a clean white base with near-black text, the
teal-to-green chevron gradient as the signature accent, charcoal dark surfaces and buttons, and the
**Jost** geometric sans-serif for headings (vendored locally). The ICT Evangelist logo appears in the
header and footer. All fonts and images are local, so the site still makes no external requests.

## Charts

The Data &amp; Findings page renders charts with [Chart.js](https://www.chartjs.org/) v4.4.1. The
library is vendored locally (`js/chart.umd.min.js`) so the site is fully self-contained and makes no
external requests. Every data value is hard-coded into `js/charts.js` and mirrored in an accessible
data table on the page, so the figures remain available even if scripting is disabled.

## Viewing

Open `index.html` in any modern browser, or serve the folder with any static file server, e.g.:

```bash
python3 -m http.server
```

## Credits

Produced by **Woodland Academy Trust** with **Mark Anderson (ICT Evangelist)** and **Sync**.
September 2025.
