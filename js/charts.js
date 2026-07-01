/* =====================================================================
   Data & Findings charts — Woodland Academy Trust AI Review
   All data values are hard-coded from the report. No external API calls;
   the only external dependency is the Chart.js library loaded via CDN.
   ===================================================================== */
(function () {
  if (typeof Chart === 'undefined') {
    // Chart.js unavailable (e.g. offline). The data table on the page
    // provides the same figures, so we fail gracefully.
    console.warn('Chart.js not loaded — see the data table for all figures.');
    return;
  }

  var BASELINE = '#8a99a3';   // slate — baseline (before AI)
  var FOLLOWUP = '#0ea3ab';   // brand teal — follow-up (after AI)
  var ACCENT   = '#45b84a';   // brand green — single-series inclusion chart
  var GRID     = 'rgba(21,32,43,.08)';
  var TICK     = '#45525d';

  // Shared defaults
  Chart.defaults.font.family = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif";
  Chart.defaults.font.size = 13;
  Chart.defaults.color = TICK;

  function legend() {
    return { position: 'top', labels: { boxWidth: 14, padding: 16, font: { size: 13 } } };
  }

  // ---- Chart 1: Weekly planning time (hours) ----
  new Chart(document.getElementById('chartPlanningTime'), {
    type: 'bar',
    data: {
      labels: ['Average', 'Median', 'Maximum'],
      datasets: [
        { label: 'Baseline (Nov 2024)', data: [10, 7, 24], backgroundColor: BASELINE, borderRadius: 5 },
        { label: 'Follow-up (Feb 2025)', data: [4.75, 4, 10], backgroundColor: FOLLOWUP, borderRadius: 5 }
      ]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: {
        legend: legend(),
        tooltip: { callbacks: { label: function (c) { return c.dataset.label + ': ' + c.parsed.y + ' hrs'; } } }
      },
      scales: {
        y: { beginAtZero: true, title: { display: true, text: 'Hours per week' }, grid: { color: GRID } },
        x: { grid: { display: false } }
      }
    }
  });

  // ---- Chart 2: Planning efficiency, confidence, class needs, adaptability (%) ----
  new Chart(document.getElementById('chartConfidence'), {
    type: 'bar',
    data: {
      labels: [['Rated efficient /', 'very efficient'], ['Teacher planning', 'confidence'], ['Planning meets', 'class needs'], ['SEND / EAL', 'adaptability']],
      datasets: [
        { label: 'Baseline', data: [0, 50, 37.5, 50], backgroundColor: BASELINE, borderRadius: 5 },
        { label: 'Follow-up', data: [88, 100, 100, 88], backgroundColor: FOLLOWUP, borderRadius: 5 }
      ]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: {
        legend: legend(),
        tooltip: { callbacks: { label: function (c) { return c.dataset.label + ': ' + c.parsed.y + '%'; } } }
      },
      scales: {
        y: { beginAtZero: true, max: 100, title: { display: true, text: '% of staff' },
             ticks: { callback: function (v) { return v + '%'; } }, grid: { color: GRID } },
        x: { grid: { display: false }, ticks: { maxRotation: 0, autoSkip: false } }
      }
    }
  });

  // ---- Chart 3: Workload impact & overwhelm (%) ----
  new Chart(document.getElementById('chartWellbeing'), {
    type: 'bar',
    data: {
      labels: [['Planning has "high impact"', 'on workload'], ['Often / always overwhelmed', 'by planning time']],
      datasets: [
        { label: 'Baseline', data: [75, 75], backgroundColor: BASELINE, borderRadius: 5 },
        { label: 'Follow-up', data: [0, 0], backgroundColor: FOLLOWUP, borderRadius: 5 }
      ]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: {
        legend: legend(),
        tooltip: { callbacks: { label: function (c) { return c.dataset.label + ': ' + c.parsed.y + '%'; } } }
      },
      scales: {
        y: { beginAtZero: true, max: 100, title: { display: true, text: '% of staff' },
             ticks: { callback: function (v) { return v + '%'; } }, grid: { color: GRID } },
        x: { grid: { display: false }, ticks: { maxRotation: 0, autoSkip: false } }
      }
    }
  });

  // ---- Chart 4: Inclusion outcomes (%) — horizontal ----
  new Chart(document.getElementById('chartInclusion'), {
    type: 'bar',
    data: {
      labels: [
        'Increased pupil engagement',
        'Improved learner independence',
        'KS2 pupils preferred AI-supported lessons',
        'More equitable access, without lowering the bar',
        'Improved speed & quality of differentiated materials'
      ],
      datasets: [
        { label: 'Reported by staff / pupils', data: [82, 78, 91, 89, 95],
          backgroundColor: [ACCENT, ACCENT, FOLLOWUP, ACCENT, FOLLOWUP], borderRadius: 5 }
      ]
    },
    options: {
      indexAxis: 'y',
      responsive: true, maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: { callbacks: { label: function (c) { return c.parsed.x + '%'; } } }
      },
      scales: {
        x: { beginAtZero: true, max: 100, title: { display: true, text: '% reporting' },
             ticks: { callback: function (v) { return v + '%'; } }, grid: { color: GRID } },
        y: { grid: { display: false } }
      }
    }
  });
})();
